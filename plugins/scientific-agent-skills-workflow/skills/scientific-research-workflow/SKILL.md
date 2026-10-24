---
name: scientific-research-workflow
description: Use when planning or carrying out scientific research, literature synthesis, data analysis, computational experiments, reproducibility checks, or scientific writing.
---

# Scientific research workflow

Use this workflow to structure research tasks carefully. This skill is process guidance; it does not itself execute external scientific databases, install domain libraries, or validate a result experimentally.

## 1. Define the research question

- Restate the scientific question, intended decision or output, domain, population/material/system, and relevant constraints.
- Separate the primary question from exploratory questions.
- Identify what evidence would support, weaken, or falsify the working hypothesis.
- Ask for missing information only when it materially affects the design; otherwise list assumptions explicitly.

## 2. Plan evidence gathering

- Prefer primary research, authoritative repositories, standards, dataset documentation, and methods papers appropriate to the question.
- Track each source's title, authors, date/version, DOI or stable URL, study type, key result, limitations, and the specific claim it supports.
- Distinguish source-reported facts from interpretation, hypothesis, and unverified inference.
- Check whether sources are current enough for the question and whether independent sources agree.
- Never fabricate citations, dataset records, identifiers, quotations, results, or access to a database. State when browsing or database access was unavailable.

## 3. Design the method before analysis

- Specify data provenance, inclusion/exclusion criteria, variables, units, preprocessing, quality checks, outcome measures, statistical methods, and known confounders.
- Identify sample-size limitations, missingness, measurement error, batch effects, leakage risks, multiple-comparison issues, and likely sources of bias where relevant.
- Prefer a method appropriate to the data-generating process rather than selecting a method solely because it is convenient.
- Predefine key evaluations when feasible; label post-hoc analyses as exploratory.

## 4. Analyze transparently

- Inspect schema, dimensions, units, missing values, duplicates, outliers, and validity constraints before modeling.
- Preserve raw data; make transformations reproducible and document every exclusion or correction.
- Use suitable baselines and diagnostics. Report effect sizes and uncertainty, not only a p-value or a single performance metric.
- For machine learning, keep evaluation data separate from training and model selection, use leakage-resistant validation, and compare against meaningful baselines.
- Run calculations or code only when the required tools and data are actually available. Do not claim a computation, experiment, or test was run unless it was.

## 5. Validate and reproduce

- Recheck units, assumptions, formulas, joins, sample counts, random seeds, software/package versions, and data splits.
- Use independent checks where possible: alternate implementations, sensitivity analyses, negative controls, external validation, or comparison with published values.
- Record the environment, commands, configuration, input versions, outputs, and failures sufficiently for another researcher to reproduce the work.
- Separate successful checks from checks not run, blocked, or inconclusive.

## 6. Communicate findings

Structure a report as: question; background; data and provenance; methods; results; uncertainty; limitations; conclusion; reproducibility notes; references.

- Match the strength of the conclusion to the evidence. Correlation is not automatically causation, and in-sample performance is not proof of generalization.
- Include units, denominators, uncertainty intervals, and relevant negative or null findings.
- Make clear which claims are established by sources, calculated from supplied data, inferred, or still unknown.
- Avoid overstating novelty, statistical significance, clinical usefulness, or practical readiness.

## 7. Domain-specific safeguards

- For medical or clinical topics, provide research-oriented evidence synthesis, not patient-specific diagnosis, treatment instructions, or a replacement for a qualified clinician.
- For animal studies, follow approved protocols, welfare requirements, and domain oversight; computational recommendations must not be presented as autonomous humane-endpoint decisions.
- For laboratory automation, hazardous materials, chemical synthesis, biological protocols, and equipment control, follow applicable safety procedures, institutional approvals, and manufacturer documentation. Do not infer a safe operating procedure from incomplete context.
- Respect licenses, privacy, consent, and data-use restrictions when handling datasets or source materials.

## 8. Use the upstream skill catalog when a specialized procedure is needed

The upstream project contains domain-specific skill files and references. Browse its catalog to select the matching skill and follow that skill's own setup and safety requirements:

- Repository: https://github.com/K-Dense-AI/scientific-agent-skills
- Skill catalog: https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/docs/skills.md
- Project overview and setup: https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/README.md

Do not imply that this compact workflow package includes all upstream skills, code, or database connectors. If the user asks for a specific domain workflow, identify the required upstream skill and tools explicitly before proceeding.
