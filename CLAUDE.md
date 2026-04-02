# CLAUDE.md — Reglas locales del proyecto scrapper

## Recuperación tras compactación de contexto

Cuando el contexto se compacte o empiece una nueva sesión, ANTES de cualquier acción:

1. Leer `roadmap.md` — identifica la fase actual, qué está hecho, qué sigue
2. Ejecutar `git log --oneline -20` — muestra los últimos checkpoints y cambios
3. Continuar desde donde se quedó, sin preguntar al usuario

## Protocolo de commits

Hacer commits granulares en cada checkpoint significativo:
- Al guardar resultados de cualquier plataforma (parciales o finales)
- Al actualizar `roadmap.md`
- Al crear o modificar cualquier script
- Al generar archivos de output (`.json`, `.csv`, `.txt`)

Formato: Conventional Commits — `type(scope): resumen imperativo`
Tipos: `feat|fix|data|docs|chore`
Siempre listar archivos explícitos — nunca `git add .`

## Protocolo de roadmap

`roadmap.md` es la fuente de verdad del progreso.
Actualizarlo inmediatamente al:
- Iniciar una nueva fase (marcar como 🔄 en progreso)
- Completar una plataforma (marcar como ✅)
- Encontrar un bloqueo o cambiar estrategia
- Terminar la sesión (dejar el estado exacto para la siguiente)

## Protocolo de loop autónomo

Este proyecto corre en modo autónomo. Seguir este ciclo:
1. Leer roadmap.md → identificar próxima plataforma pendiente
2. Scrape la plataforma (Instagram → Twitch → YouTube, en ese orden)
3. Guardar resultados en archivos de output
4. Actualizar roadmap.md
5. Commit granular con los archivos nuevos
6. Continuar con la siguiente plataforma
7. Al terminar las 3, generar `cs2_creators_combined_20k_100k.*`
