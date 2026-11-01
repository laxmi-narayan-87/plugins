---
name: rareui-components
description: Use when the user wants to discover, install, adapt or implement components from Rare UI.
---

# Rare UI Components

Rare UI is a free, open-source collection of animated React components. The catalog includes display, AI kit, navigation, inputs and feedback. Representative components include Folder, Code Block, Gravity Letters, GitHub Activity, Step Player, Animated Counter, Fluid Orb, Grid Reveal, Matrix Orb, Bounce Sidebar, Proximity Sidebar, Scroll Progress, Gooey Nav, Duration Picker, OTP Input, Password Input, Toast and Notification Bell.

## Setup and installation
The official MCP page says the project should already have shadcn configured: `components.json`, Tailwind and a `cn` helper. Add this registry to `components.json`:

```json
{ "registries": { "@rare-ui": "https://raw.githubusercontent.com/swamimalode07/rare-ui/main/public/r/{name}.json" } }
```

Install a component, for example:

```bash
npx shadcn@latest add swamimalode07/rare-ui/fluid-orb
```

The official page documents MCP initialization with `npx shadcn@latest mcp init --client claude`; use the client value appropriate to the user's editor and follow current upstream instructions. Request components by registry-qualified name, e.g. `@rare-ui/fluid-orb`, to avoid default-registry ambiguity.

## Implementation rules
Inspect the exact component page and generated files. Check peer dependencies, motion preferences, browser support, Tailwind configuration and accessibility before integration. Preserve attribution/license notices and treat installed code as project-owned only to the extent allowed by its license.

Official references: https://www.rareui.com/components ; https://www.rareui.com/mcp
