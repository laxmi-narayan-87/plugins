---
name: claudex-route
description: Use when the user wants to choose an agent/model or decide whether to continue locally, get a second opinion, diagnose a blocker, or delegate one tightly scoped task.
---

# Claudex Route

Recommend an appropriate next step for a software task. This is a decision aid, not an automatic model launcher. Unless execution tools are explicitly connected and available, do not claim to start Claude Code, Codex, or any other model.

## Routing procedure

1. Identify the requested outcome, constraints, risk, ambiguity, and whether code changes are authorized.
2. Consider whether to: stay with the current agent; request an independent plan review; ask for a read-only diagnosis; delegate a bounded implementation; or run the full Claudex Loop workflow.
3. Recommend one option with a concise rationale grounded in task fit, available tools, verification needs, cost/context constraints if the user supplied them, and account/CLI availability.
4. Define a small handoff contract: task, relevant context/files, expected output, allowed actions, prohibited actions, and proof of completion.
5. State explicitly that the recommendation itself does not launch another model or authorize changes.

## Default heuristics

- New feature or risky migration: plan first, then independent review and proof checks.
- Complex plan or architecture: independent adversarial review before implementation.
- Failing test or suspected regression: read-only diagnosis first; request repro, evidence, and a minimal fix hypothesis.
- Narrow, reversible task: keep it with the current agent when that is efficient and verified.
- Sensitive/destructive/high-impact change: tighten permissions and define user approval gates before acting.

Never declare a universally best model. Availability, the configured model, task complexity, context, verification ability, and user priorities all matter.
