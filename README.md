# Personal Plugin Archive

This repository archives the plugin packages owned by the connected Plugin Creator registry. It is a package archive, not a mirror of every upstream project's complete runtime source code.

## Current inventory

- Plugin Creator registry inventory: 51 plugins (checked 2026-10-25).
- Package directories in this branch: 51.
- The binary asset `plugins/not-ai/assets/composer-icon.png` remains unavailable through the registry's text-file interface and is not included.

## Plugin index

- [chrome-devtools-agent](plugins/chrome-devtools-agent/) — archived
- [caveman](plugins/caveman/) — archived
- [antigravity-awesome-skills](plugins/antigravity-awesome-skills/) — archived
- [skill-inspector](plugins/skill-inspector/) — archived
- [vercel-skills-workflow](plugins/vercel-skills-workflow/) — archived
- [design-md-guide](plugins/design-md-guide/) — archived
- [taste-skill](plugins/taste-skill/) — archived
- [loop-engineering](plugins/loop-engineering/) — archived
- [ruflo-agent-harness](plugins/ruflo-agent-harness/) — archived
- [openviking-context-plugin](plugins/openviking-context-plugin/) — archived
- [harness-engineering](plugins/harness-engineering/) — archived
- [diagram-design](plugins/diagram-design/) — archived
- [pya-security-audit](plugins/pya-security-audit/) — archived
- [scientific-agent-skills-workflow](plugins/scientific-agent-skills-workflow/) — archived
- [tencentdb-agent-memory](plugins/tencentdb-agent-memory/) — archived
- [browser-use-automation](plugins/browser-use-automation/) — archived
- [arena-skill](plugins/arena-skill/) — archived
- [reticle-verification](plugins/reticle-verification/) — archived
- [beyondseo](plugins/beyondseo/) — archived
- [artemis-android-qa](plugins/artemis-android-qa/) — archived
- [serena-coding-agent](plugins/serena-coding-agent/) — archived
- [context7-documentation](plugins/context7-documentation/) — archived
- [omniroute-operator](plugins/omniroute-operator/) — archived
- [pentagi-security-workflow](plugins/pentagi-security-workflow/) — archived
- [claude-mem-adapter](plugins/claude-mem-adapter/) — archived
- [qa-quality-agent](plugins/qa-quality-agent/) — archived
- [mirofish-simulation-guide](plugins/mirofish-simulation-guide/) — archived
- [wellfound-auto-apply](plugins/wellfound-auto-apply/) — archived
- [ecc-engineering-companion](plugins/ecc-engineering-companion/) — archived
- [graphify-agent](plugins/graphify-agent/) — archived
- [build-your-own-x-guide](plugins/build-your-own-x-guide/) — archived
- [claudex-loop-assistant](plugins/claudex-loop-assistant/) — archived
- [overleaf-helper](plugins/overleaf-helper/) — archived
- [harvey-sales-operator](plugins/harvey-sales-operator/) — archived
- [weknora-knowledge-assistant](plugins/weknora-knowledge-assistant/) — archived
- [slopmonster-writing-review](plugins/slopmonster-writing-review/) — archived
- [api-anything](plugins/api-anything/) — archived
- [archify-diagrams](plugins/archify-diagrams/) — archived
- [career-ops-copilot](plugins/career-ops-copilot/) — missing
- [agent-reach-guide](plugins/agent-reach-guide/) — archived
- [ai-labs-workflows](plugins/ai-labs-workflows/) — archived
- [ai-video-storyboard](plugins/ai-video-storyboard/) — archived
- [codex-security-advisor](plugins/codex-security-advisor/) — archived
- [humanizer](plugins/humanizer/) — missing
- [rea-reverse-engineering](plugins/rea-reverse-engineering/) — archived
- [not-ai](plugins/not-ai/) — archived
- [impeccable-design-workflow](plugins/impeccable-design-workflow/) — archived
- [brag-launch-video](plugins/brag-launch-video/) — archived
- [ian-xiaohei-illustrations](plugins/ian-xiaohei-illustrations/) — missing
- [inbox-intelligence](plugins/inbox-intelligence/) — archived
- [placement-intelligence](plugins/placement-intelligence/) — archived

## Scope and limitations

- Each folder contains the files available through the Plugin Creator package-file interface. These can include manifests, skill instructions, references, support scripts, and assets.
- Upstream repositories remain the source of truth for runtime implementation, dependencies, release history, and files not included in a plugin package.
- Do not commit credentials, API tokens, `.env` files, or other secrets.
- Do not fabricate unavailable binary assets. Restore them from an authoritative package/source distribution or mark them as unavailable.
- Verify each package's license and attribution requirements before redistribution. Presence in this archive does not establish redistribution rights.
- A package inventory can be complete at the directory level and still omit assets that are not accessible through the registry's text-file interface.

## Quality checks

A GitHub Actions workflow runs structural checks for JSON syntax, `SKILL.md` frontmatter, and relative Markdown links. Passing these checks does not prove runtime behavior. Test representative plugins in their intended environment.

## Completeness reporting

- **Archived** means all source files retrievable through the package-file interface were copied.
- **Partially archived** means the package exists but one or more assets/files could not be retrieved.
- **Missing** means the package directory is absent.

Regenerate this index when the registry inventory changes and record the date of that inventory.
