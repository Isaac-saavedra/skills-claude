---
name: incident-response
description: "Coordina la respuesta a incidentes técnicos y de seguridad: roles, mitigación, comunicación, evidencia y postmortem. Usar cuando hay una caída, degradación, brecha activa o se redacta un postmortem."
---

# Incident Response

## Alcance
Sistema caído o comprometido y su análisis posterior. No cubre:
- Causa raíz de un error sin impacto activo: `debugging`.
- Rotación rutinaria: `secrets-management`.

## Durante el incidente
1. Declara el incidente, la severidad y el canal único.
2. Asigna roles: comandante (coordina), comunicaciones (informa) y operaciones (mitiga). Una persona puede cubrir varios al principio.
3. Prioriza **mitigar** sobre encontrar la causa: revertir, desactivar la función, desviar o añadir capacidad.
4. Lleva una línea de tiempo con UTC: hechos, decisiones y responsables.
5. Comunica en intervalos fijos: impacto, acciones y próxima actualización, sin especular.
6. Pide autorización para cada acción de riesgo y registra su resultado.
7. Cierra con criterios acordados y confirma la recuperación mediante métricas.

## Incidente de seguridad
- Conserva evidencia antes de cambiar o reiniciar: registros, imágenes y marcas de tiempo.
- Contén: aísla sistemas y revoca credenciales.
- Avisa a legal o al responsable: las notificaciones dependen de la jurisdicción y contratos.
- Usa NIST SP 800-61r3, organizado según las funciones de CSF 2.0.

## Postmortem
- Sin culpas: analiza sistemas y procesos con lenguaje factual.
- Incluye contexto, impacto cuantificado, línea de tiempo, causa raíz, disparador, qué funcionó y qué no.
- Acciones concretas, medibles, con dueño y seguimiento; prefiere automatizar controles.
- Un único responsable y publicación pronta.

## Reglas
- No afirmes una causa sin evidencia: "hipótesis" hasta confirmarla.
- No borres registros ni historial durante un incidente.
- No ejecutes acciones destructivas sin autorización explícita.

## Verificación
La métrica de usuario volvió a la normalidad, se comprobó con una solicitud real y cada acción abierta tiene dueño.

## Entrega
Línea de tiempo, estado, acciones, comunicaciones y postmortem o borrador con los datos faltantes indicados.

## Ejemplo
"14:32 UTC. Impacto: 30 % de los pagos con error. Mitigación en curso: revertir la versión 2.4.1. Causa: hipótesis, cambio de conexión. Próxima actualización: 14:50 UTC."

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
