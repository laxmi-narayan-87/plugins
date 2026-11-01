---
name: comfyui-workflow-studio
description: Design and troubleshoot node-based generative media workflows.
---

Use when designing, documenting, or troubleshooting ComfyUI workflows for image, video, or other supported generative media.

Workflow:
1. Clarify output type, model/checkpoint availability, ComfyUI version, custom nodes, hardware/VRAM, resolution, and licensing constraints.
2. Draft a node-by-node workflow with explicit inputs, outputs, dependencies, and parameter rationale.
3. Flag custom-node requirements and model downloads; never invent node IDs or assert a node is installed without evidence.
4. For API execution, use only a verified connected ComfyUI endpoint and documented schema. Obtain approval before expensive generation, downloads, or overwriting outputs.
5. Include reproducibility details: seed, model identifiers, sampler, scheduler, dimensions, and workflow export.

This plugin does not itself host ComfyUI or supply model weights. Be transparent about resource requirements and content provenance.
