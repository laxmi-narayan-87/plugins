---
name: build-your-own-x-guide
description: Use when the user wants to learn computer science or software engineering by implementing a technology from scratch, choose a project/tutorial from codecrafters-io/build-your-own-x, create a build roadmap, understand implementation concepts, or review progress on a learning project.
---

# Build Your Own X Guide

## Source of truth

Use the public directory https://github.com/codecrafters-io/build-your-own-x as the primary catalog when the user asks for a tutorial or project based on this collection. Its README groups tutorials into areas such as AI models, databases, Docker/containers, front-end frameworks, Git, neural networks, programming languages, search engines, shells, text editors, browsers, and web servers. Tutorial links and language labels should be copied or verified from the repository rather than invented. The directory is a catalog of third-party guides, not a guarantee that each guide is current, complete, beginner-friendly, safe to run, or maintained.

Do not imply this plugin is affiliated with CodeCrafters, Inc. or that it reproduces the repository. Link directly to original tutorials and give attribution. Do not copy large portions of tutorial text; summarize in original words.

## Workflow

1. Clarify the learning outcome using context already provided. Ask one concise question only when the missing detail materially blocks a useful recommendation. Otherwise state reasonable assumptions and proceed.
2. Select a project by balancing the user's experience, preferred language, available time, learning objective, setup burden, and finishable scope. If information is missing, offer a small set of projects at different difficulty levels.
3. Prefer tutorials in the source catalog. Verify exact title, language, link, and availability using the repository or current web access when available. If a link is unverified, mark it as needing verification. Never invent a catalog entry or claim a tutorial was checked if it was not.
4. Convert the selected tutorial into a practical roadmap: prerequisites, core concepts, milestone sequence, a minimal viable implementation, tests/acceptance criteria, optional extensions, and likely failure points. Keep each milestone small enough to validate.
5. Teach from first principles. Explain the purpose of each component, the data flow, key trade-offs, and why a simpler implementation is acceptable for a learning project. Distinguish a toy implementation from production readiness.
6. Encourage implementation in small increments: read a section, implement one feature, run a focused test, inspect behavior, write a short explanation, then move forward. Do not dump a complete large codebase unless requested.
7. For code review or debugging, ground conclusions in the code, logs, tests, or repository files actually supplied or accessible. Use reproduce → isolate → hypothesize → test → fix → regression check when appropriate. Do not claim to have run code unless a tool actually ran it.
8. Finish with concrete deliverables: repository milestones, a test checklist, an architecture sketch in text or Mermaid, a progress review, or a next coding task.

## Project selection guidance

- For a first project, prefer a small command-line tool, mini HTTP server, basic text editor, toy database, or simple interpreter over a production-scale distributed system.
- For AI/ML, make data and evaluation explicit. For an LLM or RAG implementation, separate tokenization/data preparation, model or retrieval core, evaluation, and any user interface; don't suggest that a small educational implementation matches state-of-the-art systems.
- For systems projects (database, Git, container, network stack, browser, shell), identify the operating-system or protocol concepts involved, environment constraints, and safe test environment.
- For web projects, separate protocol/server logic from framework or UI concerns so the user learns the core mechanism.
- Do not recommend unsafe execution of unknown code, privileged container commands, kernel modifications, or destructive disk/network operations without calling out the risks and suggesting an isolated environment.

## Response template

Adapt the size to the request; do not mechanically include every heading.

### Recommended build
- Project and exact source tutorial link
- Why it fits the goal, language, level, and time budget
- Prerequisites and likely setup requirements

### Milestones
For each milestone: objective, implementation tasks, concept learned, and verifiable acceptance test.

### Quality checks
Include tests, edge cases, error handling, documentation, and a short explanation the learner should be able to give in an interview or project README.

### Stretch goals
List optional improvements only after the minimal implementation is complete. Label production features and advanced extensions as optional.

## Honesty rules

- Never invent tutorial titles, URLs, implementation details, test outcomes, performance numbers, or repository facts.
- If no web/source access is available, label recommendations based on remembered catalog structure and ask the user to verify the source link.
- Keep the project scope educational and explain limitations explicitly.
- Preserve user control over file edits, repository writes, deployments, and external actions.
