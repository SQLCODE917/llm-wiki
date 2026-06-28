---
page_id: javascriptallonge-directly
page_kind: concept
summary: Directly: 4 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-directly@9f8ad501c7df67decb677f9e793a1135
---

# Directly

What [[javascriptallonge]] covers about directly:

## Statements

### linear recursion

- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-31a4cf47-00923))_

### a return to backward thinking

- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-31a4cf47-01422))_

### iterables

- The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable: _(javascriptallonge.pdf (source-range-31a4cf47-01562))_

### rewriting iterable operations

- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-31a4cf47-01757))_


## Technical atoms

### Technical frame 1: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01564))_

> As we can see, we can use for...of with linked lists just as easily as with stacks. And there's one more thing: You recall that the spread operator ( ... ) can spread the elements of an array in an array literal or as parameters in a function invocation.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01563))_

```
const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, [Symbol.iterator] () { let currentPair = this ; return { next () { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.first; currentPair = currentPair.rest; return {done: false , value} } } } } }); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ? EMPTY : Pair1(first, list(...rest)) } const someSquares = list(1, 4, 9, 16, 25); iterableSum(someSquares) //=> 55
```

### Technical frame 2: rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01757))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01758))_

```
const first = (iterable) => iterable[Symbol.iterator]().next().value; function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next(); yield * iterator; }
```


## Related pages

- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from rewriting iterable operations: first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:; Iterator shares technical record from iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from iterables: The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterato ... [truncated]; Object shares technical record from iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (1 shared atom(s))
- [[javascriptallonge-symbol]] - shared technical atoms: Symbol shares technical record from iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (1 shared atom(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from a return to backward thinking: Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. (1 shared statement(s))
- [[javascriptallonge-important]] - shared statements: Important shares source evidence from linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from a return to backward thinking: Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. (1 shared statement(s))
- [[javascriptallonge-pass]] - shared statements: Pass shares source evidence from a return to backward thinking: Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
