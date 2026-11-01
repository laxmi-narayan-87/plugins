---
name: engineering-workflow
description: Use for software feature work, refactors, codebase changes, or technical tasks where requirements and implementation need careful alignment.
---

# Engineering workflow

Use this skill as the default operating mode for meaningful engineering work.

## 1. Understand before changing

- Restate the user-visible problem and desired outcome in concrete terms.
- Inspect the repository, current implementation, tests, conventions, and relevant documentation before proposing edits.
- Identify constraints, compatibility requirements, affected modules, data contracts, and likely failure modes.
- Separate facts found in the code from assumptions. Do not invent architecture or claim to have inspected files you have not read.

## 2. Align on the smallest useful change

- For material or ambiguous work, ask focused questions that expose important product and technical decisions.
- Ask one question at a time when the answer changes the solution. Do not interrogate the user about details that can be safely inferred from the codebase.
- Describe the proposed approach and key trade-offs before implementation.
- Prefer the smallest coherent change over broad rewrites or process-heavy frameworks.

## 3. Use the codebase's language

- Read project documentation, glossary, architecture decision records, naming conventions, and nearby code.
- Reuse established domain terms in code, tests, and explanations.
- Where terminology is inconsistent or missing and the concept is central, propose a concise glossary entry rather than introducing competing names.
- Respect existing architecture unless evidence shows it is causing the problem.

## 4. Implement incrementally

- Split work into small steps with observable outcomes.
- Prefer existing module boundaries and the highest practical test seam.
- Avoid unrelated cleanup. Keep diffs narrow and reversible.
- Do not change public contracts, schemas, dependencies, or deployment configuration without a reason grounded in the task.
- Keep the user informed about meaningful decisions, blockers, and verified progress.

## 5. Verify and communicate

- Run focused tests and checks as the change develops, then relevant broader checks at the end.
- Inspect the final diff for unintended changes, missing tests, error handling, security concerns, and maintainability.
- Report what changed, how it was verified, what remains uncertain, and any follow-up needed.
- Never claim a test, build, deployment, or external action succeeded unless its result was observed.
