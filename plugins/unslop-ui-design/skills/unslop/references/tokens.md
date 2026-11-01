# Design tokens and starting values

These values are starting points, not a mandatory house style. Preserve a project's established, effective design system.

## Spacing
Use a 4px rhythm: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128.
- Controls: 4–12px internal gaps.
- Related rows/items: 2–8px.
- Groups/cards: 12–24px.
- Sections: 32–64px; landing sections may use 80–128px.
- Compact/default/touch rows: 32 / 36 / 40–44px.

## App layout
- Sidebar: 240–280px when applicable; content remains fluid.
- Page padding: 24–32px; reasonable max content width 1440–1600px.
- Header: approximately 56–64px.
- Navigation rows: 32–36px, with consistent icon and text columns.
- Keep real app proportions; do not collapse dashboards into narrow centered columns.

## Color
Build one coherent neutral ramp. Apps/dashboards generally keep surfaces neutral; landing pages may take a subtle tint from the product's world. Use:
- Primary, secondary, and muted text roles.
- One restrained accent in chrome, used for primary action/selection/key metric.
- Semantic colors only for semantic states.
- Hairline borders and quiet depth; avoid hue gradients, glows, neon outlines, colored shadows, and decorative color washes.
- Check text contrast; normal text should meet WCAG AA (4.5:1).

Example graphite dark ramp: page `#141415`, card `#19191b`, raised `#232325`, primary `#ededed`, secondary `#a1a1a6`, muted `#85858b`.
Example graphite light ramp: page `#fafafa`, card `#ffffff`, raised `#f4f4f5`, primary `#171717`, secondary `#525252`, muted `#737373`.

## Typography
Use a compact scale and preserve real brand fonts. Example roles:
- Meta: 12px/16px.
- Caption: 13–14px/20px.
- Body/navigation: 14–15px/20–22px.
- Page title: 28–36px.
- Hero: 56–72px desktop, 36–44px mobile.
Use 400/500 as defaults, 600 sparingly. Prefer sentence case and tabular figures for metrics. Keep small text legible; avoid negative tracking below 16px.

## Radius and icons
- Keycaps/tags/small buttons: 4–6px.
- Inputs/buttons: 8–10px.
- Cards: 12–16px.
- Panels: 14–20px.
Use nested radius deliberately; not every element should be a pill. Icons: one set, typically 16–18px, consistent stroke and text-role color, fixed icon box, 8–10px label gap.

## Motion
Use one restrained easing curve. Typical durations: hover/press 120–180ms, menus 160–220ms, entrances 300–500ms. Prefer opacity and transform; avoid animating width/height/top/left. Honor `prefers-reduced-motion`.

---

Part of an adaptation of unslop by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)), CC BY 4.0. Source: https://github.com/heydamir/unslop
