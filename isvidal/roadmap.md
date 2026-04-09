# Roadmap — isvidal thread extraction & idea evolution analysis

## Objective

Extract every forum post written by the user **`isvidal`** in the MediaVida thread
[`react-hilo-general-libreria-para-atraerlos-atarlos-todos-657749`](https://www.mediavida.com/foro/dev/react-hilo-general-libreria-para-atraerlos-atarlos-todos-657749)
(40 pages), preserving conversational and technical context (quoted posts, code blocks,
timestamps) to support a deep, recency-weighted analysis of how his ideas on
React / TypeScript / frontend architecture evolved over the years.

The deliverable is a **Streamlit dashboard** (`app.py`) backed by structured data:

1. A clean dataset of isvidal's posts annotated with conversational context.
2. Analysis data: tech-stack mention matrices, opinion excerpts, code-block features,
   all weighted toward recent posts.
3. An interactive dashboard to explore the evolution of his ideas — filterable by
   topic and year, with code excerpts and recency-weighted "current stack" view.

---

## Current State

- `isvidal/app.py` — dashboard skeleton, loads from analysis data files when available
- `isvidal/log.md` — subproject context (confirmed HTML structure, design decisions)
- `isvidal/roadmap.md` — this file
- **Phase 1 — ✅ DONE (2026-04-09).** `scrape_isvidal.py` + `posts_all.json` (1196 posts, 199 isvidal, 119 authors, 2020-07-23 — 2026-04-07).
- **Phase 2 — ✅ DONE (2026-04-09).** `filter_isvidal.py` → `isvidal_posts.parquet` (199 rows), `isvidal_context.parquet` (149 rows), `isvidal_stats.txt`. 3-post round-trip verified.
- **Phase 3 — ✅ DONE (2026-04-09).** `analyze_isvidal.py` → 5 parquets + `analysis_report.md`. 28 terms hit, 127 total mentions, 11 code blocks from 5 posts. Top terms: Redux (39.4), useEffect (21.1), SWR (20.9), Zustand (20.5).
- **Phase 4 — ✅ DONE (2026-04-09).** `app.py` — 7 sections fully wired to real data. Fixed topic key mismatch (parquet uses snake_case), opinion→topic join via stack_summary, code_blocks JSON parsing. `streamlit run isvidal/app.py` verified healthy.
- **Phase 5 — ✅ DONE (2026-04-09).** Expanded term dictionary from 66 → 80+ terms across 12 topics (styling, data_api, platforms, backend, utils added). Removed 38 dead terms. Improved regex for compound-term variants (React Router ≡ react-router). Added `TERM_ALIASES` (TailwindCSS → Tailwind). Classified 200 opinion excerpts by stance (positivo/negativo/neutral) via Claude Haiku subagent + manual pass for the 15 excerpts added by regex improvements. Added `verdict` column (`recomienda`/`desaconseja`/`mixto`/`neutral`) to `isvidal_stack_summary.parquet`, computed from recency-weighted stance score (positive mentions ×year_weight minus negatives). Relaxed top_posts filter from `word_count≥100` to `tech_density≥2`, recovering 14 extra technical posts (10→24). Rewrote `app.py` with dual recomienda/desaconseja charts, verdict filter, stance-colored excerpts. Next.js now correctly shows as **desaconseja** (2026 "no uses Next.js"), Tailwind as **recomienda #1** (score 10.55, merged with TailwindCSS variant).

Parent repo context:
- `../scrape_mediavida.py` — working scraper skeleton to fork (fetch/cache/parse ~60 lines)
- `../raw_html/` — cached salary thread pages confirm MediaVida HTML structure
- `../venv` (Python 3.14) — has `httpx`, `bs4`, `lxml`, `polars`, `pandas`, `tqdm`; no new deps needed

---

## Approach

Four staged phases, each verifiable end-to-end before the next begins.

**Fork vs. extend.** Fork the parent scraper skeleton into `scrape_isvidal.py` and modify
the parser to preserve quote metadata and code blocks. Do not modify `../scrape_mediavida.py`.

**Include full thread.** Keep all posts in `posts_all.json` to enable `#N` → author
resolution and to capture how others responded to isvidal. The filter layer narrows
to isvidal's own posts for analysis.

---

## Phase 1 — Scraper + parser

**Goal:** `posts_all.json` with every post in the thread, quotes structured, code blocks preserved.

1. Create `scrape_isvidal.py` from the parent skeleton:
   - `BASE_URL` → React thread URL.
   - `TOTAL_PAGES = 40`, `RAW_DIR = raw_html/`, `OUTPUT = posts_all.json`.
   - Same fetch-cache logic, headers, and jitter (1.2–2.5s between pages).

2. Rewrite `parse_posts` to preserve quote + code metadata per post:
   - `quotes: list[{ref_num, inline_text, block_text}]` — walk `.post-contents` for
     `<a class="quote">`, capture trailing text (inline) and following `<blockquote>` (block).
   - `code_blocks: list[str]` — `.post-contents pre` raw text.
   - `texto` — copy of `.post-contents` after stripping quotes, `<pre>`, and code tags.

3. **Tracer bullet:** run page 1 only, spot-check one quoted post and one clean post in JSON.

4. Full run (40 pages). Populate `raw_html/page_001.html … page_040.html` + `posts_all.json`.

5. Sanity check — print: total posts, unique authors, isvidal post count, date range.
   Abort loudly if `count(isvidal) == 0`.

---

## Phase 2 — Filter, enrich, structure

**Goal:** `isvidal_posts.parquet` ready for analysis; `isvidal_stats.txt` as a quick reference.

1. Create `filter_isvidal.py`. Load `posts_all.json`, build post_num → author lookup.

2. Emit `isvidal_posts.parquet`:
   ```
   post_num, pagina, timestamp, fecha_iso, year, texto,
   quotes (list[struct]), code_blocks (list[str]),
   word_count, has_code, replied_to_autores (list[str])
   ```
   Sorted by `timestamp` ascending. Zero null timestamps.

3. Emit `isvidal_context.parquet` — non-isvidal posts that quote him. Same schema +
   `quoting_isvidal_post_num`. Useful for seeing how his ideas landed.

4. Emit `isvidal_stats.txt`: total posts, years active, posts/year, median word count,
   % posts with code, top 10 authors isvidal quoted, top 10 authors who quoted isvidal.

5. Verify: row count matches Phase 1 isvidal count; 3-post manual round-trip vs. raw HTML.

---

## Phase 3 — Idea-evolution analysis (recency-weighted)

**Goal:** structured data files that feed the dashboard, plus a human-readable summary.

Load `isvidal_posts.parquet`. All outputs land in `isvidal/` and are committed.

### 3.1 Tech-stack mention scan

Regex over `texto` + `code_blocks` for curated terms grouped by topic:

- **React hooks:** `useEffect, useState, useMemo, useCallback, useRef, useContext, useReducer, useTransition, useDeferredValue, Suspense, ErrorBoundary`
- **State/data:** `Redux, Zustand, Jotai, Recoil, MobX, React Query, SWR, TanStack, Context API`
- **Meta-frameworks:** `Next.js, Remix, Gatsby, Astro, RSC, App Router, Pages Router, server components, server actions`
- **TypeScript:** `strict, generics, zod, io-ts, any, unknown, type, interface, satisfies, as const`
- **Build/tooling:** `Webpack, Vite, Turbopack, Rollup, esbuild, Babel, SWC, pnpm, monorepo, turborepo`
- **Testing:** `Jest, Vitest, RTL, Testing Library, Cypress, Playwright, MSW`
- **Patterns:** `composition, hooks pattern, render props, HOC, compound component, colocation, DX, DRY, YAGNI, abstraction`

Output: `isvidal_term_matrix.parquet` — columns: `year, term, topic, raw_count, weighted_count`
(recency weight: linear `1.0 → 2.0` across the post timeline, applied per post before aggregating).

### 3.2 Opinion excerpts

Per term, extract sentences containing it (±1 sentence context). One row per hit.

Output: `isvidal_opinion_excerpts.parquet` — columns: `term, year, post_num, excerpt, weighted_year`

### 3.3 Code-block evolution

Per code block, detect: `tsx/ts/jsx/js`, hooks present (list), JSX present, `async/await`,
generics (`<T>`), `type`/`interface` keyword, imports (list of detected lib names).

Output: `isvidal_code_features.parquet` — columns:
`post_num, year, lang_hint, has_hooks, hook_names, has_jsx, has_async, has_generics, imports`

### 3.4 Top interesting posts

Filter: last 30% of timeline by date, `word_count >= 100` OR `has_code == True`,
sorted by `word_count` descending, top 30.

Output: `isvidal_top_posts.parquet` — same schema as `isvidal_posts.parquet`.

### 3.5 Recency-weighted stack summary

Aggregate `isvidal_term_matrix` by `term`, sum `weighted_count`, group by `topic`.
Output: `isvidal_stack_summary.parquet` — columns: `term, topic, weighted_score, first_year, last_year, total_mentions`

### 3.6 Human-readable summary

`analysis_report.md` — markdown with:
- Temporal summary (posts/year, code ratio trend).
- Top terms per topic (raw + recency-weighted).
- Opinion evolution excerpts for the 5 most interesting terms.
- Links to the dashboard for the interactive view.

---

## Phase 4 — Streamlit dashboard (app.py)

**Goal:** interactive exploration of isvidal's evolving ideas.

`app.py` loads from Phase 2+3 data files. It fails gracefully if they don't exist yet.

### Sections

1. **Header** — isvidal profile: total posts, first/last post, years active, median
   word count, % posts with code. Source link to the MediaVida thread.

2. **Activity timeline** — posts/year and words/year as a dual-axis bar+line chart.

3. **Tech mention heatmap** — Plotly heatmap: X = year, Y = term, Z = weighted_count.
   Sidebar filter by topic group (hooks / state / meta-frameworks / TS / tooling / testing / patterns).

4. **Current stack** — recency-weighted bar chart of top 20 terms (from `isvidal_stack_summary`).
   Toggle: show raw vs. recency-weighted score.

5. **Opinion deep-dive** — term selector → sorted list of excerpts across years,
   newest first. Shows `year · post_num · excerpt`. Lets you trace opinion flips.

6. **Code evolution** — stacked area or line chart: has_hooks%, has_generics%,
   has_async%, has_jsx% per year.

7. **Top posts** — interactive table with columns: year, pagina, word_count, has_code,
   preview of `texto[:200]`. Click row → expand full post + code blocks in expander.

### Sidebar filters

- Topic group (multiselect)
- Year range (slider)
- Recency weighting on/off (toggle, affects heatmap and current stack)

### Tech

```
streamlit>=1.35
plotly>=5.20
polars>=1.0
pandas         # for plotly compatibility
```

> **Checkpoint:** `streamlit run isvidal/app.py` works locally with real data (Phases 2+3 done).
> Each section degrades gracefully (info message) if its data file is missing.

---

## Files Likely Affected

```
isvidal/
├── app.py                        # dashboard (skeleton exists, activates with data)
├── roadmap.md                    # this file
├── log.md                        # subproject context log
├── scrape_isvidal.py             # Phase 1 — NEW
├── filter_isvidal.py             # Phase 2 — NEW
├── analyze_isvidal.py            # Phase 3 — NEW
├── raw_html/                     # Phase 1 cache — gitignore candidate
│   ├── page_001.html
│   └── … page_040.html
├── posts_all.json                # Phase 1 output (all thread posts)
├── isvidal_posts.parquet         # Phase 2 output
├── isvidal_context.parquet       # Phase 2 output (posts quoting isvidal)
├── isvidal_stats.txt             # Phase 2 output
├── isvidal_term_matrix.parquet   # Phase 3.1 output
├── isvidal_opinion_excerpts.parquet  # Phase 3.2 output
├── isvidal_code_features.parquet # Phase 3.3 output
├── isvidal_top_posts.parquet     # Phase 3.4 output
├── isvidal_stack_summary.parquet # Phase 3.5 output
└── analysis_report.md            # Phase 3.6 output
```

Parent files touched: **none**.

---

## Risks

| Risk | Probability | Mitigation |
|------|-------------|------------|
| Author handle mismatch (case, accent) | Low | Phase 1 aborts if count(isvidal)==0 |
| Quote-parser fragility (nested, inconsistent render) | Medium | Validate page 1 first; iterate before full run |
| Code blocks use `<code>` not `<pre>` | Low | Check page 1, adapt selector |
| isvidal posted <10 times (too few for matrix) | Low | Phase 1 stats reveal this; shrink Phase 3 scope |
| MediaVida blocks scraper | Very low | Reuse parent's headers + realistic jitter |

---

## Verification

- **Phase 1:** `posts_all.json` — 3 spot-checked posts round-trip vs. cached HTML (texto, quotes, code). isvidal count > 0. Total posts ~1200 ± 50%.
- **Phase 2:** `isvidal_posts.parquet` — no null timestamps, row count matches Phase 1 isvidal count, 3-post manual round-trip.
- **Phase 3:** `analysis_report.md` temporal numbers match `isvidal_stats.txt` exactly. Term matrix rows sum ≤ number of posts. No term appears in wrong topic group.
- **Phase 4:** `streamlit run app.py` loads all sections with real data. Sidebar filters update all charts correctly. Top posts expand cleanly.

---

## Open Questions

- **Scope of Phase 3 terms:** initial list is curated. After seeing Phase 1 stats (post
  volume, code block count), we may narrow or expand the term list. Non-blocking — proceed
  with current list and trim after the first run.
