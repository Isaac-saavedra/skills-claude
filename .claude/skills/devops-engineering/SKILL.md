---
name: devops-engineering
description: "Coordina la entrega y operación de un proyecto de extremo a extremo cuando abarca varias áreas: build, entornos, despliegue y operación. Usar para el panorama DevOps general."
---

# DevOps Engineering

## Alcance
**No cubre:** Para una sola tecnología, prefiere la Skill específica: `docker-engineering`, `kubernetes-engineering`, `terraform-iac`, `cicd-engineering`, `linux-server-engineering`, `observability-engineering`.

## Procedimiento
1. Inspecciona sistema operativo, runtime, herramientas, pipeline y entorno.
2. Identifica proceso de build, pruebas, artefactos, configuración y despliegue actual.
3. Define pipeline reproducible con etapas claras.
4. Usa imágenes base mantenidas, versiones fijadas cuando corresponda y builds reproducibles.
5. Ejecuta como usuario no privilegiado siempre que sea viable.
6. Separa configuración de código y gestiona secretos mediante mecanismos apropiados.
7. Añade health checks, logs, métricas y alertas accionables.
8. Diseña despliegues graduales y rollback.
9. Documenta dependencias, puertos, volúmenes, variables y procedimientos.
10. Verifica el pipeline con evidencia.

## Seguridad y operación
- No publiques secretos en logs o YAML.
- No uses privilegios elevados sin justificación.
- Escanea dependencias e imágenes cuando existan herramientas disponibles.
- Evita `latest` en entornos donde la reproducibilidad sea importante.
- No borres volúmenes, imágenes o recursos productivos sin confirmar impacto.
- Considera backups antes de cambios de estado.

## Entrega
Incluye pipeline, archivos modificados, instrucciones de ejecución, secretos requeridos (solo nombres), pruebas, estrategia de despliegue y rollback.

## Verificación
Ejecuta el flujo completo en un entorno no productivo: build, pruebas, despliegue, comprobación de salud y reversión. Registra resultados reales.

## Ejemplo
Proyecto desplegado a mano: identificar pasos actuales, automatizar compilación y pruebas, promover el mismo artefacto entre entornos, añadir comprobación de salud y reversión, y documentar el proceso.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
