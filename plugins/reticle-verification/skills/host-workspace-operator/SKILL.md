---
name: host-workspace-operator
description: Use when a Reticle verification task needs local repository or file inspection, project setup, code changes, or command execution. Prefer read-only discovery first and keep writes and commands within explicit user authorization.
---

# Host workspace operations

Use host-provided file, repository, shell, and Python capabilities when they are available. This skill does not grant any permissions.

1. Read repository instructions before editing.
2. Use read/list/search/grep for discovery and establish the current state before changes.
3. Treat file creation, edits, deletes, formatting, and mutating shell commands as state changes. Perform them only when requested or authorized.
4. Prefer focused patches over broad replacements. Preserve unrelated changes.
5. Inspect commands and target scripts before executing them. Do not run untrusted scripts automatically.
6. Run relevant tests and validators when the host provides execution. Do not claim a command ran without evidence.
7. Read changed files back when practical and report the exact files changed and verification results.
8. Use Python for deterministic parsing, comparisons, hashes, and package inspection when available; never claim execution if unavailable.
9. Do not expose secrets, tokens, credentials, captured customer data, or unrelated files in output.
