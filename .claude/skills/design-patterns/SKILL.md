---
name: design-patterns
description: "Selecciona y aplica patrones de diseño (Strategy, Adapter, Factory, Observer, Repository) solo cuando resuelven un problema real. Usar siempre que se pregunte qué patrón aplicar o cómo estructurar clases."
---

# Design Patterns

## Alcance
Decisiones de diseño dentro de un módulo o servicio. No cubre:
- Arquitectura de sistema: `software-architecture`.
- Patrones distribuidos como saga u outbox: `microservices-engineering`.
- Reestructurar sin cambiar comportamiento: `refactoring`.

## Procedimiento
1. Describe el problema en términos del código actual: duplicación, condicionales que crecen, acoplamiento a un proveedor.
2. Comprueba si el lenguaje o framework ya lo resuelve (funciones, interfaces, inyección de dependencias).
3. Evalúa primero la solución más simple. Exige un patrón solo si esa solución falla ante un cambio concreto y previsible.
4. Compara como máximo dos o tres candidatos usando la tabla.
5. Implementa el mínimo con nombres del dominio y añade pruebas del comportamiento.
6. Documenta en una línea por qué se eligió y qué alternativa se descartó.

## Tabla de selección
| Señal | Patrón candidato |
|---|---|
| `switch` por tipo de algoritmo que crece | Strategy |
| Librería externa con interfaz incompatible | Adapter |
| Construcción compleja o dependiente del entorno | Factory |
| Varios interesados reaccionan a un cambio | Observer |
| Añadir comportamiento sin tocar la clase | Decorator |
| Fachada simple sobre un subsistema complejo | Facade |
| Separar dominio y persistencia | Repository |

## Reglas
- No introduzcas un patrón por anticipación sin un segundo caso real o inminente.
- Evita Singleton con estado global: dificulta las pruebas.
- No crees interfaces con una sola implementación salvo que el límite lo justifique, como un proveedor externo o una prueba.
- Sigue la convención del proyecto aunque exista otra opción aceptable.

## Verificación
Las pruebas siguen pasando, el cambio previsto requiere menos archivos que antes y un revisor entiende el código sin conocer el nombre del patrón.

## Entrega
Problema, alternativas, patrón elegido o decisión de no usar ninguno, código, pruebas y compromisos.

## Ejemplo
Tres proveedores de pago en un `if/else`: Strategy con una interfaz `cobrar()`, y Adapter para el SDK incompatible. Con un único proveedor sin cambio previsto, la recomendación es no aplicar ningún patrón.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
