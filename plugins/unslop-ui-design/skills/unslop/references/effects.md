# Optional image treatments

Use these sparingly, only when they express the product's material or meaning. Treatments are optional; do not add motion or effects merely for decoration.

- **Glyphs:** render an image using characters drawn from the product's own domain (for example, code symbols for a developer tool or data marks for monitoring). Prepare pixel samples and glyph atlases once; never read pixels inside an animation loop.
- **Halftone:** vary dot size by brightness for an editorial/print character.
- **Dithering:** map an image to two or three colors from the page ramp; compute once at load.
- **Duotone:** map image brightness onto a page neutral and one accent.

Performance: cap device pixel ratio at 2, use 8–12 updates per second for subtle animated treatments, update only a small subset of cells, pause when off-screen, and honor reduced-motion preferences. If a treatment harms readability, performance, or product character, do not use it.

---

Part of an adaptation of unslop by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)), CC BY 4.0. Source: https://github.com/heydamir/unslop
