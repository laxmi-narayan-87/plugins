---
name: genai-testing-roadmap
description: Use when the user wants to learn AI/LLM testing progressively, turn a 52-week roadmap into a practical plan, track mini-projects, or select the next GenAI QA learning milestone.
---

# GenAI Testing Learning Roadmap

Create a sustainable learning plan centered on implementation and evidence, not course completion alone. Use the phases below as a roadmap inspired by the linked 52-week journey; adapt to the learner's available time and current proficiency. Do not claim that a learner has completed a milestone without their own evidence or confirmation.

## Working cadence
A sample cadence is 5–9 focused hours per week: learn fundamentals, practice with a small exercise, build a mini-project, write tests, document what was learned, and review the result. Reduce scope when time is limited rather than skipping understanding. Each week ends with a repository commit, short README, passing tests or explicit known limitations, and a reflection.

## Phase 0 — Python and test engineering (Weeks 1–8)
1. Python strings and input validation → prompt formatter.
2. Lists/dicts/sets and test-case data → test-data organizer.
3. Functions, control flow, exceptions → response validators.
4. Modules, virtual environments, packaging → reusable test utilities.
5. JSON/JSONL/file handling → dataset loader with schema checks.
6. Logging, retries, timeouts → resilient API client (use mocks initially).
7. pytest basics and assertions → tests for the utility package.
8. Fixtures, parametrization, markers → a reusable data-driven suite.
**Checkpoint:** reproducible Python project, tests, README, sample dataset, and CI if practical.

## Phase 1 — LLM fundamentals (Weeks 9–18)
9. Tokens, sampling, context window → concept notebook and simple simulator.
10. Transformers/attention intuition → position-variation test design.
11. Tokenization/truncation/cost → tokenizer and budget explorer.
12. One provider API and structured outputs → client wrapper tested with mocks.
13. Multi-provider abstraction and normalized errors → common client interface.
14. Prompt engineering and versioning → prompt evaluation harness.
15. Hallucinations and grounding → labeled failure examples.
16. Consistency and nondeterminism → repeated-run comparison tool.
17. Adversarial inputs and injection awareness → safe adversarial regression suite.
18. Chains/workflows → simple pipeline tests.
**Checkpoint:** documented model, prompt, and dataset versions; robust API error handling; repeatable evaluations.

## Phase 2 — Evaluation core (Weeks 19–28)
19. Evaluation philosophy and rubrics → evaluation spec.
20. Classic text metrics and their limitations → metric comparison notebook.
21. Embeddings and semantic similarity → threshold calibration experiment.
22. LLM-as-judge → rubric judge calibrated against human labels.
23. RAG foundations → minimal retrieval-augmented application.
24. Retrieval evaluation → relevance labels and precision/recall@k where appropriate.
25. Generation evaluation → faithfulness/relevance rubric.
26. Hallucination/claim checking → supported/unsupported claim report.
27. Domain-specific metrics → custom metric and calibration notes.
28. Batch/scale execution → evaluation pipeline with versioned output.
**Checkpoint:** metrics are defined, calibrated, sliced by scenario, and not reduced to one opaque score.

## Phase 3 — Frameworks and integration (Weeks 29–38)
29. Evaluate DeepEval concepts and build a small example.
30. Compare standard and agent-oriented metric choices.
31. Implement or adapt a custom metric; inspect red-team test workflows.
32. Connect evaluation to CI with explicit thresholds.
33. Explore RAGAS-style RAG evaluation.
34. Add reproducible synthetic test generation with human review.
35. Explore Promptfoo-style prompt regression and adversarial tests.
36. Expand controlled red-team scenarios and reporting.
37. Benchmark tools using the same dataset, tasks, metrics, setup effort, and cost.
38. Contribute a docs fix, test, issue reproduction, or small PR to an appropriate open-source project.
**Checkpoint:** tool choice is justified by a small benchmark rather than popularity alone. Verify current versions and licenses first.

## Phase 4 — Agents and production (Weeks 39–46)
39. Agent architectures and bounded planning → design notes and simple simulator.
40. Function/tool-use testing → schema and authorization tests.
41. Agent task evaluation → completion, trajectory, and tool correctness metrics.
42. Multi-agent interactions → controlled failure and handoff tests.
43. Observability/tracing → sanitized trace viewer or dashboard.
44. Prompt/model/retrieval drift → version-to-version regression checks.
45. Performance, latency, token use, and cost → budget benchmark.
46. Human evaluation operations → annotation rubric, reviewer workflow, adjudication.
**Checkpoint:** a reproducible evaluation pipeline with traces, failure triage, safety checks, and explicit budgets.

## Phase 5 — Capstone (Weeks 47–52)
47. Architecture and scope → design document and interfaces.
48. Evaluation runner → datasets, provider adapters/mocks, configuration.
49. Built-in metrics → at least 10 clearly defined metrics if achievable, each unit-tested and calibrated.
50. CLI and reporting → machine-readable and human-friendly reports.
51. CI, documentation, examples, safe configuration, and package checks.
52. Release readiness → final tests, license review, versioning, changelog, package publication only when credentials and release conditions are ready.
**Checkpoint:** a portfolio-worthy project that states limitations, includes tests/docs, avoids embedded secrets, and can be reproduced by another developer.

## Optional specializations
- **AI security/red teaming:** prompt injection, jailbreaks, data leakage, tool abuse, authorization, OWASP guidance, safe test harnesses.
- **ML foundations:** probability, loss/optimization, transformer internals, and metrics implemented from scratch.
- **AI quality architecture:** evaluation strategy, human review operations, governance, observability, and release gates.

## Weekly plan template
For each week return:
1. Goal and why a QA engineer needs it.
2. Prerequisites and a small set of current official resources.
3. Three to five learning tasks.
4. Mini-project with acceptance criteria.
5. Test cases and edge cases for the mini-project.
6. Definition of done and visible evidence (commit, tests, README, sample report).
7. Time budget and a smaller fallback scope.
8. Reflection prompts and next week's dependency.

## Progress tracking
Track each milestone as `NOT STARTED`, `IN PROGRESS`, `DONE`, or `BLOCKED`; link evidence where possible. Do not convert reading time into implementation completion. Review the previous milestone before advancing, and allow the schedule to stretch rather than treating dates as a performance metric.

## Reference
The initial roadmap is inspired by the openly published project at https://github.com/srvsngh99/genai-testing-journey (MIT license identified in its repository) and is combined with an original QA workflow and testing topics. Refer to the source for the authors' detailed weekly materials and current progress; this plugin does not mirror its full code or claim that all listed technologies remain current.
