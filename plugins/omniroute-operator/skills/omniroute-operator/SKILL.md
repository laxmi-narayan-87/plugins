---
name: omniroute-operator
description: Use when the user needs help installing, configuring, operating, connecting to, or troubleshooting their OmniRoute AI gateway, model/provider routing, quota-aware fallback, compression, or MCP/A2A interfaces.
---

# OmniRoute Operator

Help the user operate the OmniRoute project at https://github.com/cheaper-inference/OmniRoute. Treat the repository documentation and the user's installed version as the source of truth; the interface and endpoint inventory can change between releases.

## Scope and limits

- This skill is an operator's guide, not a hosted gateway, remote-control agent, or built-in MCP connection to the user's running instance.
- Never assume `localhost` on the user's machine is reachable from ChatGPT or another remote client. Local URLs only work for clients running on the same host/network namespace unless the user deliberately configures safe remote access.
- Do not claim that a provider, model, quota, free tier, test, or connection was verified unless the user supplied output or a real available tool verified it.
- Keep API keys, OAuth tokens, passwords, and session cookies out of chat transcripts, logs, screenshots, code, and plugin files. Ask for redacted logs only. Prefer the official provider login/configuration flow and environment variables or the project's secrets store.
- Do not advise exposing the admin dashboard or control-plane endpoints to the public internet without strong authentication, scoped tokens, TLS, and network restrictions.
- OmniRoute's MCP tool scopes and enforcement are version/configuration-dependent. Check the installed version's docs and runtime configuration rather than assuming scopes are enabled by default.

## First response: identify the goal

Determine whether the user wants to (1) install/run OmniRoute, (2) connect an LLM client, (3) configure a provider, (4) select or discover a model, (5) investigate routing/fallback/quota issues, (6) configure compression, (7) connect MCP/A2A, or (8) diagnose a security or deployment concern. Ask only for details necessary to proceed, typically OS/runtime, install method, redacted error, and whether the client and gateway are on the same host.

## Connection and diagnostic workflow

1. **Confirm the runtime.** Ask which release/version and install route is in use (npm/package, source, Docker, desktop/PWA, or remote VPS). Use the official project instructions for that release.
2. **Run the project's own diagnostics.** Recommend `omniroute doctor` and `omniroute setup` where applicable. For service/container installs, inspect the relevant process/container logs and port mapping without posting secrets.
3. **Confirm health and base URL.** Project examples commonly use the local dashboard/API on port `20128`, with API paths under `/v1`. Treat these as defaults only; verify actual host/port and deployment mapping.
4. **Verify API authentication.** OmniRoute examples use an OmniRoute key copied from Dashboard → Endpoints. Never ask the user to paste the key. Have them place it locally in a shell environment variable and test `GET /v1/models` against their own configured base URL. Example pattern (replace the base URL and set the key in the local shell without sharing it):

   ```sh
   curl "$OMNIROUTE_BASE_URL/v1/models" \
     -H "Authorization: Bearer $OMNIROUTE_API_KEY"
   ```

   If environment variables are not configured, show platform-specific commands only after identifying the shell. Do not print secret values as part of debugging.

5. **Connect the client.** Use the client's currently documented support for OpenAI-compatible endpoints, provider/model IDs, and API keys. Typical values are base URL ending in `/v1`, the user's OmniRoute key, and a model ID returned by `/v1/models` or the dashboard. Avoid inventing model IDs.
6. **Diagnose provider/model failures.** Check provider connection state, provider limits/terms, routing mode, model ID, timeout/network errors, rate limits, and recent redacted logs. Retry only after understanding whether the error is transient; avoid unsafe repeated requests that incur cost.
7. **Diagnose MCP.** OmniRoute documentation describes stdio MCP via `omniroute --mcp`, HTTP at `/api/mcp/stream`, and SSE at `/api/mcp/sse` on the running service. Confirm those paths and transport are present in the installed version. Prefer loopback or a trusted private network; for remote mode use the project's supported scoped-token and TLS/network configuration. Do not confuse an HTTP dashboard endpoint with an externally hosted MCP endpoint.
8. **Diagnose A2A.** The project documents an agent card at `/.well-known/agent.json`. Check current docs and service logs if it fails; do not claim an endpoint is live based only on docs.
9. **Security review.** Check bind address, firewall/reverse proxy, TLS, authentication, token scopes, audit logs, secrets in environment/config files, least privilege, and whether process-spawning features remain loopback-only. Recommend rotating any credential that appears to have been exposed and cleaning repository history where needed.
10. **Report evidence.** Separate observed facts, likely causes, and unverified hypotheses. Give a minimal reproduction, exact safe diagnostic command, expected result, and rollback step for configuration changes.

## Common usage patterns

- **Start/check:** follow the current release's installation instructions, then use `omniroute doctor`; inspect dashboard status and service logs.
- **List available models:** test `GET /v1/models` with the locally configured endpoint and key.
- **OpenAI-compatible client:** configure the client's base URL, OmniRoute key, and a model ID obtained from the running instance.
- **MCP stdio:** use the project's documented `omniroute --mcp` invocation and configure the client using its current MCP configuration format.
- **MCP HTTP/SSE:** use the documented `/api/mcp/stream` or `/api/mcp/sse` transport only if enabled and reachable for that client.
- **Remote gateway:** use the project's supported remote connection setup and scoped access tokens. Avoid exposing the admin dashboard broadly; restrict network access.
- **Quota/fallback:** validate the chosen routing mode, eligible provider credentials, quota/rate limit status, and whether provider/model terms permit the desired usage. Never guarantee availability of catalog entries marked free.
- **Compression:** start at a conservative setting, compare outputs for semantic fidelity (especially code, commands, URLs, identifiers, JSON, and test output), and disable the pipeline to isolate regressions.

## Response format for troubleshooting

1. State the most likely cause(s), clearly marking uncertainty.
2. Give 1–3 ordered checks, using commands for the user's OS/shell.
3. Explain what a healthy result looks like and what each failure implies.
4. Ask for only redacted output required for the next step.
5. For any risky change, explain impact and give a rollback procedure.

## Reference links

- Repository and current README: https://github.com/cheaper-inference/OmniRoute
- API reference: https://github.com/cheaper-inference/OmniRoute/wiki/API-Reference
- Check current installation, MCP server, security, provider and environment-variable documentation in the repository/wiki for the version the user is running.
