# Gemini / Antigravity Plugins

This directory contains plugins designed and structured for the **Google Gemini / Antigravity** agent platform.

## Plugins Directory

- **[vibe-wise](vibe-wise/)**: Learning-first AI pair programming plugin based on [nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise). Enforces deliberate human-in-the-loop checkpoints (Build, Design, Implementation) to ensure developers understand system architecture and retain design ownership.

## Installation in Antigravity

Copy or symlink any plugin from this directory into your Antigravity plugin directory:

```bash
# Global installation:
cp -r gemini/vibe-wise ~/.gemini/config/plugins/

# Project/workspace-specific installation:
mkdir -p .agents/plugins
cp -r gemini/vibe-wise .agents/plugins/
```
