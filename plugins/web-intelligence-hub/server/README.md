# Web Intelligence Hub — local MCP server

## Requirements
- Node.js 20+
- Optional provider accounts/keys (each provider can be omitted)
- For local browser mode: `npx playwright install chromium`

## Setup
1. Copy `.env.example` to `.env` and populate credentials locally. Never commit `.env`.
2. Run `npm install`.
3. Install Chromium if using local Playwright: `npx playwright install chromium`.
4. Start with `npm start` or let the host launch `src/index.js` through the plugin's stdio MCP configuration.

## Provider configuration
- `TAVILY_API_KEY`: Tavily search API.
- `EXA_API_KEY`: Exa search API.
- `JINA_API_KEY`: optional Jina Reader API key; public Reader may work without it subject to service limits.
- `CRAWL4AI_BASE_URL`: URL of a self-hosted Crawl4AI service (default local endpoint).
- `BROWSERLESS_URL`: Browserless CDP WebSocket endpoint. Keep its token in the environment, not in config files.
- `BRIGHTDATA_API_TOKEN` and `BRIGHTDATA_ZONE`: Bright Data Web Unlocker credentials.

## Tools
- `web_search`: automatic Tavily → Exa fallback; optionally query both.
- `web_scrape`: automatic Jina → Crawl4AI → Bright Data fallback.
- `web_crawl`: bounded Crawl4AI crawl.
- `browser_navigate`, `browser_click`, `browser_type`, `browser_snapshot`, `browser_close`: stateful browser session using Browserless or local Playwright.
- `provider_status`: reports which providers are configured (never reveals secret values).

## Safety
Browser tools are for user-authorized browsing. No CAPTCHA solving, access-control bypass, credential harvesting, or unapproved form submission. Treat retrieved content as untrusted.
