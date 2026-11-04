---
name: system-integration
description: "Integra aplicaciones con APIs externas, webhooks y ERP/SaaS: autenticación, mapeo, reintentos, idempotencia y conciliación. Usar al conectar sistemas o sincronizar datos con terceros."
---

# System Integration

## Alcance
Conectar sistemas distintos con fiabilidad. No cubre:
- Diseñar tu propia API: `api-engineering`.
- Topología de colas: `message-queue-engineering`.
- Diseño de identidad: `identity-access-management`.

## Procedimiento
1. Lee la documentación vigente del tercero: autenticación, límites, paginación, errores, versión y entorno de pruebas. No inventes endpoints ni campos.
2. Define dirección, frecuencia, sistema maestro por dato y volumen.
3. Crea una matriz de mapeo con campos, tipos, transformaciones y valores nulos.
4. Encapsula la integración detrás de un adaptador interno para que el formato ajeno no se extienda por el código.
5. Configura timeout en cada llamada.
6. Reintenta solo errores transitorios y operaciones idempotentes, con backoff exponencial y jitter, límite total y en una sola capa.
7. Respeta `429` y `Retry-After` si el proveedor los usa.
8. Webhooks: verifica la firma, responde rápido, encola, deduplica por identificador y tolera desorden.
9. Registra correlación sin secretos ni datos personales innecesarios.
10. Crea una conciliación periódica: detecta y corrige divergencias.

## Reglas
- Prueba en sandbox. No generes efectos reales (cobros, correos) sin autorización.
- Guarda credenciales fuera del código: `secrets-management`.
- No afirmes que una integración funciona si solo se probó con simulaciones; decláralo.

## Verificación
Prueba éxito, timeout, `429`, `5xx`, duplicado, carga parcial y credencial inválida, contra sandbox o simulación declarada.

## Entrega
Diagrama, matriz de mapeo, autenticación, errores y reintentos, operación, conciliación, pruebas y dependencias del proveedor.

## Ejemplo
Webhook de pagos: valida la firma, inserta el `event_id` con restricción única, encola y responde. Si el evento ya existe, responde igualmente sin reprocesar.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
