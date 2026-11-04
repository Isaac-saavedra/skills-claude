---
name: software-architecture
description: "Diseña y evalúa arquitecturas: límites de módulos, estilos, compromisos y requisitos no funcionales. Usar siempre al elegir entre monolito y servicios, iniciar un sistema o evaluar escalabilidad."
---

# Software Architecture

## Alcance
**No cubre:** Documentar lo existente: `architecture-documentation`. Función concreta: `technical-specification`. Ejecución de microservicios: `microservices-engineering`. Patrones de clases: `design-patterns`.

## Objetivo
Diseñar soluciones comprensibles, seguras, mantenibles y proporcionales a los requisitos. No elijas microservicios, colas, cachés ni patrones complejos por moda.

## Procedimiento
1. Resume el problema, usuarios, objetivos y restricciones conocidas.
2. Separa requisitos funcionales de no funcionales: disponibilidad, latencia, seguridad, privacidad, costo, volumen, recuperación y mantenibilidad.
3. Identifica incógnitas que cambien la arquitectura. Pregunta antes de asumirlas.
4. Inspecciona el repositorio y la infraestructura existentes antes de proponer reemplazos.
5. Presenta al menos una opción simple y, si aporta valor, alternativas. Compara complejidad, costo, riesgos y operación.
6. Define componentes, responsabilidades, límites, flujos de datos, dependencias y puntos de falla.
7. Considera autenticación, autorización, secretos, cifrado, auditoría, copias de seguridad y recuperación.
8. Produce diagramas Mermaid válidos cuando ayuden: contexto, contenedores, secuencia o despliegue.
9. Registra decisiones importantes como ADR: contexto, decisión, alternativas, consecuencias y estado.
10. Define cómo validar la arquitectura mediante pruebas, métricas y criterios de aceptación.

## Reglas
- No inventes requisitos, volúmenes, SLA, costos ni capacidades de servicios.
- Verifica las características de productos y versiones en documentación oficial cuando sean relevantes.
- Distingue hechos confirmados, supuestos explícitos y preguntas pendientes.
- Prefiere la solución más sencilla que satisfaga los requisitos.
- No presentes un diagrama como evidencia de que la arquitectura está desplegada.
- No migres ni cambies sistemas existentes sin plan, respaldo, rollback y aprobación.

## Entregables posibles
- Resumen ejecutivo y requisitos.
- Diagrama de contexto y componentes.
- Matriz de alternativas.
- ADR.
- Riesgos y mitigaciones.
- Plan de implementación por fases.
- Criterios de aceptación y operación.

## Criterio de finalización
La propuesta debe poder ser revisada por otro desarrollador y explicar qué se construye, por qué, qué queda fuera, cuáles son los riesgos y cómo se comprobará.

## Verificación
Comprueba cada requisito no funcional con un método: prueba, métrica o análisis. Marca como hipótesis lo no validado y revisa la propuesta con quien la operará.

## Ejemplo
Aplicación de 5 personas y poca carga: monolito modular con PostgreSQL como opción simple; microservicios descartados por coste operativo. Decisión registrada en un ADR, con criterios para reevaluarla.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
