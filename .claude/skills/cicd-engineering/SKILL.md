---
name: cicd-engineering
description: "Diseña y endurece pipelines de GitHub Actions o GitLab CI: compilación, pruebas, artefactos, despliegues, caché y seguridad. Usar con workflows que fallan, son lentos o inseguros."
---

# CI/CD Engineering

## Alcance
Pipelines de integración y entrega. No cubre:
- Infraestructura: `terraform-iac`.
- Imagen de contenedor: `docker-engineering`.
- Decisión de versión: `release-management`.

## Procedimiento
1. Lee los workflows actuales y mide fallos y duración. Identifica disparadores y entornos.
2. Diseña las etapas: instalar, lint, tipos, pruebas, compilar una vez, escanear, desplegar y comprobar.
3. Promueve el mismo artefacto entre entornos; no recompiles para cada uno.
4. Protege producción con aprobación y entornos protegidos.
5. Reduce tiempo con caché basada en el lockfile, paralelismo y cancelación de ejecuciones obsoletas.
6. Añade comprobación posterior al despliegue y reversión.

## Seguridad en GitHub Actions
- Fija cada acción a un SHA completo que pertenezca al repositorio de la acción, o a un lockfile si lo admite el repositorio.
- Establece `GITHUB_TOKEN` de solo lectura y eleva por trabajo.
- No interpoles valores no confiables en `run`: pásalos a una variable de entorno intermedia.
- Usa OIDC en vez de credenciales de larga duración.
- No uses runners autoalojados en repositorios públicos.

## Reglas
- No uses `continue-on-error` ni reintentos para esconder fallos.
- Trata el sistema de CI como producción. Evita que los forks accedan a secretos.
- No lances despliegues reales mientras pruebas un workflow sin autorización.
- GitLab CI y otros tienen controles distintos: consulta su documentación.

## Verificación
Ejecuta el workflow en una rama; provoca un fallo deliberado para ver que se bloquea; comprueba permisos efectivos y que no aparecen secretos en los registros.

## Entrega
Workflows, diagrama de etapas, tiempos antes y después, controles, ejecuciones reales y riesgos.

## Ejemplo
```yaml
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<sha-completo>
      - env:
          TITULO: ${{ github.event.pull_request.title }}
        run: echo "$TITULO"
```
Sustituye `<sha-completo>` por el commit verificado de la acción.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
