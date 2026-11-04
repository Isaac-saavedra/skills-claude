#!/usr/bin/env python3
"""Inventario de solo lectura de un repositorio. Solo biblioteca estándar; sin red.

Uso: python3 inventory.py <ruta>
No lee el contenido de archivos de secretos: solo informa de su ubicación.
"""
import collections
import fnmatch
import os
import subprocess
import sys
from pathlib import Path

IGNORAR = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", "target", "vendor", ".terraform"}
MANIFIESTOS = {
    "package.json": "Node.js", "pyproject.toml": "Python", "requirements.txt": "Python",
    "go.mod": "Go", "Cargo.toml": "Rust", "pom.xml": "Java (Maven)", "build.gradle": "Java/Kotlin (Gradle)",
    "composer.json": "PHP", "Gemfile": "Ruby", "pubspec.yaml": "Flutter/Dart",
}
LOCKFILES = {"package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock", "uv.lock", "Pipfile.lock",
             "go.sum", "Cargo.lock", "composer.lock", "Gemfile.lock", "pubspec.lock", ".terraform.lock.hcl"}
DOCS = {"README.md", "README", "CONTRIBUTING.md", "CLAUDE.md", "AGENTS.md", "CHANGELOG.md", "LICENSE"}
INFRA = {"Dockerfile", "docker-compose.yml", "docker-compose.yaml", "compose.yaml", "Makefile", "Jenkinsfile", ".gitlab-ci.yml"}
SECRETOS = [".env", ".env.*", "*.pem", "*.key", "id_rsa", "id_ed25519", "credentials*.json", "*.tfstate", "*.tfstate.*"]
PERMITIDOS = {".env.example", ".env.sample", ".env.template"}


def git(raiz, *args):
    try:
        r = subprocess.run(["git", "-C", str(raiz), *args], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return r.stdout.strip() if r.returncode == 0 else None


def seccion(titulo, valores):
    print(f"\n## {titulo}")
    for v in valores or ["(ninguno detectado)"]:
        print(f"- {v}")


def main():
    if len(sys.argv) != 2:
        sys.exit("Uso: python3 inventory.py <ruta>")
    raiz = Path(sys.argv[1]).resolve()
    if not raiz.is_dir():
        sys.exit(f"No es un directorio: {raiz}")

    ext, manif, locks, docs, infra, ci, sec, pruebas = collections.Counter(), [], [], [], [], [], [], []
    total = 0
    for actual, carpetas, archivos in os.walk(raiz):
        carpetas[:] = sorted(c for c in carpetas if c not in IGNORAR)
        rel = Path(actual).relative_to(raiz)
        for nombre in sorted(archivos):
            total += 1
            ruta = (rel / nombre).as_posix()
            ext[Path(nombre).suffix.lower() or "(sin extensión)"] += 1
            if nombre in MANIFIESTOS:
                manif.append(f"{ruta} ({MANIFIESTOS[nombre]})")
            if nombre in LOCKFILES:
                locks.append(ruta)
            if nombre in DOCS:
                docs.append(ruta)
            if nombre in INFRA or nombre.endswith(".tf"):
                infra.append(ruta)
            if ruta.startswith(".github/workflows/") or nombre == ".gitlab-ci.yml":
                ci.append(ruta)
            if nombre not in PERMITIDOS and any(fnmatch.fnmatch(nombre, p) for p in SECRETOS):
                sec.append(ruta)
            partes = {p.lower() for p in rel.parts}
            if partes & {"test", "tests", "__tests__", "spec"} or ".test." in nombre or ".spec." in nombre or nombre.startswith("test_"):
                pruebas.append(ruta)

    print(f"# Inventario de {raiz.name}\nArchivos analizados: {total}")
    seccion("Extensiones más frecuentes", [f"{e}: {n}" for e, n in ext.most_common(12)])
    seccion("Manifiestos", manif)
    seccion("Lockfiles", locks)
    if manif and not locks:
        print("- AVISO: hay manifiestos pero ningún lockfile reconocido.")
    seccion("Documentación", docs)
    seccion("Infraestructura y automatización", infra[:40])
    seccion("CI", ci)
    seccion(f"Pruebas (archivos: {len(pruebas)}; primeros 15)", pruebas[:15])
    seccion("Posibles archivos sensibles (contenido no leído)", sec)
    rama = git(raiz, "rev-parse", "--abbrev-ref", "HEAD")
    if rama is None:
        print("\n## Git\n- No es un repositorio Git o no está disponible.")
    else:
        seccion("Git", [f"Rama: {rama}", f"Commits: {git(raiz, 'rev-list', '--count', 'HEAD')}",
                        f"Último: {git(raiz, 'log', '-1', '--format=%h %ad %s', '--date=short')}"])


if __name__ == "__main__":
    main()
