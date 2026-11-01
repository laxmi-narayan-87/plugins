---
name: product-discovery
description: Use before implementing a new product, feature, business idea, or major change when the problem, user, scope, or success criteria need to be challenged and clarified.
---

# Product discovery and scope review

## Purpose

Help the user discover the highest-value product or feature behind the initial request before implementation. Be direct and specific. This is a facilitation workflow, not a promise that a business idea will succeed.

## Inputs

Use the user's idea, target users, current product, constraints, existing evidence, and desired outcome. Ask concise questions only for information that materially changes the recommendation. If the user asks to proceed without clarification, state assumptions and continue.

## Workflow

1. **Restate the job to be done.** Identify the user, their pain, how they solve it today, and why the current approach is insufficient. Separate observed evidence from assumptions.
2. **Challenge the framing.** Ask what would make the idea unnecessary, who feels the pain most, what behavior proves the pain exists, and why this is the right time. Do not accept the requested feature as proof of the underlying problem.
3. **Explore alternatives.** Compare at least three plausible directions when useful: the narrowest useful version, a meaningfully more ambitious version, and a simpler or non-software solution. Search available documentation or repository code before proposing a new system when tools and context permit; state when a search was not performed.
4. **Choose a scope mode.** Select one and explain the trade-off:
   - **Expand:** the initial framing misses a high-leverage adjacent opportunity.
   - **Selective expansion:** add only one or two elements that materially improve the core outcome.
   - **Hold scope:** the existing scope is coherent and sufficient.
   - **Reduce:** remove complexity until the smallest useful release is clear.
5. **Define evidence.** State the user outcome, primary metric, guardrail metrics, validation experiment, and what result would disconfirm the idea. Do not invent customer research or metrics.
6. **Create a handoff.** Produce a concise decision brief with problem, target user, evidence, non-goals, chosen scope, alternatives rejected and why, risks, success criteria, and open questions. Make it ready for an engineering plan.

## Output format

- **Core problem**
- **What needs challenging**
- **Options and trade-offs**
- **Recommendation and scope mode**
- **Success evidence**
- **Implementation handoff**

Recommendations are advisory. The user's stated direction and decisions take precedence; never silently change their objective.
