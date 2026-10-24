---
name: ai-video-storyboard
description: Use when planning a multi-shot AI video such as a Reel, Short, ad, product explainer, or brand story and the user needs a coordinated storyboard, consistent visual direction, shot prompts, audio notes, and an edit checklist.
---

# AI Video Storyboard Generator

## Purpose and limits
Turn a user-provided video brief into a coherent, multi-shot production plan. The objective is continuity across clips, not just individually polished prompts. This skill plans the work; do not claim that video clips have been generated, edited, rendered, uploaded, or sourced unless a connected tool actually did so.

Be faithful to user-provided facts, assets, brand details, websites, architecture, and source material. Never invent real product capabilities, business facts, architectural details, evidence, or source content. If a concept needs facts not supplied, ask for sources or mark clearly labeled assumptions/placeholders. Creative scene ideas may be proposed as creative choices, not represented as facts.

## When to use
- The user wants a video longer than a typical single generated clip or asks for multiple coordinated shots.
- The user needs a TikTok, Reel, Short, ad, product explainer, brand story, trailer, or B-roll sequence.
- The user has a rough idea but lacks a usable storyboard.

For a single-shot prompt, static image generation, or editing footage already generated, answer that focused request instead of forcing this workflow.

## Step 1 — Brief intake
Ask only for details not already supplied. Prefer one compact intake message covering:
1. Platform, target duration, and aspect ratio.
2. Subject, story, purpose, and intended audience.
3. Tone/brand identity and required visual references.
4. End action or exact call to action.
5. Must-use assets, facts, locations, colors, logos, URLs, source documents, and exclusions.
6. What the user actually wants delivered: storyboard, prompts, narration, shot list, production plan, or full handoff.

If the user says to proceed without details, make minimal clearly labeled creative assumptions and keep factual claims grounded. If a real website, product, or architecture is specified, inspect the supplied source or request its contents; do not replace it with an invented approximation.

## Step 2 — Plan the timeline
Choose shot count and duration to serve the story and platform. Five seconds per shot is a useful starting point, not a hard rule. Make segment durations sum exactly to the requested runtime. Explain when estimates depend on the chosen generation tool.

Useful patterns:
- Short social hook: Hook → proof/context → payoff → CTA.
- Ad: Problem → product/solution → benefit/evidence → CTA.
- Explainer: Context → concept/architecture → process → outcome → next step.
- Brand story: Atmosphere → character/detail → emotional reveal → brand/CTA.
- Tutorial: Goal → setup → steps → verification → recap.

Do not force a marketing arc when the user's brief requires a factual walkthrough, documentary, tutorial, or architecture demo.

## Step 3 — Lock the visual continuity layer
Before writing shot prompts, define a reusable **Visual Theme**:
- Palette (named colors or hex codes where useful).
- Lighting and time of day.
- Lens/framing character and depth of field.
- Image treatment (clean digital, subtle film grain, etc.).
- Motion language and camera rules.
- Recurring subject identity, wardrobe, props, environment, and graphic system.
- Continuity rules and deliberate exceptions.

If the user provides a visual reference, describe the observed traits faithfully and use that reference as the source of truth. Do not invent or claim an exact match to assets you have not inspected. A theme may be changed only when the narrative explicitly calls for the change, and the change should be documented.

## Step 4 — Build every shot
For every shot, provide:
- Number, timestamp range, duration, and story purpose.
- Composition and camera angle.
- Camera movement.
- Lighting and continuity notes.
- Exact subject and visible action.
- On-screen text or graphics, with exact copy supplied by the user or marked as proposed.
- Copy-ready prompt, normally 40–80 words unless the user asks otherwise.
- Audio direction: ambience, effects, music timing, and voice-over if needed.
- Transition or match-cut note when useful.

Prompts should be concrete and self-contained. Repeat the relevant visual continuity details in every prompt so separately generated clips remain consistent. Include aspect ratio, duration, and resolution when relevant. Do not promise that a particular phrase, parameter, resolution, or audio directive works for every video model; tool support differs. Avoid model-specific hacks unless the user names the model and the behavior is verified.

For technical product or architecture videos, distinguish confirmed system facts from illustrative visualization. Preserve correct names, relationships, data flows, labels, and security boundaries. If details are absent, use explicitly labeled placeholders rather than fabricated architecture.

## Step 5 — Audio and narrative
Describe sound per shot and the transitions between shots. Keep dialogue or voice-over aligned to actual runtime. Mark any proposed narration as a draft. Specify where music begins, develops, drops, or resolves, but do not invent licensed track availability. Recommend that users use properly licensed audio.

## Step 6 — Post-production checklist
Tailor the checklist to the user's platform and workflow. Cover as applicable:
- Generate and review all shots; regenerate continuity failures.
- Assemble in the editor of the user's choice.
- Match exposure, white balance, palette, and grain.
- Specify transition types and approximate durations.
- Mix ambience, dialogue, effects, and music.
- Add captions and check spelling, safe areas, logo usage, and CTA legibility.
- Check pacing, factual labels, continuity, and platform requirements.
- Export using suitable dimensions, frame rate, codec, and bitrate for the chosen destination; if the platform spec is unknown or may have changed, label recommendations as defaults and verify current requirements.

Do not state the footage is ready or that quality checks passed unless it was actually reviewed.

## Step 7 — Explain why it works
Briefly justify the shot order, emotional or explanatory progression, pacing, continuity choices, and CTA placement. Keep the rationale specific to this brief rather than relying on unsupported engagement statistics or generic claims.

## Required final structure
1. Title, purpose, platform, runtime, shot count, aspect ratio.
2. Brief summary and assumptions (omit assumptions if none).
3. Shared Visual Theme and continuity rules.
4. Timeline / shot list with shot-by-shot detail and copy-ready prompts.
5. Audio plan.
6. Post-production checklist.
7. Why this structure works.
8. Open questions or factual placeholders, only when needed.

## Accuracy and integrity rules
- Use user-provided and inspected source content as ground truth for factual work.
- Never invent facts or imply invented scenes are real footage, real product UI, verified architecture, or authentic source content.
- If a source URL is supplied and access is unavailable, say so and ask for relevant screenshots, files, or excerpts.
- Clearly separate verified facts, creative proposals, and unknowns.
- Use exact supplied calls to action, product names, and labels. Do not fabricate logos, names, metrics, testimonials, or proof points.
