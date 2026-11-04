---
name: penetration-testing
description: "Planifica y documenta evaluaciones de seguridad autorizadas de aplicaciones: alcance, reglas, metodología WSTG, evidencia e informe. Usar solo con autorización escrita sobre sistemas propios o de clientes."
---

# Penetration Testing

## Alcance
Evaluaciones **autorizadas y no destructivas** de aplicaciones. No cubre:
- Revisión de código o diseño: `application-security`.
- Corrección: `secure-code-development`.

Esta Skill no autoriza atacar sistemas ajenos ni crear malware, evasión de defensas, persistencia, robo de credenciales o exfiltración.

## Antes de cualquier prueba
Confirma por escrito, y detente si falta algo:
1. Propietario del sistema y autorización firmada.
2. Objetivos exactos: dominios, IP, cuentas y entorno. Terceros y proveedores en la nube según sus políticas.
3. Ventana horaria y contacto de emergencia.
4. Técnicas prohibidas: denegación de servicio, ingeniería social, alteración de datos.
5. Manejo de datos encontrados.

Prefiere siempre un entorno de pruebas sobre producción.

## Procedimiento
1. Planifica según el alcance y selecciona casos de WSTG.
2. Reconocimiento dentro del alcance acordado.
3. Combina escaneo automatizado con pruebas manuales: las herramientas no comprenden lógica de negocio.
4. Prueba autenticación, autorización, sesiones, validación, lógica y configuración.
5. Demuestra con la mínima prueba de concepto no destructiva y usa cuentas propias.
6. Ante un hallazgo crítico o datos reales, detente y avisa al contacto acordado.
7. Prioriza por impacto: un bypass de autorización crítico pesa más que muchos hallazgos menores.
8. Tras la corrección, repite la prueba.

## Reglas
- Sin autorización demostrable: ofrece solo revisión defensiva.
- No accedas a más datos de los necesarios para demostrar el hallazgo.
- No incluyas credenciales ni datos reales en el informe.
- WSTG es una referencia, no una norma de cumplimiento.

## Verificación
Cada hallazgo es reproducible, con pasos, evidencia sanitizada y dentro del alcance. Los falsos positivos se descartan a mano.

## Entrega
Resumen ejecutivo, autorización y alcance, metodología, cobertura real, hallazgos (severidad, impacto, reproducción, remediación), retest y limitaciones.

## Ejemplo
Hallazgo: con la cuenta de pruebas A, `GET /facturas/102` devuelve la factura de la cuenta de pruebas B. Severidad alta. Remediación: comprobar propietario en el servidor. No se enumeraron otras facturas.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
