---
page_id: javascriptallonge-section-and-also-closures-and-scope-shadowy-variables-from-a-shadowy-planet-1dde456f
page_kind: source
page_family: section-reference
summary: And also: / Closures and Scope / shadowy variables from a shadowy planet: 8 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-closures-and-scope-shadowy-variables-from-a-shadowy-planet-1dde456f@08d9b8d9ea6d77705c0df0861c86786b
---

# And also: / Closures and Scope / shadowy variables from a shadowy planet

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-closures-and-scope-d1679ec0]] - broader source section: And also: / Closures and Scope

## Statements

- An interesting thing happens when a variable has the same name as an ancestor environment's variable. Consider: _(javascriptallonge.pdf (source-range-7239e085-00371))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of: _(javascriptallonge.pdf (source-range-7239e085-00373))_
- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-7239e085-00375))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-7239e085-00376))_
