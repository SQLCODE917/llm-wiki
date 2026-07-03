---
page_id: javascriptallonge-recipe-the-function-keyword
page_kind: recipe
page_family: recipe-pattern
summary: the function keyword: reusable source-backed pattern with 5 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-function-keyword
projection_coverage: recipe-javascriptallonge-recipe-the-function-keyword@d8a024aeed85c2983a446e9d718d3ebe
---

# the function keyword

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-magic-names-the-function-keyword-b8eb1a25]].
- Evidence roles: decision, procedure, constraint, example, structured-state.

## Applicability And Rationale

- There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arrows.' We'll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-7239e085-00607))_
- The first magic name is this , and it is bound to something called the function's context. _(javascriptallonge.pdf (source-range-7239e085-00608))_
- The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-7239e085-00608))_
- We'll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-7239e085-00617))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. _(javascriptallonge.pdf (source-range-7239e085-00617))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00609)_

```
const plus = function (a, b) {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00611)_

```
const args = function (a, b) {
return arguments;
}
args(2,3)
//=> { '0': 2, '1': 3 }
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00614)_

```
const plus = function () {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00616)_

```
const howMany = function () {
return arguments['length'];
}
howMany()
//=> 0
howMany('hello')
//=> 1
howMany('sharks', 'are', 'apex', 'predators')
//=> 4
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-magic-names-the-function-keyword-b8eb1a25]]
