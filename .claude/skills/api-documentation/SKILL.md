---
name: api-documentation
description: "Crea y valida documentación OpenAPI/Swagger y guías de API a partir del comportamiento real: rutas, esquemas, errores, autenticación y ejemplos. Usar para documentar endpoints existentes."
---

# API Documentation

## Alcance
Documentar el contrato de una API. No cubre:
- Diseñar o cambiar la API: `api-engineering`.
- Manuales para no técnicos: `user-manual-creation`.

## Procedimiento
1. Obtén la fuente de verdad: código de rutas, validadores, pruebas o tráfico autorizado. Si hay un OpenAPI, compáralo con el código.
2. Confirma qué versión de OpenAPI soporta tu herramienta antes de escribir. Publicadas: 3.0.4, 3.1.2 y 3.2.1 en la fecha de revisión.
3. Documenta para cada operación: método, ruta, parámetros, cuerpo, respuestas, errores y autenticación.
4. Describe esquemas reutilizables con tipos, obligatorios, formatos y restricciones.
5. Usa `operationId` estable y descripciones orientadas a la tarea.
6. Documenta los errores. Si la API usa RFC 9457, describe `type`, `title`, `status`, `detail`, `instance` y `application/problem+json`.
7. Añade ejemplos reales y sanitizados, con paginación, límites de uso y versionado si existen.
8. Valida con un linter de OpenAPI y, si es posible, prueba las respuestas contra el esquema.
9. Añade la guía rápida: autenticación y primera llamada.

## Reglas
- No inventes endpoints, campos, códigos ni límites. Lo no comprobado se marca "Por confirmar".
- Si el código y la documentación se contradicen, informa de ello; no elijas en silencio.
- No incluyas credenciales reales en ejemplos.
- No llames API de producción con efectos sin autorización.

## Verificación
El archivo pasa el validador, los ejemplos concuerdan con el esquema y una muestra de operaciones se comprobó con una llamada real o prueba automatizada.

## Entrega
Especificación, guía rápida, cobertura documentada, comando de validación con resultado, discrepancias y pendientes.

## Ejemplo
```yaml
openapi: 3.1.2
info: { title: API de pedidos, version: 1.0.0 }
paths:
  /pedidos/{id}:
    get:
      operationId: obtenerPedido
      parameters:
        - { name: id, in: path, required: true, schema: { type: string } }
      responses:
        "200": { description: Pedido encontrado }
        "404": { description: Pedido no encontrado }
```

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
