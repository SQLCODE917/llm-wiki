---
page_id: javascriptallonge-section-shadowy-variables-from-a-shadowy-planet-f30dadf2
page_kind: source
summary: shadowy variables from a shadowy planet: 8 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-shadowy-variables-from-a-shadowy-planet-f30dadf2@37960eff57d59ec94fbf66ea6a049b1d
---

# shadowy variables from a shadowy planet

From [[javascriptallonge]].

## Statements

- An interesting thing happens when a variable has the same name as an ancestor environment's variable. Consider: _(javascriptallonge.pdf (source-range-31a4cf47-00374))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of: _(javascriptallonge.pdf (source-range-31a4cf47-00376))_
- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-31a4cf47-00378))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-31a4cf47-00379))_

## Technical atoms

### Technical frame 1: shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00376))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00375))_

```
(x) => (x, y) => x + y
```

### Technical frame 2: shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00378))_

> When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00377))_

```
(x) => (x, y) => (w, z) => (w) => x + y + z
```
