---
name: three-quarks-vfx
description: Design particle systems and real-time VFX for Three.js.
---

Use when designing particle systems, trails, emitters, and real-time visual effects using Three.quarks with Three.js.

Workflow:
1. Define visual reference, particle lifetime, emission rate, motion, scale, color, blending, interaction, and target performance.
2. Translate the design into emitters, behaviors, curves, textures, and update lifecycle.
3. Explain deterministic seeds where available, pooling, GPU/CPU cost, disposal, and scene integration.
4. Verify package APIs and feature support against the user's installed version or official project documentation.
5. Provide tuning ranges and QA checks for density, overdraw, transparency sorting, mobile performance, and cleanup.

Do not claim a particle effect exists in the user's scene unless verified through a connected runtime. Keep effects readable and performant.
