# Documentación de un proyecto por público

No limites la documentación al README ni a lo técnico. Cada público necesita su documento; no los mezcles en uno solo.

| Público | Contenido | Forma |
|---|---|---|
| Ejecutiva (gerencia) | Qué es, qué problema resuelve, objetivos, alcance y exclusiones, cómo funciona para el negocio, beneficios esperados o medidos, estado, indicadores, riesgos, dependencias, decisiones pendientes y siguientes pasos | Lenguaje de negocio, sin jerga, código ni nombres de servicios salvo que importen para una decisión. Presentación breve y visual, con documento de consulta si hace falta |
| Funcional (analistas y negocio) | Procesos, actores, reglas de negocio, precondiciones, excepciones, estados, resultados y casos de uso | Flujos y reglas trazables |
| Manuales de usuario | Tareas concretas con pasos claros, pantallas y campos reales, resultados esperados, errores frecuentes y soporte | Ver `user-manual-creation` |
| Técnica (desarrollo y TI) | Arquitectura, componentes, estructura, instalación y ejecución local, configuración, APIs, integraciones, modelo de datos y migraciones, seguridad y secretos, infraestructura, despliegue y operación | Ver las Skills de documentación específicas |
| QA | Estrategia, escenarios, casos de prueba, criterios de aceptación, datos de prueba, resultados y evidencias | Trazable a requisitos |
| Despliegue, operación y traspaso | Verificación, rollback, monitoreo, respaldos, incidentes, estado actual, riesgos, deuda técnica y pendientes | Ver `deployment-documentation` |

## Reglas

- Una fuente coherente y trazabilidad entre requisitos, procesos, implementación, pruebas y manuales.
- Documenta solo lo que existe y está comprobado. Distingue funciones implementadas, parciales, heredadas, deshabilitadas y planificadas.
- Si el proyecto tiene reglas propias sobre su documentación (por ejemplo, no tocar documentos heredados), prevalecen.

## Estructura sugerida

Adáptala al proyecto y no crees carpetas vacías:

```text
docs/
├── 00-general/
├── 01-arquitectura/
├── 02-documentacion-funcional/  (procesos, reglas-negocio, flujos, casos-de-uso)
├── 03-documentacion-tecnica/    (desarrollo, backend, frontend, base-datos, integraciones, seguridad, infraestructura)
├── 04-manuales-usuario/
├── 05-qa-y-pruebas/
├── 06-despliegue-y-operaciones/
├── 07-documentacion-ejecutiva/
└── 08-traspaso/
```

Los diagramas de cada sección se crean con `diagramming`.
