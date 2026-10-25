---
name: site-audit
description: Use when the user wants a website audit covering links, redirects, SEO metadata, content coverage, accessibility signals, performance symptoms, or functional defects.
---
# Evidence-based site audit

## Scope and reproducibility
1. Define domains, routes, crawl budget, blocked paths, browser types, viewport sizes and whether authenticated pages are in scope.
2. Build a URL inventory from seed links and sitemaps, then deduplicate canonical URLs and remove out-of-scope URLs.
3. Check status codes, redirects, broken internal links, image/script/style failures, canonical/title/description, heading order, language, robots/noindex signals and structured-data validity where applicable.
4. Browser-test important user journeys and inspect console errors/network failures; static crawling cannot prove interactive functionality.
5. Capture accessibility signals such as accessible names, form labels, landmarks, heading hierarchy, keyboard traversal and contrast where tooling permits. Automated checks do not replace manual accessibility review.
6. Prioritize findings by severity, scope, reproduction reliability, user impact and fix confidence. Attach URL and evidence to each finding.
7. Separate confirmed defects from warnings and hypotheses. Include sampling/coverage limits and list checks not executed.

## Security and permissions
Test only websites the user owns or is authorized to assess. Do not perform intrusive security scans or exploit attempts unless explicitly scoped and permitted. Avoid exporting secrets or personal data.
