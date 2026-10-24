#!/usr/bin/env python3
"""Structural validation for the plugin package archive.

This deliberately does not claim to validate upstream runtime behavior.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ROOT / "plugins"
errors: list[str] = []
warnings: list[str] = []

def fail(message: str) -> None:
    errors.append(message)

if not PLUGINS.is_dir():
    fail("Missing plugins/ directory")
else:
    package_dirs = sorted(p for p in PLUGINS.iterdir() if p.is_dir())
    if not package_dirs:
        fail("No plugin package directories found")

    for package in package_dirs:
        manifests = list(package.rglob("plugin.json"))
        if not manifests:
            warnings.append(f"{package.name}: no plugin.json found")
        for path in package.rglob("*.json"):
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, json.JSONDecodeError) as exc:
                fail(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")

        for path in package.rglob("SKILL.md"):
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                fail(f"{path.relative_to(ROOT)}: cannot read UTF-8: {exc}")
                continue
            match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.S)
            if not match:
                fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
                continue
            frontmatter = match.group(1)
            if not re.search(r"^name\s*:\s*\S", frontmatter, re.M):
                fail(f"{path.relative_to(ROOT)}: frontmatter missing name")
            if not re.search(r"^description\s*:\s*\S", frontmatter, re.M):
                fail(f"{path.relative_to(ROOT)}: frontmatter missing description")

        # Validate relative references explicitly written as Markdown links.
        for path in package.rglob("*.md"):
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                fail(f"{path.relative_to(ROOT)}: cannot read UTF-8: {exc}")
                continue
            for target in re.findall(r"\]\(([^)]+)\)", text):
                target = target.strip().split("#", 1)[0]
                if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    fail(f"{path.relative_to(ROOT)}: broken Markdown link target {target!r}")

readme = ROOT / "README.md"
if not readme.exists():
    fail("Missing root README.md")

for warning in warnings:
    print(f"WARNING: {warning}")
for error in errors:
    print(f"ERROR: {error}", file=sys.stderr)

if errors:
    print(f"Archive validation failed: {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1)

print(f"Archive validation passed: {len([p for p in PLUGINS.iterdir() if p.is_dir()])} package(s); {len(warnings)} warning(s)")
