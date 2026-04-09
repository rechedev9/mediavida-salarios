"""
isvidal idea evolution dashboard — Streamlit

Loads structured data produced by analyze_isvidal.py (Phase 3).
Each section degrades gracefully with an info message if its data file is missing.

Source: mediavida.com/foro/dev/react-hilo-general-libreria-para-atraerlos-atarlos-todos-657749
"""

import json
from pathlib import Path

import plotly.express as px
import polars as pl
import streamlit as st

BASE = Path(__file__).parent

POSTS_PATH = BASE / "isvidal_posts.parquet"
TERM_MATRIX_PATH = BASE / "isvidal_term_matrix.parquet"
OPINION_PATH = BASE / "isvidal_opinion_excerpts.parquet"
CODE_FEATURES_PATH = BASE / "isvidal_code_features.parquet"
TOP_POSTS_PATH = BASE / "isvidal_top_posts.parquet"
STACK_SUMMARY_PATH = BASE / "isvidal_stack_summary.parquet"

# Topic keys match parquet values; labels shown in sidebar
TOPIC_KEYS = ["hooks", "state_data", "meta_frameworks", "typescript", "tooling", "testing", "patterns"]
TOPIC_LABELS = {
    "hooks": "Hooks",
    "state_data": "Estado / datos",
    "meta_frameworks": "Meta-frameworks",
    "typescript": "TypeScript",
    "tooling": "Build / tooling",
    "testing": "Testing",
    "patterns": "Patrones",
}

st.set_page_config(
    page_title="isvidal — ideas & evolución técnica",
    page_icon="⚛️",
    layout="wide",
)


@st.cache_data
def load(path: Path) -> pl.DataFrame | None:
    if not path.exists():
        return None
    return pl.read_parquet(path)


posts = load(POSTS_PATH)
term_matrix = load(TERM_MATRIX_PATH)
opinion = load(OPINION_PATH)
code_features = load(CODE_FEATURES_PATH)
top_posts = load(TOP_POSTS_PATH)
stack_summary = load(STACK_SUMMARY_PATH)

# ─── Sidebar ─────────────────────────────────────────────────────────────────

st.sidebar.header("Filtros")

topic_sel_labels = st.sidebar.multiselect(
    "Área técnica",
    options=list(TOPIC_LABELS.values()),
    default=list(TOPIC_LABELS.values()),
    placeholder="Todas",
)
# Map selected labels back to parquet keys
label_to_key = {v: k for k, v in TOPIC_LABELS.items()}
topic_sel = [label_to_key[lbl] for lbl in topic_sel_labels]

year_min = 2017
year_max = 2026
if posts is not None:
    year_min = int(posts["year"].min())
    year_max = int(posts["year"].max())
year_range = st.sidebar.slider("Años", year_min, year_max, (year_min, year_max))

use_recency = st.sidebar.toggle("Ponderación por recencia", value=True)
score_col = "weighted_count" if use_recency else "raw_count"

# ─── Header ──────────────────────────────────────────────────────────────────

st.title("isvidal — evolución de ideas en React / TypeScript")
st.caption(
    "Fuente: [React hilo general — MediaVida](https://www.mediavida.com/foro/dev/"
    "react-hilo-general-libreria-para-atraerlos-atarlos-todos-657749)"
)

if posts is not None:
    total = len(posts)
    first = posts["fecha_iso"].min()[:10]
    last = posts["fecha_iso"].max()[:10]
    med_words = int(posts["word_count"].median())
    pct_code = 100 * posts["has_code"].sum() / total

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Posts totales", total)
    c2.metric("Primer post", first)
    c3.metric("Último post", last)
    c4.metric("Palabras (mediana)", med_words)
    c5.metric("Posts con código", f"{pct_code:.0f}%")
else:
    st.info("Ejecuta la pipeline (Fases 1-3) para activar el dashboard.")

# ─── Activity timeline ────────────────────────────────────────────────────────

st.subheader("Actividad por año")

if posts is not None:
    by_year = (
        posts.filter(pl.col("year").is_between(year_range[0], year_range[1]))
        .group_by("year")
        .agg([
            pl.len().alias("posts"),
            pl.col("word_count").sum().alias("words"),
        ])
        .sort("year")
        .to_pandas()
    )

    fig = px.bar(
        by_year,
        x="year",
        y="posts",
        labels={"year": "Año", "posts": "Posts"},
        color_discrete_sequence=["#636EFA"],
    )
    fig.add_scatter(
        x=by_year["year"],
        y=by_year["words"] / 100,
        mode="lines+markers",
        name="Palabras / 100",
        yaxis="y2",
        line=dict(color="#EF553B"),
    )
    fig.update_layout(
        xaxis=dict(dtick=1),
        yaxis2=dict(overlaying="y", side="right", showgrid=False, title="Palabras / 100"),
        legend=dict(x=0.01, y=0.99),
        margin=dict(t=10),
        showlegend=True,
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Sin datos — ejecuta Fase 2.")

# ─── Tech mention heatmap ─────────────────────────────────────────────────────

st.subheader("Mapa de menciones técnicas")

if term_matrix is not None:
    tm = (
        term_matrix
        .filter(
            pl.col("topic").is_in(topic_sel)
            & pl.col("year").is_between(year_range[0], year_range[1])
        )
        .group_by(["year", "term", "topic"])
        .agg(pl.col(score_col).sum())
        .sort(["topic", "term", "year"])
    )

    if len(tm) > 0:
        pivot = (
            tm.pivot(on="year", index="term", values=score_col, aggregate_function="sum")
            .fill_null(0)
        )
        year_cols = sorted(c for c in pivot.columns if c != "term")
        z = pivot.select(year_cols).to_numpy()
        y_labels = pivot["term"].to_list()

        fig_heat = px.imshow(
            z,
            x=year_cols,
            y=y_labels,
            color_continuous_scale="Blues",
            labels=dict(color="Score"),
            aspect="auto",
        )
        fig_heat.update_layout(
            xaxis_title="Año",
            yaxis_title="",
            margin=dict(t=10),
            height=max(300, len(y_labels) * 22),
        )
        st.plotly_chart(fig_heat, use_container_width=True)
    else:
        st.info("Sin menciones para los filtros seleccionados.")
else:
    st.info("Sin datos — ejecuta Fase 3.")

# ─── Current stack (recency-weighted) ────────────────────────────────────────

st.subheader("Stack actual — top términos" + (" (ponderado)" if use_recency else " (raw)"))

if stack_summary is not None:
    ss = (
        stack_summary
        .filter(pl.col("topic").is_in(topic_sel))
        .sort("weighted_score" if use_recency else "total_mentions", descending=True)
        .head(20)
        .to_pandas()
    )
    y_col = "weighted_score" if use_recency else "total_mentions"
    fig_bar = px.bar(
        ss,
        x=y_col,
        y="term",
        color="topic",
        orientation="h",
        labels={y_col: "Score", "term": "", "topic": "Área"},
    )
    fig_bar.update_layout(
        yaxis=dict(autorange="reversed"),
        margin=dict(t=10),
        height=max(300, len(ss) * 30),
    )
    st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.info("Sin datos — ejecuta Fase 3.")

# ─── Opinion deep-dive ────────────────────────────────────────────────────────

st.subheader("Seguimiento de opiniones por término")

if opinion is not None and stack_summary is not None:
    # Join term→topic from stack_summary (opinion doesn't carry topic)
    term_topic = stack_summary.select(["term", "topic"]).unique()
    opinion_with_topic = opinion.join(term_topic, on="term", how="left")
    available_terms = sorted(
        opinion_with_topic
        .filter(pl.col("topic").is_in(topic_sel))["term"]
        .unique().to_list()
    )
    if available_terms:
        selected_term = st.selectbox("Término", options=available_terms)
        excerpts = (
            opinion_with_topic
            .filter(
                (pl.col("term") == selected_term)
                & pl.col("year").is_between(year_range[0], year_range[1])
            )
            .sort("year", descending=True)
            .select(["year", "post_num", "excerpt"])
        )
        for row in excerpts.iter_rows(named=True):
            st.markdown(
                f"**{row['year']}** · post #{row['post_num']}\n\n> {row['excerpt']}"
            )
            st.divider()
    else:
        st.info("Sin términos para los filtros seleccionados.")
else:
    st.info("Sin datos — ejecuta Fase 3.")

# ─── Code evolution ───────────────────────────────────────────────────────────

st.subheader("Evolución del código")

if code_features is not None:
    cf = (
        code_features
        .filter(pl.col("year").is_between(year_range[0], year_range[1]))
        .group_by("year")
        .agg([
            pl.len().alias("total_blocks"),
            pl.col("has_hooks").sum().alias("has_hooks"),
            pl.col("has_generics").sum().alias("has_generics"),
            pl.col("has_async").sum().alias("has_async"),
            pl.col("has_jsx").sum().alias("has_jsx"),
        ])
        .sort("year")
        .with_columns([
            (pl.col("has_hooks") / pl.col("total_blocks") * 100).alias("% hooks"),
            (pl.col("has_generics") / pl.col("total_blocks") * 100).alias("% generics"),
            (pl.col("has_async") / pl.col("total_blocks") * 100).alias("% async"),
            (pl.col("has_jsx") / pl.col("total_blocks") * 100).alias("% jsx"),
        ])
        .to_pandas()
    )

    fig_code = px.line(
        cf,
        x="year",
        y=["% hooks", "% generics", "% async", "% jsx"],
        markers=True,
        labels={"year": "Año", "value": "%", "variable": "Feature"},
    )
    fig_code.update_layout(xaxis=dict(dtick=1), margin=dict(t=10))
    st.plotly_chart(fig_code, use_container_width=True)
else:
    st.info("Sin datos — ejecuta Fase 3.")

# ─── Top posts ────────────────────────────────────────────────────────────────

st.subheader("Posts más densos / con más código")

if top_posts is not None:
    df_top = (
        top_posts
        .filter(pl.col("year").is_between(year_range[0], year_range[1]))
        .select(["post_num", "year", "pagina", "word_count", "has_code", "texto", "code_blocks"])
        .sort("word_count", descending=True)
    )

    for row in df_top.iter_rows(named=True):
        label = f"**#{row['post_num']}** · {row['year']} · pág. {row['pagina']} · {row['word_count']} palabras"
        if row["has_code"]:
            label += " 💻"
        with st.expander(label):
            st.write(row["texto"])
            blocks = json.loads(row["code_blocks"]) if row["code_blocks"] else []
            for block in blocks:
                st.code(block, language="tsx")
else:
    st.info("Sin datos — ejecuta Fase 3.")
