---
name: qa-test-planning
description: Use when converting requirements, tickets, user stories, or vague assignment instructions into a risk-based test strategy, test cases, execution checklist, or professional defect report.
---

# QA Test Planning and Defect Reporting

## 1. Understand the change
Extract the feature, actors, acceptance criteria, business rules, integrations, data states, supported devices/browsers, accessibility needs, security constraints, and release risks. Mark missing details as questions/assumptions; never invent requirements. Build traceability: each acceptance criterion should map to one or more scenarios.

## 2. Prioritize by risk
Score each test candidate from 1-5 for impact and likelihood, and optionally detection difficulty. Risk score = impact × likelihood; use it as a consistent prioritization aid rather than a scientific probability. P0/P1 tests come first: availability, authentication/authorization, data integrity, main workflows, money/permissions, integrations, and recovery. Then cover alternate paths, boundary values, compatibility, usability, and cosmetic polish.

## 3. Design coverage
Use relevant techniques rather than generating huge redundant lists:
- Positive/negative paths and validation
- Equivalence partitions and boundary values
- Decision tables for combinations of business rules
- State-transition coverage for workflows
- Pairwise testing where parameter combinations explode
- Exploratory charters for poorly specified behavior
- Regression selection based on changed code, dependency surface, and severity
- API contracts: schema, status codes, authentication, authorization, pagination, idempotency, rate limits, timeout/retry, and error mapping
- Accessibility: semantics, labels, focus order, keyboard operation, and errors
- Non-functional checks: performance, reliability, privacy, and security, within authorized scope

## 4. Make cases executable
Each case has a unique ID, title, requirement/criterion, priority, preconditions, test data, exact steps, expected result, actual result, status, evidence, and notes. Keep expected results observable and precise. Avoid combined steps that obscure which action failed. State setup/cleanup clearly. For UI cases, identify viewport and browser. For APIs, include sanitized request/response samples and environment variables by name, never secret values.

## 5. Execute with integrity
Track `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`, and `INCONCLUSIVE`. A test passes only after it ran and evidence matched the expected result. A failure needs observed contradictory evidence. If a prerequisite is unavailable, mark blocked/not run and say why. Separate tool limitations and external environment incidents from product defects unless evidence links the issue to the product.

## 6. Write a strong bug report
Template:
- **ID / Title:** concise and searchable, with the symptom and location.
- **Severity / Priority:** justified by user and business impact.
- **Environment:** target URL/build, timestamp/timezone, browser/OS/device, account role, and relevant conditions.
- **Preconditions and test data:** sanitized and reproducible.
- **Steps to reproduce:** numbered, minimal, deterministic.
- **Expected vs actual:** distinct and factual.
- **Evidence:** screenshot, video, trace, network/console log, request ID, or exact error text.
- **Reproducibility:** always/intermittent/once/not yet reproduced; count only actual attempts.
- **Impact/workaround:** who is affected, scope, and safe workaround.
- **Suggested fix:** optional, clearly separated from the confirmed observation.

Avoid duplicate bugs; link related issues. Don't label every observation a bug: distinguish defect, UX improvement, question, and environmental blocker. Do not overstate root cause if it has not been investigated.

## 7. Final QA report
Summarize test scope, coverage by feature and priority, pass/fail/block counts, high-risk defects, trends, exclusions, and release risks. Include a go/no-go recommendation only against explicit exit criteria; explain evidence gaps and residual risk. Include a prioritized action list and a short retest plan. Never manufacture counts, timings, or test execution.

## Quick prompt pattern
“Given [URL/build or requirement], [test scope], [authorized environment/data], create P0–P3 tests in execution order. For every case provide ID, preconditions, steps, expected result, and status. Mark not-run items honestly, record blockers separately, then write reproducible bug reports only from observed evidence.”
