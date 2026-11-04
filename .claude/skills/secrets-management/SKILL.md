---
name: secrets-management
description: "Gestiona credenciales, claves y tokens: almacenamiento, inyección, rotación, auditoría y respuesta a filtraciones. Usar ante secretos en código, .env, CI/CD o una credencial expuesta."
---

# Secrets Management

## Alcance
Ciclo de vida de secretos. No cubre:
- Autenticación de usuarios: `identity-access-management`.
- Pipeline en general: `cicd-engineering`.

## Procedimiento
1. Inventaría secretos: qué son, dónde se usan, quién accede, dueño y última rotación. Nunca copies sus valores en el informe.
2. Centraliza en un gestor de secretos y separa producción de desarrollo.
3. Aplica mínimo privilegio, con permisos por secreto.
4. Prefiere identidad de carga de trabajo o credenciales dinámicas de vida corta a claves fijas.
5. Entrega en tiempo de ejecución. Evita pasarlas por el pipeline, por imágenes o por argumentos visibles.
6. Automatiza la rotación y define caducidad.
7. Audita solicitudes, uso, cambios, denegaciones y reintentos con secretos caducados.
8. Activa detección en repositorios y en pre-commit.

## Si hay una filtración
1. **Revoca primero** en el servicio de origen. Reiniciar la aplicación no revoca una credencial robada.
2. Crea un secreto nuevo por un proceso automatizado.
3. Revisa los registros de uso desde la exposición.
4. Elimina el secreto del código y los registros, conservando la integridad de la evidencia.
5. Reescribir el historial Git es opcional y destructivo: pide autorización. Nunca sustituye a revocar.
6. Avisa según el plan de respuesta: `incident-response`.

## Reglas
- No imprimas secretos en logs, salidas o mensajes de chat.
- Base64 no es cifrado.
- `.env` solo para desarrollo local, ignorado en Git, con `.env.example` sin valores.
- Protege el secreto raíz del gestor en un segundo sistema.

## Verificación
Escaneo sin hallazgos nuevos, la aplicación funciona con el secreto rotado, el antiguo ya falla y queda registro de acceso.

## Entrega
Inventario sin valores, arquitectura, plan de rotación, controles, pruebas y acciones de respuesta.

## Ejemplo
Clave de API en un commit público: revocar y emitir una nueva, revisar uso desde la fecha del commit, moverla al gestor, añadir escaneo en CI y preguntar antes de reescribir el historial.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
