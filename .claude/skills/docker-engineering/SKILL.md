---
name: docker-engineering
description: "Crea y optimiza Dockerfiles, imágenes y Compose: etapas múltiples, caché, usuario no root, secretos de build y tamaño. Usar con Dockerfile, docker-compose o contenedores que fallan."
---

# Docker Engineering

## Alcance
Imágenes y contenedores. No cubre:
- Orquestación en clúster: `kubernetes-engineering`.
- Pipeline de publicación: `cicd-engineering`.

## Procedimiento
1. Inspecciona el proyecto: runtime, lockfile, comando de arranque, puertos, Dockerfile y `.dockerignore` existentes.
2. Elige una base oficial y mínima adecuada al runtime, con versión fijada. Considera el digest si buscas reproducibilidad total.
3. Usa construcción en varias etapas: compila en una y copia solo lo necesario a la final.
4. Ordena para aprovechar la caché: primero manifiesto y lockfile, luego instalación y después el código.
5. Crea `.dockerignore` para excluir `.git`, `node_modules`, `.env` y artefactos.
6. Ejecuta con un usuario no root.
7. Pasa secretos de build con secret mounts, nunca con `ARG` o `ENV`.
8. Escribe contenedores efímeros: estado fuera, configuración por entorno y cierre correcto con `SIGTERM` usando la forma exec de `CMD`.
9. Reconstruye con frecuencia, con `--pull` en CI, para incorporar parches de la base.

## Reglas
- No uses `latest` en producción.
- No montes `docker.sock` en contenedores sin una justificación clara.
- No ejecutes `docker system prune` ni borres volúmenes sin autorización: elimina datos.
- Evita `sudo` dentro de la imagen y no alternes `USER` constantemente.
- Las etiquetas son mutables. Docker indica que fijar por digest garantiza la misma imagen, a cambio de aplicar las actualizaciones de seguridad de forma deliberada: `FROM imagen:tag@sha256:<digest>`.

## Verificación
```bash
docker build -t app:prueba .
docker run --rm app:prueba id          # no debe indicar uid=0
docker history app:prueba              # sin secretos en capas
docker image ls app:prueba             # tamaño antes y después
```
Comprueba también un arranque real y una solicitud de salud.

## Entrega
Dockerfile, `.dockerignore`, cambios de tamaño medidos, comandos ejecutados, resultados y limitaciones.

## Ejemplo
```dockerfile
FROM node:<version-lts> AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev

FROM node:<version-lts> AS runner
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
USER node
CMD ["node", "server.js"]
```
Sustituye `<version-lts>` por una versión vigente y confirmada.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
