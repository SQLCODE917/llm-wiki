---
page_id: javascriptallonge-mutation
page_kind: concept
page_family: topic-concept
summary: Mutation: 3 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-mutation@c82a70df4fd9607ea46420b49bd08880
---

# Mutation

What [[javascriptallonge]] covers about mutation:

## Statements

### Composing and Decomposing Data / Mutation / mutation and data structures

- Mutation is a surprisingly complex subject. It is possible to compute anything without ever mutating an existing entity. Languages like Haskell 70 don't permit mutation at all. In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-7239e085-01142))_

- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-7239e085-01143))_


## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01146))_

<a id="atom-technical-atom-0e73d044bed5ab75"></a>

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


## Related pages

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-mutation-d77e57e8]] - source section: Composing and Decomposing Data / Mutation shares source evidence from Composing and Decomposing Data / Mutation: In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall t ... [truncated]; Composing and Decomposing Data / Mutation shares technical record from Composing and Decomposing Data / Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (25 shared statement(s), 15 shared atom(s))

### Shared claims

- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from Composing and Decomposing Data / Mutation / mutation and data structures: One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists f ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Composing and Decomposing Data / Mutation / mutation and data structures: One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists f ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
