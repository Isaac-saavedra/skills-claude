# Claude Software Engineering Skills

Colección de Skills personalizadas para apoyar el ciclo de vida del desarrollo de software con Claude y Claude Code.

## Incluye

- `software-architecture` — Diseña y evalúa arquitecturas de software, límites de módulos, patrones, decisiones técnicas y diagramas. Úsala al iniciar un sistema, dividir un monolito, evaluar escalabilidad o documentar decisiones de arquitectura.
- `fullstack-development` — Implementa y mantiene aplicaciones web full stack, desde la interfaz hasta backend, persistencia, autenticación e integración. Úsala al crear funcionalidades, aplicaciones completas o modificar proyectos existentes.
- `frontend-design` — Diseña e implementa interfaces web modernas, accesibles y responsive con componentes reutilizables. Úsala para crear páginas, dashboards, formularios, prototipos o mejorar la experiencia visual de una aplicación.
- `backend-engineering` — Desarrolla servicios backend robustos, mantenibles y seguros, incluyendo lógica de negocio, autenticación, autorización, colas y procesos asíncronos. Úsala al crear o modificar servicios del lado servidor.
- `api-engineering` — Diseña, implementa, documenta y valida APIs HTTP/REST y sus contratos, incluyendo autenticación, versionado, errores y OpenAPI. Úsala al crear endpoints, integrar servicios o revisar APIs existentes.
- `database-engineering` — Diseña, consulta, migra y optimiza bases de datos relacionales y NoSQL. Úsala al modelar esquemas, escribir SQL, revisar índices, planificar migraciones o diagnosticar problemas de persistencia.
- `code-review` — Realiza revisiones de código enfocadas en defectos, seguridad, regresiones, mantenibilidad y rendimiento. Úsala para revisar cambios, pull requests, diffs o módulos antes de integrarlos.
- `debugging` — Diagnostica errores de software mediante síntomas, logs, trazas, reproducción y análisis de causa raíz. Úsala cuando una aplicación falle, presente resultados inesperados o tenga errores intermitentes.
- `qa-automation` — Planifica y automatiza pruebas unitarias, integración, API y end-to-end, incluyendo Playwright cuando corresponda. Úsala para validar funcionalidades, prevenir regresiones y preparar entregas.
- `application-security` — Evalúa y mejora la seguridad de aplicaciones, código, APIs y configuraciones siguiendo prácticas OWASP y mínimo privilegio. Úsala para threat modeling, revisión de vulnerabilidades o hardening defensivo.
- `aws-cloud-engineering` — Diseña, implementa y revisa soluciones AWS con foco en arquitectura, IAM, redes, cómputo, almacenamiento, monitoreo, costos y seguridad. Úsala para proyectos o incidentes sobre servicios AWS.
- `devops-engineering` — Automatiza construcción, integración, entrega, despliegue, contenedores e infraestructura como código. Úsala para Docker, CI/CD, GitHub Actions, Linux, observabilidad y operaciones.
- `technical-documentation` — Crea y mantiene documentación técnica profesional, clara y verificable para software, APIs, infraestructura y operaciones. Úsala para README, manuales, especificaciones, ADR, runbooks, informes y documentación de usuario.
- `git-workflow` — Aplica flujos Git profesionales para ramas, commits, revisiones, pull requests, releases y resolución de conflictos. Úsala al preparar cambios, organizar historial o colaborar mediante GitHub.
- `performance-optimization` — Investiga y optimiza rendimiento de aplicaciones, APIs, consultas y frontend mediante mediciones y perfiles. Úsala ante lentitud, alto consumo de CPU/memoria, latencia o costos de ejecución.
- `skill-creator` — Diseña, crea, valida y mejora Skills reutilizables para Claude siguiendo el formato Agent Skills. Úsala cuando quieras convertir procesos, estándares o conocimientos en una Skill mantenible.

## Estructura

Las Skills para Claude Code se encuentran en `.claude/skills/<skill-name>/SKILL.md`.

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

## Subir Skills a Claude Web

Usa el ZIP `claude-web-skills.zip` incluido en la distribución descargable de este proyecto. Ese ZIP contiene las carpetas de Skills en su raíz para facilitar la carga como Skills personalizadas.

La disponibilidad de carga depende del plan y las capacidades habilitadas en Claude. Consulta la documentación oficial vigente.

## Validación

Ejecuta:

```bash
python3 scripts/validate_skills.py
```

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
