---
name: refactoring
description: "Mejora la estructura interna del código sin cambiar su comportamiento observable, en pasos pequeños protegidos por pruebas. Usar ante duplicación, complejidad o código difícil de modificar."
---

# Refactoring

## Alcance
Refactorizar es reestructurar sin cambiar el comportamiento observable. No cubre:
- Corregir errores: `debugging`.
- Añadir funciones, salvo como preparación explícita.
- Código sin pruebas ni comprensión previa: empieza con `legacy-code-analysis`.

## Procedimiento
1. Define el objetivo: qué cambio futuro será más barato o qué complejidad desaparecerá.
2. Ejecuta las pruebas y registra la línea base. Si no cubren la zona, añade pruebas de caracterización primero.
3. Separa el trabajo: nunca mezcles refactorización y cambio funcional en el mismo commit.
4. Aplica una transformación cada vez: extraer función, renombrar, mover, introducir parámetro, reemplazar condicional.
5. Usa las refactorizaciones automáticas del IDE o lenguaje cuando existan.
6. Ejecuta pruebas tras cada paso. Si fallan, revierte el último paso en vez de depurar encima.
7. Haz commits pequeños y reversibles.
8. Para interfaces usadas por terceros, aplica cambio paralelo: expandir, migrar y contraer.

## Reglas
- Si cambia una respuesta, un error, un orden o un efecto secundario visible, no es una refactorización: decláralo.
- Evita reformatear archivos completos junto con cambios reales: oculta la revisión.
- No limpies código ajeno a la tarea sin acuerdo: amplía el riesgo.
- Detente cuando se cumpla el objetivo. El código poco tocado puede quedarse como está.

## Verificación
Mismas pruebas y mismos resultados antes y después; ninguna prueba debilitada para pasar; linters y tipos sin errores nuevos; diff revisable por commits.

## Entrega
Objetivo, transformaciones, pruebas antes y después con resultados reales, comportamiento confirmado sin cambios y riesgos pendientes.

## Ejemplo
Función de 120 líneas: (1) prueba de caracterización con tres pedidos reales anonimizados; (2) extraer `calcularImpuestos`; (3) extraer `aplicarDescuentos`; (4) renombrar variables. Cada paso es un commit con pruebas en verde.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
