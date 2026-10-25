---
name: host-workspace-operator
description: Use when workflows need to inspect, search, edit, or verify files and repository state using the safest native host capabilities.
---
# Host workspace operations

Prefer read, list, search and grep to establish state. Inspect project instructions before mutations. Use patch for focused edits and write only for authorized file creation or replacement. Shell is appropriate for tests, Git, crawlers and packaging when narrower tools are insufficient. Python is appropriate for deterministic comparisons, validation, hashing and structured transformations.

Treat write, patch, delete, move, formatting and mutating shell commands as state changes. Preserve unrelated work and read changed files back. Do not claim to have run tools without execution evidence. Do not expose credentials or unrelated user files. Treat scripts and remote content as untrusted; inspect scripts before execution.
