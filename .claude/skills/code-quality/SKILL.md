---
name: code-quality
description: "Define y automatiza estándares de código: formateo, linting, análisis estático, tipos, umbrales y convenciones. Usar al configurar calidad en un proyecto o reducir ruido de linters."
---

# Code Quality

## Alcance
Controles automáticos y convenciones de todo el proyecto. No cubre:
- Revisar un cambio concreto: `code-review`.
- Reescribir código: `refactoring`.
- Diseñar pruebas: `testing-strategy`.
- Vulnerabilidades: `secure-code-development`.

## Procedimiento
1. Inspecciona lo que ya existe: configuración de linter, formateador, tipos, hooks y CI. Respétalo por defecto.
2. Mide la línea base sin modificar nada y registra número y tipo de hallazgos.
3. Separa cuatro capas: formato, lint, tipos y análisis estático.
4. Elige la herramienta dominante en el ecosistema del proyecto y confirma en su documentación vigente la versión y configuración.
5. Fija la versión de cada herramienta en el manifiesto y lockfile para que local y CI coincidan.
6. Activa las reglas de forma gradual:
   - Aplica formato en un único commit aislado.
   - Exige cero errores nuevos en lo modificado.
   - Reduce el resto por tandas.
7. Integra los controles en CI y, opcionalmente, en un hook de pre-commit. CI es la barrera que manda.
8. Documenta comandos y excepciones.

## Reglas
- Ninguna supresión sin motivo: `// eslint-disable-next-line regla -- motivo`.
- No uses "cero avisos" como meta si incentiva silenciar reglas.
- Una métrica como la cobertura o la complejidad es una señal, no un objetivo en sí.
- No impongas preferencias personales como errores; el formateador resuelve el estilo.
- El objetivo de revisión es mejorar la salud del código, no buscar el código perfecto.

## Verificación
El mismo comando da igual resultado en local y CI, un cambio deliberadamente incorrecto hace fallar el control, y el commit de formato no altera el comportamiento.

## Entrega
Línea base, herramientas y versiones, reglas activadas o aplazadas, comandos, integración en CI y excepciones justificadas.

## Ejemplo
Proyecto con 3.000 avisos: formato en un commit aislado; CI compara solo archivos cambiados; plan semanal por módulo. No se desactivan reglas para mejorar la cifra.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
