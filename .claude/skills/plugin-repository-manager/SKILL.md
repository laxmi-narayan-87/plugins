---
name: plugin-repository-manager
description: Maintain an existing plugin or Agent Skill catalog repository: add or update entries, synchronize catalog metadata, create per-plugin documentation, and preserve repository conventions. Use when asked to extend, organize, or maintain a plugin repository.
---

# Plugin Repository Manager

## Workflow
1. Inspect the repository before editing: default branch, root structure, catalog/index files, plugin directories, conventions, recent commits, and current working state.
2. Translate the request into a bounded change list. Identify every affected plugin, index, manifest, README, asset, and source reference.
3. For each new or updated plugin, verify the original source and record its canonical URL. Do not infer attribution.
4. Follow existing naming, layout, metadata, and formatting conventions. Keep assets intact; don't edit unrelated files.
5. Every plugin directory must have a README with: **Name**, **Use case**, **Core functionality**, and **Original source** (a direct URL).
6. Update all relevant indexes/catalog listings so the plugin is discoverable. Check for duplicates and stale entries.
7. Implement all requested changes, not merely the first obvious fix. Keep the diff minimal and focused.
8. Validate: directory/index consistency, required README fields, source URLs, links, asset references, syntax/format, and relevant tests.
9. Report changed paths, validation commands and actual outcomes, unresolved issues, and commit/deployment state separately. Never claim an action succeeded without evidence.

## Rules
- Work on `main` only when the user has authorized it; create a PR only when explicitly requested.
- Preserve existing assets and unrelated files.
- Ask before destructive changes, publishing, sending, external deployment, or irreversible operations.
- Never invent plugins, sources, tests, or results.
- Keep documentation concise, natural, technically precise, and audience-appropriate.

## Examples

**Good:** “Inspect `plugins/` and catalog first; add the requested plugin with its verified upstream URL, README, and catalog entry; validate all changed paths and links; report exact results.”

**Good:** “The request adds 3 plugins. Check all 3 directories, required README sections, duplicate names, and catalog counts before committing.”

**Bad:** “I added the plugin and everything works.” Why bad: no repository inspection, source verification, concrete change list, or test evidence.

## Completion checklist
- [ ] Existing structure and conventions inspected
- [ ] All requested entries implemented
- [ ] Per-plugin README complete and source-linked
- [ ] Catalog/index synchronized
- [ ] Assets and unrelated files preserved
- [ ] Validation completed and honestly reported
- [ ] Approval gates respected
