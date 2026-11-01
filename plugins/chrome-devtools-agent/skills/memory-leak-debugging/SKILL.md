---
name: memory-leak-debugging
description: Use when investigating growing browser memory usage, suspected JavaScript leaks, retained DOM nodes, detached elements, or heap snapshot differences in Chrome.
---

# Browser memory leak investigation

Memory tools are optional and may require starting the server with `--memoryDebugging` (or the corresponding supported flag for the installed version). Confirm tool availability before assuming these operations exist.

1. Reproduce the suspected leak with a repeatable interaction sequence and record baseline behavior.
2. Capture a heap snapshot using `take_heapsnapshot` and compare with a snapshot taken after repeated interactions/cleanup. Keep snapshots in a controlled location because they may contain sensitive in-memory application data.
3. Use `get_heapsnapshot_summary`, `compare_heapsnapshots`, `get_heapsnapshot_details`, and class/retainer/edge/path tools as available to identify growing types and retaining references.
4. Trace a suspected retaining path to a concrete owner, such as a listener, timer, cache, closure, detached DOM tree, or long-lived collection. Growth alone is not sufficient evidence of a leak.
5. Propose a targeted cleanup or lifecycle fix, repeat the same action sequence, and verify retained-object growth decreases.
6. Close loaded heap snapshots when done and do not share raw snapshots unless explicitly required and appropriately sanitized.

Do not assert a leak solely from one memory reading; consider normal caches and garbage collection. Source: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/memory-leak-debugging/SKILL.md.
