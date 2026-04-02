"""
Parse posts_raw.json → extract salary data per post → deduplicate by user.

Inputs:  posts_raw.json
Outputs: posts_with_salary.parquet   — all posts with extraction columns
         salarios_dedup.parquet      — one row per user (latest post with salary)
         extraction_review.txt       — sample of extracted rows for manual review
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import polars as pl

INPUT = Path("posts_raw.json")
OUT_SALARY = Path("posts_with_salary.parquet")
OUT_DEDUP = Path("salarios_dedup.parquet")
OUT_REVIEW = Path("extraction_review.txt")

# ---------------------------------------------------------------------------
# Number parsing
# ---------------------------------------------------------------------------

def parse_number(raw: str) -> float | None:
    """
    Parse Spanish-format salary numbers:
      "15.000" → 15000.0
      "15,5"   → 15.5   (decimal comma)
      "15,000" → 15000.0 (thousands comma)
      "15k"    → 15000.0
      "15K"    → 15000.0
    """
    s = raw.strip()
    k_mult = 1
    if s.lower().endswith("k"):
        k_mult = 1000
        s = s[:-1]

    # Determine if comma is decimal or thousands separator
    if "." in s and "," in s:
        # e.g. "15.000,50" → European format → remove dots, replace comma
        s = s.replace(".", "").replace(",", ".")
    elif "." in s:
        # Could be thousands: "15.000" or decimal: "1.5"
        parts = s.split(".")
        if len(parts) == 2 and len(parts[1]) == 3:
            # Thousands separator: "15.000"
            s = s.replace(".", "")
        # else keep as decimal: "1.5"
    elif "," in s:
        parts = s.split(",")
        if len(parts) == 2 and len(parts[1]) == 3:
            # Thousands separator: "15,000"
            s = s.replace(",", "")
        else:
            # Decimal comma: "15,5" → "15.5"
            s = s.replace(",", ".")

    try:
        return float(s) * k_mult
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Salary extraction
# ---------------------------------------------------------------------------

# Matches a numeric salary token (with optional K suffix)
_NUM = r"(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{1,2})?|\d+(?:[.,]\d+)?)\s*[kK]?"

# Build a combined pattern that captures:
#   group 1 = the leading label (salario/sueldo/sb/cobro/gano/etc.) — optional
#   group 2 = the number
#   group 3 = optional k/K right after number
#   group 4 = currency symbol (€ or $) — may appear before or after
#   group 5 = period qualifier (/año, /mes, al año, al mes, anuales, mensuales, brutos, netos)

SALARY_RE = re.compile(
    r"""
    (?:
        # Labeled: "Salario: 15k" | "SB: 15.000€" | "Sueldo: 1.800€/mes"
        (?:salario\s*bruto|salario\s*neto|salario\w*|sueldo\w*|s\.?b\.?|s\.?n\.?|cobro|gano|gana(?:ba)?|me\s+pagan|me\s+paga(?:ban)?|percibo|ingreso|remuneraci[oó]n)
        \s*[:\-=]?\s*
    )?
    (?:€\s*)?                             # currency before number
    (\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{1,2})?[kK]?|\d{2,6}(?:[.,]\d+)?[kK]?)  # number (group 1)
    \s*
    (€|euros?)?                            # currency after number (group 2)
    \s*
    (brut[oa]s?|net[oa]s?|brutos?\s*anuales?|netos?\s*anuales?)?  # bruto/neto (group 3)
    \s*
    (al\s+año|al\s+mes|por\s+mes|\/año|\/mes|anuales?|mensuales?|al\s+año\s+brut[oa])?  # period (group 4)
    """,
    re.IGNORECASE | re.VERBOSE,
)

# Simpler targeted patterns for the most common structured formats
PATTERNS = [
    # "Salario: 15k" | "Salario: 15.000€" | "Salario: 15.000€/año"
    re.compile(
        r"(?:salario|sueldo|s\.?b\.?|sb|salary)\s*(?:bruto|neto|actual|aproximado|actual)?\s*[:\-=]\s*"
        r"(€\s*)?(\d[\d.,]*[kK]?)\s*(€|euros?)?\s*(brut[oa]s?|net[oa]s?)?\s*(anuales?|mensuales?|al\s+año|al\s+mes|\/año|\/mes)?",
        re.I,
    ),
    # "cobro/gano/me pagan X€"
    re.compile(
        r"(?:cobro|gano|me\s+pagan?|percibo|ingreso)\s+"
        r"(€\s*)?(\d[\d.,]*[kK]?)\s*(€|euros?)?\s*(brut[oa]s?|net[oa]s?)?\s*(anuales?|mensuales?|al\s+año|al\s+mes|\/año|\/mes)?",
        re.I,
    ),
    # "X€ brutos/netos [anuales/al año]"
    re.compile(
        r"(€\s*)?(\d[\d.,]*[kK]?)\s*(€|euros?)\s*(brut[oa]s?|net[oa]s?)\s*(anuales?|mensuales?|al\s+año|al\s+mes|\/año|\/mes)?",
        re.I,
    ),
    # "Xk brutos" | "Xk netos"
    re.compile(
        r"(\d[\d.,]*[kK])\s*(brut[oa]s?|net[oa]s?)\s*(anuales?|mensuales?|al\s+año|al\s+mes)?",
        re.I,
    ),
    # "Xk anuales" | "X€/año" | "X€/mes"
    re.compile(
        r"(\d[\d.,]*[kK]?)\s*(€|euros?)?\s*(anuales?|al\s+año|\/año|mensuales?|al\s+mes|\/mes)",
        re.I,
    ),
]

# "Salario: X" line pattern — very common structured format in this thread
LABEL_LINE_RE = re.compile(
    r"^(?:salario|sueldo|s\.?b\.?|sb)\s*(?:bruto|neto|actual)?\s*[:\-=]\s*(.+)$",
    re.I | re.MULTILINE,
)


def _is_template_post(texto: str) -> bool:
    """
    Detect structured "template" posts that contain labeled fields like:
      Tecnología: X / Ciudad: Y / Salario: Z
    These are almost always personal salary reports.
    """
    labels = re.findall(
        r"^(?:tecnolog[ií]as?|tec|ciudad|city|salario|sueldo|sb|experiencia|exp|estudios|formaci[oó]n)\s*[:\-=]",
        texto,
        re.I | re.MULTILINE,
    )
    return len(labels) >= 2


def _detect_currency_local(texto: str, match_start: int) -> str:
    """
    Detect currency from a ±150 char window around the salary match.
    Defaults to EUR (this is a Spanish forum).
    """
    window_start = max(0, match_start - 150)
    window_end = min(len(texto), match_start + 150)
    window = texto[window_start:window_end]

    if re.search(r"d[oó]lares?\s*\(?\s*canadienses?\)?|\bCAD\b|\bCA\$", window, re.I):
        return "CAD"
    if re.search(r"\blibras?\b|\bGBP\b|£", window, re.I):
        return "GBP"
    if re.search(r"\bd[oó]lares?\b|\bUSD\b|\$\d", window, re.I):
        return "USD"
    return "EUR"


def _is_year(val: float, raw: str) -> bool:
    """Reject bare 4-digit numbers that look like calendar years."""
    return (
        2010 <= val <= 2030
        and not re.search(r"[kK€$£]", raw)
        and val == int(val)
    )


def extract_salary(texto: str) -> dict:
    """
    Returns dict with keys:
      tiene_dato: bool
      salario_raw: str | None       raw matched text
      salario_valor: float | None   numeric value extracted
      es_bruto: bool | None         True=bruto, False=neto, None=unknown
      frecuencia: str | None        'anual' | 'mensual' | None
      moneda: str                   'EUR' | 'CAD' | 'GBP' | 'USD' | 'OTHER'
    """
    if not texto:
        return _no_dato()

    is_template = _is_template_post(texto)

    # Try labeled line first: "Salario: 15k" — most reliable
    m = LABEL_LINE_RE.search(texto)
    if m:
        line_val = m.group(1).strip()
        moneda = _detect_currency_local(texto, m.start())
        result = _parse_salary_token(line_val, moneda, in_label=True)
        if result["tiene_dato"]:
            return result

    # Try each pattern
    for pat in PATTERNS:
        m = pat.search(texto)
        if m:
            moneda = _detect_currency_local(texto, m.start())
            result = _parse_from_match(m, moneda)
            if result["tiene_dato"]:
                # For non-template posts, only accept if the match looks
                # like a first-person salary report, not quoting others
                if not is_template:
                    ctx_start = max(0, m.start() - 80)
                    context_before = texto[ctx_start:m.start()].lower()
                    # Reject third-person / hypothetical patterns
                    if re.search(
                        r"gente\s+cobr|se\s+cobr|te\s+pag|un\s+amigo|su\s+novi|"
                        r"facturando|cobrar\s*$|pagar\s*$|media\s+de|media\s+es|"
                        r"promedio|alguien|la\s+gente|en\s+general|"
                        r"como\s+para\s+cobrar|sabido\s+mover",
                        context_before,
                    ):
                        continue
                return result

    return _no_dato()


def _no_dato() -> dict:
    return {
        "tiene_dato": False,
        "salario_raw": None,
        "salario_valor": None,
        "es_bruto": None,
        "frecuencia": None,
        "moneda": "EUR",
    }


def _parse_salary_token(token: str, moneda: str, in_label: bool = False) -> dict:
    """
    Parse a salary value string like:
    "15k", "15.000€/año", "1.800€ al mes", "28k brutos", "muchos ceros", etc.

    in_label=True means this came from a "Salario: X" line, where bare numbers
    like "25" almost certainly mean "25k".
    """
    # Reject tokens where the "salary" is obviously non-numeric text.
    # Only reject if there's NO digit at all, or the entire value is a
    # rejection word (not if it's context after a number like "60k + variable").
    if not re.search(r"\d", token):
        return _no_dato()
    # Reject if the token is essentially just a non-answer
    first_word = token.split()[0].lower() if token.split() else ""
    if first_word in ("mucho", "muchos", "varios", "bastante", "variable", "negociable", "ns/nc"):
        return _no_dato()
    if re.search(r"sin\s+dato|no\s+cobr|d[ií]gitos?\b", token, re.I):
        return _no_dato()

    # Extract number
    num_m = re.search(r"(\d[\d.,]*[kK]?)", token)
    if not num_m:
        return _no_dato()

    raw_num = num_m.group(1)
    val = parse_number(raw_num)
    if val is None or val < 1:
        return _no_dato()

    # Reject calendar years: bare 2015-2030 without k/€
    if _is_year(val, raw_num):
        return _no_dato()

    # Shorthand: "Salario: 25" in a label context means 25k
    # Apply when the number is bare (no k/€) and in plausible salary range 10-200
    if in_label and 10 <= val <= 200 and not re.search(r"[kK€$£]", raw_num):
        val = val * 1000

    # bruto/neto
    es_bruto = None
    if re.search(r"brut", token, re.I):
        es_bruto = True
    elif re.search(r"net", token, re.I):
        es_bruto = False

    # frequency — be strict: "al mes" / "/mes" / "mensuales" are monthly,
    # but "a partir de este mes" or "el mes que viene" are NOT monthly salary
    frecuencia = None
    if re.search(r"anuales?|al\s+año|\/año", token, re.I):
        frecuencia = "anual"
    elif re.search(r"mensuales?|al\s+mes|\/mes", token, re.I):
        # Reject false triggers: "a partir de este mes", "el mes pasado", etc.
        if not re.search(r"(?:a\s+partir|este|pasado|pr[oó]ximo|el)\s+mes", token, re.I):
            frecuencia = "mensual"

    # In a salary label, if there's a range like "34K -> 38k" or "60-70K", take the last number
    if in_label:
        range_m = re.search(r"(\d[\d.,]*[kK]?)\s*(?:->|→|-)\s*(\d[\d.,]*[kK])", token, re.I)
        if range_m:
            last_val = parse_number(range_m.group(2))
            if last_val is not None and last_val > 0:
                val = last_val

    return {
        "tiene_dato": True,
        "salario_raw": token[:100],
        "salario_valor": val,
        "es_bruto": es_bruto,
        "frecuencia": frecuencia,
        "moneda": moneda,
    }


def _parse_from_match(m: re.Match, moneda: str) -> dict:
    groups = [g for g in m.groups() if g is not None]
    full = m.group(0)

    # Find the numeric group
    num_m = re.search(r"(\d[\d.,]*[kK]?)", full)
    if not num_m:
        return _no_dato()

    raw_num = num_m.group(1)
    val = parse_number(raw_num)
    if val is None or val < 1:
        return _no_dato()

    # Reject calendar years
    if _is_year(val, raw_num):
        return _no_dato()

    es_bruto = None
    if re.search(r"brut", full, re.I):
        es_bruto = True
    elif re.search(r"net", full, re.I):
        es_bruto = False

    frecuencia = None
    if re.search(r"anuales?|al\s+año|\/año", full, re.I):
        frecuencia = "anual"
    elif re.search(r"mensuales?|al\s+mes|\/mes", full, re.I):
        frecuencia = "mensual"

    return {
        "tiene_dato": True,
        "salario_raw": full[:100].strip(),
        "salario_valor": val,
        "es_bruto": es_bruto,
        "frecuencia": frecuencia,
        "moneda": moneda,
    }


# ---------------------------------------------------------------------------
# City extraction (best-effort)
# ---------------------------------------------------------------------------

CITIES = [
    "madrid", "barcelona", "bcn", "valencia", "sevilla", "bilbao", "málaga", "malaga",
    "zaragoza", "alicante", "murcia", "palma", "las palmas", "gran canaria",
    "valladolid", "córdoba", "cordoba", "vigo", "gijón", "gijon", "vitoria",
    "granada", "pamplona", "salamanca", "segovia", "cuenca", "toledo", "burgos",
    "santander", "logroño", "lugo", "oviedo", "badajoz", "cáceres", "cáceres",
    "huelva", "jaén", "almería", "almeria", "castellón", "castellon",
    "tenerife", "lanzarote", "ibiza", "menorca",
    # Country-level remote / abroad
    "remoto", "remote", "teletrabajo", "teletrabajar",
    "dublin", "londres", "london", "berlin", "berlín", "amsterdam",
    "holanda", "países bajos", "alemania", "reino unido", "uk", "irlanda",
    "suiza", "switzerland", "suecia", "sweden", "noruega", "norway",
    "estados unidos", "usa", "canada", "québec", "quebec",
    "portugal", "lisboa", "lisbon",
]

CITY_RE = re.compile(
    r"(?:ciudad|city|ubicaci[oó]n|lugar|localidad|localización|donde|d[oó]nde)?\s*[:\-]?\s*"
    r"(" + "|".join(re.escape(c) for c in CITIES) + r")",
    re.I,
)

# Also match plain "Ciudad: X" lines
CITY_LINE_RE = re.compile(
    r"^(?:ciudad|city|ubicaci[oó]n)\s*[:\-=]\s*(.+)$",
    re.I | re.MULTILINE,
)


def extract_city(texto: str) -> str | None:
    if not texto:
        return None

    # Try labeled line first
    m = CITY_LINE_RE.search(texto)
    if m:
        val = m.group(1).strip().split("\n")[0].strip()
        if 2 < len(val) < 60:
            return val[:60]

    # Fallback: keyword match
    m = CITY_RE.search(texto)
    if m:
        return m.group(1).strip()

    return None


# ---------------------------------------------------------------------------
# Experience extraction (best-effort)
# ---------------------------------------------------------------------------

EXP_RE = re.compile(
    r"""
    (?:a[ñn]os?\s+(?:de\s+)?(?:experiencia|exp\.?)|experiencia[:\s]+|exp[.:\s]+)
    \s*[:\-=]?\s*
    (?:menos\s+de\s+)?
    (\d+(?:[.,]\d+)?)
    (?:\s*(?:a[ñn]os?|yrs?|y(?:ears?)?))?
    """,
    re.I | re.VERBOSE,
)


def extract_experience(texto: str) -> int | None:
    m = EXP_RE.search(texto or "")
    if m:
        try:
            return int(float(m.group(1).replace(",", ".")))
        except ValueError:
            pass
    return None


# ---------------------------------------------------------------------------
# Technology extraction (best-effort)
# ---------------------------------------------------------------------------

TECH_LINE_RE = re.compile(
    r"^(?:tecnolog[ií]as?|tec|tech|stack|lenguajes?|skills?)\s*[:\-=]\s*(.+)$",
    re.I | re.MULTILINE,
)


def extract_tech(texto: str) -> str | None:
    m = TECH_LINE_RE.search(texto or "")
    if m:
        val = m.group(1).strip().split("\n")[0].strip()
        if len(val) < 200:
            return val[:200]
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    posts = json.loads(INPUT.read_text(encoding="utf-8"))
    print(f"Posts totales: {len(posts)}")

    records = []
    for p in posts:
        autor = p.get("autor") or "[Borrado]"
        texto = p.get("texto") or ""
        ts = p.get("timestamp")

        salary = extract_salary(texto)
        city = extract_city(texto)
        exp = extract_experience(texto)
        tech = extract_tech(texto)

        records.append({
            "post_num": p["post_num"],
            "pagina": p["pagina"],
            "autor": autor,
            "timestamp": ts,
            "fecha_raw": p.get("fecha_raw"),
            "texto": texto,
            "tiene_dato": salary["tiene_dato"],
            "salario_raw": salary["salario_raw"],
            "salario_valor": salary["salario_valor"],
            "es_bruto": salary["es_bruto"],
            "frecuencia": salary["frecuencia"],
            "moneda": salary["moneda"],
            "ciudad": city,
            "experiencia_anos": exp,
            "tecnologia": tech,
        })

    df = pl.DataFrame(
        records,
        schema={
            "post_num": pl.Int32,
            "pagina": pl.Int32,
            "autor": pl.Utf8,
            "timestamp": pl.Int64,
            "fecha_raw": pl.Utf8,
            "texto": pl.Utf8,
            "tiene_dato": pl.Boolean,
            "salario_raw": pl.Utf8,
            "salario_valor": pl.Float64,
            "es_bruto": pl.Boolean,
            "frecuencia": pl.Utf8,
            "moneda": pl.Utf8,
            "ciudad": pl.Utf8,
            "experiencia_anos": pl.Int32,
            "tecnologia": pl.Utf8,
        },
    )

    # Derive date column from unix timestamp
    df = df.with_columns(
        pl.from_epoch("timestamp", time_unit="s").dt.date().alias("fecha")
    )

    df.write_parquet(OUT_SALARY)

    con_dato = df.filter(pl.col("tiene_dato"))
    print(f"Posts con dato salarial: {len(con_dato)} ({100*len(con_dato)/len(df):.1f}%)")

    # Deduplicate: for each author keep the latest post with salary data.
    # Prefer template posts (structured format) over casual mentions.
    # Exclude [Borrado] since we can't track them across posts.
    con_dato_identificado = con_dato.filter(pl.col("autor") != "[Borrado]")

    # Add is_template column to help with dedup priority
    con_dato_identificado = con_dato_identificado.with_columns(
        pl.col("texto").map_elements(
            lambda t: _is_template_post(t) if t else False,
            return_dtype=pl.Boolean,
        ).alias("is_template")
    )

    # Sort: template posts first, then by date descending
    dedup = (
        con_dato_identificado
        .sort(["is_template", "timestamp"], descending=[True, True])
        .unique(subset=["autor"], keep="first")
        .drop("is_template")
        .sort("salario_valor", descending=True)
    )

    dedup.write_parquet(OUT_DEDUP)
    print(f"Usuarios únicos con dato: {len(dedup)}")

    # Write review file for manual spot-check
    with open(OUT_REVIEW, "w", encoding="utf-8") as f:
        f.write("=== REVISIÓN DE EXTRACCIÓN (muestra 50 primeros) ===\n\n")
        for row in con_dato.head(50).iter_rows(named=True):
            f.write(
                f"@{row['autor']} #{row['post_num']} [{row['fecha_raw']}]\n"
                f"  raw:    {row['salario_raw']}\n"
                f"  valor:  {row['salario_valor']}  |  bruto={row['es_bruto']}  |  freq={row['frecuencia']}  |  moneda={row['moneda']}\n"
                f"  ciudad: {row['ciudad']}  |  exp: {row['experiencia_anos']}  |  tech: {row['tecnologia']}\n"
                f"  texto:  {row['texto'][:200].replace(chr(10), ' ')}\n\n"
            )

    # Summary stats
    print(f"\nDistribución frecuencia:")
    print(con_dato.group_by("frecuencia").len().sort("len", descending=True))
    print(f"\nDistribución moneda:")
    print(con_dato.group_by("moneda").len().sort("len", descending=True))
    print(f"\nDistribución bruto/neto:")
    print(con_dato.group_by("es_bruto").len().sort("len", descending=True))
    print(f"\nTop ciudades:")
    print(
        con_dato.filter(pl.col("ciudad").is_not_null())
        .group_by("ciudad")
        .len()
        .sort("len", descending=True)
        .head(15)
    )
    print(f"\nGuardado: {OUT_SALARY}, {OUT_DEDUP}")
    print(f"Revisión: {OUT_REVIEW}")


if __name__ == "__main__":
    main()
