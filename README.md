# Personal Plugin Archive

This repository archives the plugin packages available in the connected Plugin Creator registry. It is a **package archive**, not a mirror of each upstream project's complete runtime source code.

## Inventory status

- Registry inventory: 50 plugins at the time this index was generated.
- Packages archived in this branch: 50.
- Packages still missing: 0.
- Source-of-truth for package contents: the original Plugin Creator package.

## Plugin index

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
- [career-ops-copilot](plugins/career-ops-copilot/) — archived
- [agent-reach-guide](plugins/agent-reach-guide/) — archived
- [ai-labs-workflows](plugins/ai-labs-workflows/) — archived
- [ai-video-storyboard](plugins/ai-video-storyboard/) — archived
- [codex-security-advisor](plugins/codex-security-advisor/) — archived
- [humanizer](plugins/humanizer/) — archived
- [rea-reverse-engineering](plugins/rea-reverse-engineering/) — archived
- [not-ai](plugins/not-ai/) — archived
- [impeccable-design-workflow](plugins/impeccable-design-workflow/) — archived
- [brag-launch-video](plugins/brag-launch-video/) — archived
- [ian-xiaohei-illustrations](plugins/ian-xiaohei-illustrations/) — archived
- [inbox-intelligence](plugins/inbox-intelligence/) — archived
- [placement-intelligence](plugins/placement-intelligence/) — archived

## Scope and limitations

- A package includes only the files available through the Plugin Creator package-file interface. It may contain manifests, skill instructions, references, and support assets; it does not necessarily include the full upstream runtime implementation or all dependencies.
- Upstream repositories remain authoritative for their own implementation code, releases, and dependencies.
- Do not add credentials, API tokens, `.env` files, or other secrets.
- Binary assets that are not exposed by the package-file interface must be restored from an authoritative package release or source; they should not be fabricated.
- Verify license and attribution requirements per package before redistributing files. The presence of a file in this archive does not establish that it is licensed for redistribution.

## Validation

Automated checks should validate JSON syntax, skill frontmatter, internal file references, and registry inventory completeness. Such checks are structural and do not prove that a plugin works at runtime.
