# W1 — Fundamentos legal-fiscales del contractor en España

> **Disclaimer:** documento de investigación, no asesoría fiscal ni legal. Los datos reflejan la normativa vigente en abril de 2026. Cualquier decisión real requiere consulta con gestor/asesor fiscal colegiado. Las cifras fiscales (cuotas, tramos) son las aprobadas a fecha de publicación y pueden cambiar con nueva normativa o PGE.

---

## 1. La figura: autónomo ordinario

El contractor en España **no existe como figura legal propia**. Es un autónomo dado de alta en el RETA, con toda la carga burocrática y fiscal que eso implica. La diferencia respecto al freelance clásico está en la estructura del acuerdo (6-12 meses, un solo cliente, full-time) y en la nacionalidad del cliente (extranjero).

El marco legal de referencia es:
- **Tributario:** Ley 35/2006 del IRPF + RD 439/2007 (Reglamento IRPF) + Ley 37/1992 del IVA.
- **Laboral:** Real Decreto Legislativo 2/2015 (Estatuto de los Trabajadores, ET).
- **Seguridad Social:** RETA regulado por Real Decreto Legislativo 8/2015 (TRLGSS).

---

## 2. Falso autónomo — el riesgo central

### 2.1 Definición legal

La presunción de laboralidad (Art. 1.1 ET) establece que un trabajador es asalariado cuando presta servicios voluntariamente, con ajenidad y dependencia, a cambio de retribución. El Art. 1.2 ET aclara que esta presunción aplica aunque haya un contrato mercantil de por medio.

**Ajenidad:** los frutos del trabajo pertenecen íntegramente al cliente; el autónomo no asume riesgo económico ni participa en beneficios.

**Dependencia:** el autónomo trabaja dentro del ámbito de organización y dirección del cliente — horario, herramientas, órdenes directas, metodología impuesta.

### 2.2 Indicios que usa la ITSS

La inspección no mira el contrato, mira la realidad. Los indicios documentados más relevantes para perfiles tech:

| Indicio de laboralidad | Indicio de independencia real |
|---|---|
| Email @empresa.com | Email propio |
| Portátil de empresa | Portátil propio |
| Jornada fija impuesta | Horario autodeterminado |
| Tareas asignadas por manager | Entrega de resultado pactado |
| Acceso VPN corporativo exclusivo | Herramientas y accesos propios |
| Un solo pagador al 100% | Diversificación de clientes |
| Factura idéntica cada mes | Factura varía con el trabajo entregado |

La ITSS desde 2025 puede declarar la laboralidad en su acta directamente, sin necesidad de demanda judicial previa (confirmado por el Sindicato USO, 2025). Esto acelera la exposición para ambas partes.

### 2.3 Sanciones

- **Para el cliente (empresa):** multa de **751€ a 10.000€ por trabajador** (Art. 8.11 Ley de Infracciones y Sanciones en el Orden Social, LISOS). Más cotizaciones retroactivas no ingresadas.
- **Para el autónomo:** reclasificación como empleado — pierde el régimen de autónomo y queda encuadrado en el RGSS retroactivamente. No hay sanción económica directa al trabajador, pero implica reclamaciones de diferencias de cotización.

### 2.4 Jurisprudencia reciente

Los casos Glovo (STJUE C-214/20, 2020; STS 25/09/2020) y Deliveroo establecieron que la mera existencia de un contrato mercantil no elimina la relación laboral si concurren ajenidad y dependencia. Aunque aplican a riders, los criterios son los mismos que la ITSS usa en tech: lo relevante es cómo se trabaja, no cómo se llama el acuerdo.

### 2.5 Por qué el cliente extranjero reduce el riesgo

Los mismos criterios aplican técnicamente. Lo que cambia es la **fricción operativa de la ITSS**:

1. La ITSS tiene jurisdicción española, no alemana ni francesa.
2. Para actuar contra una empresa sin presencia en España, necesita cooperación administrativa internacional — costosa y sin precedente documental en el sector tech.
3. No hay casos registrados de inspección y reclasificación de un contractor español con cliente extranjero sin filial en España.

**Lo que sí puede ocurrir:** si la empresa extranjera tiene filial o establecimiento permanente en España, la ITSS recupera jurisdicción directa. En ese caso el riesgo es el mismo que con un cliente español.

**Mitigación práctica:**
- Contrato mercantil limpio (sin cláusulas de horario, sin exclusividad de herramientas, sin subordinación).
- Al menos un cliente secundario que rompa la dependencia del 100%.
- Facturación que varíe algo mes a mes (refleja trabajo real, no nómina disfrazada).

---

## 3. TRADE — por qué no es la solución

El **Trabajador Autónomo Económicamente Dependiente** (TRADE) es una figura legal española (Ley 20/2007, Estatuto del Trabajo Autónomo) para autónomos que cobran más del 75% de sus ingresos de un solo cliente.

**Por qué no aplica al contractor con cliente extranjero:**

1. El registro como TRADE es obligatorio y se hace ante el SEPE. Para cliente extranjero, el trámite es presencial en la Dirección Provincial, porque el sistema online no acepta CIF que no sea español.
2. El TRADE requiere que el contrato cumpla condiciones específicas de la Ley 20/2007: duración mínima, definición de actividad, horario concertado. Estas condiciones suelen estar en tensión con el modelo contractor.
3. No aporta ventajas fiscales. Tributa igual que autónomo ordinario. Solo añade protecciones contractuales (preaviso de rescisión, derecho a vacaciones pactadas).
4. Más burocracia sin beneficio neto para el modelo que nos ocupa.

**Conclusión:** el TRADE es irrelevante para contractors con cliente extranjero. Alta como autónomo ordinario es suficiente y más flexible.

---

## 4. IRPF — cómo tributa el autónomo contractor

### 4.1 Régimen: Estimación Directa Simplificada

Aplicable si la facturación anual es inferior a **600.000€**. Toda facturación de contractor cae aquí.

Diferencia respecto a la normal: se permite una deducción adicional del **5% del rendimiento neto** en concepto de gastos de difícil justificación, con límite de **2.000€ anuales**. Esto reduce ligeramente la base imponible sin necesidad de factura.

### 4.2 Tramos IRPF 2026 (base imponible general — sin cambios respecto a 2025)

La escala es progresiva: cada tramo aplica solo sobre el exceso que entra en él, no sobre la renta total.

| Base liquidable | Tipo marginal (estatal) | Tipo aprox. combinado (orientativo) |
|---|---|---|
| Hasta 12.450 € | 9,50% | ~19% |
| 12.450 – 20.200 € | 12,00% | ~24% |
| 20.200 – 35.200 € | 15,00% | ~30% |
| 35.200 – 60.000 € | 18,50% | ~37% |
| 60.000 – 300.000 € | 22,50% | ~45% |
| Más de 300.000 € | 24,50% | ~47% |

> **Madrid vs. Cataluña:** el tipo marginal máximo combinado (estatal + autonómico) en Madrid es del **43,5%**; en Cataluña o Comunidad Valenciana puede llegar al **54%**. La residencia fiscal importa. Fuente: taxdown.es, datos IRPF 2026.

**Para un contractor que factura €100.000 y tiene €10.000 de gastos deducibles + €5.760 RETA:**

- Rendimiento neto: €100.000 - €10.000 - €5.760 = €84.240
- IRPF en Madrid (orientativo): ~€28.000-30.000
- Neto en mano: ~€54.000-56.000

### 4.3 Retenciones en facturas

Los clientes **españoles** están obligados a retener IRPF en las facturas de profesionales:
- **15% general** (autónomos con más de 2 años de actividad)
- **7% reducido** durante el año de inicio + los dos siguientes

Los clientes **extranjeros** no retienen nada — esa responsabilidad recae íntegramente en el autónomo. Debes presentar tú mismo los pagos a cuenta (Modelo 130) y reservar el porcentaje correspondiente de cada cobro.

**Regla práctica:** reserva el 30-35% de cada factura cobrada nada más recibirla. Ese dinero no es tuyo.

### 4.4 Modelo 130 — pago fraccionado trimestral

Obligatorio si menos del 70% de tus ingresos tienen retención de fuente española. Con clientes exclusivamente extranjeros, siempre obligatorio.

**Cálculo:**
```
(Ingresos acumulados año - Gastos acumulados año) × 20% - Pagos 130 previos = a pagar
```

La deducción del 5% por gastos de difícil justificación se aplica sobre el rendimiento neto antes del 20%.

**Plazos 2026:**
- Q1: 1-20 abril 2026
- Q2: 1-20 julio 2026
- Q3: 1-20 octubre 2026
- Q4: 1-30 enero 2027

---

## 5. IVA — tres casuísticas según el cliente

### 5.1 Cliente empresa en la UE — Reverse Charge (inversión del sujeto pasivo)

**Base legal:** Art. 44 Directiva 2006/112/CE + Art. 69 Ley 37/1992 del IVA.

Los servicios B2B entre empresas de distintos estados miembros se localizan en la sede del destinatario. Si tu cliente es una empresa alemana, el servicio tributa en Alemania, no en España. Consecuencia: la factura no lleva IVA español.

**Condiciones para facturar sin IVA:**
1. Estar dado de alta en el ROI (Registro Operadores Intracomunitarios) y tener NIF-IVA.
2. Verificar que el cliente tiene NIF-IVA intracomunitario válido en el sistema **VIES** (ec.europa.eu/taxation_customs/vies) antes de emitir la factura.
3. Incluir en la factura la mención: *"Inversión del sujeto pasivo — Art. 44 Directiva 2006/112/CE / Art. 69 Ley 37/1992"*.

**Modelos obligatorios:**
- **Modelo 303** trimestral: incluir la operación en la casilla de operaciones exentas intracomunitarias.
- **Modelo 349** mensual/trimestral: declaración recapitulativa de operaciones intracomunitarias. Debe cuadrar con el 303.
- **Modelo 390** anual: resumen de IVA.

El ROI tarda hasta 3 meses en aprobarse (AEAT puede solicitar documentación — emails de clientes potenciales, contratos previos). Sin ROI aprobado, **no puedes emitir facturas intracomunitarias sin IVA**. Solicitar el primer día.

### 5.2 Cliente empresa fuera de la UE (EE.UU., UK, Suiza, etc.)

**Base legal:** Art. 69.Uno.1° Ley 37/1992.

El servicio se considera prestado en el lugar donde está establecido el cliente. Si el cliente está fuera del Territorio de Aplicación del Impuesto (TAI), la operación **no está sujeta** a IVA español.

Nota: el **Reino Unido es tercera país** desde el Brexit (1 enero 2021). Mismo tratamiento que EE.UU.

**Factura sin IVA.** Mención obligatoria: *"Operación no sujeta al IVA — Art. 69.Uno.1° Ley 37/1992"*.

**Diferencia crítica "no sujeta" ≠ "exenta":** las operaciones no sujetas permiten deducir íntegramente el IVA soportado en los gastos relacionados. Las exentas (Art. 20 LIVA) limitan esa deducción. Usar el término incorrecto en el 303 cuesta dinero.

**Modelos:**
- **Modelo 303:** casilla 120 (operaciones no sujetas). No modelo 349.
- No se necesita ROI para clientes no-UE.

### 5.3 Comparativa rápida

| | EU B2B | No-UE B2B |
|---|---|---|
| IVA en factura | 0% (reverse charge) | 0% (no sujeta) |
| Base legal | Art. 44 Dir. 2006/112/CE | Art. 69.Uno.1° LIVA |
| ROI necesario | ✅ Sí | ❌ No |
| VIES check | ✅ Sí | ❌ No |
| Modelo 303 | ✅ Sí (exentas intracomunitarias) | ✅ Sí (casilla 120) |
| Modelo 349 | ✅ Sí | ❌ No |
| Mención en factura | Art. 44 Directiva | Art. 69.Uno.1° LIVA |

---

## 6. RETA — Seguridad Social 2026

### 6.1 Sistema de tramos por ingresos reales

Desde 2023 rige un sistema de **15 tramos** basado en los rendimientos netos mensuales previstos. La cuota 2026 se congeló respecto a 2025 (RD Ley 3/2026), con la única variación del MEI (+0,1% → 0,9% total).

| Rendimiento neto mensual | Cuota mínima mensual |
|---|---|
| < 670 € | 200 € |
| 670 – 900 € | 220 € |
| 901 – 1.166 € | 260 € |
| 1.167 – 1.700 € | 294 € |
| 1.700 – 2.030 € | 350 € |
| 2.030 – 2.330 € | 380 € |
| 2.330 – 2.760 € | 423 € |
| 2.760 – 3.190 € | 470 € |
| 3.190 – 3.620 € | 500 € |
| 3.620 – 4.050 € | 530 € |
| 4.050 – 6.000 € | 542 – 590 € |
| > 6.000 € | 590 € (máximo) |

*Tabla orientativa. Verificar en la calculadora oficial de la Seguridad Social.*

**Ajuste durante el año:** puedes cambiar de tramo hasta **6 veces al año**. Al cierre del ejercicio, la AEAT/SS compara ingresos reales con los declarados y regulariza (devolución o cargo).

**Cuota deducible en IRPF:** el 100% de la cuota RETA pagada es gasto deducible del rendimiento neto.

### 6.2 Tarifa plana para nuevos autónomos

- **Cuantía:** 80€/mes + MEI (0,9%) = ~€88,72/mes reales.
- **Duración:** 12 meses. Prorrogable otros 12 meses si los rendimientos netos son inferiores al SMI (~965€/mes en 2026).
- **Requisito:** no haber estado dado de alta en el RETA en los **2 años anteriores** (3 años si ya disfrutaste la tarifa plana antes).
- **Solicitud:** hay que marcarla expresamente en el modelo TA.0521 en el momento del alta. No se puede pedir retroactivamente.
- **Shock del mes 13:** de €88 a €290-423€/mes. Planificar el salto con 6 meses de antelación.

### 6.3 Coberturas del RETA

Las coberturas que incluye la cuota mínima:
- **Asistencia sanitaria** (acceso a la Seguridad Social — no prestación de baja laboral desde el primer día).
- **Incapacidad temporal (IT):** desde el **4° día de baja** si tienes cubierta la contingencia (optativa en el RETA, pero muy recomendable para contractors — el cliente no te paga si estás de baja).
- **Jubilación:** cotización computable para pensión. Con cuotas mínimas, la pensión esperada es baja — considerar plan de pensiones privado como complemento.
- **Cese de actividad:** acceso muy restringido (debe ser involuntario — pérdida de contrato por causas objetivas, no fin natural de un proyecto). No es comparable al paro de asalariado.

---

## 7. Deducciones fiscales típicas para dev contractor

Todas requieren factura a nombre fiscal del autónomo, directamente relacionadas con la actividad.

| Gasto | Deducción IRPF | Deducción IVA | Condición |
|---|---|---|---|
| Cuota RETA | 100% | N/A | Obligatoria |
| Gestoría / asesoría fiscal | 100% | 100% | Factura a nombre del autónomo |
| Equipos informáticos | 100% (uso exclusivo) | 100% | Exclusividad de uso profesional |
| Software / suscripciones herramientas | 100% | 100% | Uso profesional |
| Internet (línea exclusiva) | 100% | 100% | Si solo uso profesional |
| Internet (línea mixta) | 50% | 50% | Criterio Hacienda |
| Móvil (uso mixto) | 50% | 50% | Criterio Hacienda |
| Formación (cursos, libros técnicos) | 100% | 100% | Relación con actividad |
| Coworking / espacio trabajo | 100% | 100% | Factura a nombre del autónomo |
| Vivienda suministros (luz, agua, gas) | 30% × % superficie afecta | 30% × % afecta | Requiere declaración en 036 |
| Alquiler vivienda | ❌ No deducible | ❌ No | Salvo contrato mixto explícito |
| Dietas (España, sin pernocta) | Hasta 26,67€/día | N/A | Desplazamiento por actividad |
| Seguro médico privado | Hasta 500€/año/persona | N/A | Deducción en renta, no en 130 |
| Seguro RC profesional | 100% | 100% | Si relacionado con actividad |

**Gastos de difícil justificación (estimación directa simplificada):** 5% del rendimiento neto con límite de 2.000€ anuales. Sin factura requerida. Se calcula automáticamente al presentar la declaración.

**Error frecuente:** deducir el IVA de gastos en el Modelo 303 y luego intentar deducir el mismo importe en el IRPF. El IVA ya deducido en el 303 no se puede volver a deducir como gasto en IRPF. Solo el IVA no deducible (cuando la operación no genera derecho a deducir IVA) puede incluirse como mayor gasto en IRPF.

---

## 8. Autónomo vs. SL — señal de referencia para esta fase

El roadmap profundiza esto en `optimizacion.md` (Fase 6). Para contexto previo:

- Autónomo: más sencillo, menor coste fijo, tarifa plana disponible. IRPF progresivo (hasta 45-54% según CC.AA.).
- SL: Impuesto de Sociedades al 25% (23% para empresas pequeñas con facturación < 1M€). Pero: autónomo societario no puede usar tarifa plana, cuota mínima RETA de €1.000/mes base, constitución ~€1.000-3.000, gestoría más cara (~€100-150/mes).
- **Break-even fiscal orientativo:** alrededor de €50.000-70.000 de beneficio neto anual. Por debajo de esa cifra, autónomo ordinario es más eficiente.

Para el primer contrato como contractor: **autónomo ordinario** sin duda. La SL es una optimización posterior cuando el negocio esté rodado y la facturación sea estable.

---

## 9. Resumen de obligaciones periódicas

| Modelo | Periodicidad | Qué declara | Plazo |
|---|---|---|---|
| **Modelo 303** | Trimestral | IVA (ingresos vs gastos) | 1-20 del mes siguiente al trimestre |
| **Modelo 349** | Trimestral (mensual si > 50.000€ intracomunitario) | Operaciones EU B2B | 1-20 del mes siguiente |
| **Modelo 130** | Trimestral | Pago fraccionado IRPF | 1-20 del mes siguiente |
| **Modelo 390** | Anual | Resumen de IVA | Enero del año siguiente |
| **Declaración IRPF (Renta)** | Anual | Liquidación definitiva | Abril-junio del año siguiente |

Una gestoría a €80/mes gestiona todo esto. Sin gestoría, el riesgo de error y sanción es alto.

---

*Fuentes consultadas (abril 2026): AEAT sede electrónica — modelos 036/303/349/130/390; Infoautónomos; Holded; taxdown.es; tukonta.com; beel.es; Ley 37/1992 IVA; Ley 35/2006 IRPF; RD Ley 3/2026 (prórroga cuotas RETA); Directiva 2006/112/CE.*
