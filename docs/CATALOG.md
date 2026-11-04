# Catálogo de Skills

Las carpetas permanecen planas en `.claude/skills/` porque Claude Code busca `.claude/skills/<skill>/SKILL.md`. Las especialidades se organizan aquí.

## 01. Software Engineering

| Skill | Función | Fuentes leídas / localizadas |
|---|---|---|
| `software-architecture` | Diseña y evalúa arquitecturas: límites de módulos, estilos, compromisos y requisitos no funcionales. Usar siempre al elegir entre monolito y servicios, iniciar un sistema o evaluar escalabilidad. | 3 / 0 |
| `requirements-engineering` | Convierte necesidades ambiguas en requisitos verificables, historias, criterios de aceptación, reglas de negocio y trazabilidad. Usar antes de diseñar o al aclarar qué se debe construir. | 3 / 1 |
| `design-patterns` | Selecciona y aplica patrones de diseño (Strategy, Adapter, Factory, Observer, Repository) solo cuando resuelven un problema real. Usar siempre que se pregunte qué patrón aplicar o cómo estructurar clases. | 1 / 1 |
| `refactoring` | Mejora la estructura interna del código sin cambiar su comportamiento observable, en pasos pequeños protegidos por pruebas. Usar ante duplicación, complejidad o código difícil de modificar. | 3 / 1 |
| `code-quality` | Define y automatiza estándares de código: formateo, linting, análisis estático, tipos, umbrales y convenciones. Usar al configurar calidad en un proyecto o reducir ruido de linters. | 1 / 2 |
| `repository-analysis` | Inspecciona un repositorio desconocido y resume stack, estructura, comandos, dependencias, pruebas y riesgos. Usar antes de modificar un proyecto nuevo o cuando se pida entender un repo. | 3 / 1 |
| `legacy-code-analysis` | Comprende y documenta sistemas antiguos sin pruebas ni documentación: comportamiento real, costuras y dependencias. Usar antes de cambiar código heredado o planificar su reemplazo. | 3 / 1 |
| `technical-debt-management` | Identifica, clasifica y prioriza deuda técnica según su coste real y frecuencia de cambio, y crea un plan de reducción. Usar al decidir qué limpiar o justificar esa inversión. | 3 / 0 |
| `skill-creator` | Diseña, crea, valida y mejora Skills reutilizables para Claude siguiendo el formato Agent Skills. Úsala cuando quieras convertir procesos, estándares o conocimientos en una Skill mantenible. | 2 / 0 |

## 02. Development

| Skill | Función | Fuentes leídas / localizadas |
|---|---|---|
| `fullstack-development` | Implementa funcionalidades web completas que cruzan interfaz, backend y base de datos. Usar siempre que un cambio afecte a varias capas, como botón, endpoint y consulta juntos. | 3 / 0 |
| `frontend-design` | Diseña e implementa interfaces web modernas y responsive con componentes reutilizables. Usar siempre al crear o rediseñar páginas, dashboards, formularios o prototipos. | 3 / 0 |
| `backend-engineering` | Desarrolla servicios del lado servidor: lógica de negocio, capas, transacciones, errores y procesos asíncronos. Usar siempre al implementar o modificar lógica de servidor. | 3 / 0 |
| `api-engineering` | Diseña, implementa y valida APIs HTTP/REST: rutas, contratos, errores, versionado, permisos y límites. Usar al crear endpoints o revisar el diseño de una API. | 3 / 1 |
| `database-engineering` | Modela, consulta y optimiza bases de datos: esquemas, SQL, índices, migraciones de esquema y planes de ejecución. Usar siempre con consultas lentas, EXPLAIN o diseño de tablas. | 2 / 1 |
| `react-development` | Construye y corrige componentes React: hooks, estado, efectos, rendimiento y pruebas, según las reglas oficiales. Usar siempre con JSX/TSX, useEffect, bucles de render o errores de hooks. | 3 / 1 |
| `typescript-engineering` | Diseña tipos seguros y configura tsconfig: modo estricto, genéricos, uniones, narrowing y migración desde JavaScript. Usar ante errores de TypeScript o al modelar tipos. | 1 / 2 |
| `nodejs-engineering` | Desarrolla y diagnostica servicios Node.js: LTS, asincronía, event loop, streams, memoria y seguridad. Usar siempre con servidores Node lentos, bloqueados o inestables, aunque la causa parezca evidente. | 4 / 0 |
| `python-engineering` | Estructura y mantiene proyectos Python: pyproject.toml, entornos virtuales, tipado, pruebas, empaquetado y versiones con soporte. Usar al crear, ordenar o modernizar código Python. | 3 / 2 |
| `mobile-development` | Desarrolla y revisa apps móviles Android e iOS: arquitectura, estado, offline, permisos, seguridad y publicación en tiendas. Usar con Kotlin, Swift, Flutter o React Native. | 3 / 1 |
| `ui-ux-engineering` | Evalúa y mejora la experiencia de usuario: flujos, heurísticas, formularios, mensajes de error y estados de interfaz. Usar ante pantallas confusas o al revisar la usabilidad de un producto. | 1 / 1 |
| `web-accessibility` | Audita y corrige accesibilidad web según WCAG 2.2: teclado, foco, contraste, formularios, ARIA y lector de pantalla. Usar al revisar la conformidad AA o corregir barreras de acceso. | 3 / 2 |
| `data-engineering` | Diseña y mantiene pipelines ETL/ELT, modelos y calidad de datos con cargas idempotentes y reprocesables, con herramientas como Airflow o dbt. Usar con pipelines, DAGs o transformaciones. | 2 / 2 |
| `message-queue-engineering` | Diseña productores y consumidores con RabbitMQ o Kafka: entrega, reintentos, idempotencia, orden y colas de error. Usar ante mensajes duplicados, perdidos, lag o procesamiento asíncrono. | 3 / 2 |
| `microservices-engineering` | Evalúa, separa y coordina microservicios: límites, datos por servicio, sagas, outbox, comunicación y operación. Usar al decidir partir un monolito o ante fallos entre servicios. | 4 / 2 |
| `system-integration` | Integra aplicaciones con APIs externas, webhooks y ERP/SaaS: autenticación, mapeo, reintentos, idempotencia y conciliación. Usar al conectar sistemas o sincronizar datos con terceros. | 1 / 2 |

## 03. Quality Assurance

| Skill | Función | Fuentes leídas / localizadas |
|---|---|---|
| `testing-strategy` | Define qué probar y en qué nivel: pirámide, cobertura útil, regresión, aceptación y gestión de pruebas inestables. Usar al diseñar el plan de pruebas de un proyecto o de una versión. | 2 / 2 |
| `qa-automation` | Escribe y ejecuta pruebas automatizadas unitarias, de integración, API y end-to-end, incluido Playwright. Usar para automatizar casos, prevenir regresiones o corregir pruebas frágiles. | 2 / 0 |
| `debugging` | Diagnostica errores mediante síntomas, logs, trazas, reproducción y causa raíz. Usar siempre ante excepciones, stack traces, fallos intermitentes o resultados inesperados, antes de proponer una corrección. | 2 / 0 |
| `code-review` | Revisa código buscando defectos, seguridad, regresiones, mantenibilidad y rendimiento. Usar siempre que se pida revisar un pull request, diff o cambio antes de fusionarlo. | 2 / 0 |

## 04. Security

| Skill | Función | Fuentes leídas / localizadas |
|---|---|---|
| `application-security` | Audita la seguridad de aplicaciones, código, APIs y configuraciones existentes con prácticas OWASP. Usar para revisar vulnerabilidades o aplicar hardening defensivo. | 3 / 0 |
| `secure-code-development` | Aplica desarrollo seguro al escribir código: validación, consultas parametrizadas, salida segura, manejo de errores y registros. Usar al implementar funciones que procesan entrada o datos sensibles. | 4 / 1 |
| `threat-modeling` | Modela amenazas de un sistema o funcionalidad con flujos de datos, límites de confianza y STRIDE, y prioriza mitigaciones. Usar al diseñar algo nuevo o cambiar autenticación o datos sensibles. | 2 / 1 |
| `identity-access-management` | Diseña autenticación y autorización: OAuth 2.0, OIDC, sesiones, MFA, RBAC y políticas de contraseñas. Usar al implementar login, SSO, roles, tokens o control de acceso. | 3 / 1 |
| `penetration-testing` | Planifica y documenta evaluaciones de seguridad autorizadas de aplicaciones: alcance, reglas, metodología WSTG, evidencia e informe. Usar solo con autorización escrita sobre sistemas propios o de clientes. | 2 / 1 |
| `secrets-management` | Gestiona credenciales, claves y tokens: almacenamiento, inyección, rotación, auditoría y respuesta a filtraciones. Usar ante secretos en código, .env, CI/CD o una credencial expuesta. | 2 / 3 |
| `compliance-engineering` | Traduce marcos como ISO 27001, SOC 2, PCI DSS o NIST CSF en controles técnicos, evidencias y trazabilidad. Usar al preparar auditorías o mapear controles; no sustituye asesoría legal. | 3 / 2 |
| `dependency-management` | Audita, actualiza y fija dependencias: vulnerabilidades, lockfiles, SemVer, licencias y actualizaciones automáticas. Usar con npm audit, pip-audit, Dependabot o librerías obsoletas. | 6 / 2 |

## 05. Cloud & Infrastructure

| Skill | Función | Fuentes leídas / localizadas |
|---|---|---|
| `aws-cloud-engineering` | Diseña, implementa y revisa soluciones AWS con foco en arquitectura, IAM, redes, cómputo, almacenamiento, monitoreo, costos y seguridad. Úsala para proyectos o incidentes sobre servicios AWS. | 3 / 0 |
| `devops-engineering` | Coordina la entrega y operación de un proyecto de extremo a extremo cuando abarca varias áreas: build, entornos, despliegue y operación. Usar para el panorama DevOps general. | 3 / 0 |
| `docker-engineering` | Crea y optimiza Dockerfiles, imágenes y Compose: etapas múltiples, caché, usuario no root, secretos de build y tamaño. Usar con Dockerfile, docker-compose o contenedores que fallan. | 3 / 1 |
| `kubernetes-engineering` | Crea y diagnostica manifiestos Kubernetes: Deployments, Services, probes, recursos, RBAC, Secrets y Pod Security. Usar con kubectl, Helm, Pods en CrashLoopBackOff o despliegues en clúster. | 4 / 2 |
| `terraform-iac` | Escribe y revisa infraestructura como código con Terraform: módulos, estado remoto, planes, versiones y pruebas. Usar con archivos .tf, terraform plan, state o drift. | 3 / 2 |
| `cicd-engineering` | Diseña y endurece pipelines de GitHub Actions o GitLab CI: compilación, pruebas, artefactos, despliegues, caché y seguridad. Usar con workflows que fallan, son lentos o inseguros. | 3 / 1 |
| `linux-server-engineering` | Administra servidores Linux: systemd, SSH, firewall, usuarios, paquetes, logs y endurecimiento. Usar con Ubuntu, Debian o RHEL, servicios caídos, disco lleno o configuración de un servidor. | 3 / 2 |

## 06. Documentation

| Skill | Función | Fuentes leídas / localizadas |
|---|---|---|
| `technical-documentation` | Crea y mantiene documentación técnica general y verificable: README, guías para desarrolladores, informes y wikis. Usar siempre al escribir un README o documentación sin una Skill específica. | 2 / 0 |
| `technical-specification` | Redacta especificaciones técnicas y documentos de diseño: objetivos, propuesta, alternativas, contratos, datos, riesgos y despliegue. Usar antes de implementar una funcionalidad o sistema importante. | 4 / 0 |
| `api-documentation` | Crea y valida documentación OpenAPI/Swagger y guías de API a partir del comportamiento real: rutas, esquemas, errores, autenticación y ejemplos. Usar para documentar endpoints existentes. | 2 / 2 |
| `user-manual-creation` | Redacta manuales y guías para usuarios finales no técnicos, con tareas paso a paso, lenguaje claro y resolución de problemas. Usar para ayudas, manuales de un sistema o capacitación. | 2 / 2 |
| `installation-guides` | Escribe guías de instalación y configuración reproducibles, con prerrequisitos, comandos, verificación y resolución de errores. Usar al documentar cómo instalar un sistema, herramienta o entorno. | 3 / 2 |
| `deployment-documentation` | Documenta procedimientos de despliegue y reversión: runbooks, prechecks, migraciones, comprobaciones y responsables. Usar al escribir un runbook, plan de pase a producción o rollback. | 3 / 2 |
| `architecture-documentation` | Documenta arquitecturas existentes con diagramas C4 y Mermaid, plantilla arc42 y ADR. Usar al dibujar un sistema, registrar decisiones o actualizar documentación arquitectónica. | 2 / 3 |

## 07. Operations & Management

| Skill | Función | Fuentes leídas / localizadas |
|---|---|---|
| `observability-engineering` | Instrumenta logs, métricas y trazas con OpenTelemetry o Prometheus, y diseña paneles y alertas útiles. Usar al añadir telemetría, reducir ruido de alertas o diagnosticar puntos ciegos. | 4 / 1 |
| `reliability-engineering` | Define SLI, SLO y presupuestos de error, alertas por burn rate, alta disponibilidad y recuperación. Usar al fijar objetivos de fiabilidad, planificar RTO/RPO o evaluar resiliencia. | 3 / 2 |
| `incident-response` | Coordina la respuesta a incidentes técnicos y de seguridad: roles, mitigación, comunicación, evidencia y postmortem. Usar cuando hay una caída, degradación, brecha activa o se redacta un postmortem. | 4 / 0 |
| `release-management` | Gestiona versiones del producto: SemVer, changelog, notas de versión, etiquetas, ramas y coordinación de lanzamientos. Usar al preparar una versión o decidir su número. | 4 / 1 |
| `project-planning` | Convierte objetivos técnicos en planes con alcance, desglose, dependencias, estimaciones por rango, riesgos e hitos. Usar al planificar un proyecto, sprint o roadmap, o al estimar trabajo. | 2 / 1 |
| `migration-engineering` | Planifica y ejecuta migraciones de datos, aplicaciones, nube y versiones por fases, con reversión y validación. Usar al mover sistemas, actualizar plataformas o cambiar bases de datos. | 3 / 1 |
| `git-workflow` | Aplica flujos Git profesionales: ramas, commits, pull requests, historiales divergentes y conflictos. Usar siempre ante errores de git pull, merge, rebase o push, incluso si la respuesta parece simple. | 3 / 1 |
| `performance-optimization` | Investiga y optimiza rendimiento de aplicaciones, APIs, consultas y frontend mediante mediciones y perfiles. Úsala ante lentitud, alto consumo de CPU/memoria, latencia o costos de ejecución. | 3 / 0 |
