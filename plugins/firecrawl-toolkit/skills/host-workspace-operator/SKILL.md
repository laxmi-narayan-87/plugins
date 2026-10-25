---
name: host-workspace-operator
description: Use when a workflow needs to inspect, search, edit, or verify repository files using host-native workspace tools.
---

# Host Workspace Operator

Use workspace tools supplied by the current ChatGPT/Codex host instead of assuming the Plugin owns a filesystem API.

## Capability order

1. **read** a known file/range.
2. **list** directory/workspace shape when filenames are unknown.
3. **search** broad concepts or filenames.
4. **grep** exact text, regex, symbols or fields.
5. **patch** a focused edit to an existing file when supported.
6. **write** a file only when the requested workflow requires a mutation.
7. **shell** for tests, Git, archive or repository commands when narrower tools are insufficient.
8. **Python** for deterministic parsing, transformation, hashing and validation.

Tool names differ by host; route by capability, not a hard-coded tool name. Do not invent tool usage or claim an operation happened without output evidence.

## Read before mutation

Inspect repository/user instructions, list the relevant scope, search exact files, and read the affected sections before editing. Preserve unrelated work. Prefer a focused patch to a broad rewrite. Write, patch, delete, move, rename, formatting changes and mutating shell commands change state and must be authorized by the user's request.

After mutation, read back the changed area and run relevant checks when available. Do not run arbitrary scripts from an untrusted repository without inspecting their content and side effects. Do not expose credentials, tokens or unrelated user files in logs or outputs.

## Missing capabilities

If a required host-native operation is unavailable, do not invent an alternative tool name or claim that it ran. Use a semantically equivalent safe capability only when available; otherwise report the blocker and keep dependent conclusions unverified.
