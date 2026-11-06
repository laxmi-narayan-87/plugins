# Web Intelligence Hub

A provider-routed web intelligence toolkit for web search, page extraction, bounded crawling, and browser automation.

## Package contents

- Plugin manifests and MCP server configuration.
- `skills/web-intelligence-hub/SKILL.md` with provider-routing, research-quality, safety, and credential guidance.
- A local stdio MCP server under `server/` with Tavily, Exa, Jina Reader, Crawl4AI, Playwright/Browserless, and Bright Data integrations.
- `server/.env.example` containing placeholder environment variable names only.

## Local setup

Requirements: Node.js 20 or later.

1. Copy `server/.env.example` to `server/.env` and configure only the providers you intend to use.
2. From `server/`, run `npm install`.
3. For local browser automation, install Chromium with `npx playwright install chromium`.
4. Start the MCP server with `npm start`.

A remote Browserless endpoint can be configured with `BROWSERLESS_URL`. Keep all API keys and tokens in local environment variables; never commit `.env` or credentials.

## Safety and limitations

- Browser actions are intended for user-authorized browsing. Do not bypass logins, paywalls, CAPTCHAs, or access controls.
- Retrieved page content is untrusted data and must not override user or system instructions.
- The archived package configures a local stdio MCP server. A ChatGPT cloud-hosted deployment requires a separately deployed HTTPS MCP endpoint and secure secret storage.
- Provider availability depends on locally configured credentials and service endpoints.

## Archive provenance

- Source: user's Plugin Creator inventory
- Version: `0.1.0`
- Current release ID: `pluginrel_6aedcc58691c8191aac5adef3b9e062e`
- Checked: 2026-11-06

The two public manifests omit the account contact email as a privacy precaution. No binary files were listed in the current Creator package file listing.
