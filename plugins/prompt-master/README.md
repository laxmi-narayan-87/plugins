# Prompt Master — ChatGPT Plugin

A private ChatGPT plugin adaptation of [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master), originally authored by Nidhin Joseph Nelson.

## Use case

Write, diagnose, improve, simplify, split, or adapt prompts for language models, coding agents, image/video generators, research assistants, and automation tools.

## Core functionality

- Identifies the target tool and surface before selecting prompt structure.
- Extracts task, context, constraints, output format, audience, and success criteria.
- Uses 14 reusable prompt structures for common tasks.
- Diagnoses 37 common prompt failure patterns.
- Adds scope limits, stop conditions, and approval gates for agentic workflows.
- Avoids hidden-reasoning requests, credential exposure, fabricated model settings, and ungrounded citations.
- Produces one concise, ready-to-paste prompt by default.

## Original source

- Repository: https://github.com/nidhinjs/prompt-master
- Original license: MIT
- Original skill and reference content adapted and reorganized for the portable Agent Plugins format.

## Structure

- `plugin.json` — plugin metadata and ChatGPT presentation.
- `skills/prompt-master/SKILL.md` — main workflow and behavioral instructions.
- `skills/prompt-master/references/templates.md` — reusable prompt templates.
- `skills/prompt-master/references/patterns.md` — diagnostic checklist.
