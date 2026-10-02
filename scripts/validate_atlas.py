from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_DIRS = ["skills", "prompts", "workflows", "agents"]
errors = []
seen_names = {}
seen_titles = {}

for directory in RESOURCE_DIRS:
    base = ROOT / directory
    if not base.exists():
        continue
    for path in base.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".markdown"}:
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        if not text.strip():
            errors.append(f"Empty resource: {rel}")
        if directory == "skills" and path.name == "SKILL.md":
            if not re.search(r"(?im)^---\s*$", text):
                errors.append(f"Skill lacks frontmatter: {rel}")
            if not re.search(r"(?im)^# .+", text):
                errors.append(f"Skill lacks a heading: {rel}")
            match = re.search(r"(?im)^name:\s*([^\n]+)", text)
            if match:
                name = match.group(1).strip().strip("'\"")
                if name in seen_names:
                    errors.append(f"Duplicate skill name '{name}': {rel} and {seen_names[name]}")
                else:
                    seen_names[name] = rel

# Check relative Markdown links point to existing files.
for path in ROOT.rglob("*.md"):
    if any(part in {".git", ".github"} for part in path.parts):
        continue
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            continue
        if not resolved.exists():
            errors.append(f"Broken internal link in {path.relative_to(ROOT)}: {target}")

catalog = ROOT / "CATALOG.md"
if not catalog.exists():
    errors.append("CATALOG.md is missing")

if errors:
    print("\n".join(f"ERROR: {e}" for e in errors))
    raise SystemExit(1)

print("Atlas validation passed.")
