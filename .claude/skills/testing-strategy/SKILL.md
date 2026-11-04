---
name: testing-strategy
description: "Define qué probar y en qué nivel: pirámide, cobertura útil, regresión, aceptación y gestión de pruebas inestables. Usar al diseñar el plan de pruebas de un proyecto o de una versión."
---

# Testing Strategy

## Alcance
Decisiones de estrategia. No cubre:
- Escribir y ejecutar la automatización: `qa-automation`.
- Encontrar la causa de un fallo: `debugging`.

## Procedimiento
1. Identifica riesgos de negocio: qué fallo causaría más daño (dinero, datos, seguridad, disponibilidad).
2. Inventaría pruebas existentes: tipo, duración, inestabilidad y cobertura de riesgos.
3. Asigna cada riesgo al nivel más bajo que lo detecte:
   - Unitarias: lógica y casos límite; muchas y rápidas.
   - Integración: base de datos, colas y servicios reales o contenedores.
   - Contrato: compatibilidad entre consumidor y proveedor.
   - End-to-end: pocos recorridos críticos.
4. Si una prueba alta detecta un fallo que ninguna baja detectó, añade la baja.
5. Define datos de prueba, entornos y dependencias simuladas.
6. Define barreras: qué corre en cada PR, cada fusión y cada versión, con tiempos objetivo.
7. Define política de inestabilidad: aislar, asignar dueño y corregir con fecha.
8. Enlaza cada requisito o riesgo crítico con su prueba.

## Reglas
- La forma de pirámide no es un fin. Lo que importa es que las pruebas sean expresivas, rápidas, fiables y fallen solo por motivos útiles.
- La cobertura indica lo no ejecutado; no demuestra calidad. No la fijes como único objetivo.
- Evita duplicar el mismo caso en varios niveles sin motivo.
- No declares un flujo probado sin una ejecución real.

## Verificación
Cada riesgo alto tiene una prueba o una aceptación explícita, y la barrera de PR corre dentro del tiempo acordado.

## Entrega
Matriz riesgo → nivel → prueba, barreras de CI, datos y entornos, política de inestables, huecos y próximos pasos.

## Ejemplo
| Riesgo | Nivel | Dónde corre |
|---|---|---|
| Cálculo de impuestos incorrecto | Unitaria | Cada PR |
| Migración rompe consultas | Integración | Cada PR |
| El pago no se completa | E2E en sandbox | Antes de la versión |

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
