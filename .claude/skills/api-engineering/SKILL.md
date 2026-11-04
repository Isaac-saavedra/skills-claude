---
name: api-engineering
description: "Diseña, implementa y valida APIs HTTP/REST: rutas, contratos, errores, versionado, permisos y límites. Usar al crear endpoints o revisar el diseño de una API."
---

# API Engineering

## Alcance
**No cubre:** Documentar una API existente: `api-documentation`. Integrar con API de terceros: `system-integration`. Identidad y OAuth: `identity-access-management`.

## Diseño del contrato
1. Identifica consumidores, casos de uso, recursos y operaciones.
2. Inspecciona convenciones y endpoints existentes antes de proponer rutas.
3. Define métodos HTTP, rutas, parámetros, esquemas, códigos de estado y errores.
4. Diseña paginación, filtros, ordenamiento, límites y comportamiento idempotente cuando corresponda.
5. Define autenticación, autorización, scopes y permisos por recurso.
6. Considera versionado y compatibilidad hacia atrás.
7. Documenta el contrato en OpenAPI cuando el proyecto lo permita.

## Implementación
- Valida tipos, formatos, rangos y tamaño de solicitudes.
- Usa códigos HTTP coherentes y respuestas de error estables.
- No expongas detalles internos, secretos ni datos de otros usuarios.
- Protege contra abuso mediante límites y cuotas cuando corresponda.
- Define timeouts y comportamiento ante fallas de dependencias.
- Evita cambios incompatibles sin plan de migración.

## Pruebas
Cubre respuestas exitosas, entradas inválidas, falta de autenticación, permisos insuficientes, recurso inexistente, límites, conflictos y fallas de dependencias.

## Documentación
Incluye propósito, autenticación, endpoints, ejemplos realistas claramente identificados, esquemas, errores, límites, versionado y guía de cambios. No inventes ejemplos que contradigan la implementación real.

## Verificación
Pruebas de contrato con éxito, entrada inválida (`400`/`422`), sin autenticación (`401`), sin permiso (`403`), inexistente (`404`), método no permitido (`405`) y exceso de uso (`429`). Comprueba que los errores no revelen detalles internos.

## Ejemplo
`POST /pedidos` con `Idempotency-Key`: el reintento devuelve el mismo pedido sin duplicar. Los errores usan `application/problem+json` si el proyecto adopta RFC 9457.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
