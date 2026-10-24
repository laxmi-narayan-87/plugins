# Not Ai 3.0.1

Source-grounded writing and editing. Improve clarity, structure and usefulness while preserving facts, claims, citations, technical terms and the author's actual position.

Not Ai is not an authorship classifier or detector-bypass tool. It does not optimize detector scores or promise an outcome from any detector.

## What it supports
- Rewrite a supplied passage while preserving meaning.
- Draft from supplied notes without inventing details.
- Diagnose instead of rewriting when requested.
- Apply genre-aware guidance across 18 profiles.
- Run a portable, standard-library Python editorial gate.
- Treat all mechanical findings as prompts for human review, not proof of authorship or quality.

## Local gate
```bash
python3 tools/gate.py draft.txt --genre linkedin
python3 tools/gate.py draft.txt --genre student --json
python3 tools/gate.py draft.txt --genre technical --protect "API v2"
python3 tools/gate.py --stdin --genre email
```

The gate fails for empty output or a missing explicitly protected literal. Other findings are advisory. It is a compact portable gate included in this standalone package, not a byte-for-byte copy of the full upstream analytical core.

## Fidelity rules
Preserve numbers, negation, names, claims, time, scope, causality, uncertainty, citations and code identifiers. If detail is missing, ask or add a bracketed prompt. Never invent facts, experiences, quotes or citations.

## License and attribution
The upstream repository is MIT-licensed: https://github.com/udaysharmadev/Not-Ai . This private derivative package preserves attribution and clearly identifies the included gate as a compact portable implementation.
