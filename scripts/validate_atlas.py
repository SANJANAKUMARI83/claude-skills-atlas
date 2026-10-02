from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_DIRS = ["skills", "prompts", "workflows", "agents"]
errors = []

for directory in RESOURCE_DIRS:
    base = ROOT / directory
    if not base.exists():
        continue
    for path in base.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".markdown"}:
            text = path.read_text(encoding="utf-8")
            if not text.strip():
                errors.append(f"Empty resource: {path.relative_to(ROOT)}")
            if directory == "skills" and path.name == "SKILL.md":
                if not re.search(r"(?im)^---\s*$", text):
                    errors.append(f"Skill lacks frontmatter: {path.relative_to(ROOT)}")
                if not re.search(r"(?im)^# .+", text):
                    errors.append(f"Skill lacks a heading: {path.relative_to(ROOT)}")

catalog = ROOT / "CATALOG.md"
if not catalog.exists():
    errors.append("CATALOG.md is missing")

if errors:
    print("\n".join(f"ERROR: {e}" for e in errors))
    raise SystemExit(1)

print("Atlas validation passed.")
