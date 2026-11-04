---
name: observability-engineering
description: "Instrumenta logs, métricas y trazas con OpenTelemetry o Prometheus, y diseña paneles y alertas útiles. Usar al añadir telemetría, reducir ruido de alertas o diagnosticar puntos ciegos."
---

# Observability Engineering

## Alcance
Telemetría y alertas. No cubre:
- Definir SLO y presupuestos de error: `reliability-engineering`.
- Dirigir una crisis: `incident-response`.

## Procedimiento
1. Parte de preguntas operativas: "¿Están fallando los usuarios?", "¿Qué dependencia lo causa?".
2. Revisa lo existente antes de añadir herramientas.
3. Instrumenta los recorridos críticos:
   - **Trazas** para el camino entre servicios.
   - **Métricas** para tasas, errores, latencia y saturación.
   - **Logs** estructurados con identificadores de correlación.
4. Usa convenciones semánticas de OpenTelemetry si el proyecto lo usa.
5. Nombra métricas de Prometheus con prefijo de dominio, una unidad base y sufijo (`http_request_duration_seconds`, `http_requests_total`).
6. Controla la cardinalidad: cada combinación de etiquetas es una serie. Sin IDs de usuario ni correos.
7. Elimina datos sensibles antes de exportar.
8. Alerta por síntomas que sufre el usuario, en el nivel más alto posible de la pila.
9. Cada alerta debe ser accionable y enlazar a una consola o a su procedimiento.

## Reglas
- Menos alertas es mejor; si nadie debe actuar, no despiertes a nadie.
- Usa percentiles para latencia en lugar del promedio.
- No registres secretos, tokens ni datos personales innecesarios.
- Estima coste y retención antes de ampliar la telemetría.

## Verificación
Genera tráfico y un fallo de prueba: la traza aparece completa, la métrica cambia y la alerta se dispara y se resuelve. Comprueba la ausencia de datos sensibles.

## Entrega
Señales añadidas, paneles, alertas, coste o cardinalidad estimados como tal, pruebas y puntos ciegos.

## Ejemplo
Métrica: `http_request_duration_seconds` con etiquetas `route`, `method` y `status_class`, y no con la URL completa o `user_id`. Alerta sobre el error percibido por el usuario, no sobre CPU alta.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
