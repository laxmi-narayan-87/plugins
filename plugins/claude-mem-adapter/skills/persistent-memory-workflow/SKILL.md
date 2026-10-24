---
name: persistent-memory-workflow
description: Use when the user wants to capture durable context, recall prior project decisions, organize memory, or summarize history efficiently and privately.
---

# Persistent Memory Workflow

This skill adapts selected ideas from [claude-mem](https://github.com/thedotmack/claude-mem) to conversational use: durable observations, concise indexing, progressive disclosure, chronological context, and privacy-aware capture. It is not the claude-mem application and does not run lifecycle hooks, access local files automatically, or connect to its SQLite/vector database.

## Core rules

1. **Capture only durable, useful context.** Prefer recurring preferences, ongoing project decisions, constraints, verified facts, and unresolved next steps. Do not preserve transient chatter unless requested.
2. **Keep facts distinct from inference.** Label uncertain or user-reported details as such; do not turn an assumption into a fact. Preserve dates and source context when relevant.
3. **Respect privacy.** Do not store passwords, API keys, tokens, security answers, financial account identifiers, precise location, or other secrets. Avoid sensitive personal data unless the user explicitly asks to remember it and the applicable platform policy allows it. Honor requests not to retain or mention a topic.
4. **No false claims about persistence.** Only claim a memory was saved when the platform actually confirms a save. In an ordinary chat, draft a memory note or summarize what should be retained; do not claim it will automatically be available in a future session.
5. **Prefer compact, actionable notes.** Capture the decision, reason, status, and next step rather than a long raw transcript.

## Capture workflow

When asked to remember or preserve context:

- Identify the stable fact, preference, project, decision, or constraint.
- Exclude secrets and unnecessary sensitive details.
- Write a short record with an appropriate category and date where useful.
- If the user asks for memory persistence, use the available platform memory capability; otherwise provide a clearly labeled note they can save.
- If the detail is ambiguous or conflicts with an earlier record, keep the uncertainty explicit instead of silently choosing a version.

Suggested record format:

- **Topic:** concise title
- **Type:** preference / project decision / verified fact / open question
- **Context:** minimal detail needed later
- **Status:** current / superseded / uncertain
- **Next step:** only if one exists
- **Updated:** date, when useful

## Recall workflow: progressive disclosure

Use three passes instead of dumping all history at once:

### Pass 1 — Index
Return a compact list of the most relevant records with topic, date/status, and a one-line reason each. Ask for more only when needed; do not require a follow-up if the answer is already clear.

### Pass 2 — Timeline
For selected records, reconstruct chronology: what changed, why it changed, and which decision superseded another. Keep unrelated workstreams separate.

### Pass 3 — Details
Expand only the selected records, preserving exact technical names, error strings, constraints, links, and confirmed next steps. State what evidence is missing.

When searching documents, files, or repositories, search first, open the specific relevant source second, then synthesize. Cite source material when the environment supports citations. Do not claim to have searched a database, file, or past session that is not actually available.

## Memory maintenance

- Merge duplicate notes; keep the newest non-conflicting value and retain prior values only when a history matters.
- Mark completed work as completed and unresolved work as open.
- Distinguish a proposed solution from a tested or deployed solution.
- Keep project context partitioned by project; do not let one project's assumptions leak into another.
- For technical troubleshooting, retain reproducible symptoms, environment, attempted fixes, observed results, and the next diagnostic step.
- Periodically identify stale records and ask before deleting meaningful history unless the user explicitly requested cleanup.

## Response patterns

**Capture:** give a concise proposed memory entry, and be transparent about whether it was actually saved.

**Recall:** lead with the best matching concise summary, then provide chronology or deeper details only as useful.

**Project handoff:** summarize objective, current state, verified facts, decisions, blockers, next actions, and source links.

**Privacy request:** avoid repeating the requested topic. Explain platform memory controls accurately when relevant; never imply a chat message itself erased all copies or sources.

## Relationship to source project

The source repository describes a system for persistent context across coding-agent sessions using observations, summaries, hooks, a worker service, SQLite, and search tools with a compact-index → timeline → full-detail pattern. This skill intentionally adapts the workflow ideas only. No claude-mem runtime, server, tool API, data store, or automated session capture is bundled, configured, or implied.
