from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
import urllib.parse

def get_anchors(text: str) -> set:
    anchors = set()
    for match in re.finditer(r'^(#{1,6})\s+(.+)$', text, re.MULTILINE):
        heading = match.group(2).strip()
        slug = heading.lower()
        slug = re.sub(r'[^\w\- ]', '', slug)
        slug = slug.replace(' ', '-')
        if slug:
            anchors.add(slug)
    for match in re.finditer(r'<(?:a|[\w]+)[^>]+(?:id|name)="([^"]+)"', text, re.IGNORECASE):
        anchors.add(match.group(1))
    return anchors

file_cache = {}
def get_file_info(filepath: Path):
    if filepath not in file_cache:
        try:
            text = filepath.read_text(encoding="utf-8")
            file_cache[filepath] = {
                'text': text,
                'anchors': get_anchors(text)
            }
        except Exception:
            file_cache[filepath] = None
    return file_cache[filepath]

def validate_catalog(root_dir: Path) -> list:
    errors = []
    seen_names = {}
    
    for directory in ["skills", "prompts", "workflows", "agents"]:
        base = root_dir / directory
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".md", ".markdown"}:
                continue
            text = path.read_text(encoding="utf-8")
            rel = path.relative_to(root_dir).as_posix()
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

    # Check relative Markdown links point to existing files and anchors.
    for path in root_dir.rglob("*.md"):
        if any(part in {".git", ".github"} for part in path.parts):
            continue
        
        info = get_file_info(path)
        if not info:
            continue
        text = info['text']
        
        for raw_target in re.findall(r"\]\(([^)]+)\)", text):
            link = raw_target.split()[0]
            if link.startswith(("http://", "https://", "mailto:")):
                continue
                
            parsed = urllib.parse.urlparse(link)
            file_path_part = urllib.parse.unquote(parsed.path)
            anchor_part = parsed.fragment
            
            target_path = path
            if file_path_part:
                target_path = (path.parent / file_path_part).resolve()
            
            try:
                target_path.relative_to(root_dir.resolve())
            except ValueError:
                continue
                
            if not target_path.exists():
                errors.append(f"Broken internal link in {path.relative_to(root_dir)}: {link} (Missing file)")
                continue
                
            if anchor_part and target_path.is_file() and target_path.suffix.lower() in {".md", ".markdown"}:
                target_info = get_file_info(target_path)
                if target_info:
                    if anchor_part not in target_info['anchors']:
                        errors.append(f"Broken internal link in {path.relative_to(root_dir)}: {link} (Missing anchor '{anchor_part}')")

    catalog = root_dir / "CATALOG.md"
    if not catalog.exists():
        errors.append("CATALOG.md is missing")

    return errors

if __name__ == "__main__":
    ROOT = Path(__file__).resolve().parents[1]
    errors = validate_catalog(ROOT)
    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        raise SystemExit(1)
    
    print("Atlas validation passed.")
