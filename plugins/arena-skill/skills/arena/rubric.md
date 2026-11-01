# Arena judging rubric

Score each criterion from 0–10. Prefer concrete correctness and task fit over length or rhetorical confidence. Judge only evidence in the task, solution, tests, and attacks.

- **Correctness (30%)**: factual, logical, and technical accuracy; no unsupported claims.
- **Completeness (25%)**: satisfies the stated requirements and constraints; addresses important edge cases.
- **Robustness (20%)**: survives concrete counterexamples, adversarial critique, and relevant failure conditions.
- **Specificity (15%)**: actionable, checkable, sufficiently detailed for the user's purpose.
- **Clarity (10%)**: understandable and well organized without hiding caveats.

A judge sets `fatal=true` only if a verified flaw makes the solution materially wrong or unusable for the stated task. A fatal solution cannot beat a nonfatal solution. On an exact weighted-total tie, fewer standing attacks wins; if still tied, higher correctness wins. An unresolved attack should count as standing only after the judge independently verifies it.
