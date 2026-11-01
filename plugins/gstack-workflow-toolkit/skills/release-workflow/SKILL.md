---
name: release-workflow
description: Use when preparing a change for release, checking pull-request readiness, planning deployment and rollback, or verifying production health after a release.
---

# Release readiness and verification

## Intent

Guide a change from a reviewed implementation to a verified release without claiming to perform actions that were not run. This is a process skill: it does not itself push commits, open or merge pull requests, run CI, or deploy without connected tools and authorization.

## Workflow

1. **Confirm the change boundary.** Identify the intended diff, target branch/environment, acceptance criteria, and whether deployment is requested or only a readiness review.
2. **Synchronize and inspect.** When repository tools are available and authorized, inspect branch status, base-branch changes, diff, generated files, secrets, and untracked artifacts before staging or committing. Do not discard or overwrite user changes.
3. **Check implementation completeness.** Verify that the requested behavior, edge cases, error paths, relevant tests, configuration, migrations, observability, and documentation are addressed. Search for nearby affected call sites and compatibility contracts.
4. **Run validation.** Execute the narrow regression suite first, then relevant type checks, lint, full tests, build, and security/dependency checks as appropriate. Record commands and outcomes. If execution is unavailable, report the exact proposed commands as not run.
5. **Review the change independently.** Look for correctness bugs, security issues, incomplete requirements, test gaps, generated artifacts, and needless complexity. Use a second reviewer/model only if available; treat agreement as evidence, not proof.
6. **Prepare the pull request.** Summarize user-visible behavior, implementation choices, test evidence, known limitations, migration/deployment notes, and rollback. Include screenshots only if actually captured. Don't hide failures or inflate coverage claims.
7. **Deploy safely when explicitly in scope.** Check required approvals, CI, migrations, feature flags, backups, and rollback path. Use the smallest safe rollout. Avoid irreversible migrations or destructive data operations without explicit approval.
8. **Verify after release.** Check the actual deployed version, health/status, key user flows, logs/error rates, and relevant performance signals. Compare against the pre-release baseline when available. Roll back or stop rollout if pre-defined guardrails breach; never say production is healthy without post-deploy evidence.
9. **Close the loop.** Produce a factual release summary with commit/PR/deployment identifiers when returned by tools, tests performed, environment, monitoring window, residual risk, and follow-up owner/action if known.

## Final checklist

- [ ] Requirements and acceptance criteria map to implementation and tests
- [ ] No unintended files or secrets are included
- [ ] Relevant regression and neighboring tests ran successfully or are clearly marked not run
- [ ] Build, lint, and type checks are accounted for
- [ ] Documentation and configuration are current
- [ ] Migrations, compatibility, monitoring, and rollback have been considered
- [ ] PR/commit/deploy state is read back from the source system
- [ ] Post-deployment behavior has been checked when deployment occurred

## Reporting states

Use exact states: **verified**, **failed**, **blocked**, **not run**, or **not applicable**. A successful tool call that requests a deployment is not proof the application works; verify observable behavior separately. Never claim a PR was merged or production was updated unless the system confirms it.
