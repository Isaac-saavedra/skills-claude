---
name: typescript-engineering
description: "Diseña tipos seguros y configura tsconfig: modo estricto, genéricos, uniones, narrowing y migración desde JavaScript. Usar ante errores de TypeScript o al modelar tipos."
---

# TypeScript Engineering

## Alcance
El sistema de tipos y la configuración del compilador. No cubre:
- Lógica de runtime en Node: `nodejs-engineering`.
- Componentes: `react-development`.

## Procedimiento
1. Lee `tsconfig.json` y la versión instalada: `npx tsc --version`.
2. Ejecuta `npx tsc --noEmit` y registra la línea base.
3. Modela el dominio para que los estados inválidos no se puedan expresar, con uniones discriminadas.
4. Trata toda entrada externa como `unknown` y valídala en el límite del sistema (API, archivo, variable de entorno). Un tipo no comprueba nada en runtime.
5. Estrecha con guardas de tipo o comprobaciones; evita `as` para silenciar errores.
6. Añade genéricos solo cuando relacionen tipos de entrada y salida.
7. Vuelve a ejecutar el compilador y las pruebas.

## Configuración
- Nuevo proyecto: activa `strict`.
- Considera `noUncheckedIndexedAccess` y `exactOptionalPropertyTypes`: no forman parte de `strict`.
- Elige las opciones de módulos según dónde corre el código y confírmalas en la guía oficial de módulos.
- Migración: activa opciones una a una y corrige por módulos; no bajes `strict` para ocultar errores.

## Reglas
- Evita `any`. Si es inevitable, confínalo y explica por qué.
- `as unknown as T` y `@ts-ignore` requieren justificación. Prefiere `@ts-expect-error`, que avisa cuando ya no es necesario.
- No dupliques tipos que pueden derivarse.

## Verificación
`tsc --noEmit` sin errores nuevos, pruebas ejecutadas y ningún `any` o aserción añadidos sin justificar.

## Entrega
Tipos modificados, cambios de configuración, salida del compilador antes y después, y riesgos.

## Ejemplo
```ts
type Resultado =
  | { estado: "ok"; datos: Pedido }
  | { estado: "error"; mensaje: string };

function mostrar(r: Resultado) {
  if (r.estado === "ok") return r.datos.id;
  return r.mensaje;
}
```

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
