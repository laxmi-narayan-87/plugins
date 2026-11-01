---
name: threejs-studio
description: Design interactive 3D web experiences with Three.js.
---

Use when building interactive 3D scenes, product viewers, visualizations, or WebGL experiences with Three.js.

Workflow:
1. Define target devices, scene complexity, controls, asset formats, interaction model, and performance budget.
2. Propose scene architecture: renderer, scene, camera, lights, asset loaders, controls, animation loop, and cleanup.
3. Give version-aware implementation guidance; verify current Three.js APIs against official docs or the user's package version.
4. Address responsive sizing, device pixel ratio, resource disposal, accessibility alternatives, and graceful fallbacks.
5. Provide performance validation for draw calls, texture memory, geometry complexity, frame time, and mobile thermals.

Do not claim to launch a browser scene or inspect a local app unless a connected runtime is available. Avoid unnecessary dependencies.
