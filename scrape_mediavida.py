"""
Scrape the MediaVida thread on programmer salaries in Spain.
Thread: https://www.mediavida.com/foro/estudios-trabajo/programadores-haceis-donde-trabajais-cuanto-ganais-596068
88 pages total.

Outputs:
  raw_html/page_NNN.html  — raw HTML per page (cached, skipped if exists)
  posts_raw.json          — list of {post_id, autor, timestamp, fecha_raw, texto, pagina}
"""

import json
import time
import random
import re
from pathlib import Path

import httpx
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_URL = "https://www.mediavida.com/foro/estudios-trabajo/programadores-haceis-donde-trabajais-cuanto-ganais-596068"
TOTAL_PAGES = 88
RAW_DIR = Path("raw_html")
OUTPUT_FILE = Path("posts_raw.json")

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

    delay = random.uniform(1.2, 2.5)
    time.sleep(delay)
    return html


def parse_posts(html: str, pagina: int) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    posts = []

    # Select all post divs, skip post-container (OP duplicate) and post-editor (form)
    SKIP_IDS = {"post-container", "post-editor"}
    for div in soup.select('div[id^="post-"]'):
        div_id = div.get("id", "")
        if div_id in SKIP_IDS:
            continue

        # Post number from id: "post-42" → 42
        m = re.match(r"post-(\d+)$", div_id)
        if not m:
            continue
        post_num = int(m.group(1))

        meta = div.select_one(".post-meta")
        contents = div.select_one(".post-contents")
        if not meta or not contents:
            continue

        # Author
        autor_tag = meta.select_one("a.autor")
        autor = autor_tag.get_text(strip=True) if autor_tag else None

        # Timestamp from data-time attribute (Unix epoch)
        rd = meta.select_one("span.rd")
        data_time = rd.get("data-time") if rd else None
        fecha_raw = rd.get("title") if rd else None
        timestamp = int(data_time) if data_time and data_time.isdigit() else None

        # Text: remove blockquotes (cited content) before extracting
        for bq in contents.find_all("blockquote"):
            bq.decompose()
        for cita in contents.find_all(class_=re.compile(r"cit|quot")):
            cita.decompose()

        texto = contents.get_text(separator="\n", strip=True)

        posts.append({
            "post_num": post_num,
            "pagina": pagina,
            "autor": autor,
            "timestamp": timestamp,
            "fecha_raw": fecha_raw,
            "texto": texto,
        })

    return posts


def main():
    RAW_DIR.mkdir(exist_ok=True)

    all_posts: list[dict] = []

    with httpx.Client(headers=HEADERS, timeout=30) as client:
        for page in tqdm(range(1, TOTAL_PAGES + 1), desc="Páginas"):
            try:
                html = fetch_page(client, page)
                posts = parse_posts(html, pagina=page)
                all_posts.extend(posts)
            except httpx.HTTPStatusError as e:
                print(f"\n[!] HTTP {e.response.status_code} en página {page}")
            except Exception as e:
                print(f"\n[!] Error en página {page}: {e}")

    OUTPUT_FILE.write_text(
        json.dumps(all_posts, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"\n=== Resultado ===")
    print(f"Posts totales: {len(all_posts)}")
    autores = {p["autor"] for p in all_posts if p["autor"]}
    print(f"Autores únicos: {len(autores)}")
    print(f"Guardado en: {OUTPUT_FILE}")

    # Quick sanity: show first and last post
    if all_posts:
        p0 = all_posts[0]
        pN = all_posts[-1]
        print(f"\nPrimer post: #{p0['post_num']} @{p0['autor']} — {p0['fecha_raw']}")
        print(f"Último post:  #{pN['post_num']} @{pN['autor']} — {pN['fecha_raw']}")


if __name__ == "__main__":
    main()
