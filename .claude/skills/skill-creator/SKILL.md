---
name: skill-creator
description: "Diseña, crea, valida y mejora Skills reutilizables para Claude siguiendo el formato Agent Skills. Úsala cuando quieras convertir procesos, estándares o conocimientos en una Skill mantenible."
---

# Skill Creator

## Alcance
**No cubre:** Solo el contenido de esta biblioteca: el formato y límites se comprueban en la documentación oficial vigente.

## Objetivo
Crear Skills enfocadas, detectables y verificables. Una Skill debe enseñar un flujo de trabajo repetible, no ser una colección vaga de consejos.

## Estructura mínima
Cada Skill debe vivir en una carpeta con `SKILL.md` y comenzar con YAML frontmatter:
- `name`: minúsculas, números y guiones; máximo 64 caracteres.
- `description`: qué hace y cuándo debe activarse; clara y específica.
No uses nombres reservados ni XML en los metadatos.

## Proceso
1. Identifica la tarea repetible, usuario objetivo y señales de activación.
2. Define qué queda dentro y fuera del alcance.
3. Escribe una descripción concreta que permita a Claude decidir cuándo invocarla.
4. Crea instrucciones paso a paso, reglas de seguridad, criterios de calidad y formato de salida.
5. Añade ejemplos de solicitudes y resultados esperados.
6. Mueve información extensa o específica a `references/` y plantillas a `assets/`.
7. Añade scripts solo si automatizan una validación útil; documenta dependencias y uso.
8. Evita duplicar instrucciones globales y otras Skills.
9. Valida YAML, nombre de carpeta, enlaces relativos y rutas.
10. Prueba la Skill con casos positivos, negativos y ambiguos.

## Calidad
- Debe ser autónoma y fácil de mantener.
- Debe especificar qué hacer cuando falte información.
- No debe instruir a inventar hechos ni saltarse permisos.
- Debe distinguir acciones que requieren confirmación.
- No debe contener secretos ni código peligroso.
- La descripción debe incluir disparadores de uso claros.

## Entrega
Incluye carpeta, SKILL.md, referencias/plantillas necesarias, ejemplos de activación y resultado de validación. No afirmes compatibilidad universal sin probar los entornos objetivo.

## Verificación
Ejecuta `python3 scripts/validate_skills.py` y, en Claude Code 2.1.233 o posterior, `claude plugin validate .claude/skills`. Prueba la activación con `python3 scripts/test_triggers.py`.

## Ejemplo
Descripción: "Audita dependencias con npm audit y pip-audit. Usar con paquetes vulnerables u obsoletos". Tercera persona, qué hace y cuándo usarla, con lo clave al principio porque el listado puede recortarla.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
