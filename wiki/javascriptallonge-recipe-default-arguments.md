---
page_id: javascriptallonge-recipe-default-arguments
page_kind: recipe
page_family: recipe-pattern
summary: default arguments: reusable source-backed pattern with 5 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: default-arguments
projection_coverage: recipe-javascriptallonge-recipe-default-arguments@27eb2e2bee268859144c4a2340c49244
---

# default arguments

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-default-arguments-ec839e44]].
- Evidence roles: decision, example, structured-state.

## Applicability And Rationale

- But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) . _(javascriptallonge.pdf (source-range-7239e085-01004))_
- What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . _(javascriptallonge.pdf (source-range-7239e085-01004))_
- JavaScript provides this exact syntax, it's called a default argument , and it looks like this: _(javascriptallonge.pdf (source-range-7239e085-01005))_
- Now we don't need to use two functions. _(javascriptallonge.pdf (source-range-7239e085-01009))_
- A default argument is concise and readable. _(javascriptallonge.pdf (source-range-7239e085-01009))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01002)_

```
const factorial = (n, work) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1, 1)
//=> 1
factorial(5, 1)
//=> 120
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01006)_

```
const factorial = (n, work = 1) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1)
//=> 1
factorial(6)
//=> 720
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01008)_

```
const length = ([first, ...rest], numberToBeAdded = 0) =>
first === undefined
? numberToBeAdded
: length(rest, 1 + numberToBeAdded)
length(["foo", "bar", "baz"])
//=> 3
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-default-arguments-ec839e44]]
