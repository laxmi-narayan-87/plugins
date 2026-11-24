# Gemini / Antigravity Plugins

This directory contains plugins designed and structured for the **Google Gemini / Antigravity** agent platform.

## Plugins Inventory (22 Plugins)

| Plugin | Description | Source / Documentation |
|---|---|---|
| [`android-cli-plugin`](android-cli-plugin/) | Manage Android Virtual Devices, inspect UI layouts, mirror screens, and render Compose previews | Official Android Platform |
| [`chrome-devtools-plugin`](chrome-devtools-plugin/) | Browser automation, accessibility auditing, LCP/CWV performance, and debugging via Puppeteer | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| [`cloudflare`](cloudflare/) | Cloudflare Workers, Durable Objects, Agents SDK, R2, D1, KV, Basin, and framework deployments | [cloudflare/skills](https://github.com/cloudflare/skills) |
| [`context7`](context7/) | Retrieve up-to-date documentation and code examples for modern libraries and frameworks | [context7.com](https://context7.com) |
| [`firebase`](firebase/) | Cloud Firestore, Security Rules, Firebase Auth, App Hosting, Data Connect, and Crashlytics | [firebase/agent-skills](https://github.com/firebase/agent-skills) |
| [`gcalendar`](gcalendar/) | Manage Google Calendar events, check availability, resolve scheduling conflicts, and RSVP | Google Workspace |
| [`gdocs`](gdocs/) | Read, draft, format, and edit Google Docs, insert tables/chips, and export markdown | Google Workspace |
| [`gdrive`](gdrive/) | Search, organize, download, upload, and manage permissions on Google Drive files and folders | Google Workspace |
| [`gemini-api`](gemini-api/) | Call the Gemini Interactions API, Decisions API, Live API, and multimodal streaming models | [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) |
| [`gmail`](gmail/) | Search, read, draft, send, and organize emails, attachments, and labels via Gmail CLI | Google Workspace |
| [`google-antigravity-sdk`](google-antigravity-sdk/) | Design, configure, and orchestrate autonomous AI agents and multi-agent swarms with AGY Python SDK | Google Antigravity |
| [`gsheets`](gsheets/) | Read, write, format, and calculate Google Sheets spreadsheets, charts, and CSV imports | Google Workspace |
| [`gslides`](gslides/) | Create, draft, and update Google Slides presentation decks | Google Workspace |
| [`headroom`](headroom/) | Context window compression, retrieval, and token efficiency optimization | Headroom |
| [`mobbin`](mobbin/) | Search 600,000+ real app UI screens and redesign components backed by production patterns | [mobbin/skills](https://github.com/mobbin/skills) |
| [`modern-web-guidance-plugin`](modern-web-guidance-plugin/) | Web best practices, modern responsive design, dialogs/popovers, and Manifest V3 extensions | [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance) |
| [`notion`](notion/) | Notion workspace management, knowledge capture, database design, and project homes | Notion |
| [`plugin-repository-toolkit`](plugin-repository-toolkit/) | AI tool discovery, convert GitHub repos to agent skills, audit plugin repositories | [laxmi-narayan-87](https://github.com/laxmi-narayan-87/plugin-repository-toolkit) |
| [`supabase`](supabase/) | Supabase database design, migrations, RLS policies, Auth, Edge Functions, and Postgres best practices | [supabase-community/supabase-plugin](https://github.com/supabase-community/supabase-plugin) |
| [`testmu-ai`](testmu-ai/) | Evaluate, red-team, regression-test, and benchmark AI agents using Rook | TestMu AI |
| [`vercel-plugin`](vercel-plugin/) | Next.js, Vercel AI SDK, deployments, edge compute, React best practices, and Vercel MCP | [vercel/vercel-plugin](https://github.com/vercel/vercel-plugin) |
| [`vibe-wise`](vibe-wise/) | Learning-first AI pair programming with human-in-the-loop checkpoints (Build, Design, Implementation) | [nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise) |

## Installation in Antigravity

Copy or symlink any plugin from this directory into your Antigravity plugin directory:

```bash
# Global installation (available in all projects):
cp -r gemini/<plugin-name> ~/.gemini/config/plugins/

# Project-specific installation:
mkdir -p .agents/plugins
cp -r gemini/<plugin-name> .agents/plugins/
```
