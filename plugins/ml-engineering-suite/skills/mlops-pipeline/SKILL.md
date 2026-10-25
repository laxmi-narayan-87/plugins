---
name: mlops-pipeline
description: "Use when creating or improving repeatable machine-learning pipelines, CI/CD for models, orchestration DAGs, model registry workflows, deployment gates, or production monitoring."
---

# Production MLOps Pipeline Workflow

Design an end-to-end pipeline without assuming a specific cloud or orchestrator. Confirm constraints when required, or state assumptions and offer a tool-agnostic plan. Keep training and serving environments separated unless a clear reason argues otherwise.

## 1. Map stages and contracts
Model the workflow as explicit stages with declared inputs, outputs, dependencies, resource limits, and failure semantics:
1. ingest/version data;
2. validate schema, quality, and freshness;
3. transform features with versioned code;
4. split data using the task-appropriate strategy;
5. train and record parameters/artifacts;
6. evaluate against baseline and release thresholds;
7. register candidate with lineage and metadata;
8. deploy to a limited or shadow environment;
9. verify health and performance;
10. promote or roll back; monitor drift and retraining triggers.

Use a DAG orchestrator such as Airflow, Dagster, Prefect, or Kubeflow only when orchestration needs justify it. Do not add infrastructure solely for fashion.

## 2. Reproducibility and data quality
- Version code, data snapshots or hashes, feature definitions, config, dependencies, model artifacts, and evaluation outputs.
- Validate schemas, null/duplicate rates, ranges, class distributions, time freshness, and business invariants before expensive training.
- Make stages idempotent where possible. Use stable run IDs and immutable artifact paths; define retries and dead-letter/manual intervention behavior.
- Prevent target leakage and apply transforms using training-only fit data. Validate that training/serving features use consistent contracts.
- Do not store credentials in source, logs, notebook outputs, or artifacts. Use environment-backed secret management and least privilege.

## 3. Training and evaluation gate
- Track hyperparameters, seed, data/code version, environment, metrics, artifacts, and runtime/cost.
- Compare a candidate with the currently deployed baseline and minimum absolute quality thresholds; include slice metrics, safety/business checks, and latency/resource checks where relevant.
- Fail closed when evaluation is missing, data validation fails, or required metrics breach policy. Do not auto-promote based only on training metrics.
- Register only artifacts with their provenance and validation result. Use clear stages/tags such as candidate, staging, and production.

## 4. Deployment strategy
Select a strategy based on risk and serving mode:
- batch: validate input/output schemas, schedule, freshness, and backfill/re-run safety;
- online: versioned endpoint, timeouts, payload limits, latency/throughput targets, observability, and fallback behavior;
- shadow: compare candidate outputs without affecting decisions;
- canary/blue-green: route limited traffic, set promotion/rollback thresholds, and preserve a known-good version.

Never deploy or alter production merely because a plan was drafted. Require explicit user approval for production-changing actions. Include a rollback path and verify it is operational.

## 5. Monitoring and retraining
Monitor service health (availability, errors, p50/p95/p99 latency, throughput, resource use), data quality, input/prediction distribution, delayed ground-truth model quality, and cost. Distinguish data drift from concept drift; drift alone is not proof of quality loss. Define alert thresholds, owner, runbook, and retraining criteria. Revalidate retrained models through the same gates.

## 6. CI/CD and testing
- Unit-test feature logic; contract-test schemas; integration-test pipeline stages; use representative smoke data for training and inference.
- Add tests for leakage, reproducibility, artifact load, backward compatibility, and minimum evaluation thresholds.
- Validate pipeline changes on a staging dataset/environment before production.
- Keep configuration separated by environment and avoid committing secrets or large model/data artifacts.

## Deliverable
Provide architecture/stage diagram in text, stage contracts, tool choices with trade-offs, sample config or orchestration pseudocode, test matrix, observability metrics, promotion gates, recovery/rollback procedure, security concerns, and an incremental rollout plan.
