---
name: release-management
description: "Gestiona versiones del producto: SemVer, changelog, notas de versión, etiquetas, ramas y coordinación de lanzamientos. Usar al preparar una versión o decidir su número."
---

# Release Management

## Alcance
Cómo se versiona y publica. No cubre:
- Flujo diario de Git: `git-workflow`.
- Pipeline: `cicd-engineering`.
- Procedimiento paso a paso de despliegue: `deployment-documentation`.

## Procedimiento
1. Confirma el esquema de versiones del proyecto y lo que se considera su API pública.
2. Lista los cambios desde la última etiqueta: `git log <ultima-etiqueta>..HEAD --oneline`.
3. Determina el número (SemVer): incompatible → MAJOR; nueva función compatible → MINOR; corrección → PATCH.
4. Si se usan Conventional Commits: `fix` → PATCH, `feat` → MINOR y `BREAKING CHANGE` o `!` → MAJOR.
5. Actualiza el changelog con enfoque en personas. Tipos: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed` y `Security`. Mantén `Unreleased` arriba.
6. Revisa criterios de salida: pruebas, seguridad, migraciones, documentación y plan de reversión.
7. Etiqueta el commit exacto y publica el artefacto ya probado.
8. Comunica cambios incompatibles con guía de migración y plazos de retirada.
9. Observa tras publicar. Corrige hacia delante o revierte según lo acordado.

## Reglas
- Etiquetar, publicar o enviar a producción requiere autorización explícita.
- No muevas ni borres etiquetas publicadas sin autorización.
- No conviertas el registro de commits directamente en changelog: agrupa y redacta.
- Las notas automáticas de GitHub (`.github/release.yml`) son un punto de partida.

## Verificación
El número refleja los cambios reales, el artefacto corresponde a la etiqueta, los enlaces del changelog funcionan y la instalación de la versión se ha probado.

## Entrega
Número y justificación, changelog, notas, lista de comprobación, plan de reversión y estado de cada paso.

## Ejemplo
```markdown
## [Unreleased]

## [2.1.0] - 2026-11-04
### Added
- Exportación de facturas a CSV.
### Fixed
- Cálculo de redondeo en descuentos.
```

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
