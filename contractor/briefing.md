# Briefing ejecutivo — Contractor desde España (stack TS/Next/React/Go)

> **Disclaimer:** este documento es investigación, no asesoría fiscal ni legal. Los datos fiscales reflejan la normativa vigente en abril de 2026 pero son orientativos. Antes de ejecutar cualquier paso real, consulta con gestor/asesor fiscal colegiado.

---

## 1. Glosario — los 4 términos que importan

| Figura | Qué es | Por qué importa distinguirla |
|---|---|---|
| **Empleado** | Contrato laboral indefinido o temporal. RETA general del asalariado. | Referencia de comparación: tu salario neto si no te mueves. |
| **Freelance autónomo** | Múltiples clientes, proyectos cortos, precios por proyecto u horas. Classic autónomo español. | Lo que la gente imagina cuando oye "autónomo", pero no es lo que buscamos aquí. |
| **TRADE** *(Trabajador Autónomo Económicamente Dependiente)* | Figura legal española: cobras >75% de un solo cliente, pero con protecciones contractuales mínimas. Solo aplicable con **cliente español**. Registro en SEPE obligatorio. | No es lo que queremos. Requiere cliente español (falso autónomo risk intacto) y burocracia sin ventaja fiscal adicional. |
| **Contractor** | **Concepto funcional, no figura legal española.** Un cliente, contrato 6-12 meses renovable, jornada L-V simulando empleo. Se opera como autónomo ordinario (epígrafe 763). La diferencia es dónde está el cliente: fuera de España. | Lo que vamos a estudiar en este roadmap. isvidal lo llama "casi inexistente en España" porque casi nadie lo hace, no porque sea ilegal. |

**Conclusión del glosario:** cuando alguien dice que trabaja como "contractor desde España", es un autónomo dado de alta en el RETA que factura a una empresa extranjera bajo un acuerdo de 6-12 meses, full-time. Fiscalmente es un autónomo estándar. La diferencia está en quién paga y cómo se estructura el acuerdo.

---

## 2. Por qué solo funciona facturando fuera

### El problema: falso autónomo

La ley española (Art. 1.2 Estatuto de los Trabajadores) presume que una relación laboral existe cuando concurren:
- **Dependencia:** recibes órdenes, tienes horario, no decides cómo organizas tu trabajo.
- **Ajenidad:** no asumes riesgos económicos, los frutos del trabajo van íntegramente al cliente.

Si estas dos condiciones se dan durante meses, la ITSS puede reclasificarte como empleado encubierto aunque tengas un contrato mercantil y estés en el RETA. Consecuencias: cotizaciones no pagadas + multas al cliente (751€-10.000€ por trabajador). Ambas partes pierden.

Con un cliente español esto es perseguible y ha ocurrido (ver jurisprudencia Glovo/Deliveroo). La ITSS española tiene plena jurisdicción.

### Por qué el cliente extranjero reduce el riesgo

Los mismos criterios legales aplican técnicamente con un cliente extranjero. Lo que cambia es la **fricción práctica**:
- La ITSS tiene jurisdicción española, no francesa, alemana o inglesa.
- Ejecutar una inspección cruzada contra una empresa sin presencia en España es operativamente costoso y sin precedente claro.
- isvidal lo formula directo: *"solo puedes tener esta figura de contractor cuando las facturas son a empresas de fuera de España."*

**Matiz importante:** esto no es inmunidad jurídica. Es reducción práctica del riesgo por fricción jurisdiccional. El riesgo residual existe y aumenta si:
- Eres el único proveedor del cliente en España y hay evidencia de dependencia (email corporativo, acceso VPN, single-payer 100%).
- La empresa extranjera tiene filial española → la ITSS sí tiene jurisdicción.

**Recomendación:** mantener indicios de independencia real (múltiples contratos aunque sea un secundario, herramientas propias, facturación a 2+ clientes aunque uno sea pequeño, contrato mercantil limpio sin cláusulas laborales).

---

## 3. ¿Eres candidato? Árbol de decisión

```
¿Tienes 4+ años de experiencia con stack vendible fuera (TS/React/Go)?
    │
    ├── No → Construye experiencia primero. El mercado contractor no es para juniors.
    │
    └── Sí ↓

¿Puedes hacer una entrevista técnica entera en inglés (B2-C1)?
    │
    ├── No → Prioridad 0. Sin inglés fluido no accedes a empresas FR/DE/UK.
    │         Invierte 3-6 meses en esto antes de cualquier otra cosa.
    │
    └── Sí ↓

¿Tienes fondo de emergencia para 3-6 meses de gastos + cuota RETA?
    │
    ├── No → Construye el fondo antes. Sin él, el primer downtime entre contratos
    │         es una crisis financiera real.
    │
    └── Sí ↓

¿Estás dispuesto a llevar admin básica o pagar ~80€/mes de gestoría?
    │
    ├── No → El modelo no funciona sin administración. La gestoría lo hace por ti
    │         si no quieres, pero alguien tiene que hacerlo.
    │
    └── Sí ↓

¿Prefieres tener un cliente serio full-time (modelo empleado-simulado)
en vez de varios proyectos cortos simultáneos?
    │
    ├── No → Estudia "independent consultant" (distinto modelo, distinta estrategia).
    │
    └── Sí → Candidato sólido para contractor. Continúa.
```

**Perfil ideal:** mid-senior (5-8 años), inglés fluido, stack TS o Go (mejor ambos), tolerancia a downtime de 1-3 meses, apetito de papeleo bajo-moderado.

---

## 4. Los 5 pasos mínimos para arrancar

> Estos son los pasos de setup, no de encontrar un cliente. El orden importa: tienes que estar dado de alta antes de poder facturar.

### Paso 1 — Alta censal en Hacienda (Modelo 036)

Tienes que declarar a Hacienda el inicio de actividad.

- **Modelo 036** (más completo que el 037; necesario para el ROI).
- **Epígrafe IAE:** 763.1 — Programadores y Analistas de Informática. Es el epígrafe de la sección profesional para devs. Si facturas a empresas extranjeras, tus facturas **no llevan retención de IRPF** (solo aplica a clientes españoles).
- **CNAE:** 6201 — Programación informática.
- **Solicitar el ROI** en el mismo 036, casilla 582, fecha desde: el día del alta. El ROI (Registro de Operadores Intracomunitarios) es el número que te identifica en la UE y te permite facturar a empresas europeas sin IVA (reverse charge). La AEAT tarda hasta 3 meses en aprobarlo. Sin ROI no puedes emitir facturas intracomunitarias sin IVA. **Solicítalo el día uno.**

### Paso 2 — Alta en el RETA (Seguridad Social)

Simultánea al alta censal (dentro de los 30 días naturales del inicio de actividad).

- Tramitar en tu Dirección Provincial de la Seguridad Social o vía Importass.
- **Tarifa plana:** 80€/mes los primeros 12 meses si es tu primera vez en el RETA (o no has estado dado de alta en los 2 años anteriores). En el mes 13 pasas al tramo que corresponda por tus rendimientos netos previstos. Planifica el salto.
- **Tramos 2026:** el sistema funciona por 15 tramos de rendimiento neto mensual. Con €2.500 netos/mes tu cuota mínima es ~€423/mes. Con €4.000 netos/mes sube a ~€530/mes. La cuota se puede ajustar hasta 6 veces al año.

### Paso 3 — Cuenta bancaria business

No es obligatoria legalmente, pero separar finanzas personales y profesionales es necesario para la contabilidad.

- **Wise Business:** recomendado como principal si cobras en GBP o USD. Tipo de cambio sin margen, tarjeta física, IBANs en varias divisas. Acepta transferencias SWIFT de empresas UK/US sin el coste habitual de la banca tradicional.
- **Cuenta business española (Openbank, Revolut Business, BBVA Pymes):** como secundaria para domiciliar cuota RETA y pagos locales.

### Paso 4 — Gestoría

Sin gestoría puedes llevar la contabilidad tú mismo, pero el tiempo no merece la pena:

- **Lo que gestiona:** Modelo 303 (IVA trimestral), 349 (operaciones intracomunitarias), 130 (pago fraccionado IRPF trimestral), Renta anual.
- **Coste:** 60-100€/mes para un autónomo sin empleados con facturación internacional. Algunos ofrecen onboarding gratuito.
- **Qué buscar:** que tengan experiencia con autónomos que facturan fuera de España (intracomunitario + no-UE). Pregunta específicamente si llevan Modelo 349.
- **Red flags:** "no sé qué es el ROI", "vas a necesitar gestión trimestral de IVA intracomunitario y no lo hacemos".

### Paso 5 — Perfil en plataformas y pipeline

Una vez dado de alta:

- **Malt (malt.es):** plataforma más activa en España y Francia para contractors senior. Fee del 0-10% al dev. Proceso: creas perfil, fijas rate diario/hora, clientes te contactan. Perfil verificado: ventaja.
- **LinkedIn:** modo "Open to Work" → "Contractor/Freelance". Muchas empresas europeas buscan contractors directamente. Optimizar titular (ej. "Senior TypeScript / Go Engineer — open to 6-12 month contracts").
- **Canales directos:** HN Who is Hiring (mensual), WeWorkRemotely, Landing.Jobs (DACH/Portugal), OTTA, Cord.co (UK).
- **Headhunters especializados:** Distant Job, X-Team — cobran al cliente, no al dev.

---

## 5. Rates esperables 2026 — TS/Next/React/Go para UE

> Los rates de isvidal son datos de primera mano de un contractor español activo (2026). Los datos de mercado son benchmarks europeos de plataformas y estudios de contratación. La realidad está entre ambas fuentes.

### Datos de primera mano (isvidal, MediaVida, abril 2026)

| Tier | Rate diario | Rate horario | Contexto |
|---|---|---|---|
| **Floor** (entrada contractor) | 300-350 €/día | ~37-44 €/h | Acceso al primer contrato, empresa mediana, stack TS |
| **Medio** (sólido senior) | 400-600 €/día | ~50-75 €/h | Senior con historial, empresa grande (100M+ revenue) |
| **Alto** | ~560 €/día | ~70 €/h | Difícil de alcanzar como "picateclas raso" |

### Benchmark europeo (fuentes: index.dev, IT Jobs Watch, reactjsdeveloperjobs.com — 2025-2026)

| Stack | Nivel | Rate horario W. Europe | Rate diario aprox. |
|---|---|---|---|
| **TS/Next/React** | Mid | €50-80/h | €400-640/día |
| **TS/Next/React** | Senior | €80-100/h | €640-800/día |
| **Go** | Mid | €50-80/h | €400-640/día |
| **Go** | Senior | €70-110/h | €560-880/día |
| **TS+Go full-stack** | Senior | €80-110/h | €640-880/día |

**Notas:**
- UK-based roles pagan en GBP. Londres: £600-800/día para senior TS/React.
- Go tiene menos oferta de contractors → menos competencia → rates tendencialmente superiores a TS-only en el mismo nivel.
- Plataformas (Malt) descuentan 0-10% del rate acordado.
- Primer contrato suele estar en el tier floor-medio. El salto al tier alto llega con historial y referencias.

### ¿Qué se lleva a casa?

Ejemplo orientativo: contractor a €500/día, 220 días facturables al año:
- Facturación bruta: **€110.000**
- Gastos deducibles (gestoría, equipo, internet, coworking): ~€7.000
- Cuota RETA (~€480/mes promedio): ~€5.760/año
- Rendimiento neto IRPF: ~€97.240
- IRPF estimado (tramos 2026, progresivo): ~€35.000-38.000
- **Neto en mano: ~€59.000-62.000** al año

> El IRPF varía significativamente por comunidad autónoma. Madrid es la más baja; Cataluña y Euskadi las más altas. La estimación anterior asume Madrid. Pide a tu gestoría el cálculo exacto para tu situación.

---

## 6. Top 3 riesgos y cómo mitigarlos

### Riesgo 1 — Reclasificación como falso autónomo

**El riesgo:** si tu cliente extranjero es tu único pagador, trabajas bajo su dirección y control y el contrato dura 6-12 meses, cumples los criterios de laboralidad aunque el cliente sea francés o alemán. La ITSS tiene jurisdicción teórica. En la práctica, no hay casos documentados contra contractor-single con empresa extranjera sin presencia en España, pero el riesgo existe.

**Mitigación:**
1. Contrato mercantil limpio: sin cláusulas que impongan horario, lugar de trabajo o herramientas. El contrato define el output, no la forma de trabajar.
2. Diversificación: aunque sea un proyecto secundario pequeño (web al panadero amigo de isvidal) que rompa el 100% de dependencia de un pagador.
3. Herramientas propias: tu propio laptop, tu propia cuenta GitHub, tu propio dominio.
4. Sin señales de empleado: no pidas tarjeta corporativa, no pidas email @empresa.com.

### Riesgo 2 — Cashflow entre contratos (downtime)

**El riesgo:** entre contratos pasan 4-8 semanas de media. La cuota RETA sigue corriendo. Sin ingresos esos meses, necesitas un fondo que lo absorba.

**Mitigación:**
1. Fondo de emergencia de 3-6 meses de gastos personales + cuota RETA antes de arrancar.
2. Empezar a buscar el siguiente contrato cuando queden 4-6 semanas del actual, no cuando termine.
3. Tener perfil activo en plataformas todo el tiempo, no solo cuando estás buscando.
4. Nota: el "cese de actividad" como autónomo solo aplica en condiciones muy restrictivas y no es equiparable al paro de un asalariado.

### Riesgo 3 — Fiscal sin gestoría

**El riesgo:** trimestral tienes que presentar 303 (IVA), 349 (intracomunitario), 130 (IRPF fraccionado). Anual: renta. Si fallas un plazo o te equivocas en el cálculo, Hacienda recarga intereses y recargos.

**Mitigación:**
1. Contrata gestoría desde el día uno. 80€/mes vs el coste de un error fiscal: no hay debate.
2. Reserva el 30-35% de cada factura cobrada para IRPF e IVA. Ese dinero no es tuyo; es de Hacienda.
3. Abre una cuenta separada donde metas ese porcentaje cada vez que te llega un pago.

---

## 7. TL;DR — Una página

### La idea central

Trabajar como contractor desde España significa ser autónomo español que factura a una empresa extranjera bajo un acuerdo de 6-12 meses full-time. No existe como figura legal propia en España: eres autónomo ordinario (epígrafe 763), con todas las obligaciones fiscales que eso implica. La ventaja es que con clientes fuera de España el riesgo de falso autónomo se reduce a prácticamente cero en la práctica, aunque no desaparece en papel.

### ¿Para quién funciona?

Para un dev mid-senior (5+ años), inglés B2-C1 o superior, con stack TS y/o Go, que prefiera la estabilidad de un acuerdo de larga duración sobre la volatilidad de proyectos cortos.

### ¿Qué ganas?

Rates un 60-120% superiores al salario asalariado equivalente, deducción de gastos reales (equipo, gestoría, internet), side projects legales. Un dev senior con Go o TS full-stack puede esperar €50.000-65.000 netos si factura €100.000-110.000/año desde año dos.

### ¿Qué cuesta?

- Gestoría: ~€960/año (80€/mes).
- RETA: de €80/mes (tarifa plana primer año) a €423-530/mes desde el segundo año.
- Downtime: 4-8 semanas/año sin ingresos entre contratos (variable).
- Admin: dedicación de 2-4h/mes para registros, envío de facturas, revisión con gestoría.

### Los 5 pasos de arranque

1. Modelo 036 en AEAT → IAE 763.1 + solicitar ROI (casilla 582). Plazo ROI: hasta 3 meses.
2. Alta RETA → tarifa plana 80€/mes primer año.
3. Cuenta Wise Business para cobros en EUR/GBP/USD.
4. Contrata gestoría (~80€/mes) antes de emitir la primera factura.
5. Perfil activo en Malt + LinkedIn en modo "open to contractor engagements".

### Lo que tienes que verificar antes de decidir

- ¿Tienes el fondo de emergencia? (3-6 meses gastos + RETA)
- ¿Puedes hacer una entrevista técnica completa en inglés?
- ¿Cuál es tu deadline de decisión? (si es < 3 meses, el ROI puede no estar aprobado cuando lo necesites)

### Próxima lectura

Si el briefing te convence de seguir: lee `legal.md` (Fase 2) para entender en profundidad el marco fiscal completo antes de tocar ningún modelo de Hacienda.

---

*Fuentes consultadas (abril 2026): Infoautónomos, AEAT sede electrónica, Seguridad Social RETA, wolterskluwer.com, index.dev European Developer Rates 2026, reactjsdeveloperjobs.com, IT Jobs Watch UK Go contracts, posts #2659 #2662 #2671 de isvidal en MediaVida.*
