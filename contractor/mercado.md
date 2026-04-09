# W3 — Mercado y canales para contractor TS/Go desde España

> **Disclaimer:** documento de investigación, no asesoría. Los datos de rates son benchmarks orientativos de fuentes públicas (abril 2026); los rates reales varían por empresa, proyecto, nivel de inglés, historial y momento del mercado. Negocia siempre con información actual.

---

## 1. Dónde buscan contractors las empresas europeas

El mercado contractor europeo llega por tres vías: plataformas especializadas, búsqueda directa (LinkedIn + job boards), y headhunters especializados en contratos.

### 1.1 Plataformas contractor

Estas plataformas son la vía más estructurada: vetting del candidato, matching automático con clientes, contratos gestionados por la plataforma, pagos seguros. La plataforma cobra una comisión al dev (deducida del rate acordado) o al cliente.

| Plataforma | Mercado principal | Stack fuerte | Fee al dev | Vetting | Notas |
|---|---|---|---|---|---|
| **Malt** | Francia, España, DE, NL, BE, Nordics | TS/React, fullstack | 0–10% | Perfil verificado (datos básicos) | La más activa en España. Clientes desde startups hasta enterprise. Solicitud espontánea o inbound. |
| **Toptal** | Global (US, EU) | Todos los stacks | Sin fee al dev | Muy selectivo (~3% aceptados). Multi-etapa: problem solving, entrevista, proyecto de prueba | Rates más altos. Proceso de admisión largo (4-8 semanas). Una vez dentro, el matching es rápido. |
| **Arc.dev** | Global | Fullstack, backend | Sin fee al dev | Top 2% declarado. Video + live coding | Matching en 24-72h tras admisión. Rates: $60-110+/h. Clientes principalmente startups US. |
| **Lemon.io** | Global | React, Node, Fullstack | Comisión al cliente | Vetting básico + entrevista | Nicho: startups early-stage. Rates más moderados. |
| **Honeypot** (ahora parte de Xing/DACH) | Alemania, Austria, Suiza | Backend, fullstack | Sin fee al dev | CV + brief de habilidades | Empresas alemanas buscan activamente a los devs, no al revés. Muy recomendado para target DACH. |
| **YunoJuno** | Reino Unido | Todos | ~15% al cliente | Verificación básica | UK contractor market. Especialmente para contratos en GBP con empresas UK. |
| **Gun.io** | US | Fullstack, backend | Sin fee al dev | Vetting técnico + cultural | Principalmente US remote. Rates en USD. |
| **Landing.Jobs** | Portugal, España, DACH | Todos | Variable | Mínimo | Mix entre job board y plataforma. Fuerte en mercado luso-hispano y DACH. |

**Nota sobre comisiones:** algunas plataformas (Toptal, Arc) cobran al cliente directamente y el dev recibe el rate íntegro. Otras (Malt) descuentan 0-10% al dev. Al negociar el rate, sube un 5-10% si sabes que habrá fee de plataforma.

### 1.2 Búsqueda directa — canales donde empresas europeas publican contratos

Estos canales son gratuitos para el dev y llegan a empresas que no usan plataformas:

| Canal | Frecuencia | Tipo de empresa | Cómo funciona |
|---|---|---|---|
| **LinkedIn** (modo Open to Work) | Continuo | Todas | Activa "Open to freelance/contract work" en perfil. Recruiters y hiring managers te contactan. También busca contratos activos con filtro "Contract". |
| **HN Who is Hiring** | Mensual (1er día del mes) | Startups, scaleups | Hilo de Hacker News donde empresas publican posiciones. Busca "contract", "remote", "TypeScript", "Go". Responde directamente al comentario. |
| **WeWorkRemotely** | Continuo | Remote-first startups | Job board. Sección "Contract Gigs". Clientes principalmente US pero pagan a cualquier timezone. |
| **OTTA** | Continuo | Scaleups EU | Mejor curado que LinkedIn. Filtro por "contract". Empresas B2B de tamaño medio. |
| **Cord.co** | Continuo | Startups UK/EU | Dev-centric job board. Empresa ve tu perfil y contacta directamente. Contratos frecuentes. |
| **Remotive.io** | Continuo | Remote global | Newsletter + job board. Contratos remotos de todo el mundo. |
| **Topstartups.io** | Continuo | Startups EU | Centrado en startups europeas Series A-C. Menor volumen pero mejor signal/noise. |

### 1.3 Headhunters especializados en contratos

Estos no te cobran a ti — cobran al cliente una comisión sobre el primer contrato. Para que valgan la pena, tienes que tener un perfil de senior claro.

- **Distant Job:** especializado en remote. Trabajan con empresas que buscan contractors remotos de largo plazo.
- **X-Team:** modelo propio (más cercano a staff augmentation); si entras, te colocan en proyectos de sus clientes.
- **Recruiters generalistas en LinkedIn:** busca recruiters en FR, DE, UK que etiqueten sus posts con "contract", "remote", "backend", "TypeScript". Conecta con ellos aunque no haya posición — te avisan cuando algo encaje.

---

## 2. Nichos por stack — dónde está la demanda real

### 2.1 TypeScript / Next.js / React

**Demanda:** muy alta. Es el stack más buscado en EU para frontend y fullstack.

**Problema:** saturación del lado de oferta. Muchos devs TS/React buscan contratos. La diferencia la hace la especialización:

- **React Server Components / Next.js App Router:** menos candidatos que entienden realmente el modelo de datos. Diferenciador real en 2026.
- **Performance web (Core Web Vitals, SSR, edge rendering):** empresas de ecommerce o medios pagan premium por esto.
- **Testing robusto (Playwright, Vitest, Testing Library):** raro encontrar devs que hagan testing serio en frontend.
- **TypeScript avanzado (generics, type inference, satisfies):** muchos "usan TypeScript" pero pocos lo conocen bien.

**Target de empresa ideal:** scaleups B2B con producto propio (SaaS), fintech, ecommerce mid-size. Evitar agencias (rates más bajos, proyectos cortos).

### 2.2 Go (Golang)

**Demanda:** creciente, especialmente en fintech, infraestructura, herramientas de developer tooling, cloud-native. La oferta de contractors Go cualificados es notablemente menor que la de Go asalariados.

**Por qué los rates son superiores:**
- Menos devs con Go sólido que con TS/React.
- Go está concentrado en áreas de alto valor (backend financiero, servicios críticos, infra).
- Las empresas que usan Go tienden a ser más maduras y tienen presupuesto.

**Nichos de alta remuneración:**
- Fintech backend: APIs de pagos, reconciliación, compliance — demanda constante en UK, FR, DE.
- DevOps tooling: construcción de herramientas internas (CI/CD, infra-as-code) — startup o grandes tech.
- Kubernetes operators y controllers: nicho muy específico, rates al techo.
- gRPC / Protobuf microservices: común en scale-ups con arquitectura distribuida.

### 2.3 TS + Go full-stack

El perfil que mueve las agujas: frontend sólido en TS/React + backend en Go. Permite trabajar end-to-end en equipos pequeños donde el dev cubre toda la pila.

**Ventaja para contractors:** las empresas con equipos pequeños (2-8 devs en el equipo) buscan perfiles que no requieran especialización en capas — un contractor que cubra todo el stack es más valioso que dos especialistas a medio tiempo. Argumenta esto explícitamente en el proceso.

---

## 3. Rates benchmark 2026 — tabla por país y stack

La tabla fusiona datos de isvidal (experiencia directa como contractor español, abril 2026) con benchmarks de mercado (index.dev, remotepass.com, riseworks.io, IT Jobs Watch).

### Nota de lectura

- **Rate negociado (lo que recibes):** lo que llega a tu cuenta bancaria antes de impuestos.
- **Rate de mercado (lo que el cliente espera pagar):** incluye el margen de la plataforma si aplica.
- Los rates de isvidal son rates negociados directamente, sin comisión de plataforma.

### Tabla — Senior/Mid contractor desde España, 2026

| País cliente | Stack | Nivel | Rate horario | Rate diario aprox. | Fuente / notas |
|---|---|---|---|---|---|
| 🇫🇷 Francia | TS/React | Senior | €60–75/h | €480–600/día | Malt FR + isvidal tier medio |
| 🇫🇷 Francia | Go backend | Senior | €65–80/h | €520–640/día | index.dev + isvidal |
| 🇩🇪 Alemania | TS/React | Senior | €75–100/h | €600–800/día | Honeypot + index.dev |
| 🇩🇪 Alemania | Go backend | Senior | €80–110/h | €640–880/día | index.dev (cloud-native premium) |
| 🇬🇧 UK | TS/React | Senior | £70–100/h | £560–800/día | IT Jobs Watch London + YunoJuno |
| 🇬🇧 UK | Go backend | Senior | £80–120/h | £640–960/día | IT Jobs Watch London |
| 🇨🇭 Suiza | TS/React | Senior | CHF 90–130/h | CHF 720–1040/día | riseworks.io + fintech premium |
| 🇨🇭 Suiza | Go / fintech | Senior | CHF 110–150/h | CHF 880–1200/día | fintech + banking sector |
| 🇺🇸 US | TS/React | Senior | $80–120/h | $640–960/día | Arc.dev + WeWorkRemotely |
| 🇺🇸 US | Go backend | Senior | $90–130/h | $720–1040/día | Gun.io + niche premium |
| **Referencia isvidal** | TS | Mid-senior | 400–600€/día | ~€50–75/h | Directo (FR, empresa grande) |
| **Referencia isvidal** | TS | Floor | 300–350€/día | ~€37–44/h | Primer contrato o empresa mediana |

**Nota UK post-Brexit:** UK paga en GBP. Con Wise, la conversión sale a tipo mid-market. £1 ≈ €1.17 (aprox. abril 2026 — verificar al negociar).

**Nota plataforma:** si el cliente llega por Malt (fee hasta 10% al dev), sube el rate negociado un 10% para compensar. Si llegas directo, el rate del cliente y el tuyo son el mismo.

### ¿Qué esperar para el primer contrato?

Primer contrato típico: **€350-450/día** (mid-senior, cliente EU, sin historial como contractor). El salto a €500-700/día llega con el primer contrato bien ejecutado y referencia verificable. No es inmediato — espera 6-18 meses para conseguir el tier medio.

---

## 4. El proceso de selección — qué esperar

isvidal lo describe directo: el proceso de selección de un contractor es **idéntico al de un asalariado**. La diferencia es que la decisión asalariado/contractor llega al final.

### Fases habituales

1. **Screening inicial (recruiter):** 20-30 min. Verificar disponibilidad, timezone, rate esperado, tipo de contrato. En inglés casi siempre. Si el recruiter es interno de la empresa, suele ser más orientado al fit cultural.

2. **Entrevista técnica (tech lead o senior):** 45-90 min. Preguntas de arquitectura, decisiones de diseño, debugging conceptual. Para Go: puede incluir preguntas sobre concurrencia (goroutines, channels, context), gestión de memoria, interfaces. Para TS: TypeScript avanzado, React hooks, SSR vs CSR.

3. **System design (senior roles):** 60 min. Diseñar un sistema a alto nivel — API, base de datos, escalabilidad. Pregunta específica al dominio de la empresa (p.ej. sistema de pagos, pipeline de datos). Para senior+, es casi universal en empresas >50 personas.

4. **Coding assessment:** puede ser sincrónica (pair programming) o take-home (máx 3-4h). Para contractors, el take-home es común para reducir el calendario — las empresas no esperan que el candidato tenga tiempo ilimitado.

5. **Culture fit / entrevista con manager:** 30-45 min. Trabajo remoto, autonomía, comunicación asíncrona. Para un contractor, es especialmente importante porque trabajarás con mínima supervisión.

6. **Oferta:** rate diario u horario, duración del contrato (típicamente 6 meses iniciales), días de vacaciones (si los hay), notice period (aviso de rescisión — estándar: 2-4 semanas).

### Cuándo mencionar que eres contractor (no asalariado)

En el primer contacto con el recruiter. Evita llegar al final del proceso y descubrir que la empresa quería asalariado. Pregunta directamente: *"Is this role open to contractors working through a service agreement, or strictly FTE?"*

Si la empresa dice "solo asalariado": puede ser negociable dependiendo de su política. Revolut, por ejemplo, históricamente ofrece las dos opciones. Empresas más pequeñas con setup de facturación EU sencillo también suelen poder adaptarse.

### Qué negociar en la oferta (además del rate)

- **Duración inicial:** preferir 6 meses con opción a renovar en lugar de 3 meses. Más seguridad, menos fricción de búsqueda.
- **Notice period:** 2-4 semanas en ambas direcciones. Esencial — sin cláusula de preaviso, el cliente puede cancelar de un día para otro.
- **Vacaciones:** algunos contratos incluyen días pagados (común en FR, menos en UK/US). Negocia explícitamente si es importante para ti.
- **Aumento en renovación:** no es automático. Mentionarlo en la oferta o en la revisión a los 3 meses.
- **Horario y disponibilidad:** documenta en el contrato el overlap horario esperado. Evita sorpresas si el equipo es en UTC-5 y tú en UTC+2.

---

## 5. Estrategia de pipeline — cómo no buscar de golpe

El error más común: buscar contrato solo cuando el actual termina. Para el mes siguiente estás seco.

### Pipeline activo mínimo

- **Perfil siempre actualizado:** Malt, LinkedIn. Aunque tengas contrato, mantén el perfil visible.
- **Contacto con recruiters de forma proactiva:** 1-2 por semana, especialmente si el contrato actual lleva 3+ meses. No esperes a que salga el post.
- **Red de referencias:** el mejor canal para contratos buenos. El cliente satisfecho que te recomienda a otro. Cultívalo activamente — un mensaje de seguimiento cada 2-3 meses a contactos anteriores.
- **Empezar a buscar 6-8 semanas antes de que termine el contrato actual.** Proceso completo tarda 3-6 semanas desde el primer contacto hasta la firma.

### Cuándo aceptar rate bajo

- Primer contrato (sin historial como contractor): puede merecer la pena a €300-350/día para conseguir la primera referencia.
- Empresa muy conocida o con proyecto muy concreto en CV: puede justificarse temporalmente.
- No aceptar más de un contrato por debajo de tu target rate — establece el suelo rápido.

---

*Fuentes consultadas (abril 2026): isvidal posts MediaVida; index.dev European Developer Rates 2026; remotepass.com Global Contractor Rates 2025; riseworks.io Average Contractor Rates 2026; IT Jobs Watch UK (Go contracts); Malt platform overview; Arc.dev vs Toptal comparison.*
