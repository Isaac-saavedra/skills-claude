---
name: microservices-engineering
description: "Evalúa, separa y coordina microservicios: límites, datos por servicio, sagas, outbox, comunicación y operación. Usar al decidir partir un monolito o ante fallos entre servicios."
---

# Microservices Engineering

## Alcance
Sistemas compuestos por servicios independientes. No cubre:
- Arquitectura general o elección de estilo: `software-architecture`.
- Detalle de brokers: `message-queue-engineering`.
- Despliegue en clúster: `kubernetes-engineering`.

## Procedimiento
1. Cuestiona la necesidad. Pregunta qué problema actual resuelve y si un monolito modular basta. Un monolito es una opción legítima.
2. Comprueba prerrequisitos: CI/CD automatizado, observabilidad, despliegues independientes y equipos con responsabilidad clara.
3. Delimita por capacidades de negocio, no por capas técnicas.
4. Asigna a cada servicio sus datos. Prohíbe el acceso directo a la base de otro servicio.
5. Elige la comunicación: síncrona si la respuesta es imprescindible, asíncrona para desacoplar.
6. Coordina consistencia con sagas y compensaciones; usa outbox para publicar de forma fiable.
7. Define en cada llamada: timeout, reintentos limitados, idempotencia y comportamiento degradado.
8. Instrumenta con trazas y correlación entre servicios.
9. Versiona contratos y prueba su compatibilidad.
10. Para separar un monolito, extrae de forma incremental con estrangulamiento.

## Sagas
Coreografía: los servicios reaccionan a eventos. Orquestación: un coordinador da las órdenes. No hay rollback automático ni aislamiento ACID: diseña las compensaciones y contramedidas para anomalías.

## Reglas
- No uses 2PC ni transacciones distribuidas sin justificar la decisión.
- No inventes objetivos de disponibilidad o escala. Pídelos o márcalos por confirmar.
- Evita un "monolito distribuido": servicios que deben desplegarse juntos.

## Verificación
Despliegue independiente de un servicio, prueba de contrato, fallo inyectado en una dependencia y compensación de saga ejecutada.

## Entrega
Evaluación con la opción de no separar, límites, propiedad de datos, comunicación, coordinación, plan incremental, operación y riesgos.

## Ejemplo
Pedido → pago → inventario. Si inventario falla, la saga ejecuta `reembolsarPago` y marca el pedido como `cancelado`. Cada paso publica sus eventos mediante outbox.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
