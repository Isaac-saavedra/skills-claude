---
name: threat-modeling
description: "Modela amenazas de un sistema o funcionalidad con flujos de datos, límites de confianza y STRIDE, y prioriza mitigaciones. Usar al diseñar algo nuevo o cambiar autenticación o datos sensibles."
---

# Threat Modeling

## Alcance
Análisis de diseño antes o durante la construcción. No cubre:
- Búsqueda de vulnerabilidades en código existente: `application-security`.
- Pruebas activas: `penetration-testing`.

## Procedimiento
Responde a las cuatro preguntas:

**1. ¿En qué estamos trabajando?**
Dibuja un diagrama de flujo de datos con entidades externas, procesos, almacenes, flujos y límites de confianza. Enumera activos y datos sensibles.

**2. ¿Qué puede salir mal?**
Recorre con STRIDE cada elemento que cruza un límite:

| Amenaza | Propiedad violada |
|---|---|
| Suplantación | Autenticación |
| Manipulación | Integridad |
| Repudio | Trazabilidad |
| Divulgación de información | Confidencialidad |
| Denegación de servicio | Disponibilidad |
| Elevación de privilegios | Autorización |

**3. ¿Qué vamos a hacer?**
Prioriza por probabilidad, impacto y esfuerzo. Asigna una respuesta documentada:
- Mitigar.
- Eliminar la funcionalidad o el componente.
- Transferir, indicando quién asume el riesgo residual.
- Aceptar, con justificación y responsable.

**4. ¿Hicimos un trabajo suficiente?**
Revisa con las partes interesadas y comprueba que cada mitigación se pueda probar. Actualiza el modelo cuando cambie el sistema.

## Reglas
- Trabaja con el diseño real y marca los supuestos.
- Hazlo proporcional: una función pequeña necesita una página, no un proyecto.
- No uses puntuaciones numéricas como si fueran medidas precisas.
- Si hay datos personales, valora LINDDUN como técnica complementaria de privacidad.

## Verificación
Cada límite de confianza fue revisado y cada amenaza alta tiene respuesta, responsable y una prueba o criterio de comprobación.

## Entrega
Diagrama, activos, supuestos, tabla de amenazas, mitigaciones, riesgos aceptados y fecha de revisión.

## Ejemplo
Subida de archivos: **Manipulación**, archivo malicioso → validar tipo y aislar el procesado. **Divulgación**, URL adivinable → firmar y expirar enlaces. **Denegación**, archivos gigantes → límite de tamaño y cuota.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
