---
name: reliability-engineering
description: "Define SLI, SLO y presupuestos de error, alertas por burn rate, alta disponibilidad y recuperación. Usar al fijar objetivos de fiabilidad, planificar RTO/RPO o evaluar resiliencia."
---

# Reliability Engineering

## Alcance
Objetivos y diseño de fiabilidad. No cubre:
- Instrumentación: `observability-engineering`.
- Gestión de una crisis activa: `incident-response`.

## Procedimiento
1. Identifica los recorridos críticos para el usuario.
2. Define SLI con numerador y denominador claros: disponibilidad, latencia o frescura.
3. Fija un SLO según datos históricos y necesidades de usuarios. No apuntes al 100 %: es irreal y frena la entrega.
4. Calcula el presupuesto: 99,9 % en 30 días admite 43,2 minutos de indisponibilidad.
5. Acuerda una política de presupuesto: qué pasa al agotarlo.
6. Alerta con varias ventanas y tasas de consumo.
7. Identifica fallos de punto único y dependencias, y compara el SLO con el que estas ofrecen.
8. Define RTO y RPO con negocio, y **prueba** copias y restauración.
9. Diseña degradación: timeouts, reintentos limitados, disyuntores y límites.
10. Revisa los SLO periódicamente.

## Alertas por burn rate (SLO 99,9 %, 30 días)
| Severidad | Ventana larga | Ventana corta | Tasa | Presupuesto |
|---|---|---|---|---|
| Página | 1 h | 5 min | 14,4 | 2 % |
| Página | 6 h | 30 min | 6 | 5 % |
| Ticket | 3 días | 6 h | 1 | 10 % |

Son valores de ejemplo: ajústalos. La ventana corta suele ser 1/12 de la larga.

## Reglas
- SLA es un contrato con consecuencias; no lo confundas con SLO.
- Un plan de recuperación no probado no es evidencia.
- No inventes objetivos: pide o deriva los datos, y marca lo que falta.
- Haz experimentos de fallo solo en un entorno autorizado.

## Verificación
Comprueba el cálculo con datos reales, dispara la alerta en prueba y ejecuta una restauración con tiempo medido.

## Entrega
Documento SLO, política de presupuesto, alertas, análisis de dependencias, RTO y RPO, pruebas y riesgos.

## Ejemplo
SLI: solicitudes `2xx/3xx` entre las válidas de la API de pagos. SLO: 99,9 % en 30 días. Política: si se agota, se priorizan las correcciones de fiabilidad hasta recuperarlo.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
