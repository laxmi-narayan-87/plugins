# Reticle Verification Plugin

Portable Agent Plugins package for the Reticle live application verification workflow.

## Contents

- `plugin.json`: Agent Plugins 1.0 manifest.
- `mcp.json`: local stdio MCP connection to the Reticle server package.
- `skills/reticle-verify/`: workflow guidance, verdict semantics, privacy guardrails.
- `skills/host-workspace-operator/`: repository and local workspace safety guidance.
- `assets/`: square SVG mark variants for light/dark surfaces.

## Runtime requirements

The MCP server uses `npx @reticlehq/server@3.7.0 mcp`; use a supported Node.js runtime and network access to obtain the package. Reticle must also be initialized in the target app and its development server running before live verification can return a verdict. Follow https://docs.reticle.sh/quickstart.

## Important limits

This plugin guides the host through the Reticle MCP workflow. It does not itself instrument an app, create a running browser, grant shell access, or prove any test outcome. The user's host must support the configured stdio MCP runtime. Never claim success without a returned Reticle verdict. Ask before initialization because it modifies the user's project.

## Source

Adapted from the documented Reticle project: https://github.com/reticlehq/reticle and https://docs.reticle.sh.
