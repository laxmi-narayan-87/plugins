# VibeWise Plugin for Antigravity

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **"You build. AI writes."**

**VibeWise** is an Antigravity plugin inspired by [nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise). It transforms AI coding assistance from passive generation into an active learning partnership. Instead of letting an AI agent silently generate multi-file codebases that leave you detached from your own software, VibeWise introduces structured human-in-the-loop checkpoints.

---

## Why VibeWise?

"Vibe coding" often results in working software that developers cannot explain, debug, or maintain. VibeWise restores developer agency and understanding through intentional friction:

1. **Reasoning First**: Before code is written, you reason through system behavior, data structures, and edge cases.
2. **Explicit Checkpoints**: Checkpoints gate architecture decisions and file modifications.
3. **Adaptive Scaffolding**: Calibrates explanations and question depth to your self-selected skill level (Beginner, Intermediate, Advanced).
4. **Local-First Memory**: Stores your learning progress, decisions, and system maps in `.vibe-wise/` inside your repository without cloud telemetry.

---

## The Three Gated Checkpoints

```
[1. Build Checkpoint]       --> Collaborate on logic, trade-offs, and mental models
        ↓
[2. Design Checkpoint]      --> Confirm architecture ("Confirm and continue" or "Discuss")
        ↓
[3. Implementation Gate]    --> Inspect files & diffs before authorizing ("Implement this step")
        ↓
[4. Post-Implementation]   --> Concise recap of what changed, why, and test verification
```

1. **Build Checkpoint**: You and the AI reason through the feature requirements and technical tradeoffs. Unfamiliar concepts are explained using `✦ Concept:` and `✦ Why this matters:`.
2. **Design Checkpoint**: The AI summarizes the proposed architecture. You choose **[Confirm and continue]** or **[Discuss]**. *(Design confirmation does NOT authorize file modifications.)*
3. **Implementation Checkpoint**: The AI outlines the exact files to create or modify and the logic to introduce. You must explicitly authorize execution with **[Implement this step]**.
4. **Post-Implementation Breakdown**: The AI provides a concise recap of what changed, how it connects to your design decisions, and runs verification checks.

---

## Local State (`.vibe-wise/`)

VibeWise automatically tracks context in your project repository under `.vibe-wise/`:
* `profile.md`: Your experience level and learning goals.
* `project-map.md`: System components, boundaries, and architectural patterns.
* `progress.md`: Running ledger of concepts explored, decisions confirmed, and pending choices.

---

## Included Customizations

* **Rules (`rules/AGENTS.md`)**: Always-on behavioral guidelines enforcing learner ownership, the three checkpoints, and pedagogical callouts.
* **Skill (`skills/vibe-wise/SKILL.md`)**: Interactive learning workflow manager for onboarding, checkpoint gating, and state updates.

---

## Credits

Adapted for Antigravity from the open-source project [nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise) created by Noah Kim under the MIT License.
