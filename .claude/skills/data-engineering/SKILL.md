---
name: data-engineering
description: "Diseña y mantiene pipelines ETL/ELT, modelos y calidad de datos con cargas idempotentes y reprocesables, con herramientas como Airflow o dbt. Usar con pipelines, DAGs o transformaciones."
---

# Data Engineering

## Alcance
Movimiento y transformación de datos analíticos o por lotes. No cubre:
- Esquemas transaccionales y consultas: `database-engineering`.
- Mensajería en tiempo real: `message-queue-engineering`.
- Traslado único entre sistemas: `migration-engineering`.

## Procedimiento
1. Define origen, destino, propietario, frescura esperada, volumen y datos sensibles.
2. Elige carga completa o incremental. Documenta clave única y marca de agua.
3. Diseña cada tarea como una transacción, idempotente: repetirla no duplica datos (usa UPSERT o reemplazo por partición).
4. Parametriza por intervalo lógico; no uses la hora actual en cálculos críticos ni leas "lo más reciente".
5. Añade pruebas de calidad: clave primaria única y no nula, relaciones, rangos, volumen y frescura.
6. Define el reproceso histórico y cómo tratar datos tardíos.
7. Separa entornos de desarrollo y producción.
8. Monitoriza fallos, duración, filas y frescura.

## Airflow
- Sin red, base de datos ni cálculos pesados en el nivel superior del archivo del DAG.
- Sin dependencias del disco local entre tareas; XCom para mensajes pequeños y almacenamiento remoto para datos grandes.
- Credenciales en Connections o un Secrets Backend.

## dbt
Proyecto en Git, cambios revisados por PR, targets `dev` y `prod`, y como mínimo pruebas de clave primaria única y no nula.

## Reglas
- No uses datos personales reales en pruebas sin autorización.
- No ejecutes reprocesos sobre producción sin confirmar alcance y copia de seguridad.
- Declara qué significa exactamente "una vez": la mayoría de los pipelines entregan al menos una vez.

## Verificación
Ejecuta dos veces el mismo intervalo y compara: mismo conteo y misma suma de control. Prueba un fallo intermedio y su recuperación.

## Entrega
Diagrama de flujo, contratos de datos, estrategia de carga, pruebas, operación y limitaciones.

## Ejemplo
Carga diaria de ventas: la tarea reemplaza la partición del día del intervalo, por lo que un reintento no duplica filas. dbt comprueba `venta_id` único y no nulo.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
