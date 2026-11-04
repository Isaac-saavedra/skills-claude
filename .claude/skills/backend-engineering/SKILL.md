---
name: backend-engineering
description: "Desarrolla servicios del lado servidor: lógica de negocio, capas, transacciones, errores y procesos asíncronos. Usar siempre al implementar o modificar lógica de servidor."
---

# Backend Engineering

## Alcance
**No cubre:** Contrato HTTP: `api-engineering`. Runtime Node: `nodejs-engineering`. Python: `python-engineering`. Esquemas: `database-engineering`. Colas: `message-queue-engineering`.

## Procedimiento
1. Inspecciona runtime, framework, estructura, configuración, dependencias y pruebas existentes.
2. Define contrato, reglas de negocio, actores, permisos, errores y requisitos de rendimiento.
3. Valida datos en el límite de confianza y vuelve a validar reglas críticas en el servidor.
4. Separa transporte, dominio y persistencia de acuerdo con la escala real del proyecto.
5. Maneja errores de forma consistente; evita filtrar stack traces, secretos o datos personales.
6. Diseña idempotencia, timeouts, reintentos y límites para operaciones distribuidas cuando sean necesarios.
7. Usa transacciones y restricciones de base de datos para proteger invariantes.
8. Registra eventos útiles sin incluir contraseñas, tokens ni información sensible.
9. Añade pruebas unitarias, integración y contrato según riesgo.
10. Documenta configuración, endpoints, dependencias, ejecución y recuperación.

## Seguridad y confiabilidad
- Aplica autenticación y autorización en servidor.
- Usa mínimo privilegio, gestión segura de secretos y límites de tasa cuando aplique.
- Evita SQL injection, command injection, SSRF, path traversal y deserialización insegura.
- No confíes en datos enviados por el cliente.
- No uses reintentos infinitos ni ocultes errores.
- No cambies esquemas ni datos en producción sin plan de migración y rollback.

## Verificación
Ejecuta pruebas y análisis disponibles. Informa exactamente qué se ejecutó, qué pasó, qué falló y qué no se pudo verificar.
Ejecuta pruebas unitarias y de integración, incluidos fallos de dependencias, permisos y transacción interrumpida.

## Ejemplo
Transferencia de saldo: una sola transacción, restricción `saldo >= 0` en la base de datos, clave de idempotencia y prueba con dos solicitudes simultáneas.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
