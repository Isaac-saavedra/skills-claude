---
name: react-development
description: "Construye y corrige componentes React: hooks, estado, efectos, rendimiento y pruebas, según las reglas oficiales. Usar siempre con JSX/TSX, useEffect, bucles de render o errores de hooks."
---

# React Development

## Alcance
Código React. No cubre:
- Dirección visual y maquetación: `frontend-design`.
- Experiencia de usuario: `ui-ux-engineering`.
- Accesibilidad detallada: `web-accessibility`.

## Procedimiento
1. Inspecciona la versión de React, framework, enrutado, gestor de estado, estilos y pruebas. Sigue lo existente.
2. Modela el estado mínimo. Calcula durante el render lo que se pueda derivar de props o estado.
3. Coloca el estado en el ancestro común más cercano. Añade un gestor global solo con una necesidad comprobada.
4. Escribe componentes puros: mismas props, estado y contexto producen la misma salida.
5. Usa efectos solo para sincronizar con sistemas externos. Si conecta o suscribe, devuelve una limpieza.
6. Deriva las dependencias del código del efecto; no las elijas para controlar cuándo corre.
7. Maneja estados de carga, vacío, error y éxito.
8. Prueba desde la perspectiva del usuario, con selectores accesibles.
9. Activa `eslint-plugin-react-hooks` y corrige sus avisos.

## Reglas de React
- Sin efectos secundarios durante el render.
- Props, estado, valores de hooks y valores pasados a JSX son inmutables.
- No llames componentes como funciones; úsalos en JSX.
- Llama hooks en el nivel superior de componentes o hooks propios, nunca en bucles o condiciones.
- Si Strict Mode revela un doble montaje con errores, implementa la limpieza; no lo evites con refs.

## Antipatrones frecuentes
- `setState` síncrono en un efecto para derivar datos: calcula durante el render.
- `key={index}` en listas que se reordenan.
- `useMemo` o `memo` sin medición.
- Suprimir `exhaustive-deps` sin una razón escrita.

## Verificación
Linter y tipos sin errores nuevos, pruebas ejecutadas, comprobación en navegador de carga, vacío y error, y consola sin avisos de React.

## Entrega
Componentes modificados, decisiones de estado, pruebas con resultados reales y limitaciones.

## Ejemplo
```jsx
// Antes: render extra y estado duplicado
useEffect(() => { setSeleccionado(items.find(i => i.id === id)); }, [items, id]);

// Después: derivado durante el render
const seleccionado = items.find(i => i.id === id);
```

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
