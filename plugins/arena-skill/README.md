# Arena Skill plugin package

This is a skills-only plugin adaptation of [Jakeschincariol/arena-skill](https://github.com/Jakeschincariol/arena-skill), licensed MIT. It includes an Arena workflow skill plus rubric and strategy resources. The original repository's Python bracket planner is not included in this minimal account-plugin package because the Skill-only workflow here does not assume a local process runner. A full clone of the original executable project remains available from the source repository.

The workflow requires a host-provided sub-agent capability for a true independent tournament. Where that capability is absent, the skill explicitly falls back to a clearly labelled manual comparison instead of pretending to spawn agents.
