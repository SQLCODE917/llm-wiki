---
page_id: javascriptallonge-recipe-recursive-iterators
page_kind: recipe
page_family: recipe-pattern
summary: recursive iterators: reusable source-backed pattern with 6 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: recursive-iterators
projection_coverage: recipe-javascriptallonge-recipe-recursive-iterators@132b8cb77d586f63290cb5da24f8ad84
---

# recursive iterators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-like-this-generating-iterables-recursive-iterators-7e4e68e5]].
- Evidence roles: decision, constraint, procedure, explanation, structured-state, example.

## Applicability And Rationale

- Iterators maintain state, that's what they do. _(javascriptallonge.pdf (source-range-7239e085-01637))_
- Generators have to manage the exact same amount of state, but sometimes, it's much easier to manage that state in a generator. _(javascriptallonge.pdf (source-range-7239e085-01637))_
- elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-7239e085-01638))_
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. _(javascriptallonge.pdf (source-range-7239e085-01643))_
- In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit . _(javascriptallonge.pdf (source-range-7239e085-01643))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-7239e085-01644))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01639)_

```
// Generation
const isIterable = (something) =>
!!something[Symbol.iterator];
const generate = (iterable) => {
for (let element of iterable) {
if (isIterable(element)) {
generate(element)
}
else {
console.log(element)
}
}
}
generate([1, [2, [3, 4], 5]])
//=>
1
2
3
4
5
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01642)_

```
const isIterable = (something) =>
!!something[Symbol.iterator];
const treeIterator = (iterable) => {
const iterators = [ iterable[Symbol.iterator]() ];
return () => {
while (!!iterators[0]) {
const iterationResult = iterators[0].next();
if (iterationResult.done) {
iterators.shift();
}
else if (isIterable(iterationResult.value)) {
iterators.unshift(iterationResult.value[Symbol.iterator]());
}
else {
return iterationResult.value;
}
}
return;
}
}
const i = treeIterator([1, [2, [3, 4], 5]]);
let n;
while (n = i()) {
console.log(n)
}
//=>
1
2
3
4
5
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-like-this-generating-iterables-recursive-iterators-7e4e68e5]]
