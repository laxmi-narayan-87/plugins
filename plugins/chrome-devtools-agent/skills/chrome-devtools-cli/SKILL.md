---
name: chrome-devtools-cli
description: Use when the user needs repeatable shell commands or scripts to operate Chrome DevTools through the chrome-devtools CLI.
---

# Chrome DevTools CLI

The upstream npm package exposes a `chrome-devtools` CLI. If it is not globally installed, use the documented command-line installation or `npx` workflow appropriate for the user's environment. Check `chrome-devtools <tool> --help` for the current version's parameter schema; do not assume CLI flags remain unchanged across versions.

## Typical workflow

1. `chrome-devtools list_pages` to find a page ID, or `chrome-devtools new_page "https://example.com"` to create a page.
2. `chrome-devtools take_snapshot <pageId>` to obtain element UIDs.
3. Interact using those current UIDs, for example `click`, `fill`, `press_key`, or `type_text`. Re-snapshot after navigation or state changes.
4. Use `list_console_messages`, `list_network_requests`, `take_screenshot`, and performance commands to gather evidence.
5. Save outputs only to an intentional workspace path. Restrict file access with `--allowUnrestrictedPaths=false` where possible; do not use broad filesystem access unless it is explicitly needed and trusted.

## Useful commands

```bash
chrome-devtools list_pages
chrome-devtools take_snapshot 1
chrome-devtools navigate_page 1 --url "https://example.com"
chrome-devtools list_console_messages 1
chrome-devtools list_network_requests 1
chrome-devtools take_screenshot 1 --fullPage true
```

Do not run service start/stop commands before every tool use; the CLI server starts implicitly. Avoid actions that submit forms, alter accounts, delete data, or make purchases unless directly authorized by the user. Sanitize headers, cookies, and outputs before summarizing. Upstream: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/chrome-devtools-cli/SKILL.md.
