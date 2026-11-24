# Plugin Repository Toolkit

> Essential toolkit for discovering AI tools, converting GitHub repositories to agent skills, managing plugin repositories, and auditing/repairing skills.

## Overview
`plugin-repository-toolkit` packages the core repository engineering and management skills adapted from the central `.claude/skills` directory into a standalone Antigravity plugin.

## Bundled Skills
- **`ai-tool-discovery`**: Available in `skills/ai-tool-discovery/SKILL.md`
- **`github-to-agent-skill`**: Available in `skills/github-to-agent-skill/SKILL.md`
- **`plugin-repository-manager`**: Available in `skills/plugin-repository-manager/SKILL.md`
- **`repository-audit-repair`**: Available in `skills/repository-audit-repair/SKILL.md`
- **`workflow-automation-engineer`**: Available in `skills/workflow-automation-engineer/SKILL.md`

## Suggested Prompts
- `Convert a GitHub repository into an agent skill package`
- `Audit this plugin repository for schema errors and missing documentation`
- `Discover and compare AI tools and MCP servers for my project`

## Installation
```bash
Copy-Item -Recurse "plugin-repository-toolkit" "$HOME\.gemini\config\plugins\plugin-repository-toolkit"
```

## License
MIT
