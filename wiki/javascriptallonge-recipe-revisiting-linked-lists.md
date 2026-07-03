---
page_id: javascriptallonge-recipe-revisiting-linked-lists
page_kind: recipe
page_family: recipe-pattern
summary: revisiting linked lists: reusable source-backed pattern with 12 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: revisiting-linked-lists
projection_coverage: recipe-javascriptallonge-recipe-revisiting-linked-lists@dcbe69a6cd7d8fcce2d1e4e1672d288a
---

# revisiting linked lists

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-revisiting-linked-lists-e7d9bd1d]].
- Evidence roles: decision, constraint, procedure, explanation, example.

## Applicability And Rationale

- But now that we've looked at objects, we can use an object instead of a two-element array. _(javascriptallonge.pdf (source-range-7239e085-01106))_
- In essence, this simple implementation used functions to create an abstraction with named elements. _(javascriptallonge.pdf (source-range-7239e085-01106))_
- As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. _(javascriptallonge.pdf (source-range-7239e085-01109))_
- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. _(javascriptallonge.pdf (source-range-7239e085-01111))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-7239e085-01111))_
- We could follow the strategy of delaying the work. _(javascriptallonge.pdf (source-range-7239e085-01112))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01105)_

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01107)_

```
In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first:
2, rest: { first: 3, rest: EMPTY } } }.
We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01108)_

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest
//=> {"first":2,"rest":{"first":3,"rest":{}}}
OneTwoThree.rest.rest.first
//=> 3
Taking the length of a linked list is easy:
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01110)_

```
const slowcopy = (node) =>
node === EMPTY
? EMPTY
: { first: node.first, rest: slowcopy(node.rest)};
slowcopy(OneTwoThree)
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{}}}}
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01113)_

```
const copy2 = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: copy2(node.rest, { first: node.first, rest: delayed });
copy2(OneTwoThree)
//=> {"first":3,"rest":{"first":2,"rest":{"first":1,"rest":{}}}}
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01115)_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
And now, we can make a reversing map:
const reverseMapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
reverseMapWith((x) => x * x, OneTwoThree)
//=> {"first":9,"rest":{"first":4,"rest":{"first":1,"rest":{}}}}
And a regular mapWith follows:
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const mapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? reverse(delayed)
: mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
mapWith((x) => x * x, OneTwoThree)
//=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-revisiting-linked-lists-e7d9bd1d]]
