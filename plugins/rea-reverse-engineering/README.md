# REA Reverse Engineering plugin adapter

A skills-only companion plugin for planning and interpreting workflows with the REA CLI/MCP toolkit.

## Important limitation

The upstream REA MCP server uses local stdio transport (`npx rea-agents mcp`), not a verified public hosted endpoint. This package deliberately does not include an invented remote MCP URL. It provides investigation guidance but does not itself invoke local REA tools or access the user's machine. To get live REA operations, connect REA in a client that supports local stdio MCP servers, or deploy a properly secured, user-authorized remote bridge and then update the plugin to its verified endpoint.

Official upstream: https://github.com/morluto/rea
