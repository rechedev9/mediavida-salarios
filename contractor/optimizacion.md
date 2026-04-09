# W5 — Optimización y alternativas

> **Disclaimer:** documento de investigación, no asesoría fiscal ni legal. Las cifras fiscales son orientativas y varían por comunidad autónoma, situación personal y año fiscal. Toda decisión de cambio de figura jurídica o de residencia fiscal requiere asesoría especializada. La mudanza de residencia fiscal tiene implicaciones graves si no se hace correctamente — no improvisar.

---

## 1. Autónomo vs. SL — el break-even 2026

La pregunta recurrente: ¿cuándo conviene crear una Sociedad Limitada?

### La diferencia clave de tributación

**Autónomo:** IRPF progresivo sobre el rendimiento neto. Hasta 45-54% (según CC.AA.) en tramos altos. Sin estructura corporativa.

**SL:** Impuesto de Sociedades al **25%** (23% para empresas con facturación < 1 millón EUR/año en el ejercicio anterior). El socio-administrador paga IRPF solo sobre la nómina que se asigna. Los beneficios que se dejan en la empresa tributan al 25% IS. Cuando se distribuyen como dividendos, tributan adicionalmente en el IRPF del socio (19-28% en base del ahorro).

**Doble tributación de dividendos:** IS 25% + IRPF sobre dividendos ~19-28% = tipo efectivo combinado de ~38-47% sobre los beneficios distribuidos. Por eso la SL solo es ventajosa si **no distribuyes todo el beneficio** — lo que acumulas en la empresa tributa solo al 25%.

### Break-even orientativo

| Beneficio neto anual | Recomendación |
|---|---|
| < €40.000 | Autónomo. Menor coste fijo, tarifa plana disponible, sin constitución. |
| €40.000 – €50.000 | Zona gris. Analizar con gestor caso a caso. |
| €50.000 – €70.000 | SL empieza a compensar si no distribuyes todo. |
| > €70.000 | SL claramente ventajosa fiscalmente (ahorro > €4.000/año en la mayoría de casos). |

*Fuente: beel.es, devfreelance.es, boletinclaro.es — datos 2026.*

### El coste oculto de la SL

El saving fiscal tiene un coste que mucha gente ignora:

- **Constitución:** ~1.000-3.000€ (notario, Registro Mercantil, gestor).
- **Capital social mínimo:** 3.000€ (puede ser en especie — un ordenador, por ejemplo).
- **Autónomo societario:** si tienes > 33% del capital y funciones de dirección, cotizas al RETA como societario. La cuota mínima del autónomo societario en 2026 es de ~€310/mes sobre base mínima de €1.000, sin posibilidad de tarifa plana. Esto son ~€840/año más que el autónomo ordinario en tarifa plana.
- **Gestoría más cara:** la contabilidad de una SL requiere depósito de cuentas anuales, auditoría si superas ciertos umbrales, y mayor complejidad contable. Espera ~€100-150/mes vs ~€80/mes de autónomo.
- **Rigidez de extracción:** el dinero de la SL no es tuyo. Para acceder a él debes pagarte una nómina (IRPF + SS) o distribuir dividendos (IRPF base ahorro). No puedes pagar gastos personales con la cuenta de la empresa.

### Conclusión para contractors

**Para el primer año de contractor:** autónomo ordinario sin duda. La tarifa plana y la simplicidad operativa hacen que la SL no tenga sentido hasta tener historial estable.

**A partir del año 2-3, si la facturación es estable > €80.000:** analizar el paso a SL con un gestor especializado. El ahorro puede ser real si se planifica bien la retribución del socio-administrador.

---

## 2. Deducciones avanzadas — los límites que la gente no conoce

Estos gastos parecen deducibles pero tienen restricciones importantes:

### Vehículo

Deducción de un vehículo como autónomo: prácticamente imposible en estimación directa simplificada para un developer que trabaja desde casa o en oficinas de clientes.

- Para deducir el 100%, el vehículo debe ser de **uso exclusivo profesional** — sin uso personal. Hacienda presupone uso mixto para vehículos de personas físicas.
- En la práctica, los vehículos de developers no tienen deducción real. Los inspectores lo saben y es uno de los puntos de inspección más frecuentes.
- Excepción: si usas el vehículo para desplazamientos a cliente verificables (kilometraje documentado, facturas de parking, etc.) — deducción parcial posible pero documentación exhaustiva necesaria.

### Vivienda habitual

La deducción de suministros de vivienda como oficina requiere:
1. **Declaración previa en el Modelo 036** del porcentaje de metros cuadrados afectos a la actividad (ej.: habitación de 20m² sobre 100m² total = 20%).
2. Si no has hecho esa declaración al darte de alta, puedes modificar el 036 — pero Hacienda puede cuestionar el período anterior.
3. La deducción máxima de suministros es 30% × porcentaje de uso. En el ejemplo: 30% × 20% = **6%** de las facturas de luz, agua, gas, internet.
4. El alquiler de la vivienda **no es deducible** salvo contrato mixto expreso.

El ahorro real es pequeño. Para un developer en una habitación del 20% de su piso: ~€50-100/año de deducción sobre luz y gas. El internet profesional (si tienes línea separada exclusiva) es más rentable de deducir al 100%.

### Plan de pensiones

Límite anual de aportación deducible en IRPF: **€1.500** para plan de pensiones individual + €4.250 para planes de empleo simplificados de autónomos (PPSPA). Total posible: €5.750/año.

La reforma 2023 redujo drásticamente el límite del plan de pensiones individual (antes 8.000€). Los planes de empleo de autónomos son la vía principal ahora, pero requieren contratarlos específicamente.

El ahorro fiscal es real (deduce al tipo marginal — si estás al 45%, cada €5.750 aportados te ahorran ~€2.580 de IRPF), pero el dinero queda inmovilizado hasta jubilación o situaciones excepcionales.

### Seguro médico

Hasta **€500/año por persona** de la unidad familiar son deducibles como gasto en actividades económicas. Es una deducción pequeña pero limpia: si tienes seguro médico privado (frecuente cuando dejas de depender de la empresa), incluirlo.

---

## 3. Beckham Law — no aplica

Por completitud: el régimen especial de impatriados (Ley Beckham, Art. 93 LIRPF) permite tributar al tipo fijo del **24%** durante 6 años. Solo aplica a personas que **trasladan su residencia a España** por motivos laborales — los impatriados.

Un residente en España que ya es autónomo no puede acogerse. No es relevante para el perfil de este roadmap.

---

## 4. Relocalización — con disclaimer fuerte

> ⚠️ **Advertencia de alcance:** esta sección es una panorámica para que el usuario pueda decidir si investigar más. No es suficiente para tomar ninguna decisión real. La mudanza de residencia fiscal mal ejecutada puede resultar en doble imposición, exit tax (España cobra impuesto sobre plusvalías latentes al salir), o sanciones si Hacienda considera que la mudanza es ficticia. Asesoría fiscal especializada en fiscalidad internacional es imprescindible antes de cualquier movimiento.

España considera residente fiscal a quien permanece **más de 183 días** en territorio español o tiene en España el centro principal de intereses económicos. Si te mudas a Andorra pero tu empresa, clientes y cuentas siguen en España, Hacienda puede ignorar la mudanza.

### Exit tax

Si te vas con participaciones en empresas o activos financieros significativos (> €4M en activos o > €1M de plusvalía latente), España cobra el Impuesto de Salida sobre las plusvalías no realizadas. Relevante solo para founders o inversores — no para el contractor estándar.

---

### 4.1 Portugal — IFICI (NHR 2.0)

El NHR original terminó en enero de 2024. Lo reemplaza el **IFICI (Incentivo Fiscal à Investigação Científica e Inovação)**.

**Qué es:** tipo fijo del 20% sobre renta de fuente portuguesa para residentes fiscales elegibles, durante 10 años.

**Buenas noticias para tech:** los especialistas TIC y en áreas técnicas están explícitamente incluidos en las profesiones elegibles.

**La trampa para contractors con cliente extranjero:** el IFICI está diseñado para atraer talento a empresas con sustancia en Portugal. Si eres autónomo facturando directamente a clientes extranjeros sin empresa portuguesa, el acceso es complicado. La vía para autónomos digitales es crear una empresa en Portugal y ser administrador, pero esto añade complejidad y coste.

**Requisitos de elegibilidad:**
- Titulación mínima EQF nivel 6 (licenciatura) + 3 años de experiencia, o doctorado (EQF 8).
- No haber sido residente fiscal en Portugal en los 5 años anteriores.
- Solicitud antes del 15 de enero del año siguiente al año de llegada.
- Sustancia real en Portugal (no pueden ser residentes ficticios).

**Calidad de vida / coste:** Lisboa y Oporto tienen creciente comunidad tech pero coste de vida que ha subido significativamente (2022-2026). Alquiler en Lisboa: €1.200-2.000/mes para piso decente. Seguros, gestoría, seguridad social portuguesa (base mínima: ~€530/mes para autónomos).

**Resumen:** opción interesante si ya tienes vínculo con Portugal o si la calidad de vida encaja. El IFICI para contractors puros (sin empresa portuguesa) tiene fricciones. Investigación adicional requerida con asesor especializado.

---

### 4.2 Andorra

El más popular entre developers y content creators españoles que buscan reducción fiscal.

**Sistema IRPF:**
- 0% hasta €24.000/año.
- 5% entre €24.001 y €40.000.
- **10% máximo** por encima de €40.000.

Sin impuesto sobre el patrimonio, sucesiones ni dividendos (dentro de Andorra). IS: 10%. IVA local (IGI): 4,5%.

**Vía para contractor:**
1. **Residencia activa:** crear empresa andorrana (SL equivalente), tener ≥34% del capital, ser administrador. Fianza de €50.000 en la AFA (recuperable al salir). Vivir >183 días/año en Andorra.
2. **Emprendedor/nómada digital:** acceso via programa del Ministerio de Economía. Mínimo 90 días/año. Más fácil de obtener si tienes proyecto digital verificable.
3. Contribución potencial no reembolsable de €30.000 para residencia por cuenta propia (en debate para 2026 — verificar estado actual).

**El coste real:**
- Fianza €50.000 inmovilizada (sin coste, es garantía).
- Gestión empresa andorrana: €100-200/mes de gestor local.
- Seguro médico privado obligatorio (~€100-200/mes).
- Seguridad social andorrana (CASS): variable, mínimo ~€200/mes.
- Vivienda: €800-1.500/mes (Andorra la Vella). Subiendo por demanda.
- 183 días físicos al año en Andorra: implica renunciar a estar en España la mayor parte del tiempo.

**Lo que la gente ignora:** vivir en Andorra realmente (183 días) es una restricción real. Sin supermercados de gran escala, sin playa, sin cultura urbana comparable a Madrid o Barcelona. La vida tech en Andorra es muy limitada. La mayoría de developers que se mudan trabajan 100% remoto y viajan mucho.

**Ahorro real a €80.000/año de beneficio neto:**
- En España (Madrid): IRPF ~€27.000 → neto €53.000
- En Andorra: IRPF ~€4.800 (10% sobre 48k) → neto ~€75.000
- Diferencia: ~€22.000/año

**Para contractors con ingresos > €80.000/año y que puedan vivir físicamente en Andorra:** la mudanza puede justificarse económicamente en 2-3 años.

---

### 4.3 Chipre — régimen Non-Dom

Chipre ofrece el régimen **Non-Domiciled** para residentes no domiciliados de origen. Ventajas: exención en dividendos e intereses (impuesto GESY/ASD). IRPF en Chipre: progresivo hasta 35%, pero con exenciones que reducen la carga real.

Para contractors: la vía más usada es crear una empresa cipriota (IS: 12,5%) y pagarse salario moderado. La burocracia es en inglés (common law), bancos aceptables para operaciones internacionales.

**Problemas:** la banca cipriota tuvo una crisis grave (2012-2013) que dejó cicatrices de imagen. Algunos clientes/plataformas prefieren no pagar a entidades cipriotas. La reputación de Chipre como jurisdicción ha mejorado desde la entrada en la UE, pero sigue siendo una señal de alerta para algunos compliance officers de grandes empresas.

**Requisitos de residencia:** 60 días anuales en Chipre (si no tienes residencia en ningún otro país) + no pasar >183 días en ningún otro país. Más flexible que Andorra.

**Calidad de vida:** buen clima, comunidad tech pequeña pero creciente (Limassol), coste de vida moderado vs. Europa occidental.

*Nota: esta sección se basa en información disponible hasta agosto 2025. Verificar el estado del régimen Non-Dom en Chipre con fuente actualizada antes de actuar.*

---

### 4.4 Irlanda

El sistema contractor en Irlanda es más complejo que en otros países:

- La estructura típica es a través de un **Personal Service Company (PSC)** o **umbrella company**.
- Impuesto de Sociedades: 12,5% (el más bajo de la UE para actividades trading). Pero las restricciones del IR35 irlandés y las normas anti-avoidance hacen que el ahorro real sea menor de lo que parece.
- IRPF irlandés: progresivo hasta 40% + USC (Universal Social Charge) hasta 8% + PRSI (seguridad social). Tipo efectivo alto.
- Irlanda es más eficiente para **asalariados en tech** que para contractors autónomos.

**Para un contractor:** salvo que la empresa cliente sea irlandesa y pague bien (muchas big tech tienen HQ en Dublín), el setup operativo en Irlanda es más costoso que Andorra o Portugal.

---

### 4.5 Dubai / UAE

Fiscalidad: 0% IRPF. Sin impuesto sobre beneficios personales (el IS corporativo de 9% desde 2023 aplica solo a empresas con beneficios > AED 375.000).

**Realidad para developers:**
- El coste de vida en Dubai es alto (alquiler €2.000-4.000/mes para piso decente).
- Visado y residencia: free zones, freelance permit (~€1.500-3.000/año).
- Banking: complejo para transacciones internacionales. Algunos clientes europeos tienen fricciones para pagar a entidades UAE.
- Distancia con Europa: GMT+4, lo que significa solapamiento horario limitado con clientes FR/DE (8h-14h UTC+4 = 6h-12h Paris).
- Calidad de vida: polariza. Para algunos es perfecta; para otros, la cultura y el estilo de vida no compensan.

**Para contractors con clientes exclusivamente US** (más UTC-4 tolerantes) y altísimos ingresos (>€150.000/año): el ahorro puede justificar el coste y la complejidad. Para contractors EU-focused con €80.000-120.000: los números no salen tan claros.

---

## 5. Plan de carrera contractor — cómo subir el rate año a año

El rate no sube por acumular años. Sube por reducir el riesgo percibido del cliente y por señalar más valor.

### Año 1 — Establecer la base

Objetivo: conseguir el primer contrato (floor rate €300-400/día). Priorizar: referencia verificable, relación larga (6+ meses), cliente reconocible en el mercado.

**Qué construir:**
- Perfil en Malt/LinkedIn con descripción clara del stack y lo que resuelves.
- Al menos un proyecto público o case study que demuestre trabajo real (no "hice X" — "ayudé a Y a lograr Z").
- Documentar el engagement: tecnologías, escala, impacto. Al terminar, pedir testimonio al manager.

### Año 2-3 — Subir de tier

Objetivo: pasar de €350-400/día a €500-600/día. El salto requiere: historial + especialización visible.

**Acciones concretas:**
- **Especialización estrecha:** en lugar de "Senior React developer", ser "Senior React developer especializado en performance y React Server Components para ecommerce B2B". La especificidad reduce competencia.
- **Caso de estudio público:** si el cliente lo permite, un blog post o case study técnico sobre el trabajo. Los clientes nuevos lo ven.
- **Renovación de rate:** cada renovación de contrato es una oportunidad de revisión. Proponer un 5-10% de subida al renovar, con justificación concreta (valor entregado en los meses anteriores, cambios en el mercado).
- **Cambio de tier en plataformas:** si empezaste en Malt con rate bajo, actualizar el perfil con la experiencia acumulada y subir el rate. Los nuevos clientes ven el rate actual, no el histórico.

### Año 3+ — Construir diferenciación duradera

Objetivo: superar €600-700/día. Solo es sostenible con diferenciación real.

**Palancas:**
- **Referrals directos:** el canal más eficiente. Un cliente satisfecho que te presenta a otro elimina todo el proceso de selección.
- **Nicho de alto valor:** Go en fintech, TypeScript en performance, full-stack para founders de scaleups — los nichos donde el valor entregado se mide en dinero son los que pagan más.
- **Visibilidad técnica:** contribuciones open source relevantes, charlas en meetups/conferencias del stack, posts técnicos que demuestran expertise. No obligatorio, pero acelera el pipeline.
- **Proceso de selección inverso:** llegar al punto donde rechazas contratos fuera de tu rate objetivo porque tienes suficiente inbound. Este estado no llega solo — requiere construcción activa del pipeline durante los años previos.

---

*Fuentes consultadas (abril 2026): beel.es (autónomo vs SL 2026); devfreelance.es; immigrantinvest.com (IFICI 2026); portugalresidencyadvisors.com; augelegalfiscal.com (Andorra 2026); andorraxperience.com; taxandorra.com; kpmg.com (IFICI overview); Ley 35/2006 IRPF (deducciones plan de pensiones Art. 52).*
