# W2 — Setup operacional del contractor

> **Disclaimer:** documento de investigación, no asesoría legal ni fiscal. Los pasos descritos son orientativos; tu situación puede requerir variaciones. Consulta con gestor fiscal antes de ejecutar cualquier trámite.

Este documento es un **checklist ejecutable** ordenado cronológicamente. Cada paso tiene su condición de entrada y de salida.

---

## Paso 1 — Alta censal en Hacienda (Modelo 036)

### Contexto

El Modelo 037 (versión simplificada) fue **suprimido** por la Orden HAC/1526/2024, publicada en el BOE el 9 de enero de 2025. Desde entonces, **solo existe el Modelo 036** para todos los trámites de alta, modificación y baja en el Censo de Empresarios, Profesionales y Retenedores.

El 036 tiene ~20 páginas. Para un contractor con cliente extranjero, solo son relevantes unas pocas:

### Campos críticos del Modelo 036

| Página/Casilla | Qué declaras |
|---|---|
| **Página 1, casilla 110** | Causa: alta (primera vez) |
| **Página 2** | Datos de identificación (NIF, nombre, domicilio fiscal) |
| **Página 3, casilla 403** | Fecha de inicio de actividad |
| **Página 3, casilla 407** | Epígrafe IAE: **763** (Programadores y analistas informática) — subapartado 763.1 |
| **Página 3** | CNAE: **6201** (Programación informática) |
| **Página 5, casilla 582** | ✅ Solicitud de alta en el **ROI** (Registro Operadores Intracomunitarios) |
| **Página 5, casilla 584** | Fecha desde la que solicitas el ROI (pon la misma que el inicio de actividad) |
| **Página 5, casilla 501** | Régimen IVA: régimen general |
| **Página 5, casilla 700** | Régimen IRPF: estimación directa simplificada |

### ROI — lo más urgente

La AEAT tarda hasta **3 meses** en aprobar el ROI. Sin ROI aprobado no puedes emitir facturas a clientes UE sin IVA. Si tu primer cliente es europeo y no tienes ROI, tendrás que facturar con IVA español (21%) y luego rectificar cuando llegue la aprobación — posible pero incómodo.

**Solicitar el ROI el día uno.** La AEAT puede pedir documentación que acredite que necesitas el ROI: email de un cliente potencial, un contrato preliminar, capturas de oferta de trabajo. Tenla preparada.

La resolución llega por carta certificada al domicilio fiscal. Si no hay respuesta en 3 meses, se considera denegada — hay que volver a solicitar o recurrir.

### Si también facturas a clientes no-UE (UK, EE.UU., Suiza)

El ROI solo es necesario para EU B2B. Para clientes fuera de la UE no necesitas ROI, pero sí declarar esas facturas en el Modelo 303 (casilla 120, "no sujeta Art. 69.Uno.1 LIVA"). El 036 basta para cubrir ambos casos.

### Cómo presentar el 036

- **Online:** via Sede Electrónica de la AEAT con certificado digital, DNIe o Cl@ve. Es el método preferido — confirma presentación al instante.
- **Presencial:** en la Administración o Delegación de la AEAT correspondiente a tu domicilio fiscal. Más lento.

Plazo: antes del inicio de la actividad (o a más tardar el día del inicio).

---

## Paso 2 — Alta en el RETA (Seguridad Social)

### Cuándo

Simultánea al alta censal. Plazo: dentro de los **30 días naturales** del inicio de actividad declarado en el 036. Si tardas más, la alta se formaliza igualmente pero puedes incurrir en recargos.

### Dónde

- **Online:** Sede electrónica de la Seguridad Social ([importass.seg-social.es](https://importass.seg-social.es)) con certificado digital o Cl@ve.
- **Presencial:** Dirección Provincial de la Seguridad Social o Centro de Atención e Información de la Seguridad Social (CAISS).

### Formulario: TA.0521

Es el modelo de alta en el RETA. Campos relevantes:
- Actividad económica: coincidir con el IAE del 036 (763).
- **Tarifa plana:** marcar expresamente la casilla de tarifa plana si cumples los requisitos (primer alta o sin alta en RETA los últimos 2 años). **No se puede pedir retroactivamente.**
- Contingencias: marcar "incapacidad temporal" — sin ella no cobras si te pones enfermo. Para un contractor sin red de seguridad del asalariado es imprescindible.
- Base de cotización: elige la base mínima del tramo que corresponde a tus rendimientos netos previstos. Si esperas €3.000 netos/mes, tramo 8 (~€470/mes de cuota). Puedes cambiar hasta 6 veces al año.

### Tarifa plana: recordatorio rápido

- 80€/mes (+ MEI 0,9% = ~€88,72/mes reales) durante 12 meses.
- Prorrogable otros 12 meses si rendimientos netos < SMI (~€965/mes en 2026).
- Solo disponible si no has estado en el RETA en los 2 años anteriores.
- Del mes 13 en adelante: pagas según tus rendimientos netos reales (hacienda regulariza al año siguiente).

---

## Paso 3 — Cuenta bancaria business

### Por qué abrir una cuenta separada

No es obligatorio legalmente, pero es necesario en la práctica:
- La gestoría necesita separar movimientos profesionales de personales para cuadrar las declaraciones.
- Facilita el cálculo del IRPF trimestral (sabes exactamente lo que has cobrado).
- Protege ante una inspección: mezclar personal y profesional es un indicio negativo.

### Opciones y comparativa

| Opción | IBAN | Forex | Cuota mensual | Bizum | Ideal para |
|---|---|---|---|---|---|
| **Wise Business** | Belga (BE) | Real (sin margen) | 0€ (fija) + comisión por uso | ❌ | Cobros en GBP/USD, clientes UK/US |
| **Revolut Business** | Español (ES) | Real (hasta límite según plan) | Plan Grow: ~28€/mes | ✅ | Domiciliar cuota RETA, operaciones locales |
| **BBVA Pymes / Openbank Empresas** | Español (ES) | Malo (márgenes bancarios) | Variable (algunos gratuitos) | ✅ | Si prefieres banco tradicional |
| **Cuenta personal con nombre** | Español (ES) | — | 0€ | ✅ | Funciona temporalmente, no recomendable |

### Recomendación para contractor con clientes EU/UK/US

**Setup de dos cuentas:**

1. **Wise Business (principal para cobros internacionales):**
   - Abre IBANs en EUR, GBP, USD. Tus clientes te pagan "como si fuera cuenta local" en su divisa.
   - Tipo de cambio mid-market, sin margen. Ahorras 2-4% vs transferencia bancaria tradicional.
   - Sin cuota mensual. Pagas solo al convertir divisa o hacer transferencia.
   - IBAN belga: tu gestoría lo acepta sin problema. El SEPA obliga a las empresas a aceptar IBANs europeos.
   - Modelo 720: si tienes más de 50.000€ en cuenta en el extranjero a 31/12, hay que declararlo. Para cobros normales de contractor no suele alcanzarse.

2. **Cuenta española (secundaria para domiciliaciones):**
   - Domicilia la cuota RETA aquí (Seguridad Social prefiere IBAN español).
   - Bizum si lo usas para pagos personales.
   - Openbank Empresas (gratuita) o Revolut Business (plan Grow) son opciones razonables.

### Proceso apertura Wise Business

1. Registro en wise.com/business → país España → autónomo persona física.
2. Documentación: DNI o pasaporte + justificante de alta como autónomo (resolución de la AEAT o primer pago de RETA).
3. Aprobación: normalmente en 1-3 días hábiles online.
4. Activa los detalles bancarios en EUR, GBP, USD desde el panel.

---

## Paso 4 — Gestoría

### Por qué es imprescindible

Un contractor con clientes extranjeros tiene estas obligaciones periódicas:
- Modelo 303 (IVA): trimestral — 4 veces al año.
- Modelo 349 (intracomunitario): trimestral o mensual según volumen.
- Modelo 130 (pago fraccionado IRPF): trimestral — 4 veces al año.
- Modelo 390 (resumen IVA): anual.
- Declaración de Renta: anual.

En total: 12-18 presentaciones al año. Error en un plazo = recargo mínimo del 5% (dentro de los 3 meses) hasta el 20% (pasados 12 meses), más intereses.

El coste de una gestoría especializada (~960€/año) es pequeño frente al riesgo de un error.

### Qué servicios mínimos necesitas

| Servicio | Incluido en el ~80€/mes estándar |
|---|---|
| Modelos trimestrales (303, 349, 130) | ✅ Sí |
| Modelos anuales (390, Renta) | ✅ Normalmente |
| Asesoramiento IAE y ROI | ✅ Al inicio |
| Seguimiento del ROI hasta aprobación | ⚠️ Depende — preguntar |
| Facturación (emisión de facturas) | ❌ Generalmente no — tú las emites |

### Rango de precios 2026

- **Autónomo sin empleados, facturación B2B internacional simple:** 60-100€/mes.
- **Con mayor volumen o clientes en múltiples países:** 100-150€/mes.
- Las gestorías "solo online" suelen ser más baratas (~45-70€/mes) pero con menos disponibilidad para consultas.

### Cómo elegirla — checklist de preguntas para la primera llamada

1. "¿Lleváis autónomos que facturan a empresas europeas y no europeas?"
2. "¿Presentáis el Modelo 349 si hace falta mensual?"
3. "¿Ayudáis a gestionar la solicitud del ROI y el seguimiento hasta aprobación?"
4. "¿Estáis familiarizados con la no sujeción de servicios a clientes no-UE (Art. 69.Uno.1 LIVA)?"
5. "¿Qué herramienta de facturación recomendáis o proporcionáis?"

### Red flags

- Confunden "exento" con "no sujeto" al hablar de clientes no-UE.
- No saben qué es el Modelo 349.
- No han llevado nunca a un autónomo con cliente extranjero.
- Piden que envíes todo en papel.
- No dan respuesta a consultas por correo en menos de 48h laborables.

---

## Paso 5 — Herramienta de facturación

### Opciones para contractor con volumen bajo (1-8 facturas/mes)

La mayoría de contractors emiten 1-2 facturas al mes (una por cliente, a veces dos si hay más de un proyecto). No necesitas un sistema sofisticado.

| Herramienta | Coste aprox. | Modelo 349 auto | Buen para |
|---|---|---|---|
| **Quipu** | ~10-20€/mes | ⚠️ Limitado | Autónomos sencillos, integra con asesoría |
| **Holded** | ~30-60€/mes | ✅ Sí | Si quieres más control (CRM, proyectos) |
| **Contasimple** | ~8-15€/mes | ⚠️ Básico | Presupuesto ajustado |
| **La herramienta de la gestoría** | Incluida en cuota | Depende | Si tu gestoría lo ofrece — lo más cómodo |
| **Plantilla propia (Word/Google Docs + PDF)** | 0€ | N/A | Si emites < 4 facturas/mes y eres disciplinado |

**Recomendación práctica:** pregunta a la gestoría que elijas qué herramienta usan o recomiendan. Muchas gestorías tienen acceso compartido a herramientas que ya conocen y facilitan el proceso contable. Usar la misma herramienta que tu gestora elimina el trabajo de exportar/enviar datos.

---

## Paso 6 — Plantilla de factura compliant

### Requisitos legales (Reglamento de Facturación RD 1619/2012)

Toda factura debe incluir:

```
1. Número y serie (ej. 2026-001, o INT-2026-001 para internacionales)
2. Fecha de expedición
3. Nombre y apellidos / razón social del emisor (tú)
4. NIF del emisor
5. NIF-IVA del emisor (ES + tu NIF, ej. ES12345678A) — para EU B2B
6. Domicilio fiscal del emisor
7. Nombre / razón social del cliente
8. NIF-IVA del cliente (verificado en VIES)
9. Dirección del cliente
10. Descripción del servicio
11. Período de prestación del servicio (fecha inicio – fin del período facturado)
12. Importe base
13. Tipo y cuota de IVA — o mención de exención / no sujeción
14. Importe total
```

### Mención legal según destino del cliente

**Cliente empresa UE (reverse charge):**
```
IVA: 0% — Inversión del sujeto pasivo — Art. 44 Directiva 2006/112/CE
```
O en inglés para clientes angloparlantes de UE:
```
VAT: 0% — Reverse charge applies — Art. 44 EU VAT Directive 2006/112/EC
```

**Cliente empresa no-UE (US, UK, Suiza, etc.):**
```
IVA: no sujeta — Art. 69.Uno.1° Ley 37/1992
```
O en inglés:
```
VAT: Not applicable — Service located outside Spanish VAT territory (Art. 69.1 Spanish VAT Law)
```

**Nunca poner solo "IVA: 0%"** sin la mención legal — Hacienda puede rechazar la exención.

### Divisa y conversión

- Puedes facturar en EUR, GBP, USD u otras monedas.
- Si facturas en divisa distinta al EUR, incluye el tipo de cambio aplicado y la fecha de referencia (tipo BCE del día de la factura o del cobro).
- La declaración en los modelos 303 y 349 siempre se hace en EUR — tu gestoría hará la conversión.

### Numeración de series

Recomendado usar series separadas:
- `2026-XXX` para facturas nacionales (si tuvieras).
- `INT-2026-XXX` para facturas internacionales (intracomunitarias + extracomunitarias).

La numeración debe ser **correlativa y sin huecos** dentro de cada serie. No es necesario que los números sean globalmente correlativos entre series.

### Conservación

Guarda las facturas al menos **4 años** (período de prescripción IRPF) y **6 años** (IVA). En formato digital es suficiente — sin necesidad de papel — pero el fichero debe ser legible e inalterable (PDF o similar).

---

## Orden de ejecución y tiempos

```
Semana 1:
├── Presentar Modelo 036 (incluye solicitud ROI)
└── Dar de alta en RETA (TA.0521 con tarifa plana)

Semana 1-2:
├── Abrir Wise Business (1-3 días hábiles)
└── Abrir cuenta española secundaria (Revolut/Openbank)

Semana 1-3:
├── Contratar gestoría
└── Definir herramienta de facturación

Mes 1-3:
└── Seguimiento del ROI hasta aprobación (la gestoría puede ayudar)

Antes de emitir primera factura:
├── ¿Tienes el ROI aprobado? → si es cliente EU, esperar o facturar con IVA y rectificar
├── ¿Tu gestoría está contratada y sabe que vas a empezar?
└── ¿Tienes la plantilla de factura con la mención correcta según el destino?
```

---

*Fuentes consultadas (abril 2026): AEAT sede electrónica (Modelo 036, ROI); Seguridad Social — RETA; Orden HAC/1526/2024 (supresión 037); Infoautónomos; wise.com; Reglamento de Facturación RD 1619/2012; getquipu.com; holded.com.*
