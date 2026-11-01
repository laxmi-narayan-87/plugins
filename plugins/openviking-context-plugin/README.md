# OpenViking Context Assistant

A private skills-focused plugin to help configure and use OpenViking as a context database for agent memory, knowledge resources, retrieval, and skills.

- Upstream project: https://github.com/volcengine/OpenViking
- Documentation: https://docs.openviking.ai/
- Scope: instructional workflows only; no server is bundled or deployed by this package.
- Connection note: OpenViking's upstream Codex example uses local plugin files and a stdio proxy. This package intentionally does not invent a remote MCP URL. Configure a verified integration separately for the chosen runtime.

See `skills/openviking-context-workflow/SKILL.md` for the workflow and security guidance.
