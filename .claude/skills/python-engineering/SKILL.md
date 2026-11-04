---
name: python-engineering
description: "Estructura y mantiene proyectos Python: pyproject.toml, entornos virtuales, tipado, pruebas, empaquetado y versiones con soporte. Usar al crear, ordenar o modernizar código Python."
---

# Python Engineering

## Alcance
Proyecto y prácticas de Python. No cubre:
- Pipelines de datos: `data-engineering`.
- Diseño de APIs: `api-engineering`.

## Procedimiento
1. Identifica versión (`python3 --version`), `requires-python`, gestor de dependencias y estructura existentes. No cambies de herramienta sin motivo.
2. Confirma en la página oficial que la versión tiene soporte. Una en fase `security` solo recibe parches de seguridad.
3. Usa siempre un entorno aislado: `python3 -m venv .venv`.
4. Centraliza en `pyproject.toml`: `[build-system]`, `[project]` y `[tool]`.
5. Fija dependencias reproducibles con el mecanismo adoptado (lockfile o requirements con versiones).
6. Añade anotaciones de tipos en interfaces públicas y comprueba con el verificador del proyecto.
7. Maneja excepciones específicas; nunca uses `except:` vacío.
8. Para archivos, usa `pathlib` y `with`. Para registro, `logging` en vez de `print` en servicios.
9. Prueba con el framework del proyecto, incluidos casos límite.

## Reglas
- No instales en el Python del sistema.
- No uses valores por defecto mutables (`def f(x=[])`).
- No ejecutes `pickle.loads`, `eval` ni `yaml.load` sin `SafeLoader` sobre datos no confiables.
- Usa `pip-audit` u otra herramienta para detectar vulnerabilidades conocidas; no detecta paquetes maliciosos.

## Verificación
Instalación limpia en un entorno nuevo, pruebas ejecutadas, verificador de tipos y linter sin errores nuevos.

## Entrega
Cambios, versión objetivo, comandos ejecutados, resultados y limitaciones.

## Ejemplo
```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "facturacion"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []
```
Ajusta `requires-python` a las versiones realmente probadas.

## Fuentes
Consulta `references/sources.md` cuando la tarea dependa de una versión, norma o comportamiento concreto, y confirma allí el dato antes de afirmarlo.
