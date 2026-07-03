---
page_id: javascriptallonge-recipe-the-function-keyword-5d8f2243
page_kind: recipe
page_family: recipe-pattern
summary: the function keyword: reusable source-backed pattern with 16 statement(s) and 13 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-function-keyword
projection_coverage: recipe-javascriptallonge-recipe-the-function-keyword-5d8f2243@1f767f7492eabf5392a91a1fb1a9a7fc
---

# the function keyword

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-naming-functions-the-function-keyword-5d8f2243]].
- Evidence roles: decision, definition, constraint, explanation, procedure, example.

## Applicability And Rationale

- JavaScript does have a syntax for naming a function, we use the function keyword. _(javascriptallonge.pdf (source-range-7239e085-00503))_
- Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-7239e085-00503))_
- - Something else we're about to discuss is optional. _(javascriptallonge.pdf (source-range-7239e085-00510))_
- - We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-7239e085-00511))_
- - We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-7239e085-00512))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-7239e085-00513))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00505)_

```
(str) => str + str
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00507)_

```
function (str) { return str + str }
```

### Atom 3: `worked-example`

_Source: javascriptallonge.pdf (source-range-7239e085-00514)_

```
If we leave out the 'something optional' that comes after the function keyword, we can translate all of the fat arrow functions that we've seen into function keyword functions, e.g.
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00515)_

```
(n) => (1.618**n - -1.618**-n) / 2.236
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00517)_

```
function (n) {
return (1.618**n - -1.618**-n) / 2.236;
}
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00520)_

```
const repeat = function repeat (str) {
return str + str;
};
const fib = function fib (n) {
return (1.618**n - -1.618**-n) / 2.236;
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-naming-functions-the-function-keyword-5d8f2243]]
