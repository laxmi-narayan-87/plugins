---
name: design-review
description: Use when auditing an existing DESIGN.md, assessing design-system clarity, checking token consistency and accessibility risks, or planning changes between design-system revisions.
---

# DESIGN.md design review

Reference project: https://github.com/google-labs-code/design.md. This workflow offers a structured review; only report CLI findings as verified when the CLI was actually run against the supplied file.

## 1. Review design intent

Check whether the overview names a concrete visual reference, product context, and audience. Flag generic adjectives without supporting specifics. Ensure prose describes the purpose of core colors, typography, layout, shapes, elevation, motion, and components where relevant. Look for meaningful constraints and coherent do/don't guidance. Distinguish an intentionally sparse system from missing documentation.

## 2. Review format structure

Inspect:
- Valid YAML front matter or correctly placed interleaved YAML token blocks.
- A non-empty `name` and sensible token schema.
- Canonical order among recognized section headings, without assuming unknown headings are invalid.
- Duplicate recognized section headings and duplicate top-level YAML keys.
- Consistency between token names in YAML and token mentions in prose.
- Custom categories that extend the design system without conflicting with standardized semantics.

## 3. Review token consistency

Look for broken references such as `{colors.primary}` when no such token exists; keys that appear to be typos of known schema keys; color or dimension values that look malformed; components with undefined tokens; unused color tokens; incomplete typography; and state variants whose intent or naming is unclear. Do not silently rewrite ambiguous brand values.

## 4. Accessibility review

Check stated foreground/background pairs when available. WCAG AA normal-text contrast is generally at least 4.5:1, and large text contrast is generally at least 3:1; assess the applicable text size and weight before judging. Also review semantic hierarchy, focus/hover/active/disabled state coverage, reduced-motion guidance where motion is specified, and whether text alternatives or non-color cues are addressed when relevant. A prose-only review cannot certify contrast; use the project's CLI or a suitable contrast calculator for exact values.

The repository documents a `contrast-ratio` warning for component background/text pairs below 4.5:1. Report that as the tool's stated rule; do not imply its implementation covers every accessibility requirement.

## 5. Change/regression review

For two versions, describe:
- Added, removed, and modified tokens by category.
- Changed rationale or design constraints.
- Potential visual or accessibility regressions.
- Whether increases in linter errors/warnings appear in the after version.

Use `npx @google/design.md diff DESIGN.md DESIGN-v2.md` (or `npx -p @google/design.md designmd diff ...` on Windows if executable naming is problematic) to obtain actual structured comparison results. The documented diff command exits with code 1 when the after-file has more errors or warnings. Never invent CLI output.

## 6. Deliver findings

Prioritize each finding with:
- **Severity:** Error / Warning / Recommendation.
- **Location:** Section, token path, or component name.
- **Evidence:** The precise inconsistency or omission.
- **Impact:** What an implementing agent or user may experience.
- **Suggested correction:** A specific change, ideally minimal and consistent with the stated intent.

Keep objective format errors separate from subjective aesthetic preferences. End with the highest-value next action and the exact validation command relevant to the requested task.
