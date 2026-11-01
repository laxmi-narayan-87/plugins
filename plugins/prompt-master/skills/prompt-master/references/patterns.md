# Credit-Killing Patterns Reference

Adapted from the original Prompt Master project. Use these diagnostics selectively; do not mechanically apply all 37 to every prompt.

## Task patterns

| # | Pattern | Repair |
|---|---|---|
| 1 | Vague task verb | Replace “help me” with a precise operation and object. |
| 2 | Unrelated tasks combined | Split distinct outcomes or review checkpoints. |
| 3 | No success criteria | Define observable acceptance criteria. |
| 4 | Over-permissive agent | Specify allowed and forbidden actions. |
| 5 | Emotional description | Convert frustration into reproducible symptoms and evidence. |
| 6 | Whole-project request | Decompose into bounded phases. |
| 7 | Implicit reference | Restate the task instead of “that thing we discussed.” |

## Context patterns

| # | Pattern | Repair |
|---|---|---|
| 8 | Assumed prior knowledge | Include relevant project and conversation context. |
| 9 | No project context | Add only the background that changes the answer. |
| 10 | Forgotten stack | Preserve established technology choices. |
| 11 | Hallucination invitation | Require verifiable claims and explicit uncertainty. |
| 12 | Undefined audience | Identify reader expertise and expectations. |
| 13 | Missing failed attempts | Include what was tried and the observed result. |

## Format patterns

| # | Pattern | Repair |
|---|---|---|
| 14 | Missing output format | Specify structure, length, and file type as needed. |
| 15 | Implicit length | Set a useful length boundary when it affects quality. |
| 16 | Missing domain perspective | Add a role only when it improves the output. |
| 17 | Vague aesthetic adjectives | Translate adjectives into measurable design attributes. |
| 18 | Missing visual exclusions | State material negatives such as text, blur, or watermark when relevant. |
| 19 | Wrong syntax for image AI | Use the target tool's verified syntax. |

## Scope patterns

| # | Pattern | Repair |
|---|---|---|
| 20 | No scope boundary | Name files, functions, directories, or deliverable limits. |
| 21 | No stack constraints | Include required versions and compatibility limits. |
| 22 | No agent stop condition | Define when to pause for human review. |
| 23 | No file path for IDE AI | Include known exact file and symbol paths. |
| 24 | Wrong template for tool | Adapt to the target tool's workflow. |
| 25 | Excessive codebase context | Supply relevant files/symbols, not an entire repository dump. |

## Reasoning patterns

| # | Pattern | Repair |
|---|---|---|
| 26 | No audit contract | Ask for assumptions, criteria, evidence, checks, and uncertainty. |
| 27 | Requesting hidden reasoning | Ask for concise rationale and verification instead. |
| 28 | Expecting persistent session memory | Re-state needed context in the prompt. |
| 29 | Contradicting prior work | Carry forward and reconcile established decisions. |
| 30 | No grounding rule | Require citations or evidence and label uncertainty. |

## Agentic patterns

| # | Pattern | Repair |
|---|---|---|
| 31 | No starting state | Describe current files, dependencies, and behavior. |
| 32 | No target state | Define the desired observable end state. |
| 33 | Silent agent | Request milestone/blocker reporting for substantial tasks. |
| 34 | Unlocked filesystem | Set edit boundaries and protected paths. |
| 35 | No human-review trigger | Require approval before destructive or consequential actions. |
| 36 | Vague initial agent task | Front-load goal, context, scope, action boundaries, and acceptance criteria. |
| 37 | Context rot | Refresh or compact decisions, constraints, failures, and target state. |
