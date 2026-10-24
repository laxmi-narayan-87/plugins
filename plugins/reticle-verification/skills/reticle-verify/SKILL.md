---
name: reticle-verify
description: Use Reticle to prove whether a change works in a real running web or desktop app. Trigger when asked to verify a coding agent's claimed fix, investigate a UI bug, validate a user-facing change, replay a saved journey, or distinguish a real pass from an unknown result.
---

# Reticle — verify behavior in the running app

Use Reticle's MCP tools to observe and verify the real application. Do not infer success from source code, a test summary, a screenshot, or a successful setup command alone.

## Start with the active session

1. Check whether `reticle_*` tools are available.
2. If available, call `reticle_session` with `action: "list"` and follow its `next_action`.
3. If the project is not wired, explain that Reticle needs a development-only SDK in the app. Ask before running the initialization command because it changes project files and may install dependencies.
4. If the MCP server is not available, do not claim to have driven the app. Give the user the official setup path at https://docs.reticle.sh/quickstart and stop the live-verification part.

## Choose the smallest relevant check

- To ask whether a change broke a known area, use `reticle_verify` with `action: "change"` and the changed file paths.
- To replay a saved journey, inspect the available tools and call the documented flow replay route.
- To verify new behavior, inspect the interactive page once, group setup actions into `reticle_act` steps, and put an explicit expected result on each consequential step. End with `reticle_act_and_wait` whose `until` predicate states the final user-visible or application-state consequence.
- To diagnose a defect, inspect the relevant source before proposing a fix. Reticle observes behavior; it does not by itself explain the root cause.

## Verdict rules

1. Treat only `verified: "yes"` as a pass.
2. Treat `verified: "no"` as a failure and report the evidence.
3. Treat `verified: "unknown"` as inconclusive. State what evidence was missing or why Reticle could not decide.
4. Treat `verified: "no-fault"` as unproved when no expected outcome was declared. It is not a pass.
5. A page inspection, navigation, observation, or bare action is not proof. A verdict must come from a supported verification call.
6. Never weaken or remove an assertion to make a check pass. If it fails, inspect the expected and observed result and repair the product or the check.
7. Describe the consequence before taking an action. Use `reticle_act_and_wait` with an explicit `until` predicate when one action must prove its outcome.
8. Use an unambiguous target such as test ID, role and accessible name, label, or text. Do not guess when several elements match.
9. Set `durable: true` when the change must survive reload, where supported.
10. Before performing destructive actions such as deleting a record, issuing a payment, or sending an irreversible operation, obtain explicit user authorization and use the tool's required confirmation argument only for that authorized action.

## Evidence and final report

Report:
- the scenario and expected outcome;
- the actual Reticle verdict (`yes`, `no`, `unknown`, or `no-fault`);
- relevant observed network, console, route, signal, or state evidence;
- the most useful `file:line` location returned by Reticle, if present;
- the limitation or next action.

Do not say "tested", "fixed", "working", or "verified" unless a verification tool returned evidence supporting that exact claim. Distinguish setup success from a successful real flow.

## Saved flows and CI

When an existing saved flow covers the affected code, prefer replaying it. When the user asks for regression coverage, save a meaningful journey and rerun it without relying on a fresh model-generated action sequence. For CI-oriented questions, explain that Reticle's gate can require passing runs when a change affects a saved flow; do not claim the repository's CI ran unless execution evidence exists.

## Privacy and safety

- Reticle is intended for development-time instrumentation. Respect the project's security boundary and do not advise shipping the SDK in production.
- Explain that linking a project changes what may sync to Reticle's platform. Point to https://docs.reticle.sh/what-is-recorded.md and https://docs.reticle.sh/telemetry.md when the user asks about data handling.
- Do not expose captured secrets or app data in reports. Redact values that could identify users or provide credentials.
- Reticle documents a loopback bridge and redaction of passwords, tokens, and card numbers. Do not broaden those claims beyond the current documentation.
- Never run an installer, initialize the project, change repository files, or perform destructive UI actions without the applicable authorization and host approval.

## Completion condition

The task is complete only when the requested outcome has an evidence-backed verdict or when you clearly report why it could not be obtained. A successful setup or available tool list alone is not completion.

## Official references

- Quickstart: https://docs.reticle.sh/quickstart
- Tool overview: https://docs.reticle.sh/tools/overview.md
- Predicates: https://docs.reticle.sh/predicates.md
- Data recorded: https://docs.reticle.sh/what-is-recorded.md
- Telemetry: https://docs.reticle.sh/telemetry.md
