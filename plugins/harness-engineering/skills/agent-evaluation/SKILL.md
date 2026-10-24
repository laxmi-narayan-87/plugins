---
name: agent-evaluation
description: Use when designing repeatable evaluations for agent harnesses or skills, comparing prompt-only and harnessed workflows, assessing traces, or creating quality gates and regression tests.
---

# Agent Harness Evaluation

Evaluate task outcomes and workflow behavior, not persuasive explanations. Establish repeatable tasks and judge results against explicit criteria.

## Build an evaluation set

1. Define the target capability, users, operating environment, and failure costs.
2. Sample representative tasks, including edge cases, ambiguous requirements, failure recovery, long-horizon work, and security boundaries.
3. Write acceptance criteria before running the agent. Keep evaluation data separate from instructions that the agent may edit.
4. Fix the model, tools, repository state, dependencies, permissions, budgets, and evaluation procedure where feasible. Record any deviations.
5. Include baseline runs (existing workflow or prompt-only) and harnessed runs under comparable conditions.

## Score multiple dimensions

- Task success against tests or external acceptance criteria.
- Correctness and regression rate.
- Scope discipline and unauthorized side effects.
- Evidence quality and calibration of completion claims.
- Recovery after errors and ability to resume after interruption.
- Latency, token/tool consumption, and cost where observable.
- Human intervention and reviewer burden.
- Robustness across repeated runs and task subgroups.

Use deterministic graders for objective checks. Use human review or calibrated model-assisted grading for qualitative dimensions, with a rubric, examples, and disagreement checks. Never rely solely on the agent's self-assessment.

## Inspect traces

For representative passes and failures, inspect action ordering, tool inputs and outputs, state transitions, errors, retries, context loss, and whether acceptance evidence actually supports the final claim. Redact secrets and sensitive user data. Preserve reproducibility metadata without logging unnecessary personal information.

## Report results responsibly

Include dataset/task count, attempts per task, environment and model settings, metrics and definitions, baseline, uncertainty or variability, representative failures, and known limitations. Distinguish aggregate scores from critical safety failures; do not let a high average hide an unacceptable failure mode. Do not claim statistically meaningful gains without suitable sample size and analysis.

## Quality-gate design

- Fail closed for mandatory checks that cannot run or return an ambiguous result.
- Make skipped checks visible and explain why they were skipped.
- Keep the gate aligned with the definition of done and the risk of the change.
- Add a regression case when an observed failure can be reproduced.
- Re-run the full relevant pipeline after fixing a failure.

## Expected outputs

Return an evaluation plan, test-case schema, scoring rubric, run matrix, verification commands, results table, trace findings, and prioritized follow-up experiments. Do not manufacture metrics or results when no runs were performed.
