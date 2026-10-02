from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
groups = {"Skills":"skills", "Prompts":"prompts", "Workflows":"workflows", "Agents":"agents"}
lines = ["# Atlas Catalog", "", "Generated from repository resources. Do not edit manually.", ""]
for title, directory in groups.items():
    lines += [f"## {title}", ""]
    base = ROOT / directory
    if not base.exists():
        lines += ["_No resources yet._", ""]
        continue
    found = []
    for path in sorted(base.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        heading = re.search(r"(?m)^#\s+(.+)$", text)
        name = heading.group(1).strip() if heading else path.stem
        found.append((name, rel))
    if not found:
        lines += ["_No resources yet._", ""]
    else:
        for name, rel in found:
            lines.append(f"- [{name}]({rel})")
        lines.append("")
(ROOT / "CATALOG.md").write_text("\n".join(lines), encoding="utf-8")
print("Generated CATALOG.md")
