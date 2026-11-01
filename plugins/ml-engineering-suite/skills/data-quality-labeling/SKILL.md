---
name: data-quality-labeling
description: "Use when designing annotation guidelines, auditing training data, sampling examples for labeling, measuring annotator agreement, or preparing versioned ML datasets."
---

# ML Data Quality and Labeling Workflow

## 1. Define labels and intended use
- Write an operational label schema with definitions, inclusion/exclusion rules, examples, counterexamples, edge cases, and an explicit “uncertain/needs review” path.
- Align labels with the intended model decision and real-world population. Identify harmful error types, underrepresented classes, sensitive attributes, and domain-specific ambiguity.
- Choose a labeling unit and sampling plan; distinguish random representative sampling from targeted sampling for rare/error cases.

## 2. Audit the raw dataset
Check schema and types, nulls, duplicate records, invalid values, inconsistent units, broken references, class/target distribution, temporal coverage, source/provenance, possible personal data, and duplicates across train/validation/test. Document defects and remediation rules rather than silently discarding data.

## 3. Design the annotation process
- Pilot the guidelines with a small, diverse sample before scaling. Revise guidelines when annotators repeatedly disagree.
- Use overlapping labels or adjudication samples to estimate agreement. Pick a suitable statistic (raw agreement, Cohen’s kappa, Krippendorff’s alpha, etc.) based on number of annotators and label type; none replaces qualitative review.
- Measure annotator-level and class-level patterns; separate guideline ambiguity, insufficient context, and genuine subjectivity.
- Blind annotators to model predictions during initial ground-truth creation when possible. If model-assisted labeling is used, track provenance and audit for automation bias.
- Establish escalation, adjudication, change log, and quality acceptance thresholds before full production.

## 4. Manage class imbalance and representativeness
- Use stratified or targeted sampling to ensure rare classes and known edge cases receive review; retain a separate representative validation/test distribution for realistic performance estimates.
- Record sampling probabilities or weighting when results will be used to estimate population rates.
- Do not oversample validation/test data without documenting it; never let the same entity, near duplicate, or future information leak across splits.

## 5. Version and govern data
- Store immutable dataset versions or snapshots, source references, label schema version, annotation instructions, annotator/QA metadata where appropriate, code commit, and transformation history.
- Minimize sensitive data and redact or restrict access to what is not needed. Do not write sensitive examples into ordinary logs or public artifacts.
- Define policies for corrections, label changes, removal requests, retention, access controls, and dataset deprecation.
- For synthetic or augmented data, track origin and transformation and verify it does not leak test examples or distort intended deployment distributions.

## 6. Close the loop with model errors
Sample false positives/negatives and uncertain predictions for review, but guard against only labeling model-selected examples and biasing the dataset. Separate active-learning acquisitions from representative evaluation data. Maintain an untouched, leakage-safe test set and record each dataset change's impact on metrics.

## Deliverable
Return label schema draft, data audit checklist, sampling plan, annotation/QA procedure, agreement method with caveats, leakage/split strategy, versioning and privacy controls, and a measurable acceptance checklist. Clearly label estimated counts or quality thresholds as proposals until measured.
