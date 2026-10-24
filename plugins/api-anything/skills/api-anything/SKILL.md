---
name: api-anything-workflow
description: Use when setting up or using the API Anything project to turn website frontend requests into reusable operations, call existing website operations, troubleshoot authentication or drift, or follow its local CLI/MCP workflow.
---

# API Anything workflow

Use the upstream project documentation as the source of truth: https://github.com/goodnight000/api-anything and its `skills/api-anything/SKILL.md`, `INSTALL.md`, `docs/QUICKSTART.md`, and `docs/REFERENCE.md`.

## Important runtime boundary

API Anything is a local tool; it uses the user's machine, network, saved local specs, browser sessions, and optionally Chromium. This plugin package does not host API Anything and does not provide a remote API Anything endpoint. Do not claim that the MCP tools are connected unless the host explicitly shows their availability. The supported upstream MCP setup is a local stdio server launched as `api-anything mcp` after installing the CLI.

## Setup

- Follow the current upstream `INSTALL.md`; check its runtime requirements (README currently says Node.js 22.13+).
- If installing manually, follow upstream instructions: clone the repository, run `npm ci`, then install the packed package as documented. Do not use undocumented installation commands.
- Connect the local MCP server using the host's supported stdio configuration and upstream command `api-anything mcp`.
- Restart the host if required and verify that the tools are actually available before claiming completion.
- Chrome or another supported Chromium browser is needed to create operations and for browser-tier fallback; it is not needed for every direct HTTP read.

## Using existing operations

1. List configured sites, then list operations for the chosen site. Read the site's notes and operation parameter definitions.
2. Call only an operation that actually exists, using the declared parameters and formats.
3. Check `ok` before reading `data`; inspect the result identity, range, and `truncated` status. Report the `tier` and `healed` indicators when relevant.
4. An empty result can mean the website returned no results for those inputs. Do not assume it indicates a broken operation.

## Learning new operations

Use the upstream skill and CLI when shell/browser access is available. Otherwise give the user the exact, grounded CLI steps and explain what must run locally.

1. Clarify the intended questions, variable inputs, required output fields, login needs, read/write scope, and frequency if they are not already specified. Ask no more than three concise questions.
2. Propose an explicit operation plan before capturing. Wait for the user's approval to proceed with that plan.
3. Use `capture --outline` first. Prefer page-rendered HTML or stable embedded JSON-LD for server-rendered pages when appropriate. Use `inspect` only when outlines are insufficient.
4. Use `add` with two distinct example input sets when possible. Inspect warnings and previews; never save an operation that extracts the wrong data or carries credentials.
5. Test each operation using an input that was not used as an example and compare the returned fields to the website. Run `verify` as appropriate. Report what was tested and any unsupported pages/fields.

Never invent URLs, operations, selectors, parameters, fields, or test outcomes. Do not claim that a website was explored unless it was actually captured/inspected.

## Authentication

For protected sites, use the upstream login workflow. Never ask for passwords or copy cookies/tokens into the chat or operation specs. If login needs a visible browser window, 2FA, or CAPTCHA, ask the user to complete it themselves. If multiple local browser profiles are offered, ask the user to select the correct profile rather than choosing one.

## Error handling

Follow the upstream failure loop and stop after its allowed retry:

- `auth`: ask the user to run `api-anything login <site>` if refresh cannot be performed through an available MCP tool.
- `rate`: stop and report throttling; do not retry immediately.
- `blocked`: ask the user to complete the human login/challenge.
- `drift`: follow the returned `next` hint once, then stop if it fails.
- `input`: check the actual operation parameters and whether the requested data is genuinely empty; don't heal/re-add.
- `error`: retry at most once, then report the reason and next step.

## Write safety

Writes are not bundled by default. Never perform a write unless the user specifically requested that action and authorized the exact target/content. For an uncertain target or payload, confirm first. Before a real write, perform a documented dry run and inspect the redacted request. Enable `--allow-writes` only for the specific authorized task. Treat HTTP 2xx as an acknowledgment, not proof of delivery; inspect the resulting object or receipt. If the tool warns an action may have gone through, do not retry.

## Privacy and scope

API Anything stores local specs and credentials under `~/.api-anything` by default (`API_ANYTHING_HOME` can override it). Specs should store credential references, not secret values. Treat site terms, account permissions, and rate limits as constraints. Do not export specs containing session values.

## Reporting

For newly learned operations, summarize `operation | inputs | returns | verification`. Clearly separate observed facts, unverified assumptions, and local steps the user must perform. Do not claim the plugin itself installed the CLI, started a local process, imported sessions, or deployed a server unless those actions were performed and verified.
