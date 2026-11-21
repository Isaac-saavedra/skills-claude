---
name: diagramming
description: "Crea diagramas editables y verificados: archivos .drawio de draw.io, Mermaid y BPMN 2.0, técnicos o de negocio, contrastados con el código real. Usar al dibujar arquitectura, flujos, procesos, swimlanes, secuencias o modelos de datos."
---

# Diagramming

## Alcance
Producir el archivo del diagrama y validarlo. No cubre:
- Decidir la arquitectura: `software-architecture`.
- Redactar la documentación arquitectónica completa (arc42, ADR): `architecture-documentation`.

## Herramienta según el caso
- **draw.io (`.drawio`)**: principal. Editable, se versiona junto al código en `docs/`, organizado por categoría. Si existe la integración de draw.io (plugin o conector), úsala; si no, escribe el XML.
- **Mermaid**: diagramas sencillos o secuencias que conviene versionar como texto. GitHub los muestra en Markdown dentro de un bloque `mermaid`.
- **BPMN 2.0**: procesos de negocio que requieren notación formal (eventos, compuertas, carriles).
- Exporta a PNG, SVG o PDF solo si hace falta, idealmente con los datos del diagrama incrustados para que siga siendo editable. La exportación no reemplaza al editable.

## Procedimiento
1. Define propósito, público y alcance. Un diagrama, una pregunta: no metas todo el sistema en uno.
2. Inspecciona código, configuración y documentación. Identifica componentes, actores, servicios, datos, integraciones y puntos de entrada reales.
3. Comprueba cada relación en una fuente concreta. No deduzcas conexiones por el nombre de un archivo.
4. Marca lo parcial, heredado o planificado distinto de lo implementado; lo no verificable, como "pendiente de validación" o fuera.
5. Separa diagramas funcionales y técnicos: el analista entiende el proceso sin la infraestructura y el desarrollador las interacciones sin inferir reglas de negocio.
6. Dibuja y acompaña cada diagrama con propósito, alcance, fuentes revisadas (archivos o módulos) y fecha.

## Tipos
- Técnicos: contexto, contenedores o componentes, infraestructura, integraciones, secuencia y entidad-relación verificado.
- Negocio: flujograma, swimlane por responsable, BPMN, actividad y flujo de excepciones.

## Reglas de contenido
- **Flujos funcionales**: inicio y fin, actores, actividades en orden, decisiones con su condición escrita, caminos alternativos, validaciones, errores, recuperación y resultado. En swimlanes, cada actividad en el carril de quien la ejecuta.
- **Técnicos**: orden correcto de las interacciones; distingue llamadas síncronas, eventos, colas y procesos asíncronos; marca límites de confianza y servicios externos; incluye persistencia y manejo de errores cuando forman parte del flujo; no confundas recursos de infraestructura con código.
- Nunca secretos, credenciales ni datos personales en un diagrama.

## Calidad visual
Título descriptivo y leyenda cuando haga falta; agrupación por responsabilidad, dominio, entorno o participante; iconos oficiales del proveedor cuando existan (para AWS, la biblioteca vigente; la propia página de AWS advierte de conjuntos heredados); conexiones etiquetadas con el protocolo o evento comprobado; sin cruces innecesarios ni textos pequeños; divide lo grande. No comuniques diferencias importantes solo con color o forma.

## Verificación
- El `.drawio` es XML válido (por ejemplo, `python3 -c "import xml.dom.minidom,sys; xml.dom.minidom.parse(sys.argv[1])" archivo.drawio`) y abre en diagrams.net. Si no puedes abrirlo, di que solo validaste el XML.
- En Mermaid, el diagrama se renderiza sin error (vista previa o el visor de GitHub).
- Cada elemento y conexión tiene su fuente en el código, la configuración o una regla de negocio confirmada.
- Cuando cambie una funcionalidad, revisa qué diagramas afecta; no declares uno actualizado sin volver a contrastarlo.

## Entrega
Primero un inventario breve de diagramas recomendados con propósito y público; después los de mayor valor, con su ubicación, lo verificado y lo que quedó pendiente.

## Ejemplo
Inventario para un módulo de pedidos con API y cola: (1) contexto, para gerencia; (2) secuencia "crear pedido", para desarrollo, en `docs/01-arquitectura/secuencia-pedido.drawio`; (3) swimlane del proceso de devolución, para analistas. La conexión "worker → pasarela de pagos" se etiqueta "HTTPS, POST /charges" porque así figura en el cliente de pagos del código.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
