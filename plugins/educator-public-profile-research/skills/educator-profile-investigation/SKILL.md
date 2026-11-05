---
name: educator-profile-investigation
description: Use when investigating a named educator, instructor, speaker, or creator and mapping their public professional profiles across websites and platforms with verifiable evidence.
---

# Educator public-profile investigation

## Goal
Build an evidence-backed map of public professional identity. Focus on identity resolution, public teaching/employment history, creator channels, portfolio/course listings, and links voluntarily published by the subject.

## Safety boundary
- Use public pages and public professional information only.
- Do not access private accounts, bypass login or platform controls, enumerate account recovery endpoints, use leaked datasets, or infer hidden private contact data.
- Exact contact identifiers supplied by the user may be searched only to find public pages where the subject has voluntarily published them. Never use personal-email/phone enrichment or reveal tools.
- Keep same-name candidates distinct unless independent evidence links them.
- Distinguish a public contact listing from proof of identity; repeated publication on a verified creator channel is stronger than a name-only match.

## Workflow
1. Parse user-supplied names, variants, public identifiers, URLs, affiliations, and seed media.
2. Discover tools by intent with the Skills Workflow / Firecrawl Alexandria catalogue. Read complete contracts before executing a provider. Never invent capability IDs or input fields. 
3. Start with seed URLs:
   - For YouTube, call video_details for every supplied video URL. Record channel_id, channel_name, channel_url, full public description, published_at, and outbound URLs in descriptions.
   - Resolve channel and call channel_videos to capture channel description, channel handle, upload list, and publicly stated affiliations.
   - Search videos by author name only as discovery; verify with video_details.
4. Search public web for exact phrases that link the distinctive channel/brand to LinkedIn, Instagram, Facebook, Telegram, personal site, course platforms, and employer pages.
5. Use LinkedIn people search as candidate discovery, not proof. Confirm a profile using overlapping employer history, role, teaching specialty, public posts, and links from a channel or profile bio.
6. Use indexed social profile search only when relevant and review its cost/coverage. Indexed results are not complete live feeds; empty results do not prove absence.
7. Scrape/fetch public profile pages only when supported. If a platform blocks direct scraping, use public indexed search snippets and other independent sources; disclose the limitation.
8. Build an evidence table:
   - confirmed: direct or multiple independent cross-platform links;
   - strong candidate: distinctive matching affiliation/role but no direct reciprocal link;
   - possible: name/title only;
   - unrelated/false positive: contradicted by evidence.
9. Record exact URL, source type, observed evidence, publication/observation date when available, confidence, and caveat. Cite every factual claim with source URLs.
10. Summarize teaching/employment history only as stated by the public profile; do not embellish or infer.

## Output
- Identity resolution and confidence.
- Confirmed public profiles with direct links.
- Possible namesake profiles kept separate.
- Professional timeline with attributed sources.
- Public portfolio/course/creator properties.
- Gaps and platform limitations.
- Research actions performed and any unverified claims.
