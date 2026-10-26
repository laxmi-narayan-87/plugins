# Personal Plugin Archive

This repository archives the plugin packages owned by the connected Plugin Creator registry. It is a package archive, not a mirror of every upstream project's complete runtime source code.

## Current inventory

- Plugin Creator registry inventory: 61 plugins (checked 2026-10-26).
- Package directories in this branch: 61.
- Binary asset `plugins/not-ai/assets/composer-icon.png` remains unavailable through the registry's text-file interface and is not included.

## Plugin index

- [ml-engineering-suite](plugins/ml-engineering-suite/) — archived
- [web-recon-toolkit](plugins/web-recon-toolkit/) — archived
- [firecrawl-toolkit](plugins/firecrawl-toolkit/) — archived
- [ml-data-quality-labeling](plugins/ml-data-quality-labeling/) — archived
- [ml-model-deployment](plugins/ml-model-deployment/) — archived
- [ml-hyperparameter-optimization](plugins/ml-hyperparameter-optimization/) — archived
- [mlops-pipeline-engineer](plugins/mlops-pipeline-engineer/) — archived
- [ml-model-development](plugins/ml-model-development/) — archived
- [superpowers-workflow](plugins/superpowers-workflow/) — archived
- [gstack-workflow-toolkit](plugins/gstack-workflow-toolkit/) — archived
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
- [career-ops-copilot](plugins/career-ops-copilot/) — archived
- [agent-reach-guide](plugins/agent-reach-guide/) — archived
- [ai-labs-workflows](plugins/ai-labs-workflows/) — archived
- [ai-video-storyboard](plugins/ai-video-storyboard/) — archived
- [codex-security-advisor](plugins/codex-security-advisor/) — archived
- [humanizer](plugins/humanizer/) — archived
- [rea-reverse-engineering](plugins/rea-reverse-engineering/) — archived
- [not-ai](plugins/not-ai/) — **partially archived** (missing `assets/composer-icon.png`; not fabricated)
- [impeccable-design-workflow](plugins/impeccable-design-workflow/) — archived
- [brag-launch-video](plugins/brag-launch-video/) — archived
- [ian-xiaohei-illustrations](plugins/ian-xiaohei-illustrations/) — archived
- [inbox-intelligence](plugins/inbox-intelligence/) — archived
- [placement-intelligence](plugins/placement-intelligence/) — archived

## Choose a plugin by topic and use case

Use this decision flow to route a task to the most relevant archived plugin. Start with the outcome you need, then choose the matching topic. The named plugins are examples from this inventory; check each package's own instructions and dependencies before use.

```mermaid
flowchart TD
    A([Start: What do you need?]) --> B{Primary use case}
    B -->|Build, debug, or improve software| C{Engineering task}
    B -->|Research, retrieve, or connect information| D{Knowledge and research}
    B -->|Test quality or inspect security| E{QA or security}
    B -->|Create visuals or content| F{Design and writing}
    B -->|Automate browser or job workflows| G{Automation}
    B -->|Plan career or placement| H{Career support}

    C --> C1[ml-engineering-suite / ml-model-development]
    C --> C2[loop-engineering / claudex-loop-assistant]
    C --> C3[vercel-skills-workflow for deployment workflows]

    D --> D1[context7-documentation for library docs]
    D --> D2[weknora-knowledge-assistant for knowledge retrieval]
    D --> D3[graphify-agent / archify-diagrams for connected concepts]

    E --> E1[qa-quality-agent / artemis-android-qa for testing]
    E --> E2[pya-security-audit / codex-security-advisor for security review]
    E --> E3[reticle-verification for verification workflows]

    F --> F1[impeccable-design-workflow / taste-skill for UI design]
    F --> F2[humanizer / slopmonster-writing-review for writing]
    F --> F3[ai-video-storyboard / brag-launch-video for video concepts]

    G --> G1[browser-use-automation for browser tasks]
    G --> G2[wellfound-auto-apply for job-application workflows]
    G --> G3[agent-reach-guide for outreach/reach workflows]

    H --> H1[career-ops-copilot for career operations]
    H --> H2[placement-intelligence for placement research]

    C1 --> Z[Open the package README or SKILL.md]
    C2 --> Z
    C3 --> Z
    D1 --> Z
    D2 --> Z
    D3 --> Z
    E1 --> Z
    E2 --> Z
    E3 --> Z
    F1 --> Z
    F2 --> Z
    F3 --> Z
    G1 --> Z
    G2 --> Z
    G3 --> Z
    H1 --> Z
    H2 --> Z
    Z --> Y{Instructions, prerequisites, and assets available?}
    Y -->|Yes| X[Follow the package workflow and validate its output]
    Y -->|No| W[Check upstream docs or mark missing dependencies/assets]
    X --> R([Review result before relying on it])
    W --> R
```

### Topic-to-use-case quick guide

| Topic | Example use case | Start with |
|---|---|---|
| Software engineering | Implement a feature, debug code, or improve a development workflow | `ml-engineering-suite`, `ml-model-development`, `loop-engineering` |
| Documentation and knowledge | Find current library guidance or organize retrieved knowledge | `context7-documentation`, `weknora-knowledge-assistant` |
| Diagrams and architecture | Map dependencies, concepts, or system structure | `graphify-agent`, `archify-diagrams`, `diagram-design` |
| QA and testing | Plan test coverage or review an app's behavior | `qa-quality-agent`, `artemis-android-qa`, `reticle-verification` |
| Security | Audit code or structure a security review | `pya-security-audit`, `codex-security-advisor`, `pentagi-security-workflow` |
| UI and visual design | Improve interface consistency and design decisions | `impeccable-design-workflow`, `taste-skill`, `design-md-guide` |
| Writing and media | Review prose or plan video content | `humanizer`, `slopmonster-writing-review`, `ai-video-storyboard` |
| Browser and job automation | Automate browser tasks or organize job-application workflows | `browser-use-automation`, `wellfound-auto-apply` |
| Career and placement | Track career tasks or research placement opportunities | `career-ops-copilot`, `placement-intelligence` |
| Deployment and DevOps | Follow deployment-focused workflows | `vercel-skills-workflow`, `mlops-pipeline-engineer` |

These are routing suggestions based on package names and inventory topics, not guarantees of capability. Confirm each package's `SKILL.md`, manifest, permissions, dependencies, and supported inputs before selecting it. If multiple topics apply, use the narrowest task-specific package first and add supporting packages only when needed.

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
