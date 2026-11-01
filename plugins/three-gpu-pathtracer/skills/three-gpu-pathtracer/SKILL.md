---
name: three-gpu-pathtracer
description: Plan physically based path-traced scenes for Three.js.
---

Use when creating or debugging physically based path-traced rendering in Three.js using the relevant GPU path-tracing library.

Workflow:
1. Clarify Three.js and pathtracer package versions, target GPU/browser, scene assets, materials, desired quality, and interactive needs.
2. Assess scene compatibility: geometry, instancing, lights/environment, material support, texture formats, and shader constraints.
3. Explain sampling, accumulation, denoising options if supported, tone mapping, exposure, and quality/performance trade-offs.
4. Check exact package APIs and constraints against the upstream docs and user's installed version before generating code.
5. Provide a validation plan for visual convergence, noise, GPU memory, responsiveness, and fallback rendering.

Do not promise identical output across GPUs or browsers. Do not claim a path-traced render has been generated without execution evidence.
