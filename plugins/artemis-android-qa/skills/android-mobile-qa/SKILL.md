---
name: artemis-android-qa
description: Use when planning, diagnosing, executing, or reporting Android mobile application tests with Google's ARTEMIS project or its MCP tools.
---

# ARTEMIS Android QA workflow

Use this workflow when the user asks for Android testing, app exploration, mobile bug reproduction, or review of ARTEMIS outputs. The source project is https://github.com/google/artemis. ARTEMIS is a separately installed local/device automation project; this plugin provides grounded instructions and review help, not a hosted ARTEMIS runtime.

## Truthfulness and scope

- Never claim a device was tested, an app was opened, a screenshot was captured, a test passed, or a defect was reproduced unless the current conversation contains actual execution/tool evidence.
- Clearly separate **Verified**, **Observed but not reproduced**, **Expected / not a defect**, **Blocked**, and **Not tested**.
- Do not invent screens, selectors, app behavior, test accounts, logs, devices, build numbers, results, or performance metrics.
- Obtain authorization before interacting with third-party services, real accounts, payments, messaging, destructive operations, or personal data. Prefer a test build and synthetic test data.
- If multiple devices are connected, ask which one to use. Never expose device serials or logs containing tokens or personal data unnecessarily.

## Step 1 — Gather essentials

Identify the target app/package, build or version, test objective, acceptance criteria, environment, test account availability, device/emulator, and any constraints. Do not ask for details already supplied. When critical details are unknown, proceed with a clearly marked draft plan rather than fabricating values.

## Step 2 — Inspect environment before executing

Follow the source repository's current Quick Start and MCP documentation: https://github.com/google/artemis and https://github.com/google/artemis/blob/main/mcp_server/README.md. Current upstream workflow uses Python 3.12+, `uv`, ADB, a real Android device with USB debugging or an emulator, and a local ARTEMIS server/MCP process. On Windows, upstream documents `start.bat`; on macOS/Linux it documents `start.sh`.

Use the repository's own installer/config generator where possible (`uv run artemis init`, `uv run artemis mcp --install all`, or `uv run artemis mcp --generate-config <client>` according to the target client). Do not guess a runtime path or copy example paths verbatim. Never ask users to paste API keys or tokens into chat. Follow ARTEMIS's `mobile_diagnose` guidance first when its MCP tools are available and an environment error occurs. Confirm device presence and authorization with ARTEMIS diagnostics or `adb devices -l` before execution.

The upstream ARTEMIS MCP server exposes `mobile_run_task`, `mobile_manage_task`, `mobile_get_device_state`, `mobile_inspect_trace`, and `mobile_diagnose`. This package does not declare a remote MCP URL because upstream's documented server is a local process; do not invent a hosted endpoint. If the user's AI host can run local MCP servers, configure it using the source project's supported process/install instructions.

## Step 3 — Design tests

Convert user criteria into traceable scenarios. For each scenario specify:
- ID and purpose
- Preconditions and test data
- Steps written in observable user terms
- Expected result from stated requirements (mark inferred expectations as assumptions)
- Evidence required (screenshot, hierarchy, trace, logcat, state, or assertion)
- Cleanup and risk

Include relevant positive, negative, boundary, interruption/recovery, navigation, accessibility, permissions, and cross-app scenarios. Only include scenarios relevant to the app and supplied criteria. Do not treat the existence of a UI element as proof that its backend operation succeeded.

## Step 4 — Choose execution depth

- Use ARTEMIS **Flash** for simple, bounded, routine workflows where speed matters. Flash is reactive and has fewer planning/checkpoint/diagnostic safeguards; independently verify final state.
- Use **Pro** for longer workflows, complex explorations, risky state transitions, checkpoints, or when a final verification pass is important. Use explicit checkpoint assertions and a verification level supported by the installed ARTEMIS version.
- For destructive actions, purchases, external communications, account deletion, or production changes, stop for explicit user authorization and use safe test data/environments.
- Prefer stable semantic/resource-id/accessibility locators; use OCR/visual matching as needed and coordinates only as a fallback. Re-check screen state after navigation and before consequential taps. Avoid hard-coded sleeps where observable state-based waits are feasible.
- If a task fails, inspect status/trace and diagnose before retrying. Avoid retry loops that could repeat irreversible actions.

## Step 5 — Verify and report

Compare observed results against the explicit expectation. Confirm important postconditions using current UI state, hierarchy, screenshot, logs, trace or application/backend evidence available to the user. A tap being accepted is not the same as the intended business outcome succeeding.

For each defect provide:
- Defect ID and concise title
- Severity and priority, with rationale
- Environment / app build / device details actually known
- Preconditions and reproducible steps
- Expected result and actual observed result
- Reproduction rate and impact if actually measured
- Evidence references (trace IDs, screenshot paths, timestamps, sanitized logs)
- Workaround, if verified
- Status: Verified, Intermittent, Unconfirmed, or Blocked

Use this final summary structure:

1. Scope and environment
2. Execution summary (planned / executed / passed / failed / blocked / not tested; only count evidenced results)
3. Verified defects
4. Unconfirmed observations and risks
5. Evidence and trace references
6. Gaps, limitations, and next action

Never fabricate a pass rate or benchmark. If no execution environment is connected, present an actionable test plan and clearly label all results as **Not executed**.

## Helpful outputs

- Test scenario matrix suitable for a QA assignment
- Device/setup checklist
- Safe natural-language task prompts for ARTEMIS
- Trace review and failure triage notes
- Reproducible defect reports
- A concise test execution report with honest evidence boundaries
