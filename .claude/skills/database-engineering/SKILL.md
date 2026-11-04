---
name: database-engineering
description: "Diseña, consulta, migra y optimiza bases de datos relacionales y NoSQL. Úsala al modelar esquemas, escribir SQL, revisar índices, planificar migraciones o diagnosticar problemas de persistencia."
---

# Database Engineering

## Análisis inicial
1. Identifica motor, versión, esquema, volumen conocido, patrones de acceso y criticidad.
2. Inspecciona migraciones y convenciones existentes.
3. No asumas cardinalidades, volumen o distribución de datos que no se hayan proporcionado.
4. Define integridad, consistencia, retención, privacidad y recuperación.

## Modelado
- Define entidades, claves, relaciones, restricciones y nulabilidad explícitamente.
- Normaliza por defecto en sistemas relacionales; desnormaliza con justificación basada en consultas y mediciones.
- Diseña índices según consultas reales; evalúa costo de escritura y almacenamiento.
- En NoSQL, diseña alrededor de patrones de acceso y límites del motor.
- Define tipos adecuados, zonas horarias y tratamiento de dinero/decimales.

## SQL y rendimiento
- Usa consultas parametrizadas.
- Evita SELECT * en consultas de producción cuando no sea apropiado.
- Analiza planes de ejecución antes de afirmar que un índice mejorará rendimiento.
- Considera bloqueos, transacciones, aislamiento y concurrencia.
- Evita consultas N+1 y cargas innecesarias.

## Migraciones
1. Describe el cambio y su compatibilidad.
2. Incluye respaldo, validación previa y estrategia de rollback.
3. Evalúa bloqueos, duración y despliegue gradual.
4. No ejecutes operaciones destructivas sin confirmación explícita.
5. Proporciona scripts repetibles y seguros cuando sea posible.

## Entrega
Incluye diagrama o descripción del modelo, DDL/migración, índices justificados, consultas de validación y riesgos operativos.
