---
name: fullstack-development
description: "Implementa y mantiene aplicaciones web full stack, desde la interfaz hasta backend, persistencia, autenticación e integración. Úsala al crear funcionalidades, aplicaciones completas o modificar proyectos existentes."
---

# Full Stack Development

## Objetivo
Implementar funcionalidades completas, coherentes y mantenibles respetando la arquitectura y convenciones del proyecto existente.

## Flujo obligatorio
1. Inspecciona archivos, estructura, package/config files, versiones, scripts, pruebas y convenciones antes de editar.
2. Resume el comportamiento solicitado y define criterios de aceptación verificables.
3. Identifica frontend, backend, contratos API, modelo de datos, permisos y dependencias afectadas.
4. Propón un plan breve si el cambio es amplio o afecta datos, autenticación o infraestructura.
5. Implementa en incrementos pequeños y consistentes con el stack existente.
6. Valida entradas en servidor; no confíes únicamente en validaciones del navegador.
7. Maneja estados de carga, éxito, vacío y error en la interfaz.
8. Añade o actualiza pruebas relevantes.
9. Ejecuta lint, typecheck, pruebas y build disponibles. Registra los comandos y resultados reales.
10. Actualiza documentación, variables de entorno de ejemplo y notas de migración cuando corresponda.

## Principios
- No reemplaces tecnologías ni reestructures todo el proyecto sin necesidad.
- No inventes endpoints, tablas, variables, credenciales o respuestas de servicios.
- No guardes secretos en código, logs, repositorios ni archivos públicos.
- Aplica mínimo privilegio y autorización del lado servidor.
- Evita duplicar lógica y abstraer prematuramente.
- Mantén compatibilidad con clientes existentes o documenta cambios incompatibles.
- No marques tareas como terminadas si no se ejecutaron las validaciones pertinentes.

## Entrega
Resume archivos modificados, comportamiento implementado, decisiones, pruebas ejecutadas, resultados, limitaciones y pasos para ejecutar. Distingue pruebas no ejecutadas de pruebas fallidas.
