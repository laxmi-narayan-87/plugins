---
name: model-deployment
description: "Use when packaging models, building batch or online inference, exposing prediction APIs, designing rollout/rollback, or checking production ML reliability."
---

# ML Model Deployment Workflow

## 1. Capture deployment requirements
Clarify inference mode (batch, online, streaming, edge), payload/schema, traffic and concurrency, latency SLO (p50/p95/p99), throughput, availability, memory/GPU constraints, privacy/security obligations, rollout constraints, and cost. State assumptions instead of inventing requirements.

## 2. Create a portable artifact
- Package preprocessing and the estimator/model together; record model version, code commit, data lineage/reference, dependency versions, training config, evaluation report, and supported schema.
- Pin dependencies to reproducible ranges/lockfile as appropriate; avoid serializing untrusted objects and treat model artifacts as executable/sensitive inputs.
- Add model load smoke tests, schema tests, representative golden examples, and tests for empty, malformed, missing, unknown, oversized, and out-of-range inputs.
- Make preprocessing identical between training and inference. Fail clearly on incompatible schema instead of silently guessing.

## 3. Choose a serving pattern
- Batch: checkpointed jobs, idempotent output writes, partitioning, retries, freshness checks, backfills, and metrics for processed/failed rows.
- Online REST (e.g. FastAPI): request/response schema validation, bounded payloads, timeouts, concurrency limits, readiness/liveness checks, structured error responses, and appropriate worker sizing.
- Streaming: schema evolution, ordering/deduplication expectations, backpressure, checkpoint/replay semantics, and dead-letter handling.
- Edge: target hardware, artifact size, offline behavior, update and rollback mechanism.
Use a managed inference service or model server only when its benefits justify dependency and operational overhead.

## 4. Secure and observe
- Keep credentials outside source/config artifacts; use least-privilege service identities, authenticated endpoints, TLS, rate limits, and avoid logging raw sensitive payloads.
- Track request volume, error rate, latency percentiles, resource use, model version, input validation failures, drift indicators, and delayed ground-truth quality.
- Define alert thresholds, dashboard owner, on-call/runbook, capacity limits, and fallback behavior. Never invent observed production telemetry.

## 5. Roll out safely
- Validate in a staging environment with representative requests and load tests.
- Prefer shadow or canary rollout for risky changes; compare candidate and current model on aligned samples, monitor slice quality and technical SLOs, and define explicit promotion gates.
- Preserve the previous known-good artifact and configuration. Roll back when predeclared thresholds trigger; verify rollback rather than only documenting it.
- Obtain explicit approval before making production changes or migrating traffic.

## 6. Post-deployment lifecycle
- Separate drift alerts from actual model-quality degradation; wait for valid labels when quality measurement is delayed.
- Define retraining triggers, validation gates, registry promotion, compatibility policy, deprecation, and artifact retention.
- Test API compatibility and model loading during dependency or runtime upgrades.

## Deliverable
Return a proposed architecture, artifact layout, serving contract, example implementation/config if requested, security checklist, CI test matrix, monitoring/SLO table, rollout plan, rollback steps, and assumptions. Mark sample code and example metrics as illustrative until run in the target environment.

---
## Source notes

Community skill research informed these independently written workflows. Relevant source references:
- https://github.com/aiskillstore/marketplace/blob/a3598850506f8f6b146cb18b0a8635d51d3f08c0/skills/89jobrien/machine-learning/SKILL.md (Joseph OBrien, Machine Learning; accessed 2026-10-25)
- https://github.com/aiskillstore/marketplace/blob/a3598850506f8f6b146cb18b0a8635d51d3f08c0/skills/wshobson/ml-pipeline-workflow/SKILL.md (ML Pipeline Workflow; accessed 2026-10-25)
- https://github.com/xfstudio/skills/blob/1bf6044db21c12c62695a6732f1273d66ff4882e/machine-learning-ops-ml-pipeline/SKILL.md (MLOps orchestration; accessed 2026-10-25)

This package is an original synthesis, not a verbatim copy of those upstream SKILL.md files. Check each upstream repository's license and notices before redistributing upstream files.
