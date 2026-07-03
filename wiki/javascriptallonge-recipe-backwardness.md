---
page_id: javascriptallonge-recipe-backwardness
page_kind: recipe
page_family: recipe-pattern
summary: backwardness: reusable source-backed pattern with 4 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: backwardness
projection_coverage: recipe-javascriptallonge-recipe-backwardness@098c3d73d80ad830ff039b97e09a52b8
---

# backwardness

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-backwardness-d9db07eb]].
- Evidence roles: decision, procedure, example.

## Applicability And Rationale

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-7239e085-01354))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-7239e085-01358))_
- So if we wanted to use them with a two-element array, we'd need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-7239e085-01359))_
- Our latin data structure is no longer a dumb data structure, it's a function. _(javascriptallonge.pdf (source-range-7239e085-01362))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01355)_

```
const first = ([first, second]) => first,
second = ([first, second]) => second;
const latin = ["primus", "secundus"];
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01357)_

```
const first = ({first, second}) => first,
second = ({first, second}) => second;
const latin = {first: "primus", second: "secundus"};
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01361)_

```
const first = K,
second = K(I);
const latin = (selector) => selector("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-backwardness-d9db07eb]]
