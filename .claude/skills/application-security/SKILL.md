---
name: application-security
description: "Audita la seguridad de aplicaciones, código, APIs y configuraciones existentes con prácticas OWASP. Usar para revisar vulnerabilidades o aplicar hardening defensivo."
---

# Application Security

## Alcance
Trabaja únicamente sobre sistemas propios o para los que el usuario tenga autorización. Mantén el análisis en un propósito defensivo.

**No cubre:** Escribir código seguro desde el inicio: `secure-code-development`. Modelar amenazas de un diseño: `threat-modeling`. Pruebas activas autorizadas: `penetration-testing`.

## Procedimiento
1. Define activos, datos sensibles, actores, límites de confianza y superficie expuesta.
2. Realiza threat modeling proporcional al sistema.
3. Revisa autenticación, autorización, sesiones, validación, manejo de secretos, dependencias, logs y configuración.
4. Considera riesgos comunes: control de acceso roto, inyección, XSS, CSRF, SSRF, path traversal, deserialización insegura, exposición de secretos y configuración débil.
5. Comprueba hallazgos con evidencia y pruebas no destructivas.
6. Prioriza por impacto, explotabilidad y exposición.
7. Recomienda mitigaciones concretas y verificables.
8. Define pruebas de regresión y controles preventivos.

## Reglas
- No ejecutes explotación, escaneo intrusivo ni cambios en sistemas de terceros sin autorización explícita.
- No extraigas ni reveles secretos. Si aparecen, recomienda rotación y manejo seguro.
- No afirmes cumplimiento de una norma o certificación por una revisión parcial.
- Verifica versiones y avisos de seguridad en fuentes oficiales.
- Distingue vulnerabilidad confirmada, riesgo potencial y recomendación.

## Entregable
Resumen ejecutivo, alcance, metodología, hallazgos con evidencia, severidad razonada, remediación, validación y limitaciones.

## Verificación
Cada hallazgo incluye evidencia y comprobación no destructiva. Valida a mano los resultados de SAST; prioriza lo que las herramientas analizan mal, como lógica de negocio, autorización y condiciones de carrera.

## Ejemplo
Hallazgo confirmado: `GET /facturas/{id}` no comprueba el propietario (`facturas.py:42`). Severidad alta. Corrección: filtrar por usuario autenticado y añadir prueba de regresión con dos cuentas.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
