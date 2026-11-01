---
name: design-taste-frontend
description: >-
  Use when building, designing, redesigning, restyling, polishing, or reviewing public-facing websites and app screens. Prevent generic AI-looking UI by grounding art direction in the subject, choosing researched visual directions, planning sections from evidence, using credible imagery, and validating responsive layouts in a real browser.
---

# Taste Skill — distinctive frontend design

This skill adapts the workflow described by [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill). The upstream repository's full scripts, design libraries, reference documents, and visual assets should be installed alongside this workflow for the complete experience. This portable edition preserves the core design process and avoids claiming that missing local tools are available.

## Workflow

### 1. Inspect the project and facts

Identify the actual product or organization, audience, primary action, technical stack, existing brand rules, and available imagery. Record 8–12 subject-specific details—its objects, outputs, place, materials, rituals, constraints, data, language, and real artifacts. Never fabricate screenshots, testimonials, metrics, product capabilities, or photographs.

Classify the work:
- **Page**: landing page, marketing site, product page, portfolio, event page, or one-pager. Follow this complete workflow.
- **App screen**: dashboard, admin, analytics, settings, inbox, editor, or data-heavy workspace. Apply quiet borders, consistent alignment, restrained use of colour for data, truthful data, and responsive navigation. Do not use landing-page composition rules blindly on app screens.

If the brief is underspecified but actionable, state your interpretation in one line and proceed. Ask only when a missing detail blocks implementation.

### 2. Write the argument before layout

For each proposed section, write one sentence containing the claim and its proof. Order sections by what the audience needs to believe or do. Delete sections with no evidence or purpose. Do not default to the same hero + three feature cards + logos + testimonials + pricing sequence unless the actual content justifies it.

### 3. Select a direction, not a template

Generate or propose three materially different visual directions, each with a distinct composition, type system, palette proportions, imagery approach, and section structure. Explain which direction best carries the product's specific details. If the original project contains a direction-dealing script or library, use it rather than choosing the category default. Do not blend the selected direction back into a familiar template.

Check the palette against the subject and existing brand. Keep established brand colours and typography where they are required; adjust composition around those constraints. Record any deliberate deviation and why it is necessary.

### 4. Find the product-specific idea

Complete this sentence before implementation:

> On this page, **[a real detail unique to the subject]** becomes **[the visual device used by the selected direction]**.

Use the subject's real output, shape, name, place, ritual, material, data, or artifact as the idea. Run a competitor test: if the sentence remains equally true for a close competitor, it is still too generic.

### 5. Build with substance

- Prefer a strong, deliberate composition and a coherent type hierarchy over ornamental UI.
- Use meaningful content, real product interfaces, or relevant and rights-compatible imagery. Credit external open-archive imagery as required by its license.
- Never fabricate product UI and pass it off as a real screenshot. For software sites without screenshots, build a genuine representative interface as part of the page.
- Make every section earn its place with complete, specific content. Do not remove detail merely to achieve minimalism.
- Avoid reflexive centred three-line hero headlines, generic gradient glows, repetitive icon cards, decorative rules, fake code captions, invented vanity metrics, and cookie-cutter feature grids unless justified by the design concept.
- Make controls useful and semantically correct. Do not present decorative elements as working interactions.
- Respect the existing framework, conventions, accessibility needs, and brand constraints.

### 6. App-screen discipline

For dashboards and operational screens, design for work, not marketing. Prioritize task hierarchy, navigation, scannable data, alignment, readable tables, filters, empty/loading/error states, and mobile behavior. Use plausible sample data only when clearly identified as sample data; calculations and chart totals must be internally consistent. Spend colour primarily on meaningful state and data. Avoid gradients, glows, rainbow charts, invented vanity numbers, and icon-in-tinted-square decoration.

### 7. Verify in a real browser

When the project environment supports it, run the app and inspect screenshots at desktop, tablet, and mobile widths. Check first-screen clarity, container margins, overflow, typography, image crops, section rhythm, navigation, keyboard/focus behavior, contrast, console errors, and broken requests. For app screens, test the real work area, dense tables, and responsive navigation too.

Fix the three most important visual or functional problems, take screenshots again, and repeat for up to three rounds. Do not say browser testing passed unless you actually ran it. When a browser or scripts are unavailable, report that limitation and give the exact manual or automated checks still needed.

### 8. Deliver with an evidence-based report

Summarize the chosen direction, why it fits this subject, key sections, imagery provenance, responsive/accessibility checks actually performed, and remaining limitations. Include screenshots or measurements only when they were actually produced. Never claim use of upstream draw/inspect scripts unless those files were available and executed.

## Local upstream tooling

The full upstream implementation has scripts such as `scripts/draw.mjs`, `scripts/assets.mjs`, `scripts/inspect.mjs`, and `scripts/lint.mjs`, plus design libraries and reference guides. It requires Node.js 22+, a locally installed Chrome/Edge/Chromium, and network access for image discovery. Preserve the upstream repository structure when bundling these files; run the tools from the target project root and follow its current `README.md` and `SKILL.md` for exact commands.
