---
name: hallmark-design
description: Use when creating, redesigning, polishing, or auditing a website or app interface and the user wants deliberate visual design rather than generic AI-generated UI. Covers design discovery, theme selection, implementation, preservation checks, accessibility, responsiveness, and browser-based quality review.
---

# Hallmark Design

An implementation-oriented design workflow adapted from [Hallmark](https://github.com/Nutlope/hallmark), originally made by Nutlope / Together AI. The upstream project describes itself as a design skill for Claude Code, Codex, Cursor, and OpenCode. This package preserves the core workflow and decision rules as a portable skill; it does not claim to bundle the upstream theme library or executable scripts.

## Operating principles

- Design for the user's task and the product's actual purpose. A booking page should make booking easy; a shop should make product discovery and purchase easy; a dashboard should make decisions and next actions clear.
- Establish a visual point of view. Avoid generic SaaS layouts, interchangeable card grids, decorative gradients, arbitrary accent words, and repetitive section patterns unless they serve the product.
- Do not fabricate product facts, metrics, customer logos, reviews, testimonials, inventory, pricing, or integrations. Use provided evidence, inspect the existing product, or mark missing content as a deliberate placeholder.
- Preserve existing behavior during redesign. Keep routes, content, links, form fields, labels, handlers, validation, API wiring, and state transitions unless the user explicitly requests a change.
- Prioritize accessibility, legibility, responsive behavior, and working interactions over decorative polish.

## Workflow A — create a new interface

### 1. Pre-flight

Inspect the repository before editing:

- Identify framework, routing, component conventions, styling system, fonts, existing design tokens, assets, and build/test commands.
- Inspect the current page and adjacent components to understand established patterns.
- Read any `design.md`, brand guide, or product brief and treat explicit constraints as binding.
- Determine the target audience, page purpose, primary action, and essential information hierarchy.
- Ask for missing assets or factual content only when they materially affect the design. Never invent them.

Summarize the intended approach before large implementation changes. Reuse the project's stack and conventions rather than introducing unnecessary dependencies.

### 2. Choose a visual direction

Pick a coherent visual material that fits the product, audience, and content. Consider typography, color, surfaces, borders, density, imagery, iconography, motion, and component behavior as one system. Use a theme as visual language, not as a page template.

Possible directions (illustrative, not an upstream theme catalog):

- Editorial: expressive typography, restrained palette, clear reading rhythm.
- Technical/instrument: dense but legible data, precise alignment, functional states.
- Warm craft: tactile surfaces, human-scale typography, authentic imagery.
- Modernist/architectural: strong geometry, whitespace, disciplined type scale.
- Playful/expressive: distinctive shapes and color with strong usability controls.
- Quiet utility: calm surfaces, excellent hierarchy, fast task completion.

Do not choose a direction solely because it is fashionable. Explain briefly why it fits the product.

### 3. Build the first screen first

Implement the header/navigation and hero or primary workspace before expanding the page. The first screen must communicate:

- What the product/page is.
- Who it is for or what task it supports.
- The primary action and what happens when the user takes it.
- Credible proof or context, only when supplied or verifiable.

Render or inspect the first screen before building every lower section. Fix hierarchy, spacing, typography, contrast, composition, and responsive behavior early.

### 4. Build around the job

Create only sections that serve the user's goal. Vary layout according to content. Use real product UI, diagrams, relevant photographs, or meaningful data where appropriate; do not fill space with empty frames or decorative cards. Keep conversion or task completion focused, and end with a relevant next action rather than a boilerplate signup section.

Make every visible control meaningful. Forms must validate and submit to a real implemented action; do not show a success message when nothing was sent or saved. Include loading, empty, error, and success states where applicable.

### 5. Responsive and accessible implementation

Check narrow mobile, intermediate/tablet, laptop, and wide desktop sizes. Ensure:

- No horizontal overflow or clipped critical content.
- Navigation and primary actions remain usable by touch and keyboard.
- Text remains readable and line lengths sensible.
- Layout adapts rather than simply shrinking desktop columns.
- Semantic landmarks and heading order are coherent.
- Every input has a programmatic label; errors are associated with fields.
- Interactive elements are keyboard accessible with visible focus.
- Color contrast is sufficient; color is not the only way to convey state.
- Motion respects `prefers-reduced-motion` and never blocks the task.
- Images have useful alt text when informative and empty alt text when decorative.

## Workflow B — redesign an existing interface

Use only when the user names the existing page or asks for a redesign.

### 1. Baseline and preservation inventory

Before editing, inspect the target and record:

- Page routes and navigation destinations.
- Visible text, headings, and content blocks.
- Links, buttons, forms, inputs, labels, and validation behavior.
- Event handlers, state transitions, API calls, and important data bindings.
- Responsive breakpoints and accessibility semantics.

Capture screenshots or a visual baseline when browser tooling is available. Do not assume a control is decorative because its implementation is not immediately obvious; trace it.

### 2. Redesign scope

Interpret the user's wording carefully:

- **Redesign:** may change layout and visual system while preserving content and wiring.
- **Restyle / keep layout:** keep information architecture and geometry, update visual presentation.
- **Polish:** make targeted craft improvements without broad restructuring.
- **Audit:** report findings and recommendations only; do not edit.

### 3. Implement and verify preservation

Change the smallest coherent set of files. Compare the post-change implementation with the baseline inventory. Confirm every route, link, field, label, handler, validation path, and state transition remains intact unless an explicit change was requested. Report any behavior that could not be verified.

Provide a before/after summary and mention any intentional deviations.

## Workflow C — audit a UI without editing

Inspect the implementation and, where possible, render it in a real browser. Report findings grouped by severity:

1. **Floor (must fix):** accessibility failures, missing focus states, poor contrast, broken mobile layouts, clipped content, nonfunctional controls, invented or misleading facts, and critical usability blockers.
2. **Reflex (strong defaults):** repetitive eyebrow labels, overused all-caps tracking, arbitrary highlighted words, excessive card grids, generic decorative gradients, empty image frames, redundant CTAs, stock-looking hero composition, and boilerplate closing sections. A deliberate reason may justify an exception.
3. **Finish (craft):** small spacing inconsistencies, type-rhythm issues, icon alignment, subtle transitions, and visual details that should not block release.

For each finding include location, evidence, impact, and a concrete recommendation. Distinguish observed defects from subjective suggestions. Never claim a browser check was run when it was not.

## Quality gates before handoff

- [ ] The page's purpose and primary action are obvious.
- [ ] Visual direction is coherent and product-specific.
- [ ] Typography, spacing, color, and surfaces form a deliberate system.
- [ ] No fabricated facts, fake testimonials, or nonfunctional controls.
- [ ] Existing behavior is preserved on redesigns.
- [ ] Mobile, tablet, and desktop layouts have been inspected.
- [ ] Keyboard navigation and visible focus work.
- [ ] Contrast, semantics, labels, and reduced-motion behavior are addressed.
- [ ] Empty, loading, error, and success states are handled where relevant.
- [ ] Tests, type checks, lint, and build commands pass where available.
- [ ] Browser screenshots or manual inspection are reported accurately.

## Tooling guidance

Prefer the repository's existing browser/test setup. The upstream Hallmark v2 README describes `scripts/sloplint.mjs --render` for browser-rendered UI checks, `scripts/theme.mjs` for theme selection, and a fresh-context reviewer. These scripts are available only when the upstream repository is installed; this lightweight package does not include them. If the source repository is present, inspect its actual scripts and use them rather than assuming flags or behavior.

When browser automation is unavailable, perform static inspection and state that runtime verification remains outstanding.

## Handoff format

Summarize:

- The visual direction and why it fits.
- The key structural and interaction decisions.
- Files changed.
- Preservation results for redesigns.
- Checks run and their outcomes.
- Known limitations or unverified behavior.

## Original source and attribution

- Original project: https://github.com/Nutlope/hallmark
- Website: https://www.usehallmark.com
- Project authorship: Hallmark by Nutlope / Together AI (as stated in upstream README).
- Upstream license: MIT. Include the copyright and permission notice when redistributing substantial portions of upstream source. This package is a concise workflow adaptation, not a copy of the full upstream repository or its assets.
- Upstream project README reports inspiration from Impeccable, Anthropic frontend-design, Open Design, Kami, taste-skill, huashu-design, UI UX Pro Max, Emil Kowalski's skills, and Web Interface Guidelines.
