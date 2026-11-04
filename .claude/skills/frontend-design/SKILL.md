---
name: frontend-design
description: "Diseña e implementa interfaces web modernas y responsive con componentes reutilizables. Usar siempre al crear o rediseñar páginas, dashboards, formularios o prototipos."
---

# Frontend Design

## Alcance
**No cubre:** Lógica de componentes React: `react-development`. Evaluación de usabilidad: `ui-ux-engineering`. Auditoría WCAG: `web-accessibility`.

## Objetivo
Crear interfaces originales, claras, consistentes, accesibles y útiles. La estética debe apoyar la tarea del usuario y no ocultar problemas funcionales.

## Antes de diseñar
1. Inspecciona el framework, sistema de estilos, componentes y dependencias existentes.
2. Identifica usuarios, tareas principales, contenido, estados y dispositivos objetivo.
3. Respeta identidad visual y componentes existentes. Si no hay guía, propone una paleta y tipografía coherentes.
4. Evita agregar librerías sin justificar su necesidad.

## Diseño
- Establece jerarquía visual, espaciado, tipografía, contraste y estados.
- Diseña primero el flujo principal; contempla carga, error, vacío, éxito y permisos insuficientes.
- Usa layouts responsive y evita anchos rígidos innecesarios.
- Usa HTML semántico, navegación por teclado, foco visible, etiquetas y mensajes comprensibles.
- Mantén componentes reutilizables sin fragmentar en exceso.
- Evita texto de relleno, datos ficticios presentados como reales y controles decorativos sin acción.
- Los gráficos deben indicar unidades, periodos, fuentes y tratamiento de datos.
- No uses color como único indicador de estado.

## Implementación
1. Crea o adapta tokens de diseño cuando convenga.
2. Implementa componentes pequeños con responsabilidades claras.
3. Verifica contraste, teclado, tamaños de pantalla y estados.
4. Ejecuta pruebas visuales o funcionales disponibles.
5. Comprueba consola, errores de red y build si las herramientas lo permiten.

## Entrega
Describe decisiones de UX, componentes creados, responsive, accesibilidad, pruebas realizadas y cualquier dependencia añadida. No afirmes cumplimiento total de WCAG sin una auditoría suficiente.

## Verificación
Revisa en navegador, a ancho móvil y de escritorio, los estados de carga, vacío, error y éxito. Comprueba teclado, foco visible y contraste (4,5:1 en texto normal).

## Ejemplo
Panel de ventas: jerarquía con tres indicadores clave, gráfico con unidades y periodo, tabla en una columna en móvil, y datos de ejemplo identificados como tales.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
