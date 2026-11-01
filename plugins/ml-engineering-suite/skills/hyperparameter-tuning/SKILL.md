---
name: hyperparameter-tuning
description: "Use when setting up grid/random/Bayesian hyperparameter search, cross-validation, early stopping, model comparison, or an optimization budget for ML models."
---

# Hyperparameter Optimization Workflow

## 1. Define the optimization problem
- Specify target metric, optimization direction, hard constraints (latency, memory, model size, fairness/slice metrics), compute budget, deadline, and deployment context.
- Establish a reproducible baseline and a leakage-safe split. Keep the final test set untouched until model and threshold selection are complete.
- Identify parameters that materially affect performance; avoid searching a huge space without a hypothesis.

## 2. Choose the search strategy
- Grid search: small, discrete, low-dimensional spaces where exhaustive coverage is useful.
- Random search: strong starting point for larger spaces or unknown parameter importance.
- Bayesian optimization (e.g. Optuna/Hyperopt/Ray Tune): when trials are expensive and useful feedback can guide later trials.
- Successive halving/Hyperband or early stopping: when partial training results predict final performance reliably.
- Manual/local search: after evidence shows a narrow region worth exploring.
Explain trade-offs and do not assume any package is installed.

## 3. Design a sound validation protocol
- Use k-fold or repeated cross-validation when data supports it; stratify for classification as appropriate. Use group-aware splits for related entities and time-ordered splits for forecasting/temporal leakage risks.
- Place preprocessing, feature selection, imputation, scaling, target encoding, and resampling inside each training fold (for example, a Pipeline) to prevent leakage.
- Use nested cross-validation if unbiased model-selection estimates are required and data/compute budget permits.
- Tune thresholds/calibration on validation data only. Never use final test performance to select parameters, features, model families, or thresholds.
- If the dataset or split is small/noisy, report fold-level spread and caution against ranking candidates by tiny score differences.

## 4. Structure the search space
- Use log scales for scale-sensitive parameters such as learning rate or regularization where appropriate.
- Bound depth/complexity and include regularization to manage overfit.
- Use conditional parameters only when the corresponding model/solver supports them.
- Fix and record seeds when meaningful; record environment, data version/hash, code commit, parameters, fold metrics, elapsed time, and failed trials.
- Start with a modest pilot budget, inspect learning curves and parameter importance cautiously, then expand based on evidence.

## 5. Compare candidates
- Compare candidates on the same folds and metric definition. Include baseline score, mean/median and variation, training time, inference latency, memory/size, and operational complexity.
- Inspect error slices, calibration and threshold trade-offs; optimize business costs where a single generic metric is misleading.
- Prefer the simplest model meeting quality/operational requirements. Treat near-ties as near-ties, not proof of superiority.
- Refit using the approved training data only after selection, save the entire preprocessing/model pipeline, then evaluate once on the untouched test set.

## 6. Deliverable
Provide search space and rationale, split protocol, code/config for the chosen framework, resource budget, early-stopping behavior, experiment-record schema, results table only for observed runs, diagnosis of failed/unstable trials, final validation steps, and a reproducible rerun command. Distinguish planned results from measured results.
