---
page_id: javascriptallonge-section-composing-and-decomposing-data-mutation-mutation-and-data-structures-5828e27e
page_kind: source
summary: Composing and Decomposing Data / Mutation / mutation and data structures: 12 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-mutation-mutation-and-data-structures-5828e27e@ed7c13dd309ab9371574b474cd621ff4
---

# Composing and Decomposing Data / Mutation / mutation and data structures

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-mutation-d77e57e8]] - broader source section: Composing and Decomposing Data / Mutation

## Statements

- Mutation is a surprisingly complex subject. It is possible to compute anything without ever mutating an existing entity. Languages like Haskell 70 don't permit mutation at all. In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-7239e085-01142))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-7239e085-01143))_
- The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. ' _(javascriptallonge.pdf (source-range-7239e085-01150))_
- So back to avoiding mutation. In general, it's easier to reason about data that doesn't change. We don't have to remember to use copying operations when we pass it as a value to a function, or extract some data from it. We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be 'safe.' _(javascriptallonge.pdf (source-range-7239e085-01151))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01144))_

> But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:

### Technical frame 2: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01146))_

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

### Technical frame 3: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01148))_

```
const OneToFive = [1, 2, 3, 4, 5];
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] = OneToFive;
```

### Technical frame 4: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01149))_

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

### Technical frame 5: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01151))_

> We don't have to remember to use copying operations when we pass it as a value to a function, or extract some data from it.
