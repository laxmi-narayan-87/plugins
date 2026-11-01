---
name: tweakpane-controls
description: Create developer-facing controls for interactive demos.
---

Use when adding Tweakpane panels for live parameter tuning, debugging, and creative coding demos.

Workflow:
1. List parameters, types, defaults, valid ranges, grouping, presets, and which values affect rendering.
2. Design a compact control schema with folders, labels, constraints, and sensible defaults.
3. Provide version-aware integration guidance and ensure pane lifecycle cleanup.
4. Separate debug controls from user-facing product UI; avoid exposing secrets or unsafe controls.
5. Include checks for value validation, state synchronization, keyboard accessibility, and performance.

Check current Tweakpane APIs for the installed version. Do not claim to modify a running app unless a connected environment confirms it.
