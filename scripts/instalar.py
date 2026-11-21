#!/usr/bin/env python3
"""Instala la biblioteca en ~/.claude: Skills, instrucciones globales y ajustes.

Uso:
  python3 scripts/instalar.py             # simulación: muestra qué cambiaría
  python3 scripts/instalar.py --aplicar   # respalda y aplica

Qué hace al aplicar:
  1. Respalda ~/.claude/skills (sin synced/), CLAUDE.md, CLAUDE-omc.md y settings.json
     en ~/.claude-respaldos/<fecha>.tar.gz.
  2. Copia cada Skill del repositorio a ~/.claude/skills/<skill>/, reemplazándola.
     Retira solo las Skills que una instalación anterior registró como propias y que
     ya no están en el repositorio. Nunca toca synced/ ni Skills de otras fuentes.
  3. Instala global/CLAUDE.md como ~/.claude/CLAUDE.md. Si el archivo actual tiene un
     bloque de oh-my-claudecode y no existe ~/.claude/CLAUDE-omc.md, guarda ese bloque
     allí (es el archivo que carga `omc launch`).
  4. Fusiona global/ajustes.json en ~/.claude/settings.json: solo esas claves; el resto
     de la configuración queda igual.
  5. Registra lo instalado en ~/.claude/skills/.skills-claude.json.

Restaurar: extrae el respaldo sobre ~/.claude (ver README).
"""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tarfile
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ORIGEN = REPO / ".claude" / "skills"
CLAUDE = Path.home() / ".claude"
DESTINO = CLAUDE / "skills"
MANIFIESTO = DESTINO / ".skills-claude.json"
RESPALDOS = Path.home() / ".claude-respaldos"
MARCA_OMC = "<!-- OMC:START -->"
PROTEGIDAS = {"synced"}

ap = argparse.ArgumentParser()
ap.add_argument("--aplicar", action="store_true", help="aplica los cambios (sin esto, solo simula)")
args = ap.parse_args()


def huella(carpeta: Path) -> str:
    h = hashlib.sha256()
    for f in sorted(p for p in carpeta.rglob("*") if p.is_file()):
        h.update(str(f.relative_to(carpeta)).encode())
        h.update(f.read_bytes())
    return h.hexdigest()


def leer_json(ruta: Path) -> dict:
    if not ruta.exists():
        return {}
    try:
        return json.loads(ruta.read_text(encoding="utf-8"))
    except ValueError:
        sys.exit(f"ERROR: {ruta} no es JSON válido; corrígelo antes de instalar.")


# --- validación previa: no se instala una biblioteca rota ---
r = subprocess.run([sys.executable, str(REPO / "scripts" / "validate_skills.py")], capture_output=True, text=True)
if r.returncode != 0:
    sys.exit("ERROR: la validación falló; no se instala nada.\n" + r.stdout)

skills = sorted(p.name for p in ORIGEN.iterdir() if p.is_dir())
choque = PROTEGIDAS.intersection(skills)
if choque:
    sys.exit(f"ERROR: el repositorio usa nombres reservados: {choque}")
previo = leer_json(MANIFIESTO)
propias_antes = set(previo.get("skills", [])) or set(skills)  # primera vez: las del repo
retirar = sorted(propias_antes - set(skills) - PROTEGIDAS)

plan = []
for s in skills:
    d = DESTINO / s
    if not d.exists():
        plan.append(("nueva", s))
    elif huella(d) != huella(ORIGEN / s):
        plan.append(("actualiza", s))
for s in retirar:
    if (DESTINO / s).exists():
        plan.append(("retira", s))

claude_md = CLAUDE / "CLAUDE.md"
global_md = (REPO / "global" / "CLAUDE.md").read_text(encoding="utf-8")
actual_md = claude_md.read_text(encoding="utf-8") if claude_md.exists() else ""
omc_md = CLAUDE / "CLAUDE-omc.md"
mover_omc = MARCA_OMC in actual_md and not omc_md.exists()

ajustes = leer_json(REPO / "global" / "ajustes.json")
settings_path = CLAUDE / "settings.json"
settings = leer_json(settings_path)
nuevo = dict(settings)
for k, v in ajustes.items():
    nuevo[k] = {**settings.get(k, {}), **v} if isinstance(v, dict) and isinstance(settings.get(k), dict) else v

print(f"Repositorio: {REPO}")
print(f"Skills en el repositorio: {len(skills)}")
for accion, s in plan:
    print(f"  {accion:9} {s}")
if not plan:
    print("  (todas las Skills ya están al día)")
print(f"CLAUDE.md global: {'sin cambios' if actual_md == global_md else 'se reemplaza'}"
      + (" (el bloque de oh-my-claudecode pasa a CLAUDE-omc.md)" if mover_omc else ""))
print(f"settings.json: {'sin cambios' if nuevo == settings else 'se actualizan ' + ', '.join(ajustes)}")

if not args.aplicar:
    print("\nSimulación. Ejecuta con --aplicar para instalar.")
    sys.exit(0)

# --- 1. respaldo ---
RESPALDOS.mkdir(exist_ok=True)
copia = RESPALDOS / f"claude-{time.strftime('%Y%m%d-%H%M%S')}.tar.gz"
with tarfile.open(copia, "w:gz") as tar:
    if DESTINO.exists():
        tar.add(DESTINO, arcname="skills", filter=lambda t: None if t.name.startswith("skills/synced") else t)
    for f in (claude_md, omc_md, settings_path):
        if f.exists():
            tar.add(f, arcname=f.name)
with tarfile.open(copia, "r:gz") as tar:  # comprobar que se puede leer
    n = len(tar.getmembers())
print(f"\nRespaldo: {copia} ({n} entradas)")

# --- 2. Skills ---
DESTINO.mkdir(parents=True, exist_ok=True)
for accion, s in plan:
    d = DESTINO / s
    if d.exists():
        shutil.rmtree(d)
    if accion != "retira":
        shutil.copytree(ORIGEN / s, d)
for s in skills:
    if huella(DESTINO / s) != huella(ORIGEN / s):
        sys.exit(f"ERROR: {s} no quedó igual que en el repositorio. Restaura desde {copia}")

# --- 3. CLAUDE.md global ---
if mover_omc:
    omc_md.write_text(actual_md, encoding="utf-8")
    print(f"Bloque de oh-my-claudecode guardado en {omc_md}")
claude_md.write_text(global_md, encoding="utf-8")

# --- 4. settings.json ---
if nuevo != settings:
    tmp = settings_path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(nuevo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    json.loads(tmp.read_text(encoding="utf-8"))
    tmp.replace(settings_path)

# --- 5. manifiesto ---
commit = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
MANIFIESTO.write_text(json.dumps({"origen": str(REPO), "commit": commit or None,
                                  "instalado": time.strftime("%Y-%m-%d %H:%M:%S"), "skills": skills},
                                 ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Instalado: {len(skills)} Skills, CLAUDE.md y ajustes (commit {commit or 'sin commit'}).")
print("Reinicia Claude Code para que cargue los cambios.")
