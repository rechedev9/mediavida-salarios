# W4 — Mecánica contractual del contractor

> **Disclaimer:** documento de investigación, no asesoría legal. El análisis de cláusulas es orientativo; todo contrato real debe ser revisado por un abogado antes de firmar, especialmente los de derecho extranjero. Este documento ayuda a saber qué preguntar, no a sustituir la revisión legal.

---

## 1. MSA + SOW — la estructura estándar

La mayoría de las empresas europeas y norteamericanas que contratan contractors usan una estructura de dos documentos:

### MSA (Master Service Agreement)

El marco general de la relación. Se negocia **una vez** y rige todos los proyectos futuros. Cubre:
- Propiedad intelectual
- Confidencialidad
- Limitación de responsabilidad
- Non-compete y non-solicitation
- Terminación del acuerdo
- Ley aplicable y jurisdicción
- Resolución de conflictos

Duración habitual: indefinida o 2-3 años, renovable automáticamente.

### SOW (Statement of Work)

El acuerdo específico de cada contrato. Se firma por cada engagement. Cubre:
- Descripción del trabajo (scope)
- Deliverables y criterios de aceptación
- Duración (start date / end date)
- Rate (diario u horario)
- Condiciones de pago (payment terms)
- Aviso de terminación anticipada (notice period)
- Horas y metodología de tracking (si aplica)

**En caso de conflicto entre MSA y SOW:** la mayoría de contratos establece que el MSA tiene prioridad en asuntos legales (IP, indemnización, liability), mientras el SOW prevalece en condiciones operativas (scope, rate, timing). Leer la cláusula de "order of precedence".

### Service Agreement one-shot

Alternativa al MSA+SOW. Un único documento que combina condiciones generales y específicas. Común en startups pequeñas o proyectos cortos. Es suficiente para engagements de hasta 3 meses con cliente sin historial. Para relaciones largas, la estructura MSA+SOW es más limpia.

### Qué NO firmar

- **Employment contract disfrazado de service agreement:** si el documento menciona "hours per week", "salary", "benefits", "notice of termination as employee", estás firmando un contrato de empleo. Rechazar y pedir reformulación como service agreement.
- **Agreement sin límite de liability:** si no hay cap de responsabilidad, el cliente puede reclamarte daños ilimitados por cualquier fallo. Inaceptable.
- **IP assignment total de todo tu conocimiento existente:** cesión del software que escribes en el proyecto: bien. Cesión de tu IP preexistente o de cualquier cosa que desarrolles durante el periodo del contrato: no.

---

## 2. Cláusulas críticas — qué negociar y cómo

### 2.1 IP (Intellectual Property) — la más importante

**Lo que quieren las empresas:** que todo el código que produces durante el contrato les pertenezca 100%.

**Lo que debes negociar:**
- La cesión aplica solo al trabajo producido **dentro del scope definido en el SOW**. No a proyectos paralelos, no a librerías open source que uses, no a tu setup personal de herramientas.
- Si aportas código preexistente al proyecto (tu propia librería, un framework que has desarrollado), eso no se cede — se licencia (license, not assign). Especificarlo explícitamente.
- El cliente obtiene una licencia completa para usar el resultado, no necesariamente el copyright sobre el proceso de creación.

**Cláusula razonable:**
> *"Contractor assigns to Client all IP rights in the Deliverables created specifically under this Agreement. This assignment does not include: (a) Contractor's pre-existing IP; (b) open-source components incorporated under their existing licenses; (c) any work developed outside the scope defined in the SOW."*

### 2.2 Non-compete

**Lo que quieren las empresas:** que no trabajes para sus competidores durante y después del contrato.

**La realidad legal:** para autónomos contratados bajo derecho civil/mercantil (no laboral), las cláusulas de non-compete son válidas si son razonables en tiempo, geografía y scope. Sin compensación económica específica, son difíciles de ejecutar en muchos sistemas europeos.

**Lo que puedes negociar:**
- Duración máxima: **6 meses** post-contrato. Un año es demasiado.
- Geografía: solo el mercado donde opera el cliente.
- Scope: solo competidores directos y definidos por nombre, no "empresas en el mismo sector".
- Durante el contrato: razonable. Post-contrato sin compensación: debatir.

**Red flag:** non-compete de 2 años en toda la UE sin compensación económica. Rechazar o consultar abogado antes de firmar.

### 2.3 Indemnification (indemnización)

**Lo que quieren las empresas:** que si el código que entregas causa un daño (infracción de IP, bug en producción, brecha de seguridad), te hagas responsable de las consecuencias económicas.

**Lo que debes negociar:**
- **Cap de responsabilidad:** limitar la indemnización al valor total del contrato (fees paid under the agreement). Sin cap, podrías responder por daños millonarios por un error puntual.
- **Carve-outs:** el cap no aplica en casos de dolo (willful misconduct) o fraude — esto es razonable.
- **IP indemnification recíproca:** el cliente también te indemniza si te proporciona materiales con IP de terceros que generan reclamaciones.

**Cláusula tipo:**
> *"Each party's total liability under this Agreement shall not exceed the total fees paid by Client in the twelve (12) months preceding the claim."*

### 2.4 Payment terms

**Standard:** Net 30 — el cliente paga dentro de los 30 días desde la fecha de factura.

**Lo que puedes pedir:**
- **Net 15** para contratos cortos o sin historial de relación.
- **Net 30** es aceptable para clientes establecidos.
- **Net 60+** negociar a la baja — no aceptar. Net 60 significa que tienes dinero inmovilizado dos meses y asumes el riesgo de liquidez.

Para contratos de duración media (6-12 meses), negociar facturación **mensual**, no semanal ni por hito. La mensualidad da previsibilidad a ambas partes.

### 2.5 Notice period (aviso de terminación anticipada)

Sin notice period, el cliente puede cancelar el contrato el viernes y el lunes ya no tienes ingresos.

**Lo que debes pedir:**
- **4 semanas mínimo** en ambas direcciones (tú también puedes irte dando 4 semanas de aviso).
- Para contratos de 6+ meses: 4-8 semanas.
- Que el notice period se aplique tanto para terminación del contrato completo como para no renovación.

**Cláusula tipo:**
> *"Either party may terminate this Agreement upon [30] days' written notice. In case of termination, Client shall compensate Contractor for all work performed through the termination date."*

### 2.6 Time tracking

Algunos clientes requieren registro de horas. Es razonable para contratos por hora, menos para contratos day-rate.

**Si el cliente requiere timesheet:**
- Definir en el SOW la herramienta (Toggl, Harvest, su propio sistema interno).
- Definir el proceso de aprobación — quién aprueba, en qué plazo.
- La factura no puede emitirse sin la aprobación del timesheet — esto puede retrasar el cobro. Negociar: si el cliente no aprueba en 5 días hábiles, se considera aprobado automáticamente.

**Si el contrato es day-rate (tarifa diaria fija):**
- El timesheet puede ser más simple — confirmación de días trabajados por email.
- Definir qué cuenta como "día" (8h, o media jornada, o per project).

---

## 3. Divisa y FX

### Qué divisa facturar

| Cliente en | Facturar en | Por qué |
|---|---|---|
| Francia, Alemania, España | **EUR** | Sin FX risk. Más sencillo. |
| UK | **GBP** o EUR | GBP es lo habitual en UK. EUR posible si el cliente lo prefiere. |
| USA, Canadá | **USD** | El cliente no suele querer EUR. |
| Suiza | **CHF** o EUR | CHF da rates más altos. EUR es más fácil. |

**Recomendación:** facturar en EUR cuando sea posible. Reduce la fricción de conversión y la incertidumbre cambiaria.

### Gestión del FX con clientes no-EUR

Usando Wise Business:
- El cliente te transfiere en su divisa local.
- Wise convierte al tipo mid-market (sin margen oculto).
- Ahorro típico: 2-4% vs transferencia bancaria tradicional.

Para la declaración fiscal (Modelo 303, Modelo 130, Renta):
- El importe a declarar es **siempre en EUR**.
- Tipo de cambio de referencia: tipo BCE del día de la factura (disponible en ecb.europa.eu/stats/exchange).
- Tu gestoría hace la conversión. Asegúrate de que tiene el tipo de cambio de cada factura documentado.

### Riesgo de tipo de cambio

Si facturas en GBP o USD y el contrato dura 6 meses, el tipo de cambio puede variar un 5-10%. Para contratos cortos o pagos rápidos (Net 30) el riesgo es bajo. Para contratos de 12 meses en divisa no-EUR, considera facturar en EUR directamente si el cliente lo acepta.

---

## 4. Ciclo de cobro — timesheet → factura → pago

### El flujo estándar

```
Fin del período (fin de mes habitualmente)
    │
    ▼
[Si hay timesheet] Enviar timesheet al manager
    │ Esperar aprobación (normalmente 2-5 días hábiles)
    ▼
Emitir factura (fecha: fin del período o día de aprobación)
    │
    ▼
Cliente procesa el pago
    │ Plazo: los días de payment terms desde fecha factura (Net 30 = 30 días)
    ▼
Cobro recibido en cuenta Wise / bancaria
    │
    ▼
Tu gestoría registra el cobro y lo incluye en el 303/130 del trimestre
```

### Qué controlar cada mes

- Emitir la factura el primer día laborable del mes siguiente (o el último del mes en curso).
- Anotar la fecha de vencimiento de cada factura (fecha + payment terms).
- Hacer seguimiento 3 días antes del vencimiento si no hay confirmación de pago.
- No esperar a que venza para hacer seguimiento — muchas empresas tienen ciclos internos de aprobación de pagos que tardan.

---

## 5. Qué hacer si no pagan

### Escalada en orden

**Paso 1 — Recordatorio amistoso (D+1 del vencimiento)**

Email directo al contacto de finanzas + al manager:
> *"Hi [name], just a quick note that invoice #INT-2026-003 for [amount] was due on [date]. Could you let me know the expected payment date? Thanks."*

No empezar con tono agresivo — la mayoría de retrasos son administrativos, no intencionales.

**Paso 2 — Reclamación formal (D+7 del vencimiento)**

Email documentado (o burofax si tienes acceso presencial). La Agencia Tributaria acepta el correo electrónico como medio fehaciente desde 2024 para efectos de reclamar impagos. Guardar el email con acuse de recibo.

**Paso 3 — Monitorio europeo (clientes UE, D+30)**

**Reglamento (CE) 1896/2006.** Proceso específico para reclamaciones transfronterizas dentro de la UE:
- Aplica a deudas civiles y mercantiles entre partes de distintos estados miembros.
- Se presenta ante los juzgados del país del deudor (o del país de la prestación del servicio según el contrato).
- El reglamento incluye formularios estandarizados — rellenar en el idioma del tribunal del país del deudor.
- Funcionamiento desigual por país: eficiente en DE/AT, lento en FR/IT.
- Para deudas pequeñas (< €5.000): usar **Reglamento (CE) 861/2007** (proceso de escasa cuantía) — más sencillo.

**Paso 4 — Para clientes fuera de la UE (UK, US)**

No hay equivalente europeo. Opciones:
- Arbitraje comercial internacional (caro, para deudas grandes).
- Cláusula de dispute resolution en el contrato — si incluiste una cláusula de arbitraje (AAA, ICC), activarla.
- Si la deuda es pequeña, evaluarlo económicamente: el coste de reclamar puede superar la deuda.

**Paso 5 — Recuperar el IVA ante la AEAT**

Si la factura es incobrable, puedes solicitar la rectificación de la declaración de IVA para recuperar el IVA devengado no cobrado. Condición: haber agotado los mecanismos de reclamación documentados (burofax o email fehaciente). La normativa 2024 amplió los medios válidos para esta acreditación.

**Compensación adicional:** por cada factura impagada, tienes derecho a reclamar **40€ de compensación** por gastos de gestión de cobro (Art. 6.1 Directiva 2011/7/UE, transpuesta en la Ley 3/2004). Se puede incluir en la reclamación formal.

---

## 6. Templates y recursos de referencia

### Dónde encontrar templates de MSA/SOW revisables

- **Law Insider** (lawinsider.com): repositorio de contratos reales de empresas cotizadas. Buscar "Master Service Agreement software development" o "Contractor Agreement SaaS". Son contratos reales presentados ante la SEC — lenguaje estándar de mercado.
- **Clerky** (clerky.com): templates para startups, especialmente US. Buena referencia para contratos con clientes americanos.
- **Mollie Docs** / Stripe Atlas guides: documentación sobre contratos de pago y servicios para founders europeos — útil para entender el lenguaje de cláusulas de pago.

### Lo que debes hacer con cualquier template

1. Leer la sección de IP y marcar cualquier cesión más amplia de lo descrito en la sección 2.1.
2. Leer la sección de liability y verificar que haya cap.
3. Leer la sección de non-compete y verificar duración y scope.
4. Si el contrato está en inglés bajo ley francesa/alemana/UK, buscar que la ley aplicable sea la del país que conozcas o que el arbitraje sea en una jurisdicción neutral (ICC, AAA).
5. Si hay algo que no entiendes: abogado antes de firmar. Un contrato de 6 meses a €500/día es un acuerdo de €65.000. El coste de revisión legal (~300-500€) es irrelevante comparado con una cláusula de IP mal firmada.

---

*Fuentes consultadas (abril 2026): upcounsel.com (MSA key clauses); hyperstart.com (MSA guide); gwabogados.es (monitorio europeo); Reglamento CE 1896/2006; Directiva 2011/7/UE morosidad; autonomosyemprendedor.es (burofax y medios fehacientes 2024).*
