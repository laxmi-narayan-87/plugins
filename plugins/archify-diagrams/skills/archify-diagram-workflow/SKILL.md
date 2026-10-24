---
name: archify-diagram-workflow
description: Use when the user wants to turn an idea, plan, process, or codebase into a clear interactive architecture diagram, flowchart, sequence diagram, system map, or explainer page in the style documented by Archify.
---

# Archify diagram workflow

Use this workflow to plan and author diagram-ready content inspired by the public Archify project. The upstream project describes an agent skill that can produce interactive HTML visualizations from ideas, plans, and codebases, including source-backed architecture maps. This plugin only supplies workflow guidance; it does not bundle Archify's JavaScript implementation, render diagrams by itself, run repository inspection commands, or provide a hosted MCP endpoint.

## 1. Identify the task and evidence boundary

Determine which input the user supplied:

- **Idea or plan:** model only relationships explicitly stated by the user. Mark missing details as assumptions or open questions.
- **Codebase or repository:** inspect actual files using the available repository/file tools before describing implementation. Do not infer architecture from a repository name or README alone when code-level claims are requested.
- **Existing diagram:** preserve confirmed nodes and edges, then make only requested changes.
- **Explainer:** give the conclusion first, then organize the explanation into focused panels that pair each question or step with the relevant diagram section.

Never invent components, integrations, endpoints, infrastructure, behavior, metrics, sources, or repository paths. Distinguish verified facts, reasonable inferences, and unknowns.

## 2. Choose a diagram type

Choose the smallest useful representation:

- **Architecture/component diagram** for services, components, stores, and dependencies.
- **Flowchart** for decisions and sequential processes.
- **Sequence diagram** for ordered interactions among actors or services over time.
- **Data-flow diagram** for source-to-destination movement and transformations.
- **Timeline or journey map** for stages, events, itineraries, or user journeys.

If more than one view is useful, explain why and keep each view focused. Do not force a software architecture diagram onto non-technical content.

## 3. Define a clear model before styling

Write a compact diagram specification with:

1. A descriptive title and the question the diagram answers.
2. Nodes with stable IDs, readable labels, and a concise role.
3. Directed edges with meaningful relationship labels.
4. Explicit boundaries or groupings where supported by evidence.
5. A legend for any non-obvious notation.
6. Known unknowns and assumptions, separated from verified facts.

For a codebase, associate each implementation claim with file paths and, where possible, line ranges or immutable commit references. Cite actual excerpts when available. If source evidence cannot be obtained, say so and ask for files or access rather than fabricating a map.

## 4. Design interactions only when they aid understanding

Useful interaction patterns may include:

- Click a node to open a concise detail panel.
- Highlight a route or sequence selected by the user.
- Focus upstream or downstream relationships that are explicitly modeled.
- Filter or group by an evidence-backed category.
- Switch between light and dark themes.
- Provide an accessible textual summary so the content is not available only visually.

An interaction must reflect the authored diagram model. Do not describe a highlighted path as actual runtime traffic or causal impact unless supported by telemetry or source evidence. Keep interactions keyboard-accessible and label controls clearly when implementing the HTML in an available coding environment.

## 5. Explain complex subjects as a page

For explainer pages, use this order:

1. Conclusion or answer.
2. Key evidence and its source.
3. One panel per sub-question or step.
4. A diagram section that visually reinforces the adjacent explanation.
5. Caveats, assumptions, and follow-up investigations.

Put citations next to claims, not in an unconnected bibliography. For repository evidence, cite an immutable commit when possible and make source paths easy to inspect. Do not fabricate numbered references or represent uncited statements as sourced.

## 6. Produce the requested deliverable honestly

Return the deliverable requested by the user:

- A diagram specification if no rendering/runtime is available.
- Mermaid or another supported text diagram when that is sufficient.
- HTML/CSS/JavaScript only when the environment supports file creation or code delivery and the user asked for an artifact.
- A source-grounded codebase map only after inspecting relevant source files.

If the user explicitly expects Archify's complete interactive renderer, explain that this plugin is guidance-only and direct them to the upstream repository and official site. Do not claim that an HTML diagram has been generated, tested, or deployed unless the corresponding artifact was actually created and checked.

## 7. Revision checklist

Before finishing, confirm:

- Nodes and edges answer the user's stated question.
- Every implementation-specific claim has evidence or is visibly marked as an assumption.
- Labels are concise and consistent; directionality is unambiguous.
- Interactions are useful, accessible, and faithful to the model.
- The diagram has a text explanation and its limitations are clear.
- No repository writes, commits, pull requests, or deployments were performed unless explicitly requested.

## Upstream project

- Repository: https://github.com/tt-a1i/archify
- Official site: https://archify.si
- Upstream describes outputs including interactive HTML diagrams and explainer pages. Its renderer and installation/runtime tooling are not included in this plugin package.
