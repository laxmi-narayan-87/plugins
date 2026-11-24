# Headroom Context Optimizer Plugin

Integrates [Headroom](https://github.com/headroomlabs-ai/headroom) into Antigravity as an MCP server to reduce token usage when processing large payloads.

## Features
- **Token Compression (`headroom_compress`)**: Compresses verbose strings, terminal logs, and JSON structures.
- **Lossless Retrieval (`headroom_retrieve`)**: Looks up uncompressed original text via its unique content hash.
- **Session Telemetry (`headroom_stats`)**: Tracks tokens and estimated dollars saved across sessions.

## Prerequisites
- Requires `uv` (or Python 3.10+) installed on the host system.

## Usage
The plugin automatically exposes Headroom MCP tools in your sessions:
- Compress large outputs before feeding them to downstream models or analysis tasks.
- Retrieve full uncompressed content whenever precise details are needed.
- Inspect `headroom_stats` to verify real-time token and cost savings.
