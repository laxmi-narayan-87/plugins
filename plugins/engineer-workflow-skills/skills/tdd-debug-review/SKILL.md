---
name: tdd-debug-review
description: Use when implementing behavior, fixing a bug, diagnosing a failure, or reviewing code for correctness and regression risk.
---

# Test, debug, and review

## Test-driven development

Use a red-green-refactor loop whenever practical:

1. **Red:** write or identify a test that demonstrates the desired behavior or reproduces the defect. Run it and confirm that it fails for the intended reason.
2. **Green:** make the smallest production change that satisfies the test. Run the focused test and confirm it passes.
3. **Refactor:** improve structure without changing behavior. Re-run the relevant tests.

Test observable behavior rather than private implementation details. Prefer the highest practical seam, such as a public API, service boundary, command, or user-facing component. Cover boundaries, invalid inputs, failure paths, and regression cases. Avoid brittle snapshots and tests that merely mirror the implementation.

When a failing-test-first approach is impractical, explain why and use the strongest available verification strategy.

## Systematic debugging

1. Reproduce the issue or obtain a precise failure trace.
2. Establish expected versus actual behavior.
3. Narrow the failing boundary using logs, tests, types, and targeted inspection.
4. Form a falsifiable hypothesis and run the smallest experiment that can disprove it.
5. Fix the root cause rather than hiding the symptom.
6. Add a regression test where feasible.
7. Re-run focused checks, then relevant integration or full-suite checks.

Do not make several speculative changes at once. Do not suppress exceptions, loosen assertions, or change tests merely to make the suite green unless the behavior specification itself is wrong and that change is justified.

## Code review checklist

Review the diff, not just the intended design. Check:

- Correctness, edge cases, state transitions, and error handling.
- Data validation, authorization, secrets handling, and injection risks.
- Compatibility of APIs, schemas, persisted data, and callers.
- Concurrency, retries, idempotency, and resource lifecycle where relevant.
- Test quality and whether important behavior is uncovered.
- Performance or accessibility regressions where relevant.
- Unnecessary complexity, duplication, unclear naming, and unrelated changes.

Prioritize findings by severity and explain the concrete impact and reproduction path. Distinguish confirmed defects from risks or suggestions. Do not approve or merge changes that have unresolved critical correctness or security defects.

## Final verification report

State the commands run and their observed outcomes. List skipped checks and why they were skipped. Summarize residual risk. Never imply that unrun checks passed.
