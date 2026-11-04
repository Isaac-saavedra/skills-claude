---
name: migration-engineering
description: "Planifica y ejecuta migraciones de datos, aplicaciones, nube y versiones por fases, con reversión y validación. Usar al mover sistemas, actualizar plataformas o cambiar bases de datos."
---

# Migration Engineering

## Alcance
Traslados entre versiones, plataformas o sistemas. No cubre:
- Migraciones de esquema rutinarias: `database-engineering`.
- Comprender el sistema de origen: `legacy-code-analysis`.

## Procedimiento
1. Define motivo, alcance, criterio de éxito, tiempo de inactividad permitido y responsable de la decisión.
2. Inventaría aplicaciones, datos, volúmenes, integraciones, credenciales y dependencias.
3. Elige estrategia. En la nube, las 7 R: Retire, Retain, Rehost, Relocate, Repurchase, Replatform y Refactor. En migraciones grandes, AWS recomienda evitar refactorizar durante el traslado y modernizar después.
4. Reduce riesgo con entrega incremental:
   - **Estrangulamiento**: sustituye comportamiento poco a poco.
   - **Cambio paralelo**: expandir, migrar y contraer para esquemas e interfaces.
5. Diseña migración de datos: mapeo, transformación, idempotencia, reanudación, validación y delta final.
6. Escribe el plan de corte: pasos, responsables, tiempos y punto de no retorno.
7. Escribe y **prueba** la reversión.
8. Ensaya con un volumen realista en un entorno aislado y mide duración.
9. Tras el corte, compara, monitoriza y retira lo antiguo solo tras un periodo acordado.

## Reglas
- No ejecutes la migración real sin autorización explícita y copia de seguridad restaurable comprobada.
- No borres el origen como parte del corte.
- No uses datos personales reales en pruebas sin autorización.
- No prometas tiempos sin un ensayo: márcalos como estimación.

## Verificación
Conteos y sumas de control por tabla o entidad, muestras de negocio, pruebas funcionales, reversión ensayada y métricas posteriores.

## Entrega
Inventario, estrategia, runbook de corte, reversión, resultados del ensayo, validación y riesgos.

## Ejemplo
Renombrar una columna sin tiempo de inactividad:
1. **Expandir**: añadir `email_nuevo` y escribir en ambas.
2. **Migrar**: rellenar por lotes y cambiar lecturas.
3. **Contraer**: eliminar `email` tras un periodo sin uso.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
