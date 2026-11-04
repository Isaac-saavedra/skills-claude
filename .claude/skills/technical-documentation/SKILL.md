---
name: technical-documentation
description: "Crea y mantiene documentación técnica profesional, clara y verificable para software, APIs, infraestructura y operaciones. Úsala para README, manuales, especificaciones, ADR, runbooks, informes y documentación de usuario."
---

# Technical Documentation

## Objetivo
Entregar documentación profesional, utilizable y alineada con el sistema real. La documentación es parte del producto, no un añadido opcional.

## Regla de veracidad
- Documenta únicamente comportamientos comprobados en el código, configuración, pruebas o fuentes citadas.
- No inventes comandos, capturas, endpoints, variables, resultados, responsables, fechas ni requisitos.
- Marca claramente los datos pendientes como `Por confirmar`.
- Distingue procedimiento probado de procedimiento propuesto.
- Verifica que los comandos y rutas correspondan al sistema operativo y versión indicados.
- No incluyas secretos, tokens, datos personales ni información interna innecesaria.

## Proceso
1. Identifica audiencia: desarrolladores, operadores, administradores, usuarios o responsables.
2. Define propósito, alcance, prerrequisitos y nivel técnico.
3. Inspecciona repositorio, configuración, contratos, pruebas y documentación previa.
4. Organiza el contenido de lo general a lo específico.
5. Incluye pasos numerados, comandos completos, ejemplos, resultados esperados y recuperación.
6. Añade diagramas Mermaid cuando aclaren arquitectura, secuencias o procesos.
7. Incluye tablas de variables, endpoints, permisos, errores y compatibilidad cuando corresponda.
8. Revisa consistencia entre documentación y comportamiento implementado.
9. Actualiza README, changelog y guías afectadas junto con el cambio de software.
10. Entrega una lista de verificaciones y asuntos pendientes.

## Documentos que puedes producir

### README profesional
- Nombre y propósito.
- Características reales.
- Stack y versiones verificadas.
- Requisitos previos.
- Instalación y configuración.
- Variables de entorno usando `.env.example` sin secretos.
- Ejecución local.
- Pruebas.
- Despliegue.
- Estructura del proyecto.
- Solución de problemas.
- Licencia y contribución, si se conocen.

### Manual técnico
- Portada, versión, fecha y estado del documento.
- Objetivo, alcance y audiencia.
- Arquitectura y componentes.
- Requisitos y prerrequisitos.
- Instalación y configuración paso a paso.
- Operación y mantenimiento.
- Seguridad, backups y recuperación.
- Diagnóstico de errores.
- Anexos y referencias.

### Manual de usuario
- Objetivo y audiencia.
- Requisitos de acceso.
- Navegación.
- Procedimientos por tarea.
- Capturas reales si están disponibles.
- Mensajes y errores frecuentes.
- Preguntas frecuentes y soporte.

### API / especificación
- Propósito, autenticación y autorización.
- Base URL por entorno si se conoce.
- Endpoints y métodos.
- Parámetros y esquemas.
- Ejemplos coherentes con el contrato.
- Códigos de respuesta y errores.
- Paginación, límites y versionado.

### Runbook operativo
- Síntoma y alcance.
- Impacto.
- Comprobaciones previas.
- Diagnóstico paso a paso.
- Mitigación y recuperación.
- Validación posterior.
- Escalamiento y rollback.
- Riesgos y permisos requeridos.

### ADR
- Título, estado y fecha confirmada.
- Contexto.
- Decisión.
- Alternativas consideradas.
- Consecuencias y riesgos.

## Calidad editorial
- Español claro y profesional, salvo que se solicite otro idioma.
- Títulos consistentes, numeración estable y términos definidos.
- Explica siglas la primera vez.
- Evita párrafos excesivos y redundancias.
- Usa tablas para información comparable.
- Usa bloques de código con lenguaje indicado.
- Añade índice si el documento es extenso.
- Mantén tono objetivo y evita marketing no sustentado.

## Archivos de salida
Cuando el usuario solicite un archivo, utiliza las herramientas disponibles para generar el formato solicitado (Markdown, DOCX, PDF, XLSX, PPTX, etc.). No afirmes que el archivo existe hasta haberlo creado y verificado. Si no puedes generar un formato, entrega una alternativa editable y explica la limitación.

## Control final
Antes de entregar, comprueba:
- ¿El documento refleja el sistema real?
- ¿Cada comando tiene contexto y resultado esperado?
- ¿Las versiones y fechas están confirmadas?
- ¿Los riesgos y prerrequisitos están claros?
- ¿Se eliminaron secretos y datos sensibles?
- ¿Se distinguen hechos de pendientes?
- ¿La audiencia puede ejecutar las instrucciones sin adivinar?

## Entregable
Incluye el documento completo y un breve resumen de archivos creados/actualizados, fuentes consultadas, verificaciones realizadas y pendientes.
