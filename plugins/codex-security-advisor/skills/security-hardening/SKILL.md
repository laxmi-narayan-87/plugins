---
name: security-hardening
description: Use when creating a prioritized application-security hardening plan, reviewing threat-model gaps, drafting security policy guidance, or converting confirmed findings into testable engineering tasks.
---

# Security hardening plan

Build a practical plan based on the actual repository and deployment architecture. Do not claim to generate or install a canonical `SECURITY.md` policy, modify source, or run automated verification unless that action was performed by an available tool.

1. Summarize architecture, exposed entry points, identities, sensitive assets, trust boundaries, and security assumptions from available evidence.
2. Separate confirmed vulnerabilities from defensive improvements and questions needing evidence.
3. Prioritize by plausible impact, likelihood, exposure, exploit prerequisites, and whether a control is currently missing or bypassable. Note dependencies and operational costs.
4. For each task, include: desired security outcome, scoped component, concrete implementation direction, regression test/acceptance criteria, suggested owner role, and dependencies. Avoid arbitrary dates unless the user requests a timeline.
5. Cover relevant areas only: identity and authorization; tenant isolation; request/input validation; secret management and rotation; cryptography; data minimization/retention; audit logging without sensitive values; dependency and build integrity; CI/CD permissions; secure deployment defaults; backups and recovery; monitoring and incident response.
6. Preserve existing vulnerability-reporting instructions and disclosure routes when drafting `SECURITY.md`. Keep threat models and sensitive scan artifacts access-controlled and outside public repositories unless intentionally approved.
7. State assumptions, missing evidence, and what a successful verification would require. Prefer small, reviewable, reversible changes and targeted automated tests.

Output a prioritized backlog with rationale, acceptance criteria, verification steps, and explicit evidence gaps.
