---
name: user-manual-creation
description: "Redacta manuales y guías para usuarios finales no técnicos, con tareas paso a paso, lenguaje claro y resolución de problemas. Usar para ayudas, manuales de un sistema o capacitación."
---

# User Manual Creation

## Alcance
Documentación para quien usa el producto. No cubre:
- Instalación técnica: `installation-guides`.
- Documentación para desarrolladores: `technical-documentation` o `api-documentation`.

## Procedimiento
1. Define el lector, sus conocimientos y qué necesita lograr.
2. Obtén el comportamiento real: usa el sistema, sus capturas o sus pruebas. Lo que no pudiste comprobar queda marcado.
3. Ordena por tareas del usuario, no por pantallas o módulos internos.
4. Separa tipos: tutorial para aprender, guía para resolver un objetivo, referencia para consultar y explicación para comprender.
5. Escribe cada procedimiento:
   - Título con el objetivo.
   - Antes de empezar: permisos y datos.
   - Pasos numerados, con una acción por paso, imperativo y lugar antes de la acción.
   - Resultado esperado después de la acción.
6. Usa los mismos nombres que aparecen en la interfaz.
7. Añade errores frecuentes: síntoma, causa probable y solución.
8. Añade glosario solo si es necesario.
9. Haz que imágenes y tablas sean accesibles, con texto alternativo y sin información solo por color.

## Reglas
- No inventes pantallas, botones, rutas, resultados ni capturas. Marca "Por confirmar".
- Oraciones breves y términos comunes. Explica la jerga o elimínala.
- Oculta datos personales reales de las capturas.
- Avisa antes de una acción irreversible.

## Verificación
Sigue cada procedimiento desde cero en el sistema real o pide a alguien que lo haga. Registra lo que no pudo ser comprobado.

## Entrega
Manual, control de versión, sistema y versión documentados, procedimientos comprobados y pendientes.

## Ejemplo
```markdown
## Crear una factura
Antes de empezar: necesitas permiso de Facturación.

1. En el menú principal, selecciona **Facturas > Nueva**.
2. En **Cliente**, escribe el nombre y selecciónalo de la lista.
3. Haz clic en **Guardar**. La factura aparece con el estado *Borrador*.
```

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
