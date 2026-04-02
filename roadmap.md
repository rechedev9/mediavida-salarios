# Roadmap: Tabla salarial de programadores en España (MediaVida)

## Objective

Scrapear el hilo de MediaVida (88 páginas), producir una tabla salarial limpia con ajuste por inflación, y publicar los resultados como un dashboard Streamlit desplegado en Streamlit Community Cloud con URL compartible en el foro.

---

## Current State

### Pipeline de datos (COMPLETADA)

| Script | Función | Estado |
|---|---|---|
| `scrape_mediavida.py` | Descarga 88 páginas con httpx+brotli, HTML cacheado en `raw_html/` | ✅ |
| `extract_salary.py` | Regex con filtros de tercera persona, dedup template-first por usuario | ✅ |
| `build_table.py` | Armoniza bruto/neto/mensual→anual, IPC España, normaliza ciudades, exporta CSV/Parquet/stats | ✅ |

### Datos producidos

- `posts_raw.json` — 2602 posts, 416 autores (Oct 2017 – Abr 2026)
- `salarios_tabla.csv` / `.parquet` — **231 programadores** con dato válido
- Mediana bruto anual €2026: **38.711€** | P25: 28.933€ | P75: 57.514€
- Ciudades normalizadas: 118 valores raw → ~30 canónicos (Madrid 37, Remoto 49, Barcelona 29, Valencia 10…)
- Columnas derivadas: `ciudad` (canónica), `ciudad_raw`, `modalidad` (Presencial/Híbrido/Remoto), `pais` (España 79% / Extranjero 11%)
- Distribución por ciudad, año, experiencia, tecnología disponible

### Lo que falta

- No existe repositorio Git aún
- No existe app Streamlit
- No hay `requirements.txt` ni configuración de deploy

---

## Constraints

- **Streamlit Community Cloud:** requiere repo público en GitHub con `requirements.txt` y un `.py` de entrada.
- **Tamaño de datos:** `salarios_tabla.parquet` es pequeño (~200 filas), se puede embeber en el repo directamente. No necesita base de datos.
- **Sin secretos:** no hay API keys ni tokens necesarios para la app (solo lee datos estáticos).
- El `raw_html/` y otros artefactos pesados NO deben ir al repo público.
- Los datos del foro son públicos (MediaVida es de acceso libre), pero la app debe citar la fuente.

---

## Workstreams

1. **W8 — Dashboard Streamlit:** Crear `app.py` con visualizaciones interactivas.
2. **W9 — Repo GitHub:** Inicializar repo, `.gitignore`, `requirements.txt`, push.
3. **W10 — Deploy Streamlit Cloud:** Conectar repo → Streamlit Community Cloud → URL pública.

---

## Step-by-Step Plan

### Fase 8: Dashboard Streamlit (W8)

**Script:** `app.py`

Visualizaciones previstas:

1. **Header** — Título, fuente (link al hilo de MV), N, período, metodología breve
2. **KPIs** — Mediana, media, P25, P75 en tarjetas tipo `st.metric`
3. **Histograma** — Distribución de salario bruto anual €2026 (Plotly)
4. **Boxplot por ciudad** — Top 8-10 ciudades con N≥3 (Plotly)
5. **Evolución temporal** — Mediana por año de post, original vs. €2026 (Plotly)
6. **Scatter experiencia vs. salario** — Solo rows con `experiencia_anos` no nulo (Plotly)
7. **Tabla interactiva** — DataFrame filtrable con `st.dataframe` (sin texto completo del post)
8. **Sección de transparencia** — % bruto/neto/asumido, % frecuencia inferida, fuente IPC

**Filtros laterales (sidebar):**
- Rango de salario (slider)
- Ciudad (multiselect — usa columna `ciudad` normalizada)
- Año de post (range slider)
- Solo España / incluir extranjero (toggle — usa columna `pais`)
- Modalidad (multiselect — usa columna `modalidad`: Presencial/Híbrido/Remoto)

**Dependencias adicionales:**
```
streamlit
plotly
polars
```

> **Checkpoint:** Probar `streamlit run app.py` en local antes de pushear.

---

### Fase 9: Repo GitHub (W9)

1. **Inicializar git** en `/Users/reche/projects/scrapper`
2. **`.gitignore`** — excluir:
   ```
   venv/
   raw_html/
   __pycache__/
   *.pyc
   posts_raw.json
   posts_with_salary.parquet
   salarios_dedup.parquet
   extraction_review.txt
   # Artefactos del proyecto CS2 anterior
   cs2_*
   find_creators.py
   log.md
   roadmap_youtube.md
   ```
3. **`requirements.txt`**:
   ```
   streamlit>=1.35
   plotly>=5.20
   polars>=1.0
   ```
4. **Archivos que SÍ van al repo:**
   ```
   app.py                  ← dashboard
   salarios_tabla.parquet  ← datos finales (pequeño, ~50KB)
   salarios_stats.txt      ← estadísticas texto plano
   requirements.txt        ← deps para Streamlit Cloud
   .gitignore
   roadmap.md              ← este archivo
   README.md               ← opcional, breve
   ```
5. **Archivos de pipeline (opcionales, para reproducibilidad):**
   ```
   scrape_mediavida.py
   extract_salary.py
   build_table.py
   ```
   Incluirlos permite a cualquiera re-ejecutar el scraping. No son necesarios para la app.

6. **Crear repo** en GitHub (nombre sugerido: `mediavida-salarios`)
7. **Push** rama `main`

> **Checkpoint:** Confirmar que el repo contiene `app.py`, `requirements.txt`, `salarios_tabla.parquet`, y que NO contiene `raw_html/`, `venv/`, ni datos intermedios pesados.

---

### Fase 10: Deploy Streamlit Cloud (W10)

1. Ir a [share.streamlit.io](https://share.streamlit.io)
2. Conectar cuenta GitHub (el usuario debe hacer esto manualmente — requiere OAuth)
3. Seleccionar repo `mediavida-salarios`, rama `main`, archivo `app.py`
4. Deploy automático — URL generada tipo `mediavida-salarios.streamlit.app`
5. Pegar URL en el hilo de MediaVida

> **Nota:** Streamlit Cloud hace cold start de ~30s si la app lleva rato sin visitas. Es normal.

---

## Files Likely Affected / Created

```
scrapper/
├── app.py                      # NUEVO — Streamlit dashboard
├── requirements.txt            # NUEVO — deps para Streamlit Cloud
├── .gitignore                  # NUEVO — excluye venv, raw_html, datos intermedios
├── salarios_tabla.parquet      # EXISTENTE — datos finales para la app
├── salarios_stats.txt          # EXISTENTE — estadísticas texto plano
├── scrape_mediavida.py         # EXISTENTE — pipeline de scraping
├── extract_salary.py           # EXISTENTE — pipeline de extracción
├── build_table.py              # EXISTENTE — pipeline de armonización
└── roadmap.md                  # EXISTENTE — este archivo (actualizado)
```

---

## Risks

| Riesgo | Probabilidad | Mitigación |
|--------|-------------|------------|
| Streamlit Cloud duerme la app por inactividad | Segura | Documentar en el post del foro que puede tardar ~30s en cargar |
| Repo público expone datos de usuarios del foro | Baja | Los datos de MV son públicos; la app solo muestra nick, año, ciudad, salario — no texto completo |
| El parquet no se lee bien en Streamlit Cloud | Muy baja | Polars lee parquet sin problemas; testado localmente |
| La app se rompe si Streamlit cambia API | Baja | Fijar versión mínima en `requirements.txt` |

---

## Verification

- [ ] `streamlit run app.py` funciona en local con todos los gráficos
- [ ] Filtros de sidebar funcionan correctamente
- [ ] No se expone texto completo de los posts (privacidad de contexto)
- [ ] Repo en GitHub no contiene `venv/`, `raw_html/`, ni datos intermedios
- [ ] URL de Streamlit Cloud carga correctamente tras deploy
- [ ] Gráficos son legibles en móvil (el foro se lee mucho desde móvil)

---

## Open Questions

1. **Nombre del repo:** ¿`mediavida-salarios` o prefieres otro nombre?

2. **Cuenta GitHub:** ¿Quieres crear el repo bajo tu cuenta personal o una organización?

3. **Texto completo en la tabla:** ¿Incluir el texto del post en la tabla interactiva (permite al lector ver el contexto original) o excluirlo (más limpio, menos ruido)?

---

---

# Roadmap: Creadores CS2 hispanos 20k-100k seguidores

## Objetivo

Encontrar creadores de contenido de CS2 de habla hispana con entre 20,000 y 100,000 seguidores/suscriptores en Instagram, Twitch y YouTube.
Rango anterior completado: 2k-20k (18 IG + 8 Twitch + 13 YT = 39 total).

## Estado actual

| Plataforma | Estado | Archivo de output |
|---|---|---|
| Instagram | ✅ completado (6 creadores) | `cs2_instagram_20k_100k.json` |
| Twitch | ✅ completado (3 creadores — hora baja actividad) | `cs2_twitch_20k_100k.json` |
| YouTube | ✅ completado (15 creadores) | `cs2_youtube_20k_100k.json` |

## Estrategia por plataforma

### Instagram
- Google dorking via Chrome (`site:instagram.com "cs2" español` etc.)
- Extraer usernames de los snippets de Google
- Visitar cada perfil, leer meta description para obtener seguidores
- Filtrar 20k-100k, descartar organizaciones/tiendas/compilaciones

### Twitch
- TwitchTracker ranking (`twitchtracker.com/channels/ranking/spanish?game=Counter-Strike+2`)
  - Para 20k-100k estarán en páginas anteriores (más arriba en el ranking) vs. las páginas 10-13 del rango 2k-20k
- Twitch GQL API (`gql.twitch.tv/gql`, client-id: `kimne78kx3ncx6brgo4mv6wki5h1ko`) para verificar followers y último juego
- Filtrar variety streamers (último juego: Roblox, slots, etc.)

### YouTube
- YouTube search con filtro de canales (`sp=EgIQAg%3D%3D`)
- YouTube internal API (`/youtubei/v1/search`) para ejecutar múltiples queries sin navegar
- Filtrar no-hispanos, organizaciones, canales de cheats, compilaciones

## Archivos de output esperados

```
cs2_instagram_20k_100k.json / .txt / .csv
cs2_twitch_20k_100k.json / .txt / .csv
cs2_youtube_20k_100k.json / .txt / .csv
cs2_creators_combined_20k_100k.txt / .csv
```

## Log de progreso

### Twitch — ✅ 2026-04-02
- TwitchTracker páginas 1-9 (423 candidatos)
- Batch GQL API (22 requests × 20 usuarios = followers + lastGame)
- 3 con lastGame = Counter-Strike en rango 20k-100k
- 0 streamers en vivo (hora baja — 09:27h)
- Para completar: re-run en horario pico LATAM/España
- Resultados: `cs2_twitch_20k_100k.json/txt`

### YouTube — ✅ 2026-04-02
- 20 queries via YouTube internal API (/youtubei/v1/search, channels filter EgIQAg==)
- 309 canales únicos descubiertos
- 30 en rango 20k-100k
- 15 clasificados como creadores individuales hispanos
- Excluidos: BLAST/StarLadder/ESL (orgs), LiminhaG0d/illegal Moments/LIM-CS/DEKO/Thour/EVY/GODxpEEzY/BIBA (no hispanos), CS2 Cheats (cheat site), CS Argentina (compilación)
- Resultados: `cs2_youtube_20k_100k.json/txt/csv`
- Combinado: `cs2_creators_combined_20k_100k.txt/csv` (24 total: 15 YT + 3 Twitch + 6 IG)

### Instagram — ✅ 2026-04-02
- 10 queries de Google dorking via Chrome browser automation
- 54 perfiles verificados con fetch() desde instagram.com
- 10 en rango 20k-100k, 6 clasificados como creadores individuales
- Excluidos: csg0fun/drunkgamingcs (clips), bonoxs_latam/enagenda_ (org/media)
- Resultados: `cs2_instagram_20k_100k.json/txt/csv`

---

# Roadmap: Creadores CS2 hispanos 100k-500k seguidores

## Estado actual

| Plataforma | Estado | Creadores | Archivo de output |
|---|---|---|---|
| YouTube   | ✅ completado | 6 creadores | `cs2_youtube_100k_500k.json` |
| Twitch    | ✅ completado | 5 creadores | `cs2_twitch_100k_500k.json` |
| Instagram | ✅ completado | 1 creador   | `cs2_instagram_100k_500k.json` |

## Log de progreso

### Twitch — ✅ 2026-04-02
- TwitchTracker páginas 1-5 (Spanish+CS2 filter), 82 candidatos en rango 100k-500k
- Batch GQL API (4 batches × 20 usuarios) → followers exactos + lastGame
- 5 con lastGame = Counter-Strike: starwraith (398K), strakatv (272K), forg1 (251K), safiro01 (174K), elmorocho7 (112K)
- Resultados: `cs2_twitch_100k_500k.json`

### YouTube — ✅ 2026-04-02
- 35 queries via YouTube internal API (514 canales únicos)
- 23 en rango 100k-500k
- 6 creadores individuales hispanos: Blackelespanolito (488K), vLADOPARD (354K), SirMaza (287K), Dareh (235K), FlipiN (211K), Serious (140K)
- Excluidos: csproland/Waffle/Trainwreckstv (inglés), mch/MADHOUSE (portugués), NaToSaphiX/ZywOo/EliGE (no hispanos), ESL orgs
- Resultados: `cs2_youtube_100k_500k.json`

### Instagram — ✅ 2026-04-02
- 70+ perfiles verificados via Instagram web_profile_info API
- Handles reales de creadores encontrados via Twitch social links (GQL)
- Solo 1 creador individual hispano en rango: blackelespanolito (150K)
- Excluidos: teamisurus/shindengg (orgs), madhousetv_/kscerato (portugueses), peereira7 (variety/JC)
- Nota: ecosistema CS2 hispano en Instagram es reducido a esta escala
- Resultados: `cs2_instagram_100k_500k.json`

## Combinado
- `cs2_creators_combined_100k_500k.txt / .csv` — 12 entradas, 11 creadores únicos
- blackelespanolito aparece en YouTube (488K) e Instagram (150K)
