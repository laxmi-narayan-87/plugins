# Claudex Loop Assistant plugin package

This is a skills-based ChatGPT plugin inspired by the public `chaseai-yt/claudex-loop` repository. It includes a careful workflow for software recon, planning, adversarial review, implementation boundaries, proof checks, and independent inspection, plus a separate task-routing skill.

## Scope and limitations

This package provides instructions and workflow support. It does not include a remote MCP server, provision local processes, or run the Claude Code/Codex CLIs. Full cross-provider execution depends on those CLIs being installed and authenticated in the user's own environment. Do not represent workflow guidance as a completed execution.

## Included files

- `plugin.json` — plugin identity and interface metadata.
- `skills/claudex-loop/SKILL.md` — full workflow.
- `skills/claudex-route/SKILL.md` — routing workflow.

Source concept: https://github.com/chaseai-yt/claudex-loop

## Use case and core functionality

Use case: Run a disciplined multi-stage engineering loop for complex software tasks.

Core functionality: Reconnaissance, planning, adversarial review, implementation boundaries, proof checks, independent inspection, and task routing.

