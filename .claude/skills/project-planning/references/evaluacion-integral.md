# Evaluación integral y proporcional de un proyecto

Aplica a cualquier proyecto nuevo o existente: software, infraestructura, automatización, datos, integración o negocio. Evalúa de forma integral aunque la tarea sea puntual, sin ampliar el alcance ni hacer cambios no pedidos sin explicarlo y pedir autorización.

## Antes de proponer, desarrollar o documentar

1. Comprende objetivo, problema, alcance, usuarios y actores: gerencia, negocio, analistas, usuarios finales, desarrollo, QA, infraestructura y operaciones.
2. Inspecciona archivos, código, configuraciones, documentación y decisiones existentes.
3. Identifica tecnologías, componentes, dependencias, integraciones y entornos reales.
4. Distingue lo implementado, parcial, heredado, pendiente y propuesto.
5. Identifica requisitos funcionales, técnicos, de seguridad, operación y cumplimiento relevantes.
6. Detecta vacíos, riesgos, restricciones y decisiones que podrían cambiar la solución.
7. Propón un plan proporcional al tamaño del proyecto.

No asumas que todo proyecto necesita frontend, backend, base de datos, nube o arquitectura distribuida. No crees carpetas por cumplir una plantilla ni muevas código heredado sin verificar referencias, dependencias y uso.

## Dimensiones (según aplique)

| Dimensión | Qué revisar |
|---|---|
| Objetivo y alcance | Problema, resultados esperados, exclusiones, responsables, requisitos, criterios de aceptación |
| Arquitectura | Límites del sistema, componentes, infraestructura, integraciones, APIs, colas y eventos, estructura del repositorio, decisiones y sus motivos |
| Desarrollo | Versiones compatibles, calidad, validaciones, manejo de errores, configuración por entorno, dependencias, migraciones, pruebas, deuda técnica |
| Seguridad y privacidad | Autenticación, autorización, roles, datos y secretos, cifrado, validación de entradas, auditoría. Un control documentado no está implementado hasta comprobarlo |
| QA | Estrategia proporcional al riesgo; pruebas unitarias, de integración, funcionales y de regresión; casos positivos, negativos y excepciones; evidencias; defectos conocidos |
| Despliegue | Entornos, infraestructura como código, permisos, CI/CD, variables, verificación posterior, rollback |
| Operación | Logs, métricas, monitoreo, alertas, backups y restauración, procedimientos, incidentes, rendimiento, soporte |
| Gestión | Estado, hitos, riesgos, bloqueos, decisiones pendientes, indicadores medibles, traspaso |

No inventes fechas, responsables, costos, porcentajes, beneficios, ROI ni métricas. Si no hay datos, indica qué debe medirse y déjalo pendiente de definición.

## Entrega

No generes decenas de documentos o diagramas de golpe. Primero una evaluación breve:

- qué necesita el proyecto;
- qué existe y está vigente;
- qué está incompleto o desactualizado;
- qué falta y qué es prioritario;
- qué no aplica y por qué.

Luego recomienda un orden de trabajo, empezando por lo que reduce riesgos o permite desarrollar, probar, desplegar y operar.

## Proporcionalidad

- Proyecto pequeño: puede bastar un README, una estructura sencilla, un diagrama principal, instrucciones de ejecución y pruebas básicas.
- Sistema empresarial: todos los niveles de documentación, QA, seguridad, despliegue y operación.
- Infraestructura: arquitectura, inventario de recursos, configuración, seguridad, despliegue, monitoreo y recuperación.
- Automatización o integración: origen, destino, datos, autenticación, reglas, errores, reintentos, monitoreo y soporte.

Integral no significa complejo.
