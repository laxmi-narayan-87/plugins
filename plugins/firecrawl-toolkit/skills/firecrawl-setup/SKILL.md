---
name: firecrawl-setup
description: Use when someone needs to connect, configure, authenticate, or understand Firecrawl access through an existing ChatGPT app, API key, MCP server, SDK, or CLI.
---

# Set up Firecrawl safely

## Workflow

1. Establish the target surface: the existing ChatGPT Firecrawl app, a coding-agent MCP connection, the CLI, or an SDK. Do not ask the user to repeat details already visible in the current host.
2. Prefer the already registered Firecrawl app when it is available. Resolve operation names and parameter contracts from the live tool inventory; do not assume every Firecrawl endpoint is exposed by every client.
3. For local coding-agent setup, begin from Firecrawl's official docs and the repository README. The upstream README currently documents `npx -y firecrawl-cli@latest init --all --browser` for CLI/skill onboarding. Explain that this changes local configuration and may start an authentication flow; execute only when the user has authorized local setup and the host can run commands.
4. For direct API access, use the current official documentation at https://docs.firecrawl.dev/ and the API specification from the repository. Verify SDK names, endpoint versions, accepted formats, and response shape against the currently installed SDK/docs before writing code.
5. Keep credentials out of chat, prompts, screenshots, Git, plugin files, logs, examples, and generated output. Never ask the user to paste an API key. Direct them to configure it through the product's supported secret or environment-variable mechanism. Use placeholders such as `fc-YOUR_API_KEY` in examples.
6. Before large crawling or agent jobs, explain the likely credit cost and scope. If a credit-usage tool is exposed, inspect usage before launching a potentially expensive batch when appropriate. Do not launch a paid or persistent operation merely to test connectivity.
7. If tools fail with authentication, credits, rate-limit, or permission errors, report the exact blocker and stop; do not change accounts, retry with a different identity, or fabricate a successful result.

## Completion criteria

Report which access path is configured or documented, what still requires the user's own action, and what was actually tested. Clearly distinguish source/documentation review from successful live Firecrawl execution.
