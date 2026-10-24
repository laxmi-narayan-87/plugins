# QA Quality Agent

A skills-only private plugin for evidence-first software testing, inspired by public QA/AI-testing resources. It contains original workflows rather than bundling or copying the linked projects' implementation code.

## Included skills
- `website-qa-agent`: structured website walkthrough, safe execution boundaries, evidence collection, and final reports.
- `qa-test-planning`: requirements analysis, test design, risk prioritization, execution tracking, and defect reporting.
- `ai-system-testing`: AI/LLM/RAG/agent evaluation, safety, robustness, security, and regression testing.
- `genai-testing-roadmap`: a 52-week modular learning path with weekly deliverables and project-based checkpoints.

## Reference projects
- https://github.com/bug0inc/qa-agent — Playwright-oriented AI browser regression automation. Review its FSL-1.1-ALv2 license before incorporating any code or redistributing derivatives.
- https://github.com/naodeng/awesome-qa-skills — broad QA skill catalog. Its repository identifies a PolyForm Noncommercial 1.0.0 license; this plugin uses an original workflow and does not copy its skill files.
- https://github.com/tugkanboz/awesome-ai-testing — curated AI-testing tools/resource list, CC0-1.0 according to GitHub metadata.
- https://github.com/srvsngh99/genai-testing-journey — 52-week GenAI testing learning journey, MIT licensed.

This plugin does not install or execute browser automation, connect to a website, or call third-party AI APIs by itself. It guides testing and reporting; actual actions must be performed by available browser, terminal, or testing tools and must be described as executed only when evidence exists.
