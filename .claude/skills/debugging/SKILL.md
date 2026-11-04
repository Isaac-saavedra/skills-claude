---
name: debugging
description: "Diagnostica errores de software mediante síntomas, logs, trazas, reproducción y análisis de causa raíz. Úsala cuando una aplicación falle, presente resultados inesperados o tenga errores intermitentes."
---

# Debugging

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
