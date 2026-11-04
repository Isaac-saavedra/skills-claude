---
name: compliance-engineering
description: "Traduce marcos como ISO 27001, SOC 2, PCI DSS o NIST CSF en controles técnicos, evidencias y trazabilidad. Usar al preparar auditorías o mapear controles; no sustituye asesoría legal."
---

# Compliance Engineering

## Alcance
Puente entre requisitos de cumplimiento y controles técnicos. No cubre:
- Asesoría legal o declaración de conformidad.
- Implementación detallada de cada control: usa la Skill técnica correspondiente.

## Procedimiento
1. Confirma marco, versión exacta, alcance del sistema y quién auditará. Obtén el texto oficial. Varias normas son de pago: no reconstruyas su contenido de memoria.
2. Inventaría sistemas, datos, proveedores y responsabilidades compartidas.
3. Crea la matriz: requisito → control → responsable → evidencia → frecuencia → estado.
4. Usa los estados: **implementado y con evidencia**, **implementado sin evidencia**, **parcial**, **ausente**, **no aplica con justificación**.
5. Prefiere evidencia automatizada y fechada: configuración, registros y resultados de CI.
6. Identifica brechas y priorízalas por riesgo y fecha de auditoría.
7. Reutiliza controles entre marcos con mapeos publicados, como los de CIS.
8. Protege la evidencia: puede contener datos sensibles.

## Referencias
- NIST CSF 2.0: Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar.
- CIS Controls v8.1: 18 controles.
- Comprueba las demás referencias en la fuente oficial vigente: ISO/IEC 27001, SOC 2 (AICPA) y PCI DSS.

## Reglas
- Nunca afirmes "cumple" o "certificado": solo un auditor o la entidad correspondiente puede concluirlo.
- No inventes evidencias, fechas, controles ni responsables.
- No cites cláusulas sin el texto oficial; marca "Por confirmar".
- Requisitos legales locales (privacidad, sector): remite a asesoría legal.

## Verificación
Cada control marcado como implementado enlaza a una evidencia comprobable y actual; una muestra se contrasta con el sistema real.

## Entrega
Alcance y versión, matriz, brechas, plan de remediación, evidencias, riesgos aceptados y lista de lo que requiere confirmación de auditor o legal.

## Ejemplo
| Requisito | Control | Evidencia | Estado |
|---|---|---|---|
| Por confirmar según el texto oficial | MFA para administradores | Exportación fechada del proveedor de identidad | Implementado sin evidencia |

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
