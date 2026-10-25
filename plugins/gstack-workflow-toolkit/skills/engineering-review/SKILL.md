---
name: engineering-review
description: Use to review a software implementation plan, repository diff, API design, data model, or technical proposal for correctness, architecture, maintainability, and test completeness.
---

# Engineering plan and code review

## Principles

Search before building. Prefer reuse in this order: an existing repository helper or pattern; the language standard library; native platform/database capabilities; an already-installed dependency; only then a new dependency. Build the complete solution within the user's scope, including relevant error paths and regression tests, but don't smuggle unrelated migrations into the task. Keep the user in control of consequential direction changes.

## For implementation plans

1. Establish the requested behavior, constraints, non-goals, and acceptance criteria.
2. Trace current architecture and existing patterns from supplied code and files. Clearly identify any repository inspection that was not possible.
3. Describe data/control flow and boundaries. Name affected modules, functions, schemas, APIs, and contracts when evidence is available.
4. Check state ownership, concurrency, retries/idempotency, validation, error handling, access control, observability, migration/backward compatibility, and operational failure modes where relevant.
5. Identify edge cases and failure paths; define tests alongside each behavior, including a regression test for known failures.
6. Note dependencies and justify new ones. Search for existing solutions when web/repository tools are available and useful; separate verified findings from assumptions.
7. Return a sequenced, implementation-ready plan with risks, test strategy, rollout/rollback steps, and explicit decisions the user must make.

## For a code review

Review the actual diff or source, not a summary alone. Follow each important path from inputs to visible effects. Prioritize findings by severity and impact. Each finding should include:

- Severity (critical/high/medium/low)
- Exact file and line or symbol when available
- Concrete triggering condition
- User or operational impact
- Why existing tests or guards do not prevent it
- A specific fix and regression test

Look for: correctness, security/privacy boundaries, data loss, races, null/error handling, authorization, API compatibility, resource leaks, brittle assumptions, and missing tests. Separate functional defects from style preferences. An advisory simplification pass can identify unnecessary abstraction or dependency, but must not block or auto-apply changes by itself.

## Evidence and integrity

Never claim tests, builds, scans, browser checks, deployments, or external reviews were run unless tools actually executed them and returned evidence. A test plan is not a test result; a mock is not a live integration. Do not weaken or delete a test to make a change pass without explicit user authorization and a recorded reason. Report unavailable tools and incomplete coverage.

## Output

Start with the highest-risk findings or the most important plan gaps. Then provide the reasoning, prioritized fixes, regression tests, and residual risks. Be concise but concrete; avoid generic best-practice lists that are not tied to the reviewed code.
