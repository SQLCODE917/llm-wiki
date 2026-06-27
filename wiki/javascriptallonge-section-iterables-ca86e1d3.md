---
page_id: javascriptallonge-section-iterables-ca86e1d3
page_kind: source
summary: **iterables**: 24 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-iterables-ca86e1d3@677b7e48840aa5f07868b022caa498af
---

# **iterables**

From [[javascriptallonge]].

## Statements

- Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. _(javascriptallonge.pdf (source-range-83ecb080-02412))_
- People have been writing iterators since JavaScript was first released in the late 1990s. _(javascriptallonge.pdf (source-range-83ecb080-02412))_
- So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. _(javascriptallonge.pdf (source-range-83ecb080-02413))_
- Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-83ecb080-02413))_
- Symbols are unique constants that are guaranteed not to conflict with existing strings. _(javascriptallonge.pdf (source-range-83ecb080-02414))_
- Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols.[88] _(javascriptallonge.pdf (source-range-83ecb080-02414))_
- To ensure that the method would not conflict with any existing code, JavaScript provides a _symbol_ . _(javascriptallonge.pdf (source-range-83ecb080-02414))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02415))_
- > 88 You can read more about JavaScript symbols in Axel Rauschmayer’s Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-83ecb080-02416))_
- Our stack does, so instead of binding the existing iterator method to the name iterator, we bind it to the Symbol.iterator. _(javascriptallonge.pdf (source-range-83ecb080-02419))_
- The for...of loop works directly with any object that is _iterable_ , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. _(javascriptallonge.pdf (source-range-83ecb080-02431))_
- And there’s one more thing: You recall that the spread operator (...) can spread the elements of an array in an array literal or as parameters in a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-02437))_
- Now is the time to note that we can spread any iterable. _(javascriptallonge.pdf (source-range-83ecb080-02438))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- That might be very wasteful for extremely large collections. _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- And if we have an infinite collection, spreading is going to fail outright as we’re about to see. _(javascriptallonge.pdf (source-range-83ecb080-02445))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02424))_

> **const** collectionSum = (collection) => { **const** iterator = collection[Symbol.iterator]();

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02425))_

> **let** eachIteration, sum = 0;

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02426))_

> **while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 2015_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02428))_

> Indeed we do. Behold the for...of loop:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02429))_

> **const** iterableSum = (iterable) => { **let** sum = 0;

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02438))_

> Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02439))_

> - ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02440))_

> And we can also spread the elements of an array literal into parameters:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02441))_

> **const** firstAndSecondElement = (first, second) => ({first, second})

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02440))_

> And we can also spread the elements of an array literal into parameters:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02442))_

> firstAndSecondElement(...stack) _//=> {"first":5,"second":10}_
