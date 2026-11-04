---
name: qa-automation
description: "Escribe y ejecuta pruebas automatizadas unitarias, de integración, API y end-to-end, incluido Playwright. Usar para automatizar casos, prevenir regresiones o corregir pruebas frágiles."
---

# QA Automation

## Alcance
**No cubre:** Decidir qué probar y en qué nivel: `testing-strategy`. Causa de un fallo de la aplicación: `debugging`.

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

## Verificación
Ejecuta las pruebas en local y CI. Provoca un fallo deliberado para confirmar que la prueba lo detecta. Repite las inestables varias veces antes de darlas por corregidas.

## Ejemplo
```ts
await page.getByRole('button', { name: 'Guardar' }).click();
await expect(page.getByText('Pedido guardado')).toBeVisible();
```
Selectores por rol y aserciones que reintentan, sin pausas fijas.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
