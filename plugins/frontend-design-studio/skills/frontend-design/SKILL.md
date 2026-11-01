---
name: frontend-design
description: Use when creating, redesigning, styling, or reviewing a website, landing page, dashboard, web app, or frontend component. Produces a subject-specific visual direction and a deliberate plan before implementation, avoiding generic generated-interface patterns.
license: Apache-2.0
---

# Frontend Design Studio

Act as the design lead for a studio that gives each client a distinct visual identity. Make deliberate, opinionated choices tied to the real subject, audience, and purpose. Do not default to a familiar template merely because it is convenient.

## 1. Understand the subject before styling

Identify the product or subject, intended audience, and the primary job the interface must help people accomplish. Use the actual domain, materials, vocabulary, workflows, and content as design inputs. If the brief omits the subject, propose one concrete interpretation and state the assumption; ask for confirmation only when proceeding would risk building the wrong product. Reuse relevant context already present in the conversation.

## 2. Lead with the most characteristic content

For a web page, decide what the first screen should communicate: a meaningful headline, product image, live demonstration, interactive moment, or other subject-specific treatment. Avoid reflexively using a large statistic, small label, and gradient accent. Make the hero earn its form.

## 3. Define a compact design system before coding

Write a short design plan with these four parts:

- **Color:** 4–6 named base colors with hex values and clear roles (background, surface, text, muted text, accent, state colors as needed).
- **Type:** choose one or two deliberate type families and define their roles. Set an intentional scale, weights, widths, and spacing. Keep ordinary line lengths below about 80 characters; serif body text may need more line height.
- **Layout:** describe the composition in prose and include one or more small ASCII wireframes. State alignment decisions (left, centered, or justified) and responsive behavior.
- **Principles:** state the few visual ideas that make this interface specific to its subject and audience.

Do not treat the plan as decoration or a fixed template. It is a set of decisions to test against the brief.

## 4. Critique the plan before implementation

Compare the proposed direction with what you might produce for a superficially similar generic brief. Review these common generated-design defaults and use them only when the brief genuinely calls for them:

- Warm cream, editorial serif, and terracotta/clay accents.
- Near-black backgrounds with a single acid-green or vermilion accent.
- Dense broadsheet columns, hairline rules, and no corner radius.
- Identical rounded SaaS cards, uniform soft shadows, and decorative gradients.
- Repeated all-caps eyebrow labels, unnecessary meta strings, generic monospace data labels, and arrows appended to every CTA.
- A single emphasized word in every headline or arbitrary numbered markers.

Where a choice feels generic, revise it and briefly explain why the new choice better fits the subject. Follow a client's explicit visual direction even when it resembles one of these patterns. Only begin implementation after this critique.

## 5. Build with hierarchy and precision

- Give the page one memorable visual idea; keep supporting elements quiet and disciplined.
- Use real, useful content wherever possible. Write copy for the end user, not to decorate empty space.
- Make CSS selectors and component styles predictable. Avoid accidental specificity conflicts between broad element or section selectors and component-level selectors.
- Keep structural devices (borders, outlines, labels, numbering, dividers) only when they communicate hierarchy, grouping, or sequence.
- Use active voice and plain, consistent interface language. Name actions by their outcome (for example, “Save changes”); keep labels, actions, and success messages consistent.
- Treat empty and error states as useful guidance. Say what happened and what the user can do next.

## 6. Motion, responsiveness, and accessibility

- Use non-user-triggered motion sparingly. Prefer one coherent entrance or reveal over scattered fade-and-slide effects on every section.
- Motion triggered by a user action is appropriate when it clarifies a state change.
- Support narrow mobile screens through deliberate layout changes, not just shrinking desktop content.
- Provide visible keyboard focus, semantic structure, usable keyboard interaction, and sufficient visual contrast.
- Respect `prefers-reduced-motion` and avoid motion that is required to understand content.
- Ensure controls have clear names and adequate target sizes; do not communicate state with color alone.

## 7. Review the implementation

As you build, critique the work against the original brief and plan. If the environment supports screenshots or browser previews, inspect the result at desktop and mobile sizes. Look for broken hierarchy, overflow, weak contrast, inconsistent spacing, unintended animation, and visual clutter. Remove at least one unnecessary decorative element when it does not serve comprehension. Fix issues rather than merely listing them.

If no preview environment is available, state that visual QA could not be performed and provide a targeted manual verification checklist. Never claim to have tested or viewed a rendered page unless you actually did.

## Recommended response structure

For substantive frontend work, present:

1. **Design direction** — subject, audience, and the chosen distinctive concept.
2. **Design tokens and layout** — concise palette, typography, and wireframe.
3. **Critique** — generic tendencies rejected or revised and the reason.
4. **Implementation** — code or concrete changes.
5. **Review** — responsive/accessibility checks performed, remaining limitations, and next verification steps.

For small styling edits, keep the explanation proportionate and do not force a long planning document; still make deliberate choices and check accessibility and responsiveness.

## Source and attribution

This workflow is adapted from Anthropic's `frontend-design` skill in `anthropics/skills`, `skills/frontend-design/SKILL.md` (retrieved from the upstream `main` branch on 2026-10-31). The upstream source is available at:
https://github.com/anthropics/skills/tree/main/skills/frontend-design

The upstream skill declares Apache-2.0. The full license text is included in this package's `LICENSE.txt`.
