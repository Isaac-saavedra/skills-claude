# Contribuir

1. Crea una rama para el cambio.
2. Mantén cada Skill enfocada en una tarea clara y sin duplicar otra: si se solapa, define el límite en "No cubre".
3. Actualiza `SKILL.md`, `references/sources.md` y `docs/CATALOG.md`. Incluye las secciones Alcance, Verificación, Ejemplo y Fuentes.
4. Comprueba el frontmatter, nombre y descripción.
5. Añade ejemplos que reflejen casos reales sin datos sensibles ni nombres de personas o proyectos reales.
6. Ejecuta `python3 scripts/validate_skills.py` y añade un caso en `tests/trigger_cases.json`.
7. Registra el cambio en `CHANGELOG.md`.
8. Describe el cambio, motivación, pruebas y limitaciones en el pull request.

Las reglas detalladas para trabajar en el repositorio están en `CLAUDE.md`. No incluyas secretos, datos personales ni instrucciones para acciones no autorizadas.
