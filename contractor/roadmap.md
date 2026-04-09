# Roadmap — Contractor desde España (stack TS / Next.js / React / Go)

## Objetivo

Producir una guía concreta y accionable sobre cómo trabajar como **contractor** (no freelance) desde España para un desarrollador mid-senior TypeScript / Next.js / React / Go, facturando a empresas fuera de España para esquivar la figura del falso autónomo. Resultado final: un conjunto de documentos de referencia en `contractor/` que permitan al usuario decidir si arrancar, y si sí, saber exactamente los siguientes pasos.

Scope explícito: **investigación, no ejecución**. No se da de alta, no se abre cuenta, no se firma con ninguna plataforma. La decisión y la ejecución las hace el usuario después.

---

## Current State

### Contexto ya validado (sin web, de los screenshots del usuario)

Los posts `#2659`, `#2662`, `#2671` de `isvidal` en MediaVida establecen:

- **Contractor ≠ freelance.** Es un concepto distinto que en España "casi ni existe".
- **Modelo operativo:** contratos 6-12 meses renovables con **una sola empresa**, jornada L-V tipo empleado. Algunas pagan vacaciones/enfermedad, otras no.
- **Quién contrata:** empresas grandes (decenas a cientos de millones de revenue) → pagos predecibles. Referencias: Revolut (mencionada por otro usuario), empresa francesa (isvidal actualmente).
- **El "demonio" del falso autónomo:** en España, trabajar 6-10 meses para una empresa como único pagador te clasifica como falso autónomo. Sale no lícito.
- **Por qué facturar fuera sirve:** la ITSS no persigue estos casos cuando el pagador es una empresa extranjera → la figura contractor sólo es viable con clientes fuera.
- **Reclutamiento idéntico al de asalariado:** estas empresas ofrecen "asalariado o contractor, tú eliges" (ejemplo Revolut).
- **Rates reales 2026 (experiencia isvidal):**
  - Floor: 300-350 €/día (~35-40 €/h)
  - Medio: 400-600 €/día (~40-60 €/h)
  - Alto/senior: ~70 €/h (difícil, "picateclas raso")
- **Ventajas secundarias del alta autónomo:** side projects legales ("web al amigo panadero 3K extra"), equipo deducible.

### Lo que falta validar con fuentes externas

- Reforma cuotas autónomo 2023 — tramos aplicables en 2026
- Tarifa plana para nuevos autónomos 2026 (cuantía y duración actual)
- Criterios vigentes ITSS sobre falso autónomo (Glovo, Deliveroo como jurisprudencia)
- Epígrafe IAE correcto para desarrollo software B2B internacional
- ROI (Registro Operadores Intracomunitarios): trámite, plazos, obligaciones derivadas
- Plataformas contractor activas en 2026 para el stack del usuario
- Rates desglosados por stack (TS vs Go) y país pagador (FR, DE, UK, CH, US)
- Break-even autónomo vs SL a rates reales 2026
- Alternativas jurisdicción tras reforma Portugal NHR 2024 (IFICI), Andorra, Chipre, Irlanda
- Templates MSA/SOW limpias y revisables

### Estado del repo

- `scrapper/` contiene 3 subproyectos previos: MediaVida salary pipeline (completo), CS2 creator finder (completo), isvidal thread analysis (Fase 3 hecha, Fase 4 dashboard pendiente).
- Patrón establecido: líneas de trabajo nuevas viven en subcarpetas con su propio `roadmap.md` y `log.md` (`isvidal/` es el ejemplo canónico).
- No hay trabajo previo sobre contractor en el repo.

### Fases completadas

| Fase | Deliverable | Estado |
|---|---|---|
| Fase 0 — Scaffolding | `roadmap.md` + `log.md` | ✅ 2026-04-09 |
| Fase 1 — Briefing ejecutivo | `briefing.md` | ✅ 2026-04-09 |
| Fase 2 — W1 Legal/fiscal | `legal.md` | ✅ 2026-04-09 |
| Fase 3 — W2 Setup operacional | `setup.md` | ✅ 2026-04-09 |
| Fase 4 — W3 Mercado y canales | `mercado.md` | ✅ 2026-04-09 |
| Fase 5 — W4 Mecánica contractual | `contratos.md` | ⏳ pendiente |

---

## Approach

**Subproyecto nuevo `contractor/`** siguiendo el patrón `isvidal/`. No se toca el `roadmap.md` top-level ni ningún otro subproyecto.

**Investigación bottom-up con tracer bullet.** El tracer bullet (Fase 1) es un briefing ejecutivo de 3-5 páginas que cubre los puntos críticos end-to-end en una sola pasada — suficiente para que el usuario tome decisión informada. Luego se profundiza por capas.

**Orden:** legal/fiscal → operacional → mercado → contratos → optimización → riesgos. El orden no es arbitrario: lo fiscal-legal habilita o bloquea todo lo demás (si no puedes facturar fuera limpio, no hay contractor). Lo operacional se monta una vez decidido. Mercado y contratos se ejecutan para encontrar y firmar el primer cliente. Optimización y riesgos son refinamiento.

**Rechazado:** investigación horizontal por áreas en paralelo. Riesgo de inconsistencias entre capas (p.ej. recomendar una plataforma asumiendo un setup fiscal que no aplica). El orden bottom-up evita ese gap.

**Rechazado:** escribir una sola gran guía monolítica. Split por documento permite que el usuario lea sólo lo que necesita y facilita iteración por fase.

---

## Constraints

- **Residencia fiscal:** España. No se asume movilidad a corto plazo (aunque se incluye como alternativa en Fase 6).
- **Perfil técnico:** TypeScript, Next.js, React, Go. Mid-senior (asumido a partir del stack; confirmar en Open Questions).
- **Moneda principal:** EUR. Aceptable cobrar GBP/USD via Wise/Revolut Business.
- **Cliente objetivo:** empresa fuera de España. Prioridad 1: UE (IVA intracomunitario sencillo). Prioridad 2: UK, US, CH.
- **Actualidad:** toda información fiscal/legal debe reflejar estado 2026 (post-reforma autónomos 2023). Fuentes anteriores sólo como referencia histórica.
- **Research-only:** no se ejecuta ningún trámite real. Output = markdown.
- **Disclaimer:** el resultado NO es asesoría legal/fiscal. Toda decisión real requiere gestoría/abogado — flagging explícito en cada documento.

---

## Workstreams

1. **W1 — Fundamentos legal-fiscales** (qué es lícito, cómo tributa)
2. **W2 — Setup operacional** (cómo te das de alta, qué herramientas)
3. **W3 — Mercado y canales** (dónde buscar, rates reales)
4. **W4 — Mecánica contractual** (qué firmas, cómo cobras, en qué divisa)
5. **W5 — Optimización y alternativas** (autónomo vs SL, jurisdicciones)
6. **W6 — Riesgos y pipeline** (seguros, cashflow, diversificación)

---

## Step-by-Step Plan

### Fase 0 — Scaffolding del subproyecto

- Crear `contractor/` con `roadmap.md` + `log.md` (este commit).
- Dejar en `log.md` el contexto destilado de los screenshots de isvidal como fuente inicial citable.
- No crear placeholders vacíos para los deliverables futuros — se crean en su fase.

### Fase 1 — Tracer bullet: briefing ejecutivo

**Deliverable:** `contractor/briefing.md`

**Contenido (3-5 páginas):**
- Glosario: contractor vs freelance vs empleado vs TRADE.
- Por qué sólo funciona facturando fuera (explicación del falso autónomo en 1 párrafo).
- Mini decision tree: ¿soy candidato? (años experiencia, nivel de inglés, tolerancia a downtime, appetite para papeleo).
- Los 5 pasos mínimos para arrancar (alta 036 + ROI + cuenta bancaria + gestoría + primera plataforma).
- Rates esperables 2026 para TS/Next/React/Go en UE (anclados en datos isvidal + 2ª fuente).
- Top 3 riesgos y cómo mitigarlos.
- TL;DR de una página al final.

**Criterio de éxito:** un dev que lo lea sabe (a) si esto le encaja y (b) si sí, cuáles son los próximos 3 pasos concretos, sin necesidad de leer el resto de documentos.

> **Checkpoint 1** — Revisar briefing con el usuario antes de abrir W1-W6. Si el tracer bullet va mal orientado, rehacer ahora es barato; rehacer después de escribir 7 documentos no.

### Fase 2 — W1 Fundamentos legal-fiscales

**Deliverable:** `contractor/legal.md`

**Contenido:**
- Figura autónomo vs SL (por qué autónomo es el default para empezar).
- **Falso autónomo en profundidad:** criterios ITSS (dependencia económica, ajenidad, herramientas, horario), jurisprudencia reciente (Glovo/Deliveroo y su aplicabilidad), Art. 1.2 ET + Art. 8.11 LISOS.
- TRADE como figura: por qué NO es salida (requiere cliente español con >75% facturación).
- **Por qué facturar fuera esquiva:** jurisdicción ITSS, ausencia de casos perseguidos, riesgo residual real.
- **IRPF:** estimación directa simplificada, tramos 2026 (estatal + autonómico), retenciones 15% / 7% primer años, Modelo 130 trimestral.
- **IVA:** reverse charge intracomunitario (Art. 44 Directiva 2006/112/EC), IVA 0% a B2B no-UE, Modelos 303 + 349 + 390.
- **RETA:** cuota 2026 por tramos (reforma 2023), tarifa plana nuevos autónomos, coberturas (IT, jubilación).
- **Deducciones típicas dev:** equipo, % vivienda, internet/móvil, formación, coworking, gestoría.

**Fuentes prioritarias:** BOE (Ley 31/2022 autónomos), Agencia Tributaria (modelos 036/130/303/349), portal Seguridad Social RETA, 2-3 guías 2026 (Infoautónomos, Holded, Declarando).

### Fase 3 — W2 Setup operacional

**Deliverable:** `contractor/setup.md` (checklist ejecutable)

**Contenido:**
- Alta censal: Modelo 036 vs 037, epígrafe IAE correcto para contractor software B2B internacional.
- Alta RETA simultánea.
- Alta ROI (Registro Operadores Intracomunitarios): via 036, plazo ~1 mes.
- **Cuenta bancaria business:** tradicional vs digital vs Wise/Revolut Business — tradeoffs (coste, divisa, fricción).
- **Herramientas facturación:** Quipu / Holded / Contasimple / Contabilum — comparativa.
- **Gestoría:** servicios mínimos necesarios, rango de precios (~60-120 €/mes), red flags al elegir.
- **Plantilla factura compliant:** numeración consecutiva, datos fiscales ambos lados, VAT number cliente, leyenda reverse charge, conversión divisa.

**Fuentes:** mismas que Fase 2 + sitios oficiales Quipu/Holded/Wise.

### Fase 4 — W3 Mercado y canales

**Deliverable:** `contractor/mercado.md`

**Contenido:**
- **Canales directos:** LinkedIn (filtro contract), HN Who is Hiring, WeWorkRemotely, OTTA, Cord, Landing.Jobs.
- **Plataformas contractor 2026:** Malt (FR), Toptal, Arc.dev, Gun.io, Honeypot (DACH), YunoJuno (UK), Lemon.io, CodementorX — qué vetting, qué fee, fit por stack.
- **Nichos por stack:**
  - TS/Next/React: demanda alta, saturación alta → diferenciación vía perf/RSC/testing.
  - Go: menos competencia contractor, rates típicamente superiores. Nichos: fintech backend, infra, dev tools.
  - Full-stack TS+Go: perfil muy vendible en scaleups.
- **Headhunters especializados:** NearForm, Distant Job, X-Team — modelo (cobran del cliente, no de ti).
- **Rates benchmark 2026** (tabla): desglose por stack (TS/Next/React vs Go) × país pagador (FR/DE/UK/CH/US) × nivel (mid/senior/principal). Anclado en datos isvidal + cruzado con Malt, Honeypot, posts foros.
- **Proceso típico:** screening → technical → system design → culture fit → oferta (rate, term, holidays).

**Fuentes:** sitios oficiales plataformas, Malt salary reports, Honeypot State of Tech, encuestas Stack Overflow, hilos foros (MediaVida, r/cscareerquestionsEU, r/digitalnomad).

### Fase 5 — W4 Mecánica contractual

**Deliverable:** `contractor/contratos.md`

**Contenido:**
- **Tipos:** MSA + SOW vs Service Agreement one-shot. Qué no firmar (employment contract disfrazado).
- **Cláusulas críticas:** IP assignment (limitar al scope), non-compete (limitadas en España), indemnification (capear al valor del contrato), payment terms (Net 30 sí, Net 60+ negociar), termination notice (2-4 semanas), time tracking obligatoriedad.
- **Divisa y FX:** facturar EUR por defecto, Wise para USD/GBP (0.5% vs 3-5% banco), fecha factura vs fecha cobro y su impacto.
- **Ciclo cobro:** timesheet → aprobación → factura → pago. Qué hacer si no pagan: burofax, orden europea de pago (Reglamento 1896/2006).
- **Templates:** links a MSA/SOW/invoice/timesheet limpios y revisables.

**Fuentes:** templates Law Insider, Clerky, Mollie guides, documentación oficial UE orden europea de pago.

### Fase 6 — W5 Optimización y alternativas

**Deliverable:** `contractor/optimizacion.md`

**Contenido:**
- **Autónomo vs SL:** break-even 2026 (aprox 50-70k € beneficio neto, a verificar con números reales), costes fijos SL (constitución, contabilidad formal), tributación SL (25% IS / 15% reducido), doble tributación dividendos, sueldo socio-administrador.
- **Deducciones avanzadas y sus límites reales:** vehículo (muy difícil justificar en software), vivienda (% afectado y problema IVA), plan pensiones (límites 2023+).
- **Beckham Law:** sólo aplicable a impatriados, no a residentes → no aplica al usuario.
- **Relocalización (con disclaimer fuerte):**
  - Portugal (post reforma NHR 2024 → IFICI: qué cambió, qué queda).
  - Andorra (residencia activa/pasiva, IRPF ~10%, realidad día a día).
  - Irlanda (contractor más complicado que asalariado).
  - Chipre (Non-Dom 17% tech).
  - Dubái (0%, pero banking UE, distancia, calidad de vida).
  - Riesgos cross-cutting: exit tax, residencia fiscal dual, mudanza fake.
- **Plan de carrera contractor:** cómo subir rate año a año (portfolio, case studies, referrals, negociación renovación).

**Fuentes:** BOE IS, guías fiscales 2026 cada jurisdicción, relatos reales (podcast/blogs de developers que han movido).

### Fase 7 — W6 Riesgos y pipeline

**Deliverable:** `contractor/riesgos.md`

**Contenido:**
- **Seguros:**
  - Responsabilidad civil profesional (~200-400 €/año, algunos clientes lo exigen).
  - Salud privada (compensación coberturas RETA limitadas).
  - Complementario IT (baja).
- **Cashflow:**
  - Fondo emergencia: 6-12 meses gastos personales + cuotas.
  - Buffer trimestral IVA/IRPF (no gastar ese dinero).
  - Payment terms vs ritmo facturas = dinero en la calle simultáneo.
- **Downtime entre contratos:** planificación anticipada, networking constante vs búsqueda reactiva, coste real de un sabático (cuota RETA sigue corriendo).
- **Diversificación:** la regla útil <75% facturación de un solo cliente (reduce riesgo residual falso autónomo y te da colchón ante cancelación).
- **Qué pasa si pierdes el contrato:** "cese de actividad" autónomos (condiciones estrictas), cotización para jubilación.

**Fuentes:** Mapfre/Mutua RC profesional, guías cese actividad autónomos, portal SS.

### Fase 8 — Consolidación y README

**Deliverable:** `contractor/README.md`

**Contenido:**
- Índice de todos los documentos con 1 frase cada uno.
- Orden de lectura recomendado (new → briefing → legal → setup → mercado → contratos → optimizacion → riesgos).
- TL;DR de 1 página (para quien sólo puede leer uno).
- Checklist de arranque concreto (next 3 steps).

> **Checkpoint 2** — Revisión final con el usuario. Decidir si pasar a ejecución real (fuera del scope de este roadmap).

---

## Checkpoints

- **Checkpoint 1 (tras Fase 1):** briefing ejecutivo revisado con el usuario. Validar dirección antes de abrir W1-W6.
- **Checkpoint 2 (tras Fase 8):** investigación completa. Decidir ejecución real como siguiente roadmap separado.

---

## Files Likely Affected / Created

```
scrapper/
└── contractor/                      # NUEVO subproyecto
    ├── roadmap.md                   # este archivo (Fase 0)
    ├── log.md                       # contexto acumulado (Fase 0)
    ├── briefing.md                  # Fase 1 — tracer bullet
    ├── legal.md                     # Fase 2 — W1
    ├── setup.md                     # Fase 3 — W2
    ├── mercado.md                   # Fase 4 — W3
    ├── contratos.md                 # Fase 5 — W4
    ├── optimizacion.md              # Fase 6 — W5
    ├── riesgos.md                   # Fase 7 — W6
    └── README.md                    # Fase 8 — índice + TL;DR
```

**No se tocan:** `roadmap.md` top-level, `log.md` top-level, `isvidal/`, ni ningún script o dato de los proyectos existentes.

---

## Risks

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| Información fiscal desactualizada (reformas 2023-2026) | Alta | BOE + Agencia Tributaria como oracle. Fecha en cada cita. Desconfiar de guías sin fecha. |
| Rates benchmark imposibles de verificar numéricamente | Media | Cruzar ≥3 fuentes: Malt reports, Honeypot, foros dev. Datos isvidal como anclaje. |
| Confundir "freelance" con "contractor" en fuentes en español | Alta | Glosario explícito en briefing. Marcar cuando una fuente mezcla los términos. Tratar fuentes españolas sobre "freelance" con precaución. |
| Scope creep (documento-enciclopedia inútil) | Media | Fase 1 tracer bullet fuerza entrega mínima útil temprana. Each doc ≤ 10 páginas hard cap. |
| Recomendaciones legales sin disclaimer | Media | Cada documento abre con disclaimer: esto es investigación, no asesoría fiscal/legal. |
| Consejos obsoletos sobre Portugal NHR (pre-reforma 2024) | Alta | Comprobar que toda referencia a Portugal sea post-IFICI. |
| Repetición entre documentos | Media | Cada tema vive en UN doc. Cross-reference con links internos, no duplicar. |

---

## Verification

- **Fase 1 (briefing):** ¿el usuario sabe, tras leerlo, si esto le encaja y los próximos 3 pasos? Si no, rehacer.
- **Fases 2-7:** cada documento cita fuentes con fecha. Sin "se suele cobrar" o "normalmente". Números concretos o nada.
- **Cross-check:** rates, umbrales fiscales y cuotas cruzados con ≥2 fuentes.
- **Actualidad:** toda referencia legal es post-reforma 2023 autónomos y post-reforma Portugal 2024.
- **Utilidad:** el usuario debe poder tomar 3 decisiones reales tras leer todo: (1) arranco ya, (2) espero X meses/condiciones, (3) descartado.
- **Sin sangre:** no hay links muertos ni referencias a plataformas que han cerrado.

---

## Open Questions

Estas no bloquean el arranque del roadmap — se pueden responder en el Checkpoint 1 o antes si el usuario quiere precisarlas.

1. **Deadline de decisión.** ¿Estás evaluando esto con vistas a arrancar pronto (semanas/meses) o es investigación de fondo para tener en el bolsillo? Afecta la profundidad de la Fase 6 (alternativas y relocalización).

2. **Nivel exacto de experiencia.** Leyendo el stack supongo mid-senior (5-8 años). ¿Correcto, o eres más senior (10+) o más junior? Cambia los rate benchmarks y las plataformas recomendadas.

3. **Perfil de trabajo preferido.** El modelo que describe isvidal es "classic contractor" (1 cliente, full-time, simula empleo 6-12 meses). ¿Es el modelo que buscas, o prefieres "independent consultant" (varios clientes, part-time)? Cambia la estrategia de pipeline y el peso del falso autónomo.
