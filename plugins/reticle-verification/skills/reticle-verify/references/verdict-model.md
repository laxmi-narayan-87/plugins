# Reticle verdict model

Use the actual structured response from the current Reticle tool; do not synthesize a verdict.

- `yes`: evidence supports the declared expectation.
- `no`: evidence contradicts the expectation or the observed behavior failed the check.
- `unknown`: available evidence cannot establish the expectation.
- `no-fault`: no declared expectation or fault was established. It is not evidence that the feature works.

A setup check is not a behavior verdict. An observation is evidence about activity, not by itself proof of a required outcome. State the difference clearly in reports.
