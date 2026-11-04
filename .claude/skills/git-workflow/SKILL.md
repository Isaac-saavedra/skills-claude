---
name: git-workflow
description: "Aplica flujos Git profesionales: ramas, commits, pull requests, historiales divergentes y conflictos. Usar siempre ante errores de git pull, merge, rebase o push, incluso si la respuesta parece simple."
---

# Git Workflow

## Alcance
**No cubre:** Numerar y publicar versiones: `release-management`. Pipelines: `cicd-engineering`.

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

## Verificación
Comprueba `git status`, `git log --oneline --graph -10` y el diff antes de un push. Confirma que no se incluyeron secretos y que las pruebas se ejecutaron.

## Ejemplo
`fatal: Need to specify how to reconcile divergent branches`: revisa ambas historias con `git log --oneline --graph --all -20`. Con `git pull --no-rebase` fusionas; `--rebase` reescribe tus commits locales. Sin `--force` ni borrados sin autorización.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
