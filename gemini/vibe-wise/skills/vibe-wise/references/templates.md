# VibeWise State File Templates

When initializing a new workspace with VibeWise, create the `.vibe-wise/` folder and populate these templates as needed.

---

## 1. `.vibe-wise/profile.md`

```markdown
# Learner Profile

- **Experience Level**: [Beginner | Intermediate | Advanced]
- **Target Tech Stack**: [e.g., React, TypeScript, Node.js, Go]
- **Primary Learning Goals**: [e.g., Master system design, understand state management, clean architecture]
- **Explanation Preferences**: [e.g., Visual diagrams, code snippets, deep theoretical explanations]
```

---

## 2. `.vibe-wise/project-map.md`

```markdown
# Project Architecture Map

## Overview
[One-paragraph summary of what the system does]

## Key Components & Responsibilities
- `src/core/`: [Business logic and domain entities]
- `src/api/`: [Route handlers and controllers]
- `src/db/`: [Data persistence and models]

## Confirmed Architectural Decisions
- [Decision 1: e.g., Using SQLite with Drizzle ORM for local-first persistence]
- [Decision 2: e.g., Repository pattern for data access layer]
```

---

## 3. `.vibe-wise/progress.md`

```markdown
# Learning Progress & Decision Ledger

## Current Status
- **Active Task**: [Current feature or bug being addressed]
- **Active Checkpoint**: [Build | Design | Implementation | Complete]

## Decisions Made
- [Date] - [Architecture Choice]: [Short rationale]

## Concepts Explored
- [Concept Name]: [Brief summary of understanding demonstrated]

## Pending Decisions
- [ ] [Unresolved question or architectural trade-off waiting for learner input]
```
