---
page_id: javascriptallonge-recipe-const-and-lexical-scope
page_kind: recipe
page_family: recipe-pattern
summary: const and lexical scope: reusable source-backed pattern with 8 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: const-and-lexical-scope
projection_coverage: recipe-javascriptallonge-recipe-const-and-lexical-scope@9d9ad12c8684fc54da4dcb6158509007
---

# const and lexical scope

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-that-constant-coffee-craving-const-and-lexical-scope-518692ba]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we're to place const anywhere we like. _(javascriptallonge.pdf (source-range-7239e085-00448))_
- It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. _(javascriptallonge.pdf (source-range-7239e085-00452))_
- We can use any expression in there, and that expression can invoke diameter_fn . _(javascriptallonge.pdf (source-range-7239e085-00452))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-7239e085-00454))_
- This is called lexical scoping 31 , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-7239e085-00455))_
- We can see that PI is bound in an environment surrounding (diameter) => diameter * PI , we don't need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-7239e085-00455))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00451)_

```
((diameter_fn) =>
// ...
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00453)_

```
((diameter_fn) =>
diameter_fn(2)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00457)_

```
((diameter_fn) =>
((PI) =>
diameter_fn(2)
)(3)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00461)_

```
((diameter_fn) => {
const PI = 3;
return diameter_fn(2)
})(
(() => {
const PI = 3.14159265;
return (diameter) => diameter * PI
})()
)
//=> 6.2831853
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-that-constant-coffee-craving-const-and-lexical-scope-518692ba]]
