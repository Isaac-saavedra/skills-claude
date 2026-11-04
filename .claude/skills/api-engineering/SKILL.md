---
name: api-engineering
description: "Diseña, implementa, documenta y valida APIs HTTP/REST y sus contratos, incluyendo autenticación, versionado, errores y OpenAPI. Úsala al crear endpoints, integrar servicios o revisar APIs existentes."
---

# API Engineering

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
