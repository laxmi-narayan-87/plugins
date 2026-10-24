#!/usr/bin/env python3
"""Structural validation for the plugin package archive."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ROOT / "plugins"
errors = []
warnings = []

def error(message):
    errors.append(message)

if not PLUGINS.is_dir():
    error("Missing plugins/ directory")
else:
    packages = sorted(p for p in PLUGINS.iterdir() if p.is_dir())
    if not packages:
        error("No package directories found")
    for package in packages:
        manifests = list(package.rglob("plugin.json"))
        if not manifests:
            warnings.append(f"{package.name}: no plugin.json found")
        for path in package.rglob("*.json"):
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, json.JSONDecodeError) as exc:
                error(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        for path in package.rglob("SKILL.md"):
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                error(f"{path.relative_to(ROOT)}: cannot read UTF-8: {exc}")
                continue
            match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.S)
            if not match:
                error(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
                continue
            fm = match.group(1)
            if not re.search(r"^name\s*:\s*\S", fm, re.M):
                error(f"{path.relative_to(ROOT)}: frontmatter missing name")
            if not re.search(r"^description\s*:\s*\S", fm, re.M):
                error(f"{path.relative_to(ROOT)}: frontmatter missing description")
        for path in package.rglob("*.md"):
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                error(f"{path.relative_to(ROOT)}: cannot read UTF-8: {exc}")
                continue
            for target in re.findall(r"\]\(([^)]+)\)", text):
                target = target.strip().split("#", 1)[0]
                if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                    continue
                if not (path.parent / target).resolve().exists():
                    error(f"{path.relative_to(ROOT)}: broken Markdown link {target!r}")

if not (ROOT / "README.md").exists():
    error("Missing root README.md")
for item in warnings:
    print("WARNING:", item)
for item in errors:
    print("ERROR:", item, file=sys.stderr)
if errors:
    print(f"Failed: {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1)
print(f"Passed: {len([p for p in PLUGINS.iterdir() if p.is_dir()])} package(s), {len(warnings)} warning(s)")
