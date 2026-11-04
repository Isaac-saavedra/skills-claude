# Reglas del proyecto para Claude Code

## Veracidad
- No inventes hechos, comandos, resultados de pruebas, versiones, archivos ni fuentes.
- Inspecciona el repositorio antes de editar.
- Si falta información que cambia la solución, pregunta o marca el supuesto explícitamente.
- Investiga en documentación oficial cuando la respuesta dependa de versiones, APIs, seguridad o servicios actuales.
- Distingue hechos comprobados, hipótesis y recomendaciones.

## Cambios
- Conserva las convenciones y arquitectura existentes.
- Realiza cambios pequeños y revisables.
- No sobrescribas cambios del usuario.
- No ejecutes acciones destructivas, migraciones productivas, despliegues, force push o eliminación de datos sin autorización explícita.
- No introduzcas secretos en el repositorio.

## Calidad
- Añade o actualiza pruebas para los cambios.
- Ejecuta las comprobaciones disponibles y reporta los comandos y resultados reales.
- No afirmes que algo funciona si no se ha validado.
- Considera seguridad, accesibilidad, rendimiento y mantenibilidad.

## Documentación obligatoria
- Actualiza README, documentación técnica, ejemplos de configuración y changelog cuando el cambio lo requiera.
- Documenta prerrequisitos, instalación, configuración, uso, pruebas, despliegue, recuperación y limitaciones.
- No inventes endpoints, variables, resultados, capturas, responsables o fechas.
- Marca la información pendiente como “Por confirmar”.

## Entrega
Resume qué cambió, por qué, archivos afectados, pruebas realizadas, resultados, riesgos, limitaciones y próximos pasos.
