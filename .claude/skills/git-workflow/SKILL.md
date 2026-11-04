---
name: git-workflow
description: "Aplica flujos Git profesionales para ramas, commits, revisiones, pull requests, releases y resolución de conflictos. Úsala al preparar cambios, organizar historial o colaborar mediante GitHub."
---

# Git Workflow

## Principios
- Inspecciona `git status`, rama, remotos y diff antes de actuar.
- No sobrescribas cambios locales del usuario.
- No hagas force push, reset destructivo, rebase compartido ni borrado de ramas sin autorización explícita.
- No incluyas secretos, archivos generados o datos sensibles en commits.
- Sigue las convenciones del repositorio.

## Flujo
1. Identifica objetivo y alcance del cambio.
2. Revisa estado y cambios existentes.
3. Propón rama y estrategia coherentes con el equipo.
4. Mantén commits pequeños y descriptivos.
5. Ejecuta pruebas pertinentes antes de proponer commit.
6. Revisa el diff completo y archivos incluidos.
7. Prepara descripción de PR con contexto, cambios, pruebas, riesgos y capturas si aplican.
8. Documenta breaking changes y migraciones.
9. Para releases, verifica versión, changelog, tags y artefactos.

## Mensajes
Usa Conventional Commits solo si el repositorio lo adopta o el usuario lo solicita. No impongas una convención sin revisar.

## Entrega
Resume rama, archivos, commits sugeridos o creados, pruebas y pasos siguientes. No afirmes que se hizo push o merge si no ocurrió.
