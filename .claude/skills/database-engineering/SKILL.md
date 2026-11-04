---
name: database-engineering
description: "Modela, consulta y optimiza bases de datos: esquemas, SQL, índices, migraciones de esquema y planes de ejecución. Usar siempre con consultas lentas, EXPLAIN o diseño de tablas."
---

# Database Engineering

## Alcance
**No cubre:** Traslado entre motores o sistemas: `migration-engineering`. Pipelines: `data-engineering`.

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

## Verificación
Compara el plan de ejecución antes y después, en datos representativos. Prueba migraciones de ida y vuelta fuera de producción. En PostgreSQL, tras `CREATE INDEX CONCURRENTLY` comprueba que el índice no quedó `INVALID`.

## Ejemplo
Índice en tabla activa de PostgreSQL: `CREATE INDEX CONCURRENTLY` no bloquea escrituras, pero tarda más y no corre dentro de una transacción. Si falla, elimina el índice inválido y repite.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
