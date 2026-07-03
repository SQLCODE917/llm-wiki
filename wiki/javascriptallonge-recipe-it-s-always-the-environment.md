---
page_id: javascriptallonge-recipe-it-s-always-the-environment
page_kind: recipe
page_family: recipe-pattern
summary: it's always the environment: reusable source-backed pattern with 8 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: it-s-always-the-environment
projection_coverage: recipe-javascriptallonge-recipe-it-s-always-the-environment@d32cf7bac7ebf14fd3a63c2904345a4f
---

# it's always the environment

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-closures-and-scope-it-s-always-the-environment-47a785c5]].
- Evidence roles: decision, explanation, constraint, structured-state, example.

## Applicability And Rationale

- As we've said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-7239e085-00355))_
- We also hand-waved something when describing our environment. _(javascriptallonge.pdf (source-range-7239e085-00355))_
- To understand how closures are evaluated, we need to revisit environments. _(javascriptallonge.pdf (source-range-7239e085-00355))_
- Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. _(javascriptallonge.pdf (source-range-7239e085-00358))_
- The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) . _(javascriptallonge.pdf (source-range-7239e085-00365))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-7239e085-00366))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00360)_

```
bh
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00362)_

```
(x) =>
(y) =>
(z) => x + y + z
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00364)_

```
(x, y, z) => x + y + z
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00367)_

```
ah
bh
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-closures-and-scope-it-s-always-the-environment-47a785c5]]
