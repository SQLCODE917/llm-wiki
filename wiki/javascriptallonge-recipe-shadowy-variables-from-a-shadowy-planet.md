---
page_id: javascriptallonge-recipe-shadowy-variables-from-a-shadowy-planet
page_kind: recipe
page_family: recipe-pattern
summary: shadowy variables from a shadowy planet: reusable source-backed pattern with 6 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: shadowy-variables-from-a-shadowy-planet
projection_coverage: recipe-javascriptallonge-recipe-shadowy-variables-from-a-shadowy-planet@e2891bd4909da43573acb88b56a5bfdc
---

# shadowy variables from a shadowy planet

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-closures-and-scope-shadowy-variables-from-a-shadowy-planet-1dde456f]].
- Evidence roles: decision, example.

## Applicability And Rationale

- An interesting thing happens when a variable has the same name as an ancestor environment's variable. _(javascriptallonge.pdf (source-range-7239e085-00371))_
- Although its parent also defines an x , it is ignored when evaluating x + y . _(javascriptallonge.pdf (source-range-7239e085-00373))_
- The x in the great-great-grandparent scope is ignored, as are both w s. _(javascriptallonge.pdf (source-range-7239e085-00375))_
- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. _(javascriptallonge.pdf (source-range-7239e085-00375))_
- When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-7239e085-00375))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-7239e085-00376))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00372)_

```
(x) =>
(x, y) => x + y
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00374)_

```
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-closures-and-scope-shadowy-variables-from-a-shadowy-planet-1dde456f]]
