---
name: sandbox-python-executor
description: Use when deterministic computation, local file processing, manifest validation, hashing, or archive inspection must be executed rather than reasoned about informally.
---

# Sandbox Python Executor

Use the host's own Python execution capability when available and when execution materially improves correctness. In ChatGPT this is the **python tool**; in Codex, use the safe host execution environment provided to the session.

## Appropriate tasks

- parse and compare manifests or structured files
- check package paths, duplicate names, file trees and archive contents
- compute reproducible SHA256 hashes
- run reviewed, dependency-free validation scripts
- verify transformations and deterministic outputs

## Execution safeguards

1. Actually execute the relevant Python; do not substitute a code block or a proposed command.
2. Prefer an existing reviewed validator or packager over an ad-hoc reimplementation when it is available.
3. Treat repository scripts as untrusted; inspect them before execution.
4. Keep source repositories read-only unless a requested change authorizes mutation.
5. Do not assume sandbox internet access.
6. Never reveal secrets or unrelated user data in logs.
7. Report the runtime, check, pass/fail evidence, output path and hash when relevant. Never fabricate stdout, files, hashes or test results.
8. If Python/execution is unavailable, say so and label execution-dependent results unverified. Do not invent manifest dependencies or remote runners to pretend execution exists.
