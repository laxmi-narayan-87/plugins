---
name: kobra-ui
description: Use when a frontend task specifically references Kobra Systems or a component from kobra.systems.
---

# Kobra Systems UI

Official source: https://kobra.systems

## Retrieval status
The public page was reachable but its content extraction was dominated by an OTP verification interaction and a source preview. The surfaced example is an animated OTP input with React, `input-otp`, `motion/react`, `@tabler/icons-react`, `react-dom` `flushSync`, and a project-local `cn` utility. This is evidence for one example only; it is not a verified complete component catalog or installation specification.

## Workflow
1. Open the exact Kobra component URL the user wants.
2. Inspect the current source, dependency list, CSS and prompt/readme supplied by the site.
3. Confirm the framework, React version, Tailwind version, animation package and any required utility aliases.
4. Install only the documented dependencies. Avoid guessing package names or import paths.
5. Adapt the component to the project's existing design tokens and accessibility patterns. For OTP inputs, verify paste behavior, numeric normalization, focus order, invalid/success states, autofill and screen-reader labeling.
6. Respect reduced-motion preferences and clean up timers/animations. Test keyboard-only and mobile input behavior.

Do not represent this plugin as an official Kobra integration. It is an assistant-side reference workflow. If a source page remains gated or inaccessible, ask the user to provide its component URL or copied source.

