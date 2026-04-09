#!/usr/bin/env python3
"""
Phase 3 — Idea-evolution analysis for isvidal.

Outputs (all to isvidal/):
  isvidal_term_matrix.parquet       — 3.1 term × year raw+weighted counts
  isvidal_opinion_excerpts.parquet  — 3.2 per-term sentence excerpts
  isvidal_code_features.parquet     — 3.3 per-code-block feature flags
  isvidal_top_posts.parquet         — 3.4 top 30 posts (last 30% timeline)
  isvidal_stack_summary.parquet     — 3.5 recency-weighted per-term totals
  analysis_report.md                — 3.6 human-readable summary
"""
import re
import json
from pathlib import Path

import polars as pl

OUT = Path(__file__).parent

# ── Term dictionary ────────────────────────────────────────────────────────────
TERMS: dict[str, list[str]] = {
    "hooks": [
        "useEffect", "useState", "useMemo", "useCallback", "useRef",
        "useContext", "useReducer", "useTransition", "useDeferredValue",
        "Suspense", "ErrorBoundary",
    ],
    "state_data": [
        "Redux", "Zustand", "Jotai", "Recoil", "MobX",
        "React Query", "SWR", "TanStack", "Context API",
    ],
    "meta_frameworks": [
        "Next.js", "Remix", "Gatsby", "Astro", "RSC",
        "App Router", "Pages Router", "server components", "server actions",
    ],
    "typescript": [
        "strict", "generics", "zod", "io-ts", "any", "unknown",
        "type", "interface", "satisfies", "as const",
    ],
    "tooling": [
        "Webpack", "Vite", "Turbopack", "Rollup", "esbuild",
        "Babel", "SWC", "pnpm", "monorepo", "turborepo",
    ],
    "testing": [
        "Jest", "Vitest", "RTL", "Testing Library",
        "Cypress", "Playwright", "MSW",
    ],
    "patterns": [
        "composition", "hooks pattern", "render props", "HOC",
        "compound component", "colocation", "DX", "DRY", "YAGNI", "abstraction",
    ],
}


def _compile(term: str) -> re.Pattern:
    escaped = re.escape(term)
    if re.fullmatch(r"[A-Za-z0-9_]+", term):
        return re.compile(r"\b" + escaped + r"\b", re.IGNORECASE)
    return re.compile(escaped, re.IGNORECASE)


COMPILED: dict[str, re.Pattern] = {
    term: _compile(term)
    for terms in TERMS.values()
    for term in terms
}
TERM_TO_TOPIC: dict[str, str] = {
    term: topic
    for topic, terms in TERMS.items()
    for term in terms
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_posts() -> pl.DataFrame:
    return pl.read_parquet(OUT / "isvidal_posts.parquet").sort("timestamp")


def recency_weights(n: int) -> list[float]:
    """Linear weights: 1.0 (oldest post) → 2.0 (newest post)."""
    if n == 1:
        return [2.0]
    return [1.0 + i / (n - 1) for i in range(n)]


def post_searchable_text(row: dict) -> str:
    """texto + all code blocks concatenated for term scanning."""
    parts = [row["texto"] or ""]
    try:
        blocks = json.loads(row["code_blocks"] or "[]")
        parts.extend(b for b in blocks if b)
    except (json.JSONDecodeError, TypeError):
        pass
    return " ".join(parts)


def split_sentences(text: str) -> list[str]:
    """Naive sentence splitter for Spanish/English forum text."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


# ── 3.1  Term matrix ──────────────────────────────────────────────────────────

def build_term_matrix(df: pl.DataFrame, weights: list[float]) -> pl.DataFrame:
    rows = []
    for row_dict, w in zip(df.iter_rows(named=True), weights):
        text = post_searchable_text(row_dict)
        year = row_dict["year"]
        for term, pat in COMPILED.items():
            count = len(pat.findall(text))
            if count > 0:
                rows.append({
                    "year": year,
                    "term": term,
                    "topic": TERM_TO_TOPIC[term],
                    "raw_count": count,
                    "weighted_count": count * w,
                })

    if not rows:
        return pl.DataFrame(schema={
            "year": pl.Int64, "term": pl.String, "topic": pl.String,
            "raw_count": pl.Int64, "weighted_count": pl.Float64,
        })

    return (
        pl.DataFrame(rows)
        .group_by(["year", "term", "topic"])
        .agg([
            pl.sum("raw_count"),
            pl.sum("weighted_count"),
        ])
        .sort(["term", "year"])
    )


# ── 3.2  Opinion excerpts ─────────────────────────────────────────────────────

def build_opinion_excerpts(df: pl.DataFrame, weights: list[float]) -> pl.DataFrame:
    rows = []
    for row_dict, w in zip(df.iter_rows(named=True), weights):
        text = row_dict["texto"] or ""
        sentences = split_sentences(text)
        year = row_dict["year"]
        post_num = row_dict["post_num"]
        for term, pat in COMPILED.items():
            for i, sent in enumerate(sentences):
                if pat.search(sent):
                    start = max(0, i - 1)
                    end = min(len(sentences), i + 2)
                    excerpt = " ".join(sentences[start:end])
                    rows.append({
                        "term": term,
                        "year": year,
                        "post_num": post_num,
                        "excerpt": excerpt[:500],
                        "weighted_year": w,
                    })

    if not rows:
        return pl.DataFrame(schema={
            "term": pl.String, "year": pl.Int64, "post_num": pl.Int64,
            "excerpt": pl.String, "weighted_year": pl.Float64,
        })
    return pl.DataFrame(rows)


# ── 3.3  Code-block features ──────────────────────────────────────────────────

_HOOK_PAT = re.compile(
    r"\b(use(?:Effect|State|Memo|Callback|Ref|Context|Reducer|Transition|DeferredValue))\b"
)
_JSX_PAT = re.compile(r"<[A-Z][A-Za-z0-9]*[\s/>]|</[A-Z]")
_ASYNC_PAT = re.compile(r"\basync\b|\bawait\b")
_GENERIC_PAT = re.compile(r"<[A-Za-z][A-Za-z0-9_]*>")
_IMPORT_PAT = re.compile(r"""from\s+['"]([^'"]+)['"]""")


def _detect_lang(block: str) -> str:
    first_line = block.split("\n")[0].strip().lower()
    for lang in ("tsx", "ts", "jsx", "js"):
        if lang in first_line:
            return lang
    has_jsx = bool(_JSX_PAT.search(block))
    has_ts = bool(re.search(r":\s*[A-Z]|\binterface\b|<[A-Za-z][A-Za-z0-9_]*>", block))
    if has_jsx and has_ts:
        return "tsx"
    if has_jsx:
        return "jsx"
    if has_ts:
        return "ts"
    return "js"


def build_code_features(df: pl.DataFrame) -> pl.DataFrame:
    rows = []
    for row_dict in df.iter_rows(named=True):
        try:
            blocks = json.loads(row_dict["code_blocks"] or "[]")
        except (json.JSONDecodeError, TypeError):
            blocks = []
        for block in blocks:
            if not block or not block.strip():
                continue
            hooks = list(dict.fromkeys(_HOOK_PAT.findall(block)))
            imports = list(dict.fromkeys(_IMPORT_PAT.findall(block)))
            rows.append({
                "post_num": row_dict["post_num"],
                "year": row_dict["year"],
                "lang_hint": _detect_lang(block),
                "has_hooks": bool(hooks),
                "hook_names": json.dumps(hooks),
                "has_jsx": bool(_JSX_PAT.search(block)),
                "has_async": bool(_ASYNC_PAT.search(block)),
                "has_generics": bool(_GENERIC_PAT.search(block)),
                "imports": json.dumps(imports),
            })

    if not rows:
        return pl.DataFrame(schema={
            "post_num": pl.Int64, "year": pl.Int64, "lang_hint": pl.String,
            "has_hooks": pl.Boolean, "hook_names": pl.String,
            "has_jsx": pl.Boolean, "has_async": pl.Boolean,
            "has_generics": pl.Boolean, "imports": pl.String,
        })
    return pl.DataFrame(rows)


# ── 3.4  Top posts ────────────────────────────────────────────────────────────

def build_top_posts(df: pl.DataFrame) -> pl.DataFrame:
    n = len(df)
    cutoff_idx = int(n * 0.70)
    recent = df[cutoff_idx:]
    filtered = recent.filter(
        (pl.col("word_count") >= 100) | pl.col("has_code")
    )
    return filtered.sort("word_count", descending=True).head(30)


# ── 3.5  Stack summary ────────────────────────────────────────────────────────

def build_stack_summary(matrix: pl.DataFrame) -> pl.DataFrame:
    if matrix.is_empty():
        return pl.DataFrame(schema={
            "term": pl.String, "topic": pl.String, "weighted_score": pl.Float64,
            "first_year": pl.Int64, "last_year": pl.Int64, "total_mentions": pl.Int64,
        })
    return (
        matrix
        .group_by(["term", "topic"])
        .agg([
            pl.sum("weighted_count").alias("weighted_score"),
            pl.min("year").alias("first_year"),
            pl.max("year").alias("last_year"),
            pl.sum("raw_count").alias("total_mentions"),
        ])
        .sort("weighted_score", descending=True)
    )


# ── 3.6  Human-readable report ────────────────────────────────────────────────

def build_report(
    df: pl.DataFrame,
    matrix: pl.DataFrame,
    summary: pl.DataFrame,
    excerpts: pl.DataFrame,
    top_posts: pl.DataFrame,
) -> str:
    lines: list[str] = []
    lines.append("# isvidal — Idea Evolution Analysis Report\n")

    # Temporal summary
    lines.append("## Temporal Summary\n")
    by_year = (
        df
        .group_by("year")
        .agg([
            pl.len().alias("posts"),
            pl.sum("word_count").alias("words"),
            pl.mean("has_code").cast(pl.Float64).alias("code_ratio"),
        ])
        .sort("year")
    )
    lines.append("| Year | Posts | Words | Code% |")
    lines.append("|------|-------|-------|-------|")
    for row in by_year.iter_rows(named=True):
        lines.append(
            f"| {row['year']} | {row['posts']} | {row['words']} "
            f"| {row['code_ratio'] * 100:.0f}% |"
        )
    lines.append("")

    # Top terms per topic
    lines.append("## Top Terms per Topic (Recency-Weighted)\n")
    if not summary.is_empty():
        for topic in TERMS:
            t = summary.filter(pl.col("topic") == topic).head(5)
            if t.is_empty():
                continue
            lines.append(f"### {topic.replace('_', ' ').title()}\n")
            lines.append("| Term | Weighted Score | Total Mentions | Years |")
            lines.append("|------|----------------|----------------|-------|")
            for row in t.iter_rows(named=True):
                lines.append(
                    f"| {row['term']} | {row['weighted_score']:.1f} "
                    f"| {row['total_mentions']} "
                    f"| {row['first_year']}–{row['last_year']} |"
                )
            lines.append("")

    # Opinion excerpts for top 5 terms
    lines.append("## Opinion Evolution — Top 5 Terms\n")
    if not summary.is_empty() and not excerpts.is_empty():
        top5 = summary.head(5)["term"].to_list()
        for term in top5:
            ex = (
                excerpts
                .filter(pl.col("term") == term)
                .sort("year", descending=True)
            )
            if ex.is_empty():
                continue
            lines.append(f"### `{term}`\n")
            for row in ex.head(5).iter_rows(named=True):
                lines.append(f"**{row['year']} · post #{row['post_num']}**")
                lines.append(f"> {row['excerpt']}\n")

    # Top posts table
    lines.append("## Top Posts (Last 30% of Timeline)\n")
    lines.append("| Year | Post # | Page | Words | Has Code | Preview |")
    lines.append("|------|--------|------|-------|----------|---------|")
    for row in top_posts.iter_rows(named=True):
        preview = (row["texto"] or "")[:100].replace("\n", " ")
        lines.append(
            f"| {row['year']} | #{row['post_num']} | {row['pagina']} "
            f"| {row['word_count']} | {'✓' if row['has_code'] else ''} | {preview}… |"
        )
    lines.append("")

    lines.append(
        "\n---\n"
        "*Dashboard:* `streamlit run isvidal/app.py`  \n"
        "*Data:* `isvidal/isvidal_posts.parquet`  \n"
        "*Thread:* [react-hilo-general](https://www.mediavida.com/foro/dev/"
        "react-hilo-general-libreria-para-atraerlos-atarlos-todos-657749)\n"
    )
    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print("Loading isvidal_posts.parquet …")
    df = load_posts()
    print(f"  {len(df)} posts, years {df['year'].min()}–{df['year'].max()}")

    weights = recency_weights(len(df))
    print(f"  Recency weights: {weights[0]:.4f} (oldest) → {weights[-1]:.4f} (newest)")

    print("\n3.1  Building term matrix …")
    matrix = build_term_matrix(df, weights)
    matrix.write_parquet(OUT / "isvidal_term_matrix.parquet")
    print(f"  {len(matrix)} rows → isvidal_term_matrix.parquet")

    print("\n3.2  Building opinion excerpts …")
    excerpts = build_opinion_excerpts(df, weights)
    excerpts.write_parquet(OUT / "isvidal_opinion_excerpts.parquet")
    print(f"  {len(excerpts)} rows → isvidal_opinion_excerpts.parquet")

    print("\n3.3  Building code-block features …")
    code_features = build_code_features(df)
    code_features.write_parquet(OUT / "isvidal_code_features.parquet")
    print(f"  {len(code_features)} rows → isvidal_code_features.parquet")

    print("\n3.4  Building top posts …")
    top_posts = build_top_posts(df)
    top_posts.write_parquet(OUT / "isvidal_top_posts.parquet")
    print(f"  {len(top_posts)} rows → isvidal_top_posts.parquet")

    print("\n3.5  Building stack summary …")
    summary = build_stack_summary(matrix)
    summary.write_parquet(OUT / "isvidal_stack_summary.parquet")
    print(f"  {len(summary)} rows → isvidal_stack_summary.parquet")

    print("\n3.6  Writing analysis_report.md …")
    report = build_report(df, matrix, summary, excerpts, top_posts)
    (OUT / "analysis_report.md").write_text(report, encoding="utf-8")
    print("  analysis_report.md written")

    # Verification
    print("\n── Verification ──")
    print(
        f"  Term matrix: {len(matrix)} rows, "
        f"{matrix['term'].n_unique() if not matrix.is_empty() else 0} unique terms"
    )
    if not matrix.is_empty():
        print(f"  Total raw hits: {matrix['raw_count'].sum()}")
    print(f"\n  Top 10 terms by weighted score:")
    if not summary.is_empty():
        for row in summary.head(10).iter_rows(named=True):
            print(f"    {row['term']:25s}  {row['weighted_score']:7.1f}  [{row['topic']}]")
    n_posts_with_code = (
        code_features["post_num"].n_unique() if not code_features.is_empty() else 0
    )
    print(
        f"\n  Code features: {len(code_features)} blocks "
        f"from {n_posts_with_code} posts"
    )
    print(f"  Top posts: {len(top_posts)}")
    n_excerpt_terms = excerpts["term"].n_unique() if not excerpts.is_empty() else 0
    print(f"  Excerpts: {len(excerpts)} hits across {n_excerpt_terms} terms")
    print("\nPhase 3 complete.")


if __name__ == "__main__":
    main()
