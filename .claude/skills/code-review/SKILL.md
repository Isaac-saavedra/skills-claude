---
name: code-review
description: "Realiza revisiones de código enfocadas en defectos, seguridad, regresiones, mantenibilidad y rendimiento. Úsala para revisar cambios, pull requests, diffs o módulos antes de integrarlos."
---

# Code Review

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
