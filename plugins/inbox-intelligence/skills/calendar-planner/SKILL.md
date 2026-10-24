---
name: calendar-planner
description: Extract reviewable calendar candidates from inbox and placement emails, detect conflicts, plan preparation, and perform calendar actions only with explicit authorization.
---

# Inbox Intelligence V2 — Calendar Planner

Turn evidence-backed email facts into reviewable calendar candidates. Prefer the user's connected calendar service when available. Separate **Email fact → Calendar candidate → User approval → Calendar action**.

## Event types
- Assessment / Online Test
- Interview
- Recruiter / HR Call
- Meeting
- Placement Event
- College / Academic
- Deadline
- Suggested Preparation Block

## Extraction
For each candidate event extract:
- title
- company/organization
- role
- date
- start time
- end time/duration
- timezone
- location
- meeting/test link
- source email/thread
- confidence: Confirmed / Partially Confirmed / Inferred / Unknown
- preparation requirements
- related deadline

Never silently convert a deadline into an event time. If timezone is absent, use the user's configured timezone only when available; otherwise mark unknown. Never present inferred time as confirmed.

## Thread authority and updates
Use the latest explicit authoritative information from the email thread. Detect and report:
- rescheduled/postponed/cancelled events
- location changes
- meeting/test link changes
- assessment time changes
- deadline extensions/shortenings
- role or interview-round changes

When an existing planned event is changed, show previous vs new details and the source thread. Do not silently overwrite an existing calendar event.

## Conflict detection
Before proposing calendar events, check existing calendar events when calendar access is available. Detect:
- exact overlaps
- near overlaps
- multiple assessments on one day
- interview + assessment conflicts
- interview + college schedule conflicts
- insufficient travel time when physical attendance is indicated
- insufficient preparation time
- multiple deadlines on the same day

Report:
**⚠️ Calendar conflict**
- Event A: …
- Event B: …
- Conflict: …

Do not decide which event the user should prioritize. Present the facts and let the user decide.

## Preparation planning
Extract requirements such as coding, aptitude, webcam, laptop, ID proof, platform, technical round, HR round, resume, project discussion, and meeting link. When requested, propose preparation blocks. Mark every preparation block **Suggested**, not confirmed. Do not claim a preparation block is a user commitment unless explicitly approved.

## Draft vs create
- “Draft a calendar”, “prepare a calendar”, “create a calendar plan”, and “plan it” mean **planning only**.
- “Add these to my calendar” or an equivalent explicit request authorizes creation of the confirmed events in the current request.
- Before consequential calendar changes, show title, date, time, duration, location/link, source email, confidence, and any conflict.
- Never silently overwrite an existing event.
- Do not create an event simply because an email mentions a date.

## Output
| Date/time | Event | Type | Company | Source | Confidence | Action |

Then provide:
- **Conflicts**
- **Deadlines**
- **Suggested preparation blocks**
- **Calendar actions awaiting approval**

For “prepare tomorrow's schedule”, combine confirmed calendar events with evidence-backed email candidates and clearly separate confirmed events from suggestions.
