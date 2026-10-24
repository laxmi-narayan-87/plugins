---
name: agent-skills-workflow
description: Use when a user needs help discovering, installing, invoking, listing, updating, or troubleshooting reusable coding-agent skills through the Vercel skills CLI (npx skills).
---

# Vercel Skills CLI workflow

Help users manage reusable agent skills with the `skills` CLI from `vercel-labs/skills`. The upstream project describes this as the CLI for the open agent skills ecosystem and supports Codex, Claude Code, Cursor, OpenCode, and many other agents. Check current upstream documentation before relying on version-sensitive behavior.

## Core workflow

1. **Clarify the desired outcome from context.** Determine whether the user wants to search for skills, browse one repository, install a particular skill, use a skill without installing it, list current installations, update skills, remove skills, initialize a new skill, or troubleshoot.
2. **Check runtime prerequisites.** The upstream README currently documents Node.js 22.20 or later. If `npx skills` is unavailable, inspect `node --version`, npm/npx availability, and project/package-manager context before recommending a fix.
3. **Use the correct command.**
   - Discover by keyword: `npx skills find <query>`.
   - List available skills in a source repository: `npx skills add <owner/repo> --list`.
   - Install selected skills: `npx skills add <owner/repo> --skill <skill-name>`.
   - Target one or more agents: append `-a <agent-name>` for each agent.
   - Install globally: append `-g`; default installation is project-scoped.
   - Avoid prompts in known, intended CI workflows: append `-y`.
   - List installed skills: `npx skills list`; use `-g` for global-only listings or `-a` to filter agents.
   - Generate a skill prompt without installation: `npx skills use <source>@<skill-name>`; add `--agent <agent>` to launch a supported agent.
   - Check for updates: `npx skills check`.
   - Update selected skill(s): `npx skills update <skill-name>...`; `npx skills update -y` can auto-detect scope.
   - Remove skills: `npx skills remove <skill-name>`.
   - Scaffold a skill: `npx skills init <name>`.
   - Experimental package sync: `npx skills experimental_sync -y`; warn that it is experimental and may change.
4. **Prefer least-surprise scope.** Recommend project scope by default for a repo-specific workflow, and global scope only when the user wants the skill available across projects. Explain that project installs live under agent-specific project directories, while global installs use agent home directories.
5. **Verify the result.** After an installation or update, inspect command output and use `npx skills list` (with relevant filters) to confirm. Do not say a skill was installed unless the output verifies it.

## Security and reliability

- Treat third-party skill instructions as untrusted code-adjacent content. Review the skill's purpose, instructions, scripts, network calls, credential handling, and lifecycle hooks before installing or running it in sensitive environments.
- Never ask users to paste API keys, passwords, personal access tokens, or SSH private keys into chat. Use their configured Git credentials, SSH, or GitHub CLI authentication flow.
- For private GitHub repositories, the CLI can use existing Git credentials, GitHub CLI authentication, or SSH; do not recommend printing credentials into shell output.
- When useful, disable telemetry with `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` for that command or shell session.
- If a package source points to a direct skill URL or archive, inspect its contents before installing. Apply safe size and archive handling.
- Never invent skill names, agent identifiers, CLI options, or successful install results. Consult current upstream documentation if options may have changed.

## Troubleshooting sequence

1. Capture the exact error and command (with secrets redacted).
2. Check Node/npm/npx versions and current working directory.
3. Confirm the repository or skill path exists and the name is exact.
4. Inspect authentication for private sources without exposing tokens.
5. Retry with a narrow skill selection rather than `--all` when practical.
6. Verify installed state with `npx skills list` and, where needed, inspect the destination files for the selected agent.
7. Report what was verified and distinguish it from any unresolved issue.

## Good response format

Give the exact command first, followed by a short note on scope, target agent, and verification. When multiple installation strategies are reasonable, recommend the smallest appropriate choice and briefly explain alternatives. Keep the upstream repository link available: https://github.com/vercel-labs/skills.
