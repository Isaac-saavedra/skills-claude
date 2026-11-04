---
name: project-planning
description: "Convierte objetivos técnicos en planes con alcance, desglose, dependencias, estimaciones por rango, riesgos e hitos. Usar al planificar un proyecto, sprint o roadmap, o al estimar trabajo."
---

# Project Planning

## Alcance
Planificación de trabajo de software. No cubre:
- Definir requisitos: `requirements-engineering`.
- Diseño técnico: `technical-specification`.

## Procedimiento
1. Aclara objetivo, resultado medible, fecha o restricción fija, equipo disponible y metodología.
2. Delimita qué entra y qué no.
3. Desglosa en entregables (WBS). Regla del 100 %: los elementos hijos suman exactamente el alcance del padre.
4. Divide hasta tareas con resultado verificable, sin sobrepasar lo que se puede terminar en una iteración.
5. Identifica dependencias, ruta crítica, recursos compartidos y decisiones bloqueantes.
6. Estima por rangos (optimista, probable, pesimista), con quien hará el trabajo y datos históricos. Marca los supuestos.
7. Registra riesgos: probabilidad, impacto, respuesta y dueño.
8. Define hitos con criterios de salida; prefiere entregas incrementales que validen pronto.
9. Revisa el plan con datos reales de avance.

## Con Scrum
Eventos: Sprint, Planning, Daily, Review y Retrospective. Compromisos: Meta del Producto, Meta del Sprint y Definición de Hecho.

## Reglas
- No inventes capacidad, fechas, responsables ni costes. Usa "Por confirmar".
- Una estimación no es un compromiso: indica incertidumbre.
- No añadas personas como solución sin evaluar el coste de coordinación.
- Si el alcance, la fecha y el equipo son incompatibles, dilo y plantea alternativas.

## Verificación
Cada tarea tiene criterio de finalización, dependencias resueltas, dueño o "Por confirmar", y la suma de tareas cubre el alcance.

## Entrega
Objetivo, alcance, desglose, dependencias, estimaciones con supuestos, cronograma, riesgos y decisiones pendientes.

## Ejemplo
| Tarea | Depende de | Estimación (días) | Dueño | Hecho cuando |
|---|---|---|---|---|
| Diseñar esquema | Requisitos | 1–2–4 | Por confirmar | Revisión aprobada |
| API de pedidos | Esquema | 3–5–8 | Por confirmar | Pruebas de contrato en verde |

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
