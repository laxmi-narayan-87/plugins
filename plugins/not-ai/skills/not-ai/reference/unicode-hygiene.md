# Unicode hygiene

Invisible or unusual Unicode can distort tokenization and simple counts. Its presence is an encoding fact, not evidence of authorship or intent. Do not insert zero-width characters to influence detectors. Inspect suspicious characters and normalize only an analysis copy; preserve the source text unless the writer requests a correction.
