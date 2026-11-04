---
name: deployment-documentation
description: "Documenta procedimientos de despliegue y reversión: runbooks, prechecks, migraciones, comprobaciones y responsables. Usar al escribir un runbook, plan de pase a producción o rollback."
---

# Deployment Documentation

## Alcance
El documento que una persona seguirá para desplegar. No cubre:
- Automatizar el pipeline: `cicd-engineering`.
- Decidir la versión: `release-management`.

## Procedimiento
1. Reúne evidencia: pipeline, infraestructura, scripts, migraciones y despliegues anteriores.
2. Describe entornos, responsables, aprobaciones y ventana.
3. Lista **prechecks**: versión exacta, copia de seguridad restaurable, capacidad, dependencias y alertas.
4. Escribe pasos numerados con comando, duración estimada, salida esperada y qué hacer si falla.
5. Indica la estrategia: despliegue gradual, canary o blue-green, y el criterio de avance. En canary, compara métricas con el grupo de control y con los SLO.
6. Documenta migraciones de datos y si son compatibles con la versión anterior.
7. Escribe la **reversión** con su disparador, sus pasos y el punto de no retorno.
8. Define comprobaciones posteriores: salud, métricas y prueba funcional.
9. Define comunicación y registro.

## Reglas
- No inventes comandos, servidores o responsables: usa `<valor>` y "Por confirmar".
- Una reversión sin probar se marca como **no comprobada**.
- Indica explícitamente cuando una migración impide revertir.
- No incluyas secretos: referencia dónde obtenerlos.
- Documentar no autoriza ejecutar: no despliegues sin autorización.

## Verificación
Ensayo en un entorno previo, o revisión paso a paso con quien lo ejecutará. Registra fecha y resultado.

## Entrega
Runbook completo, estado de ensayo, riesgos, reversión y datos pendientes.

## Ejemplo
```markdown
### Paso 4: activar canary (5 %)
Comando: `<comando del proyecto>`
Espera: 15 min
Continuar si: tasa de error por debajo de <umbral>
Si falla: ir a "Reversión", paso 1
```

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
