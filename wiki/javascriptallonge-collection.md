---
page_id: javascriptallonge-collection
page_kind: concept
summary: Collection: 7 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-collection@445f2988ffa8b13101f8a9f1c3e2c61a
---

# Collection

What [[javascriptallonge]] covers about collection:

## Statements

- Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-83ecb080-02365))_
- This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. _(javascriptallonge.pdf (source-range-83ecb080-02742))_
- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-83ecb080-02801))_
- It isn’t a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-83ecb080-03042))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02389))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02390))_

> **let** eachIteration, sum = 0;

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02391))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02447))_

> Iterables needn’t represent finite collections:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02448))_

> **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02449))_

> There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02452))_

> ['all the numbers', ...Numbers] _//=> infinite loop!_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02457))_

> The iterables we’re discussing represent _ordered collections_ . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02458))_

> **const** abc = ["a", "b", "c"];

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02475))_

> Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02476))_

> **const** Evens = mapWith((x) => 2 * x, Numbers);

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02484))_

> Mind you, we can also map non-collection iterables, like RandomNumbers:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02485))_

> **const** ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers);

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02497))_

> And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02499))_

> [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] [...UpTo1000] _//=>_ [1,81,121,361,441,841,961]

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02508))_

> One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in Array class already has one:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02509))_

> Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_


## Related pages

- [[javascriptallonge-object]] - shared statements and technical atoms (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterable]] - shared technical atoms (5 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms (4 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms (4 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-program]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
