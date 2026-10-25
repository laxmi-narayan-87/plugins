---
name: crawl-and-extract
description: Use when the user needs bounded website crawling, URL discovery, clean text extraction, schema-based records, PDFs or crawl output saved for downstream analysis.
---
# Crawl and extract website data

## Select the engine
- Prefer Crawl4AI for Python-first, self-hosted crawling and LLM-ready Markdown, CSS/XPath/LLM extraction, screenshots, caching and deep-crawl strategies.
- Prefer Crawlee for Node.js/TypeScript crawling jobs needing persistent queues, retries, storage and session/proxy management.
- Use a connected search/extraction API only when the host actually exposes it and the requested workflow warrants hosted processing.
- Use ordinary HTTP requests only for simple accessible pages; switch to a browser-backed crawler when JavaScript renders the relevant content.

## Workflow
1. Confirm seed URL(s), allowed domains, URL/path filters, maximum pages/depth, output format and whether to include PDFs or assets.
2. Inspect sitemap/robots signals and domain scope. Respect access rules and site policies. Do not bypass authentication, CAPTCHAs, paywalls or anti-abuse controls.
3. Map/discover URLs first, then crawl only the approved scope. Track requested, visited, skipped, failed and duplicate URLs.
4. Extract raw HTML, visible text/Markdown, title, meta description, canonical, headings, links, status, timestamps and optional schema fields as needed.
5. For structured records, define a schema, capture source URL and extraction method, distinguish absent values from inferred values, and validate types and required fields.
6. Save raw outputs and normalized records separately when the host/runtime supports file writes. Record crawler/version/configuration, date, URL rules and page limit.
7. Report crawl coverage and gaps. Never claim complete site coverage from a bounded run or a sitemap alone.

## Local setup examples
Crawl4AI (Python): `pip install -U crawl4ai` then `crawl4ai-setup`; run `crawl4ai-doctor` to verify.
Crawlee (Node): use the official docs and project package manager; review setup and storage configuration before running a large crawl.
Always verify current upstream commands before execution. Do not assume these runtimes are installed or network access is available.
