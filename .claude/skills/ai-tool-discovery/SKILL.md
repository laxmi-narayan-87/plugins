---
name: ai-tool-discovery
description: Discover, verify, compare, and catalog AI tools, plugins, frameworks, GitHub repositories, or Agent Skills from user-provided links, posts, or research requests. Use when collecting or evaluating AI resources.
---

# AI Tool Discovery

## Workflow
1. Capture the user's exact seed: link, post, repository, list, or topic. Preserve every explicitly named item.
2. Extract candidates and canonical source URLs. Resolve redirects and prefer the author's official repository/docs over reposts.
3. Verify each candidate's purpose, capabilities, maintenance signals, license/availability when relevant, and requirements using primary sources. Clearly label anything unverified.
4. Deduplicate by canonical project, not just display name. Note forks or alternatives only when meaningfully distinct.
5. Organize results in a useful compact table: name, what it does, best use, source, and caveat/status.
6. Distinguish facts, evaluation, and recommendations. Explain why a resource is relevant; avoid hype and unsupported “best” claims.
7. If asked to add resources to a repository, hand off implementation to the repository manager skill; do not independently invent its schema.
8. Provide a concise next action or prioritized shortlist. Preserve source references for later reuse.

## Rules
- No fabricated projects, features, stars, benchmarks, licenses, or maintenance status.
- Prefer original sources and link each item directly.
- Don't include duplicates or merely adjacent resources to inflate a list.
- Adapt tone: professional research, engaging social copy, or technical notes according to audience.
- If information is time-sensitive, verify it at the time of research.

## Examples

**Good:** “These 8 projects were named in the post. I verified 6 official repositories; 2 have no primary source link. Here is a deduplicated table and what each enables.”

**Good:** “Compare 3 UI skill libraries by supported framework, interaction patterns, license, setup cost, and upstream maintenance; cite official docs.”

**Bad:** “Here are 30 trending AI tools” with copied descriptions and no canonical sources. Why bad: noisy, unverified, duplicated, and not actionable.

##Completion checklist
- [ ] All named candidates captured
- [ ] Canonical sources verified
- [ ] Duplicates removed
- [ ] Key claims grounded in primary references
- [ ] Caveats and unknowns stated
- [ ] Actionable summary delivered
