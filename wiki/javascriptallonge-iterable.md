---
page_id: javascriptallonge-iterable
page_kind: concept
summary: Iterable: 12 statement(s) and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iterable@59e9e1868508af56dbd12ca7192c306a
---

# Iterable

What [[javascriptallonge]] covers about iterable:

## Statements

- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-02501))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-83ecb080-02455))_
- The iterables we’re discussing represent _ordered collections_ . _(javascriptallonge.pdf (source-range-83ecb080-02457))_
- Iterables needn’t represent ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-02461))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- Now is the time to note that we can spread any iterable. _(javascriptallonge.pdf (source-range-83ecb080-02438))_
- There are useful things we can do with iterables representing an infinitely large collection. _(javascriptallonge.pdf (source-range-83ecb080-02449))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- For completeness, here are two more handy iterable functions. _(javascriptallonge.pdf (source-range-83ecb080-02501))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. _(javascriptallonge.pdf (source-range-83ecb080-02508))_
- This object declares a [Symbol.iterator] function that makes it iterable. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- So to summarize, ThreeNumbers is an object that we’ve made iterable, by way of writing a _generator_ method for [Symbol.iterator]. _(javascriptallonge.pdf (source-range-83ecb080-02665))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02438))_

> Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02439))_

> - ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02447))_

> Iterables needn’t represent finite collections:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02448))_

> **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02449))_

> There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02452))_

> ['all the numbers', ...Numbers] _//=> infinite loop!_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02457))_

> The iterables we’re discussing represent _ordered collections_ . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02458))_

> **const** abc = ["a", "b", "c"];

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02484))_

> Mind you, we can also map non-collection iterables, like RandomNumbers:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02485))_

> **const** ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers);

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02501))_

> For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest]:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02502))_

> **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **const** rest = (iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **return** iterator; } });

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02508))_

> One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in Array class already has one:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02509))_

> Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02658))_

> Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02656))_

> **const** iterator = ThreeNumbers[Symbol.iterator]();

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02662, source-range-83ecb080-02664))_

> generator methods for objects: This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02663))_

> **const** ThreeNumbers = { *[Symbol.iterator] () { **yield** 1; **yield** 2; **yield** 3 } }


## Related pages

- [[javascriptallonge-element]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms (5 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
