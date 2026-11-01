---
name: spec-and-tickets
description: Use to turn an engineering request or discussion into a concise implementation spec and dependency-aware, independently verifiable tickets.
---

# Specs and implementation tickets

## Synthesize a spec

Use available conversation context and codebase evidence. Do not re-ask questions already answered. Separate confirmed requirements from assumptions.

Structure the spec as:

1. **Problem:** user-visible problem and why it matters.
2. **Outcome:** what will be possible when the work is complete.
3. **User stories:** user/actor, desired capability, benefit.
4. **Behavior and acceptance criteria:** externally observable success and failure behavior.
5. **Implementation decisions:** affected conceptual modules, interfaces, data contracts, architecture, migration and compatibility choices. Avoid fragile file paths unless essential.
6. **Testing decisions:** behaviors to test, test seams, important edge cases, and existing patterns to reuse.
7. **Out of scope:** explicit boundaries.
8. **Open questions and risks:** only unresolved decisions that materially affect delivery.

Prefer one clear spec over a large process document. Do not invent decisions or claim user approval where none was given.

## Decompose into tickets

Create narrow vertical slices, not layer-by-layer task lists. Each ticket should deliver an end-to-end behavior that can be demonstrated or verified independently and fits in one focused implementation session.

For each ticket include:

- Title.
- User-visible behavior delivered.
- Acceptance criteria that can be objectively checked.
- Blocked by: explicit ticket identifiers, or none.
- Verification approach.

Create dependencies only when a ticket genuinely cannot start before another. Prefer a small set of independent tickets when possible. For broad mechanical refactors, use expand-migrate-contract sequencing so the system remains usable during migration.

## Review the plan

Before publishing or creating tracker issues, show the proposed tickets and dependency graph for approval when the action is consequential or externally visible. Do not modify parent issues or close work unless explicitly requested. When publishing, create blockers before dependent tickets so their identifiers can be referenced accurately.
