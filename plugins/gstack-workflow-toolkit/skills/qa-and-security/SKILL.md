---
name: qa-and-security
description: Use to create or execute a bounded QA plan, investigate a reproducible defect, assess common application security risks, or prepare evidence-backed test coverage.
---

# QA, root-cause debugging, and security review

## A. Root-cause investigation

1. State the observed failure, expected behavior, actual behavior, and environment. Preserve the original error and reproduction steps.
2. Reproduce before editing when the environment and tools permit. If reproduction is unavailable, say so and continue with clearly labeled hypotheses.
3. Trace the data/control path across callers, shared helpers, persistence, network boundaries, and user-visible output. Find the earliest point where actual behavior diverges from expected behavior.
4. Form a small set of competing hypotheses. For each, identify the evidence that would confirm or eliminate it; test one change at a time.
5. Fix the root cause rather than adding scattered caller-side guards. Stop after three unsuccessful fixes, reassess assumptions, and report what evidence is missing instead of piling on speculative patches.
6. Add or propose a regression test that fails before the repair and passes afterward. Re-run the relevant suite and adjacent checks when execution tools are available.

## B. QA workflow

1. Define the test target and authorization boundary: page, API, CLI, job, worker, webhook, or feature. Stay within the specified scope and avoid destructive production actions.
2. Convert acceptance criteria into a compact matrix of normal paths, edge cases, invalid inputs, permissions, failure/retry behavior, state changes, accessibility/usability, and cross-browser/device issues where relevant.
3. Explore the target and gather evidence. Record exact steps, environment, expected result, observed result, logs/network details when available, and screenshot or trace references only when actually captured.
4. For each defect, establish a minimal reproduction and severity based on impact and likelihood. Distinguish an observed failure from a potential risk.
5. Before repair, ensure the regression case demonstrates the failure where safe and feasible. After repair, re-run it and related tests.
6. Report pass, fail, blocked, and not-run distinctly. Never infer a pass from a lack of error output or from a test being listed in a plan.

## C. Security assessment

Use a defensive, authorized review. Choose applicable checks based on the actual architecture and supplied evidence:

- Authentication, session handling, authorization and tenant isolation
- Input validation, injection, unsafe deserialization, path traversal and SSRF
- Secret exposure, token handling, logs, telemetry and sensitive data retention
- CORS/CSRF, security headers, TLS and cookie flags where applicable
- Dependency and supply-chain risks, vulnerable or unnecessary packages
- File upload, resource exhaustion, rate limits and abuse controls
- Database permissions, migrations, backups and least privilege
- Browser/UI trust boundaries, prompt injection and untrusted external content when agents or automation are involved

Use established checklists (such as OWASP guidance) when web access is available. Do not claim to have run scanners or a comprehensive OWASP/STRIDE audit unless that work actually happened. Avoid exploit instructions beyond what is necessary to validate a permitted test environment; don't attack third-party or production systems without explicit authorization.

## Output

Provide scope and assumptions, the highest-risk evidence-backed findings first, reproduction or validation steps, severity and impact, recommended fixes, regression tests, and coverage limits. Label security areas as **observed**, **not observed**, or **not assessed** rather than implying completeness.
