---
name: message-queue-engineering
description: "Diseña productores y consumidores con RabbitMQ o Kafka: entrega, reintentos, idempotencia, orden y colas de error. Usar ante mensajes duplicados, perdidos, lag o procesamiento asíncrono."
---

# Message Queue Engineering

## Alcance
Mensajería entre procesos. No cubre:
- Reparto de un sistema en servicios: `microservices-engineering`.
- Integración con APIs de terceros: `system-integration`.

## Procedimiento
1. Define por qué hace falta asincronía, garantías requeridas, volumen y requisitos de orden.
2. Elige con esta regla: RabbitMQ para colas de trabajo y enrutamiento; Kafka para registro de eventos reproducible a gran escala. Confirma frente a lo que ya exista en el proyecto.
3. Asume entrega **al menos una vez** y haz cada consumidor idempotente con un identificador de mensaje.
4. Si la base de datos y el mensaje deben ser coherentes, aplica outbox transaccional.
5. Define reintentos con límite y retroceso, y una cola de mensajes fallidos con dueño y proceso de reproceso.
6. Versiona el esquema del mensaje de forma compatible.
7. Monitoriza profundidad o lag, antigüedad del mensaje más viejo, reintentos y errores.

## RabbitMQ
- Publisher confirms y acks del consumidor; sin ellos la entrega es como máximo una vez.
- Confirma el mensaje solo después de procesarlo.
- Colas durables o replicadas (quorum) y mensajes persistentes para no perder datos.
- `redelivered` solo indica una posible repetición.

## Kafka
- El orden solo se garantiza dentro de una partición: elige bien la clave.
- El productor idempotente evita duplicados de reenvío en el log, no los de tu lógica de negocio.
- Exactly-once requiere productor transaccional y consumidor `read_committed` o Kafka Streams, y se limita a lo que está en Kafka.

## Reglas
- No afirmes "exactly once" de extremo a extremo con efectos externos sin idempotencia.
- No purgues colas ni reinicies offsets en producción sin autorización.
- No pongas datos sensibles en mensajes sin evaluar retención y acceso.

## Verificación
Prueba con duplicados, consumidor caído antes del ack, mensaje venenoso y reinicio del broker. Debe quedar sin efecto duplicado ni pérdida silenciosa.

## Entrega
Topología, garantías, esquema, reintentos, operación, pruebas y riesgos.

## Ejemplo
Consumidor de pagos: guarda `message_id` y el efecto en una sola transacción; si llega un duplicado, confirma sin repetir el cobro. Tras cinco fallos, el mensaje va a la cola de error y genera alerta.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
