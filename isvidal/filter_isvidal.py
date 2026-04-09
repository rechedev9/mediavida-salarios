"""
Phase 2 — Filter, enrich, and structure isvidal's posts.

Inputs:  isvidal/posts_all.json
Outputs: isvidal/isvidal_posts.parquet
         isvidal/isvidal_context.parquet
         isvidal/isvidal_stats.txt
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

import polars as pl

ROOT = Path(__file__).parent
POSTS_JSON = ROOT / "posts_all.json"
OUT_POSTS = ROOT / "isvidal_posts.parquet"
OUT_CONTEXT = ROOT / "isvidal_context.parquet"
OUT_STATS = ROOT / "isvidal_stats.txt"

AUTHOR = "isvidal"


def load_posts():
    with open(POSTS_JSON, encoding="utf-8") as f:
        return json.load(f)


def word_count(text: str) -> int:
    return len(text.split()) if text else 0


def build_isvidal_posts(posts: list[dict], num_to_author: dict) -> list[dict]:
    rows = []
    for p in posts:
        if p["autor"] != AUTHOR:
            continue

        # Authors that isvidal quoted in this post
        replied_to = []
        for q in p["quotes"]:
            author = num_to_author.get(q["ref_num"])
            if author and author not in replied_to:
                replied_to.append(author)

        wc = word_count(p["texto"])
        rows.append(
            {
                "post_num": p["post_num"],
                "pagina": p["pagina"],
                "timestamp": p["timestamp"],
                "fecha_iso": p["fecha_iso"],
                "year": datetime.fromisoformat(p["fecha_iso"]).year,
                "texto": p["texto"],
                "quotes": p["quotes"],
                "code_blocks": p["code_blocks"],
                "word_count": wc,
                "has_code": len(p["code_blocks"]) > 0,
                "replied_to_autores": replied_to,
            }
        )

    # Sort ascending by timestamp
    rows.sort(key=lambda r: r["timestamp"])
    return rows


def build_context_posts(posts: list[dict], isvidal_post_nums: set) -> list[dict]:
    """Non-isvidal posts that quote at least one isvidal post."""
    rows = []
    for p in posts:
        if p["autor"] == AUTHOR:
            continue
        quoting_nums = [
            q["ref_num"]
            for q in p["quotes"]
            if q["ref_num"] in isvidal_post_nums
        ]
        if not quoting_nums:
            continue
        wc = word_count(p["texto"])
        rows.append(
            {
                "post_num": p["post_num"],
                "pagina": p["pagina"],
                "autor": p["autor"],
                "timestamp": p["timestamp"],
                "fecha_iso": p["fecha_iso"],
                "year": datetime.fromisoformat(p["fecha_iso"]).year,
                "texto": p["texto"],
                "quotes": p["quotes"],
                "code_blocks": p["code_blocks"],
                "word_count": wc,
                "has_code": len(p["code_blocks"]) > 0,
                "replied_to_autores": [],  # not used here
                "quoting_isvidal_post_nums": quoting_nums,
            }
        )
    rows.sort(key=lambda r: r["timestamp"])
    return rows


def to_polars_posts(rows: list[dict]) -> pl.DataFrame:
    return pl.DataFrame(
        {
            "post_num": [r["post_num"] for r in rows],
            "pagina": [r["pagina"] for r in rows],
            "timestamp": [r["timestamp"] for r in rows],
            "fecha_iso": [r["fecha_iso"] for r in rows],
            "year": [r["year"] for r in rows],
            "texto": [r["texto"] for r in rows],
            "quotes": [json.dumps(r["quotes"], ensure_ascii=False) for r in rows],
            "code_blocks": [
                json.dumps(r["code_blocks"], ensure_ascii=False) for r in rows
            ],
            "word_count": [r["word_count"] for r in rows],
            "has_code": [r["has_code"] for r in rows],
            "replied_to_autores": [
                json.dumps(r["replied_to_autores"], ensure_ascii=False) for r in rows
            ],
        }
    )


def to_polars_context(rows: list[dict]) -> pl.DataFrame:
    return pl.DataFrame(
        {
            "post_num": [r["post_num"] for r in rows],
            "pagina": [r["pagina"] for r in rows],
            "autor": [r["autor"] for r in rows],
            "timestamp": [r["timestamp"] for r in rows],
            "fecha_iso": [r["fecha_iso"] for r in rows],
            "year": [r["year"] for r in rows],
            "texto": [r["texto"] for r in rows],
            "quotes": [json.dumps(r["quotes"], ensure_ascii=False) for r in rows],
            "code_blocks": [
                json.dumps(r["code_blocks"], ensure_ascii=False) for r in rows
            ],
            "word_count": [r["word_count"] for r in rows],
            "has_code": [r["has_code"] for r in rows],
            "quoting_isvidal_post_nums": [
                json.dumps(r["quoting_isvidal_post_nums"]) for r in rows
            ],
        }
    )


def build_stats(posts: list[dict], isvidal_rows: list[dict], context_rows: list[dict]) -> str:
    num_to_author = {p["post_num"]: p["autor"] for p in posts}

    years = [r["year"] for r in isvidal_rows]
    posts_by_year = Counter(years)
    wcs = [r["word_count"] for r in isvidal_rows]
    wcs_sorted = sorted(wcs)
    n = len(wcs_sorted)
    median_wc = wcs_sorted[n // 2] if n % 2 == 1 else (wcs_sorted[n // 2 - 1] + wcs_sorted[n // 2]) // 2
    code_pct = 100 * sum(1 for r in isvidal_rows if r["has_code"]) / len(isvidal_rows)

    # Top 10 authors isvidal quoted
    quoted_authors: list[str] = []
    for r in isvidal_rows:
        for q in r["quotes"]:
            a = num_to_author.get(q["ref_num"])
            if a:
                quoted_authors.append(a)
    top_quoted = Counter(quoted_authors).most_common(10)

    # Top 10 authors who quoted isvidal
    quoting_authors = [r["autor"] for r in context_rows]
    top_quoting = Counter(quoting_authors).most_common(10)

    lines = [
        "=== isvidal stats ===",
        f"Total posts:        {len(isvidal_rows)}",
        f"Years active:       {min(years)} – {max(years)}",
        "",
        "Posts per year:",
    ]
    for yr in sorted(posts_by_year):
        lines.append(f"  {yr}: {posts_by_year[yr]}")
    lines += [
        "",
        f"Median word count:  {median_wc}",
        f"Posts with code:    {code_pct:.1f}%",
        "",
        "Top 10 authors isvidal quoted:",
    ]
    for author, count in top_quoted:
        lines.append(f"  {count:3d}  {author}")
    lines += ["", "Top 10 authors who quoted isvidal:"]
    for author, count in top_quoting:
        lines.append(f"  {count:3d}  {author}")

    return "\n".join(lines) + "\n"


def main():
    print("Loading posts_all.json …")
    posts = load_posts()
    print(f"  {len(posts)} posts loaded")

    num_to_author = {p["post_num"]: p["autor"] for p in posts}

    print("Filtering isvidal posts …")
    isvidal_rows = build_isvidal_posts(posts, num_to_author)
    print(f"  {len(isvidal_rows)} isvidal posts")

    if len(isvidal_rows) == 0:
        print("ERROR: zero isvidal posts found — aborting", file=sys.stderr)
        sys.exit(1)

    isvidal_post_nums = {r["post_num"] for r in isvidal_rows}

    print("Building context posts (non-isvidal quoting isvidal) …")
    context_rows = build_context_posts(posts, isvidal_post_nums)
    print(f"  {len(context_rows)} context posts")

    print("Writing isvidal_posts.parquet …")
    df_posts = to_polars_posts(isvidal_rows)
    df_posts.write_parquet(OUT_POSTS)

    print("Writing isvidal_context.parquet …")
    df_ctx = to_polars_context(context_rows)
    df_ctx.write_parquet(OUT_CONTEXT)

    print("Writing isvidal_stats.txt …")
    stats = build_stats(posts, isvidal_rows, context_rows)
    OUT_STATS.write_text(stats, encoding="utf-8")

    print()
    print(stats)

    # Verify: no null timestamps in isvidal posts
    null_ts = [r for r in isvidal_rows if r["timestamp"] is None]
    assert len(null_ts) == 0, f"{len(null_ts)} null timestamps — unexpected"

    # Verify: parquet row count matches
    assert df_posts.height == len(isvidal_rows), "Parquet row count mismatch"

    print("All checks passed.")


if __name__ == "__main__":
    main()
