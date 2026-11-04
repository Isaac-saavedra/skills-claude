---
name: code-review
description: "Revisa código buscando defectos, seguridad, regresiones, mantenibilidad y rendimiento. Usar siempre que se pida revisar un pull request, diff o cambio antes de fusionarlo."
---

# Code Review

## Alcance
**No cubre:** Configurar linters y estándares: `code-quality`. Auditoría de seguridad completa: `application-security`.

## Objetivo
Encontrar problemas concretos y accionables. No conviertas preferencias de estilo en defectos.

## Proceso
1. Inspecciona el diff y el contexto necesario del código relacionado.
2. Comprende el comportamiento esperado y las convenciones del proyecto.
3. Sigue flujos de datos, permisos, errores, concurrencia y efectos secundarios.
4. Busca defectos funcionales, regresiones, riesgos de seguridad, pérdida de datos, problemas de rendimiento y falta de pruebas.
5. Ejecuta análisis o pruebas solo si las herramientas están disponibles y es seguro.
6. Prioriza hallazgos por severidad y probabilidad.

## Formato de hallazgo
- Severidad: crítica, alta, media o baja.
- Archivo y línea exacta, si está disponible.
- Problema observado.
- Escenario concreto de reproducción o impacto.
- Por qué ocurre.
- Corrección recomendada.
- Evidencia o prueba.

## Reglas
- No inventes vulnerabilidades ni escenarios no sustentados por el código.
- No reportes una posibilidad remota como defecto confirmado.
- Distingue hallazgos confirmados de preguntas o sugerencias.
- No modifiques el código durante una revisión de solo lectura, salvo que el usuario pida corregirlo.
- No declares que el código es seguro por no haber encontrado problemas.

## Resumen
Incluye alcance revisado, hallazgos ordenados, pruebas ejecutadas y limitaciones de la revisión.

## Verificación
Cada hallazgo confirmado cita archivo, línea y un escenario concreto. Si una prueba se ejecutó, incluye el comando y resultado.

## Ejemplo
**Alta**. `pagos.py:88`. El reintento repite el cobro porque falta clave de idempotencia. Escenario: timeout tras cobrar → segundo cobro. Corrección: enviar la clave y añadir una prueba.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
