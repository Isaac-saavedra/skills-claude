---
name: mobile-development
description: "Desarrolla y revisa apps móviles Android e iOS: arquitectura, estado, offline, permisos, seguridad y publicación en tiendas. Usar con Kotlin, Swift, Flutter o React Native."
---

# Mobile Development

## Alcance
Aplicaciones móviles nativas o multiplataforma. No cubre:
- Backend de la app: `backend-engineering`.
- Componentes React web: `react-development`.

## Procedimiento
1. Identifica plataforma, framework, versiones mínimas de sistema, navegación y gestión de estado. Sigue lo que ya existe.
2. Aplica la arquitectura por capas: UI y datos, más dominio solo si reutiliza lógica o reduce complejidad.
3. Sigue flujo unidireccional de datos y una única fuente de verdad por tipo de dato.
4. Diseña para condiciones móviles: red lenta o nula, cambios de ciclo de vida, cierre del proceso, rotación, batería y permisos denegados.
5. Pide cada permiso en contexto y ofrece una alternativa si se deniega.
6. Almacena datos sensibles según los controles de MASVS y usa el almacén seguro de la plataforma. No guardes secretos del servidor en la app: se pueden extraer.
7. Prueba en dispositivo real o emulador de la versión mínima y actual.
8. Antes de publicar, revisa las políticas vigentes de cada tienda.

## Reglas
- Toda comprobación de seguridad decisiva debe residir también en el servidor.
- Apple exige política de privacidad, consentimiento y eliminación de cuenta dentro de la app si esta permite crearla: confirma las condiciones vigentes.
- No afirmes que una app cumple MASVS sin una verificación por control.
- No publiques en tiendas sin autorización explícita del usuario.

## Verificación
Compilación de las plataformas objetivo, pruebas ejecutadas y flujo probado sin conexión, con permiso denegado y tras reiniciar el proceso.

## Entrega
Cambios, plataformas probadas con versiones, casos cubiertos, requisitos de tienda pendientes y limitaciones.

## Ejemplo
Pantalla de pedidos sin red: la interfaz muestra datos del repositorio local con la fecha de actualización y encola los cambios. Un `ViewModel` expone el estado; el repositorio decide entre caché y red.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
