"""
isvidal — conclusiones técnicas sobre su stack (Streamlit dashboard).

Carga los parquets generados por analyze_isvidal.py (Fase 3).
Cada sección degrada con un info si falta su fuente de datos.

Fuente: mediavida.com/foro/dev/react-hilo-general-libreria-para-atraerlos-atarlos-todos-657749
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
TREND_LABELS = {
    "activo": "🟢 Activo",
    "declinante": "🟡 Declinante",
    "abandonado": "🔴 Abandonado",
}
TREND_COLORS = {
    "activo": "#16a34a",
    "declinante": "#ca8a04",
    "abandonado": "#dc2626",
}

st.set_page_config(
    page_title="isvidal — conclusiones técnicas",
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

latest_year = int(posts["year"].max()) if posts is not None else 2026

# ─── Sidebar ─────────────────────────────────────────────────────────────────

st.sidebar.header("Filtros")

topic_sel_labels = st.sidebar.multiselect(
    "Área técnica",
    options=list(TOPIC_LABELS.values()),
    default=list(TOPIC_LABELS.values()),
    placeholder="Todas",
)
label_to_key = {v: k for k, v in TOPIC_LABELS.items()}
topic_sel = [label_to_key[lbl] for lbl in topic_sel_labels]

trend_sel_labels = st.sidebar.multiselect(
    "Tendencia",
    options=list(TREND_LABELS.values()),
    default=[TREND_LABELS["activo"]],  # default: only show what he still uses
    placeholder="Todas",
)
label_to_trend = {v: k for k, v in TREND_LABELS.items()}
trend_sel = [label_to_trend[lbl] for lbl in trend_sel_labels]

year_min_default = 2020
year_max_default = latest_year
if posts is not None:
    year_min_default = int(posts["year"].min())
year_range = st.sidebar.slider(
    "Años (heatmap histórico)",
    year_min_default,
    year_max_default,
    (year_min_default, year_max_default),
)

st.sidebar.markdown("---")
st.sidebar.caption(
    f"**Ponderación por recencia:** decaimiento exponencial con half-life 2 años. "
    f"Un post de {latest_year - 4} pesa 0.25× uno de {latest_year}."
)
st.sidebar.caption(
    "**Limitación:** el conteo de menciones es neutral — una mención puede ser "
    "recomendación o crítica. Usar 'Últimas palabras' para ver contexto."
)

# ─── Header ──────────────────────────────────────────────────────────────────

st.title("isvidal — conclusiones técnicas")
st.caption(
    "Evolución de su uso de tools, libs y frameworks. Los valores recientes pesan más "
    f"por decaimiento exponencial (half-life 2 años). Ventana: **{year_min_default}–{latest_year}**. "
    "Fuente: [React hilo general — MediaVida]"
    "(https://www.mediavida.com/foro/dev/"
    "react-hilo-general-libreria-para-atraerlos-atarlos-todos-657749)"
)

# ─── 1. Stack recomendado actual ──────────────────────────────────────────────

st.subheader("Stack recomendado actual")
st.caption(
    "Top términos por score ponderado. Por defecto filtrado a **activos** "
    "(mencionados en los últimos 2 años). Cambia la tendencia en el sidebar."
)

if stack_summary is not None:
    ss = (
        stack_summary
        .filter(pl.col("topic").is_in(topic_sel))
        .filter(pl.col("trend").is_in(trend_sel))
        .sort("weighted_score", descending=True)
        .head(20)
        .to_pandas()
    )
    if len(ss) > 0:
        fig_bar = px.bar(
            ss,
            x="weighted_score",
            y="term",
            color="topic",
            orientation="h",
            hover_data=["total_mentions", "recent_mentions", "last_year", "trend"],
            labels={"weighted_score": "Score ponderado", "term": "", "topic": "Área"},
        )
        fig_bar.update_layout(
            yaxis=dict(autorange="reversed"),
            margin=dict(t=10, b=10),
            height=max(300, len(ss) * 30),
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("Sin términos con los filtros actuales.")
else:
    st.info("Sin datos — ejecuta `python isvidal/analyze_isvidal.py`.")

# ─── 2. Tendencias (tabla) ────────────────────────────────────────────────────

st.subheader("Clasificación por tendencia")
st.caption(
    "**Activo**: mencionado en los últimos 2 años · "
    "**Declinante**: última mención hace 2–3 años · "
    "**Abandonado**: última mención hace 4+ años."
)

if stack_summary is not None:
    table = (
        stack_summary
        .filter(pl.col("topic").is_in(topic_sel))
        .select([
            "term", "topic", "trend",
            "weighted_score", "total_mentions", "recent_mentions",
            "first_year", "last_year", "years_since_last",
        ])
        .sort(["trend", "weighted_score"], descending=[False, True])
        .to_pandas()
    )
    # Pretty labels
    table["topic"] = table["topic"].map(TOPIC_LABELS)
    table["trend"] = table["trend"].map(TREND_LABELS)
    table["weighted_score"] = table["weighted_score"].round(2)
    table = table.rename(columns={
        "term": "Término",
        "topic": "Área",
        "trend": "Tendencia",
        "weighted_score": "Score",
        "total_mentions": "Total",
        "recent_mentions": "Recientes",
        "first_year": "Desde",
        "last_year": "Hasta",
        "years_since_last": "Años sin mención",
    })
    st.dataframe(table, hide_index=True, use_container_width=True, height=420)
else:
    st.info("Sin datos — ejecuta Fase 3.")

# ─── 3. Últimas palabras — excerpt más reciente por término ──────────────────

st.subheader("Últimas palabras por término")
st.caption(
    "Qué dice AHORA, no un promedio histórico. "
    "Selecciona un término para ver su mención más reciente y el histórico debajo."
)

if opinion is not None and stack_summary is not None:
    term_topic = stack_summary.select(["term", "topic", "trend"]).unique()
    opinion_wt = opinion.join(term_topic, on="term", how="left")
    available_terms = (
        opinion_wt
        .filter(pl.col("topic").is_in(topic_sel))
        .filter(pl.col("trend").is_in(trend_sel))
        .sort("term")["term"]
        .unique(maintain_order=True)
        .to_list()
    )
    if available_terms:
        # Default to top-ranked term with excerpts
        default_idx = 0
        if stack_summary is not None:
            ranked = (
                stack_summary
                .filter(pl.col("topic").is_in(topic_sel))
                .filter(pl.col("trend").is_in(trend_sel))
                .sort("weighted_score", descending=True)["term"]
                .to_list()
            )
            for i, t in enumerate(available_terms):
                if t == next((r for r in ranked if r in available_terms), None):
                    default_idx = i
                    break

        selected_term = st.selectbox(
            "Término",
            options=available_terms,
            index=default_idx,
        )
        excerpts = (
            opinion_wt
            .filter(pl.col("term") == selected_term)
            .sort("year", descending=True)
            .select(["year", "post_num", "excerpt"])
        )
        if len(excerpts) > 0:
            latest = excerpts.row(0, named=True)
            st.markdown("**Última mención**")
            st.markdown(
                f"<div style='border-left: 4px solid #16a34a; padding: 8px 16px; "
                f"background: #f0fdf4; border-radius: 4px;'>"
                f"<strong>{latest['year']}</strong> · post #{latest['post_num']}<br>"
                f"<em>{latest['excerpt']}</em>"
                f"</div>",
                unsafe_allow_html=True,
            )
            if len(excerpts) > 1:
                with st.expander(f"Histórico completo ({len(excerpts)} menciones)"):
                    for row in excerpts.iter_rows(named=True):
                        st.markdown(
                            f"**{row['year']}** · post #{row['post_num']}\n\n"
                            f"> {row['excerpt']}"
                        )
                        st.divider()
    else:
        st.info("Sin términos para los filtros seleccionados.")
else:
    st.info("Sin datos — ejecuta Fase 3.")

# ─── 4. Evolución histórica (heatmap) ─────────────────────────────────────────

st.subheader("Evolución histórica de menciones")
st.caption("Qué se menciona cuándo. Útil para ver cuándo entró/salió cada término.")

if term_matrix is not None and stack_summary is not None:
    # Only show terms matching trend filter
    keep_terms = (
        stack_summary
        .filter(pl.col("trend").is_in(trend_sel))
        .filter(pl.col("topic").is_in(topic_sel))["term"]
        .to_list()
    )
    tm = (
        term_matrix
        .filter(pl.col("term").is_in(keep_terms))
        .filter(pl.col("year").is_between(year_range[0], year_range[1]))
        .group_by(["year", "term", "topic"])
        .agg(pl.col("weighted_count").sum())
        .sort(["topic", "term", "year"])
    )

    if len(tm) > 0:
        pivot = (
            tm.pivot(on="year", index="term", values="weighted_count", aggregate_function="sum")
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
            labels=dict(color="Score ponderado"),
            aspect="auto",
        )
        fig_heat.update_layout(
            xaxis_title="Año",
            yaxis_title="",
            margin=dict(t=10, b=10),
            height=max(300, len(y_labels) * 22),
        )
        st.plotly_chart(fig_heat, use_container_width=True)
    else:
        st.info("Sin menciones para los filtros actuales.")
else:
    st.info("Sin datos — ejecuta Fase 3.")

# ─── 5. Evolución del código ──────────────────────────────────────────────────

st.subheader("Evolución del código escrito")
st.caption("% de bloques de código con cada feature, por año.")

if code_features is not None and not code_features.is_empty():
    cf = (
        code_features
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
    cf["year"] = cf["year"].astype(str)

    fig_code = px.line(
        cf,
        x="year",
        y=["% hooks", "% generics", "% async", "% jsx"],
        markers=True,
        labels={"year": "Año", "value": "%", "variable": "Feature"},
    )
    fig_code.update_layout(margin=dict(t=10, b=10))
    st.plotly_chart(fig_code, use_container_width=True)
    st.caption(f"{len(code_features)} bloques de código detectados a lo largo del histórico.")
else:
    st.info("Sin bloques de código detectados.")

# ─── 6. Posts técnicos densos ─────────────────────────────────────────────────

st.subheader("Posts técnicos densos (último 30% del timeline)")
st.caption("Posts con más palabras o código, para leer en detalle sus argumentos.")

if top_posts is not None:
    df_top = (
        top_posts
        .select(["post_num", "year", "pagina", "word_count", "has_code", "texto", "code_blocks"])
        .sort("word_count", descending=True)
    )
    for row in df_top.iter_rows(named=True):
        label = (
            f"**#{row['post_num']}** · {row['year']} · "
            f"pág. {row['pagina']} · {row['word_count']} palabras"
        )
        if row["has_code"]:
            label += " 💻"
        with st.expander(label):
            st.write(row["texto"])
            blocks = json.loads(row["code_blocks"]) if row["code_blocks"] else []
            for block in blocks:
                st.code(block, language="tsx")
else:
    st.info("Sin datos — ejecuta Fase 3.")
