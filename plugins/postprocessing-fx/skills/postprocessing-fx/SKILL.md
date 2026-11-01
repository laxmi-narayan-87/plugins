---
name: postprocessing-fx
description: Compose performant post-processing effects for Three.js.
---

Use when designing visual effects pipelines for Three.js with the postprocessing ecosystem.

Workflow:
1. Identify renderer, Three.js and postprocessing versions, target device, visual goal, and acceptable frame-time budget.
2. Select only effects that serve the goal; explain ordering and interactions in the composer pipeline.
3. Account for color space, tone mapping, resolution scaling, multisampling, depth/normal requirements, and alpha handling.
4. Verify effect constructors and APIs against the installed version/upstream docs.
5. Provide profiling and visual QA steps, including low-end-device fallback and reduced-motion alternatives where relevant.

Do not claim effects are rendered or benchmarked without runtime evidence. Avoid stacking expensive effects by default.
