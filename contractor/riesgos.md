# W6 — Riesgos y pipeline

> **Disclaimer:** documento de investigación, no asesoría. Los rangos de precios de seguros son orientativos (abril 2026) — consulta corredores especializados para cotizaciones exactas. Las condiciones del cese de actividad autónomos varían y cambian con frecuencia; verifica el estado actual en la web oficial de la Seguridad Social antes de actuar.

---

## 1. Seguros

### 1.1 Responsabilidad Civil Profesional (RC)

**¿Para qué sirve?** Cubre reclamaciones de terceros por daños económicos causados durante el ejercicio de la actividad. Si entregas código defectuoso que provoca una pérdida económica al cliente (downtime en producción, brecha de seguridad, bug en integración de pagos), la RC cubre la reclamación hasta el límite asegurado.

**¿Es obligatorio?** No en general. Pero en 2026, el 95% de clientes corporativos medianos y grandes lo exigen en el contrato o en el proceso de onboarding de proveedores. Si tu primer cliente grande te lo exige, ya lo necesitas antes de firmar.

**Cobertura recomendada para developer contractor:**
- Capital asegurado: **€300.000 mínimo** (algunos clientes piden €500.000 o €1M).
- Incluir cláusula **E&O (Errors & Omissions)**: cubre errores e inexactitudes en el trabajo entregado.
- Incluir **ciberriesgos**: RGPD, brechas de datos. Las pólizas de nueva generación ya lo integran.
- Cobertura territorial: **UE mínimo**, global si tienes clientes US.

**Precios orientativos 2026:**
- Cobertura básica €150.000: desde **€85-150/año**.
- Cobertura €300.000 con E&O y ciberriesgos: **€200-400/año**.
- Cobertura €1M para cliente corporativo exigente: **€400-800/año**.

**Aseguradoras especializadas:** Hiscox (referencia europea para tech), Berkley (mejor para ciberriesgos integrados), Mapfre (más económica, red amplia).

**Deducibilidad:** 100% deducible como gasto de actividad.

---

### 1.2 Salud privada

La cobertura sanitaria del RETA incluye asistencia sanitaria del sistema público. Lo que no cubre bien:
- Especialistas con listas de espera largas (semanas a meses).
- Salud mental (cobertura muy limitada en el sistema público).
- Pruebas de imagen rápidas (ecografías, resonancias sin urgencia).

Para un contractor que no puede permitirse estar fuera de servicio semanas esperando diagnóstico: el seguro médico privado tiene sentido.

**Coste:** ~€50-100/mes para póliza individual básica (Adeslas, Sanitas, Asisa). Con copago, menos. Sin copago, más.

**Deducibilidad:** hasta **€500/año** deducibles en IRPF como gasto de actividad económica (Art. 30.2.5° LIRPF). Para unidad familiar: €500/persona/año con un máximo conjunto.

---

### 1.3 Complementario de Incapacidad Temporal (IT)

El RETA cubre la IT desde el **4° día** si tienes contratada la contingencia (obligatoria desde 2019 para autónomos en estimación directa). La prestación es ~60% de la base de cotización desde el día 4 hasta el día 20, y 75% desde el día 21.

**El problema para contractors:** si el cliente paga por días o horas trabajadas, los días de baja son días sin cobrar — aunque recibas la prestación de la SS, probablemente es inferior a tu rate diario.

**Opción complementaria:** seguro de accidentes e IT que complementa la prestación de la SS hasta el rate objetivo. Precio: ~€20-50/mes dependiendo del capital complementario.

**Prioridad:** menor que RC y salud. Configurable según tu tolerancia al riesgo.

---

## 2. Cashflow — gestión del dinero

Este es el talón de Aquiles de muchos contractors. El asalariado cobra el día 28 de cada mes pase lo que pase. El contractor cobra Net 30 después de que el cliente apruebe la factura — y a veces el cliente tarda.

### 2.1 Fondo de emergencia

**Cuánto:** mínimo **3 meses** de gastos totales (personales + RETA + gestoría + seguros). Recomendado: **6 meses**.

¿Por qué 6 meses y no 3?
- Un contrato puede cancelarse con 4 semanas de aviso.
- El proceso de búsqueda + selección + firma tarda 4-8 semanas.
- El primer cobro del nuevo cliente llega 30-60 días después de empezar.
- Pueden encadenarse dos situaciones adversas (cancelación + proceso largo).

6 meses de fondo absorbe casi cualquier escenario realista de downtime.

**Ejemplo de fondo mínimo:** developer con gastos personales de €2.000/mes + RETA €423/mes + gestoría €80/mes + seguros €30/mes = €2.533/mes. Fondo de 6 meses: **€15.200**.

**Dónde guardar el fondo:** cuenta de alta remuneración o fondo monetario. Acceso inmediato, sin riesgo de mercado. No en bolsa ni criptomonedas para el fondo de emergencia.

---

### 2.2 Buffer de impuestos — el dinero que no es tuyo

Cada vez que recibes un cobro, una parte pertenece a Hacienda. La regla básica:

**Reserva inmediata del 30-35% de cada factura cobrada** en una cuenta separada.

Este porcentaje cubre:
- IVA que has cobrado al cliente y tienes que ingresar en el Modelo 303 (21% del IVA intracomunitario no aplica directamente a tu cuenta — el reverse charge significa que no cobras IVA al cliente EU). Para clientes no-UE tampoco hay IVA. Este punto aplica si tuvieras clientes españoles.
- **IRPF (Modelo 130):** 20% de tu rendimiento neto trimestral. Si no has reservado, la sorpresa del trimestre es dolorosa.
- **Renta anual:** ajuste definitivo. Puede resultar en pago adicional o devolución.

**Mecánica práctica:**
- Abre una cuenta separada ("cuenta Hacienda").
- Cada vez que cae un cobro en tu cuenta Wise/bancaria, transfiere el 30-35% a la cuenta Hacienda ese mismo día.
- Toca esa cuenta solo cuando llega el plazo del 130 o el 303.

Con clientes EU en reverse charge, no cobras IVA — solo reservas para el IRPF. Con el 30-35% ya cubierto, nunca tendrás una sorpresa fiscal.

---

### 2.3 Payment terms y dinero en la calle

Con Net 30 y 4 facturas/mes (si tienes más de un cliente), en un momento dado tienes 30-60 días de facturación "en la calle" — emitida pero no cobrada. Para un contractor a €500/día × 22 días = €11.000/mes, eso son potencialmente €11.000-22.000 circulando en cuentas de clientes.

Implicaciones:
- No puedes contar el dinero como propio hasta que está en tu cuenta.
- Si un cliente falla, esa factura puede tardar semanas o meses en recuperarse.
- Seguimiento puntual de cobros es parte del trabajo — no es negociable.

**Herramienta simple:** una hoja de cálculo o una vista de "facturas pendientes" en tu herramienta de facturación. Fecha de vencimiento de cada factura, estado, seguimiento.

---

## 3. Downtime entre contratos

### 3.1 El coste real de un mes de downtime

Un mes sin contrato no es solo un mes sin ingresos. Es:
- 0€ de facturación.
- RETA: sigue corriendo (~€423-530/mes si estás en el tramo habitual, €88/mes en tarifa plana el primer año).
- Gestoría: sigue corriendo (~€80/mes).
- Seguros, gastos personales: siguen corriendo.

Un mes de downtime puede costar **€2.500-3.500 de coste total** (ingresos perdidos + gastos fijos mantenidos).

Dos meses seguidos de downtime = €5.000-7.000. Por eso el fondo de emergencia de 6 meses es el presupuesto real.

---

### 3.2 Planificación del siguiente contrato

**Regla básica:** empieza a buscar el siguiente contrato cuando al actual le quedan **6-8 semanas**.

Por qué 6-8 semanas:
- El proceso de selección (contacto → entrevistas → oferta → firma) tarda 3-5 semanas.
- El onboarding y el primer día de trabajo toman otra semana.
- Si empiezas la búsqueda con 4 semanas, el gap entre contratos es casi inevitable.

**La búsqueda no debe ser reactiva.** Mantener perfil activo en Malt y LinkedIn continuamente — no solo cuando buscas. Los recruiters que contactan en ese momento no saben que tienes contrato; cuando termines, tendrás un pipeline caliente.

---

### 3.3 El cese de actividad de autónomos — realidad vs. expectativa

Muchos developers asumen que si pierden el contrato pueden acceder al "paro" como un asalariado. **No funciona así.**

El cese de actividad de los autónomos (regulado por el TRLGSS) tiene condiciones muy restrictivas:

**Condiciones para acceder:**
- Baja involuntaria de la actividad (no cierre voluntario).
- Tener cotizados al menos **12 meses continuados** de la contingencia de cese de actividad (incluida automáticamente en la cuota desde 2019 para estimación directa).
- Estar al corriente de pago con la SS y con Hacienda.
- Solicitar la prestación dentro del plazo (15 días hábiles tras el cese).
- No superar el tope de edad para jubilación ordinaria.

**¿Qué cuenta como "cese involuntario"?**
- Causas económicas, técnicas, productivas u organizativas (requiere acreditación).
- Pérdida de licencia administrativa (poco aplicable a developers).
- Divorcio del autónomo colaborador (específico).
- **No cuenta:** fin natural de un contrato, no renovación por decisión del cliente, o simplemente no encontrar nuevo contrato.

**El fin de un contrato contractor no suele cualificar** para el cese de actividad en la práctica. Un contrato de 6 meses que no se renueva es un "fin de contrato", no un "cese involuntario de la actividad".

**Cuantía si qualifica:** 70% de la base reguladora durante la primera mitad del período, 50% después. Duración: de 2 a 24 meses según cotizaciones previas.

**Conclusión práctica:** no cuentes con el cese de actividad como red de seguridad. Cuenta con el fondo de emergencia.

---

## 4. Diversificación — la regla del 75%

isvidal lo menciona como ventaja secundaria del modelo contractor: la posibilidad de hacer trabajos adicionales sin problema legal.

**La regla práctica:** mantener una segunda fuente de ingresos que represente al menos el **25% de la facturación total** reduce el riesgo en dos dimensiones:

1. **Riesgo de falso autónomo:** con más del 75% de ingresos de un solo cliente puedes ser clasificado como TRADE en relación con ese cliente (si fuera español) o, teóricamente, con el mismo riesgo de dependencia con cliente extranjero. Diversificar protege.

2. **Riesgo de cashflow:** si el cliente cancela, no pierdes el 100% de los ingresos inmediatamente.

**Qué cuenta como segunda fuente:**
- Proyecto secundario pequeño (isvidal: "web al amigo panadero" 3K extras).
- Consultoría puntual: code review, asesoría técnica de pocas horas para otra empresa.
- Formación o mentoring remunerado.
- Proyecto propio (SaaS, librería, producto digital) que genere ingresos aunque sean pequeños.

La cantidad no importa tanto como que exista y esté documentada en las facturas del año.

---

## 5. Resumen de gestión de riesgos — checklist

### Antes de empezar (setup)

- [ ] Fondo de emergencia de 6 meses constituido.
- [ ] Cuenta separada "Hacienda" con primer depósito del 30-35%.
- [ ] RC profesional contratada (≥300.000€, E&O, ciberriesgos).
- [ ] Contingencia de IT incluida en la cuota RETA (verificar alta en SS).
- [ ] Gestoría contratada y enterada de que vas a empezar.

### Durante el primer contrato

- [ ] Seguimiento semanal de facturas pendientes de cobro.
- [ ] A los 3 meses: empezar a mirar el mercado con perfil actualizado.
- [ ] A las 6-8 semanas del fin: búsqueda activa del siguiente contrato.
- [ ] En cada cobro: transferir 30-35% a la cuenta Hacienda ese mismo día.
- [ ] Al terminar: documentar el engagement para el CV y perfil Malt (tecnologías, escala, resultado). Pedir testimonio al manager si es posible.

### Pipeline permanente (una vez en régimen de crucero)

- [ ] Perfil Malt y LinkedIn actualizados con rate y disponibilidad.
- [ ] Al menos 1-2 contactos con recruiters/headhunters al mes, aunque tengas contrato.
- [ ] Segunda fuente de ingresos aunque sea pequeña (rompe el 100% de dependencia).
- [ ] Revisión trimestral del fondo de emergencia — ¿sigue siendo 6 meses de gastos actuales?

---

*Fuentes consultadas (abril 2026): devfreelance.es (RC profesional developers 2026); autonotools.app; hiscox.es; TRLGSS Art. 327-341 (cese de actividad autónomos); Seguridad Social (IT autónomos); Ley 20/2007 Estatuto Trabajo Autónomo.*
