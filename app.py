"""
Tabla Salarial de Programadores en España — Dashboard Streamlit

Fuente: hilo de MediaVida (mediavida.com/foro/dev/tabla-salarial-programadores-596068)
Datos: 231 programadores, Oct 2017 – Abr 2026, salarios ajustados por IPC a €2026.
"""

from pathlib import Path

import plotly.express as px
import polars as pl
import streamlit as st

DATA_PATH = Path(__file__).parent / "salarios_tabla.parquet"

st.set_page_config(
    page_title="Salarios Programadores España — MediaVida",
    page_icon="💶",
    layout="wide",
)


@st.cache_data
def load_data() -> pl.DataFrame:
    return pl.read_parquet(DATA_PATH)


df_all = load_data()

# ─── Sidebar filters ──────────────────────────────────────────────────────────

st.sidebar.header("Filtros")

# País toggle
solo_espana = st.sidebar.toggle("Solo España", value=True)

# Salary range
sal_min = int(df_all["salario_bruto_2026"].min())
sal_max = int(df_all["salario_bruto_2026"].max())
sal_range = st.sidebar.slider(
    "Salario bruto anual €2026",
    min_value=sal_min,
    max_value=sal_max,
    value=(sal_min, sal_max),
    step=1_000,
    format="%d€",
)

# Year range
year_min = int(df_all["year"].min())
year_max = int(df_all["year"].max())
year_range = st.sidebar.slider(
    "Año del post",
    min_value=year_min,
    max_value=year_max,
    value=(year_min, year_max),
)

# City multiselect
ciudades_disponibles = sorted(
    df_all.filter(pl.col("ciudad").is_not_null())["ciudad"].unique().to_list()
)
ciudades_sel = st.sidebar.multiselect(
    "Ciudad",
    options=ciudades_disponibles,
    default=[],
    placeholder="Todas",
)

# Modalidad multiselect
modalidades_disponibles = sorted(
    df_all.filter(pl.col("modalidad").is_not_null())["modalidad"].unique().to_list()
)
modalidad_sel = st.sidebar.multiselect(
    "Modalidad",
    options=modalidades_disponibles,
    default=[],
    placeholder="Todas",
)

# ─── Apply filters ─────────────────────────────────────────────────────────────

df = df_all

if solo_espana:
    df = df.filter(pl.col("pais") == "España")

df = df.filter(
    pl.col("salario_bruto_2026").is_between(sal_range[0], sal_range[1])
    & pl.col("year").is_between(year_range[0], year_range[1])
)

if ciudades_sel:
    df = df.filter(pl.col("ciudad").is_in(ciudades_sel))

if modalidad_sel:
    df = df.filter(pl.col("modalidad").is_in(modalidad_sel))

# ─── Header ────────────────────────────────────────────────────────────────────

st.title("Tabla Salarial de Programadores en España")
st.caption(
    "Fuente: [hilo de MediaVida](https://www.mediavida.com/foro/dev/tabla-salarial-programadores-596068) "
    f"· {len(df_all)} respuestas válidas · Oct 2017 – Abr 2026 · Salarios ajustados por IPC a €2026"
)

if len(df) == 0:
    st.warning("No hay datos con los filtros seleccionados.")
    st.stop()

# ─── KPIs ──────────────────────────────────────────────────────────────────────

vals = df["salario_bruto_2026"]
mediana = vals.median()

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("N", f"{len(df)}")
k2.metric("Mediana", f"{mediana:,.0f}€")
k3.metric("Media", f"{vals.mean():,.0f}€")
k4.metric("P25", f"{vals.quantile(0.25):,.0f}€")
k5.metric("P75", f"{vals.quantile(0.75):,.0f}€")

# ─── Histogram ─────────────────────────────────────────────────────────────────

st.subheader("Distribución de salario bruto anual (€2026)")

fig_hist = px.histogram(
    df.to_pandas(),
    x="salario_bruto_2026",
    nbins=30,
    labels={"salario_bruto_2026": "Salario bruto anual €2026"},
    color_discrete_sequence=["#636EFA"],
)
fig_hist.update_layout(
    yaxis_title="Programadores",
    xaxis_tickformat=",",
    bargap=0.05,
    showlegend=False,
    margin=dict(t=10),
)
fig_hist.add_vline(
    x=mediana, line_dash="dash", line_color="red",
    annotation_text=f"Mediana: {mediana:,.0f}€",
    annotation_position="top right",
)
st.plotly_chart(fig_hist, use_container_width=True)

# ─── Boxplot by city ──────────────────────────────────────────────────────────

st.subheader("Salario por ciudad (N ≥ 3)")

city_counts = (
    df.filter(pl.col("ciudad").is_not_null())
    .group_by("ciudad")
    .len()
    .filter(pl.col("len") >= 3)
)
top_cities = city_counts["ciudad"].to_list()

if top_cities:
    df_cities = df.filter(pl.col("ciudad").is_in(top_cities)).to_pandas()

    # Order by median salary descending
    city_order = (
        df.filter(pl.col("ciudad").is_in(top_cities))
        .group_by("ciudad")
        .agg(pl.col("salario_bruto_2026").median().alias("med"))
        .sort("med", descending=True)["ciudad"]
        .to_list()
    )

    fig_box = px.box(
        df_cities,
        x="salario_bruto_2026",
        y="ciudad",
        labels={
            "salario_bruto_2026": "Salario bruto anual €2026",
            "ciudad": "",
        },
        color_discrete_sequence=["#636EFA"],
        category_orders={"ciudad": city_order},
    )
    fig_box.update_layout(
        xaxis_tickformat=",",
        showlegend=False,
        margin=dict(t=10),
        height=max(350, len(top_cities) * 45),
    )
    st.plotly_chart(fig_box, use_container_width=True)
else:
    st.info("No hay ciudades con N ≥ 3 en la selección actual.")

# ─── Temporal evolution ────────────────────────────────────────────────────────

st.subheader("Evolución temporal de la mediana salarial")

by_year = (
    df.group_by("year")
    .agg([
        pl.col("salario_bruto_anual").median().round(0).alias("Mediana original €"),
        pl.col("salario_bruto_2026").median().round(0).alias("Mediana €2026"),
        pl.len().alias("n"),
    ])
    .filter(pl.col("n") >= 2)
    .sort("year")
    .to_pandas()
)

if len(by_year) > 1:
    fig_time = px.line(
        by_year,
        x="year",
        y=["Mediana original €", "Mediana €2026"],
        labels={"year": "Año del post", "value": "Salario bruto anual €", "variable": ""},
        markers=True,
    )
    fig_time.update_layout(
        xaxis=dict(dtick=1),
        yaxis_tickformat=",",
        margin=dict(t=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    # Annotate N per year
    for _, row in by_year.iterrows():
        fig_time.add_annotation(
            x=row["year"], y=row["Mediana €2026"],
            text=f"n={int(row['n'])}", showarrow=False,
            yshift=15, font=dict(size=10, color="gray"),
        )
    st.plotly_chart(fig_time, use_container_width=True)
else:
    st.info("No hay suficientes años para mostrar evolución temporal.")

# ─── Scatter: experience vs salary ─────────────────────────────────────────────

st.subheader("Experiencia vs. salario")

df_exp = df.filter(pl.col("experiencia_anos").is_not_null())

if len(df_exp) >= 5:
    fig_scatter = px.scatter(
        df_exp.to_pandas(),
        x="experiencia_anos",
        y="salario_bruto_2026",
        color="pais",
        hover_data=["autor", "ciudad", "year"],
        labels={
            "experiencia_anos": "Años de experiencia",
            "salario_bruto_2026": "Salario bruto anual €2026",
            "pais": "País",
        },
        color_discrete_map={"España": "#636EFA", "Extranjero": "#EF553B"},
    )
    fig_scatter.update_layout(
        xaxis=dict(dtick=2),
        yaxis_tickformat=",",
        margin=dict(t=10),
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
else:
    st.info("No hay suficientes datos con experiencia para este gráfico.")

# ─── Interactive table ─────────────────────────────────────────────────────────

st.subheader("Tabla de datos")

table_cols = [
    "autor", "year", "salario_bruto_anual", "salario_bruto_2026",
    "ciudad", "modalidad", "pais", "experiencia_anos", "tecnologia",
]
df_table = (
    df.select(table_cols)
    .sort("salario_bruto_2026", descending=True)
    .with_columns(
        pl.col(c).fill_null("") for c in ("ciudad", "modalidad", "pais", "tecnologia")
    )
)

st.dataframe(
    df_table.to_pandas(),
    use_container_width=True,
    hide_index=True,
    column_config={
        "autor": st.column_config.TextColumn("Usuario"),
        "year": st.column_config.NumberColumn("Año", format="%d"),
        "salario_bruto_anual": st.column_config.NumberColumn("Bruto anual €", format="%.0f"),
        "salario_bruto_2026": st.column_config.NumberColumn("€2026 (IPC)", format="%.0f"),
        "ciudad": st.column_config.TextColumn("Ciudad"),
        "modalidad": st.column_config.TextColumn("Modalidad"),
        "pais": st.column_config.TextColumn("País"),
        "experiencia_anos": st.column_config.NumberColumn("Exp. (años)", format="%d"),
        "tecnologia": st.column_config.TextColumn("Tecnología"),
    },
)

# ─── Transparency ─────────────────────────────────────────────────────────────

with st.expander("Metodología y transparencia"):
    n_total = len(df_all)
    n_bruto = df_all.filter(pl.col("es_bruto") == True).height
    n_neto = df_all.filter(pl.col("es_bruto") == False).height
    n_asumido = n_total - n_bruto - n_neto
    n_freq_inferred = df_all.filter(
        pl.col("nota_harmonizacion").str.contains("freq_inferida", literal=True)
    ).height

    st.markdown(f"""
**Fuente:** [Hilo de MediaVida — Tabla salarial programadores](https://www.mediavida.com/foro/dev/tabla-salarial-programadores-596068) (88 páginas, 2602 posts)

**Procesamiento:**
- Extracción automática con regex + filtros de tercera persona
- Deduplicación por usuario (se conserva el último post)
- Armonización: mensual→anual (×12), neto→bruto (IRPF aprox.), divisas→EUR (FX histórico)
- Ajuste por inflación: IPC España (INE) a €2026

**Transparencia del dato** (sobre {n_total} registros totales):
- Bruto explícito: {n_bruto} ({100*n_bruto/n_total:.0f}%)
- Neto explícito: {n_neto} ({100*n_neto/n_total:.0f}%)
- No especificado (asumido bruto): {n_asumido} ({100*n_asumido/n_total:.0f}%)
- Frecuencia inferida: {n_freq_inferred} ({100*n_freq_inferred/n_total:.0f}%)

**Limitaciones:**
- Self-reported: los datos dependen de la honestidad de los participantes
- Sesgo de selección: usuarios de MediaVida, no representativo de toda España
- La mayoría no especifica bruto/neto — se asume bruto, lo cual puede infraestimar el salario real de quienes reportaron neto
""")
