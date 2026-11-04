---
name: terraform-iac
description: "Escribe y revisa infraestructura como código con Terraform: módulos, estado remoto, planes, versiones y pruebas. Usar con archivos .tf, terraform plan, state o drift."
---

# Terraform IaC

## Alcance
Terraform de cualquier proveedor. No cubre:
- Decisiones de servicios AWS: `aws-cloud-engineering`.
- Manifiestos de aplicaciones: `kubernetes-engineering`.

## Procedimiento
1. Lee código, versión, proveedores y configuración de backend. Identifica el entorno y el estado que afectará.
2. Organiza los archivos: `terraform.tf`, `providers.tf`, `backend.tf`, `main.tf`, `variables.tf`, `outputs.tf` y `locals.tf`. Separa por grupos lógicos si crece.
3. Fija versiones: `required_version`, `required_providers` y `version` de módulos. Versiona `.terraform.lock.hcl`.
4. Usa un backend remoto. Comprueba en la documentación de tu backend si admite bloqueo.
5. Pasa credenciales por variables de entorno: con `-backend-config` o en el código quedan en texto plano en `.terraform` y en los planes.
6. Formatea y valida: `terraform fmt -recursive` y `terraform validate`.
7. Revisa un plan guardado y aplica exactamente ese plan.
8. Añade pruebas con `terraform test` a módulos reutilizables.

## Flujo en automatización
```bash
terraform init -input=false
terraform plan -out=tfplan -input=false
# revisión humana del plan
terraform apply -input=false tfplan
```

## Reglas
- `apply`, `destroy`, `state rm` e `import` en entornos reales requieren autorización explícita.
- Lee cada `destroy` y `replace` del plan y resáltalos.
- `-auto-approve` solo para infraestructura no crítica.
- El estado y los planes contienen datos sensibles. Nunca los subas al repositorio.
- No versiones `.terraform`, `*.tfstate*`, planes ni `.tfvars` con secretos.
- Un `validate` correcto no prueba valores del proveedor ni garantiza que `apply` funcione.

## Verificación
`fmt -check`, `validate`, plan revisado y comprobación del recurso creado. Un nuevo plan debe indicar que no hay cambios.

## Entrega
Código, resumen del plan (crear, cambiar, destruir), comandos ejecutados, riesgos, reversión y pendientes.

## Ejemplo
Plan: `1 to add, 1 to change, 1 to destroy`. El elemento destruido es la base de datos por un cambio de nombre. Se detiene el proceso, se avisa y se propone un bloque `moved` tras confirmar en la documentación.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
