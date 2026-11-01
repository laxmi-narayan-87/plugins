---
name: source-verification
description: Use when fact-checking claims, tracing citations to original documents, or researching websites, documentation, and GitHub repositories.
---

# Primary Source Verification

Trace claims to first-hand evidence and report what the source actually supports.

## Workflow
1. Extract each factual claim from the draft or research question.
2. Identify the best primary source: official documentation, original paper, government publication, company release, repository, changelog, dataset, or direct statement.
3. Retrieve source content using available browsing, Firecrawl integration if connected, or direct source links. Never imply Firecrawl is connected unless its tools are available.
4. Capture exact URL, title, publisher, date, and relevant passage or section.
5. Label each claim supported, partially supported, unsupported, contradicted, or time-sensitive.
6. Follow citations recursively when useful until reaching the original source.
7. Return a source ledger and rewrite unsupported claims conservatively.

## Output
Table: claim, verdict, primary source, evidence, date, recommended correction. Distinguish primary from secondary sources and note inaccessible pages.

## Guardrails
Never fabricate quotations, page numbers, citations, or dates. A search snippet is a lead, not proof. Do not cite secondary reporting as primary evidence.