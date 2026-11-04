---
name: technical-debt-management
description: "Identifica, clasifica y prioriza deuda técnica según su coste real y frecuencia de cambio, y crea un plan de reducción. Usar al decidir qué limpiar o justificar esa inversión."
---

# Technical Debt Management

## Alcance
Decide qué deuda pagar, cuándo y por qué. No cubre:
- Ejecutar la limpieza: `refactoring`.
- Calidad automatizada: `code-quality`.
- Dependencias obsoletas en detalle: `dependency-management`.

## Procedimiento
1. Reúne candidatos con evidencia: incidentes, tiempos de cambio, zonas temidas, pruebas lentas o inestables y `TODO` antiguos.
2. Cruza con frecuencia de cambio. Lista archivos más modificados:
   `git log --since="12 months ago" --name-only --pretty=format: | grep -v '^$' | sort | uniq -c | sort -rn | head -30`
3. Describe cada elemento en dos partes: principal (coste de corregirlo) e interés (coste extra por cada cambio).
4. Clasifícalo por origen: deliberada o inadvertida, prudente o imprudente.
5. Puntúa con: interés, frecuencia de cambio, riesgo y esfuerzo. Usa escalas relativas y marca las estimaciones como tales.
6. Decide: pagar ahora, pagar al tocar la zona, aceptar con fecha de revisión o eliminar la funcionalidad.
7. Crea tareas con resultado medible y dueño.
8. Mide el efecto con las métricas DORA disponibles u otros indicadores del proyecto.

## Reglas
- No todo código feo es deuda relevante: si casi no se toca, su interés es bajo y puede quedarse como está.
- No inventes horas ni costes económicos; si los datos no existen, usa rangos relativos y dilo.
- Comunica a negocio en coste de cambio y riesgo, no en pureza técnica.

## Verificación
Cada elemento priorizado tiene evidencia; las estimaciones están marcadas; las tareas tienen criterio de finalización comprobable.

## Entrega
Registro de deuda, puntuación, decisión, plan por trimestres o iteraciones y métricas de seguimiento.

## Ejemplo
| Elemento | Interés | Cambios en 12 meses | Decisión |
|---|---|---|---|
| Módulo de facturación sin pruebas | Alto | 84 | Pagar ahora |
| Informe antiguo con código duplicado | Bajo | 1 | Aceptar y revisar en 6 meses |

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
