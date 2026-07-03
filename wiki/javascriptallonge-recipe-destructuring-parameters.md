---
page_id: javascriptallonge-recipe-destructuring-parameters
page_kind: recipe
page_family: recipe-pattern
summary: destructuring parameters: reusable source-backed pattern with 3 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: destructuring-parameters
projection_coverage: recipe-javascriptallonge-recipe-destructuring-parameters@ffe86c26758a08971b881c13329ea4ad
---

# destructuring parameters

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-parameters-6cd226a5]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-7239e085-00878))_
- This is very useful indeed, and we'll see more of it in a moment. _(javascriptallonge.pdf (source-range-7239e085-00880))_
- 59 Gathering in parameters has a long history, and the usual terms are to call gathering 'pattern matching' and to call a name that is bound to gathered values a 'rest parameter.' The term 'rest' is perfectly compatible with gather: 'Rest' is the noun, and 'gather' is the verb. _(javascriptallonge.pdf (source-range-7239e085-00881))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00875)_

```
foo()
bar("smaug")
baz(1, 2, 3)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00877)_

```
const foo = () => ...
const bar = (name) => ...
const baz = (a, b, c) => ...
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00879)_

```
const numbers = (...nums) => nums;
numbers(1, 2, 3, 4, 5)
//=> [1,2,3,4,5]
const headAndTail = (head, ...tail) => [head, tail];
headAndTail(1, 2, 3, 4, 5)
//=> [1,[2,3,4,5]]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-parameters-6cd226a5]]
