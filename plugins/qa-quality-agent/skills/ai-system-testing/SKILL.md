---
name: ai-system-testing
description: Use when testing an AI feature, LLM chatbot, RAG system, agent, model-backed workflow, prompt, tool call, or AI-enabled quality automation.
---

# AI System Testing and Evaluation

## Core principle
AI outputs can vary, so test quality with an explicit evaluation contract, curated datasets, repeated trials where needed, and multiple kinds of evidence. Do not treat fluent output, an LLM judge, or one successful example as proof of correctness. Define thresholds and human-review rules before interpreting results.

## 1. Define intended behavior
Document user goals, allowed/forbidden behavior, ground-truth sources, tool permissions, privacy expectations, harm/security constraints, response schema, latency/cost budgets, and fallback behavior. Define severity and launch thresholds. Separate deterministic product assertions from probabilistic semantic evaluation.

## 2. Build test datasets
Use a versioned, diverse dataset with stable case IDs, source/provenance, expected outcomes or scoring rubrics, tags, difficulty, risk class, and privacy classification. Include normal, boundary, ambiguous, multilingual, adversarial, out-of-scope, and regression cases. Avoid train/evaluation leakage when measuring model quality. Protect personal or confidential data; use synthetic/redacted cases where possible.

## 3. Dimensions to measure
- **Task correctness:** exact answers, schema validity, task completion, business-rule compliance.
- **Grounding/faithfulness:** whether factual claims follow from supplied context and whether citations support them.
- **Retrieval (RAG):** retrieval relevance, recall@k/precision@k where labeled, context coverage, chunking, freshness, and access control.
- **Robustness:** paraphrases, spelling/format changes, long context, empty or malformed inputs, multilingual and ambiguous requests, repeated runs, and model/version/prompt drift.
- **Safety and security:** prompt injection, jailbreak resistance, secret/PII leakage, unsafe requests, authorization, untrusted retrieved content, data exfiltration via tools, and refusal quality. Use controlled non-destructive test cases and do not target systems without authorization.
- **Agent and tool use:** correct tool selection, schema-valid arguments, minimum necessary permissions, correct sequencing, recovery from tool errors, bounded loops, task completion, and no unauthorized side effects.
- **Operational quality:** latency distributions (not only averages), token/cost budgets, rate-limit handling, retries, traceability, availability, fallback, and monitoring.
- **User experience:** usefulness, clarity, uncertainty calibration, consistency, response relevance, accessibility, and suitable escalation to a human.

## 4. Evaluation techniques
1. Use deterministic assertions for structured output, exact business rules, permissions, tool schemas, and safety invariants.
2. Use rubric-based human review for ambiguous high-impact outputs; define rater guidance and adjudication.
3. Use an LLM-as-judge only with a documented rubric, blinded/reference comparisons when feasible, calibration against human labels, repeated validation of judge reliability, and explicit treatment of judge uncertainty. Avoid evaluating a model only with itself.
4. Compare model/prompt versions on fixed datasets. Track aggregate and slice-level metrics; a global score must not hide a severe subgroup regression.
5. Run multiple trials for stochastic behavior and report variance/confidence where useful. Preserve raw outputs and configuration.
6. Validate synthetic test generation against known cases and human review; generated test count is not equivalent to coverage.

## 5. RAG-specific checklist
- Does retrieval return relevant, current, permitted documents?
- Are source IDs and citations valid and traceable?
- Does the answer stay within evidence, admit missing evidence, and handle conflicting sources?
- Are irrelevant or malicious retrieved instructions treated as untrusted data?
- Are tenant/user access controls applied before retrieval and before response generation?
- Do chunk boundaries, top-k, reranking, context truncation, and indexing updates change expected behavior safely?
- Measure retrieval and generation separately as well as end-to-end. Include no-answer and low-confidence cases.

## 6. Agent-specific checklist
- Are available tools allowlisted with least privilege?
- Are arguments type-checked, validated, and constrained?
- Are approval gates required for irreversible, external, financial, or high-impact actions?
- Can the agent identify tool errors, retry safely, avoid duplicate side effects, and terminate within budget?
- Does it distinguish instructions from untrusted webpage/file/tool output?
- Do traces explain the sequence of model decisions, tool calls, returned data, and final outcome without leaking secrets?
- Test partial failures, timeouts, permission denial, stale data, tool disagreement, and recovery.

## 7. AI-assisted browser automation guardrails
AI-generated browser steps can target the wrong element, infer success from a visual cue, or self-heal into an unintended interaction. For critical paths, verify locators and postconditions deterministically. Keep screenshots/traces, record model/tool versions, and review each healed locator or changed path. Compare multi-model disagreement as a diagnostic, not a vote that automatically establishes truth. Make model/API cost and secrets handling explicit; use environment-managed credentials and never commit keys.

## 8. Reporting template
Include system/build, model/provider/version, system prompt or prompt hash, retrieval/index version, test dataset version, tool configuration, sampling parameters, run date, trial count, metric definitions, results overall and by slice, regressions, representative sanitized examples, security findings, judge/human agreement, limitations, latency/cost, and release recommendation against pre-agreed thresholds.

## Reference resources
- AI-testing landscape: https://github.com/tugkanboz/awesome-ai-testing
- QA skill catalog: https://github.com/naodeng/awesome-qa-skills
- AI browser regression example: https://github.com/bug0inc/qa-agent
- 52-week learning journey: https://github.com/srvsngh99/genai-testing-journey

These links are references, not claims that the plugin installs or executes those projects. Check each project's current documentation, maintenance, provider support, security practices, and license before adopting a tool or copying code.
