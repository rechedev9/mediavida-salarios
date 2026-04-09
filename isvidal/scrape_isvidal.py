"""
Scrape the MediaVida React hilo general thread for user isvidal.
Thread: https://www.mediavida.com/foro/dev/react-hilo-general-libreria-para-atraerlos-atarlos-todos-657749
40 pages total.

Usage:
  python scrape_isvidal.py            # full run → posts_all.json
  python scrape_isvidal.py --tracer   # page 1 only, prints spot-check, no output file

Outputs (relative to this file's directory):
  raw_html/page_NNN.html  — cached raw HTML per page
  posts_all.json          — list of dicts: {post_num, pagina, autor, timestamp,
                            fecha_raw, fecha_iso, texto, quotes, code_blocks}
"""

import json
import re
import sys
import time
import random
from datetime import datetime, timezone
from pathlib import Path

import httpx
from bs4 import BeautifulSoup, NavigableString, Tag
from tqdm import tqdm

BASE = Path(__file__).parent
BASE_URL = (
    "https://www.mediavida.com/foro/dev/"
    "react-hilo-general-libreria-para-atraerlos-atarlos-todos-657749"
)
TOTAL_PAGES = 40
RAW_DIR = BASE / "raw_html"
OUTPUT_FILE = BASE / "posts_all.json"
TARGET_AUTHOR = "isvidal"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}


def page_url(page: int) -> str:
    if page == 1:
        return BASE_URL
    return f"{BASE_URL}/{page}"


def fetch_page(client: httpx.Client, page: int) -> str:
    path = RAW_DIR / f"page_{page:03d}.html"
    if path.exists():
        return path.read_text(encoding="utf-8")

    url = page_url(page)
    resp = client.get(url, follow_redirects=True)
    resp.raise_for_status()
    html = resp.text
    path.write_text(html, encoding="utf-8")

    time.sleep(random.uniform(1.2, 2.5))
    return html


def _parse_ref_num(a: Tag) -> int | None:
    """Extract the quoted post number from <a class="quote">."""
    # rel="N" is the canonical source per confirmed HTML structure
    rel_val = a.get("rel", [])
    rel_str = (rel_val[0] if isinstance(rel_val, list) else str(rel_val)) if rel_val else ""
    if rel_str.isdigit():
        return int(rel_str)
    # Fallback: href="#N"
    href = a.get("href", "")
    frag = href.lstrip("#")
    if frag.isdigit():
        return int(frag)
    return None


def extract_quotes(contents: Tag) -> list[dict]:
    """Read structured quote metadata from .post-contents without modifying the tree.

    Two confirmed shapes:
      Inline: <p><a class="quote" href="#N" rel="N">#N</a> reply text</p>
      Block:  <p><a class="quote" href="#N">#N</a></p>
              <blockquote class="quote">full quoted body</blockquote>
    """
    quotes = []
    for a in contents.find_all("a", class_="quote"):
        ref_num = _parse_ref_num(a)

        # Inline text: text nodes / elements that follow the anchor inside its parent <p>
        inline_text = ""
        parent = a.parent
        if parent and parent.name == "p":
            parts = []
            for sib in a.next_siblings:
                if isinstance(sib, NavigableString):
                    parts.append(str(sib))
                elif isinstance(sib, Tag):
                    parts.append(sib.get_text())
            inline_text = "".join(parts).strip()

        # Block text: <blockquote> immediately following the anchor's parent <p>
        block_text = ""
        if parent and parent.name == "p":
            next_sib = parent.find_next_sibling()
            if next_sib and next_sib.name == "blockquote":
                block_text = next_sib.get_text(separator="\n", strip=True)

        quotes.append({
            "ref_num": ref_num,
            "inline_text": inline_text,
            "block_text": block_text,
        })
    return quotes


def parse_posts(html: str, pagina: int) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    posts = []

    SKIP_IDS = {"post-container", "post-editor"}
    for div in soup.select('div[id^="post-"]'):
        div_id = div.get("id", "")
        if div_id in SKIP_IDS:
            continue

        m = re.match(r"post-(\d+)$", div_id)
        if not m:
            continue
        post_num = int(m.group(1))

        meta = div.select_one(".post-meta")
        contents = div.select_one(".post-contents")
        if not meta or not contents:
            continue

        autor_tag = meta.select_one("a.autor")
        autor = autor_tag.get_text(strip=True) if autor_tag else None

        rd = meta.select_one("span.rd")
        data_time = rd.get("data-time") if rd else None
        fecha_raw = rd.get("title") if rd else None
        timestamp = int(data_time) if data_time and data_time.isdigit() else None
        fecha_iso = (
            datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()
            if timestamp
            else None
        )

        # Read quote metadata before touching the tree
        quotes = extract_quotes(contents)

        # Read code blocks from <pre> before stripping
        code_blocks = [pre.get_text(strip=True) for pre in contents.find_all("pre")]

        # Strip quotes and code to produce clean texto
        # Walk anchors in document order; decompose parent <p> and its following <blockquote>
        for a in list(contents.find_all("a", class_="quote")):
            parent = a.parent
            if parent and parent.name == "p":
                next_sib = parent.find_next_sibling()
                if next_sib and next_sib.name == "blockquote":
                    next_sib.decompose()
                parent.decompose()
        # Catch any remaining blockquotes not preceded by a quote-anchor <p>
        for bq in contents.find_all("blockquote"):
            bq.decompose()
        for pre in contents.find_all("pre"):
            pre.decompose()
        for code in contents.find_all("code"):
            code.decompose()

        texto = contents.get_text(separator="\n", strip=True)

        posts.append({
            "post_num": post_num,
            "pagina": pagina,
            "autor": autor,
            "timestamp": timestamp,
            "fecha_raw": fecha_raw,
            "fecha_iso": fecha_iso,
            "texto": texto,
            "quotes": quotes,
            "code_blocks": code_blocks,
        })

    return posts


def sanity_check(all_posts: list[dict], tracer: bool) -> None:
    total = len(all_posts)
    autores = {p["autor"] for p in all_posts if p["autor"]}
    isvidal_posts = [p for p in all_posts if p["autor"] == TARGET_AUTHOR]

    label = "(tracer bullet — página 1)" if tracer else ""
    print(f"\n=== Resultado {label} ===")
    print(f"Posts totales:        {total}")
    print(f"Autores únicos:       {len(autores)}")
    print(f"Posts de {TARGET_AUTHOR}: {len(isvidal_posts)}")

    ts_list = [p["timestamp"] for p in all_posts if p["timestamp"]]
    if ts_list:
        first_date = datetime.fromtimestamp(min(ts_list), tz=timezone.utc).strftime("%Y-%m-%d")
        last_date = datetime.fromtimestamp(max(ts_list), tz=timezone.utc).strftime("%Y-%m-%d")
        print(f"Rango de fechas:      {first_date} — {last_date}")

    if len(isvidal_posts) == 0:
        print(f"\n[ABORT] No se encontraron posts de '{TARGET_AUTHOR}'. Verificar URL o handle.")
        sys.exit(1)

    if tracer:
        print("\n--- Tracer: primer post de isvidal ---")
        p = isvidal_posts[0]
        print(f"  post #{p['post_num']} — {p['fecha_iso']}")
        print(f"  texto[:200]: {p['texto'][:200]!r}")
        print(f"  quotes: {p['quotes']}")
        print(f"  code_blocks count: {len(p['code_blocks'])}")

        posts_with_quotes = [p for p in all_posts if p["quotes"]]
        if posts_with_quotes:
            print("\n--- Tracer: primer post con citas (cualquier autor) ---")
            pq = posts_with_quotes[0]
            print(f"  post #{pq['post_num']} @{pq['autor']} — {pq['fecha_iso']}")
            print(f"  quotes[0]: {pq['quotes'][0]}")

        posts_with_code = [p for p in all_posts if p["code_blocks"]]
        if posts_with_code:
            print("\n--- Tracer: primer post con código (cualquier autor) ---")
            pc = posts_with_code[0]
            print(f"  post #{pc['post_num']} @{pc['autor']} — {pc['fecha_iso']}")
            print(f"  code_blocks[0][:200]: {pc['code_blocks'][0][:200]!r}")


def main(tracer: bool = False) -> None:
    RAW_DIR.mkdir(exist_ok=True)

    pages = range(1, 2) if tracer else range(1, TOTAL_PAGES + 1)
    all_posts: list[dict] = []

    with httpx.Client(headers=HEADERS, timeout=30) as client:
        for page in tqdm(pages, desc="Páginas"):
            try:
                html = fetch_page(client, page)
                posts = parse_posts(html, pagina=page)
                all_posts.extend(posts)
            except httpx.HTTPStatusError as e:
                print(f"\n[!] HTTP {e.response.status_code} en página {page}")
            except Exception as e:
                print(f"\n[!] Error en página {page}: {e}")

    sanity_check(all_posts, tracer)

    if not tracer:
        OUTPUT_FILE.write_text(
            json.dumps(all_posts, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Guardado en: {OUTPUT_FILE}")


if __name__ == "__main__":
    main(tracer="--tracer" in sys.argv)
