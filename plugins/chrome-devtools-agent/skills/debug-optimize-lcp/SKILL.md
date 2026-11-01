---
name: debug-optimize-lcp
description: Use when investigating slow page loads or Largest Contentful Paint (LCP), analyzing performance traces and insights, and validating web performance improvements.
---

# Performance and LCP workflow

1. Establish the page, navigation state, test conditions, viewport, and whether the aim is lab diagnostics or field performance. Avoid comparing runs with materially different conditions.
2. Start a trace using `performance_start_trace` (reload when appropriate), stop it with `performance_stop_trace`, and inspect specific insight details using `performance_analyze_insight`.
3. Identify the LCP element and break down delays into TTFB, resource load delay, resource load duration, and render delay when data is available. Inspect the corresponding network request and relevant CSS/DOM.
4. Check common causes with evidence: server response delay, render-blocking resources, late-discovered images, oversized assets, font loading, client-side rendering, and main-thread work.
5. Prefer changes directly connected to the measured bottleneck. Re-run the trace under comparable conditions and report deltas, variability and limits.

If the tool exposes CrUX/field information, explain that it is real-user data and distinct from the lab trace. The server can send trace URLs to the Google CrUX API by default; use `--no-performance-crux` when that data-sharing behavior is not desired. Source: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/debug-optimize-lcp/SKILL.md.
