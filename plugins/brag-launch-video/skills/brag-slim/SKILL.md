---
name: brag-slim
description: Create a short launch-video plan or render a project video with local tools, without requiring the full Hyperframes workflow. Use when a user asks for /brag-slim or a lean launch-video production path and a compatible local agent/tooling environment is available.
---
# /brag-slim

Use the upstream project as the source of truth: https://github.com/latent-spaces/brag. This skill is a portable workflow guide; it does not bundle a renderer, audio assets, or executable dependencies.

## Source inspection

Determine whether input is a project directory or website URL. For a project, inspect the actual main page, styles, README, routes, key components, fonts, images, animations, and relevant product-in-use flow. For a website, inspect the fully rendered site; scroll section by section when needed, and note actual copy, colors, fonts, logo, screenshots, videos, and metadata. Reuse genuine UI and styles rather than reconstructing it. Do not infer absent features or metrics.

Before planning, state: one-sentence product summary; intended audience; value; differentiation; strongest substantiated claim; visual hook; real UI to show; tone; share caption.

## Plan and build

Write `brag-plan.md` with a hook, angle, 2–3 highlights, punchline/outro, visual identity, and scene-by-scene storyboard. Target 18–22 seconds (15–25 allowed), with timings summing exactly to target. Support `--tone`, `--format landscape|vertical|square`, `--duration`, and natural-language direction. Work in `brag-output/`, timestamping the directory if it already exists, and keep intermediates in `work/`.

Build using available local tools. If using browser rendering, every frame must be a pure function of time and image/font loads must complete before capture. Review stills from every scene and from transitions; correct overflow, collisions, low contrast, and muddy double-exposures before full render. Audio and SFX should feel like one balanced piece.

## Creative rules

- Make it clear to a stranger what the project does after one viewing.
- The first 2 seconds matter most; plan the hook first.
- Show the real working product, UI, or artifact. Small illustrative UI details are acceptable, but never fabricate claims, numbers, or testimonials.
- Specificity over generic SaaS language; no abstract filler.
- Keep text settled long enough to read (roughly 0.3s per word); motion comes from cuts and animation, not text vanishing early.
- Music/SFX must be licensed/available for the user’s intended use and balanced; do not bundle copyrighted assets without permission.

## Delivery

Deliver `brag.mp4`, `brag.jpg` with the strongest settled frame baked into frame 0 (replace that frame, preserving length/audio sync), and `share-copy.txt` (1–3 specific, postable sentences). Confirm the files actually exist. If rendering tools are missing, stop at plan/instructions and report the blocker honestly. Do not publish or deploy without explicit permission.
