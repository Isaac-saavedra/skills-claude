---
name: identity-access-management
description: "Diseña autenticación y autorización: OAuth 2.0, OIDC, sesiones, MFA, RBAC y políticas de contraseñas. Usar al implementar login, SSO, roles, tokens o control de acceso."
---

# Identity and Access Management

## Alcance
Quién es el usuario y qué puede hacer. No cubre:
- Almacenamiento de claves: `secrets-management`.
- Permisos de nube en detalle: `aws-cloud-engineering`.

## Procedimiento
1. Define actores, tipos de cliente (web, móvil, SPA, máquina a máquina), recursos y requisitos de sesión.
2. Prefiere un proveedor de identidad mantenido en vez de construir autenticación propia.
3. Elige el flujo. Por defecto, código de autorización con PKCE.
4. Modela la autorización (RBAC o por atributos) y aplícala en el servidor, en cada operación y por objeto.
5. Define ciclo de vida: alta, cambio de rol, baja, revocación y recuperación.
6. Registra eventos de autenticación y cambios de permisos.

## OAuth 2.0 (RFC 9700)
- Coincidencia exacta de `redirect_uri`.
- PKCE obligatorio en clientes públicos, recomendado en confidenciales, con `S256`.
- No uses el flujo de contraseña. Evita el implícito.
- Clientes públicos: refresh tokens con rotación o restringidos al remitente.
- Tokens limitados a su audiencia; cada servidor de recursos debe rechazar los que no sean para él.

## Contraseñas (NIST SP 800-63B-4)
- Mínimo 15 caracteres en factor único; 8 si forman parte de MFA.
- Permite al menos 64 caracteres y gestores de contraseñas.
- Sin reglas de composición ni rotación periódica. Exige cambio si hay evidencia de compromiso.
- Compara con una lista de contraseñas comunes o filtradas.
- Sin preguntas de seguridad.
- Guarda con hash resistente, con sal.

## Otras defensas
Usa mensajes de error idénticos ante cualquier fallo de login, limita intentos por cuenta y ofrece MFA.

## Reglas
- No confíes en un rol enviado por el cliente.
- Valida firma, emisor, audiencia y expiración de cada token.
- Consulta el marco aplicable a tu país o sector: estas referencias no equivalen a cumplimiento legal.

## Verificación
Pruebas negativas: usuario A sobre recurso de B, token de otra audiencia, token vencido, rol retirado y redirect no registrado.

## Entrega
Flujo elegido, matriz de roles, parámetros de token y sesión, pruebas y riesgos.

## Ejemplo
SPA con API: código de autorización + PKCE `S256`, `aud` de la API validado en cada solicitud y comprobación de propietario en `GET /pedidos/{id}`.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
