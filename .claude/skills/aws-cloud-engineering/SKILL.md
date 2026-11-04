---
name: aws-cloud-engineering
description: "Diseña, implementa y revisa soluciones AWS con foco en arquitectura, IAM, redes, cómputo, almacenamiento, monitoreo, costos y seguridad. Úsala para proyectos o incidentes sobre servicios AWS."
---

# AWS Cloud Engineering

## Alcance
**No cubre:** Código Terraform: `terraform-iac`. Kubernetes: `kubernetes-engineering`. Otros proveedores de nube.

## Reglas de verificación
AWS cambia con frecuencia. Verifica nombres, límites, regiones, precios, disponibilidad y comportamiento en documentación oficial AWS antes de afirmarlos. No inventes ARN, cuotas ni capacidades.

## Flujo
1. Identifica cuenta/entorno, región, objetivo, restricciones, criticidad y recursos existentes.
2. Inspecciona IaC y configuración actual antes de proponer cambios.
3. Diseña con mínimo privilegio, segmentación de red, cifrado, logging y recuperación.
4. Evalúa alta disponibilidad, escalabilidad, backups, RTO/RPO y observabilidad.
5. Considera costos y alternativas sin inventar estimaciones.
6. Prefiere IaC reproducible cuando sea apropiado.
7. Propón cambios pequeños, revisables y reversibles.
8. Define validaciones previas y posteriores.
9. Incluye rollback y riesgos operativos.

## Seguridad
- IAM: privilegios mínimos, roles y credenciales temporales cuando sea posible.
- Red: exposición mínima, security groups y controles por capas.
- Datos: cifrado, políticas de acceso, retención y backups.
- Observabilidad: CloudTrail, CloudWatch y logs según necesidad.
- Secretos: no incluirlos en código, plantillas ni repositorios.

## Cambios productivos
No ejecutes ni recomiendes aplicar cambios destructivos sin aprobación. Identifica recursos afectados y posibles interrupciones. Para políticas IAM/WAF, explica el efecto de cada regla y valida sintaxis y alcance.

## Entrega
Incluye región, servicios, diagrama, configuración/IaC, permisos, costos conocidos o pendientes, monitoreo, pruebas, rollback y fuentes oficiales AWS.

## Verificación
Usa IaC con plan revisado o comandos de solo lectura y confirma cuenta y región con `aws sts get-caller-identity`. Valida políticas con IAM Access Analyzer antes de aplicarlas.

## Ejemplo
Aplicación en EC2 que usa claves fijas: sustituirlas por un rol de instancia con permisos mínimos, generar la política con Access Analyzer según actividad de CloudTrail y probarla antes de desplegar.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
