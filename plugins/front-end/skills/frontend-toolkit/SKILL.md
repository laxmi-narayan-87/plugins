---
name: frontend-toolkit
description: Use when building or improving frontend interfaces and choosing among the five integrated UI component sources. Routes tasks to the most suitable library and provides implementation and QA guidance.
---

# Front-End Toolkit

Use this skill for React/Next.js interface work, component discovery, visual implementation, responsive behavior, motion, accessibility and frontend QA. This is a skills-based router and reference guide; it does not install, mirror, or automatically connect the upstream libraries.

## Source routing
- **Rare UI** (`https://www.rareui.com`): distinctive animated React components; use for unusual interactions, AI-oriented UI, navigation, inputs and feedback. Official setup: shadcn must already be configured (`components.json`, Tailwind and `cn` helper); add registry `@rare-ui` pointing to `https://raw.githubusercontent.com/swamimalode07/rare-ui/main/public/r/{name}.json`. Example: `npx shadcn@latest add swamimalode07/rare-ui/fluid-orb`; MCP workflow uses `npx shadcn@latest mcp init --client claude` as documented by Rare UI.
- **Kobra Systems** (`https://kobra.systems`): treat as an interactive component/source reference. The public page extraction was gated and surfaced an animated OTP input example using React, `input-otp`, `motion/react`, Tabler icons and a local `cn` utility. Do not infer a complete catalog or installation contract; inspect the exact component page and its source before implementation.
- **EasyUI** (`https://easyui.site`): modern React components. Observed examples include interactive area chart, lock input, origin dropdown, slide pagination, spring accordion, liquid toggle, gooey menu, pill navigation and neon edge button. Use for polished controls, navigation, charts and motion-rich interface elements.
- **Pin UI** (`https://www.pinui.xyz`): single-file components derived from visual inspiration, with live previews and copyable source. Categories observed: inputs & controls, cards & widgets, audio & media, lists & pickers. Examples include search card, selection list, desk computer, liquid voice, file box, task card, magnify, calendar card, prompt composer and OTP input.
- **Aceternity UI** (`https://ui.aceternity.com`): React, Tailwind CSS and Motion components, blocks and Next.js templates. Use for landing pages, hero sections, feature grids, backgrounds, shaders, 3D effects, testimonials, pricing and animated text. Verify whether a requested block/template is free or requires All-Access; do not assume paid content is available.

## Workflow
1. Ask or infer framework, version, styling system, current project conventions and target screen. If unknown, state assumptions.
2. Match the component to the right source; compare at least two sources when the choice is not obvious.
3. Open the exact official component page and confirm current installation command, dependencies, source code, license/usage terms and any paid gate. Never invent an API or copy a component from memory.
4. Prefer the smallest compatible implementation. Preserve the project's existing stack; do not add a new animation library if the project already has an equivalent.
5. Integrate keyboard support, semantic HTML, accessible names, focus states, reduced-motion behavior, responsive layout, loading/empty/error states and touch behavior.
6. Run typecheck, lint, unit tests and relevant browser tests where available. Check desktop and mobile breakpoints and report unverified behavior.

## Selection guidance
- Unusual animated micro-interaction: Rare UI or EasyUI.
- OTP, input, selection and utility widgets: compare Rare UI, Kobra, EasyUI and Pin UI.
- Audio/media and compact bespoke widgets: Pin UI.
- Landing-page composition, hero/feature/pricing blocks and visual effects: Aceternity UI.
- Data visualization: EasyUI chart examples, then validate data semantics and accessibility independently.

## Guardrails
These are independent third-party projects, not one shared codebase. Their licenses, dependencies, API conventions, pricing and update cadence differ. Attribute the chosen source in handoff notes, retain upstream notices, and do not rehost or reproduce proprietary/paid source. If a site's current docs cannot be reached, say so and ask for a link or source snippet rather than guessing.

## Official sources
- Rare UI: https://www.rareui.com/components and https://www.rareui.com/mcp
- Kobra Systems: https://kobra.systems
- EasyUI: https://easyui.site
- Pin UI: https://www.pinui.xyz/components
- Aceternity UI: https://ui.aceternity.com/components, https://ui.aceternity.com/blocks, https://ui.aceternity.com/templates


## Inspiration and prompt sources

Use these sites as a visual research layer before designing or implementing a page. Extract patterns and translate them into original work; do not copy a full design verbatim. Check current access, attribution and usage terms.

- **MotionSites** (`https://motionsites.ai`): motion/animation inspiration and prompt library for backgrounds and motion sections. Treat the user's counts (800+ prompts, 1,000+ backgrounds) as claims to verify on the live site; do not promise the full catalog is accessible. Use its prompts as a starting point for Claude or other coding assistants, then adapt to the actual stack.
- **Land-book** (`https://land-book.com`): curated landing-page inspiration. Search by industry, style, layout or color; study hero hierarchy, CTA placement, section sequencing and responsive structure.
- **Recent Design** (`https://recent.design`): contemporary web-design gallery for visual direction, layout patterns and fresh interface trends.
- **Landdding** (`https://landdding.com`): landing-page showcase for polished page composition, conversion patterns and section ideas. Verify the site's current availability before relying on it.
- **Font in Logo** (`https://fontinlogo.com`): typography research for brand/logo lettering. Use it to identify type styles and font alternatives; verify licensing before use in production.
- **Godly** (`https://godly.website`): curated standout/award-worthy websites and interactive experiences. Study art direction, storytelling and interaction details; avoid reproducing proprietary assets.
- **60fps** (`https://60fps.design`): motion and interaction inspiration. Inspect animation timing, transitions, scroll behavior and micro-interactions; implement accessible reduced-motion alternatives.

## Inspiration-to-implementation workflow
1. Clarify the page goal, audience, content, CTA and framework.
2. Browse 2–4 relevant references across the galleries; record specific patterns rather than vague adjectives.
3. Use MotionSites/60fps for motion and Godly/Recent Design for interaction/art direction; Land-book/Landdding for page structure; Font in Logo for typography.
4. Create an original moodboard and section outline; do not copy one site's complete layout or protected assets.
5. Implement with the existing Front-End source routing (Rare UI, Kobra, EasyUI, Pin UI, Aceternity UI), and test responsiveness, accessibility, performance and reduced motion.

## New reference directory
- MotionSites: https://motionsites.ai
- Land-book: https://land-book.com
- Recent Design: https://recent.design
- Landdding: https://landdding.com
- Font in Logo: https://fontinlogo.com
- Godly: https://godly.website
- 60fps: https://60fps.design
