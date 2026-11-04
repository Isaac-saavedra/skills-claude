---
name: application-security
description: "Evalúa y mejora la seguridad de aplicaciones, código, APIs y configuraciones siguiendo prácticas OWASP y mínimo privilegio. Úsala para threat modeling, revisión de vulnerabilidades o hardening defensivo."
---

# Application Security

## Alcance
Trabaja únicamente sobre sistemas propios o para los que el usuario tenga autorización. Mantén el análisis en un propósito defensivo.

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
