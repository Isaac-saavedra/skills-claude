---
name: qa-automation
description: "Planifica y automatiza pruebas unitarias, integración, API y end-to-end, incluyendo Playwright cuando corresponda. Úsala para validar funcionalidades, prevenir regresiones y preparar entregas."
---

# QA Automation

## Estrategia
1. Identifica requisitos, criterios de aceptación, riesgos y flujos críticos.
2. Inspecciona framework, herramientas y pruebas existentes.
3. Selecciona niveles adecuados: unitario, integración, contrato, API, E2E y visual.
4. Diseña casos positivos, negativos, límites, permisos, estados vacíos y errores.
5. Prioriza pruebas deterministas y aisladas.
6. Usa datos de prueba no sensibles y entornos seguros.
7. Automatiza con el framework ya adoptado; no agregues dependencias sin justificar.
8. Ejecuta pruebas y registra resultados reales.
9. Aísla fallas intermitentes; no las ocultes con reintentos ilimitados.
10. Integra las pruebas al pipeline cuando se solicite.

## E2E y Playwright
- Usa selectores accesibles y estables; evita depender de clases CSS frágiles.
- Espera condiciones observables, no pausas arbitrarias.
- Limpia y prepara datos de forma reproducible.
- No automatices acciones reales de pago, correo o producción sin autorización.
- Captura trazas, screenshots o logs cuando ayuden a diagnosticar.

## Reporte
Incluye entorno, versión, casos ejecutados, aprobados, fallidos, omitidos, evidencia y defectos. Nunca afirmes que una prueba pasó si no se ejecutó.
