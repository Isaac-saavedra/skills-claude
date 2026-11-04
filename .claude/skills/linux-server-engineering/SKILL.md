---
name: linux-server-engineering
description: "Administra servidores Linux: systemd, SSH, firewall, usuarios, paquetes, logs y endurecimiento. Usar con Ubuntu, Debian o RHEL, servicios caídos, disco lleno o configuración de un servidor."
---

# Linux Server Engineering

## Alcance
Administración de un host Linux. No cubre:
- Contenedores: `docker-engineering`.
- Clústeres: `kubernetes-engineering`.

## Procedimiento
1. Identifica sistema y versión: `cat /etc/os-release`, `uname -r`. Las rutas y herramientas varían por distribución.
2. Diagnostica antes de cambiar, con solo lectura:
   ```bash
   systemctl status <servicio>
   journalctl -u <servicio> --since "1 hour ago"
   df -h; df -i; free -h; ss -tulpn
   ```
3. Respalda cada archivo antes de modificarlo.
4. Valida la configuración antes de aplicar: por ejemplo, `sudo sshd -t` o `nginx -t`.
5. Cambia una cosa cada vez y comprueba.

## SSH
- Usa claves `ed25519` con passphrase.
- En Ubuntu, los fragmentos en `/etc/ssh/sshd_config.d/` tienen prioridad porque gana el primer valor leído.
- Por defecto, `PasswordAuthentication` es `yes` y `PermitRootLogin` es `prohibit-password` en OpenSSH; revisa la configuración efectiva con `sudo sshd -T`.
- **Mantén abierta una sesión** y prueba una segunda conexión antes de cerrarla.

## Servicios con systemd
```ini
[Service]
User=app
NoNewPrivileges=yes
ProtectSystem=strict
ProtectHome=yes
Restart=on-failure
```
Comprueba estas opciones con tu versión. `ProtectSystem=strict` deja el sistema en solo lectura: declara las rutas de escritura.

## Reglas
- No ejecutes `rm -rf`, reformateos, cambios de firewall ni reinicios en producción sin autorización.
- Antes de activar el firewall, permite la vía de administración, para no perder el acceso.
- Prueba en un entorno aparte, con acceso de consola de emergencia.
- No desactives SELinux o AppArmor para resolver un error de permisos sin analizarlo.

## Verificación
Servicio activo, registros sin errores nuevos, segunda conexión SSH correcta y prueba funcional tras reiniciar el servicio.

## Entrega
Sistema, diagnóstico, comandos ejecutados, cambios con respaldo, resultado y reversión.

## Ejemplo
Disco al 100 %: `du -xh / --max-depth=2 | sort -h` revela registros de 40 GB. Se propone configurar rotación y se pide autorización antes de borrar nada.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
