---
name: impeccable-design-workflow
description: Use when a user wants to audit, critique, improve, polish, or creatively redesign a website or frontend UI using an AI coding agent. Especially useful for portfolios, project pages, dashboards, landing pages, and responsive experiences where visual quality must improve without breaking existing functionality.
---

# Impeccable Design Workflow

Use this skill as a practical design-and-implementation process for an existing frontend. It is inspired by the public Impeccable repository's design vocabulary, but it is an independent workflow and does not install or invoke the official `/impeccable` CLI.

## Operating principles

1. **Inspect before changing.** Establish the framework, build/test commands, route structure, styling conventions, design tokens, and current behavior. Review the user's existing instructions and working tree before modifying files.
2. **Product truth before visual direction.** Identify the audience, primary task, content hierarchy, brand personality, and conversion goal. Do not confuse product requirements with aesthetic preferences.
3. **Specificity over generic polish.** Avoid default-looking SaaS patterns, excessive nested cards, gratuitous gradients, repetitive icon tiles, indiscriminate rounded corners, and decorative motion with no purpose. Choose typography, color, spacing, imagery, and layout to match the product.
4. **Preserve behavior.** Keep existing routes, content, links, forms, keyboard access, data flows, analytics hooks, and working button actions unless the user specifically asks to change them. Do not replace real functionality with mock controls.
5. **Small, verifiable changes.** Work in coherent increments. Use existing dependencies and components when sensible. Do not rewrite the application or introduce libraries simply to achieve a styling effect.
6. **Accessible by default.** Maintain semantic HTML, visible focus, keyboard navigation, sufficient contrast, labels and names for controls, reduced-motion support, and non-color-only status cues.
7. **Be evidence-led.** Separate observed defects from hypotheses. If browser access or a running app is unavailable, say so and use source inspection plus available tests rather than claiming visual verification.

## Workflow

### Phase 1 — Reconnaissance

- Confirm repository root and framework, package manager, app entry point, primary routes, component system, and styling method.
- Read project instructions such as `AGENTS.md`, `README`, and relevant package scripts.
- Inspect existing design tokens, fonts, responsive breakpoints, reused components, and interaction handlers.
- Run the existing test, lint, type-check, or build command when practical; record baseline failures rather than attributing them to planned changes.
- If the target or intent is unclear, make a conservative assumption and state it. Ask one concise question only when an essential choice blocks useful work.

### Phase 2 — Critique

Assess the page against these dimensions:

- **Hierarchy:** Can a visitor identify what the page is, its main message, and the primary action immediately?
- **Typography:** Is type purposeful, legible, consistently scaled, and appropriate to the brand? Avoid changing fonts solely for novelty.
- **Layout and rhythm:** Are alignment, whitespace, widths, and vertical spacing consistent? Does the composition have a clear focal point and deliberate asymmetry where useful?
- **Color and contrast:** Are color roles coherent? Is contrast adequate across text, states, borders, and focus indicators?
- **Content and density:** Is copy concrete and scannable? Are repeated cards, labels, stats, badges, or sections adding value?
- **Interaction:** Do buttons and links communicate outcomes? Are navigation, forms, toggles, filters, tabs, modals, and external links functional and understandable?
- **Responsive behavior:** Check narrow mobile, tablet, laptop, and wide desktop widths; look for overflow, cramped navigation, awkward stacking, and excessively long line lengths.
- **Accessibility:** Check semantics, landmarks, heading order, keyboard operation, focus, accessible names, form errors, reduced motion, and non-color cues.
- **Performance and resilience:** Avoid large layout shifts, unnecessary animation, costly effects, oversized assets, and content overflow with long text or missing data.
- **Consistency:** Prefer a small set of shared tokens and components over one-off values, but do not force every section into the same card pattern.

Prioritize findings by impact, confidence, and effort. State a brief rationale and the affected component/route for each. Do not invent audit findings that have not been observed.

### Phase 3 — Select a design direction

Choose one coherent direction that fits the product context. Possible directions include editorial, technical/terminal-inspired, restrained luxury, playful, data-dense, or expressive portfolio. Avoid combining unrelated styles without a reason.

Write a short design brief that defines:

- audience and page goal;
- visual personality and references expressed as qualities, not copied assets;
- typography roles and scale;
- color roles and surface treatments;
- grid, spacing, widths, and responsive rules;
- component and interaction principles;
- motion principles, including reduced-motion behavior.

For a developer portfolio, emphasize proof of work, clear project outcomes, credible technical depth, readable experience, and obvious contact or source-code actions. Be creative through composition, type, project storytelling, small purposeful interaction details, and meaningful visualizations—not decoration alone.

### Phase 4 — Plan and implement

- Convert the brief into an ordered set of tasks with clear acceptance criteria.
- Start with structural issues and shared tokens, then typography/layout, then component styling, then motion and micro-interactions.
- Reuse existing components and design tokens where they help consistency; make shared abstractions only when at least two real use cases justify them.
- Keep actual link destinations and button handlers intact. Every interactive control must perform its stated action or be clearly disabled with a reason.
- Make empty, loading, success, validation, and error states explicit where relevant.
- Add animation only when it communicates hierarchy, state, or spatial relationships; honor `prefers-reduced-motion` and avoid bounce/elastic motion as a default.
- Do not fabricate testimonials, metrics, project results, experience, ratings, or social proof. Keep supplied content factually intact unless asked to edit it.
- Before adding a dependency, check whether the current stack already supports the need.

### Phase 5 — Verify

- Run the project’s available checks (tests, lint, type checking, build) and report the exact results.
- Inspect changed routes and components in the browser when a browser is available. Verify mobile, tablet, and desktop layouts, including menu states and long content.
- Exercise every affected visible control: logo/home navigation, internal/external links, project buttons, filters, form submission and errors, tabs, theme toggles, modals, and keyboard focus as applicable.
- Check console/runtime errors and broken assets if browser tooling is available.
- Compare the implemented result against the acceptance criteria and fix obvious regressions.
- If a visual/browser check could not be run, identify it as unverified. Never claim a build, test, or button audit succeeded unless it actually ran.

## Command vocabulary

Users may request any of these verbs in natural language; treat them as workflow presets, not magic commands unless the host coding tool has matching commands installed.

- **init** — inspect project context and document durable product truth; recommend next steps.
- **shape** — map page purpose, audience, hierarchy, user journeys, wireframe structure, and acceptance criteria before coding.
- **critique** — give a prioritized UX, visual, content, and interaction review grounded in source/browser evidence.
- **audit** — check responsive behavior, accessibility, performance, and technical quality; produce reproducible findings.
- **bolder** — increase memorability and visual distinction while preserving clarity and product fit.
- **quieter** — reduce competing emphasis, effects, and decoration; improve restraint and focus.
- **distill** — remove redundant sections, components, labels, borders, and decoration while preserving useful information.
- **typeset** — improve font roles, type scale, line length, weight, leading, and hierarchy.
- **layout** — correct spacing, alignment, grid, widths, density, and responsive rhythm.
- **colorize** — introduce coherent semantic color roles and states without sacrificing contrast.
- **animate** — add limited purposeful motion with reduced-motion support.
- **delight** — add a small, relevant moment of personality that does not impede usability.
- **clarify** — improve UI copy, labels, action names, instructions, errors, and empty states.
- **adapt** — target specific device sizes, input methods, and responsive conditions.
- **harden** — handle keyboard, errors, loading, overflow, localization, missing data, and edge cases.
- **onboard** — improve first-run guidance, empty states, and next actions.
- **optimize** — improve measured or source-evident performance without sacrificing UX.
- **polish** — perform final consistency and shipping-readiness review.
- **craft** — run the full sequence: inspect, shape, build, iterate, verify.

## Response format

For analysis-only requests, return:

1. Overall diagnosis.
2. Prioritized findings with evidence, impact, and effort.
3. Recommended visual direction.
4. Ordered implementation plan and checks.

For implementation requests, summarize:

1. What changed and why.
2. Files or components affected.
3. Checks that actually ran and their outcomes.
4. Any unresolved or unverified items.

Keep the user informed when a multi-step coding task will take several actions. Do not imply that changes have been made to a repository unless the coding environment actually performed them.
