---
name: xint-analysis
description: Use when analyzing X posts, engagement interactions, discussion themes, or sentiment from supplied data or accessible public sources.
---

# X Post Analytics

Analyze the available post corpus transparently. Do not assume the xint repository or X API is connected.

## Workflow
1. Define query, date window, keywords, accounts, and intended analysis.
2. Collect posts only through available authorized sources or user-provided exports; state collection method and coverage.
3. Normalize timestamps, remove duplicates, and preserve original post URLs and IDs.
4. Calculate engagement metrics only from retrieved fields. Define each metric and denominator.
5. Identify recurring topics, high-interaction examples, reply themes, and changes over time.
6. Estimate sentiment cautiously, accounting for sarcasm, slang, and ambiguity; include confidence and examples.
7. Report sampling bias, unavailable private data, and platform/API limitations.

## Output
Query scope, dataset size, collection date, metric definitions, top posts with links, theme analysis, sentiment caveats, and content implications.

## Guardrails
Do not invent impressions, reach, demographics, or deleted/private post contents. Do not equate likes with approval. Do not deanonymize users or infer sensitive attributes.