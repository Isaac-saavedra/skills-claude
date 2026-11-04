---
name: performance-optimization
description: "Investiga y optimiza rendimiento de aplicaciones, APIs, consultas y frontend mediante mediciones y perfiles. Úsala ante lentitud, alto consumo de CPU/memoria, latencia o costos de ejecución."
---

# Performance Optimization

## Alcance
**No cubre:** Bloqueos del event loop en Node: `nodejs-engineering`. Objetivos de fiabilidad: `reliability-engineering`. Telemetría nueva: `observability-engineering`.

## Regla principal
Mide antes de optimizar. No declares una mejora sin una comparación válida.

## Proceso
1. Define síntoma, métrica, objetivo, entorno y carga.
2. Obtén una línea base reproducible.
3. Perfila CPU, memoria, I/O, red, consultas y renderizado según el caso.
4. Identifica el cuello de botella con evidencia.
5. Formula cambios pequeños y medibles.
6. Evalúa efectos secundarios, complejidad y costo.
7. Repite mediciones bajo condiciones comparables.
8. Añade pruebas o monitoreo para prevenir regresiones.

## Áreas
- Frontend: bundle, renderizados, imágenes, caché, carga y Core Web Vitals si se miden.
- Backend: latencia, concurrencia, pooling, colas, serialización y dependencias.
- Base de datos: planes, índices, N+1, bloqueos y cardinalidad.
- Infraestructura: CPU, memoria, disco, red, escalado y costos.
- Procesos asíncronos: backpressure, lotes, reintentos e idempotencia.

## Reglas
- No inventes métricas ni porcentajes.
- No uses microbenchmarks como sustituto automático de carga real.
- No cambies arquitectura sin demostrar necesidad.
- No elimines controles de seguridad para ganar rendimiento.
- Protege datos productivos durante pruebas.

## Informe
Incluye línea base, metodología, cuello de botella, cambio, resultados medidos, entorno, limitaciones y recomendación.

## Verificación
Compara la misma métrica antes y después con igual carga y entorno. En web, Core Web Vitals se evalúa en el percentil 75: LCP ≤ 2,5 s, INP ≤ 200 ms y CLS ≤ 0,1.

## Ejemplo
Listado lento: línea base p95 de 2,4 s; el perfil muestra consultas N+1. Tras la corrección, se mide de nuevo con la misma carga y se informa la cifra real.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
