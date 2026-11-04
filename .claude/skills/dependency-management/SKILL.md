---
name: dependency-management
description: "Audita, actualiza y fija dependencias: vulnerabilidades, lockfiles, SemVer, licencias y actualizaciones automáticas. Usar con npm audit, pip-audit, Dependabot o librerías obsoletas."
---

# Dependency Management

## Alcance
Dependencias de terceros en un proyecto. No cubre:
- Versiones del propio producto: `release-management`.
- Actualizar el runtime o una migración grande: `migration-engineering`.

## Procedimiento
1. Identifica manifiestos, lockfiles y gestor. Si falta el lockfile, señálalo como riesgo.
2. Audita con la herramienta del ecosistema, por ejemplo `npm audit` o `pip-audit`. Revisa lo que realmente es alcanzable por el código y contrasta el aviso de seguridad.
3. Clasifica por severidad y exposición:
   - Crítica: de inmediato.
   - Alta: lo antes posible.
   - Moderada: cuando haya tiempo.
   - Baja: a criterio.
4. Actualiza primero parches, luego menores y por separado las mayores, cada una con su guía de migración.
5. Haz un cambio pequeño y ejecuta pruebas por tanda.
6. Verifica un paquete nuevo antes de añadirlo: existencia, nombre exacto, mantenimiento, licencia y publicación reciente.
7. Automatiza con Dependabot o equivalente, con PR revisables e integrados en CI.
8. Instala de forma reproducible en CI: `npm ci`.

## Reglas
- No ejecutes `npm audit fix --force` sin revisar: instala actualizaciones mayores de dependencias directas. Prueba antes con `npm audit fix --dry-run`.
- `pip-audit` y escáneres similares no detectan paquetes maliciosos ni analizan tu código.
- SemVer es una promesa de quien publica, no una garantía: ejecuta pruebas.
- No afirmes "sin vulnerabilidades"; indica herramienta, fecha y resultado.
- La compatibilidad de licencias requiere revisión legal si hay dudas.

## Verificación
Lockfile actualizado, instalación limpia, pruebas ejecutadas y nueva auditoría con su resultado real.

## Entrega
Hallazgos, cambios por paquete (versión antes y después), riesgos aceptados, pruebas y automatización.

## Ejemplo
Aviso crítico en una librería de análisis de XML usada en una ruta pública: se actualiza el parche, se ejecutan pruebas y se repite la auditoría. Un aviso moderado en una herramienta solo de desarrollo se documenta y se programa.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
