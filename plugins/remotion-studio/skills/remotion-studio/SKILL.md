---
name: remotion-studio
description: Plan and build programmatic videos with Remotion and React.
---

Use when creating programmatic videos, explainers, product demos, social clips, or reusable motion templates with Remotion.

Workflow:
1. Establish output format, duration, aspect ratio, frame rate, target platform, visual references, and whether the user has an existing Remotion project.
2. Convert the brief into a scene-by-scene timeline with durations, transitions, typography, asset requirements, and audio cues.
3. Propose a maintainable React composition structure: root composition, scene components, reusable layers, data props, and shared design tokens.
4. Generate implementation guidance or code only for the project files and APIs actually known. Prefer deterministic frame-based animation and Remotion primitives. Check current API details against official Remotion docs or the user's installed version before asserting an API.
5. Include render commands and validation steps appropriate to the user's environment, plus output checks for dimensions, duration, frame rate, audio sync, and safe margins.

Do not claim to render or export a video unless a connected execution environment has actually done so. Never invent asset paths, project files, or render results. Preserve user assets and ask before overwriting or publishing.
