# contractor subproject — accumulated context log

This log captures durable context for the contractor research subproject.
Append new entries; do not rewrite existing ones.

---

## 2026-04-09 — subproject scope & relationship to parent

`contractor/` is a new subproject inside the `scrapper` repo, following the pattern
established by `isvidal/`: dedicated folder with its own `roadmap.md`, `log.md`, and
deliverables. It does NOT share the top-level `roadmap.md` (which documents the
MediaVida salary pipeline and CS2 creator finder — thematically unrelated, mostly
finished work).

**Why subfolder instead of rewriting top-level roadmap.md (the strict goldroger
default):** the scraping projects' roadmap is still valuable context and would be
destroyed by a rewrite. The repo has an explicit subproject pattern. Applying
goldroger's "repository root" rule at the subproject level is the pragmatic
interpretation for this multi-project repo.

**Scope hard rule:** research only. This subproject produces markdown documents; it
does NOT execute any real-world action (no alta autónomo, no opening bank accounts,
no platform signup, no gestoría contacts). Any real execution is a separate
subsequent task with its own roadmap.

---

## 2026-04-09 — seed context from isvidal forum screenshots (#2659, #2662, #2671)

The user provided three screenshots of posts by `isvidal` on the MediaVida dev
forum. These are treated as validated seed context — every claim below should still
be cross-referenced with a second source in the deliverables, but they set the
baseline of what "contractor from Spain" means in this research.

**Definition distinction.** Contractor is NOT freelance. isvidal calls the concept
"casi inexistente en España". The core distinction:
- Freelance: multiple clients, project-based, variable hours, classic autónomo.
- Contractor: one client, 6-12 month renewable contracts, full-time Mon-Fri like an
  employee, some paid time off.

**Operating model.**
- Single-payer relationship with a large (tens-to-hundreds of millions revenue)
  company.
- Contract term: 6 months to 1 year, renewable.
- Work pattern: L-V, tipo empleado.
- Some contracts include paid holidays and sick days; others don't.
- Payment is predictable because these are financially stable companies.

**The falso autónomo barrier.** Spain's labor law (Art. 1.2 Estatuto de los
Trabajadores + inspection criteria) classifies a single-payer 6-10-month
relationship as false self-employment. ITSS can reclassify the relationship as
employment, fining both parties. This makes the contractor model unviable with
Spanish clients.

**Why invoicing foreign clients sidesteps this.** The ITSS does not practically
pursue cases where the contracting party is a foreign entity — jurisdictional
friction, lack of precedent, and no realistic enforcement path. isvidal's explicit
framing: "solo puedes tener esta figura de contractor cuando las facturas son a
empresas de fuera de España."

This is a key research axis: the deliverables must NOT recommend contractor with
Spanish clients. All guidance assumes invoicing abroad.

**Concrete company references.**
- Revolut was mentioned in the thread as an example (offers "asalariado o contractor,
  tú eliges" during recruitment; process is identical).
- isvidal currently works for a French company as contractor.
- A curious cultural detail: the French company cannot invite its *French*
  contractors to company parties (strict French rules around worker classification
  at events), but can invite Spanish contractors freely because they fall under
  cross-border rules.

**Rate tiers (isvidal's stated experience, 2026).**
- Floor: 300-350 €/day (~35-40 €/h)
- Medium: 400-600 €/day (~40-60 €/h)
- Senior/high end: around 70 €/h as a "picateclas raso" — explicitly described as a
  hard-to-reach extreme.
- isvidal mentions he currently earns around 70 €/h but didn't negotiate hourly.

**Side benefits of being autónomo mentioned.**
- Legal side projects: isvidal explicitly mentions doing a website "al amigo
  panadero por 3K extras" occasionally.
- Equipment is deductible ("iPhone, que por cierto, desgravas").

**Recruitment funnel.** Identical to salaried recruitment: screening, technical
interview, system design (for senior), culture fit, offer with rate + term +
holiday terms. The decision "asalariado o contractor" typically comes at the offer
stage and is the developer's choice.

---

## 2026-04-09 — researcher stack context

The user is a developer with TypeScript, Next.js, React, and Go. This shapes the
research:

- **Breadth** (frontend + backend + strong typing) suggests mid-senior minimum.
- **Stack relevance to contractor market:**
  - TS/Next/React: high demand but saturated. Differentiation matters.
  - Go: lower supply of contractor talent, rates typically higher than TS-only.
  - TS+Go full-stack: very marketable in scaleups/fintech.
- **Rate benchmarks should segment by stack.** A TS-only benchmark undersells Go
  opportunities; a Go-only benchmark misses the broad market.

Note: isvidal (the seed source) is TS/React-focused, so his rate quotes lean toward
TS stack. Go benchmarks will need separate sources.

---

## 2026-04-09 — Fase 1 completada: briefing.md

`contractor/briefing.md` escrito en una pasada. Cubre:
- Glosario (contractor vs freelance vs TRADE vs empleado)
- Por qué solo funciona con cliente extranjero (falso autónomo)
- Árbol de decisión de candidatura
- Los 5 pasos mínimos de arranque (036+ROI, RETA, Wise, gestoría, plataformas)
- Rates 2026 para TS/React y Go — datos isvidal + benchmarks europeos
- Top 3 riesgos con mitigaciones
- TL;DR de una página

Fuentes verificadas via WebSearch (2026): AEAT sede electrónica, Infoautónomos, wolterskluwer, index.dev European Developer Rates, reactjsdeveloperjobs.com.

**Estado:** en Checkpoint 1. Esperar revisión del usuario antes de abrir Fase 2 (legal.md).

Datos clave confirmados:
- Tarifa plana: 80€/mes, 12 meses, prorroga si rendimientos < SMI
- RETA 2026: congelado desde 2025, rango 200€-590€/mes según rendimientos netos
- ROI: hasta 3 meses aprobación, imprescindible para facturar intracomunitario sin IVA
- IAE 763.1 como epígrafe para developers autónomos
- Falso autónomo: criterios técnicamente aplicables a clientes extranjeros, pero fricción práctica reducida

---

## 2026-04-09 — method: research-only, bottom-up, tracer-bullet first

Phase 1 is a tracer bullet: a single short `briefing.md` covering the entire path
end-to-end so the user can decide if this pursuit fits before deeper investigation.
If the briefing is wrong-oriented, rework is cheap; reworking after 7 deliverables
is not.

Order of deeper phases is bottom-up from what enables everything else:
legal/fiscal → operational → market → contracts → optimization → risk. Horizontal
parallel research was explicitly rejected because it creates inconsistencies
between layers (e.g., platform rates assumed under a fiscal structure that doesn't
apply to the reader).

Each deliverable is capped at roughly 10 pages and lives in a single dedicated
topic — no enciclopedia-style monoliths, no topic duplication across files.
