---
name: debugging
description: "Diagnostica errores mediante síntomas, logs, trazas, reproducción y causa raíz. Usar siempre ante excepciones, stack traces, fallos intermitentes o resultados inesperados, antes de proponer una corrección."
---

# Debugging

## Alcance
**No cubre:** Incidente activo con impacto en usuarios: `incident-response`. Lentitud sin error: `performance-optimization`.

## Principio
No adivines la causa. Construye y verifica hipótesis con evidencia.

## Flujo
1. Recopila mensaje exacto, stack trace, logs, entorno, versión, hora, frecuencia y cambios recientes.
2. Separa hechos observados de hipótesis.
3. Determina alcance: usuario, módulo, entorno, instancia o sistema completo.
4. Intenta reproducir sin alterar datos productivos.
5. Formula hipótesis ordenadas por evidencia y costo de comprobación.
6. Ejecuta una prueba por vez y registra resultado.
7. Identifica causa raíz y factores contribuyentes.
8. Propón corrección mínima, mitigación temporal y prevención.
9. Define pruebas de regresión y monitoreo.
10. Documenta el incidente y los pasos de recuperación.

## Seguridad operativa
- No borres logs, datos ni cachés indiscriminadamente.
- No reinicies servicios ni cambies producción sin autorización.
- Protege secretos y datos personales al compartir logs.
- Antes de comandos potencialmente destructivos, explica impacto y pide confirmación.
- No confundas correlación con causalidad.

## Informe
Incluye síntoma, impacto, evidencia, hipótesis descartadas, causa confirmada o estado no concluyente, solución, validación y acciones preventivas.

## Verificación
El fallo se reproduce antes de la corrección y no después. Añade una prueba de regresión y confirma con el mismo procedimiento.

## Ejemplo
Error intermitente: los registros coinciden con una rotación de conexiones. Hipótesis: el pool reutiliza conexiones cerradas. Prueba: reproducir con `max_lifetime` bajo. Resultado confirmado; corrección y prueba de regresión.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
