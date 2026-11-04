---
name: backend-engineering
description: "Desarrolla servicios backend robustos, mantenibles y seguros, incluyendo lógica de negocio, autenticación, autorización, colas y procesos asíncronos. Úsala al crear o modificar servicios del lado servidor."
---

# Backend Engineering

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
