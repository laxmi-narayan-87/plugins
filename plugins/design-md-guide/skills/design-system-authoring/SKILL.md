---
name: design-system-authoring
description: Use when creating, structuring, or improving a DESIGN.md file that communicates a product's visual identity to coding agents through design tokens and design rationale.
---

# DESIGN.md authoring workflow

Use the `google-labs-code/design.md` project as the format reference: https://github.com/google-labs-code/design.md. Treat the repository as the source of truth for current behavior; the format is documented as alpha and may change.

## Core model

A DESIGN.md has two complementary layers:

1. **Machine-readable context:** YAML design tokens, either in a top-level front-matter block or as YAML fences interleaved within sections.
2. **Human-readable intent:** Markdown prose explaining the design's character, audience, rationale, constraints, and how the tokens should be applied.

The prose is not decorative filler. It communicates why the visual choices belong together and which uses are appropriate. Tokens provide exact context but do not replace narrative direction.

## Start by eliciting intent

Collect or infer from supplied materials:
- Product and audience, plus the context where the interface is used.
- A specific visual reference or recognizable design tradition, not just adjectives such as “modern,” “clean,” or “premium.”
- Desired emotional tone and information hierarchy.
- The role of color, typography, layout, shape, depth, motion, iconography, and interaction.
- Explicit boundaries: what must not appear, and what should remain visually restrained.
- Accessibility and responsive requirements.

If key inputs are missing, make transparent provisional assumptions and mark them for confirmation rather than inventing brand facts.

## Suggested document structure

A top-level YAML front matter block may define `name`, optional `version` and `description`, and tokens such as `colors`, `typography`, `rounded`, `spacing`, and `components`. Then write `##` sections in the canonical order when present:

1. Overview (alias: Brand & Style)
2. Colors
3. Typography
4. Layout (alias: Layout & Spacing)
5. Elevation & Depth (alias: Elevation)
6. Shapes
7. Components
8. Do's and Don'ts

A section may be omitted intentionally. Existing/custom headings should not be rejected solely for being unknown; the documented consumer behavior preserves them. Avoid duplicate section headings and duplicate top-level YAML keys.

## Token guidance

- Colors may use valid CSS color syntax.
- Dimensions use numbers with units such as `px`, `em`, or `rem`; spacing may also use numbers.
- Token references use the form `{colors.primary}`.
- Typography may include `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`, `fontFeature`, and `fontVariation`.
- Components map component names to supported properties such as `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, and `width`.
- Express hover, active, and pressed states as separate, related component entries.
- Keep custom token categories when useful (for example, motion or iconography); do not force everything into the standardized categories.
- Do not introduce token values without reason. Explain a token's purpose and usage in prose when its role is not self-evident.

## Write the rationale

For each key section, explain what choices mean and where they apply. Use concrete references and constraints. For example, state that an accent is reserved for interactive elements or diagram annotations if that is the design intent. Include specific do/don't rules to preserve distinctive qualities and prevent a generic result. Avoid a long list of negative rules when a precise visual reference already communicates them.

## Verification

Do not claim a document has been linted or exported unless the command was actually run. Recommend these commands when the user's environment has Node/npm access:

- Validate structure and tokens: `npx @google/design.md lint DESIGN.md`
- On Windows/PowerShell, avoid the `.md` executable-name collision by using: `npx -p @google/design.md designmd lint DESIGN.md`
- Compare versions: `npx @google/design.md diff DESIGN.md DESIGN-v2.md`
- Export to Tailwind v3 JSON: `npx @google/design.md export --format json-tailwind DESIGN.md`
- Export to Tailwind v4 CSS theme: `npx @google/design.md export --format css-tailwind DESIGN.md`
- Export to W3C DTCG JSON: `npx @google/design.md export --format dtcg DESIGN.md`
- Print the current specification: `npx @google/design.md spec`

The linter's documented checks include broken token references, missing primary color, low-contrast component pairs, orphaned color tokens, missing typography, section ordering, likely schema typos, ignored token-like keys, and `omitted` configuration rules. A warning is a prompt to inspect intent, not automatically proof a design is wrong. The CLI uses JSON output by default; interpret actual findings rather than fabricate results.

## Response format

When drafting a file, return a complete Markdown document the user can save as `DESIGN.md`, plus a short summary of provisional assumptions. When reviewing an existing file, separate concrete errors from warnings, optional design recommendations, and subjective aesthetic feedback. Attribute the specification to the repository and note its alpha status when material.
