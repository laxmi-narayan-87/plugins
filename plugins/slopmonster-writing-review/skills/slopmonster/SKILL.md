---
name: slopmonster-review
description: Use when a user wants to humanize, de-slop, review, or improve English writing for AI-like patterns, clarity, audience fit, or factual integrity.
---

# SlopMonster Writing Review

Use this workflow for English drafts such as READMEs, landing pages, emails, scripts, product copy, and documentation. It is inspired by the public SlopMonster project: https://github.com/ItsssssJack/SlopMonster.

## Scope and transparency

This skill provides a conversational editorial review. It does **not** execute the repository's Python checker, regex patterns, CLI scripts, local files, or rival-model CLI. Do not claim to have run its score or an independent-model pass unless a tool actually ran it. When exact automated scoring is needed, direct the user to the repository's documented `python3 tools/deslop.py <file>` workflow.

A clean score in the original tool means no scored pattern matched; it does not establish human authorship, factual correctness, or good writing. The rule system is English-focused, may flag normal wording, may miss problematic copy, and cannot verify claims.

## Step 1: Establish context

Use the supplied brief and the draft to identify:
- intended reader and purpose;
- format and publishing context;
- required voice, key facts, terms, links, and constraints.

Ask a concise question only when missing context would materially change the rewrite. Otherwise state reasonable assumptions and proceed.

## Step 2: Review five pattern categories

Inspect the copy for the following groups. Treat these as prompts for editorial judgment, not proof of AI authorship.

1. **Vocabulary:** promotional or vague terms such as “delve,” “tapestry,” “seamless,” “robust,” “unlock,” “game-changing,” “revolutionary,” “holistic,” “ever-evolving,” “cutting-edge,” “leverage,” “empower,” and “world-class.” Keep terms when their literal or technical meaning is necessary. Prefer concrete descriptions of what happens.
2. **Sentence patterns:** empty contrasts (“not just X, but Y”), “more than just,” generic audience pairings, “that's where X comes in,” “say goodbye to,” repeated hooks, self-answering questions, and redundant hedging. Remove only what is unnecessary; retain useful qualifications and uncertainty.
3. **Punctuation cadence:** clusters of em dashes, excessive semicolons, or repeated hyphenated compounds that interrupt readability. Punctuation is not inherently wrong.
4. **Three-item-list rhythm:** promotional triads such as “faster, smarter, better.” Keep lists when each item adds useful information; never force fragments or change list length merely to dodge a heuristic.
5. **Possible unsupported proof:** figures placed near words such as “users” or “customers,” or other claims that imply evidence. These patterns cannot verify proof. Do not create or embellish metrics, testimonials, rankings, dates, specifications, or outcomes.

## Step 3: Edit in the right order

1. Lead with the reader's actual question or need. Avoid vague hooks that delay the explanation.
2. Improve structure and progression. Each sentence should answer a question, add information, explain a consequence, or provide a useful example. Remove duplicated points and repeated metaphors.
3. Make wording direct and specific. Use natural sentence-length variation; contractions are fine where suitable.
4. Preserve the author's meaning, supported facts, technical behavior, commands, links, and position. Do not add a personal anecdote, typo, fake opinion, artificial fragment, or arbitrary quota of short sentences to simulate humanity.
5. If a necessary detail lacks evidence, keep the supplied wording carefully qualified or flag it as `[needs verification]`. Do not silently fill the gap.
6. Review tone for the intended format. A README should explain the project and usage early; an email should make its purpose clear; sales copy should make supported benefits concrete without exaggeration.

## Step 4: Fact-preserving comparison

After rewriting, compare the new copy to the original. Check that:
- claims, quantities, dates, names, product behavior, command syntax, URLs, and placeholders have not changed accidentally;
- caveats and uncertainty remain where needed;
- no new evidence or promises appeared;
- the opening explains rather than merely teases;
- the new wording suits the audience and author's voice.

List any unresolved evidence needs or meaningful tradeoffs. Be candid about anything that could not be verified.

## Step 5: Recheck and report accurately

If the user supplied output from the actual checker, review it directly. If no execution tool is available, perform a manual heuristic pass and label it **manual review**, not a SlopMonster CLI score. Never invent a score such as 5/5.

The original repository documents these commands for the user to run locally:

```bash
python3 tools/deslop.py draft.md
python3 tools/deslop.py --text "paste a draft"
python3 tools/test_deslop.py
```

It also documents an optional edit pass using a different model family via `tools/cleanse.sh`, provided that CLI is installed and authenticated. A different model is not a guarantee of better writing. Unless actually invoked and verified in the current environment, state that a second-model pass was not completed.

## Output format

Return the revised copy first when the user asks for a rewrite. Then provide up to five short notes about the substantive edits. State whether the review was manual or the actual checker was run; identify remaining findings and claims requiring evidence. Never claim that copy has been proven to be human-written.
