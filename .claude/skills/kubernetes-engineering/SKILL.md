---
name: kubernetes-engineering
description: "Crea y diagnostica manifiestos Kubernetes: Deployments, Services, probes, recursos, RBAC, Secrets y Pod Security. Usar con kubectl, Helm, Pods en CrashLoopBackOff o despliegues en clúster."
---

# Kubernetes Engineering

## Alcance
Cargas en Kubernetes. No cubre:
- Construir la imagen: `docker-engineering`.
- Aprovisionar la nube del clúster: `terraform-iac` o `aws-cloud-engineering`.

## Procedimiento
1. Confirma el contexto antes de actuar: `kubectl config current-context` y el namespace. Comprueba la versión del clúster.
2. Lee los manifiestos, Helm o Kustomize existentes; no generes un sistema paralelo.
3. Define réplicas, imagen con versión fijada, solicitudes y límites de recursos y estrategia de despliegue.
4. Configura probes:
   - **Startup**: arranque lento.
   - **Readiness**: si falla, el Pod sale de los endpoints del Service sin reiniciarse.
   - **Liveness**: si falla, se reinicia. Úsalo solo para bloqueos irrecuperables y sin depender de servicios externos: puede provocar reinicios en cascada.
5. Aplica Pod Security Standards con la etiqueta `pod-security.kubernetes.io/<modo>: <nivel>`:
   - Niveles: `privileged`, `baseline` y `restricted`.
   - Modos: `enforce` rechaza el Pod; `audit` y `warn` lo permiten y lo registran o avisan.
   - Añade RBAC mínimo y omite el token de cuenta de servicio si no se necesita.
6. Secrets: por defecto se guardan sin cifrar en etcd y base64 no es cifrado. Activa cifrado en reposo y limita `get`, `list` y `watch`.
7. Valida primero: `kubectl diff -f` y `kubectl apply --dry-run=server -f`.

## Diagnóstico
```bash
kubectl get pods -n <ns> -o wide
kubectl describe pod <pod> -n <ns>
kubectl logs <pod> -n <ns> --previous
kubectl get events -n <ns> --sort-by=.lastTimestamp
```
Lee los eventos antes de reiniciar nada.

## Reglas
- No apliques, elimines ni escales en producción sin autorización explícita.
- Revisa `kubectl get` antes de un `delete`, y nunca uses `--all` sin confirmación.
- Prueba un cambio de Pod Security antes de aplicarlo: `kubectl label --dry-run=server --overwrite ns <ns> pod-security.kubernetes.io/enforce=baseline`.
- Prueba en un entorno distinto de producción.

## Verificación
`kubectl rollout status`, Pods listos, Service con endpoints y solicitud real. Comprueba la reversión con `kubectl rollout undo` en entorno de prueba.

## Entrega
Manifiestos, comandos y resultados reales, plan de reversión, riesgos y contexto usado.

## Ejemplo
`CrashLoopBackOff`: `logs --previous` muestra un error de variable ausente; se añade la referencia al Secret, se valida con dry-run y se comprueba el rollout. La liveness no estaba relacionada y no se cambia.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
