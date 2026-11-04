---
name: secure-code-development
description: "Aplica desarrollo seguro al escribir código: validación, consultas parametrizadas, salida segura, manejo de errores y registros. Usar al implementar funciones que procesan entrada o datos sensibles."
---

# Secure Code Development

## Alcance
Decisiones de seguridad mientras se programa. No cubre:
- Auditoría de una app existente: `application-security`.
- Análisis de diseño: `threat-modeling`.
- Autenticación y autorización: `identity-access-management`.
- Credenciales: `secrets-management`.

## Procedimiento
1. Identifica qué entradas cruzan un límite de confianza: HTTP, archivos, colas, terceros y variables.
2. Valida en el servidor con lista de permitidos: sintaxis (tipo y formato) y semántica (sentido para la operación). La validación del cliente es solo comodidad.
3. Separa datos de instrucciones:
   - SQL con consultas parametrizadas.
   - Comandos con listas de argumentos y sin shell.
   - HTML con escape según el contexto.
4. Comprueba autorización en cada operación y objeto, en el servidor.
5. Para archivos: limita tamaño y tipo, genera el nombre en el servidor y evita recorridos de ruta.
6. Para URLs provistas por usuarios: aplica lista de destinos permitidos para limitar SSRF.
7. Maneja errores sin revelar detalles internos; registra eventos de seguridad sin secretos ni datos sensibles.
8. Usa criptografía de bibliotecas mantenidas; no diseñes la tuya.
9. Añade pruebas negativas: entrada maliciosa, acceso de otro usuario y límites.
10. Con código generado por IA, comprueba que cada paquete exista, audita dependencias y revisa el diff completo.

## Reglas
- No uses concatenación para SQL, comandos o HTML.
- No confíes en campos ocultos, cabeceras del cliente o identificadores de la URL.
- No afirmes que un código es seguro: indica qué se comprobó.

## Verificación
Pruebas negativas ejecutadas, analizador estático si existe, y comprobación manual de cada ruta de autorización modificada.

## Entrega
Límites de confianza, controles aplicados, pruebas con resultados y riesgos residuales.

## Ejemplo
```python
# Mal
cur.execute(f"SELECT * FROM pedidos WHERE id = {pedido_id}")
# Bien: parámetro y control del propietario
cur.execute("SELECT * FROM pedidos WHERE id = %s AND usuario_id = %s", (pedido_id, usuario_id))
```

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
