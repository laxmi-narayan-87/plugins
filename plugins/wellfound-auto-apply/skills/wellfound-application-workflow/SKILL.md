---
name: wellfound-application-workflow
description: Use when the user wants help setting up, configuring, testing, or troubleshooting the wellfound_autoApply GitHub repository.
---

# Wellfound Auto-Apply: setup and controlled use

## Ground truth

Repository: https://github.com/ankitbaghel01/wellfound_autoApply
Read its current README and source before giving repo-specific steps. The repository README describes a Node.js + Playwright runner that opens a visible Chrome session with a saved Wellfound login, fills application forms, logs submissions to a CSV, and enforces a daily cap. It says dry-run is the default, while `--live` clicks submit. Do not claim that this plugin can access the user's local machine, Chrome profile, `.env`, or files unless a connected tool explicitly provides that access.

## Safety and user control

- Start in dry-run mode. Never run live submissions or schedule automatic live applications without an explicit, current user request.
- Explain that auto-applying may violate Wellfound's terms and can lead to rate limits or account restrictions; encourage checking the current terms and manually reviewing every application.
- Never bypass CAPTCHA, anti-bot checks, access controls, or platform restrictions. If a verification challenge appears, pause automation and ask the user to complete any permitted verification manually; do not add stealth, evasion, fingerprint masking, or retry tactics.
- Keep personal data and API keys local. Never ask the user to paste passwords, session cookies, browser profile files, or secrets into chat. Use `.env.example` as a template and ensure `.env` stays untracked.
- Verify each job's fit, location, eligibility, work authorization, resume, salary, and application answers. Do not fabricate credentials or experience. Prefer human approval before each actual submission.
- Do not promise the workflow is running, has applied, or is scheduled unless a tool confirms it.

## Setup workflow

1. Confirm the user is on their own machine and inspect the repository's latest README and package scripts.
2. Guide them to clone the repository and install dependencies with the documented commands.
3. Create `.env` from `.env.example`; help populate it with verified profile details without collecting secrets in chat. Warn that example settings may include fields for unrelated job-site workflows; only use fields consumed by the Wellfound code.
4. Launch a one-time visible login with the repository's documented `node auto-apply-runner.js wellfound login` command. The user should log in personally and close the browser when finished.
5. Run `node auto-apply-runner.js wellfound` in dry-run mode. Review logs and the visible browser results; no application should be submitted.
6. Inspect configuration and matching logic before any live action. Prefer manual submission or a supervised one-at-a-time workflow over bulk unattended submission. Do not default to `--live` or create unattended live schedules.
7. Help diagnose issues using logs and error text. Do not advise defeating CAPTCHA/bot checks or changing automation fingerprints to avoid detection.

## Logging and verification

- The README says `applications.csv` records live submissions, and state files track daily counts. Confirm actual file content before reporting success.
- Dry-run output is simulation, not a submitted application. State that difference explicitly.
- Avoid deleting state files or logs unless the user specifically requests it and understands the effect.
- Keep resume, cover letter, and application answers accurate and tailored to the specific role.

## Suggested deliverables

Provide concise OS-specific commands, a local configuration checklist, a dry-run checklist, and a troubleshooting path. If the user says "run this" but no local execution capability is connected, inspect the code and guide local execution transparently rather than saying it ran.
