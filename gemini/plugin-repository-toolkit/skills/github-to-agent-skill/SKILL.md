---
name: github-to-agent-skill
description: Convert a GitHub repository, tool, framework, or documented workflow into a focused reusable Claude Code Agent Skill with verified source attribution. Use when the user provides an upstream repository/link and asks to create a skill or plugin from it.
---

# GitHub Project to Agent Skill

## Workflow
1. Open the exact user-provided source. Confirm canonical repository, owner, purpose, license when relevant, current structure, and original documentation.
2. Identify the narrow capability the skill should teach. Do not copy an entire repository or combine unrelated jobs.
3. Extract only task-relevant procedures, constraints, API usage, examples, and prerequisites. Distinguish upstream facts from your own adaptations.
4. Draft `.claude/skills/<skill-name>/SKILL.md` with frontmatter:
   - `name`: lowercase, hyphenated, stable
   - `description`: precise trigger conditions and intended task
5. Write focused instructions: prerequisites, ordered workflow, safety constraints, verification, and output expectations. Include 2 good examples and 1 bad example with why it fails.
6. Add `CHANGELOG.md` in the same skill directory. Add templates/scripts only if they remove repeated effort and are truly needed.
7. Preserve original-source attribution with a direct upstream URL. Never claim upstream endorsement.
8. Check the skill for excessive length, duplicated instructions, vague triggers, unsupported claims, secrets, and overlap with existing skills.
9. Test against one real task: follow the skill, record expected actions/output, identify gaps, revise the skill (not merely the one output), then rerun.

## Rules
- Keep one skill focused on one job; compose other skills rather than duplicating them.
- Plain language, concise by default; detailed only where needed.
- Never put passwords, API keys, tokens, or private credentials in skill files.
- A skill must not send, post, delete, pay, publish, or deploy without explicit approval.
- Do not invent upstream behavior or license terms; state unknowns.

## Examples

**Good:** “Source: https://github.com/owner/project. Skill: `project-test-helper`. Trigger only for testing this project's supported APIs; document prerequisites and test commands; verify the command against upstream docs.”

**Good:** “Adapt the upstream frontend-design workflow into a skill for creating polished UI; preserve attribution, add a focused description, and test it on an existing portfolio page.”

**Bad:** “Copy the repository README wholesale into a skill and call it done.” Why bad: no task boundary, workflow adaptation, trigger description, verification, or maintainability.

## Completion checklist
- [ ] Exact upstream source checked
- [ ] One focused use case defined
- [ ] Frontmatter name and trigger description precise
- [ ] Workflow, rules, 2 good examples, 1 bad example included
- [ ] Changelog added
- [ ] Attribution verified
- [ ] No secrets or unsafe autonomous actions
- [ ] Real case test run and skill revised if needed
