---
name: security-finding-triage
description: Use when evaluating an existing vulnerability report, scanner alert, researcher claim, or suspected bug and deciding whether the available evidence substantiates it.
---

# Evidence-based finding triage

For each supplied finding, decide what source evidence supports, contradicts, or leaves unresolved. Do not treat a scanner label, severity, or report text as proof.

1. Identify the affected component, version/commit, deployment context, claim, attacker starting privilege, and stated impact.
2. Trace the claimed input/control from the entry point to the sensitive sink. Check guards, authorization decisions, validation/canonicalization, error paths, and relevant call sites.
3. Evaluate prerequisites and trust boundaries. Separate the ability to trigger a path from the ability to cross a security boundary. Identify whether the claim relies on already having equivalent privileges.
4. Assign a verdict: **supported**, **partially supported**, **not supported by available evidence**, or **inconclusive**. Define the verdict based on evidence, not confidence theater.
5. Explain why, with file/symbol and line references only when available. Include the minimum additional test, configuration fact, trace, or reproduction needed to resolve gaps.
6. Reassess severity in context; explain practical impact and required attacker access. Do not assert a formal CVSS score unless the vector and calculation are provided.
7. Recommend a minimal fix and regression test only when the evidence supports them. Avoid exploit chains beyond what is necessary to demonstrate the claim on an authorized target.
8. Never publish sensitive vulnerability details, credentials, customer data, or exploit PoCs for an unpatched third-party issue. Follow the affected project's coordinated disclosure policy.

End with concise evidence, uncertainty, severity rationale, and remediation/next validation step. Static analysis alone must not be described as dynamic validation.
