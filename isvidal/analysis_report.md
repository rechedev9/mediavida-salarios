# isvidal — Idea Evolution Analysis Report

## Temporal Summary

| Year | Posts | Words | Code% |
|------|-------|-------|-------|
| 2020 | 86 | 5211 | 5% |
| 2021 | 46 | 2023 | 0% |
| 2022 | 8 | 125 | 0% |
| 2023 | 27 | 581 | 0% |
| 2024 | 4 | 139 | 0% |
| 2025 | 23 | 1236 | 4% |
| 2026 | 5 | 359 | 0% |

## Top Terms per Topic (Recency-Weighted)

### Hooks

| Term | Weighted Score | Total Mentions | Years |
|------|----------------|----------------|-------|
| useEffect | 21.1 | 13 | 2020–2026 |
| useReducer | 5.0 | 4 | 2020–2020 |
| useState | 4.6 | 3 | 2021–2021 |
| useCallback | 3.6 | 2 | 2023–2025 |
| Suspense | 3.5 | 2 | 2022–2024 |

### State Data

| Term | Weighted Score | Total Mentions | Years |
|------|----------------|----------------|-------|
| Redux | 39.4 | 28 | 2020–2025 |
| SWR | 20.9 | 15 | 2020–2023 |
| Zustand | 20.5 | 11 | 2021–2026 |
| React Query | 11.7 | 6 | 2023–2026 |
| TanStack | 5.9 | 3 | 2025–2026 |

### Meta Frameworks

| Term | Weighted Score | Total Mentions | Years |
|------|----------------|----------------|-------|
| Gatsby | 7.8 | 7 | 2020–2020 |
| Next.js | 7.4 | 5 | 2020–2026 |
| Astro | 3.6 | 2 | 2023–2023 |
| Remix | 3.6 | 2 | 2023–2023 |
| server components | 1.8 | 1 | 2023–2023 |

### Typescript

| Term | Weighted Score | Total Mentions | Years |
|------|----------------|----------------|-------|
| zod | 8.0 | 4 | 2026–2026 |
| any | 3.5 | 2 | 2021–2026 |
| strict | 2.0 | 1 | 2026–2026 |
| type | 1.3 | 1 | 2020–2020 |

### Tooling

| Term | Weighted Score | Total Mentions | Years |
|------|----------------|----------------|-------|
| Vite | 10.8 | 6 | 2021–2026 |
| monorepo | 1.9 | 1 | 2025–2025 |

### Testing

| Term | Weighted Score | Total Mentions | Years |
|------|----------------|----------------|-------|
| Jest | 1.0 | 1 | 2020–2020 |
| Testing Library | 1.0 | 1 | 2020–2020 |

### Patterns

| Term | Weighted Score | Total Mentions | Years |
|------|----------------|----------------|-------|
| DX | 1.9 | 1 | 2025–2025 |

## Opinion Evolution — Top 5 Terms

### `Redux`

**2025 · post #1085**
> Pero Vite tambien es dios, por comodidad (tienes que hacer el setup the tanstack-router), pues tiro por nextjs. Sobre estado/context normalmente con react-query no necesitas ningúna libreria para gestionar el estado aparte, si aún asi lo necesitas lo mejor es usar la url como source of truth, y si la URL no te vale tampoco entonces ya si te recomiendo zustand, pero ya te digo 99,99% de las veces si estas usando redux/zustand para almacenar estado lo estas haciendo mal. (1.

**2023 · post #827**
> Usar redux es mala practica cuando tienes Zustand que le da mil patadas. Pero vamos, si tienes que compartir estado entre componentes que estan separados por mil componente intermedios, pues ya puedes pensar todo lo duro que quieras, que no queda otra que user alguna solucion de state management, eso a prop drilling a muerte.

**2023 · post #827**
> Pero vamos, si tienes que compartir estado entre componentes que estan separados por mil componente intermedios, pues ya puedes pensar todo lo duro que quieras, que no queda otra que user alguna solucion de state management, eso a prop drilling a muerte. Eso si, redux a pelo da asco, redux toolkit se salva ya, pero vamos, zustander a muerte.

**2023 · post #847**
> Me cuesta verle el beneficio para cosas simples vs Zustand por ejemplo. Asi que si, para el 99% de casos no recomendaria redux, ni redux-toolkit, porque zustand te va a hacer lo mismo en muchas menos lineas.

**2021 · post #512**
> Listado => [items, setItems] = useState([])
ElementoDelListado setItems={setItems}
Entonces en ElementoDelListado simplemente haces el setItems(i => [...i, item])
Y en el padre (Listado) puedes hacer lo que quieras pues es donde tienes el hook. No se si me he explicado, eso en un caso super simple claro, si entre el listado y los elementos hay 20 cosas por medio, o estos elementos tambien afectan a otras cosas en la otra punta de la app, pues ahi si que ya lo mejor es tirar de context o redux

### `useEffect`

**2026 · post #1194**
> Nunca any. UseEffect es un code smell, si necesitas/usas un useEffect hay una probabilidad muy alta de que lo estas haciendo mal. Eso no quiere decir que no se deban/tengan que usar.

**2023 · post #799**
> useEffect(() => {
console.log(getAll())
}
Mira a ver que te esta devolviendo este getAll, que no sera una promesa, de ahi el undefined del then.

**2021 · post #649**
> Evidentemente esto no es una regla de oro (Y puedes ahorrarte el get), y hay mil casos particulares, pero normalmente suele ser raro tener posts en useEffects. Osea, lo que quiero decir, es que "normalmente" primeros harias el post (Mediante onSubmit, onClick) y si este es 200 entonces es cuando actualizas redux, de tal forma que nunca necesitarias un useEffect. Hay casos especiales, ejemplo, logging de eventos y cosas asi, que si que tienen sentido un post en un useEffect o en un listener.

**2021 · post #649**
> Osea, lo que quiero decir, es que "normalmente" primeros harias el post (Mediante onSubmit, onClick) y si este es 200 entonces es cuando actualizas redux, de tal forma que nunca necesitarias un useEffect. Hay casos especiales, ejemplo, logging de eventos y cosas asi, que si que tienen sentido un post en un useEffect o en un listener.

**2021 · post #651**
> Un useEffect sin dependencias (segundo parametro) se lanzara despues de cada ciclo de re-renderizado . Un useEffect con dependencias vacias (array vacio) solo se lanzara la primera vez que se renderiza el componente.

### `SWR`

**2023 · post #792**
> Y no entiendo porque useCallback deberia ser solucion de esto. En cualquier caso, porfavor, olvidate de todo esto (context etc...) y empieza a usar react-query o swr, yo soy mas de swr pero ya cada uno.

**2023 · post #829**
> Menos con cositas como swr o react-query para fetchear, que ya te abstraen ellos el manejar esas cositas.

**2023 · post #872**
> Uses nextjs o no, cosas como tailwind, react query o swr, date-fns, clsx y cualquier otra mierda que se te ocurra vas a tenir que seguir instalandolas con yarn, de esa es imposible salvarte. Pero vamos, yarn add clsx y luego importas, friccion y pain poco
te recuerdo que react es una libreria que basicamente lo unico que tiene son unos helpers para manipular el dom de forma mas developer friendly

**2021 · post #603**
> Los de Redux han sacado una api para el fetcheo de data, substituto de react-query o SWR. Cuanto menos interesante, y bastante nuevo, o al menos yo no lo conocia:
RTK-QUERY

**2021 · post #640**
> Han sacado la version 1.0.0 de SWR:
https://swr.vercel.app/blog/swr-v1
Mejor hook de data fetching del ecosistema de React, discutidmelo

### `Zustand`

**2026 · post #1198**
> Si es algo muy basico context te vale. Si crees que vas a necesitar una gestión de estado local algo mas compleja (99.9% estas haciendo algo mal) entonces zustand. Luego no cometas el error de usar axios o alguna mierda de estas para fetchear, solo necesitas el fetch basico + react query.

**2025 · post #1085**
> Pero Vite tambien es dios, por comodidad (tienes que hacer el setup the tanstack-router), pues tiro por nextjs. Sobre estado/context normalmente con react-query no necesitas ningúna libreria para gestionar el estado aparte, si aún asi lo necesitas lo mejor es usar la url como source of truth, y si la URL no te vale tampoco entonces ya si te recomiendo zustand, pero ya te digo 99,99% de las veces si estas usando redux/zustand para almacenar estado lo estas haciendo mal. (1.

**2025 · post #1085**
> url, 4. url, 5 ya usa zustand (o react context)). Sobre memoización pues a no ser que te piques un figma o algo muy muy pesado te suda la polla y no deberias usar ni useCallback ni useMemo, y tampoco .memo().

**2025 · post #1089**
> Sobre estado local pues ahi ya depende del caso particular, si no esta en la db/api y no puede estar en la url, pues no te queda mas que state management, mi pick suele ser zustand. Pero es muy muy edge case, normalmente no necesitas estado inherente al cliente, ejemplo auth/user, puedes pensar que state managment no?

**2025 · post #1134**
> Nuqs y la url, olvidate de zustand

### `React Query`

**2026 · post #1194**
> No uses Next.js
El stack que yo recomiendo: React  + Vite + TypeScript + TailwindCSS (+shadcdn) + Tanstack Router + React Query. 99.9% es sobre ingenieria, con React Query deberias tener todo cubierto.

**2026 · post #1194**
> No uses Next.js
El stack que yo recomiendo: React  + Vite + TypeScript + TailwindCSS (+shadcdn) + Tanstack Router + React Query. 99.9% es sobre ingenieria, con React Query deberias tener todo cubierto. React Query.

**2026 · post #1194**
> 99.9% es sobre ingenieria, con React Query deberias tener todo cubierto. React Query. Es correcto.

**2026 · post #1198**
> Si crees que vas a necesitar una gestión de estado local algo mas compleja (99.9% estas haciendo algo mal) entonces zustand. Luego no cometas el error de usar axios o alguna mierda de estas para fetchear, solo necesitas el fetch basico + react query.

**2025 · post #1089**
> Pero es muy muy edge case, normalmente no necesitas estado inherente al cliente, ejemplo auth/user, puedes pensar que state managment no? Pero realmente es puro react query -> ‘/api/me’ y vas reusando esa query key cuando necesitas el usuario o validar el rol.

## Top Posts (Last 30% of Timeline)

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
