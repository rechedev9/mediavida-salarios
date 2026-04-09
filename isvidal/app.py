"""
isvidal — conclusiones técnicas sobre su stack (Streamlit dashboard).

Carga los parquets generados por analyze_isvidal.py (Fase 3) con clasificación
de stance cached en `stance_cache.json`. Cada sección degrada con un info si
falta su fuente de datos.

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

TOPIC_LABELS = {
    "hooks": "Hooks",
    "state_data": "Estado / datos",
    "meta_frameworks": "Meta-frameworks",
    "typescript": "TypeScript",
    "tooling": "Build / tooling",
    "testing": "Testing",
    "patterns": "Patrones",
    "styling": "Styling / UI",
    "data_api": "Data / API",
    "platforms": "Platforms",
    "backend": "Backend",
    "utils": "Utils",
}

TREND_LABELS = {
    "activo": "🟢 Activo",
    "declinante": "🟡 Declinante",
    "abandonado": "🔴 Abandonado",
}

VERDICT_LABELS = {
    "recomienda": "✅ Recomienda",
    "desaconseja": "❌ Desaconseja",
    "mixto": "🔀 Mixto",
    "neutral": "➖ Neutral",
}

VERDICT_COLORS = {
    "recomienda": "#16a34a",
    "desaconseja": "#dc2626",
    "mixto": "#d97706",
    "neutral": "#6b7280",
}

STANCE_STYLE = {
    "positivo": ("#16a34a", "#f0fdf4"),
    "negativo": ("#dc2626", "#fef2f2"),
    "neutral":  ("#6b7280", "#f9fafb"),
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
earliest_year = int(posts["year"].min()) if posts is not None else 2020

# ─── Sidebar ─────────────────────────────────────────────────────────────────

st.sidebar.header("Filtros")

topic_sel_labels = st.sidebar.multiselect(
    "Área técnica",
    options=list(TOPIC_LABELS.values()),
    default=list(TOPIC_LABELS.values()),
    placeholder="Todas",
)
label_to_topic = {v: k for k, v in TOPIC_LABELS.items()}
topic_sel = [label_to_topic[lbl] for lbl in topic_sel_labels]

verdict_sel_labels = st.sidebar.multiselect(
    "Verdict",
    options=list(VERDICT_LABELS.values()),
    default=list(VERDICT_LABELS.values()),
    placeholder="Todos",
)
label_to_verdict = {v: k for k, v in VERDICT_LABELS.items()}
verdict_sel = [label_to_verdict[lbl] for lbl in verdict_sel_labels]

trend_sel_labels = st.sidebar.multiselect(
    "Tendencia temporal",
    options=list(TREND_LABELS.values()),
    default=[TREND_LABELS["activo"]],
    placeholder="Todas",
)
label_to_trend = {v: k for k, v in TREND_LABELS.items()}
trend_sel = [label_to_trend[lbl] for lbl in trend_sel_labels]

year_range = st.sidebar.slider(
    "Años (heatmap histórico)",
    earliest_year,
    latest_year,
    (earliest_year, latest_year),
)

st.sidebar.markdown("---")
st.sidebar.caption(
    f"**Recencia:** decaimiento exponencial, half-life 2 años. "
    f"Un post de {latest_year - 4} pesa 0.25× uno de {latest_year}."
)
st.sidebar.caption(
    "**Verdict:** agregado desde excerpts clasificados con stance (positivo/negativo/neutral). "
    "Ponderado por recencia: una mención reciente negativa vence a muchas positivas antiguas."
)

# ─── Header ──────────────────────────────────────────────────────────────────

st.title("isvidal — conclusiones técnicas")
st.caption(
    f"Qué recomienda y desaconseja ahora mismo sobre frontend/JS/TS. "
    f"Ventana: **{earliest_year}–{latest_year}** · 199 posts analizados · "
    "200 excerpts clasificados por stance con Haiku + revisión manual. "
    "Fuente: [React hilo general — MediaVida]"
    "(https://www.mediavida.com/foro/dev/"
    "react-hilo-general-libreria-para-atraerlos-atarlos-todos-657749)"
)


def filter_stack(df: pl.DataFrame) -> pl.DataFrame:
    """Apply sidebar filters to stack_summary."""
    return (
        df
        .filter(pl.col("topic").is_in(topic_sel))
        .filter(pl.col("verdict").is_in(verdict_sel))
        .filter(pl.col("trend").is_in(trend_sel))
    )


# ─── 1. Stack actual — recomienda vs desaconseja ──────────────────────────────

st.subheader("Stack actual")
st.caption(
    "Izquierda: lo que **recomienda**. Derecha: lo que **desaconseja** explícitamente. "
    "Ordenado por score ponderado por recencia. Por defecto filtrado a `activo`."
)

if stack_summary is not None:
    filtered = filter_stack(stack_summary)
    col_rec, col_des = st.columns(2)

    with col_rec:
        st.markdown("#### ✅ Recomienda")
        rec = (
            filtered
            .filter(pl.col("verdict") == "recomienda")
            .sort("weighted_score", descending=True)
            .head(20)
            .to_pandas()
        )
        if len(rec) > 0:
            rec["topic_label"] = rec["topic"].map(TOPIC_LABELS)
            fig_rec = px.bar(
                rec,
                x="weighted_score",
                y="term",
                color="topic_label",
                orientation="h",
                hover_data=["total_mentions", "recent_mentions", "last_year",
                            "positive_excerpts", "negative_excerpts"],
                labels={"weighted_score": "Score", "term": "", "topic_label": "Área"},
            )
            fig_rec.update_layout(
                yaxis=dict(autorange="reversed"),
                margin=dict(t=10, b=10),
                height=max(280, len(rec) * 28),
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.3),
            )
            st.plotly_chart(fig_rec, use_container_width=True)
        else:
            st.info("Ningún término recomendado con los filtros actuales.")

    with col_des:
        st.markdown("#### ❌ Desaconseja")
        des = (
            filtered
            .filter(pl.col("verdict") == "desaconseja")
            .sort("weighted_score", descending=True)
            .head(20)
            .to_pandas()
        )
        if len(des) > 0:
            des["topic_label"] = des["topic"].map(TOPIC_LABELS)
            fig_des = px.bar(
                des,
                x="weighted_score",
                y="term",
                color="topic_label",
                orientation="h",
                hover_data=["total_mentions", "recent_mentions", "last_year",
                            "positive_excerpts", "negative_excerpts"],
                labels={"weighted_score": "Score", "term": "", "topic_label": "Área"},
            )
            fig_des.update_layout(
                yaxis=dict(autorange="reversed"),
                margin=dict(t=10, b=10),
                height=max(280, len(des) * 28),
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.3),
            )
            st.plotly_chart(fig_des, use_container_width=True)
        else:
            st.info("Ningún término desaconsejado con los filtros actuales.")
else:
    st.info("Sin datos — ejecuta `python isvidal/analyze_isvidal.py`.")

# ─── 2. Tabla completa ────────────────────────────────────────────────────────

st.subheader("Clasificación completa")
st.caption(
    "Todos los términos con verdict (recomienda/desaconseja/mixto/neutral) y "
    "tendencia temporal (activo/declinante/abandonado). Los filtros del sidebar aplican."
)

if stack_summary is not None:
    table = (
        stack_summary
        .filter(pl.col("topic").is_in(topic_sel))
        .filter(pl.col("verdict").is_in(verdict_sel))
        .filter(pl.col("trend").is_in(trend_sel))
        .select([
            "term", "topic", "verdict", "trend",
            "weighted_score", "stance_score",
            "positive_excerpts", "negative_excerpts", "neutral_excerpts",
            "total_mentions", "first_year", "last_year",
        ])
        .sort(["verdict", "weighted_score"], descending=[False, True])
        .to_pandas()
    )
    if len(table) > 0:
        table["topic"] = table["topic"].map(TOPIC_LABELS)
        table["verdict"] = table["verdict"].map(VERDICT_LABELS)
        table["trend"] = table["trend"].map(TREND_LABELS)
        table["weighted_score"] = table["weighted_score"].round(2)
        table["stance_score"] = table["stance_score"].round(2)
        table = table.rename(columns={
            "term": "Término",
            "topic": "Área",
            "verdict": "Verdict",
            "trend": "Tendencia",
            "weighted_score": "Score",
            "stance_score": "Stance±",
            "positive_excerpts": "➕",
            "negative_excerpts": "➖",
            "neutral_excerpts": "◯",
            "total_mentions": "Total",
            "first_year": "Desde",
            "last_year": "Hasta",
        })
        st.dataframe(table, hide_index=True, use_container_width=True, height=460)
    else:
        st.info("Sin términos con los filtros actuales.")
else:
    st.info("Sin datos — ejecuta Fase 3.")

# ─── 3. Últimas palabras por término ──────────────────────────────────────────

st.subheader("Últimas palabras por término")
st.caption(
    "Qué dice AHORA, no un promedio histórico. "
    "Cada excerpt está etiquetado con su stance (positivo/negativo/neutral)."
)

if opinion is not None and stack_summary is not None:
    term_meta = stack_summary.select(["term", "topic", "trend", "verdict"]).unique()
    opinion_wt = opinion.join(term_meta, on="term", how="left")
    available_terms = (
        opinion_wt
        .filter(pl.col("topic").is_in(topic_sel))
        .filter(pl.col("verdict").is_in(verdict_sel))
        .filter(pl.col("trend").is_in(trend_sel))
        .sort("term")["term"]
        .unique(maintain_order=True)
        .to_list()
    )
    if available_terms:
        ranked = (
            stack_summary
            .filter(pl.col("topic").is_in(topic_sel))
            .filter(pl.col("verdict").is_in(verdict_sel))
            .filter(pl.col("trend").is_in(trend_sel))
            .sort("weighted_score", descending=True)["term"]
            .to_list()
        )
        default_term = next((t for t in ranked if t in available_terms), available_terms[0])
        default_idx = available_terms.index(default_term)

        selected_term = st.selectbox(
            "Término",
            options=available_terms,
            index=default_idx,
        )
        excerpts = (
            opinion_wt
            .filter(pl.col("term") == selected_term)
            .sort("year", descending=True)
            .select(["year", "post_num", "excerpt", "stance"])
        )
        if len(excerpts) > 0:
            latest = excerpts.row(0, named=True)
            border, bg = STANCE_STYLE.get(latest["stance"], STANCE_STYLE["neutral"])
            st.markdown("**Última mención**")
            st.markdown(
                f"<div style='border-left: 4px solid {border}; padding: 10px 16px; "
                f"background: {bg}; border-radius: 4px;'>"
                f"<strong>{latest['year']}</strong> · post #{latest['post_num']} · "
                f"<span style='color: {border}; font-weight: 600;'>{latest['stance']}</span><br>"
                f"<em>{latest['excerpt']}</em>"
                f"</div>",
                unsafe_allow_html=True,
            )
            if len(excerpts) > 1:
                with st.expander(f"Histórico completo ({len(excerpts)} menciones)"):
                    for row in excerpts.iter_rows(named=True):
                        border2, bg2 = STANCE_STYLE.get(row["stance"], STANCE_STYLE["neutral"])
                        st.markdown(
                            f"<div style='border-left: 3px solid {border2}; padding: 6px 12px; "
                            f"background: {bg2}; margin-bottom: 8px; border-radius: 3px;'>"
                            f"<strong>{row['year']}</strong> · post #{row['post_num']} · "
                            f"<span style='color: {border2};'>{row['stance']}</span><br>"
                            f"{row['excerpt']}</div>",
                            unsafe_allow_html=True,
                        )
    else:
        st.info("Sin términos para los filtros seleccionados.")
else:
    st.info("Sin datos — ejecuta Fase 3.")

# ─── 4. Evolución histórica (heatmap) ─────────────────────────────────────────

st.subheader("Evolución histórica de menciones")
st.caption("Qué término se menciona cuándo. Intensidad = score ponderado.")

if term_matrix is not None and stack_summary is not None:
    keep_terms = (
        filter_stack(stack_summary)["term"].to_list()
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
            height=max(300, len(y_labels) * 20),
        )
        st.plotly_chart(fig_heat, use_container_width=True)
    else:
        st.info("Sin menciones para los filtros actuales.")
else:
    st.info("Sin datos — ejecuta Fase 3.")

# ─── 5. Posts técnicos densos ─────────────────────────────────────────────────

st.subheader("Posts técnicos densos")
st.caption(
    "Posts del último 30% del timeline con ≥2 términos técnicos o código. "
    "Ordenados por densidad técnica. Clic para expandir el post completo."
)

if top_posts is not None and not top_posts.is_empty():
    df_top = (
        top_posts
        .select(["post_num", "year", "pagina", "word_count", "has_code", "texto", "code_blocks"])
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
