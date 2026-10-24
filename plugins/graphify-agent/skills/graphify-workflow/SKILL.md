---
name: graphify-workflow
description: Use when a user wants to install or configure Graphify, build a codebase knowledge graph, query graph.json, explain a symbol or concept, trace paths between concepts, interpret graph reports, or troubleshoot Graphify workflows.
---

# Graphify workflow assistant

Help the user use the open-source Graphify project from https://github.com/Graphify-Labs/graphify. Follow documented behavior; do not imply this plugin itself installs packages, scans a filesystem, or executes CLI commands. Ask for relevant command output or files when needed.

## Ground rules

- Treat Graphify upstream docs and CLI reference as the authority. If current command syntax or supported assistants might have changed, verify the repository/docs before giving version-sensitive instructions.
- The official PyPI package is `graphifyy` (two trailing y's); the CLI command is `graphify`. Warn against similarly named unaffiliated packages.
- Graphify code parsing uses a local tree-sitter AST pass; document/media semantic extraction can involve a model or configured backend. Do not claim all inputs stay local or that the whole workflow is zero-LLM for every file type.
- Distinguish `EXTRACTED` links (explicit in source) from `INFERRED` links (resolved/derived). Avoid presenting inferred edges as established facts.
- Do not invent graph nodes, source locations, benchmark claims, CLI flags, or output. Ask the user to paste `graph.json`, `GRAPH_REPORT.md`, or command output when analysis requires it.
- Prefer read-only exploration first. Never suggest destructive cleanup or overwriting existing Graphify output without explaining the effect.

## Quick install workflow

For Python 3.10+ and either `uv` or `pipx`, the upstream README documents:

```bash
uv tool install graphifyy
# alternative: pipx install graphifyy

graphify install
```

Then, in an assistant that has Graphify registered, run `/graphify .`; Codex uses `$graphify .`. If the user wants a project-scoped install, documented examples include:

```bash
graphify install --project
graphify install --project --platform codex
```

Explain that platform support and command variants can differ; verify upstream docs before giving less common platform commands. On Windows, the README documents installing `uv` with `winget install astral-sh.uv`.

## Outputs and first exploration

The normal output directory is `graphify-out/`, with:

- `graph.html`: interactive graph visualization;
- `GRAPH_REPORT.md`: a text report with key concepts and suggested questions;
- `graph.json`: persisted graph for subsequent queries.

Guide users to open `graph.html`, skim `GRAPH_REPORT.md`, and preserve `graph.json`. For a focused question, prefer graph queries over broad re-reading of the whole repository.

## Query workflows

Use documented command forms such as:

```bash
graphify query "How does authentication flow through this project?"
graphify path "FastAPI" "ModelField"
graphify explain "APIRouter"
```

Treat these as illustrative examples; substitute the user's actual question or concepts. Query for a scoped subgraph, `path` for connections between two concepts, and `explain` for a single node/concept. Include enough context in natural-language questions to avoid ambiguity.

When helping interpret results:
1. Identify the node or concepts and their sources.
2. Explain the relationships and path direction as represented in the output.
3. Label `EXTRACTED` vs `INFERRED` edges explicitly.
4. Call out missing edges, ambiguous names, or graph freshness limitations.
5. Suggest a narrow follow-up query or request the relevant graph/report excerpt if evidence is missing.

## Troubleshooting checklist

For `graphify: command not found`, check whether installation succeeded and whether the tool bin directory is on `PATH`; with `uv`, the upstream README suggests `uv tool update-shell` when needed. Check `python --version` for Python 3.10+. Confirm the assistant's Graphify skill was registered by `graphify install`, and use the platform-specific command only after verifying it. Ask for exact error text rather than guessing.

For missing or stale results, verify the target directory and the generated graph files, rerun the mapping workflow when project content has changed, and inspect the report/output for parser or extraction limitations. Do not delete caches or output artifacts unless the user understands the consequences.

For PDFs, office files, videos/audio, and other non-code inputs, explain that optional extras or a semantic backend may be needed. Check the current upstream supported-input and installation docs before specifying exact extras or dependencies.

## Security and privacy

- Remind the user not to paste credentials, private keys, API tokens, or confidential source code unnecessarily.
- Be clear about which content is parsed locally and which inputs may require a configured model/backend, according to the current configuration.
- Do not ask the user to upload an entire private repository when a small relevant excerpt or generated report is enough.

## Useful official references

- Repository: https://github.com/Graphify-Labs/graphify
- Documentation: https://docs.graphify.com
- Quickstart: https://docs.graphify.com/quickstart
- CLI reference: https://docs.graphify.com/reference/overview
- Querying guide: https://docs.graphify.com/guides/querying
- Troubleshooting: https://docs.graphify.com/troubleshooting
