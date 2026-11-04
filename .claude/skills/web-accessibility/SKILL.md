---
name: web-accessibility
description: "Audita y corrige accesibilidad web según WCAG 2.2: teclado, foco, contraste, formularios, ARIA y lector de pantalla. Usar al revisar la conformidad AA o corregir barreras de acceso."
---

# Web Accessibility

## Alcance
Accesibilidad de contenido e interfaces web. No cubre:
- Usabilidad general: `ui-ux-engineering`.
- Asesoría legal de cumplimiento.

## Procedimiento
1. Confirma el nivel objetivo (normalmente AA) y qué páginas o flujos entran en la revisión.
2. Ejecuta una herramienta automática como primer filtro. Detecta solo parte de los problemas: no concluyas "accesible" con su resultado.
3. Prueba manualmente con teclado: orden lógico, foco visible (2.4.7, AA) y sin trampas.
4. Revisa estructura: títulos en orden, puntos de referencia, HTML semántico y `lang`.
5. Comprueba contraste: 4,5:1 para texto normal y 3:1 para texto grande (AA).
6. Revisa formularios: etiquetas asociadas e identificación de errores en texto (3.3.1, nivel A).
7. Comprueba tamaños de objetivo: 24 × 24 px CSS como mínimo AA, con excepciones.
8. Comprueba arrastres: debe existir alternativa sin arrastrar.
9. Comprueba con un lector de pantalla los flujos clave e indica cuál y versión.
10. Usa ARIA solo si el HTML nativo no basta; sigue los patrones de la guía APG.

## Novedades de WCAG 2.2
Criterios nuevos: 2.4.11, 2.5.7, 2.5.8 y 3.3.8 (AA); 3.2.6 y 3.3.7 (A); 2.4.12, 2.4.13 y 3.3.9 (AAA). El criterio 4.1.1 Parsing se eliminó.

## Reglas
- No declares conformidad WCAG tras una revisión parcial o automática; indica el alcance real.
- Cita el criterio exacto de cada hallazgo y comprueba su texto en la referencia rápida.
- No uses un `div` con `onClick` donde corresponde un `button`.

## Verificación
Flujo completo con teclado, cada corrección comprobada otra vez y herramientas, navegadores y lectores usados registrados.

## Entrega
Alcance, método, hallazgos (criterio, nivel, impacto, ubicación, corrección), elementos corregidos, pendientes y lo no probado.

## Ejemplo
Hallazgo: icono de cerrar de 16 × 16 px sin nombre accesible. Criterios: 2.5.8 (revisar excepciones) y 4.1.2. Corrección: `<button aria-label="Cerrar">` con área de 24 × 24 px.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
