---
name: brag
description: Plan and produce a short, polished, project-specific launch video from a software project or website. Use when a user asks to /brag, make a launch video, show off a project, or create video and share copy for something they built.
---
# /brag — You built it. Now brag.

Use the upstream workflow from https://github.com/latent-spaces/brag as the reference for command syntax and creative principles. This plugin is a reusable guide, not a bundled copy of the upstream repository, its music/SFX assets, Hyperframes, or local rendering binaries. Do not claim that rendering happened unless the required environment was actually used and the output verified.

## Invocation

Parse any project/URL and preferences first. Support these options in the plan: `--tone` (default, polished, yc-parody, chaotic, deadpan, cinematic, app-store, or freeform), `--format` (landscape, vertical, square), `--duration` (normally 15–25 seconds), `--no-music`, `--no-sfx`, `--title`, and `--voice` (off unless expressly requested). Preserve custom creative direction.

## Workflow

1. **Inspect the source.** If a local project is available, read its README, entry pages, styles, routes/components, real UI, assets, and project evidence. For a URL, inspect the rendered site including scrolling/animated sections and real copy, palette, fonts, and metadata. Don't assume files or a working directory. If source access is unavailable, state exactly what can and cannot be inspected and provide a source-specific plan only from known information.
2. **Answer the planning rubric.** What is the product? Who is it for? What does it do? What makes it distinct? What's the strongest grounded claim? Visual hook? Real UI or flow? Tone? Share caption? Commit to a specific angle.
3. **Write `brag-plan.md`.** Include hook, angle, tone, storyboard, timings, text, transition and SFX cues. Scene durations must sum to the target. Typical pattern: hook (2–3s), reveal (2–4s), 2–3 highlights (5–12s), closing (2–4s).
4. **Write `composition-brief.md` and compose.** Use the actual product/code/styles/assets where possible; prefer a working UI flow to fake UI or flat screenshots. Keep generated intermediates in `brag-output/` (use timestamped output if the directory already exists) and do not modify the application source merely to produce the video.
5. **Validate before rendering.** Follow the current upstream `skills/brag/SKILL.md` and Hyperframes domain references when available. For full workflow, confirm Node.js 22+, FFmpeg on PATH, and Hyperframes CLI (`npx hyperframes doctor`). Run `npx hyperframes check` in the composition directory and fix all errors; preview settled frames and transitions, correct clipping/collisions/contrast, and check audio balance.
6. **Deliver and verify.** Render `brag.mp4`, choose the strongest settled poster and save `brag.jpg`, bake it into frame 0 without changing duration/audio sync, and write `share-copy.txt`. Verify every file exists before reporting completion. If local tools aren't available, provide reproducible commands and describe deliverables as pending, not complete.

## Creative rules

- Keep it short (15–25s) and make the first 2 seconds specific and strong.
- Show genuine product UI, code, results, or artifacts; no abstract filler.
- Never invent metrics, user quotes, features, testimonials, or outcomes. Flag missing proof.
- Avoid generic SaaS copy such as “streamline your workflow.” Be specific to the project.
- Make all intended-to-be-read text visible long enough (roughly 0.3 seconds per word after it settles). Use movement and cuts rather than flashing text.
- Every frame should work as a shareable still. Respect contrast, keyboard/assistive accessibility when relevant, and reduced-motion preferences on web-hosted previews.
- Voiceover is opt-in only. If explicitly enabled, use the configured upstream supported approach; do not silently select alternative providers.

## Output

Tell the user the creative angle and the exact verified output paths. Include the caption from `share-copy.txt`. Offer changes to a scene or tone if relevant. Never publish/deploy without explicit instruction.
