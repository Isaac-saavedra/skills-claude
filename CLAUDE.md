# Reglas para trabajar en este repositorio

Las reglas generales de comportamiento están en `global/CLAUDE.md` (se instala como `~/.claude/CLAUDE.md`). Aquí solo lo propio de este repositorio.

## Estructura
- Skills planas en `.claude/skills/<skill>/`: Claude Code no detecta subcarpetas por especialidad. La organización por especialidad vive en `docs/CATALOG.md`.
- `global/` contiene lo que se instala en `~/.claude`: `CLAUDE.md` y `ajustes.json`.
- `docs/instrucciones-maestras.md` guarda el texto original de las instrucciones y dónde quedó cada sección. Si cambias `global/CLAUDE.md` o una Skill que recibió una sección, actualiza esa tabla.

## Al crear o modificar una Skill
- Frontmatter con `name` igual a la carpeta y `description` que diga qué hace y cuándo usarla ("Usar…"), lo clave al principio porque el listado puede recortarla.
- Secciones obligatorias: Alcance (con "No cubre" y la Skill que sí lo cubre), Verificación, Ejemplo y Fuentes.
- `references/sources.md` con al menos una fuente leída de verdad. "Leída" solo si se abrió y se leyó; si no, "Localizada".
- Nada de datos de proyectos reales, nombres de personas ni secretos: el repositorio es público.
- Actualiza `docs/CATALOG.md`, añade un caso en `tests/trigger_cases.json` y registra el cambio en `CHANGELOG.md`.

## Comprobaciones
- `python3 scripts/validate_skills.py` debe terminar sin errores antes de cada commit.
- `claude plugin validate .claude/skills` cuando cambie la estructura.
- `python3 scripts/test_triggers.py` consume uso de la cuenta: córrelo solo cuando haga falta medir la activación, y reporta el resultado real.
- Instala con `python3 scripts/instalar.py` (simulación) y `--aplicar`; nunca copies a mano sobre `~/.claude/skills`.
