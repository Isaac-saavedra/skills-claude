---
name: requirements-engineering
description: "Convierte necesidades ambiguas en requisitos verificables, historias, criterios de aceptación, reglas de negocio y trazabilidad. Usar antes de diseñar o al aclarar qué se debe construir."
---

# Requirements Engineering

## Alcance
Define qué debe hacer el sistema y cómo se comprobará. No cubre:
- Diseño técnico de la solución: `technical-specification`.
- Calendario y estimación: `project-planning`.
- Plan de pruebas completo: `testing-strategy`.

## Procedimiento
1. Identifica objetivo de negocio, usuarios, partes interesadas y problema actual.
2. Separa hechos dichos por el usuario, supuestos y preguntas. Formula solo las preguntas que cambian la solución.
3. Fija alcance: incluido, excluido y aplazado.
4. Redacta requisitos funcionales, uno por enunciado, con identificador estable (`RF-001`).
5. Redacta requisitos no funcionales con umbral y condición medibles (`RNF-001`).
6. Extrae reglas de negocio aparte, con su fuente (`RN-001`).
7. Escribe criterios de aceptación. Con Gherkin usa `Given/When/Then` y 3 a 5 pasos por ejemplo.
8. Añade casos negativos, límites, permisos y estados vacíos.
9. Construye la matriz de trazabilidad: objetivo → requisito → criterio → prueba.
10. Registra decisiones pendientes con responsable.

## Calidad de un requisito
Evita términos no medibles como "rápido", "fácil", "seguro" o "intuitivo". Cada requisito debe ser necesario, inequívoco, viable y verificable. Si falta el valor, escribe "Por confirmar"; no lo inventes.

## Verificación
- Cada requisito tiene al menos un criterio comprobable.
- Ningún criterio introduce comportamiento ausente de los requisitos.
- La matriz no tiene filas huérfanas.
- Ninguna regla de negocio se presenta como confirmada sin fuente.

## Entrega
Contexto, alcance, requisitos, reglas, criterios, matriz, supuestos, riesgos y decisiones pendientes.

## Ejemplo
Entrada: "El login debe ser seguro y rápido".
Salida:
- `RF-001`: el sistema bloquea temporalmente la cuenta tras N intentos fallidos. N: Por confirmar.
- `RNF-001`: el 95 % de los inicios de sesión responde en menos de X ms con la carga Y. X e Y: Por confirmar.

```gherkin
Scenario: Credenciales incorrectas
  Given un usuario registrado
  When envía una contraseña incorrecta
  Then ve un mensaje genérico que no revela si la cuenta existe
```

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
