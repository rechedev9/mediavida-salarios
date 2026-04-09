# Guía completa — Contractor desde España
### Stack: TypeScript / Next.js / React / Go · Perfil: Luis Reche · Abril 2026

> **Disclaimer:** documento de investigación, no asesoría fiscal ni legal. Los datos fiscales reflejan la normativa vigente en abril de 2026. Toda decisión real requiere gestor/abogado especializado.

---

## Índice

1. [Qué es un contractor — glosario](#1-qué-es-un-contractor--glosario)
2. [Por qué solo funciona con cliente extranjero](#2-por-qué-solo-funciona-con-cliente-extranjero)
3. [Análisis de perfil y mercado](#3-análisis-de-perfil-y-mercado)
4. [Rates esperables 2026](#4-rates-esperables-2026)
5. [Marco legal y fiscal](#5-marco-legal-y-fiscal)
6. [Setup operacional — checklist ejecutable](#6-setup-operacional--checklist-ejecutable)
7. [Plataformas y canales de búsqueda](#7-plataformas-y-canales-de-búsqueda)
8. [Mecánica contractual](#8-mecánica-contractual)
9. [Optimización fiscal y alternativas](#9-optimización-fiscal-y-alternativas)
10. [Riesgos y gestión de cashflow](#10-riesgos-y-gestión-de-cashflow)
11. [Plan de ejecución](#11-plan-de-ejecución)
12. [Preparación de entrevista técnica](#12-preparación-de-entrevista-técnica)
13. [Oportunidad de nicho — AI Tooling y MCP](#13-oportunidad-de-nicho--ai-tooling-y-mcp)
14. [Conclusiones](#14-conclusiones)

---

## 1. Qué es un contractor — glosario

| Figura | Qué es | Relevancia |
|---|---|---|
| **Empleado** | Contrato laboral, empresa cotiza por ti. | Referencia de comparación. |
| **Freelance autónomo** | Múltiples clientes, proyectos cortos, precios por proyecto. | Lo que la gente imagina al oír "autónomo". No es lo que buscamos. |
| **TRADE** | Autónomo con >75% de ingresos de un solo cliente. Registro SEPE obligatorio. Solo aplicable con cliente español. | No aplica para contractor con cliente extranjero — más burocracia sin beneficio. |
| **Contractor** | Concepto funcional, no figura legal española. Un cliente, contrato 6-12 meses renovable, jornada L-V. Opera como autónomo ordinario (IAE 763.1). La diferencia está en dónde está el cliente: fuera de España. | Lo que vamos a montar. |

**En la práctica:** eres autónomo español que factura a empresa extranjera bajo un contrato de servicios de 6-12 meses full-time. Fiscalmente no hay ninguna diferencia con un autónomo estándar — las diferencias están en el cliente, el contrato y el rate.

---

## 2. Por qué solo funciona con cliente extranjero

### El falso autónomo

La ley española (Art. 1.2 ET) presume relación laboral cuando concurren:

- **Dependencia:** recibes órdenes, tienes horario impuesto, no decides cómo organizas tu trabajo.
- **Ajenidad:** no asumes riesgo económico, los frutos van íntegramente al cliente.

Con estas dos condiciones durante meses, la ITSS puede reclasificarte como empleado encubierto aunque tengas un contrato mercantil y estés en el RETA. Consecuencias: cotizaciones retroactivas + multas al cliente (€751-10.000 por trabajador).

Con cliente **español** esto es perseguible activamente (ver jurisprudencia Glovo/Deliveroo). La ITSS desde 2025 puede declarar la laboralidad en su acta directamente sin sentencia judicial previa.

### Por qué el cliente extranjero reduce el riesgo

Los mismos criterios legales aplican técnicamente. Lo que cambia es la **fricción operativa**:
- La ITSS tiene jurisdicción española, no francesa, alemana o inglesa.
- Ejecutar una inspección contra una empresa sin presencia en España requiere cooperación administrativa internacional — costosa y sin precedente documentado en el sector tech.
- No hay casos registrados de reclasificación de contractor español con cliente extranjero sin filial en España.

**Matiz:** si la empresa extranjera tiene filial o establecimiento permanente en España, la ITSS recupera jurisdicción directa — mismo riesgo que con cliente español.

### Indicios de laboralidad vs. independencia

| Indicio de laboralidad ❌ | Indicio de independencia real ✅ |
|---|---|
| Email @empresa.com | Email propio |
| Portátil de empresa | Portátil propio |
| Jornada fija impuesta | Horario autodeterminado |
| Tareas asignadas por manager | Entrega de resultado pactado |
| Un solo pagador al 100% | Segunda fuente de ingresos (aunque pequeña) |
| Factura idéntica cada mes | Factura varía con el trabajo entregado |

---

## 3. Análisis de perfil y mercado

### Perfil actual

- **Experiencia:** 2 años.
- **Inglés:** perfecto (C1-C2) — diferenciador real en EU.
- **Stack:** TypeScript, Next.js, React, Go.
- **Situación:** en el paro, sin capitalización del paro.

### Portfolio analizado (github.com/rechedev9)

| Repo | Stack | Lo que demuestra |
|---|---|---|
| **`riskforge`** | Go + GCP Cloud Run + Spanner + Terraform | Fan-out paralelo, hedging adaptativo (EMA p95), circuit breakers, rate limiters por carrier. Arquitectura de producción real. |
| **`gravity-room`** | React 19 + Go API + FastAPI + Docker + Caddy + Prometheus + Playwright | Monorepo full-stack deployado en VPS, JWT con refresh token rotation, E2E tests, métricas. |
| **`nextrespawn`** | Next.js 16 + Auth.js v5 + Prisma + Stripe + Resend | SaaS boilerplate bleeding-edge — versiones más recientes del ecosistema. |
| **`recon-cli`** | Go | CLI tool propio para AI coding assistants — sabe construir tooling, no solo productos. |
| **`tealium-mcp-server`** | TypeScript | MCP server — entiende el protocolo de agentes AI, nicho de 2026. |
| **`honey-encryption-proxy`** | TypeScript | Proxy de seguridad para Claude Code — criterio de seguridad aplicado. |

**Conclusión:** estos no son proyectos de tutorial. `riskforge` en particular (fan-out con hedging basado en EMA p95, circuit breakers, Spanner, Terraform GCP) es un sistema con arquitectura de producción real. El portfolio compite por encima de lo que los años dicen.

### Correcciones urgentes en el GitHub

Antes de aplicar a cualquier sitio — el hiring manager va al GitHub después de ver el perfil:

1. **10 repos sin descripción** (`carrier-gateway`, `gravity-room`, `proyectozack`, etc.) — añadir una línea descriptiva a cada uno.
2. **Pinear los 6 repos más fuertes:** `riskforge`, `gravity-room`, `nextrespawn`, `recon-cli`, `tealium-mcp-server` + uno más.
3. **`gravity-room` README roto** — hay boilerplate de Next.js pegado al final del Stack table. Eliminarlo.
4. **Profile README** — añadir pitch de 3-4 líneas: quién eres, stack, que estás abierto a contratos.

### Foco de mercado recomendado

#### Primario — Go backend contractor

`riskforge` es el anchor. Un hiring manager de insurtech o fintech que vea ese README entiende inmediatamente el nivel. Es el nicho con menos competencia relativa (menos contractors Go que TS) y rates superiores.

**Clientes objetivo:** startups de insurtech, fintech, healthtech, dev tools en DE, NL, UK, FR con backend en Go.

**Pitch:**
> "Go backend engineer with production experience in fan-out architectures, GCP Cloud Run + Spanner, and Terraform. Portfolio includes a multi-carrier insurance quote aggregation system with adaptive hedging and circuit breakers."

#### Secundario — Next.js fullstack

`nextrespawn` + `gravity-room` cubren el stack fullstack moderno: Next.js 16, React 19, Auth.js v5. Las versiones más nuevas del ecosistema son un diferenciador real frente a seniors que siguen en Next.js 13/Pages Router.

**Clientes objetivo:** SaaS B2B startups que necesitan producto completo, 5-30 personas de equipo.

#### Diferenciador de nicho — AI tooling

`tealium-mcp-server` + `shenronSDD` + `honey-encryption-proxy`. Hay creciente demanda de devs que entiendan MCP, tool calling, integraciones Claude/OpenAI. Poca competencia, rates altos cuando encuentras el cliente.

No como perfil principal en Malt, sí como mención en LinkedIn y conversaciones con startups AI-native.

---

## 4. Rates esperables 2026

### Con tu perfil específico

| Momento | Rate orientativo |
|---|---|
| Primer contrato (sin historial contractor) | **€280-380/día** |
| Segundo contrato (con referencia verificable) | €350-450/día |
| Año 2 como contractor | €450-600/día |

*Más alto de lo que sugeriría para 2 años genérico, porque el portfolio es más sólido de lo esperado.*

---

### Datos reales de Malt 2026 — fuente directa

> Los datos de Malt son las tarifas medias diarias de freelancers activos en la plataforma en los últimos 3 meses. Son el benchmark más fiable disponible públicamente porque reflejan lo que realmente se está cobrando, no estimaciones.

#### Malt España — mercado local (referencia, no target)

Los rates de Malt España reflejan clientes españoles. Para contractors con clientes extranjeros son un suelo mínimo, no el objetivo.

| Perfil | 0-2 años | 3-7 años | Experimentado (media) |
|---|---|---|---|
| Backend (general) | €175/día | €243/día | €300/día |
| Fullstack | €172/día | €240/día | €297/día |
| JavaScript/TS | €169/día | €236/día | €291/día |
| **ReactJS** | **€189/día** | **€295/día** | **€334/día** |

Por especialidad en España (experimentados):
- ReactJS: **€451/día** — el más alto del frontend
- Microservices: €338/día
- Fullstack: €326/día
- Node.js: €317/día

*(Malt España, barómetro abril 2026. Fuente: malt.es/t/barometro-tarifas)*

#### Malt Francia — mercado target principal

Francia es el mercado más accesible para contractors españoles (timezone idéntica, proximidad cultural, isvidal trabaja para empresa francesa). Los rates son casi el doble que en España.

| Perfil | 0-2 años | 3-7 años | Experimentado (media) | París |
|---|---|---|---|---|
| Backend (general) | €313/día | €426/día | €561/día | €604/día |
| **ReactJS** | **€302/día** | **€420/día** | **€563/día** | €588/día |
| JavaScript | — | — | €540/día | €567/día |

Por especialidad en Francia (experimentados):
- Microservices: €609/día
- Node.js: €577/día
- Fullstack: **€571/día**
- ReactJS: **€567/día**
- JavaScript: €540/día

*(Malt Francia, barómetro abril 2026. Fuente: malt.fr/t/barometre-tarifs)*

**Perfiles Go observados en Malt Francia:**
- *Vincent Composieux — Tech Lead Full-stack + Go + DevOps + Cloud:* **€750/día** (Annecy, 41 reviews)
- *Dani Gilabert — Go + NodeJS + ReactJS fullstack:* **€382/día** (Palamós, 8 reviews)

Go no tiene categoría propia en el barómetro de Malt España/Francia — aparece bajo "Backend" o "Fullstack". Los profiles con Go listado explícitamente tienen rates 10-30% sobre la media de backend.

#### ¿Qué significa esto para ti con 2 años?

Con 2 años + portfolio de `riskforge` nivel tu target realista en **Malt Francia**:
- **Primer contrato:** €300-380/día (zona "3-7 años" francesa, justificable con portfolio)
- **Con primera referencia:** €380-480/día

**La brecha España/Francia es el argumento más claro para buscar cliente extranjero:** el mismo perfil cobra €189/día en Malt España vs. €302/día en Malt Francia con 0-2 años. Un 60% más por cruzar la frontera virtual.

---

### Benchmark europeo por país (Senior, 2026)

| País | Go backend | TS/React/Next.js |
|---|---|---|
| 🇫🇷 Francia | €65-80/h (~€520-640/día) | €60-75/h (~€480-600/día) |
| 🇩🇪 Alemania | €80-110/h (~€640-880/día) | €75-100/h (~€600-800/día) |
| 🇬🇧 UK | £80-120/h (~£640-960/día) | £70-100/h (~£560-800/día) |
| 🇨🇭 Suiza | CHF 110-150/h | CHF 90-130/h |
| 🇺🇸 US | $90-130/h | $80-120/h |

*Fuentes: index.dev European Developer Rates 2026, IT Jobs Watch UK, isvidal MediaVida.*

### Cuánto se lleva a casa (orientativo, Madrid)

| Facturación anual | Gastos deducibles | Rend. neto IRPF | IRPF aprox. | Neto en mano |
|---|---|---|---|---|
| €60.000 | ~€7.000 | ~€53.000 | ~€14.500 | **~€38.500** |
| €80.000 | ~€7.500 | ~€72.500 | ~€23.000 | **~€49.500** |
| €100.000 | ~€8.000 | ~€86.200 | ~€28.500 | **~€57.700** |

*IRPF varía por CC.AA. Madrid es la más baja (tipo máx. 43,5%). Cataluña/Valencia pueden llegar al 54%.*

---

## 5. Marco legal y fiscal

### Figura: autónomo ordinario

No existe figura legal "contractor" en España. Eres autónomo dado de alta en el RETA (epígrafe IAE 763.1 — Programadores y Analistas de Informática).

### IRPF 2026 — Estimación Directa Simplificada

**Régimen:** estimación directa simplificada (aplicable con facturación < €600.000/año).

**Tramos 2026** (sin cambios respecto a 2025):

| Base liquidable | Tipo marginal estatal | Tipo combinado orientativo |
|---|---|---|
| Hasta 12.450 € | 9,50% | ~19% |
| 12.450 – 20.200 € | 12,00% | ~24% |
| 20.200 – 35.200 € | 15,00% | ~30% |
| 35.200 – 60.000 € | 18,50% | ~37% |
| 60.000 – 300.000 € | 22,50% | ~45% |
| > 300.000 € | 24,50% | ~47% |

**Retenciones:** clientes extranjeros NO retienen IRPF. Debes presentar el **Modelo 130** trimestral (20% del rendimiento neto acumulado). Reservar 30-35% de cada cobro desde el primer día.

**Plazos Modelo 130:**
- Q1: 1-20 abril
- Q2: 1-20 julio
- Q3: 1-20 octubre
- Q4: 1-30 enero del año siguiente

**Deducción extra (estimación simplificada):** 5% del rendimiento neto en concepto de gastos de difícil justificación, límite €2.000/año — sin factura requerida.

### IVA — tres casuísticas

#### Cliente empresa en la UE (reverse charge)
- **Base legal:** Art. 44 Directiva 2006/112/CE + Art. 69 Ley 37/1992.
- **Factura:** 0% IVA. Mención obligatoria: *"Inversión del sujeto pasivo — Art. 44 Directiva 2006/112/CE"*.
- **Requisitos:** estar dado de alta en el ROI + verificar NIF-IVA del cliente en VIES + declarar en Modelo 349.
- **Modelos:** 303 (trimestral) + 349 (operaciones intracomunitarias).

#### Cliente fuera de la UE (UK, EE.UU., Suiza, etc.)
- **Base legal:** Art. 69.Uno.1° Ley 37/1992. UK es tercer país desde el Brexit (2021).
- **Factura:** 0% IVA. Mención: *"Operación no sujeta — Art. 69.Uno.1° Ley 37/1992"*.
- **Modelos:** solo 303 (casilla 120). No necesitas ROI ni Modelo 349.
- **Distinción crítica:** "no sujeta" ≠ "exenta" — usar el término incorrecto en el 303 puede costar la deducción del IVA de tus gastos.

### RETA 2026

**Sistema de 15 tramos** por rendimiento neto mensual (congelado respecto a 2025 — RD Ley 3/2026):

| Rend. neto mensual | Cuota mínima |
|---|---|
| < 670 € | 200 €/mes |
| 670 – 900 € | 220 €/mes |
| 901 – 1.166 € | 260 €/mes |
| 1.700 – 2.030 € | 350 €/mes |
| 2.330 – 2.760 € | 423 €/mes |
| 3.620 – 4.050 € | 530 €/mes |
| > 6.000 € | 590 €/mes (máx.) |

**Tarifa plana:** 80€/mes (~€88,72 con MEI) durante 12 meses si es tu primera alta o llevas >2 años sin estar en el RETA. Prorrogable otros 12 meses si rendimientos < SMI. Solicitar en el momento del alta (TA.0521) — no se puede pedir retroactivamente.

**La cuota RETA es 100% deducible en IRPF.**

### ROI — el trámite más urgente

El **Registro de Operadores Intracomunitarios** (casilla 582 del Modelo 036) es imprescindible para facturar a clientes EU sin IVA. La AEAT tarda hasta **3 meses** en aprobarlo. Sin ROI, tienes que facturar con IVA español (21%) y luego rectificar.

**Solicitar el ROI el día del alta**, aunque el primer cliente sea de UK o US (sin ROI). Si el primer cliente es EU, el ROI es crítico.

### Deducciones típicas

| Gasto | IRPF | IVA | Condición |
|---|---|---|---|
| Cuota RETA | 100% | — | Obligatoria |
| Gestoría | 100% | 100% | Factura a tu nombre |
| Equipos informáticos | 100% | 100% | Uso exclusivo profesional |
| Software / herramientas | 100% | 100% | Uso profesional |
| Internet (línea exclusiva) | 100% | 100% | Solo uso profesional |
| Internet (mixta) | 50% | 50% | Criterio Hacienda |
| Formación técnica | 100% | 100% | Vinculada a la actividad |
| Coworking | 100% | 100% | Factura a tu nombre |
| RC profesional | 100% | 100% | Relacionado con actividad |
| Seguro médico privado | Hasta 500€/año | — | Deducción en renta |
| Suministros vivienda | 30% × % superficie afecta | 30% × % afecta | Requiere declaración en 036 |

### Obligaciones periódicas

| Modelo | Periodicidad | Qué declara |
|---|---|---|
| 303 | Trimestral | IVA |
| 349 | Trimestral (o mensual si >€50.000 intracomunitario) | Operaciones EU B2B |
| 130 | Trimestral | Pago fraccionado IRPF |
| 390 | Anual | Resumen IVA |
| Renta | Anual | Liquidación definitiva IRPF |

---

## 6. Setup operacional — checklist ejecutable

### Paso 1 — Alta censal: Modelo 036 en la AEAT

El Modelo 037 (simplificado) fue **suprimido** por Orden HAC/1526/2024 (BOE enero 2025). Solo existe el 036.

**Campos clave:**

| Casilla | Qué declaras |
|---|---|
| 110 | Alta (primera vez) |
| 403 | Fecha de inicio de actividad |
| 407 | IAE: **763** (subapartado 763.1 — Programadores y Analistas) |
| — | CNAE: **6201** (Programación informática) |
| **582** | ✅ Solicitud ROI |
| **584** | Fecha desde la que solicitas el ROI (misma que inicio) |
| 501 | Régimen IVA: general |
| 700 | Régimen IRPF: estimación directa simplificada |

**Cómo presentar:** online en `sede.agenciatributaria.gob.es` con certificado digital o Cl@ve (recomendado), o presencial en delegación AEAT.

### Paso 2 — Alta RETA

Simultánea al 036 o dentro de los 30 días naturales siguientes. Online en `importass.seg-social.es`.

**Formulario TA.0521:**
- ✅ Marcar **tarifa plana** (80€/mes primer año).
- ✅ Incluir contingencia de **IT** (incapacidad temporal) — sin ella no cobras si te pones enfermo.
- Base de cotización: tramo más bajo inicialmente. Ajustable 6 veces al año.

### Paso 3 — Cuenta bancaria business

**Setup recomendado (dos cuentas):**

1. **Wise Business** (cobros internacionales): IBANs en EUR, GBP, USD. Tipo de cambio mid-market sin margen. Sin cuota mensual. IBAN belga — el SEPA obliga a aceptarlo. Abrir en `wise.com/es/business`.

2. **Cuenta española secundaria** (domiciliaciones): Revolut Business o Openbank Empresas. Para domiciliar la cuota RETA y pagos locales.

### Paso 4 — Gestoría

**Precio objetivo:** €60-100/mes. Gestiona: 303, 349, 130, 390, Renta.

**Preguntas para elegir:**
1. "¿Lleváis autónomos con clientes extranjeros (reverse charge intracomunitario + Art. 69.Uno.1 LIVA)?"
2. "¿Presentáis el Modelo 349 mensual si supero €50.000 intracomunitario?"
3. "¿Ayudáis a hacer el seguimiento del ROI hasta aprobación?"
4. "¿Cuál es la cuota mensual para autónomo sin empleados, facturación B2B internacional?"

**Red flags:** no saben qué es el Modelo 349, confunden "exento" con "no sujeto", nunca han llevado a un autónomo con cliente extranjero.

### Paso 5 — Plantilla de factura

**Campos obligatorios (RD 1619/2012):**
```
- Número y serie (ej. INT-2026-001 para internacionales)
- Fecha de expedición
- Nombre y NIF del emisor (tú)
- NIF-IVA del emisor: ES + tu NIF (ej. ES12345678A) — para EU B2B
- Nombre, NIF-IVA y dirección del cliente
- Descripción del servicio y período
- Importe base
- Mención de IVA (exención/no sujeción con base legal)
- Importe total
```

**Mención según destino:**
- Cliente EU: `"IVA: 0% — Inversión del sujeto pasivo — Art. 44 Directiva 2006/112/CE"`
- Cliente UK/US: `"IVA: no sujeta — Art. 69.Uno.1° Ley 37/1992"`
- **Nunca poner solo "IVA: 0%"** sin base legal.

---

## 7. Plataformas y canales de búsqueda

### Plataformas contractor

| Plataforma | Acceso con 2 años | Fee al dev | Notas |
|---|---|---|---|
| **Malt** (malt.es) | ✅ Sin filtro de seniority | 0-10% | La más activa en España y Francia. Primera opción. |
| **Honeypot** (DACH) | ✅ Posible con portfolio sólido | Sin fee | Empresas alemanas te contactan a ti. Muy recomendado para target DE/AT. |
| **YunoJuno** (UK) | ✅ Posible | ~15% al cliente | Mercado UK en GBP. |
| **Landing.Jobs** | ✅ | Variable | Mix job board + plataforma. Fuerte en ES/PT y DACH. |
| **Toptal / Arc.dev** | ⚠️ Difícil | Sin fee al dev | Vetting selectivo — probable rechazo con 2 años sin historial. |

### Canales directos

| Canal | Frecuencia | Cómo usar |
|---|---|---|
| **LinkedIn** | Continuo | Activar "Open to Contract". Buscar con filtro "Contract" + stack + Remote. |
| **HN Who is Hiring** | 1er día del mes | Buscar "contract", "remote", "TypeScript", "Go". Responder directamente al comentario. |
| **WeWorkRemotely** | Continuo | Sección "Contract Gigs". Clientes principalmente US. |
| **OTTA** | Continuo | Scaleups EU. Filtro "contract". |
| **Cord.co** | Continuo | Dev-centric, UK/EU, contratos frecuentes. |

### Proceso de selección — qué esperar

1. **Screening (recruiter):** 20-30 min. Rate esperado, disponibilidad, timezone, tipo de contrato.
2. **Entrevista técnica (tech lead):** 45-90 min. Arquitectura, decisiones de diseño. Para Go: concurrencia, context, interfaces. Para TS: generics, RSC, hooks.
3. **System design (senior):** 60 min. Diseñar un sistema. Con `riskforge` en el CV, es tu terreno.
4. **Take-home / pair programming:** 3-4h max para contractors.
5. **Culture fit:** trabajo remoto, autonomía, comunicación asíncrona.
6. **Oferta:** rate, duración, vacaciones, notice period.

**Mencionar desde el primer contacto que buscas contrato**, no empleo fijo. Pregunta: *"Is this role open to contractors working through a service agreement, or strictly FTE?"*

---

## 8. Mecánica contractual

### Estructura MSA + SOW

**MSA (Master Service Agreement):** marco general de la relación. Se negocia una vez. Cubre: IP, confidencialidad, liability, non-compete, terminación, ley aplicable.

**SOW (Statement of Work):** acuerdo específico de cada contrato. Cubre: scope, rate, duración, notice period, payment terms.

En conflicto: el MSA prevalece en asuntos legales; el SOW en condiciones operativas.

### Cláusulas críticas

**IP (la más importante):**
- La cesión aplica solo al trabajo producido dentro del scope del SOW.
- Tu IP preexistente no se cede — se licencia.
- Librerías open source incorporadas: bajo sus propias licencias, no cedidas.

**Indemnification:**
- Exigir **cap de responsabilidad** = fees pagados en los últimos 12 meses.
- Sin cap, respondes por daños ilimitados por cualquier bug. Inaceptable.

**Non-compete:**
- Máximo 6 meses post-contrato. Un año ya es excesivo.
- Scope acotado: solo competidores directos definidos por nombre.
- Sin compensación económica: difícil de ejecutar en la mayoría de jurisdicciones europeas.

**Payment terms:**
- Net 30 aceptable. Net 60+ negociar a la baja — no aceptar.
- Facturación mensual para contratos de 6-12 meses.

**Notice period:**
- Mínimo 4 semanas en ambas direcciones.
- Para contratos de 6+ meses: 4-8 semanas.
- Sin notice period, el cliente puede cancelar de un día para otro.

### IVA en facturas — resumen rápido

| | EU B2B | No-UE B2B |
|---|---|---|
| IVA | 0% reverse charge | 0% no sujeta |
| Base legal | Art. 44 Dir. 2006/112/CE | Art. 69.Uno.1° LIVA |
| ROI necesario | ✅ | ❌ |
| VIES check | ✅ | ❌ |
| Modelo 349 | ✅ | ❌ |

### Ciclo de cobro

```
Fin de mes → enviar timesheet (si aplica) → aprobación cliente (2-5 días)
→ emitir factura → esperar payment terms (Net 30)
→ cobro en Wise → transferir 30-35% a cuenta Hacienda ese mismo día
```

### Si no pagan

1. **D+1:** email amistoso al contacto de finanzas + manager.
2. **D+7:** reclamación formal por email fehaciente (aceptado por AEAT desde 2024).
3. **D+30 (cliente EU):** proceso monitorio europeo — Reglamento CE 1896/2006. Para deudas < €5.000: Reglamento CE 861/2007 (escasa cuantía). Funciona bien en DE/AT, lento en FR/IT.
4. **Recuperar IVA ante AEAT:** si la factura es incobrable y has agotado las vías de reclamación documentadas.
5. **+40€ por factura impagada:** compensación por gastos de gestión (Art. 6.1 Directiva 2011/7/UE).

---

## 9. Optimización fiscal y alternativas

### Autónomo vs. SL — break-even 2026

| Beneficio neto anual | Recomendación |
|---|---|
| < €40.000 | Autónomo. Tarifa plana, menor coste fijo. |
| €40.000 – €70.000 | Zona gris — analizar con gestor. |
| > €70.000 | SL empieza a compensar si no distribuyes todo el beneficio. |

**Coste oculto de la SL:** autónomo societario no tiene tarifa plana (cuota mínima ~€310/mes vs. €88 de tarifa plana), gestoría más cara (~€120-150/mes), constitución €1.000-3.000, capital social mínimo €3.000.

**Conclusión:** autónomo ordinario para los primeros 1-2 años. La SL es una optimización posterior con facturación estable > €80.000.

### Deducciones avanzadas — los límites reales

- **Vehículo:** prácticamente imposible de deducir para developer en estimación directa. Hacienda presupone uso mixto.
- **Vivienda:** 30% × % de metros afectos a la actividad. Con habitación de 20m² en piso de 100m² = 6% de suministros. Ahorro real: ~€50-100/año. Requiere declaración previa en el 036.
- **Plan de pensiones:** límite €1.500/año individual + €4.250 planes de empleo autónomos (PPSPA) = €5.750/año total deducible.

### Alternativas de residencia fiscal

> ⚠️ Requieren asesoría fiscal especializada. La mudanza mal ejecutada = doble imposición o exit tax.

**Portugal — IFICI (NHR 2.0):**
- 20% tipo fijo sobre rentas portuguesas, exención rentas extranjeras (excepto pensiones), 10 años.
- Programadores y especialistas TIC explícitamente incluidos.
- **Problema para contractor puro:** requiere empresa con sustancia en Portugal. Como autónomo facturando directamente a clientes extranjeros, el acceso es complicado.
- Titulación EQF nivel 6 (licenciatura) + 3 años experiencia, o doctorado.

**Andorra:**
- IRPF: 0% hasta €24.000 / 5% hasta €40.000 / **10% máximo**.
- Residencia activa: empresa andorrana con ≥34% capital, ser administrador, fianza €50.000 (recuperable), >183 días/año físicos en Andorra.
- **Ahorro real a €80.000/año:** ~€22.000/año vs. Madrid.
- **Coste real:** vivienda €800-1.500/mes, CASS ~€200/mes, seguro médico obligatorio, gestión empresa. Y 183 días físicos fuera de España.

**Chipre — Non-Dom:**
- IS: 12,5%. Exención dividendos e intereses bajo Non-Dom.
- Banking con reputación más compleja. Algunos compliance officers de grandes empresas lo ven como señal de alerta.
- Mínimo 60 días/año en Chipre (si no tienes residencia en otro país).

**Beckham Law:** solo para impatriados. **No aplica** a residentes ya en España.

---

## 10. Riesgos y gestión de cashflow

### Seguros

**RC Profesional (imprescindible):**
- Cobertura mínima: **€300.000**, con E&O (Errors & Omissions) y ciberriesgos.
- Precio 2026: **€200-400/año** para esa cobertura.
- Aseguradoras: Hiscox (referencia europea tech), Berkley (mejor ciberriesgos), Mapfre.
- 100% deducible. Los clientes corporativos la exigen.

**Salud privada:**
- €50-100/mes. Deducible hasta €500/año/persona en IRPF.
- Útil porque la cobertura RETA para especialistas y pruebas de imagen tiene esperas largas.

**IT (Incapacidad Temporal):**
- Ya incluida en la cuota RETA desde 2019. Cubre desde el 4° día de baja.
- Con contratos day-rate, los días de baja = días sin cobrar. Considerar seguro complementario (~€20-50/mes).

### Fondo de emergencia

**Cuánto:** mínimo 3 meses de gastos. Recomendado: **6 meses**.

¿Por qué 6 meses?
- Cancelación con 4 semanas de aviso + búsqueda 4-6 semanas + primer cobro Net 30 = potencialmente 3 meses en seco.
- Pueden encadenarse dos situaciones adversas.

**Cálculo ejemplo:** gastos personales €1.800 + RETA €423 + gestoría €80 + seguros €35 = €2.338/mes → fondo de 6 meses: **~€14.000**.

### Buffer de impuestos

**Regla:** transferir el **30-35% de cada cobro** a una cuenta separada ("cuenta Hacienda") el mismo día que llega.

Con clientes EU en reverse charge no cobras IVA — el 30-35% va íntegramente a cubrir el IRPF del Modelo 130 + ajuste en la Renta anual.

### Downtime entre contratos

**Coste real de 1 mes sin contrato:** 0€ ingresos + €2.338 gastos fijos = pérdida real.

**Regla:** empezar a buscar el siguiente contrato cuando al actual le quedan **6-8 semanas**, no cuando termina.

### El cese de actividad autónomos — realidad

**No es comparable al paro del asalariado.** El fin natural de un contrato de 6 meses que no se renueva **no cualifica** como cese involuntario. Para acceder a la prestación de cese de actividad se necesitan causas económicas/técnicas/productivas acreditadas y ≥12 meses cotizados de esa contingencia.

**No cuentes con ello como red de seguridad.** Cuenta con el fondo de emergencia.

### Diversificación

Mantener al menos una segunda fuente de ingresos (aunque pequeña) que rompa el 100% de dependencia de un cliente. Reduce el riesgo de falso autónomo y el riesgo de cashflow simultáneamente.

---

## 11. Plan de ejecución

### Situación de partida

- En el paro (sin capitalización — decisión tomada).
- Portfolio sólido, GitHub necesita ajustes de presentación.
- Sin historial como contractor aún.

### Timeline

```
Semana 1 (esta semana):
├── Contratar gestoría — llamar a 2-3 con el checklist de preguntas
├── Abrir Wise Business
├── Arreglar GitHub: descriptions, repos pinados, gravity-room README, profile README
└── Activar perfil LinkedIn en modo "Open to Contract"

Semana 2:
├── Presentar Modelo 036 (con la gestoría o solo online)
│   → IAE 763.1 + solicitar ROI (casilla 582)
├── Alta RETA — tarifa plana 80€/mes
└── Crear perfil en Malt con rate €280-320/día

Semana 2-3:
├── Primeras candidaturas:
│   ├── Malt — proyectos publicados + perfil visible
│   ├── LinkedIn — búsqueda manual "Go contract remote", "Next.js contract"
│   ├── HN Who is Hiring (primer día del próximo mes)
│   └── WeWorkRemotely — Contract Gigs
└── Preparar kit de entrevista (pitch 2 min, 3-5 ejemplos de trabajo)

Mes 2-3:
├── ROI aprobado (si AEAT va rápido)
├── Primeras entrevistas
└── Objetivo: primer contrato firmado en semana 6-12 desde candidaturas

Mes 3-4:
└── Primera factura emitida
```

### Acciones concretas de esta semana

1. **Contratar gestoría** — es el paso más importante porque te guiará en el 036. Llama a 2-3 esta semana con el checklist de preguntas de la sección 6.

2. **Abrir Wise Business** — proceso 100% online, 1-3 días hábiles. `wise.com/es/business`.

3. **Arreglar el GitHub** — antes de que cualquier hiring manager lo vea:
   - Añadir descripción a todos los repos (una línea).
   - Pinear `riskforge`, `gravity-room`, `nextrespawn`, `recon-cli`, `tealium-mcp-server` + uno más.
   - Eliminar el boilerplate de Next.js del final del README de `gravity-room`.
   - Escribir un profile README con pitch de 3-4 líneas.

4. **LinkedIn** — activar "Open to Work" → Contract/Freelance. Actualizar el titular.

### Rate de entrada recomendado

**Malt:** €300/día como rate inicial visible. Es negociable y sitúa el perfil en zona mid (no junior, no top-tier sin historial). Ajustar a €350-380 cuando lleguen las primeras conversaciones y veas la reacción del mercado.

**Para el primer contrato:** si un cliente interesante ofrece €250-270/día, vale la pena aceptar una vez para tener la primera referencia verificable. Establecer el suelo rápido — no aceptar un segundo contrato por debajo del target.

---

---

## 12. Preparación de entrevista técnica

### Go/Golang — preguntas habituales

Las entrevistas de Go contractor se centran en dos ejes: **arquitectura de sistemas concurrentes** y **decisiones de diseño**. Con `riskforge` en el CV, es muy probable que profundicen en fan-out, hedging y circuit breakers — te preguntarán cómo lo hiciste y por qué.

#### Temas a dominar (ordenados por frecuencia)

| Tema | Nivel | Lo que suelen preguntar |
|---|---|---|
| Goroutines vs OS threads | Básico | Diferencias de peso, gestión por el runtime, escalado a miles |
| Channels buffered/unbuffered | Básico | Cuándo usar cada uno, qué pasa si el buffer está lleno |
| `select` statement | Intermedio | Cómo manejar múltiples channels, el caso `default` |
| `context.Context` | Intermedio | Cancelación, deadlines, propagación por goroutines |
| `sync.Mutex` / `RWMutex` / `WaitGroup` | Intermedio | Cuándo usar mutex vs channel, diferencia Read/Write mutex |
| Race conditions y race detector | Intermedio | Cómo detectar, por qué los maps no son thread-safe |
| `sync.Map` | Intermedio | Cuándo preferir a map + mutex |
| Patrones: fan-out, pipelines, worker pools | Avanzado | Implementar, gestionar backpressure, cancelación limpia |
| Scheduler GMP model | Avanzado | G (goroutine), M (OS thread), P (processor) |
| `pprof` y profiling | Avanzado | Identificar goroutine leaks, memory pressure |

#### Preguntas concretas frecuentes

```
1. ¿Cómo implementarías un worker pool con N workers y cancelación limpia?
2. ¿Cuándo usas channels vs mutexes para sincronización?
3. ¿Qué pasa si escribes en un channel cerrado? ¿Y si lees de uno?
4. ¿Cómo propagas cancelación a través de una cadena de goroutines?
5. ¿Por qué los maps estándar de Go no son safe para concurrencia?
6. ¿Cómo diseñarías un circuit breaker en Go? (relevante con riskforge)
7. ¿Cuál es la diferencia entre panic/recover y error handling?
8. ¿Cómo detectas y evitas goroutine leaks en producción?
```

#### Tu ventaja con riskforge

`riskforge` implementa fan-out paralelo con hedging adaptativo (EMA p95), circuit breakers y rate limiters por carrier. Puedes responder las preguntas de concurrencia con código real que has escrito y decisiones concretas que tomaste. Esto pesa mucho más que respuestas teóricas.

Prepara la narrativa: *"En riskforge implementé un fan-out a múltiples carriers en paralelo. El hedging funciona calculando el p95 de latencia con EMA para cada carrier y lanzando una request alternativa cuando un carrier supera su umbral. El circuit breaker tiene tres estados..."*

---

### Next.js / React — preguntas habituales

Las entrevistas frontend/fullstack para contractors europeos se enfocan en arquitectura RSC y performance, no en sintaxis básica.

| Tema | Lo que preguntan |
|---|---|
| React Server Components | Cuándo un componente debe ser server vs client, por qué |
| Next.js App Router vs Pages Router | Trade-offs, cuándo migrar, qué se gana |
| Streaming y Suspense | Cómo mejora TTFB, `loading.tsx`, streaming de datos |
| Hidratación y "waterfall" | Qué es el JS waterfall, cómo evitarlo con RSC |
| `use server` / Server Actions | Cuándo usar, seguridad, validación server-side |
| Performance (Core Web Vitals) | LCP, CLS, FID — cómo medir y mejorar |
| Auth patterns en Next.js | Auth.js v5, middleware, session edge runtime |
| Testing | Vitest, Testing Library, Playwright — estrategia de tests |
| TypeScript avanzado | Generics, `satisfies`, type inference, conditional types |

---

### System Design — con perfil Go + Next.js

Para contratos senior, el system design es casi universal en empresas de 50+ personas. Con tu stack, los escenarios típicos:

- *"Diseña una API de notificaciones en tiempo real para 100k usuarios"* → WebSockets/SSE, fan-out, cola de mensajes.
- *"Diseña un sistema de rate limiting para una API pública"* → Token bucket (ya tienes implementado en riskforge), sliding window.
- *"Diseña el backend de un sistema de pagos con múltiples providers"* → Patrón similar a riskforge: fan-out, retry, idempotencia, reconciliación.

En estas preguntas usa riskforge como punto de referencia — ya tienes el modelo mental.

---

## 13. Oportunidad de nicho — AI Tooling y MCP

### El mercado MCP en 2026

El **Model Context Protocol (MCP)**, lanzado por Anthropic en noviembre 2024 y ahora bajo la Linux Foundation, se ha convertido en el estándar de facto para integrar LLMs con herramientas externas. En 18 meses pasó de 100.000 a 8 millones de descargas mensuales. Gartner predice que el 75% de los gateway vendors tendrán soporte MCP en 2026.

Esto crea un nicho contractor emergente: **devs que saben construir MCP servers e integrar LLMs en sistemas existentes**.

### Por qué tu portfolio te posiciona aquí

- `tealium-mcp-server` — MCP server real, funcional, no un tutorial.
- `honey-encryption-proxy` — proxy de seguridad para Claude Code, entiende el protocolo de agentes.
- `shenronSDD` — herramienta de Spec-Driven Development para Claude Code.

Estos tres repos juntos dicen: *"Este dev entiende cómo funcionan los agentes AI internamente, no solo cómo llamar a una API."*

### Cómo monetizarlo como contractor

**No es el perfil principal de Malt** — los clientes que buscan MCP aún no buscan con ese término. Pero en **LinkedIn y HN Who is Hiring**, hay creciente volumen de startups AI-native que buscan:
- Devs que puedan integrar Claude/GPT-4 en sistemas Go/TS existentes.
- Constructores de MCP servers para sus productos internos.
- "AI Engineer" con experiencia en tool calling y agentes.

El rate de estos roles es 20-40% superior al backend genérico porque la oferta es escasa.

**Dónde buscarlo:**
- LinkedIn: "AI Engineer", "LLM integration", "MCP developer", "AI tooling"
- HN Who is Hiring: buscar "MCP", "agents", "Claude", "tool use"
- Wellfound (AngelList): startups AI Series A/B que buscan integración

**Cómo presentarlo:**
No pongas "MCP developer" en el titular — es demasiado nicho para que los filtros lo encuentren. Pon en la descripción del perfil una mención a integración de LLMs y enlaza a `tealium-mcp-server`. Quien busque activamente MCP lo encontrará; quien no sepa qué es no lo penalizará.

### Job boards Go específicos

Además de los canales genéricos, estos son específicos para posiciones Go:

| Board | URL | Tipo de roles |
|---|---|---|
| **GolangProjects** | golangprojects.com | Backend Go, remote EU |
| **ReadyToTouch** | readytotouch.com/golang | FinTech, InsurTech, infra Go |
| **RemoteOK** | remoteok.com/remote-golang-jobs | Global remote |
| **Wellfound** | wellfound.com/role/r/golang-developer | Startups globales |
| **Working Nomads** | workingnomads.com/remote-golang-jobs | Remote only |

### Cómo funciona el algoritmo de Malt (para optimizar el perfil)

- El algoritmo contacta ~30 freelancers por búsqueda. Aparecer en esos 30 requiere: perfil completo con keywords técnicas específicas, disponibilidad actualizada, y actividad reciente (conectarte al menos 1 vez al mes).
- Si no te conectas en un mes, el algoritmo para de enviarte mensajes.
- **Keywords que importan:** ser "desarrollador backend" es genérico. Añadir "Go", "Golang", "Next.js 16", "App Router", "React Server Components" mejora la precisión del matching.
- **Responder siempre** a los mensajes (aunque rechaces el proyecto) mejora el score del algoritmo — no penaliza el rechazo.
- Las primeras reseñas son críticas. Considera hacer un proyecto pequeño a precio reducido para conseguir las primeras 3-5 valoraciones que desbloquean visibilidad.

---

## 14. Conclusiones

### Lo que dicen los datos reales de Malt

La fuente más fiable para rates en Europa son los barómetros de Malt (datos en tiempo real, abril 2026), no los benchmarks de informes de terceros. Lo que muestran para tu perfil:

**La brecha España/Francia es el argumento central para buscar cliente extranjero:**

| Perfil | Malt España 0-2 años | Malt Francia 0-2 años | Diferencia |
|---|---|---|---|
| Backend general | €175/día | €313/día | +79% |
| ReactJS | €189/día | €302/día | +60% |
| Experimentado (media) | €300-334/día | €561-563/día | +67-87% |

El mismo trabajo, en el mismo idioma (inglés), facturado a un cliente francés en lugar de español: +60-80% de ingresos. Esa es la matemática del modelo contractor.

**Tu portfolio te sube de tramo en Malt Francia:** con 2 años de experiencia en papel pero `riskforge` en el portfolio, te posicionas en la zona "3-7 años" francesa (€426/día de media) en lugar de "0-2 años" (€313/día). El portfolio compensa la falta de años nominales.

**Perfiles Go observados directamente en Malt Francia:**
- Tech lead Go + DevOps + Cloud: **€750/día** (41 reviews)
- Fullstack Go + React: **€382/día** (8 reviews — comparable a tu entry point)

Go no tiene categoría propia en el barómetro — aparece bajo "Backend" o "Fullstack". Los perfiles con Go listado explícitamente cobran 10-30% sobre la media de backend de su tramo.

---

### El stack que más renta para tu situación específica

Con 2 años, inglés perfecto y el portfolio que tienes, el orden de prioridad óptimo es:

1. **Go backend** (anchor: `riskforge`) — menor competencia, rates superiores, `riskforge` es el argumento concreto para convencer a un hiring manager de que llevas 2 años pero piensas como senior. El nicho fintech/insurtech en FR/DE/UK paga el premium más alto.

2. **Next.js fullstack** (anchor: `nextrespawn` + `gravity-room`) — más demanda, más fácil de vender, pero más competencia. Next.js 16 + App Router + React 19 te diferencia de seniors desactualizados en el Pages Router.

3. **AI tooling / MCP** (anchor: `tealium-mcp-server`) — nicho emergente con oferta escasa. Rates 20-40% superiores al backend genérico cuando encuentras el cliente AI-native. No para el primer contrato, sí para mencionar en conversaciones y como diferenciador en LinkedIn.

---

### Preparación de entrevista — síntesis de lo crítico

Para que el primer contrato lleve rate de "3-7 años" en lugar de "0-2 años", hay que pasar las entrevistas en ese nivel. Los puntos donde `riskforge` te da ventaja directa:

**Go (lo que preguntarán con tu CV):**
- Fan-out paralelo: cómo lanzas N goroutines y recoges resultados — ya lo tienes implementado.
- Hedging adaptativo: calculaste p95 con EMA para detectar carriers lentos — explícalo con código real.
- Circuit breakers: tres estados, transiciones, reset automático — explícalo con lo que hiciste.
- Context: cómo propagas cancelación a través de la cadena de goroutines del fan-out.

Prepara la narrativa de `riskforge` en 3-4 minutos: qué problema resuelve, cómo funciona el fan-out, por qué el hedging, qué aprendiste. Esa narración vale más que 20 respuestas teóricas.

**Next.js (lo que diferencia del resto):**
- Server Components vs Client Components: cuándo cada uno y por qué — la mayoría lo confunde.
- Streaming con Suspense: cómo reduce el TTFB percibido.
- Auth.js v5 con edge runtime: lo tienes en `nextrespawn` — es bleeding edge en 2026.

---

### Correcciones urgentes del GitHub antes de aplicar

El GitHub es el primer sitio que visita un hiring manager. Estos problemas específicos dañan la primera impresión:

1. **10 repos sin descripción** — sin una línea descriptiva, el perfil parece descuidado.
2. **`gravity-room` tiene boilerplate de Next.js pegado** al final del README — eliminar.
3. **Profile README** (`rechedev9`) — necesita un pitch de 3-4 líneas con stack y disponibilidad.
4. **Repos pinados** — actualmente cualquiera puede ver primero repos irrelevantes. Pinear: `riskforge`, `gravity-room`, `nextrespawn`, `recon-cli`, `tealium-mcp-server`, `portfolio`.

Ninguna de estas correcciones requiere escribir código — solo texto. Son la inversión de menor coste y mayor retorno antes de enviar la primera candidatura.

---

### El primer mes — qué hacer en qué orden

```
Esta semana:
├── Arreglar GitHub (descriptions, pins, profile README, gravity-room)
├── Contratar gestoría (llamar a 2-3 con el checklist de preguntas)
└── Abrir Wise Business

Semana 2:
├── Modelo 036 + alta RETA (tarifa plana 80€/mes)
├── Crear perfil Malt con rate €300-320/día
└── Activar LinkedIn "Open to Contract"

Semana 3-4:
├── Candidaturas activas: Malt FR, LinkedIn, HN Who is Hiring (1 mayo)
└── Preparar pitch narrativo de riskforge (3-4 minutos, en inglés)

Objetivo realista:
└── Primer contrato firmado entre semana 6 y semana 12 desde las primeras candidaturas
```

---

### Los números finales

Con el primer contrato en zona **€300-380/día**, 200 días facturables al año:

| Escenario | Facturación | Gastos deducibles | Neto IRPF | IRPF Madrid | **Neto en mano** |
|---|---|---|---|---|---|
| **Conservative** (€300/día) | €60.000 | ~€7.000 | ~€53.000 | ~€14.500 | **~€38.500** |
| **Base** (€340/día) | €68.000 | ~€7.000 | ~€61.000 | ~€18.000 | **~€43.000** |
| **Optimista** (€380/día) | €76.000 | ~€7.500 | ~€68.500 | ~€21.000 | **~€47.500** |

Año 2 con referencia y rate €450/día × 210 días → neto en mano ~€65.000.

Para comparación: el salario neto mediano de un programador con 2 años en España según el hilo de MediaVida (231 registros, mediana €38.711 bruto €2026) es ~€28.000-30.000 netos. El modelo contractor duplica eso desde el primer año si consigues el primer contrato.

---

*Investigación realizada en abril 2026. Fuentes: AEAT sede electrónica, Seguridad Social, Infoautónomos, Holded, taxdown.es, index.dev European Developer Rates 2026, IT Jobs Watch UK, remotepass.com, riseworks.io, posts #2659 #2662 #2671 de isvidal en MediaVida, github.com/rechedev9, Malt barómetro España (malt.es/t/barometro-tarifas, abril 2026), Malt barómetro Francia (malt.fr/t/barometre-tarifs, abril 2026), GolangProjects, a16z MCP deep dive, Gartner MCP forecast 2026, tabla salarial MediaVida scrapper/salarios_tabla.parquet.*
