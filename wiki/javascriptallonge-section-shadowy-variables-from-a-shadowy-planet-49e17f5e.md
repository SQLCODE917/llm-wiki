---
page_id: javascriptallonge-section-shadowy-variables-from-a-shadowy-planet-49e17f5e
page_kind: source
summary: **shadowy variables from a shadowy planet**: 9 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-shadowy-variables-from-a-shadowy-planet-49e17f5e@72df7590fad7422ee5a0270851e84fee
---

# **shadowy variables from a shadowy planet**

From [[javascriptallonge]].

## Statements

- An interesting thing happens when a variable has the same name as an ancestor environment’s variable. _(javascriptallonge.pdf (source-range-83ecb080-00520))_
- Although its parent also defines an x, it is ignored when evaluating x + y. _(javascriptallonge.pdf (source-range-83ecb080-00522))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-00522))_
- When a variable has the same name as an ancestor environment’s binding, it is said to _shadow_ the ancestor. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- The x in the great-great-grandparent scope is ignored, as are both ws. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-83ecb080-00525))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00520, source-range-83ecb080-00522))_

> An interesting thing happens when a variable has the same name as an ancestor environment’s variable. Consider: The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00521))_

> - (x) => (x, y) => x + y

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00522))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00523))_

> (x) => (x, y) => (w, z) => (w) => x + y + z
