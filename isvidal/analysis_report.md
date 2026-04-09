# isvidal — Technical Recommendations Report

Analysis window: **2020–2026**. Recency weighting: exponential decay, half-life **2 years**. A mention from 2022 is worth 0.25 of a 2026 mention.

## Current Stack (trend = activo)

| Term | Topic | Score | Total | Recent | Last |
|------|-------|-------|-------|--------|------|
| Zustand | state_data | 6.48 | 11 | 7 | 2026 |
| Redux | state_data | 5.74 | 28 | 1 | 2025 |
| React Query | state_data | 5.06 | 6 | 5 | 2026 |
| useEffect | hooks | 4.07 | 13 | 2 | 2026 |
| zod | typescript | 4.00 | 4 | 4 | 2026 |
| Vite | tooling | 3.19 | 6 | 3 | 2026 |
| TanStack | state_data | 2.71 | 3 | 3 | 2026 |
| Next.js | meta_frameworks | 1.88 | 5 | 1 | 2026 |
| any | typescript | 1.18 | 2 | 1 | 2026 |
| useCallback | hooks | 1.06 | 2 | 1 | 2025 |
| strict | typescript | 1.00 | 1 | 1 | 2026 |
| useMemo | hooks | 0.88 | 2 | 1 | 2025 |
| DX | patterns | 0.71 | 1 | 1 | 2025 |
| monorepo | tooling | 0.71 | 1 | 1 | 2025 |

## Top Terms per Topic

### Hooks

| Term | Score | Trend | Years |
|------|-------|-------|-------|
| useEffect | 4.07 | activo | 2020–2026 |
| useCallback | 1.06 | activo | 2023–2025 |
| useMemo | 0.88 | activo | 2021–2025 |
| Suspense | 0.75 | declinante | 2022–2024 |
| useState | 0.53 | abandonado | 2021–2021 |

### State Data

| Term | Score | Trend | Years |
|------|-------|-------|-------|
| Zustand | 6.48 | activo | 2021–2026 |
| Redux | 5.74 | activo | 2020–2025 |
| React Query | 5.06 | activo | 2023–2026 |
| SWR | 3.00 | declinante | 2020–2023 |
| TanStack | 2.71 | activo | 2025–2026 |

### Meta Frameworks

| Term | Score | Trend | Years |
|------|-------|-------|-------|
| Next.js | 1.88 | activo | 2020–2026 |
| Gatsby | 0.88 | abandonado | 2020–2020 |
| Astro | 0.71 | declinante | 2023–2023 |
| Remix | 0.71 | declinante | 2023–2023 |
| server components | 0.35 | declinante | 2023–2023 |

### Typescript

| Term | Score | Trend | Years |
|------|-------|-------|-------|
| zod | 4.00 | activo | 2026–2026 |
| any | 1.18 | activo | 2021–2026 |
| strict | 1.00 | activo | 2026–2026 |
| type | 0.12 | abandonado | 2020–2020 |

### Tooling

| Term | Score | Trend | Years |
|------|-------|-------|-------|
| Vite | 3.19 | activo | 2021–2026 |
| monorepo | 0.71 | activo | 2025–2025 |

### Testing

| Term | Score | Trend | Years |
|------|-------|-------|-------|
| Jest | 0.12 | abandonado | 2020–2020 |
| Testing Library | 0.12 | abandonado | 2020–2020 |

### Patterns

| Term | Score | Trend | Years |
|------|-------|-------|-------|
| DX | 0.71 | activo | 2025–2025 |

## Abandoned Terms (no mention in last 4+ years)

| Term | Topic | Last Year | Total Mentions |
|------|-------|-----------|----------------|
| useState | hooks | 2021 | 3 |
| useRef | hooks | 2021 | 1 |
| Gatsby | meta_frameworks | 2020 | 7 |
| useReducer | hooks | 2020 | 4 |
| Recoil | state_data | 2020 | 1 |
| useContext | hooks | 2020 | 1 |
| Jest | testing | 2020 | 1 |
| type | typescript | 2020 | 1 |
| Testing Library | testing | 2020 | 1 |

## Latest Opinion — Top 5 Active Terms

### `Zustand`

**2026 · post #1198**
> Si es algo muy basico context te vale. Si crees que vas a necesitar una gestión de estado local algo mas compleja (99.9% estas haciendo algo mal) entonces zustand. Luego no cometas el error de usar axios o alguna mierda de estas para fetchear, solo necesitas el fetch basico + react query.

### `Redux`

**2025 · post #1085**
> Pero Vite tambien es dios, por comodidad (tienes que hacer el setup the tanstack-router), pues tiro por nextjs. Sobre estado/context normalmente con react-query no necesitas ningúna libreria para gestionar el estado aparte, si aún asi lo necesitas lo mejor es usar la url como source of truth, y si la URL no te vale tampoco entonces ya si te recomiendo zustand, pero ya te digo 99,99% de las veces si estas usando redux/zustand para almacenar estado lo estas haciendo mal. (1.

### `React Query`

**2026 · post #1194**
> No uses Next.js
El stack que yo recomiendo: React  + Vite + TypeScript + TailwindCSS (+shadcdn) + Tanstack Router + React Query. 99.9% es sobre ingenieria, con React Query deberias tener todo cubierto.

### `useEffect`

**2026 · post #1194**
> Nunca any. UseEffect es un code smell, si necesitas/usas un useEffect hay una probabilidad muy alta de que lo estas haciendo mal. Eso no quiere decir que no se deban/tengan que usar.

### `zod`

**2026 · post #1196**
> El "ideal" en un codebase es que Zod sea el source of truth del tipado, y de zod (runtime) generes los tipos (build time). Y el idealmente x2 es que los tipos que generas automaticamente de la api se generen directamente en Zod y de ahi los pasas a TypeScript.

## Dense Technical Posts (Last 30% of Timeline)

| Year | Post # | Page | Words | Has Code | Preview |
|------|--------|------|-------|----------|---------|
| 2025 | #1085 | 37 | 220 |  | No hay stack mas productivo que ese, ademas las LLM lo cagan como churros de oro. Yo nextjs lo uso a… |
| 2025 | #1125 | 38 | 177 |  | no usar tailwind en 2025 es de estar cocido de la cabeza en mi opinión, o mejor dicho, no tener ni i… |
| 2026 | #1194 | 40 | 162 |  | No uses Next.js El stack que yo recomiendo: React  + Vite + TypeScript + TailwindCSS (+shadcdn) + Ta… |
| 2025 | #1119 | 38 | 155 |  | Tailwind >>>>>>>>>>>>>>> (introduce aqui 2 millones mas) >>>>>>> CSS-Modules >>>>> CSS-IN-JS >>>>>>>… |
| 2025 | #1128 | 38 | 148 |  | Mi opinión en 8 años ya de esto es que he tocado todo profesionalmente: CSS a pelo, Bootstrap, CSS-i… |
| 2025 | #1068 | 36 | 135 |  | La razón es simple, tienen la mejor DX, y por ende estan en todos lados, millones y millones de line… |
| 2023 | #870 | 29 | 133 |  | NextJs ahora shippea con dos formas de "routing", ambas file based, pero que la api es muy diferente… |
| 2025 | #1046 | 35 | 124 |  | Yo aún tengo que ver un caso donde no sea sobre-igenieria. Posiblemente vuestras necesidas tecnicas … |
| 2024 | #993 | 34 | 103 |  | Cuando se empieza a extender el va a cambiar un poquito el paradigma. En otro orden de cosas, gracia… |
| 2025 | #1122 | 38 | 40 | ✓ | className -> "buttons-container gap-4" (gap-4 es una clase de css global -> o en el css en la clase … |


---
*Dashboard:* `streamlit run isvidal/app.py`  
*Data:* `isvidal/isvidal_posts.parquet`  
*Thread:* [react-hilo-general](https://www.mediavida.com/foro/dev/react-hilo-general-libreria-para-atraerlos-atarlos-todos-657749)
