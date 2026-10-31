---
name: repository-audit-repair
description: Inspect a repository for structural, documentation, asset, dependency, configuration, or implementation defects; repair all confirmed in-scope issues and validate the result. Use when asked to audit, debug, fix, or sign off a code repository.
---

# Repository Audit & Repair

## Workflow
1. Establish repository and branch, inspect the full relevant tree, README, configuration, manifests, recent changes, and existing tests before touching files.
2. Convert the request into audit dimensions: structure, missing/duplicate files, broken links/assets, imports, dependencies, configuration, code behavior, security/safety, and tests as applicable.
3. Gather evidence for each finding. Label findings **confirmed**, **likely**, or **not reproducible**; don't turn guesses into defects.
4. Rank by impact and scope. Identify unrelated files and assets that must remain untouched.
5. Propose the smallest complete fix set. Resolve all confirmed in-scope findings, not just the first one. Avoid broad refactors.
6. Implement fixes. If a change is destructive, externally visible, or irreversible, stop and request explicit approval.
7. Run relevant automated tests, lint/type checks, build, link/path checks, and manual verification where appropriate. Do not claim tests you couldn't run.
8. Inspect the final diff and compare it to the initial scope. Verify no accidental asset deletion, unrelated edits, or generated clutter.
9. Report findings, fixes, commands, pass/fail/skipped results, and remaining risks.

## Rules
- Never infer test success from code inspection.
- Preserve existing assets and conventions.
- Use current project files as source of truth; verify dependency/version claims.
- Explain blockers plainly; don't silently skip them.
- Prefer a regression test for every behavior fix.

## Examples

**Good:** “Tree audit found 4 missing README files and 2 invalid local asset paths. Add only those docs and correct the confirmed paths; run path validation and relevant tests; review diff.”

**Good:** “Reproduce the deployment build error, inspect environment assumptions, patch the root cause, and rerun the same build plus a regression check.”

**Bad:** “The app looks fine, so audit passed.” Why bad: no systematic checks, reproducible evidence, or test results.

## Completion checklist
- [ ] Initial tree/config/tests inspected
- [ ] Findings grounded in evidence
- [ ] All in-scope confirmed issues addressed
- [ ] Regression coverage added where appropriate
- [ ] Relevant tests/build/lint executed
- [ ] Final diff checked for scope and asset preservation
- [ ] Results and limitations accurately reported
