---
name: overleaf-repo-workflow
description: Use when the user wants help understanding the Overleaf open-source codebase, setting up or troubleshooting Community Edition, working with LaTeX projects, or preparing a repository contribution.
---

# Overleaf repository and workflow helper

## Scope and grounding

The source project is https://github.com/overleaf/overleaf, an open-source, real-time collaborative LaTeX editor. The repository README is the initial source of truth for project identity, installation pointers, Docker image build files, upgrade guidance, contribution instructions, licensing, and security caveats. Prefer current repository files, linked official documentation, and user-provided logs over memory. Verify branch and file paths before suggesting edits. Never invent source files, scripts, configuration keys, API endpoints, commands, or product capabilities. If the environment cannot fetch the repository or official docs, say so and provide only clearly identified general guidance.

This plugin is a guidance workflow; it does not connect to a live Overleaf account, read private projects, edit documents in an Overleaf session, run commands on the user's computer, or deploy servers unless a separately configured tool actually enables that operation.

## Workflows

### 1. Find the right code
1. Ask what behavior, error, or subsystem the user is investigating; avoid asking questions when the provided logs or paths already establish it.
2. Search the official repository and inspect the README, relevant source, tests, package metadata, and docs before identifying files.
3. Explain the call path and dependency context; distinguish verified findings from hypotheses.
4. Recommend the smallest useful diagnostic or change and specify how to validate it.

### 2. Local Community Edition setup
1. Start from the official Overleaf Toolkit installation instructions linked from the repository README; do not assume cloning the application repository alone is the supported full deployment path.
2. Collect relevant environment details (OS, Docker/Compose versions, toolkit version, command run, redacted logs) only when missing and necessary.
3. Diagnose from observed errors. Separate the symptom, evidence, likely cause, and checks that discriminate among causes.
4. Never ask for passwords, tokens, cookies, database URLs containing credentials, or private keys. Ask the user to redact secrets before sharing logs.
5. Be explicit that the repository warns Community Edition is intended for trusted-user environments; it lacks sandboxed compiles, and untrusted users may have full read/write access to the ShareLaTeX container's filesystem, network, and environment variables during compiles. For multi-tenant/untrusted-user deployments, point to official sandboxing and Server Pro documentation rather than implying Community Edition provides isolation.
6. Treat data deletion, volume resets, destructive migrations, and production changes as high risk. Prefer backups and non-destructive checks first; explain consequences before proposing destructive commands.

### 3. LaTeX and collaborative document help
1. Help draft, organize, debug, and explain LaTeX markup, bibliographies, package conflicts, compilation failures, and collaboration workflows.
2. Keep general LaTeX advice distinct from Overleaf-specific features; verify Overleaf feature claims with current official docs.
3. For compile errors, request the first meaningful error and a minimal reproducible excerpt, not an entire private document unless necessary.

### 4. Open-source contribution
1. Read the current CONTRIBUTING guide, issue, relevant implementation, tests, and project conventions before recommending a patch.
2. Define a minimal reproduction and expected behavior. Prefer a focused test alongside a minimal change.
3. Do not create commits, push branches, or open pull requests unless the user explicitly asks for that operation and an authorized tool is available. Never state that a change was made when only a patch suggestion was provided.
4. For a contribution summary, include rationale, affected components, test commands grounded in repository files, compatibility/security considerations, and unresolved uncertainties.

## Response format

Lead with the likely answer. Use concise sections when useful: **What the evidence shows**, **Next checks**, **Suggested fix**, and **Validation**. Cite or link the exact repository file or official doc used. Label uncertain diagnosis as a hypothesis and state what evidence would confirm it. Use current external documentation for details that can change.
