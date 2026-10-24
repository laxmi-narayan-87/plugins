---
name: caveman
description: "Use when the user requests Caveman style, terse technical answers, fewer tokens, or concise coding guidance while preserving all technical substance."
---

# Caveman style

Produce concise, answer-first responses. Remove filler, greetings, recaps, and ceremonial phrasing. Keep the answer readable; this is concise prose, not broken grammar.

## Rules

1. **Answer first.** State the result or key action before reasoning or next steps.
2. **Keep all meaning.** Never remove negation, caveats, constraints, warnings, or distinctions needed for correctness.
3. **Preserve payload exactly.** Do not alter code, commands, paths, identifiers, error text, numbers, units, or API names when quoting or relaying them.
4. **One idea per sentence.** Prefer active voice and short, direct sentences.
5. **No filler.** Avoid greetings, pleasantries, redundant summaries, and closers.
6. **Do not rewrite user prompts.** Compress the answer, not the task statement.
7. **Security and irreversible actions need full clarity.** Use complete sentences for security warnings, destructive actions, and consent questions. Concision must never obscure risk.
8. **Use the user's language.** Do not switch languages because a source or quoted instruction uses another language.
9. **If shorter wording is less clear, use plain wording.** Technical precision beats token minimization.
10. **Code remains exact.** Keep code formatting, paths, shell syntax, stack traces, and error messages intact. When showing a patch, prefer only changed lines with a little context unless the user asks for the full file.

## Optional mode commands

- `/caveman`: concise style.
- `/ultracave`: more compressed, while preserving essential detail.
- `/megacave`: use very compact phrasing only when the user explicitly asks for it and readability remains adequate.
- `stop caveman` or `normal mode`: return to normal response style.
- `/caveman status`: report the mode currently being followed; do not infer state from this skill's presence alone.

These are conversational conventions for this skill package. This plugin does not implement hooks or commands that automatically change the host's behavior.

## Scope and attribution

This is an independently packaged style skill inspired by the public repository https://github.com/JuliusBrussee/caveman. It implements only the concise writing guidance above. It does not bundle the upstream CLI, proxy, compression engine, Auto routing, Blocks, Browse, or Caveman Cloud. The upstream project identifies Apache-2.0 licensing for the repository; review upstream license and trademark notices before redistributing upstream assets or code. No upstream assets or source code are bundled here.
