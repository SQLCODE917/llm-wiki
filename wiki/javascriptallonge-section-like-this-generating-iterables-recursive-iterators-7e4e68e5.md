---
page_id: javascriptallonge-section-like-this-generating-iterables-recursive-iterators-7e4e68e5
page_kind: source
summary: Like this: / Generating Iterables / recursive iterators: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-like-this-generating-iterables-recursive-iterators-7e4e68e5@8e07f07268bbf69a8d571965052d157f
---

# Like this: / Generating Iterables / recursive iterators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-like-this-generating-iterables-283d51ed]] - broader source section: Like this: / Generating Iterables

## Statements

- Iterators maintain state, that's what they do. Generators have to manage the exact same amount of state, but sometimes, it's much easier to manage that state in a generator. One of those cases is when we have to recursively enumerate something. _(javascriptallonge.pdf (source-range-7239e085-01637))_
- For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-7239e085-01638))_
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit . _(javascriptallonge.pdf (source-range-7239e085-01643))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-7239e085-01644))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-7239e085-01644))_

## Technical atoms

### Technical frame 1: Like this: / Generating Iterables / recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01638))_

> For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01637))_

> One of those cases is when we have to recursively enumerate something.

### Technical frame 2: Like this: / Generating Iterables / recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01643))_

> If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01639))_

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

### Technical frame 3: Like this: / Generating Iterables / recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01643))_

> If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01642))_

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
