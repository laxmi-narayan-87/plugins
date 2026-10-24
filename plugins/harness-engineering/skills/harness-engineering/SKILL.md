---
name: harness-engineering
description: Use when designing or improving a harness around an AI coding or research agent, including repository instructions, environment setup, persistent state, scope control, verification, observability, and clean session handoff.
---

# Harness Engineering Workflow

Use this workflow to design the system around an agent, not merely to rewrite its prompt. The harness should constrain where the agent works, what state persists, how work is checked, and what constitutes completion.

## 1. Establish the task contract

Before proposing implementation, capture:
- Goal and user-visible outcome.
- Repository/runtime and supported agent(s).
- Constraints, forbidden side effects, data sensitivity, and approval boundaries.
- Acceptance criteria that can be checked independently.
- Explicit out-of-scope work.
- Expected deliverables and final evidence.

Ask a concise question only when a missing detail blocks safe progress. Otherwise state assumptions and proceed.

## 2. Inspect before changing

Inspect the current repository tree, existing instruction files, package scripts, tests, CI, environment setup, agent skills, local state artifacts, and security boundaries. Preserve working conventions. Distinguish verified facts from assumptions, and do not claim a control exists until its implementation is inspected.

## 3. Design the five subsystems

### Instructions
- Provide a short root entry point that routes to detailed, relevant instructions.
- Put durable repository conventions, commands, architecture boundaries, and definitions of done in version control.
- Use progressive disclosure rather than one enormous instruction file.
- Make instructions actionable and specific; avoid contradictory or untestable guidance.

### State
- Keep a machine-readable feature/task list with stable IDs and statuses.
- Persist current objective, completed work, changed files, known issues, commands/results, and next step.
- Treat source control and explicit state files as the source of truth, not conversational memory alone.
- Record decisions and blockers without rewriting history to make progress look better.

### Verification
- Define test commands and acceptance criteria before implementation.
- Prefer deterministic checks: unit tests, type checks, lint, build, integration tests, smoke tests, and end-to-end validation as appropriate.
- Run the relevant checks after the change, capture exit codes and output, and distinguish passed, failed, skipped, and not run.
- Do not infer correctness from confidence, a successful build alone, or a test that does not cover the claimed behavior.

### Scope and authorization
- Work on one bounded feature or task at a time.
- Track dependencies and prohibit unrelated refactors unless needed and approved.
- Separate read-only inspection, reversible edits, external side effects, destructive operations, and privileged actions.
- Require human approval at irreversible or high-impact boundaries. Use least privilege and isolated worktrees/sandboxes where possible.

### Session lifecycle
- At startup, establish a clean and known environment; install dependencies reproducibly and run baseline checks.
- During work, keep state and verification evidence current.
- At handoff, leave the repository in a clean, resumable state with status, changes, commands run, results, and next action.
- Do not commit or claim completion when the repository is knowingly broken unless explicitly instructed to checkpoint a failing state.

## 4. Choose the minimum useful harness

Start with a minimal set appropriate to the repository, commonly:
- `AGENTS.md` (or the repository's existing equivalent)
- `init.sh` or another documented environment/bootstrap command
- a machine-readable feature/task list
- a session progress/handoff log
- canonical verification commands in CI or a script

Do not add files just to satisfy a template. Add a mechanism when it addresses an observed failure mode.

## 5. Make completion evidence-based

For each acceptance criterion, map it to a test or inspection method and record the result. If something cannot be verified, mark it explicitly and explain what evidence is missing. Final reporting should summarize changes, tests run, outcomes, risks, and remaining work.

## Output format

Deliver: (1) repository observations, (2) design or changes grouped by subsystem, (3) acceptance-to-evidence mapping, (4) verification results, (5) risks and next actions. Avoid claiming that harness improvements guarantee agent correctness; they reduce specific failure modes and must themselves be validated.
