# Claude Software Engineering Skills

Colección de Skills personalizadas para apoyar el ciclo de vida del desarrollo de software con Claude y Claude Code.

## Incluye

59 Skills en 7 especialidades. La lista completa, con su función y el número de fuentes, está en [docs/CATALOG.md](docs/CATALOG.md).

| Especialidad | Skills |
|---|---|
| Software Engineering | 9 |
| Development | 16 |
| Quality Assurance | 4 |
| Security | 8 |
| Cloud & Infrastructure | 7 |
| Documentation | 7 |
| Operations & Management | 8 |

## Estructura

```text
.claude/
  settings.json                  # amplía el presupuesto del listado de Skills
  skills/<skill>/
    SKILL.md                     # instrucciones
    references/sources.md        # fuentes y estado de verificación
docs/CATALOG.md                  # organización por especialidades
scripts/validate_skills.py       # validación estructural
scripts/test_triggers.py         # prueba de activación
tests/trigger_cases.json         # casos de activación
```

Las carpetas son planas a propósito: Claude Code busca `.claude/skills/<skill>/SKILL.md`, por lo que una subcarpeta por especialidad haría que no se detectaran.

## Instalación en Claude Code

### Instalación personal (todos tus proyectos)

Copia las carpetas de Skills a:

```bash
mkdir -p ~/.claude/skills
cp -r .claude/skills/* ~/.claude/skills/
```

### Instalación por proyecto

Copia `.claude/skills/` a la raíz del proyecto donde quieras que estén disponibles y versionadas.

## Actualizar desde Git

Si ya clonaste este repositorio:

```bash
cd ruta/al/repositorio
git pull
cp -r .claude/skills/* ~/.claude/skills/
```

La copia no elimina Skills locales que hayas quitado del repositorio. Revisa manualmente antes de borrar.

## Presupuesto del listado de Skills

Claude Code carga nombres y descripciones de todas las Skills, con un presupuesto del 1 % de la ventana de contexto. Si se supera, recorta las descripciones de las Skills menos usadas y Claude puede dejar de reconocerlas.

Con 59 Skills, este repositorio incluye `.claude/settings.json` con `skillListingBudgetFraction: 0.02` (2 %). En una instalación personal, añade esa misma clave a `~/.claude/settings.json`, sin sustituir lo que ya tengas. Usa `/doctor` para ver el coste estimado y `/skill-doctor` para detectar Skills que no usas. Instala solo las que necesites si quieres ahorrar contexto.

## Subir Skills a Claude Web

Comprime cada carpeta de Skill por separado y súbela como Skill personalizada. La disponibilidad depende del plan y las capacidades habilitadas: consulta la documentación oficial vigente.

## Validación

Ejecuta:

```bash
python3 scripts/validate_skills.py          # estructura, metadatos, fuentes y catálogo
claude plugin validate .claude/skills       # requiere Claude Code 2.1.233 o posterior
python3 scripts/test_triggers.py            # activación real; consume uso de tu cuenta
```

## Verificación de la información

Cada Skill tiene `references/sources.md`, con la fecha de revisión y dos estados:

- **Leída**: se consultó el contenido para respaldar lo indicado.
- **Localizada**: la URL oficial se encontró, pero no se leyó su contenido.

Versiones, normas y servicios cambian. Las Skills indican consultar la fuente vigente en lugar de fijar versiones actuales. Revisa las fuentes periódicamente y actualiza la fecha.

## Principios

- No inventar datos, resultados, versiones ni verificaciones.
- Inspeccionar el proyecto antes de modificarlo.
- Priorizar cambios mínimos, seguros y reversibles.
- Ejecutar pruebas y reportar resultados reales.
- Mantener documentación alineada con el comportamiento implementado.
- Solicitar autorización antes de acciones destructivas o cambios productivos.

## Compatibilidad

Estas Skills siguen la estructura de Agent Skills basada en `SKILL.md` y YAML frontmatter. La detección y disponibilidad pueden variar según el producto, versión y entorno de ejecución. Validar en cada entorno objetivo.

## Licencia

MIT. Revisa si esta licencia es adecuada antes de redistribuir o incorporar contenido de terceros.
