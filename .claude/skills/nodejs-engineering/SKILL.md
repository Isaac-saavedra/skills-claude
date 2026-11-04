---
name: nodejs-engineering
description: "Desarrolla y diagnostica servicios Node.js: LTS, asincronía, event loop, streams, memoria y seguridad. Usar siempre con servidores Node lentos, bloqueados o inestables, aunque la causa parezca evidente."
---

# Node.js Engineering

## Alcance
Runtime y procesos Node. No cubre:
- Diseño de servicios: `backend-engineering`.
- Contrato HTTP: `api-engineering`.
- Tipos: `typescript-engineering`.

## Procedimiento
1. Comprueba versión instalada, `engines`, gestor de paquetes y sistema de módulos (ESM o CommonJS).
2. Confirma en la tabla oficial que la versión está en LTS. Producción debe usar Active o Maintenance LTS.
3. Propaga errores asíncronos: `await`, manejo de rechazos y cierre ordenado con `SIGTERM`.
4. No bloquees el event loop en rutas de servidor:
   - Evita APIs síncronas como `fs.readFileSync` o `crypto.pbkdf2Sync`.
   - Limita el tamaño antes de `JSON.parse`.
   - Revisa expresiones regulares vulnerables a ReDoS.
   - Particiona con `setImmediate` o usa workers para cálculo pesado.
5. Usa streams para datos grandes y respeta la contrapresión.
6. Aplica la seguridad del runtime:
   - Timeouts de `http.Server` y proxy inverso.
   - Instalación reproducible con `npm ci`.
   - Valora `--ignore-scripts`.
   - Sin inspector en producción.
7. Diagnostica lentitud midiendo con perfiles antes de cambiar nada.

## Reglas
- El calendario de Node cambia: desde Node 27 hay una versión mayor anual y todas pasan a LTS. No afirmes qué versión está activa sin consultar la tabla.
- Compara secretos con `crypto.timingSafeEqual`.
- Evita fusiones recursivas sin proteger `__proto__`.
- No afirmes una fuga de memoria sin evidencia de heap.

## Verificación
Pruebas ejecutadas, cierre limpio ante `SIGTERM`, ninguna API síncrona nueva en rutas y mediciones antes y después si se optimizó.

## Entrega
Versión evaluada, causa o cambio, medición, pruebas y riesgos.

## Ejemplo
Latencia alta con picos: el perfil muestra `JSON.stringify` de 40 MB en el hilo principal. Solución: paginar la respuesta y medir de nuevo; no añadir réplicas para ocultar el bloqueo.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
