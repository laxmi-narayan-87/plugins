---
name: wensity-workflow
description: Use when the user wants to explore Wensity UI, select React or Next.js components, understand pricing and licensing, configure its MCP server, or plan and safely install Wensity components.
---

# Wensity UI workflow

## Purpose and boundaries

Wensity UI is a React and Next.js component library with animated components, UI primitives, full-page blocks, templates, and browser-based design tools. Primary site: https://ui.wensity.com/.

Use the live Wensity catalog and official documentation whenever available. Do not fabricate component slugs, props, source code, dependency lists, license status, prices, or compatibility. The official MCP server uses local stdio and is not a remotely hosted HTTP service. Do not invent a remote MCP URL or claim a ChatGPT cloud connection exists.

## Official resources

- Component catalog: https://ui.wensity.com/components
- UI primitives: https://ui.wensity.com/primitives
- Blocks: https://ui.wensity.com/blocks
- Templates: https://ui.wensity.com/templates
- Design tools: https://ui.wensity.com/tools
- Background Studio: https://ui.wensity.com/background-studio
- Getting started: https://ui.wensity.com/docs/getting-started
- MCP setup: https://ui.wensity.com/docs/mcp
- CLI: https://ui.wensity.com/docs/cli
- Pricing: https://ui.wensity.com/pricing
- License: https://ui.wensity.com/license
- Token management: https://ui.wensity.com/dashboard/tokens

## Discovery and selection

1. Clarify the UI outcome in practical terms (for example: cinematic hero, animated testimonial, pricing table, command palette, dashboard card, form, or navigation).
2. Search the live catalog for matching components, primitives, and blocks. Filter by category, tags, tier, type, or dependencies as supported by the current catalog.
3. Compare candidates by behavior, visual effect, props, dependencies, responsive behavior, accessibility, framework compatibility, and license tier.
4. Retrieve item details before recommending implementation. Explain what the component does and link its detail page and preview.
5. Offer a free alternative when an item is Pro or access is unavailable.

Never imply that a premium item is installable just because it is visible in the catalog.

## Licensing and cost

The Wensity site's published FAQ describes a free core, including MIT-licensed free components and primitives, and paid Pro components/blocks covered by a commercial license. Exact counts and prices may change; verify current official pricing and license pages before quoting them. Do not redistribute Pro source, bundle it into a public component library, or expose source from a licensed project as a general-purpose kit. The official site says Pro source is intended for licensed personal/commercial/client work and may not be passed on as a component library, template, UI kit, or public repository. Check the current license terms rather than treating a summary as legal advice.

## Official MCP setup

The official package documented by Wensity is `@wensity/mcp`; the docs currently show version `0.1.2` and require Node.js 20+ and an MCP client that can launch local stdio servers. Pin the documented version unless checking the official update notice for a newer release.

Codex command:

```bash
codex mcp add wensity -- npx -y @wensity/mcp@0.1.2
```

Equivalent Codex config:

```toml
[mcp_servers.wensity]
command = "npx"
args = ["-y", "@wensity/mcp@0.1.2"]
```

Cursor config (`.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "wensity": {
      "command": "npx",
      "args": ["-y", "@wensity/mcp@0.1.2"]
    }
  }
}
```

VS Code config (`.vscode/mcp.json`):

```json
{
  "servers": {
    "wensity": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@wensity/mcp@0.1.2"]
    }
  }
}
```

Claude Code project setup:

```bash
claude mcp add --transport stdio --scope project wensity -- npx -y @wensity/mcp@0.1.2
```

After setup, restart/reload the MCP client and ask it to list the connected `wensity_` tools. If setup fails, first check `node --version` (must be 20+) and `npx -y @wensity/mcp@0.1.2 --version`. Use the official docs for the latest configuration and version.

## Wensity MCP tool workflow

The official documentation lists six tools:

- `wensity_search`: search live components, primitives, and blocks.
- `wensity_get_item`: inspect description, props, dependencies, install command, and links; it does not return component source.
- `wensity_auth_status`: verify local Wensity credentials and accessible tier.
- `wensity_inspect_project`: inspect framework, language, package manager, aliases, Tailwind file, helper availability, and already installed Wensity files. Project inspection is local and should not expose file contents.
- `wensity_plan_install`: generate the exact proposed file changes, token diff, dependency additions, command, conflicts, and compatibility checks without writing.
- `wensity_install`: apply one previously reviewed plan using its plan token.

Use the safe sequence below.

### Plan first

1. Inspect the target project. Confirm the user selected the correct project directory; never guess a home directory or unrelated project.
2. Check auth status. Free assets require no token. Pro assets require an active Pro license and a credential configured locally with `npx wensity login`.
3. Fetch item details and confirm the exact item slug and tier.
4. Generate an install plan. Present all files to create/modify, npm dependencies, exact package-manager command, Tailwind token changes, compatibility warnings, and conflicts.
5. Wait for explicit approval before calling `wensity_install`. A request to explore or plan is not permission to install.

### Install after approval

1. Use only the plan token from the just-approved plan.
2. Install once. Plans expire after 10 minutes and can be used once.
3. Report installed files and dependency outcome. Package-manager changes may not be rolled back after a failure even though Wensity attempts to roll back its own file writes.
4. Run the project's formatter, linter, type checker, and build where available. Review the diff and test the affected UI at desktop and mobile sizes.
5. Do not delete `.wensity-tmp` recovery journals if an interrupted install reports recovery required. Follow the recovery instructions and inspect `git diff` first.

## Project requirements and cautions

- Node.js 20+ for the MCP server.
- React 18+ for component installs.
- Wensity is built for Next.js and Tailwind CSS v4, but compatibility checks may issue warnings for other setups.
- Run `npx wensity init` when the project needs a Wensity config, as directed by current docs.
- Components are installed as source files, not as a runtime library dependency.
- JavaScript projects may receive `.tsx` files; ensure TypeScript/TSX compilation is supported.
- Templates are standalone projects and are not installed by the MCP server.
- Package-manager operations can run lifecycle scripts and are not transactional. Show the exact command in the plan before approval.
- For Pro access, never ask the user to paste a Wensity token into chat. The user must run `npx wensity login` in their terminal. Tokens are stored locally by the CLI. The assistant should never request or reveal the credential file.
- To revoke access, the user can revoke the token in Wensity's dashboard or run `npx wensity logout` locally.

## CLI alternative

For manual terminal installation, use the official CLI. The docs show `npx wensity@latest init` and `npx wensity@latest add <slug>`; Pro users authenticate with `npx wensity login`. For a block, consult the CLI docs for the correct `--type block` flag. Verify command syntax against the live docs before execution.

## Response format

For component recommendations, provide the exact name/slug, what it does, Free/Pro/Needs Pro status, relevant props/dependencies, compatibility caveats, detail/preview links, and a clear recommendation. For installation, separate the plan from the execution and never skip explicit approval. Be transparent when only guidance is available and the official MCP server is not connected to the current environment.
