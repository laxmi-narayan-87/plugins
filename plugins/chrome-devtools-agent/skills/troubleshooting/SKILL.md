---
name: troubleshooting
description: Use when the Chrome DevTools MCP server fails to launch, connect, discover tools, control Chrome, or returns browser/transport errors.
---

# Chrome DevTools MCP troubleshooting

1. Capture the exact error message and identify the host client, OS, Node.js version, installed package/version and whether Chrome is installed.
2. Verify that the client configuration uses the package command and valid JSON, for example `npx -y chrome-devtools-mcp@latest`. Restart the host client after configuration changes unless configuration watching is explicitly enabled and supports the changed option.
3. Check Node.js LTS and a supported Google Chrome or Chrome for Testing installation. The server starts a browser lazily when the first browser-dependent tool is called.
4. For existing Chrome sessions, verify the debugging endpoint is intentionally enabled and is reachable. Use documented `--browserUrl` or `--wsEndpoint` settings only with a known endpoint; do not fabricate endpoints or expose auth headers.
5. Check flags: optional categories (extensions/PWA/WebAuthn/memory) may be disabled by default and their tools will not exist unless enabled at startup. Confirm whether `--slim` is reducing the tool surface.
6. If startup still fails, consult the upstream troubleshooting documentation and request sanitized logs. Keep secrets and personal browser data out of diagnostic output.

Upstream guide: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/troubleshooting.md.
