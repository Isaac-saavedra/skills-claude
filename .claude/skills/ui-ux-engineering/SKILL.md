---
name: ui-ux-engineering
description: "Evalúa y mejora la experiencia de usuario: flujos, heurísticas, formularios, mensajes de error y estados de interfaz. Usar ante pantallas confusas o al revisar la usabilidad de un producto."
---

# UI/UX Engineering

## Alcance
Cómo funciona la experiencia para quien la usa. No cubre:
- Identidad visual y maquetación: `frontend-design`.
- Conformidad WCAG: `web-accessibility`.

## Procedimiento
1. Define usuario, tarea principal, contexto y criterio de éxito.
2. Recorre el flujo real, paso a paso, y registra fricción con capturas o referencias de código.
3. Evalúa con las 10 heurísticas.
4. Da severidad a cada hallazgo: frecuencia, impacto y persistencia.
5. Propón cambios concretos: texto exacto, estructura o estado que falta.
6. Revisa siempre estos estados: carga, vacío, error, éxito, sin permiso y sin conexión.
7. Formularios: etiquetas visibles, validación útil, conservar lo escrito tras un error y marcar lo obligatorio.
8. Cuando la decisión dependa de usuarios reales, recomienda una prueba de usabilidad y sus tareas.

## Heurísticas
1. Visibilidad del estado del sistema.
2. Relación con el mundo real.
3. Control y libertad.
4. Consistencia y estándares.
5. Prevención de errores.
6. Reconocer antes que recordar.
7. Flexibilidad y eficiencia.
8. Diseño estético y minimalista.
9. Reconocer, diagnosticar y recuperarse de errores.
10. Ayuda y documentación.

## Reglas
- Una evaluación heurística orienta; no sustituye la observación de usuarios reales.
- No inventes métricas de conversión ni resultados de estudios.
- Separa problema observado, hipótesis y recomendación.

## Verificación
Se puede completar la tarea principal sin explicación externa, y cada estado de la interfaz fue revisado o quedó listado como no revisado.

## Entrega
Flujo evaluado, hallazgos con heurística y severidad, cambios propuestos o implementados, y pruebas recomendadas.

## Ejemplo
Hallazgo: "Error 422" al guardar. Heurística 9, severidad alta. Cambio: "No pudimos guardar: la fecha de fin debe ser posterior a la de inicio". El campo queda marcado y los datos se conservan.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
