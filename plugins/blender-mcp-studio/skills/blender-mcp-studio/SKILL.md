---
name: blender-mcp-studio
description: Plan and orchestrate Blender scene workflows through an available MCP connection.
---

Use when planning 3D scene creation, modeling, materials, lighting, camera work, animation, or render workflows in Blender, especially when a Blender MCP server is connected.

Workflow:
1. Clarify the scene goal, Blender version, render engine, output format, scale, assets, and whether the Blender MCP connection is available.
2. Break the work into reversible scene operations: collections, objects, transforms, materials, lights, cameras, animation, and render settings.
3. Before any destructive or expensive action, summarize the proposed change and seek explicit approval.
4. Use only tools actually exposed by the connected Blender MCP server. Inspect scene state before editing; do not invent tool names or claim actions that were not returned as successful.
5. Validate geometry, normals, material nodes, camera framing, lighting, render settings, and save/export destination.

If no Blender connection is present, provide a script or step-by-step plan rather than pretending to control Blender. Never overwrite source files without approval.
