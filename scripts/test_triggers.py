#!/usr/bin/env python3
"""Mide si Claude Code elige la Skill esperada. Consume uso de la cuenta.

Uso: python3 scripts/test_triggers.py [--jobs 4] [--out resultados.json]
Requisitos: CLI `claude` autenticada; ejecutar desde la raíz del repositorio.
Solo observa la primera decisión del modelo (--max-turns 1); no ejecuta las tareas.
"""
import argparse
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--jobs", type=int, default=4)
ap.add_argument("--out", default="")
ap.add_argument("--only", default="", help="Skills separadas por comas")
ap.add_argument("--repeat", type=int, default=1)
args = ap.parse_args()
casos = json.loads(Path("tests/trigger_cases.json").read_text(encoding="utf-8"))
if args.only:
    casos = [c for c in casos if c[0] in args.only.split(",")]
casos = casos * args.repeat


def correr(caso):
    esperado, prompt = caso
    try:
        r = subprocess.run(["claude", "-p", prompt, "--max-turns", "1", "--output-format", "stream-json", "--verbose"],
                           capture_output=True, text=True, timeout=240)
    except subprocess.TimeoutExpired:
        return {"esperado": esperado, "obtenido": "TIMEOUT", "prompt": prompt}
    obtenido, primera = None, None
    for linea in r.stdout.splitlines():
        try:
            ev = json.loads(linea)
        except ValueError:
            continue
        if ev.get("type") != "assistant":
            continue
        for b in ev["message"].get("content", []):
            if b.get("type") == "tool_use":
                primera = primera or b.get("name")
                if b.get("name") == "Skill" and obtenido is None:
                    obtenido = b["input"].get("skill")
    return {"esperado": esperado, "obtenido": obtenido, "primera_herramienta": primera, "prompt": prompt}


with ThreadPoolExecutor(args.jobs) as ex:
    res = list(ex.map(correr, casos))
ok = [r for r in res if r["esperado"] == r["obtenido"]]
print(f"Aciertos: {len(ok)}/{len(res)}")
for r in res:
    if r["esperado"] != r["obtenido"]:
        print(f"- esperado={r['esperado']} obtenido={r['obtenido']} primera={r.get('primera_herramienta')} :: {r['prompt'][:70]}")
if args.out:
    Path(args.out).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
