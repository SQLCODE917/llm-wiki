---
page_id: javascriptallonge-section-values-are-expressions-closures-and-scope-shadowy-variables-from-a-shadowy-planet-e2e09ba7
page_kind: source
summary: values are expressions / Closures and Scope / shadowy variables from a shadowy planet: 7 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-closures-and-scope-shadowy-variables-from-a-shadowy-planet-e2e09ba7@43fa89dcd41e93f35b6603a956a2e39a
---

# values are expressions / Closures and Scope / shadowy variables from a shadowy planet

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-closures-and-scope-27942b9b]] - broader source section

## Statements

- An interesting thing happens when a variable has the same name as an ancestor environment’s variable. _(javascriptallonge.pdf (source-range-83ecb080-00411))_
- Although its parent also defines an x, it is ignored when evaluating x + y. _(javascriptallonge.pdf (source-range-83ecb080-00413))_
- When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. _(javascriptallonge.pdf (source-range-83ecb080-00414))_
- When a variable has the same name as an ancestor environment’s binding, it is said to _shadow_ the ancestor. _(javascriptallonge.pdf (source-range-83ecb080-00414))_
- The x in the great-great-grandparent scope is ignored, as are both ws. _(javascriptallonge.pdf (source-range-83ecb080-00414))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-83ecb080-00415))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00411, source-range-83ecb080-00413))_

> An interesting thing happens when a variable has the same name as an ancestor environment’s variable. Consider: The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of: (x) => (x, y) => (w, z) => (w) => x + y + z

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00412))_

> - (x) => (x, y) => x + y
