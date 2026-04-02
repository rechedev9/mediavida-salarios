"""
Harmonize salary data, apply Spain CPI inflation adjustment, and produce the
final salary table with descriptive statistics.

Inputs:  salarios_dedup.parquet
Outputs: salarios_tabla.csv / .parquet
         salarios_stats.txt
"""

from pathlib import Path

import polars as pl

IN_DEDUP = Path("salarios_dedup.parquet")
OUT_CSV = Path("salarios_tabla.csv")
OUT_PARQUET = Path("salarios_tabla.parquet")
OUT_STATS = Path("salarios_stats.txt")

# Reference year for CPI adjustment
REF_YEAR = 2026

# ---------------------------------------------------------------------------
# Spain CPI index — base 2021 = 100
# Annual average (INE). 2026 estimated to April.
# ---------------------------------------------------------------------------
SPAIN_CPI: dict[int, float] = {
    2015: 82.5,
    2016: 83.0,
    2017: 85.1,
    2018: 87.5,
    2019: 88.2,
    2020: 87.7,
    2021: 100.0,
    2022: 109.4,
    2023: 113.8,
    2024: 117.1,
    2025: 119.5,
    2026: 121.0,
}

# ---------------------------------------------------------------------------
# FX rates: approximate average mid-year rates for foreign currencies → EUR.
# Used to convert non-EUR salaries to EUR before inflation adjustment.
# Sources: ECB historical data (averages per year).
# ---------------------------------------------------------------------------
FX_TO_EUR: dict[tuple[str, int], float] = {
    # (currency, year): EUR per 1 unit of currency
    # CAD
    ("CAD", 2017): 0.685, ("CAD", 2018): 0.669, ("CAD", 2019): 0.670,
    ("CAD", 2020): 0.660, ("CAD", 2021): 0.680, ("CAD", 2022): 0.720,
    ("CAD", 2023): 0.695, ("CAD", 2024): 0.680, ("CAD", 2025): 0.660,
    ("CAD", 2026): 0.650,
    # GBP
    ("GBP", 2017): 1.141, ("GBP", 2018): 1.130, ("GBP", 2019): 1.140,
    ("GBP", 2020): 1.125, ("GBP", 2021): 1.163, ("GBP", 2022): 1.172,
    ("GBP", 2023): 1.150, ("GBP", 2024): 1.178, ("GBP", 2025): 1.180,
    ("GBP", 2026): 1.175,
    # USD
    ("USD", 2017): 0.887, ("USD", 2018): 0.848, ("USD", 2019): 0.893,
    ("USD", 2020): 0.877, ("USD", 2021): 0.845, ("USD", 2022): 0.954,
    ("USD", 2023): 0.925, ("USD", 2024): 0.927, ("USD", 2025): 0.920,
    ("USD", 2026): 0.910,
}

# ---------------------------------------------------------------------------
# City normalization: raw ciudad → (ciudad_norm, modalidad, pais)
# modalidad: Presencial | Remoto | Híbrido | None (unknown)
# pais: España | Extranjero
# ---------------------------------------------------------------------------

CIUDAD_MAP: dict[str, tuple[str | None, str | None, str]] = {
    # ── Pure remote (no city specified) ────────────────────────────────────
    "100% Remoto":                              ("Remoto", "Remoto", "España"),
    "100% Remoto para empresa de Holanda":      ("Remoto", "Remoto", "España"),
    "100% Remoto.":                             ("Remoto", "Remoto", "España"),
    "100% remote":                              ("Remoto", "Remoto", "España"),
    "100% remoto":                              ("Remoto", "Remoto", "España"),
    "100% remoto.":                             ("Remoto", "Remoto", "España"),
    "100% tele trabajo para empresa española, cliente": ("Remoto", "Remoto", "España"),
    "100% teletrabajo":                         ("Remoto", "Remoto", "España"),
    "Full remoto":                              ("Remoto", "Remoto", "España"),
    "Hibrido (3 Remoto + 2 Ofi)":              ("Remoto", "Híbrido", "España"),
    "Provincia pequeña pero 100% remoto para una cárnica": ("Remoto", "Remoto", "España"),
    "Remoto":                                   ("Remoto", "Remoto", "España"),
    "Remoto (2 dias al mes oficina)":           ("Remoto", "Híbrido", "España"),
    "Remoto / Mi casa en españita":             ("Remoto", "Remoto", "España"),
    "Remoto 100%":                              ("Remoto", "Remoto", "España"),
    "Remoto 100% especificado en contrato.":    ("Remoto", "Remoto", "España"),
    "Remoto desde un pueblo de 20k habitantes": ("Remoto", "Remoto", "España"),
    "Remoto en españa":                         ("Remoto", "Remoto", "España"),
    "remote":                                   ("Remoto", "Remoto", "España"),
    "remoto":                                   ("Remoto", "Remoto", "España"),
    "remoto (empresa en Alemania)":             ("Remoto", "Remoto", "España"),
    "teletrabajando para una startup con base en EEUU": ("Remoto", "Remoto", "España"),
    "Empresa de Barcelona, 100% remoto desde otra provincia": ("Remoto", "Remoto", "España"),
    "Estoy en remoto, empresa en Málaga.":      ("Remoto", "Remoto", "España"),
    "todas y ninguna":                          (None, None, "España"),

    # ── Madrid ─────────────────────────────────────────────────────────────
    "4 remoto 1 madrid":                        ("Madrid", "Híbrido", "España"),
    "Madrid":                                   ("Madrid", None, "España"),
    "Madrid (Malaga 100% remoto)":              ("Málaga", "Remoto", "España"),
    "Madrid (teletrabajando para una empresa de Badajoz)": ("Madrid", "Remoto", "España"),
    "Madrid aunque es remoto 100%":             ("Madrid", "Remoto", "España"),
    "Madrid híbrido, 3 días de oficina por semana.": ("Madrid", "Híbrido", "España"),
    "Madrid, Híbrido":                          ("Madrid", "Híbrido", "España"),
    "Madrid, pero el puesto es full remote (empresa europea)": ("Madrid", "Remoto", "España"),
    "Madrid. (3 días teletrabajo 2 presencial)": ("Madrid", "Híbrido", "España"),

    # ── Barcelona ──────────────────────────────────────────────────────────
    "Barcelona":                                ("Barcelona", None, "España"),
    "Barcelona (4 días a la semana remoto)":    ("Barcelona", "Híbrido", "España"),
    "Barcelona/Remoto":                         ("Barcelona", "Híbrido", "España"),
    "Bcn":                                      ("Barcelona", None, "España"),
    "Bcn (Remoto, 1 día cada 15 días a la oficina)": ("Barcelona", "Híbrido", "España"),
    "Belfast (Remoto desde Barcelona)":         ("Barcelona", "Remoto", "España"),
    "Remoto 100% aunque a veces voy a bcn.":   ("Barcelona", "Remoto", "España"),
    "Sant Cugat del Vallès 100 % presencial.": ("Barcelona", "Presencial", "España"),
    "barcelona (proximamente ho chi minh city)": ("Barcelona", None, "España"),
    "bcn":                                      ("Barcelona", None, "España"),
    "Cáceres, para una empresa de Barcelona":   ("Cáceres", None, "España"),
    "Las Palmas de GC (viviendo ahora en Barcelona)": ("Barcelona", None, "España"),

    # ── Valencia ───────────────────────────────────────────────────────────
    "Valencia":                                 ("Valencia", None, "España"),
    "Valencia (podría ser remoto 100%)":        ("Valencia", "Remoto", "España"),
    "Valencia (remoto 100%)":                   ("Valencia", "Remoto", "España"),
    "Valencia full remote":                     ("Valencia", "Remoto", "España"),
    "full remote, pero sede en Valencia por si tal": ("Valencia", "Remoto", "España"),
    "Castellón":                                ("Castellón", None, "España"),

    # ── Sevilla ────────────────────────────────────────────────────────────
    "Sevilla":                                  ("Sevilla", None, "España"),
    "Sevilla (Híbrido. 1d cada 2 semanas)":     ("Sevilla", "Híbrido", "España"),
    "Sevilla (Remoto)":                         ("Sevilla", "Remoto", "España"),
    "Sevilla (aquí comes en un bar por 5€)":    ("Sevilla", None, "España"),

    # ── Málaga ─────────────────────────────────────────────────────────────
    "Málaga":                                   ("Málaga", None, "España"),
    "Málaga (100% remoto con posibilidad de ir a la oficina)": ("Málaga", "Remoto", "España"),
    "Málaga, en el PTA.":                       ("Málaga", "Presencial", "España"),
    "Málaga, híbrido (WFO 2, WFH 3)":          ("Málaga", "Híbrido", "España"),
    "Málaga.":                                  ("Málaga", None, "España"),

    # ── Zaragoza ───────────────────────────────────────────────────────────
    "Zaragoza":                                 ("Zaragoza", None, "España"),
    "Remoto Zaragoza":                          ("Zaragoza", "Remoto", "España"),

    # ── Alicante ───────────────────────────────────────────────────────────
    "Alicante":                                 ("Alicante", None, "España"),
    "Interior de Alicante":                     ("Alicante", None, "España"),
    "Provincia de Alicante":                    ("Alicante", None, "España"),
    "Remoto para Begica desde Alicante":        ("Alicante", "Remoto", "España"),

    # ── Palma de Mallorca ──────────────────────────────────────────────────
    "Mallorca (Es full remote, así que podría irme fuera)": ("Palma de Mallorca", "Remoto", "España"),
    "Mallorca / Ibiza":                         ("Palma de Mallorca", None, "España"),
    "Mallorca, presencial":                     ("Palma de Mallorca", "Presencial", "España"),
    "Palma":                                    ("Palma de Mallorca", None, "España"),
    "Palma de Mallorca":                        ("Palma de Mallorca", None, "España"),
    "estoy en Palma (en remoto para la peninsula)": ("Palma de Mallorca", "Remoto", "España"),

    # ── Las Palmas ─────────────────────────────────────────────────────────
    "Las Palmas":                               ("Las Palmas", None, "España"),
    "Las Palmas de G.C":                        ("Las Palmas", None, "España"),
    "Las Palmas de Gran Canaria":               ("Las Palmas", None, "España"),

    # ── Murcia ─────────────────────────────────────────────────────────────
    "Murcia":                                   ("Murcia", None, "España"),
    "Murcia (100% remoto a Madrid)":            ("Murcia", "Remoto", "España"),

    # ── Other Spanish cities ───────────────────────────────────────────────
    "Almería":                                  ("Almería", None, "España"),
    "Roquetas de mar (remoto)":                 ("Almería", "Remoto", "España"),
    "Córdoba":                                  ("Córdoba", None, "España"),
    "Córdoba (remoto)":                         ("Córdoba", "Remoto", "España"),
    "Granada / trabajo en remoto":              ("Granada", "Remoto", "España"),
    "Girona (híbrido)":                         ("Girona", "Híbrido", "España"),
    "Ourense":                                  ("Ourense", None, "España"),
    "Ourense (Remoto 100%)":                    ("Ourense", "Remoto", "España"),
    "Salamanca":                                ("Salamanca", None, "España"),
    "salamanca":                                ("Salamanca", None, "España"),
    "Santander":                                ("Santander", None, "España"),
    "Segovia":                                  ("Segovia", None, "España"),
    "Reus":                                     ("Reus", None, "España"),
    "Tortosa":                                  ("Tortosa", None, "España"),
    "Ciudad Real":                              ("Ciudad Real", None, "España"),
    "Ciudad Real, pero viviendo en un pueblo de 2k": ("Ciudad Real", None, "España"),
    "Remoto desde Tenerife":                    ("Tenerife", "Remoto", "España"),

    # ── Spanish regions (no specific city) ─────────────────────────────────
    "Andalucía":                                ("Andalucía", None, "España"),
    "Cataluña":                                 ("Cataluña", None, "España"),

    # ── Foreign ────────────────────────────────────────────────────────────
    "Alemania":                                 ("Alemania", None, "Extranjero"),
    "Berlin":                                   ("Berlín", None, "Extranjero"),
    "Colonia":                                  ("Colonia", None, "Extranjero"),
    "Munich":                                   ("Múnich", None, "Extranjero"),
    "Cracovia":                                 ("Cracovia", None, "Extranjero"),
    "Dublin":                                   ("Dublín", None, "Extranjero"),
    "Dublin (100% remoto, la empresa es de Madrid)": ("Dublín", "Remoto", "Extranjero"),
    "Irlanda":                                  ("Irlanda", None, "Extranjero"),
    "Londres":                                  ("Londres", None, "Extranjero"),
    "Manchester":                               ("Manchester", None, "Extranjero"),
    "UK":                                       ("UK", None, "Extranjero"),
    "uk":                                       ("UK", None, "Extranjero"),
    "Lucerna (Suiza)":                          ("Lucerna", None, "Extranjero"),
    "Zurich, Suiza.":                           ("Zúrich", None, "Extranjero"),
    "Quebec":                                   ("Quebec", None, "Extranjero"),
    "Riyadh, Arabia Saudi":                     ("Riyadh", None, "Extranjero"),
    "Remote(EEUU)":                             ("EEUU", "Remoto", "Extranjero"),
    "Empleador EEUU":                           ("EEUU", "Remoto", "Extranjero"),
    "costa este EEUU (3 dias en oficina / 2 remoto)": ("EEUU", "Híbrido", "Extranjero"),
    "países bajos":                             ("Países Bajos", None, "Extranjero"),
}


def normalize_ciudad(raw: str | None) -> tuple[str | None, str | None, str | None]:
    """Return (ciudad_norm, modalidad, pais) for a raw ciudad string."""
    if raw is None:
        return None, None, None

    if raw in CIUDAD_MAP:
        return CIUDAD_MAP[raw]

    # Heuristic fallback for values not in the map
    low = raw.lower()

    has_remote = any(k in low for k in ("remoto", "remote", "teletrabaj"))
    has_hybrid = any(k in low for k in ("híbrido", "hibrido"))
    has_presencial = "presencial" in low

    if has_hybrid or (has_remote and has_presencial):
        modalidad: str | None = "Híbrido"
    elif has_remote:
        modalidad = "Remoto"
    elif has_presencial:
        modalidad = "Presencial"
    else:
        modalidad = None

    foreign = ("eeuu", "usa", "uk", "reino unido", "alemania", "germany",
               "francia", "france", "suiza", "switzerland", "irlanda",
               "ireland", "holanda", "países bajos", "portugal", "italia")
    pais = "Extranjero" if any(k in low for k in foreign) else "España"

    print(f"  ⚠ Ciudad sin mapear: {raw!r}")
    return raw, modalidad, pais


# ---------------------------------------------------------------------------
# Neto → Bruto conversion table (Spain IRPF approximation, 2020-2026)
# These are simplified marginal multipliers; the mapping is non-linear.
# ---------------------------------------------------------------------------
def neto_to_bruto(neto: float) -> float:
    """Approximate conversion from annual net to annual gross (Spain IRPF)."""
    if neto < 12_000:
        return neto * 1.15
    elif neto < 15_000:
        return neto * 1.18
    elif neto < 20_000:
        return neto * 1.22
    elif neto < 25_000:
        return neto * 1.27
    elif neto < 30_000:
        return neto * 1.32
    elif neto < 40_000:
        return neto * 1.38
    elif neto < 55_000:
        return neto * 1.44
    else:
        return neto * 1.50


def cpi_for_year(year: int) -> float:
    """Return CPI index for a given year. Extrapolate if out of range."""
    if year in SPAIN_CPI:
        return SPAIN_CPI[year]
    if year < min(SPAIN_CPI):
        return SPAIN_CPI[min(SPAIN_CPI)]
    if year > max(SPAIN_CPI):
        return SPAIN_CPI[max(SPAIN_CPI)]
    # Linear interpolation between nearest years
    years = sorted(SPAIN_CPI)
    for i in range(len(years) - 1):
        y0, y1 = years[i], years[i + 1]
        if y0 <= year <= y1:
            t = (year - y0) / (y1 - y0)
            return SPAIN_CPI[y0] + t * (SPAIN_CPI[y1] - SPAIN_CPI[y0])
    return SPAIN_CPI[year]


def fx_to_eur(moneda: str, year: int, valor: float) -> float:
    """Convert a salary value in moneda to EUR using approximate historical rate."""
    if moneda == "EUR":
        return valor
    rate = FX_TO_EUR.get((moneda, year))
    if rate is None:
        # Fallback: nearest available year
        available = [y for (m, y) in FX_TO_EUR if m == moneda]
        if not available:
            return valor  # unknown currency, leave as-is
        nearest = min(available, key=lambda y: abs(y - year))
        rate = FX_TO_EUR[(moneda, nearest)]
    return valor * rate


# ---------------------------------------------------------------------------
# Process row-by-row (Python UDF — small dataset, performance not critical)
# ---------------------------------------------------------------------------

def harmonize_row(
    salario_valor: float,
    es_bruto: bool | None,
    frecuencia: str | None,
    moneda: str,
    year: int,
) -> tuple[float | None, bool, str]:
    """
    Returns (salario_bruto_anual_eur, conversion_aplicada, nota)
    """
    if salario_valor is None or salario_valor <= 0:
        return None, False, "valor_nulo"

    val = salario_valor
    conversion = False
    nota = ""

    # 1. Infer frequency if unknown
    freq = frecuencia
    if freq is None:
        if val < 6_000:
            freq = "mensual"
        else:
            freq = "anual"
        nota += f"freq_inferida={freq};"

    # 2. Convert to annual
    if freq == "mensual":
        val = val * 12
        nota += "×12;"

    # 3. Convert foreign currency to EUR
    if moneda != "EUR":
        val = fx_to_eur(moneda, year, val)
        nota += f"fx_{moneda}→EUR;"

    # 4. Convert neto → bruto if known to be neto
    if es_bruto is False:
        val = neto_to_bruto(val)
        conversion = True
        nota += "neto→bruto;"

    # 5. Sanity filter
    if val < 8_000 or val > 250_000:
        return None, conversion, f"fuera_de_rango({val:.0f});" + nota

    return round(val, 2), conversion, nota.strip(";")


def main():
    df = pl.read_parquet(IN_DEDUP)
    print(f"Rows in dedup: {len(df)}")

    # Fix CAD/USD misclassification: any row where moneda=USD and text contains
    # "canadiense" should be CAD
    df = df.with_columns(
        pl.when(
            (pl.col("moneda") == "USD") & pl.col("texto").str.contains("(?i)canadiense")
        )
        .then(pl.lit("CAD"))
        .otherwise(pl.col("moneda"))
        .alias("moneda")
    )

    # Extract year from fecha
    df = df.with_columns(
        pl.col("fecha").dt.year().alias("year")
    )

    # Normalize cities → canonical name, modalidad, pais
    df = df.rename({"ciudad": "ciudad_raw"})
    norm = [normalize_ciudad(v) for v in df["ciudad_raw"].to_list()]
    ciudades, modalidades, paises = (list(x) for x in zip(*norm)) if norm else ([], [], [])
    df = df.with_columns(
        pl.Series("ciudad", ciudades, dtype=pl.Utf8),
        pl.Series("modalidad", modalidades, dtype=pl.Utf8),
        pl.Series("pais", paises, dtype=pl.Utf8),
    )

    # Apply harmonization (Python UDF via map_elements on each row)
    results = []
    for row in df.iter_rows(named=True):
        bruto_anual, conv, nota = harmonize_row(
            salario_valor=row["salario_valor"],
            es_bruto=row["es_bruto"],
            frecuencia=row["frecuencia"],
            moneda=row["moneda"],
            year=row["year"] or 2020,
        )
        results.append({
            "salario_bruto_anual": bruto_anual,
            "conversion_aplicada": conv,
            "nota_harmonizacion": nota,
        })

    harmonized = pl.DataFrame(results)
    df = pl.concat([df, harmonized], how="horizontal")

    # Apply CPI inflation adjustment
    cpi_ref = cpi_for_year(REF_YEAR)

    inflation_vals = []
    for row in df.iter_rows(named=True):
        sba = row["salario_bruto_anual"]
        year = row["year"] or 2020
        if sba is None:
            inflation_vals.append(None)
        else:
            cpi_post = cpi_for_year(year)
            adjusted = round(sba * (cpi_ref / cpi_post), 2)
            inflation_vals.append(adjusted)

    df = df.with_columns(
        pl.Series("salario_bruto_2026", inflation_vals, dtype=pl.Float64)
    )

    # Remove rows where harmonization failed (out-of-range, null, etc.)
    df_clean = df.filter(pl.col("salario_bruto_anual").is_not_null())
    df_outliers = df.filter(pl.col("salario_bruto_anual").is_null())
    print(f"Filas válidas: {len(df_clean)}  |  Descartadas (fuera rango/nulas): {len(df_outliers)}")

    if len(df_outliers) > 0:
        print("Descartadas:")
        for r in df_outliers.select(["autor", "salario_raw", "nota_harmonizacion"]).iter_rows(named=True):
            print(f"  @{r['autor']}: {r['salario_raw']} → {r['nota_harmonizacion']}")

    # Select and order final columns
    final = df_clean.select([
        "autor",
        "fecha",
        "year",
        "post_num",
        "pagina",
        "salario_bruto_anual",
        "salario_bruto_2026",
        "salario_valor",
        "salario_raw",
        "es_bruto",
        "frecuencia",
        "moneda",
        "conversion_aplicada",
        "nota_harmonizacion",
        "ciudad",
        "ciudad_raw",
        "modalidad",
        "pais",
        "experiencia_anos",
        "tecnologia",
        "texto",
    ]).sort("salario_bruto_2026", descending=True)

    final.write_csv(OUT_CSV)
    final.write_parquet(OUT_PARQUET)
    print(f"\nGuardado: {OUT_CSV}, {OUT_PARQUET}")

    # ---------------------------------------------------------------------------
    # Descriptive statistics
    # ---------------------------------------------------------------------------
    stats_lines = []
    add = stats_lines.append

    add("=" * 60)
    add("TABLA SALARIAL PROGRAMADORES ESPAÑA — MediaVida")
    add(f"Fuente: mediavida.com/foro thread #596068  |  Ref: €{REF_YEAR}")
    add("=" * 60)
    add("")

    vals = final["salario_bruto_2026"].drop_nulls()
    n = len(vals)
    add(f"N (respuestas válidas con dato, deduplicadas por usuario): {n}")
    add(f"Período cubierto: {final['fecha'].min()} → {final['fecha'].max()}")
    add("")
    add("--- Salario Bruto Anual ajustado a €2026 (IPC España) ---")
    add(f"  Mediana:  {vals.median():>10,.0f} €")
    add(f"  Media:    {vals.mean():>10,.0f} €")
    add(f"  P10:      {vals.quantile(0.10):>10,.0f} €")
    add(f"  P25:      {vals.quantile(0.25):>10,.0f} €")
    add(f"  P75:      {vals.quantile(0.75):>10,.0f} €")
    add(f"  P90:      {vals.quantile(0.90):>10,.0f} €")
    add(f"  Min:      {vals.min():>10,.0f} €")
    add(f"  Max:      {vals.max():>10,.0f} €")
    add(f"  Desv.std: {vals.std():>10,.0f} €")
    add("")

    add("--- Salario Bruto Anual ORIGINAL (sin ajuste inflación) ---")
    orig = final["salario_bruto_anual"].drop_nulls()
    add(f"  Mediana:  {orig.median():>10,.0f} €")
    add(f"  Media:    {orig.mean():>10,.0f} €")
    add(f"  P25:      {orig.quantile(0.25):>10,.0f} €")
    add(f"  P75:      {orig.quantile(0.75):>10,.0f} €")
    add("")

    add("--- Distribución por año de post ---")
    by_year = (
        final
        .group_by("year")
        .agg([
            pl.len().alias("n"),
            pl.col("salario_bruto_anual").median().round(0).alias("mediana_original"),
            pl.col("salario_bruto_2026").median().round(0).alias("mediana_2026"),
        ])
        .sort("year")
    )
    add(f"  {'Año':<6} {'N':>5} {'Mediana orig.€':>15} {'Mediana €2026':>14}")
    for row in by_year.iter_rows(named=True):
        add(f"  {row['year']:<6} {row['n']:>5} {row['mediana_original']:>15,.0f} {row['mediana_2026']:>14,.0f}")
    add("")

    add("--- Top ciudades (N ≥ 3) ---")
    by_city = (
        final.filter(pl.col("ciudad").is_not_null())
        .group_by("ciudad")
        .agg([
            pl.len().alias("n"),
            pl.col("salario_bruto_2026").median().round(0).alias("mediana_2026"),
        ])
        .filter(pl.col("n") >= 3)
        .sort("mediana_2026", descending=True)
    )
    add(f"  {'Ciudad':<30} {'N':>4} {'Mediana €2026':>14}")
    for row in by_city.iter_rows(named=True):
        add(f"  {row['ciudad']:<30} {row['n']:>4} {row['mediana_2026']:>14,.0f}")
    add("")

    add("--- Transparencia del dato ---")
    bruto_known = final.filter(pl.col("es_bruto").is_not_null())
    bruto_true = final.filter(pl.col("es_bruto") == True)
    neto_true = final.filter(pl.col("es_bruto") == False)
    add(f"  Bruto explícito:    {len(bruto_true):>4} ({100*len(bruto_true)/n:.1f}%)")
    add(f"  Neto explícito:     {len(neto_true):>4} ({100*len(neto_true)/n:.1f}%)")
    add(f"  No especificado:    {n - len(bruto_known):>4} ({100*(n - len(bruto_known))/n:.1f}%)  ← asumido bruto")
    add(f"  Con conversión n→b: {final['conversion_aplicada'].sum():>4}")
    add("")
    add(f"  Frecuencia explícita anual:   {len(final.filter(pl.col('frecuencia')=='anual')):>4}")
    add(f"  Frecuencia explícita mensual: {len(final.filter(pl.col('frecuencia')=='mensual')):>4}")
    add(f"  Frecuencia inferida:          {len(final.filter(pl.col('nota_harmonizacion').str.contains('freq_inferida', literal=True))):>4}")
    add("")
    add(f"  Moneda EUR:  {len(final.filter(pl.col('moneda')=='EUR')):>4}")
    add(f"  Moneda CAD:  {len(final.filter(pl.col('moneda')=='CAD')):>4}")
    add(f"  Moneda GBP:  {len(final.filter(pl.col('moneda')=='GBP')):>4}")
    add(f"  Moneda USD:  {len(final.filter(pl.col('moneda')=='USD')):>4}")
    add("")

    add("--- Modalidad ---")
    for m in ("Presencial", "Híbrido", "Remoto"):
        cnt = len(final.filter(pl.col("modalidad") == m))
        add(f"  {m:<15} {cnt:>4} ({100*cnt/n:.1f}%)")
    cnt_null = len(final.filter(pl.col("modalidad").is_null()))
    add(f"  {'No indicado':<15} {cnt_null:>4} ({100*cnt_null/n:.1f}%)")
    add("")

    add("--- País ---")
    for p in ("España", "Extranjero"):
        cnt = len(final.filter(pl.col("pais") == p))
        add(f"  {p:<15} {cnt:>4} ({100*cnt/n:.1f}%)")
    add("")

    add("--- Top 20 salarios más altos (€2026) ---")
    add(f"  {'Usuario':<20} {'Año':>5} {'Ciudad':<20} {'Bruto orig.€':>13} {'€2026':>10}")
    for row in final.head(20).iter_rows(named=True):
        ciudad = (row["ciudad"] or "-")[:18]
        add(
            f"  {row['autor']:<20} {row['year']:>5} {ciudad:<20} "
            f"{row['salario_bruto_anual']:>13,.0f} {row['salario_bruto_2026']:>10,.0f}"
        )
    add("")

    stats_text = "\n".join(stats_lines)
    OUT_STATS.write_text(stats_text, encoding="utf-8")
    print(stats_text)


if __name__ == "__main__":
    main()
