#!/usr/bin/env python3
"""Valida estructura, metadatos, fuentes y catálogo de las Skills. Solo biblioteca estándar.

Uso: python3 scripts/validate_skills.py [--root RUTA]
Código de salida: 0 sin errores, 1 con errores. Los avisos no hacen fallar.
No comprueba si el contenido es correcto ni si una Skill se activa: para eso
ver scripts/test_triggers.py y la revisión de references/sources.md.
"""
import argparse
import json
import re
import sys
from pathlib import Path

CAMPOS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
SECCIONES = ["Alcance", "Verificación", "Ejemplo", "Fuentes"]
RESERVADAS = ("anthropic", "claude")
REF = re.compile(r"`((?:references|scripts|assets)/[^`\s]+)`")
ap = argparse.ArgumentParser()
ap.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
raiz = Path(ap.parse_args().root)
carpeta = raiz / ".claude" / "skills"
errores, avisos, nombres, listado = [], [], [], 0


def error(skill, texto):
    errores.append(f"{skill}: {texto}")


for d in sorted(p for p in carpeta.iterdir() if p.is_dir()):
    n = d.name
    nombres.append(n)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", n) or len(n) > 64:
        error(n, "nombre de carpeta no válido")
    if any(r in n for r in RESERVADAS):
        error(n, "el nombre contiene una palabra reservada")
    f = d / "SKILL.md"
    if not f.is_file():
        error(n, "falta SKILL.md")
        continue
    texto = f.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", texto, re.S)
    if not m:
        error(n, "frontmatter ausente o sin cierre")
        continue
    front, cuerpo = m.groups()
    claves = re.findall(r"(?m)^([A-Za-z-]+):", front)
    for c in set(claves) - CAMPOS:
        error(n, f"campo no admitido fuera de Claude Code: {c}")
    nm = re.search(r"(?m)^name:\s*(\S+)\s*$", front)
    if not nm or nm.group(1) != n:
        error(n, "name ausente o distinto de la carpeta")
    ds = re.search(r"(?m)^description:\s*(.+)$", front)
    if not ds:
        error(n, "falta description")
        continue
    desc = ds.group(1).strip()
    if desc.startswith('"'):
        try:
            desc = json.loads(desc)
        except ValueError:
            error(n, "description entre comillas mal formada")
    if not desc or len(desc) > 1024 or "<" in desc or ">" in desc:
        error(n, "description vacía, mayor de 1024 caracteres o con < >")
    if "usar" not in desc.lower() and "úsala" not in desc.lower():
        error(n, "description no indica cuándo usarla")
    listado += len(n) + len(desc)
    if cuerpo.count("\n") >= 500:
        error(n, "el cuerpo supera las 500 líneas")
    for s in SECCIONES:
        if not re.search(rf"(?m)^## {s}\b", cuerpo):
            error(n, f"falta la sección {s}")
    fuentes = d / "references" / "sources.md"
    if not fuentes.is_file():
        error(n, "falta references/sources.md")
    else:
        contenido = fuentes.read_text(encoding="utf-8")
        filas = re.findall(r"(?m)^\| (Leída|Localizada) \| \[[^\]]+\]\((https?://[^)\s]+)\)", contenido)
        if not any(e == "Leída" for e, _ in filas):
            error(n, "sources.md no tiene ninguna fuente leída")
    for r in set(REF.findall(cuerpo)):
        if not (d / r).exists():
            error(n, f"referencia inexistente: {r}")
    for otra in set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", cuerpo)):
        if otra.endswith(("-engineering", "-documentation", "-management", "-analysis", "-testing", "-modeling", "-review")) and not (carpeta / otra).is_dir():
            error(n, f"cita una Skill inexistente: {otra}")

catalogo = raiz / "docs" / "CATALOG.md"
if catalogo.is_file():
    cat = set(re.findall(r"(?m)^\| `([a-z0-9-]+)` \|", catalogo.read_text(encoding="utf-8")))
    for x in sorted(set(nombres) - cat):
        errores.append(f"catálogo: falta {x}")
    for x in sorted(cat - set(nombres)):
        errores.append(f"catálogo: sobra {x}")
else:
    errores.append("falta docs/CATALOG.md")

print(f"Skills encontradas: {len(nombres)}")
print(f"Tamaño del listado (nombres y descripciones): {listado} caracteres")
for a in avisos:
    print("AVISO:", a)
if errores:
    print("VALIDACIÓN CON ERRORES:")
    for e in errores:
        print(f"- {e}")
    sys.exit(1)
print("Validación completada sin errores.")
