# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

## [Unreleased]

## [2.0.0] - 2026-11-21

### Added
- `global/CLAUDE.md`: instrucciones generales condensadas a partir de las instrucciones maestras, para instalar como `~/.claude/CLAUDE.md`.
- `docs/instrucciones-maestras.md`: texto original completo y tabla de destino de cada sección.
- Skill `diagramming`: diagramas editables en draw.io, Mermaid y BPMN 2.0, verificados contra el código.
- Skill `professional-writing`: correos, mensajes y documentos en español claro y natural.
- `project-planning/references/evaluacion-integral.md` y `technical-documentation/references/documentacion-por-publico.md`.
- `scripts/instalar.py`: instalación con simulación previa, respaldo, sincronización por manifiesto y fusión de ajustes.
- `global/ajustes.json`: presupuesto del listado de Skills y desactivación de Skills duplicadas de plugins.
- Casos de activación para las dos Skills nuevas.

### Changed
- Se incorporó a `code-review`, `debugging`, `testing-strategy`, `technical-debt-management`, `software-architecture`, `incident-response`, `release-management`, `technical-documentation` y `web-accessibility` lo que aportaban sus equivalentes de los plugins `engineering` y `design`, que quedan desactivados mediante `skillOverrides`.
- `aws-cloud-engineering` se centra en el diseño transversal y remite a las Skills oficiales de AWS por servicio.
- `skill-creator` distingue las comprobaciones del repositorio de las que sirven en cualquier proyecto.
- `CLAUDE.md` del repositorio queda solo con reglas propias; las generales pasan a `global/CLAUDE.md`.
- README actualizado: instalación con el script, presupuesto del listado y restauración.

## [1.0.0] - 2026-11-04

### Added
- 59 Skills en 7 especialidades, con fuentes, validador estructural y prueba de activación.
