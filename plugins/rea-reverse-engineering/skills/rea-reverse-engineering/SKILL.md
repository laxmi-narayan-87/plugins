---
name: rea-reverse-engineering
description: Use when planning, running through, or interpreting software reverse-engineering workflows based on the REA CLI/MCP toolkit, including websites, JavaScript/Electron apps, native binaries, Android artifacts, databases, and captured network traffic.
---

# REA reverse-engineering workflows

## Purpose and limits

Guide an evidence-led investigation using the public REA project at https://github.com/morluto/rea. This skill is a companion workflow, not the REA execution engine. Do not claim to have run commands, accessed a local target, connected to REA's MCP server, or observed artifacts unless a connected tool actually did so.

REA's documented standard local MCP package is `rea-agents`, launched with the `mcp` argument over stdio. Its primary setup command is `npx rea-agents@latest setup`. Use the user's compatible local agent/client and carefully review the setup plan before approving changes. Follow the current official installation guide at https://github.com/morluto/rea/blob/main/docs/installation.md; runtime and supported tools can change between releases.

## Investigation workflow

1. **Clarify target and authorization.** Identify the artifact (file/path, application, website, device, database, or capture), the exact question, the user's authorization, operating system, and any constraints. For third-party systems, limit work to authorized testing and lawful access. Avoid collecting secrets or private data beyond what is necessary.
2. **Choose the narrowest workflow.** Check REA's current README and the target-specific documentation. Do not assume a feature exists in the installed version; the repository may be ahead of the published package.
3. **Check prerequisites.** Distinguish static analysis from runtime capture. Static JavaScript/.NET analysis can inspect supplied files without executing the application. Runtime workflows may launch processes or interact with targets. Native analysis may require a configured provider such as Hopper, Ghidra, IDA, or another documented provider; other formats may need caller-supplied tools such as JADX, adb, WABT, tshark, or platform utilities. Explain the relevant side effects before running commands.
4. **Plan before execution.** Prefer read-only inventory or diagnostic calls first, scoped paths, explicit timeouts, and output limits. Do not suggest destructive edits, uploads, device transfers, or live interaction without describing their effect and getting appropriate authorization.
5. **Inspect evidence.** When connected to REA, use its actual advertised tool schemas and returned structured content. Preserve evidence IDs, artifact identity, analysis profile, coverage, and limitations. For large results, follow the tool's documented continuation/view mechanism rather than inferring missing fields from a truncated response.
6. **Report carefully.** Separate observed facts from hypotheses and recommendations. Include artifact/path, method, evidence, limitations, and a reproducible next step. An absent result is not proof of absence when coverage is partial or unknown. Static artifact equality does not establish equivalent runtime behavior.
7. **Suggest validation.** Where useful, reproduce the behavior on a controlled sample, compare artifacts using compatible REA evidence, or run documented tests. Never invent tool output or claim validation that has not occurred.

## Useful entry points

- Setup / connect local agents: `npx rea-agents@latest setup`
- CLI install: `npm install --global rea-agents` (or use the current official package instructions)
- CLI help: `rea --help`
- Runtime readiness: `rea doctor --json` where supported by the installed version
- JavaScript/Electron analysis example from the README: `npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json`

Commands are examples, not automatic permission to run them. Verify current documentation and the installed CLI's help before relying on exact flags.

## Output format

For an investigation plan, return:
- Question and authorized target
- Recommended REA workflow and why
- Prerequisites and side effects
- Minimal commands or MCP operations
- What evidence to save
- How to interpret results and what they cannot prove
- One safe follow-up test

For findings, label each key conclusion as **Observed**, **Inferred**, or **Unknown** and cite the returned REA evidence or source location when available.
