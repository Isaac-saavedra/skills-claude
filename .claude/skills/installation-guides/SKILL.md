---
name: installation-guides
description: "Escribe guías de instalación y configuración reproducibles, con prerrequisitos, comandos, verificación y resolución de errores. Usar al documentar cómo instalar un sistema, herramienta o entorno."
---

# Installation Guides

## Alcance
Llevar un sistema de cero a funcionando. No cubre:
- Publicar versiones en producción: `deployment-documentation`.
- Uso diario: `user-manual-creation`.

## Procedimiento
1. Define destinatario, entorno, sistema operativo y versiones compatibles.
2. Lista prerrequisitos con versión mínima y cómo comprobarlos.
3. Extrae los comandos de archivos reales (`Dockerfile`, `Makefile`, CI, manifiestos). Nunca de memoria.
4. Ejecútalos en un entorno limpio: contenedor o máquina virtual.
5. Escribe cada paso: propósito, comando con marcadores, resultado esperado y forma de comprobarlo.
6. Documenta configuración y variables en una tabla, con `.env.example` sin valores reales.
7. Añade la comprobación final de funcionamiento.
8. Añade solución de problemas con errores que hayan ocurrido realmente.
9. Añade actualización y desinstalación.

## Reglas
- Separa lo probado de lo no probado e indica el entorno y fecha de la prueba.
- Explica los comandos que requieren `sudo` o modifican el sistema.
- Advierte antes de `curl | sh` y ofrece alternativa cuando exista.
- Marca los valores que se deben reemplazar: `<dominio>`.
- No incluyas secretos reales.

## Verificación
Ejecuta la guía completa en un entorno limpio. Si no fue posible, indica exactamente qué pasos no se probaron.

## Entrega
Guía, entorno de prueba, resultado de la ejecución, pasos no comprobados y limitaciones.

## Ejemplo
```markdown
### 1. Comprobar Node
Ejecuta `node --version`.
Resultado esperado: la versión que indica `engines` en `package.json`.

### 2. Instalar dependencias
Ejecuta `npm ci`.
Si falla con `EBADENGINE`, instala la versión requerida de Node.

### 3. Verificar
Ejecuta `curl http://localhost:3000/salud`.
Resultado esperado: `{"estado":"ok"}`.
```
La ruta `/salud` y su respuesta deben provenir del proyecto.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
