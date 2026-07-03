---
page_id: javascriptallonge-recipe-mutation-and-data-structures
page_kind: recipe
page_family: recipe-pattern
summary: mutation and data structures: reusable source-backed pattern with 7 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: mutation-and-data-structures
projection_coverage: recipe-javascriptallonge-recipe-mutation-and-data-structures@6178a23586bd2e78d1991d2d69a87775
---

# mutation and data structures

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-mutation-mutation-and-data-structures-5828e27e]].
- Evidence roles: decision, constraint, example, structured-state.

## Applicability And Rationale

- In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-7239e085-01142))_
- Mutation is a surprisingly complex subject. _(javascriptallonge.pdf (source-range-7239e085-01142))_
- It is possible to compute anything without ever mutating an existing entity. _(javascriptallonge.pdf (source-range-7239e085-01142))_
- While we're executing the mapWith function, we're constructing a new linked list. _(javascriptallonge.pdf (source-range-7239e085-01143))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. _(javascriptallonge.pdf (source-range-7239e085-01143))_
- The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. _(javascriptallonge.pdf (source-range-7239e085-01150))_

## Technical Atoms

### Atom 1: `worked-example`

_Source: javascriptallonge.pdf (source-range-7239e085-01144)_

```
But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01146)_

```
const EMPTY = {};
const OneToFive = { first: 1,
rest: {
first: 2,
rest: {
first: 3,
rest: {
first: 4,
rest: {
first: 5,
rest: EMPTY } } } } };
OneToFive
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\
r","rest":{"first":"five","rest":{}}}}}}
const ThreeToFive = OneToFive.rest.rest;
ThreeToFive
//=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}}
ThreeToFive.first = "three";
ThreeToFive.rest.first = "four";
ThreeToFive.rest.rest.first = "five";
ThreeToFive
//=> {"first":"three","rest":{"first":"four","rest":{"first":"five","rest":{}}\
}}
OneToFive
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\
r","rest":{"first":"five","rest":{}}}}}}
Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we
wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of {"first":3,"rest":{"firs
we were getting a reference to the same chain of nodes.
Structure sharing like this is what makes linked lists so fast for taking everything but the first item
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01148)_

```
const OneToFive = [1, 2, 3, 4, 5];
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] = OneToFive;
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01149)_

```
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] =
ThreeToFive
//=> [3, 4, 5]
ThreeToFive[0] = "three";
ThreeToFive[1] = "four";
ThreeToFive[2] = "five";
ThreeToFive
//=> ["three","four","five"]
OneToFive
//=> [1,2,3,4,5]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-mutation-mutation-and-data-structures-5828e27e]]
