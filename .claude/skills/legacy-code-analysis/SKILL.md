---
name: legacy-code-analysis
description: "Comprende y documenta sistemas antiguos sin pruebas ni documentación: comportamiento real, costuras y dependencias. Usar antes de cambiar código heredado o planificar su reemplazo."
---

# Legacy Code Analysis

## Alcance
Descubre lo que el sistema hace hoy y cómo cambiarlo con seguridad. No cubre:
- Inventario general de un repositorio: `repository-analysis`.
- Ejecución de la migración: `migration-engineering`.
- Priorización de deuda: `technical-debt-management`.

## Procedimiento
1. Confirma motivo del análisis, zona afectada y si el sistema sigue en producción.
2. Establece un entorno de ejecución aislado. Si no es posible, indícalo y limita el análisis a lectura.
3. Reúne evidencia: código, esquema de datos, trabajos programados, registros, integraciones y conocimiento de usuarios.
4. Traza los flujos críticos desde la entrada hasta el efecto final.
5. Documenta las reglas de negocio implícitas con ubicación exacta. Trata el comportamiento extraño como posible requisito hasta confirmar lo contrario.
6. Localiza costuras: lugares donde cambiar comportamiento sin editar ese punto.
7. Protege lo que vas a tocar con pruebas de caracterización, que fijan el comportamiento actual y no el deseado.
8. Sigue el orden: identificar costuras, romper dependencias con el mínimo cambio, añadir pruebas, cambiar y refactorizar.
9. Enumera funciones sin uso solo con evidencia de registros o métricas.

## Reglas
- Nunca ejecutes contra producción ni con datos reales sin autorización.
- No corrijas un "error" descubierto sin confirmar que nadie depende de él.
- No propongas igualar todas las funciones del sistema antiguo como objetivo: suele copiar funciones sin uso y subestimar el esfuerzo. Prioriza necesidades actuales.
- Distingue comportamiento observado, intención supuesta y recomendación.

## Verificación
Cada regla cita archivo y línea o una ejecución; las pruebas de caracterización pasan contra el código sin cambios y fallan al alterar deliberadamente la regla.

## Entrega
Mapa del sistema, flujos, reglas implícitas, dependencias, costuras, pruebas añadidas, zonas sin comprender y riesgos de cambio.

## Ejemplo
Un procedimiento almacenado redondea descuentos hacia abajo. El informe lo registra como `comportamiento observado`, añade una prueba de caracterización y pregunta a negocio si es intencional antes de cambiarlo.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
