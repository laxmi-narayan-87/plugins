---
name: jolt-physics-simulator
description: Model and troubleshoot real-time rigid-body physics workflows.
---

Use when designing or debugging real-time physics simulations using Jolt Physics.

Workflow:
1. Determine language/bindings, Jolt version, simulation scale, timestep, collision requirements, constraints, and target platform.
2. Model bodies, shapes, layers, broad-phase settings, constraints, and update loop at a conceptual level before code.
3. Explain fixed timestep, interpolation, determinism limits, collision filtering, sleeping, and performance implications.
4. Verify API details against the exact binding/version and official Jolt documentation or supplied source.
5. Provide reproducible test cases for tunneling, stacking, contacts, constraint stability, and performance.

Do not claim deterministic behavior unless the specific setup guarantees it. Do not claim to execute a simulation without a connected runtime.
