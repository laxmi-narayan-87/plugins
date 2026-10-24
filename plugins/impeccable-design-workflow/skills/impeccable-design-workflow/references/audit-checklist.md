# Website design audit checklist

Use this checklist to keep reviews concrete. Mark items as **Pass**, **Issue**, or **Not verified**, and reference the route/component or viewport tested.

## Visual quality
- Clear first-screen message and primary action
- Typography roles and hierarchy are consistent
- Content width and line length are comfortable
- Spacing and alignment follow a deliberate rhythm
- Palette and surface treatments serve the content
- Repetition (cards, icons, badges, borders) is purposeful
- Assets load correctly and have appropriate crop/alt text

## Interaction
- Every interactive control has a real outcome
- Link destination and action label match
- Navigation works by mouse and keyboard
- Forms have labels, validation, success, and failure feedback
- Disabled/loading states are explained and perceivable
- Focus is visible; modal/drawer focus behavior is sensible
- No dead buttons, placeholder `#` links, or misleading toggles

## Responsive
- 320–375 px narrow mobile and a typical modern mobile width
- Tablet portrait/landscape where relevant
- Laptop and wide desktop
- No horizontal overflow or clipped content
- Header/menu, project grids, tables, and forms reflow correctly
- Touch targets are comfortably usable
- Images, headings, and long unbroken strings wrap safely

## Accessibility
- Semantic landmarks and logical heading levels
- Keyboard-only navigation and focus order
- Accessible names for icon-only controls
- Contrast checked for text, UI controls, focus, and states
- Errors announced and linked to relevant fields where feasible
- Status not conveyed by color alone
- Motion honors `prefers-reduced-motion`
- Useful image alternatives; decorative images ignored by assistive technology

## Technical resilience
- Build, lint, type-check, and tests as available
- No obvious console exceptions or missing resources in browser checks
- Loading, empty, success, error, and long-content states considered
- No avoidable layout shifts or oversized effects/assets
- Existing routes, analytics hooks, data operations, and outbound links preserved

A checklist item should not be marked Pass unless it was checked; otherwise use Not verified.
