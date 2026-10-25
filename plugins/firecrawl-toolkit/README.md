# Firecrawl Toolkit (private, unofficial)

A focused ChatGPT/Codex plugin package built from a read-only review of the public Firecrawl repository and its current README and contributor instructions.

## Source reviewed

- Repository: https://github.com/firecrawl/firecrawl
- Inspected `main` commit: `13673be17227b3af0131e7f9c96b5a05152a34bd` (committer timestamp: 2026-10-24T18:24:56Z)
- Core reference files: `README.md`, `AGENTS.md`, and `apps/api/openapi-v0.json` / `apps/api/openapi.json` paths from the repository tree.
- Current source snapshot link: https://github.com/firecrawl/firecrawl/tree/13673be17227b3af0131e7f9c96b5a05152a34bd

## Architecture

This is a private hybrid workflow package. It binds optionally to the already registered Firecrawl app by its verified plugin ID and ships Skills that orchestrate its available tools. The app binding is optional so that general workflow guidance remains useful when the app is unavailable; Skills must never pretend that missing tools ran.

## Included workflows

- Setup and authentication hygiene.
- Search, scrape, map, bounded crawl and source-grounded synthesis.
- Agent-driven research and schema-shaped extraction.
- Browser interaction with explicit action boundaries and verification.
- Document parsing, website monitoring and account-credit awareness.
- Firecrawl repository contribution guidance based on upstream `AGENTS.md`.
- Portable workspace-operation and Python-verification policies.

## Deliberate exclusions

No Firecrawl API/server implementation, workers, deployment workflows, environment files, keys, user data, tests requiring service credentials, or internal-only operational functions are copied into the plugin. The repository tree included an `apps/api/.env.local` path; it was not read or packaged. Treat environment files as sensitive and audit their history separately when contributing to the upstream repo.

## Limitations and status

- This package is an independent private companion, not an official Firecrawl product or an upstream Firecrawl release.
- The package does not host or deploy Firecrawl's service.
- Live web operations depend on the connected Firecrawl app and account. They can consume Firecrawl credits and may fail when the app/account is unavailable or out of credits.
- External app connectivity is not proven by static package validation; test it after installation.
- Public-directory readiness is not claimed: the package includes a private registered-app binding and a generic private listing identity. Do not upload this exact private package to the public directory.

## Verification plan

1. Validate JSON and skill frontmatter.
2. Check referenced app ID, skill paths, SVG dimensions and path safety.
3. Build two deterministic ZIPs and compare SHA-256.
4. Inspect archive entries and validate a clean extraction.
5. Save to the authenticated private plugin account and, after installation, smoke-test app tool invocation and missing-app fallback.
