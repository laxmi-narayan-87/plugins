---
name: visual-regression
description: Use when the user needs screenshot-based comparison of a reference site and its clone, redesign, deployment, or UI before and after changes.
---
# Visual regression and reference matching

## Purpose
Compare evidence captured under controlled conditions; do not infer exact pixel parity from text or a single screenshot.

## Capture protocol
1. Establish reference URL, candidate URL, route mapping, page list, browser/version, viewport sizes, device scale factor, locale, timezone, color scheme, and authentication state.
2. Capture both sites with the same browser, viewport and scroll positions. Wait for a stable state, fonts and images; disable animations only if that does not hide behavior being tested.
3. Capture full-page and targeted viewport screenshots. Preserve originals and label source URL, candidate URL, viewport, timestamp and commit/deployment.
4. Compare screenshots and, where possible, compute pixel diff, overlay and perceptual/structural metrics. Align crop and page dimensions before interpreting differences.
5. Separate real mismatches from dynamic content, timestamps, ads, randomized IDs, third-party widgets and font-rendering noise.
6. Report each mismatch with page, viewport, region, severity, evidence image or coordinates, confidence and likely cause. Label unverified explanations as hypotheses.
7. Rerun after fixes using the same protocol. Do not call the site an exact clone until all specified routes/viewports have been checked.

## Functional parity
Pair visual comparison with checks for links, nav, controls, content completeness, responsiveness, loading failures, accessibility basics and browser console errors.

## Output
Produce a route-by-route report and a concise pass/fail/unknown matrix. Preserve reference assets and text; do not redesign or silently change content when the request is fidelity reproduction.
