# Personal Plugin Archive

This repository stores the retrievable source files for **34 private plugins** currently listed in the Plugin Creator account for `laxmi-narayan-87`. Each folder under `plugins/` preserves the source-relative directory layout for manifests, skill instructions, references, tests, scripts, and text assets that were readable through the registry.

## Plugin index

- [reticle-verification](plugins/reticle-verification/)
- [beyondseo](plugins/beyondseo/)
- [artemis-android-qa](plugins/artemis-android-qa/)
- [serena-coding-agent](plugins/serena-coding-agent/)
- [context7-documentation](plugins/context7-documentation/)
- [omniroute-operator](plugins/omniroute-operator/)
- [pentagi-security-workflow](plugins/pentagi-security-workflow/)
- [claude-mem-adapter](plugins/claude-mem-adapter/)
- [qa-quality-agent](plugins/qa-quality-agent/)
- [mirofish-simulation-guide](plugins/mirofish-simulation-guide/)
- [wellfound-auto-apply](plugins/wellfound-auto-apply/)
- [ecc-engineering-companion](plugins/ecc-engineering-companion/)
- [graphify-agent](plugins/graphify-agent/)
- [build-your-own-x-guide](plugins/build-your-own-x-guide/)
- [claudex-loop-assistant](plugins/claudex-loop-assistant/)
- [overleaf-helper](plugins/overleaf-helper/)
- [harvey-sales-operator](plugins/harvey-sales-operator/)
- [weknora-knowledge-assistant](plugins/weknora-knowledge-assistant/)
- [slopmonster-writing-review](plugins/slopmonster-writing-review/)
- [api-anything](plugins/api-anything/)
- [archify-diagrams](plugins/archify-diagrams/)
- [career-ops-copilot](plugins/career-ops-copilot/)
- [agent-reach-guide](plugins/agent-reach-guide/)
- [ai-labs-workflows](plugins/ai-labs-workflows/)
- [ai-video-storyboard](plugins/ai-video-storyboard/)
- [codex-security-advisor](plugins/codex-security-advisor/)
- [humanizer](plugins/humanizer/)
- [rea-reverse-engineering](plugins/rea-reverse-engineering/)
- [not-ai](plugins/not-ai/)
- [impeccable-design-workflow](plugins/impeccable-design-workflow/)
- [brag-launch-video](plugins/brag-launch-video/)
- [ian-xiaohei-illustrations](plugins/ian-xiaohei-illustrations/)
- [inbox-intelligence](plugins/inbox-intelligence/)
- [placement-intelligence](plugins/placement-intelligence/)

## What is included

- Plugin manifests and metadata files (`plugin.json`, `manifest.json`, and `.codex-plugin/plugin.json`, where present).
- Skill instructions, supporting reference documents, README files, tests, scripts, and readable text assets exposed by the plugin registry.
- Separate folders per plugin to avoid filename collisions and preserve the original relative paths.

## Archive limitations

- This is an archive of the plugin package files exposed by the registry, **not necessarily each upstream project's complete runtime codebase**. Some plugins explicitly rely on their upstream repositories or external runtimes.
- Binary assets that the file interface cannot return as UTF-8 text are not included. In particular, the `not-ai/assets/composer-icon.png` binary asset was not transferred; textual SVG assets were included where available.
- No secrets, tokens, environment files, or credentials should be committed to this public repository. Review carefully before adding any locally stored runtime configuration.
- Upstream projects remain governed by their own licenses and are linked from each plugin's metadata when present.

## Branch

All archive commits were pushed to `main` without force-pushing or deleting existing repository content.
