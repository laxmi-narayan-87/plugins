---
name: a11y-debugging
description: Use when auditing or diagnosing web accessibility, including semantic structure, keyboard navigation, accessible names, focus behavior, ARIA, color contrast, and Lighthouse accessibility findings.
---

# Accessibility debugging

1. Run `lighthouse_audit` with `mode: "navigation"` for a baseline where appropriate. Save reports to a known output directory when needed.
2. Inspect the accessibility tree with `take_snapshot`; evaluate landmark and heading hierarchy, names/roles/states, form labels, and whether interactive controls are exposed meaningfully.
3. Check Chrome issue messages using `list_console_messages` with issue filtering and preserved messages when supported.
4. Test keyboard flow with `press_key` (Tab, Shift+Tab, Enter, Space, Escape) and verify focus visibility, order, focus traps, and expected activation. Use screenshots for visual contrast/layout context.
5. Inspect the exact failing audit elements and report their selectors/snippets before proposing changes. Prefer semantic HTML and native controls; use ARIA only when native semantics are insufficient.
6. Re-run the targeted check after the fix. Distinguish Lighthouse findings from manual keyboard and screen-reader verification; do not claim a complete audit when only one was performed.

Do not treat visual hiding as equivalent to removing an element from the accessibility tree. Avoid arbitrary contrast or touch-target claims unless measured or supported by the audit output. Source guidance: https://web.dev/learn/accessibility/ and https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/a11y-debugging/SKILL.md.
