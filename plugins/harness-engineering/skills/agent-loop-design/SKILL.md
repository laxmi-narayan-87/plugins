---
name: agent-loop-design
description: Use when building bounded autonomous coding-agent loops, maker-checker workflows, multi-step orchestration, retries, checkpoints, or human-in-the-loop approval flows.
---

# Bounded Agent Loop Design

Design a controlled operating loop with observable state and explicit stopping conditions. Autonomy should be bounded by policy and evidence, not an unending retry prompt.

## 1. Define the state machine

Specify explicit states such as `queued`, `initializing`, `in_progress`, `verification`, `blocked`, `approval_required`, `completed`, and `failed`. Define allowed transitions, who or what can make each transition, persisted fields, and terminal states. Do not let an agent mark a task complete merely by writing a status field.

## 2. Separate planner, worker, and evaluator where useful

- Planner: decomposes the objective into bounded tasks and acceptance checks.
- Worker: performs the task inside the specified worktree, environment, and permissions.
- Evaluator: checks independent evidence against acceptance criteria, ideally with deterministic tests first.
- Human: approves high-impact decisions, scope expansion, sensitive access, releases, or irreversible actions.

Avoid extra agents when the coordination overhead is not justified. Give each role narrow inputs, outputs, and permissions.

## 3. Bound execution

Set explicit limits for iterations, elapsed time, tool calls, concurrency, token or monetary spend where measurable, and external side effects. Specify retryable versus permanent errors; use bounded exponential backoff with jitter when appropriate. Require idempotency keys or state checks for operations that might be repeated. Stop and escalate when limits are reached.

## 4. Persist checkpoints

For each cycle, record task ID, attempt, current state, selected plan, changed files or actions, verification evidence, errors, approvals, and next step. Checkpoint only coherent states; recovery must be able to distinguish a completed side effect from a side effect whose result is unknown.

## 5. Verify and recover

Use the sequence: preflight → execute one bounded change → verify → evaluate acceptance criteria → accept, retry, rollback, or escalate. Prefer deterministic tests and independent checks. Keep failure output and traces sufficient to reproduce failures, while redacting credentials and sensitive data.

Rollback only when the rollback semantics are understood. If a transaction has an uncertain external result, reconcile state before retrying to avoid duplicate effects.

## 6. Human approval boundaries

Pause before deleting important data, publishing, spending money, changing access controls, rotating production credentials, deploying to production, or contacting external parties where authorization is unclear. Present the exact action, target, expected effect, risk, and rollback path for approval.

## 7. Measure the loop

Track task completion rate, acceptance-test pass rate, regressions, retry frequency, human interventions, recovery success, latency, and cost when available. Compare with a prompt-only or existing-workflow baseline. Report the sample size and evaluation conditions; do not claim causal improvement from an uncontrolled comparison.

## Deliverables

Produce a state diagram or transition table, roles and permissions, persisted state schema, retry/timeout policy, approval gates, verification steps, recovery strategy, observability fields, and failure-mode tests.
