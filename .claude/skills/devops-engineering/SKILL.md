---
name: devops-engineering
description: "Automatiza construcción, integración, entrega, despliegue, contenedores e infraestructura como código. Úsala para Docker, CI/CD, GitHub Actions, Linux, observabilidad y operaciones."
---

# DevOps Engineering

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
