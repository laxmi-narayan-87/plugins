---
name: sandbox-python-executor
description: Use when deterministic parsing, URL normalization, report generation, screenshot-diff computation, archive inspection, hashing or validation should be executed rather than guessed.
---
# Deterministic verification

Use an actual host-provided Python/runtime when available. Prefer reproducible scripts that:
- normalize URLs and detect duplicate routes
- validate JSON/CSV output against explicit schemas
- compare crawled inventories and internal/external link sets
- compute hashes and exact/pixel image diffs
- inspect package contents and referenced paths
- summarize status codes, missing metadata and test outcomes

Record command, runtime, input scope, output path, counts, exit status and hash when appropriate. Do not claim execution, successful tests or generated evidence without real tool output. If execution is unavailable, label those checks unverified.
