# Personal Plugin Archive

This repository tracks plugin packages created in the connected Plugin Creator registry. It is a **package archive**, not a mirror of every upstream project's complete runtime source code.

## Inventory

The authoritative package list is maintained in the registry. Check the package folders under [plugins/](plugins/) to see which packages have been archived.

## Archive scope

- Packages contain the files exposed by the Plugin Creator package-file interface, which may include manifests, skill instructions, references, scripts, and support assets.
- A package's presence does not imply that it includes the upstream project's entire runtime implementation, dependencies, or history. Upstream repositories remain the source of truth for those.
- Do not commit credentials, API tokens, `.env` files, or other secrets.
- Do not fabricate unavailable binary assets. Restore them from an authoritative package/source distribution or explicitly document that they remain unavailable.
- Verify each package's license and attribution requirements before redistributing it. A file being present here does not by itself establish redistribution rights.

## Quality checks

Run the repository validation workflow on pull requests. Structural checks should cover JSON syntax, `SKILL.md` frontmatter, references to files within each package, and the expected plugin inventory. Passing these checks does not prove runtime behavior; representative plugins must still be tested in their intended environment.

## Completeness reporting

An inventory report should distinguish:
- **Archived**: the original package files available through the registry have been copied.
- **Partially archived**: one or more source files or assets could not be retrieved.
- **Missing**: the package directory is absent.

The report should record the registry inventory date and identify unavailable files rather than silently omitting them.
