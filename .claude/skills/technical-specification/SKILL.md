---
name: technical-specification
description: "Redacta especificaciones técnicas y documentos de diseño: objetivos, propuesta, alternativas, contratos, datos, riesgos y despliegue. Usar antes de implementar una funcionalidad o sistema importante."
---

# Technical Specification

## Alcance
Cómo se construirá algo concreto, antes de construirlo. No cubre:
- Qué se debe construir: `requirements-engineering`.
- Documentar la arquitectura global: `architecture-documentation`.
- Otros documentos técnicos generales: `technical-documentation`.

## Procedimiento
1. Lee los requisitos y el código afectado. No diseñes sobre un sistema imaginado.
2. Escribe el problema y los objetivos, y también los **no objetivos**.
3. Describe la solución: componentes, flujo, contratos, modelo de datos y errores.
4. Expón alternativas reales y por qué se descartaron.
5. Cubre aspectos transversales: seguridad, privacidad, rendimiento, observabilidad, compatibilidad, migración y reversión.
6. Divide la implementación en fases con entregables.
7. Enumera preguntas abiertas con responsable.
8. Solicita revisión de las personas afectadas.

## Plantilla
```markdown
# Título
Estado: Borrador | Autor: Por confirmar | Fecha: Por confirmar
## Contexto
## Objetivos y no objetivos
## Propuesta
## Alternativas consideradas
## Seguridad y privacidad
## Observabilidad y operación
## Migración y reversión
## Plan de entrega
## Preguntas abiertas
```

## Reglas
- Proporcional: un cambio pequeño no necesita diez páginas.
- Etiqueta supuestos. No inventes cifras de carga, costes o resultados de pruebas.
- Si una sección no aplica, indícalo con una frase justificada.
- Actualiza el estado cuando la implementación se desvíe.

## Verificación
Un desarrollador ajeno puede descomponer el trabajo sin preguntas básicas; los nombres citados existen en el código; cada requisito tiene su parte en el diseño.

## Entrega
Documento completo, supuestos, decisiones pendientes y siguiente paso de revisión.

## Ejemplo
No objetivo: "Esta versión no admite importación por lotes". Alternativa descartada: "WebSockets: la actualización cada minuto no justifica mantener conexiones". Reversión: "Desactivar `feature_x`; las columnas nuevas siguen siendo compatibles".

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
