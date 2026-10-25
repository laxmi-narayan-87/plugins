---
name: model-development
description: "Use when designing, training, validating, comparing, or debugging machine-learning models and the datasets/features they depend on."
---

# ML Model Development Workflow

Use this workflow for classical ML, tabular ML, time series, NLP, or computer vision. Be explicit about assumptions; do not fabricate dataset properties or results. Ask only for missing details that materially change the plan; otherwise start with a clearly stated baseline.

## 1. Frame the task
- Identify decision/use case, prediction unit, target, prediction horizon, inference constraints, failure costs, and success metric.
- Classify task: regression, classification, ranking, clustering, anomaly detection, forecasting, retrieval, or representation learning.
- Establish a simple baseline and a leakage-safe evaluation protocol before model complexity grows.
- For imbalanced classification, report precision/recall, F1 and PR-AUC as appropriate; do not rely on accuracy alone. For regression consider MAE/RMSE/R² and error slices; ranking use NDCG/MAP/MRR when suitable.

## 2. Inspect and prepare data
- Inspect schema, row counts, unique IDs, target distribution, missingness, duplicates, outliers, units, timestamps, groups, label quality, and train/serve availability.
- Check target leakage and post-outcome features. Split before fitting transformations; fit imputers, scalers, encoders, feature selection, and resampling only on training folds.
- Select a random, stratified, group, or time-based split that matches deployment. Keep an untouched final test set; avoid random splits for temporal or correlated entities.
- Document each transformation and preserve a reproducible data version/hash and split seed.

## 3. Build a baseline
- Prefer simple and interpretable baselines before advanced models: dummy predictor, linear/logistic model, tree, or domain heuristic.
- Use scikit-learn Pipelines/ColumnTransformer where possible so preprocessing is fitted inside cross-validation.
- Choose methods based on data scale, modality, latency, interpretability, resource constraints, and maintenance burden—not fashionable defaults.
- For tabular data consider regularized linear models and tree ensembles (Random Forest, XGBoost, LightGBM, CatBoost where available); text/image/deep learning choices should be justified by data volume and task.

## 4. Train and tune
- Establish fixed seeds where appropriate, log package/runtime versions, dataset version, code commit, config, metrics, and artifact location.
- Tune in stages: broad random search, then Bayesian/Optuna-like optimization if warranted. Reserve a budget and use early stopping only with a valid validation set.
- Use cross-validation on training data; keep the final test set out of model selection. Avoid repeatedly tuning against test results.
- Handle imbalance through class weights, carefully scoped resampling, and threshold selection; put resampling inside training folds to avoid leakage.
- Compare against baseline, report variation across folds/seeds when material, and inspect feature importance only with awareness of its limitations.

## 5. Evaluate and diagnose
- Report chosen metric, baseline, validation protocol, data split, confidence/variation where available, and relevant constraints.
- Inspect confusion matrix, calibration, threshold trade-offs, residual plots, subgroup/slice performance, and representative false positives/negatives.
- Check overfitting, data leakage, distribution mismatch, unstable metrics, and sensitivity to seeds. Never claim metrics unless measured by actual execution or provided evidence.
- If models are close, prefer the simpler, more interpretable, cheaper option unless the measured benefit justifies added operational complexity.

## 6. Package and hand off
- Save model and preprocessing pipeline together; include schema, expected feature types, training data/version reference, metric summary, dependency lock or requirements, and reproducible training command.
- Add prediction-time input validation, explicit missing/unknown-category handling, and safe behavior for malformed or out-of-range inputs.
- Include tests for preprocessing consistency, schema compatibility, deterministic smoke inference, and known edge cases.
- For deployment, define latency/throughput/memory needs and a rollback plan; seek explicit approval before changing production systems.

## Deliverable format
Return: assumptions; task/metric; split/leakage plan; baseline; candidate models; training and tuning plan; measured results (or clearly marked expected results); error analysis; artifact/test checklist; next actions. If code is requested, produce runnable, minimally complete code and mention any unverified dependencies.
