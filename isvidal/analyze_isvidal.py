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
import sys
from pathlib import Path

import polars as pl

OUT = Path(__file__).parent

# ── Term dictionary ────────────────────────────────────────────────────────────
# Dead terms (0 hits) removed. New topics added after gap analysis on
# isvidal's actual corpus: styling, data_api, platforms, backend, utils.
TERMS: dict[str, list[str]] = {
    "hooks": [
        "useEffect", "useState", "useMemo", "useCallback", "useRef",
        "useContext", "useReducer", "Suspense",
    ],
    "state_data": [
        "Redux", "Zustand", "Recoil", "React Query", "SWR",
        "Nuqs", "Valtio",
    ],
    "meta_frameworks": [
        "Next.js", "Remix", "Gatsby", "Astro",
        "TanStack", "React Router",
    ],
    "typescript": [
        "TypeScript", "strict", "zod", "any", "type",
    ],
    "tooling": [
        "Vite", "monorepo", "Prettier", "ESLint", "Biome",
    ],
    "testing": [
        "Jest", "Testing Library",
    ],
    "patterns": [
        # DX removed: matches "developer experience" concept, not a tool
    ],
    "styling": [
        "Tailwind", "TailwindCSS", "styled-components",
        "CSS Modules", "CSS-in-JS", "shadcn", "shadcdn",
        "Radix", "Chakra", "MUI",
    ],
    "data_api": [
        "axios", "fetch", "tRPC", "GraphQL",
        "REST", "OpenAPI", "Prisma", "Supabase",
    ],
    "platforms": [
        "React Native", "Expo",
        "Vercel", "Netlify", "Cloudflare",
    ],
    "backend": [
        "PHP", "Node.js", "Bun", "Deno",
        "Django", "Laravel", "Express",
    ],
    "utils": [
        "date-fns", "clsx", "Framer Motion",
    ],
}


def _compile(term: str) -> re.Pattern:
    """
    Build a case-insensitive regex that tolerates common forum writing variants:
    - "React Router" matches "React Router" AND "react-router"
    - "Node.js" matches "Node.js" AND "node.js"
    - Single alphanumeric words use word boundaries to prevent partial matches
    """
    # Multi-word terms: allow whitespace OR hyphen as the separator
    if " " in term:
        parts = [re.escape(p) for p in term.split(" ")]
        pattern = r"\b" + r"[\s-]+".join(parts) + r"\b"
        return re.compile(pattern, re.IGNORECASE)
    # Single alphanumeric token: word boundaries on both sides
    if re.fullmatch(r"[A-Za-z0-9_]+", term):
        return re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)
    # Anything else (dotted names, slashes, etc.): literal escape, no boundaries
    return re.compile(re.escape(term), re.IGNORECASE)


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

# Canonicalize variant spellings into a single term to avoid splitting scores.
# The dictionary term still matches via regex (so "TailwindCSS" is detected)
# but gets stored under the canonical name ("Tailwind").
TERM_ALIASES: dict[str, str] = {
    "TailwindCSS": "Tailwind",
    "shadcdn": "shadcn",  # isvidal's consistent typo for shadcn
}


def canonical(term: str) -> str:
    return TERM_ALIASES.get(term, term)


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_posts() -> pl.DataFrame:
    return pl.read_parquet(OUT / "isvidal_posts.parquet").sort("timestamp")


# Exponential decay — half-life 2 years. A 2026 mention is worth 1.0,
# a 2024 mention 0.5, a 2022 mention 0.25, a 2020 mention 0.125.
# Aligned with frontend churn: old tooling is almost certainly outdated.
HALF_LIFE_YEARS = 2.0
# Posts with year >= latest_year - RECENT_LOOKBACK_YEARS count as "recent".
# With value 1, recent = the latest year and the one before it (2 calendar years).
RECENT_LOOKBACK_YEARS = 1


def year_weight(year: int, latest_year: int) -> float:
    return 0.5 ** ((latest_year - year) / HALF_LIFE_YEARS)


def build_year_weights(df: pl.DataFrame) -> list[float]:
    latest = int(df["year"].max())
    return [year_weight(int(y), latest) for y in df["year"].to_list()]


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
                    "term": canonical(term),
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
    """
    Extract sentence-level excerpts mentioning each dictionary term.
    Per (post, term), dedupe by the first 200 chars of the excerpt so that the
    SAME ±1-sentence window is not emitted twice (which happens when a term
    appears multiple times in one sentence). Near-duplicates from overlapping
    windows at adjacent sentences can still slip through — those are rare
    enough in practice that stance aggregation isn't materially affected.
    """
    rows = []
    for row_dict, w in zip(df.iter_rows(named=True), weights):
        text = row_dict["texto"] or ""
        sentences = split_sentences(text)
        year = row_dict["year"]
        post_num = row_dict["post_num"]
        for term, pat in COMPILED.items():
            term_canon = canonical(term)
            seen_excerpts: set[str] = set()
            for i, sent in enumerate(sentences):
                if pat.search(sent):
                    start = max(0, i - 1)
                    end = min(len(sentences), i + 2)
                    excerpt = " ".join(sentences[start:end])[:500]
                    # Dedupe by content prefix (first 200 chars are stable enough)
                    key = excerpt[:200]
                    if key in seen_excerpts:
                        continue
                    seen_excerpts.add(key)
                    rows.append({
                        "term": term_canon,
                        "year": year,
                        "post_num": post_num,
                        "excerpt": excerpt,
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
    """
    Posts técnicos densos del último 30% del timeline.
    Filtro: ≥2 hits del diccionario O has_code. Sort por densidad técnica.
    Excluye el post #1 (índice/glosario del hilo, no opinión).
    """
    n = len(df)
    cutoff_idx = int(n * 0.70)
    recent = df[cutoff_idx:].filter(pl.col("post_num") != 1)

    # Count term hits per post (tech density)
    tech_density = []
    for row in recent.iter_rows(named=True):
        text = post_searchable_text(row)
        hits = sum(1 for pat in COMPILED.values() if pat.search(text))
        tech_density.append(hits)

    recent = recent.with_columns(pl.Series("tech_density", tech_density))
    filtered = recent.filter(
        (pl.col("tech_density") >= 2) | pl.col("has_code")
    )
    # Composite score: term hits are the main signal, code adds 5, words add /20
    return (
        filtered
        .with_columns(
            (
                pl.col("tech_density")
                + pl.col("has_code").cast(pl.Int64) * 5
                + pl.col("word_count") / 20
            ).alias("_score")
        )
        .sort("_score", descending=True)
        .drop("_score")
        .head(30)
    )


# ── 3.5  Stack summary ────────────────────────────────────────────────────────

# ── Stance merge (Phase 5) ────────────────────────────────────────────────────

STANCE_VAL = {"positivo": 1.0, "negativo": -1.0, "neutral": 0.0}
STANCE_CACHE = OUT / "stance_cache.json"


def _cache_key(term: str, post_num: int, excerpt: str) -> str:
    return f"{term}|{post_num}|{excerpt[:150]}"


def _content_key(post_num: int, excerpt: str) -> str:
    """Term-agnostic key so canonicalization doesn't invalidate cached stances."""
    return f"{post_num}|{excerpt[:150]}"


def apply_stance_cache(
    excerpts: pl.DataFrame, latest_year: int
) -> tuple[pl.DataFrame, pl.DataFrame]:
    """
    Attach stance from cache (if present) and compute per-term stance summary.
    Returns (excerpts_with_stance, term_stance_summary).

    Lookup order: full key (term|post_num|excerpt) → content-only fallback
    (post_num|excerpt) → "neutral". The content-only fallback is critical so
    that renaming a term (e.g., TailwindCSS → Tailwind via TERM_ALIASES) does
    not erase its prior classification.
    """
    if not STANCE_CACHE.exists() or excerpts.is_empty():
        stance_vals = ["neutral"] * len(excerpts)
    else:
        try:
            with open(STANCE_CACHE, encoding="utf-8") as f:
                cache = json.load(f)
        except json.JSONDecodeError as e:
            print(
                f"  WARN: {STANCE_CACHE.name} is malformed ({e}); "
                "skipping stance merge, all excerpts default to neutral",
                file=sys.stderr,
            )
            cache = {}

        def lookup(row):
            full = _cache_key(row["term"], row["post_num"], row["excerpt"])
            if full in cache:
                return cache[full]
            return cache.get(_content_key(row["post_num"], row["excerpt"]), "neutral")

        stance_vals = [lookup(r) for r in excerpts.iter_rows(named=True)]

    excerpts = excerpts.with_columns(pl.Series("stance", stance_vals))

    # Recency-weighted stance score per term — pure native Polars expression
    # (avoids per-row Python callbacks).
    year_w_expr = (
        pl.lit(0.5) ** ((pl.lit(latest_year) - pl.col("year")) / HALF_LIFE_YEARS)
    )
    weighted = excerpts.with_columns(
        (pl.col("stance").replace_strict(STANCE_VAL, default=0.0) * year_w_expr)
        .alias("_wstance")
    )

    term_stance = (
        weighted
        .group_by("term")
        .agg([
            pl.col("_wstance").sum().alias("stance_score"),
            pl.col("stance").filter(pl.col("stance") == "positivo").len().alias("positive_excerpts"),
            pl.col("stance").filter(pl.col("stance") == "negativo").len().alias("negative_excerpts"),
            pl.col("stance").filter(pl.col("stance") == "neutral").len().alias("neutral_excerpts"),
        ])
    )

    # Verdict logic — order matters:
    # 1. mixto FIRST: any term with both ≥2 positive and ≥2 negative excerpts is
    #    contested, regardless of which side currently wins by score.
    # 2. desaconseja: strong negative wins (score <= -0.5).
    # 3. recomienda: strong positive wins (score >= +0.5).
    # 4. neutral: insufficient signal.
    term_stance = term_stance.with_columns(
        pl.when((pl.col("positive_excerpts") >= 2) & (pl.col("negative_excerpts") >= 2))
        .then(pl.lit("mixto"))
        .when(pl.col("stance_score") <= -0.5)
        .then(pl.lit("desaconseja"))
        .when(pl.col("stance_score") >= 0.5)
        .then(pl.lit("recomienda"))
        .otherwise(pl.lit("neutral"))
        .alias("verdict")
    )

    return excerpts, term_stance


def build_stack_summary(matrix: pl.DataFrame, latest_year: int) -> pl.DataFrame:
    if matrix.is_empty():
        return pl.DataFrame(schema={
            "term": pl.String, "topic": pl.String, "weighted_score": pl.Float64,
            "first_year": pl.Int64, "last_year": pl.Int64, "total_mentions": pl.Int64,
            "recent_mentions": pl.Int64, "recent_share": pl.Float64,
            "years_since_last": pl.Int64, "trend": pl.String,
        })
    recent_cutoff = latest_year - RECENT_LOOKBACK_YEARS
    base = (
        matrix
        .group_by(["term", "topic"])
        .agg([
            pl.sum("weighted_count").alias("weighted_score"),
            pl.min("year").alias("first_year"),
            pl.max("year").alias("last_year"),
            pl.sum("raw_count").alias("total_mentions"),
        ])
    )
    recent = (
        matrix
        .filter(pl.col("year") >= recent_cutoff)
        .group_by(["term", "topic"])
        .agg(pl.sum("raw_count").alias("recent_mentions"))
    )
    return (
        base
        .join(recent, on=["term", "topic"], how="left")
        .with_columns(pl.col("recent_mentions").fill_null(0))
        .with_columns([
            (pl.col("recent_mentions") / pl.col("total_mentions")).alias("recent_share"),
            (latest_year - pl.col("last_year")).alias("years_since_last"),
        ])
        .with_columns(
            pl.when(pl.col("years_since_last") <= 1).then(pl.lit("activo"))
            .when(pl.col("years_since_last") <= 3).then(pl.lit("declinante"))
            .otherwise(pl.lit("abandonado"))
            .alias("trend")
        )
        .sort("weighted_score", descending=True)
    )


# ── 3.6  Human-readable report ────────────────────────────────────────────────

def build_report(
    df: pl.DataFrame,
    matrix: pl.DataFrame,
    summary: pl.DataFrame,
    excerpts: pl.DataFrame,
    top_posts: pl.DataFrame,
    latest_year: int,
) -> str:
    lines: list[str] = []
    lines.append("# isvidal — Technical Recommendations Report\n")
    lines.append(
        f"Analysis window: **{df['year'].min()}–{latest_year}**. "
        f"Recency weighting: exponential decay, half-life **{HALF_LIFE_YEARS:.0f} years**. "
        f"A mention from {latest_year - 4} is worth "
        f"{year_weight(latest_year - 4, latest_year):.2f} of a {latest_year} mention.\n"
    )

    # Current stack (trend = activo, sorted by weighted_score)
    lines.append("## Current Stack (trend = activo)\n")
    if not summary.is_empty():
        active = (
            summary
            .filter(pl.col("trend") == "activo")
            .sort("weighted_score", descending=True)
            .head(20)
        )
        lines.append("| Term | Topic | Score | Total | Recent | Last |")
        lines.append("|------|-------|-------|-------|--------|------|")
        for row in active.iter_rows(named=True):
            lines.append(
                f"| {row['term']} | {row['topic']} "
                f"| {row['weighted_score']:.2f} | {row['total_mentions']} "
                f"| {row['recent_mentions']} | {row['last_year']} |"
            )
        lines.append("")

    # Top terms per topic
    lines.append("## Top Terms per Topic\n")
    if not summary.is_empty():
        for topic in TERMS:
            t = summary.filter(pl.col("topic") == topic).head(5)
            if t.is_empty():
                continue
            lines.append(f"### {topic.replace('_', ' ').title()}\n")
            lines.append("| Term | Score | Trend | Years |")
            lines.append("|------|-------|-------|-------|")
            for row in t.iter_rows(named=True):
                lines.append(
                    f"| {row['term']} | {row['weighted_score']:.2f} "
                    f"| {row['trend']} "
                    f"| {row['first_year']}–{row['last_year']} |"
                )
            lines.append("")

    # Abandoned terms
    lines.append("## Abandoned Terms (no mention in last 4+ years)\n")
    if not summary.is_empty():
        abandoned = (
            summary
            .filter(pl.col("trend") == "abandonado")
            .sort("last_year", descending=True)
        )
        if not abandoned.is_empty():
            lines.append("| Term | Topic | Last Year | Total Mentions |")
            lines.append("|------|-------|-----------|----------------|")
            for row in abandoned.iter_rows(named=True):
                lines.append(
                    f"| {row['term']} | {row['topic']} "
                    f"| {row['last_year']} | {row['total_mentions']} |"
                )
            lines.append("")

    # Latest opinion per top-5 active term
    lines.append("## Latest Opinion — Top 5 Active Terms\n")
    if not summary.is_empty() and not excerpts.is_empty():
        top5 = (
            summary
            .filter(pl.col("trend") == "activo")
            .head(5)["term"]
            .to_list()
        )
        for term in top5:
            latest = (
                excerpts
                .filter(pl.col("term") == term)
                .sort("year", descending=True)
                .head(1)
            )
            if latest.is_empty():
                continue
            row = latest.row(0, named=True)
            lines.append(f"### `{term}`\n")
            lines.append(f"**{row['year']} · post #{row['post_num']}**")
            lines.append(f"> {row['excerpt']}\n")

    # Top posts table (still useful — technical content density)
    lines.append("## Dense Technical Posts (Last 30% of Timeline)\n")
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
    if df.is_empty():
        print("ERROR: isvidal_posts.parquet is empty — run filter_isvidal.py first", file=sys.stderr)
        sys.exit(1)
    latest_year = int(df["year"].max())
    print(f"  {len(df)} posts, years {df['year'].min()}–{latest_year}")

    weights = build_year_weights(df)
    print(
        f"  Year weights (half-life {HALF_LIFE_YEARS}y): "
        f"{latest_year - 6}={year_weight(latest_year - 6, latest_year):.3f}  "
        f"{latest_year - 4}={year_weight(latest_year - 4, latest_year):.3f}  "
        f"{latest_year - 2}={year_weight(latest_year - 2, latest_year):.3f}  "
        f"{latest_year}={year_weight(latest_year, latest_year):.3f}"
    )

    print("\n3.1  Building term matrix …")
    matrix = build_term_matrix(df, weights)
    matrix.write_parquet(OUT / "isvidal_term_matrix.parquet")
    print(f"  {len(matrix)} rows → isvidal_term_matrix.parquet")

    print("\n3.2  Building opinion excerpts …")
    excerpts = build_opinion_excerpts(df, weights)
    print(f"  {len(excerpts)} rows (pre-stance)")

    print("\n3.3  Building code-block features …")
    code_features = build_code_features(df)
    code_features.write_parquet(OUT / "isvidal_code_features.parquet")
    print(f"  {len(code_features)} rows → isvidal_code_features.parquet")

    print("\n3.4  Building top posts …")
    top_posts = build_top_posts(df)
    top_posts.write_parquet(OUT / "isvidal_top_posts.parquet")
    print(f"  {len(top_posts)} rows → isvidal_top_posts.parquet")

    print("\n3.5  Building stack summary + stance merge …")
    summary = build_stack_summary(matrix, latest_year)
    # Apply cached stance classifications (if available), add verdict cols.
    # opinion_excerpts is written ONCE here, with stance, to avoid leaving a
    # stale parquet on disk if anything between the writes raises.
    excerpts_with_stance, term_stance = apply_stance_cache(excerpts, latest_year)
    excerpts_with_stance.write_parquet(OUT / "isvidal_opinion_excerpts.parquet")
    print(f"  {len(excerpts_with_stance)} rows → isvidal_opinion_excerpts.parquet")
    summary = summary.join(term_stance, on="term", how="left").with_columns([
        pl.col("positive_excerpts").fill_null(0),
        pl.col("negative_excerpts").fill_null(0),
        pl.col("neutral_excerpts").fill_null(0),
        pl.col("stance_score").fill_null(0.0),
        pl.col("verdict").fill_null("neutral"),
    ])
    summary.write_parquet(OUT / "isvidal_stack_summary.parquet")
    print(f"  {len(summary)} rows → isvidal_stack_summary.parquet")
    if STANCE_CACHE.exists():
        print(f"  stance cache applied: {len(summary.filter(pl.col('verdict') != 'neutral'))} terms classified")

    print("\n3.6  Writing analysis_report.md …")
    report = build_report(df, matrix, summary, excerpts_with_stance, top_posts, latest_year)
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
