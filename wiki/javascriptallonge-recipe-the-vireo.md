---
page_id: javascriptallonge-recipe-the-vireo
page_kind: recipe
page_family: recipe-pattern
summary: the vireo: reusable source-backed pattern with 5 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-vireo
projection_coverage: recipe-javascriptallonge-recipe-the-vireo@744a73210894dd7cfab4c659268e8d0c
---

# the vireo

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-vireo-6fe9a149]].
- Evidence roles: decision, example, structured-state.

## Applicability And Rationale

- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-7239e085-01364))_
- For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function: _(javascriptallonge.pdf (source-range-7239e085-01367))_
- It is known to most programmers as .tap . _(javascriptallonge.pdf (source-range-7239e085-01374))_
- One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. _(javascriptallonge.pdf (source-range-7239e085-01374))_
- It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-7239e085-01374))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01366)_

```
(first, second) => (selector) => selector(first)(second)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01368)_

```
(first) => (second) => (selector) => selector(first)(second)
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01370)_

```
const first = K,
second = K(I),
pair = (first) => (second) => (selector) => selector(first)(second);
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01373)_

```
const first = K,
second = K(I),
pair = V;
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-vireo-6fe9a149]]
