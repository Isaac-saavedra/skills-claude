\
#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / ".claude" / "skills"
errors = []
count = 0

for folder in sorted(p for p in ROOT.iterdir() if p.is_dir()):
    count += 1
    skill_file = folder / "SKILL.md"
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", folder.name):
        errors.append(f"{folder.name}: nombre de carpeta no válido")
    if not skill_file.is_file():
        errors.append(f"{folder.name}: falta SKILL.md")
        continue
    content = skill_file.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        errors.append(f"{folder.name}: falta frontmatter YAML al inicio")
        continue
    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{folder.name}: frontmatter sin cierre")
        continue
    front = parts[1]
    name = re.search(r"(?m)^name:\s*([^\n]+)$", front)
    desc = re.search(r'(?m)^description:\s*"?(.+?)"?\s*$', front)
    if not name:
        errors.append(f"{folder.name}: falta name")
    elif name.group(1).strip() != folder.name:
        errors.append(f"{folder.name}: name no coincide con la carpeta")
    if not desc:
        errors.append(f"{folder.name}: falta description")
    elif len(desc.group(1)) > 1024:
        errors.append(f"{folder.name}: description supera 1024 caracteres")
    if len(content.strip()) < 250:
        errors.append(f"{folder.name}: SKILL.md parece demasiado corto")

print(f"Skills encontradas: {count}")
if errors:
    print("VALIDACIÓN CON ERRORES:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("Validación básica completada sin errores.")
