---
name: superpowers-workflow
description: Use when implementing software features, fixing bugs, planning coding work, reviewing code, or verifying a software change; especially useful for non-trivial tasks where an evidence-driven workflow reduces risk.
---

# Superpowers Workflow

Apply a systematic, evidence-driven engineering method rather than improvising. These instructions are a ChatGPT/plugin-format adaptation inspired by [obra/superpowers](https://github.com/obra/superpowers). They are not a claim that the upstream repository's hooks, scripts, subagent orchestration, or external auto-updating skill library are running here.

## 1. Understand the task and the existing system

- Read the user's request and any supplied specification, repository instructions, relevant files, tests, and recent changes before deciding how to implement.
- Establish the desired behavior, constraints, out-of-scope work, and what evidence will count as success.
- If the request already specifies these clearly, proceed without needless questions. If a missing decision materially changes the result, ask one focused question. When the user has explicitly asked you to make reasonable decisions and continue, state the assumptions and proceed.
- For substantial design work, compare a few viable approaches, explain the trade-offs, and recommend the simplest approach that satisfies the requirements. Do not fabricate user approval.
- Prefer the smallest complete change. Avoid unrelated refactors, speculative abstractions, or scope creep.

## 2. Plan work that has multiple steps

- Break substantial work into small, ordered, checkable tasks.
- Identify files/components likely to change and the verification command or observable behavior for each change.
- Keep the plan proportional: straightforward edits do not need elaborate plans.
- If parallel workers or subagents are actually available and useful, divide work into independent pieces with clear boundaries. Otherwise, do not imply that delegated work occurred.

## 3. Test-driven development

For behavior changes and bug fixes, use RED → GREEN → REFACTOR:

1. **RED:** Add a small test expressing the intended behavior before implementing it.
2. Run the test and observe that it fails for the expected behavioral reason. If it fails because of setup, syntax, or test defects, fix that first.
3. **GREEN:** Implement the smallest change that makes the test pass.
4. Run the targeted test and then the relevant broader test suite.
5. **REFACTOR:** Improve naming and structure without changing behavior, keeping tests green.

Do not claim to have observed a failing test unless it was actually run and its output supports that claim. For throwaway prototypes, generated files, or configuration-only changes, use judgment; explain material exceptions where relevant. Do not change a test merely to make a faulty implementation pass.

## 4. Systematic debugging

When behavior is broken:

1. Reproduce the failure and capture the exact error/output.
2. Trace the flow from the observable failure to the responsible component; inspect logs, state, inputs, boundaries, environment, and recent changes.
3. Write down a falsifiable root-cause hypothesis and perform the smallest experiment that can confirm or reject it.
4. Fix the underlying cause, not just the symptom. Add a regression test that would have caught the issue.
5. Re-run the regression test and the wider relevant checks.

Avoid shotgun fixes, unrelated changes, repeated speculative edits, and claiming a root cause without evidence. If evidence is insufficient, report what is known and what remains uncertain.

## 5. Work with code reviews

When reviewing code, prioritize findings by severity and impact. Look for correctness defects, regressions, security/privacy problems, data loss, compatibility, performance risks, missing tests, and misleading documentation. Tie each finding to a specific file/location and explain the triggering conditions and consequence. Distinguish definite bugs from risks or style preferences. Do not praise or criticize vaguely in place of actionable findings.

When receiving review feedback, understand the concrete concern and validate it against the code and evidence. Do not reflexively agree or disagree. Reproduce or test the concern when feasible; fix valid issues and clearly explain any rejected suggestion with reasons.

## 6. Keep Git changes safe

- Inspect repository status and local instructions before making changes.
- Do not discard user changes or overwrite unrelated work.
- Use a separate branch/worktree when the user or repository workflow requires it and the available tools support it.
- Review the diff for accidental files, secrets, generated artifacts, and unrelated edits before committing.
- Commit or push only when requested or clearly authorized. Never claim that a change was committed, pushed, or deployed without successful evidence.

## 7. Verify before completion

Before saying the task is done:

- Run the most relevant test, lint, type-check, build, or validation commands available.
- Check edge cases and the complete relevant suite, not only the newly added test, when practical.
- Inspect the final diff and confirm it addresses the request without collateral changes.
- If any check cannot run, state exactly which one and why. Separate verified results from assumptions and unverified outcomes.
- Report what changed, which validations ran and their outcomes, and any important limitation. Evidence over confidence; never invent command output or completion.

## 8. Practical decision guide

- **New feature or behavior change:** clarify acceptance criteria → plan → failing test → minimal implementation → full relevant verification.
- **Bug:** reproduce → trace → test hypothesis → regression test → fix root cause → re-verify.
- **Code review:** inspect the diff and surrounding code → rank actionable findings → verify uncertain claims.
- **Large change:** work in small independently verifiable stages and keep the user informed at meaningful checkpoints.
- **Simple edit:** make the requested minimal change and run proportionate validation.

## Limitations of this adaptation

This package provides workflow guidance only. It does not itself execute shell commands, inspect a repository without connected tools, install runtime hooks, automatically load other skills, create subagents, or sync upstream updates. Use only tools actually available in the current environment. Refer to upstream for its canonical releases and harness-specific installation instructions: https://github.com/obra/superpowers.
