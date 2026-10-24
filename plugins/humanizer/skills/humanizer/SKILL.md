---
name: humanizer
description: |
  Rewrite AI-sounding text so it reads naturally and like the writer, without changing its meaning.
  Use when editing prose with stock AI phrasing, dramatic closers, staged openers, forced triads,
  excessive dashes, inflated claims, sales language, decorative formatting, or chatbot residue.
license: MIT
metadata:
  version: "1.0.0"
---

# Humanizer

Edit prose for human readers. Preserve the writer's meaning, voice, opinions, uncertainty, and supported facts. Do not invent details or add claims to make the writing sound more convincing. The goal is clear, natural writing, not evading AI detectors.

## Workflow

1. Read the entire text before editing. Identify repeated patterns in sentences, paragraphs, and structure.
2. Draft a rewrite that states the point directly. Keep supported claims, names, numbers, dates, quotations, links, and citations. Do not add factual details not present in the source or supplied by the user.
3. Match the voice of the text. When the user supplies a writing sample, follow its rhythm, word choice, punctuation, and quirks. Personal writing can keep humor, asides, mixed feelings, and uncertainty. Technical, reference, legal, and factual prose should remain neutral and precise.
4. Compare the draft with the source. Check for added or omitted claims, numbers, dates, names, quotes, citations, rankings, or implications. Re-scan for common AI writing patterns.
5. Return the result in the format appropriate to the task.

## Patterns to review

### Staging instead of stating
- **Empty contrasts:** “It's not just X, it's Y” and similar constructions. Remove the negative half unless it corrects a real misconception or adds information.
- **Dramatic closers:** A standalone sentence that merely repeats the preceding paragraph, such as “That is the real win.” Cut it unless it adds a new fact or consequence.
- **Pseudo-profound sayings:** Phrases such as “at its core,” “the real question,” or abstract metaphors that replace a specific point. State the point directly.
- **Staged openers:** “Let's dive in,” “Here's the thing,” and similar announcements before a routine point. Start with the point.
- **Imaginary objections:** “I'm not saying X,” “Don't get me wrong,” or alternatives no one raised. Remove the defensive framing while keeping any real claim.

### Rhythm and phrasing by rule
- **Forced triads:** Keep three items only when the meaning needs all three.
- **Repeated sentence openings:** Vary or combine repeated openings when they sound mechanical; preserve deliberate rhetorical repetition.
- **Excessive dashes:** Do not use em or en dashes as universal connectors. Prefer a comma, colon, period, parentheses, or a rewritten sentence. Follow the writer's sample when it uses dashes naturally. Never alter dashes inside code, commands, paths, or URLs.
- **Stacked qualifiers:** Remove redundant hedges, but preserve genuine uncertainty and necessary scope limits.
- **Hyphenated pairs:** Avoid unnecessary compound modifiers, especially after the noun, while respecting standard spelling.
- **Hidden actors:** Prefer active voice when it makes responsibility and action clearer.

### Inflation and borrowed authority
- Replace stock AI vocabulary when a simpler word works, including “delve,” “pivotal,” “testament,” “landscape” used abstractly, “showcase,” and “underscore.” Do not ban words where they are precise or natural.
- Remove inflated significance, generic “future looks bright” claims, and formulaic “challenges and outlook” endings. End on a concrete fact.
- Specify relationships when the source supports them. Do not infer titles, roles, or associations.
- Remove unsupported “experts say” claims or lists of prestigious publications when they add no evidence.
- Prefer simple verbs such as “is,” “are,” and “has” over inflated alternatives when accurate.

### Formatting
- Remove bold used only as decoration. Do not mechanically turn every list item into a bold label and explanation.
- Use sentence case for headings where appropriate. Remove decorative emoji and arrows from formal prose unless they fit the writer and audience.
- Preserve quotations as written when their exact style matters; otherwise match the target format consistently.

### Chat and draft residue
- Remove chatbot wrappers such as “Great question,” “I hope this helps,” and offers to continue when the text is meant to stand alone.
- Do not add knowledge-cutoff disclaimers or speculative guesses. State what the evidence does and does not establish.
- Do not repeat a heading in the first sentence beneath it.
- Write about the subject, not the document or editing process, unless the document is specifically about revisions or methodology.
- In a reply or thread, assume the reader knows the context already. Lead with the decision or answer and include only reasoning that changes the reader's understanding.

## When not to edit

A watched phrase is not automatically wrong. Leave it alone when it appears in a quotation, title, proper name, or discussion of the phrase itself. A single dash, formal word, triad, or repeated opening may be deliberate. Evaluate patterns in context instead of applying a mechanical ban. Preserve specific details, authentic quirks, slang, unusual observations, and unresolved tension when they belong to the writer.

## Output modes

- **Pasted text (default):** Return the rewrite, a brief note on the main patterns corrected, and the final version. Keep the explanation short.
- **File mode:** If asked to edit a file, change prose only. Preserve code, inline code, commands, paths, YAML/frontmatter, structured data, and link targets. Write only the final prose to the file, then summarize the edits.
- **Embedded mode:** If rewriting text as part of another task, such as a pull request, commit message, or document, return only the final text unless the user asks for explanation.

Humanize for people, not for AI detectors. Detector evasion is not a goal and must not be promised.

## Source

This approach is informed by Wikipedia's “Signs of AI writing”: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
