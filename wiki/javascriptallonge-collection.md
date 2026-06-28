---
page_id: javascriptallonge-collection
page_kind: concept
summary: Collection: 7 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-collection@d7f7cffee3dde1e5e5a5d63a02988e19
---

# Collection

What [[javascriptallonge]] covers about collection:

## Statements

### Iteration and Iterables

- All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-31a4cf47-01530))_

### iterator objects

- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-31a4cf47-01547))_

### iterables

- One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-31a4cf47-01570))_

### Lazy and Eager Collections

- Over time, this informal 'interface' for collections grows by accretion. Some methods are only added to a few collections, some are added to all. But our objects grow fatter and fatter. We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-31a4cf47-01766))_

- This 'fat object' style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don't need for the collection to handle every single detail. That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-31a4cf47-01768))_

### lazy collection operations

- Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-31a4cf47-01801))_

### interactive generators

- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-31a4cf47-01943))_


## Technical atoms

### Technical frame 1: lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01801))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01800))_

```
const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false , value: n++}) } } }, LazyCollection); const firstCubeOver1234 = Numbers .map((x) => x * x * x) .filter((x) => x > 1234) .first() //=> 1331
```

### Technical frame 2: interactive generators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01942))_

> Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1)

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01941))_

```
function * generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield 3; break ; case 3: const x3 = yield 8; switch (x3) { case 2: case 5: case 7: yield 4; break ; case 4: yield 7; break ;
```


## Related pages

- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from interactive generators: function * generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield ... [truncated] (1 shared atom(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Iteration and Iterables: All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and ... [truncated] (2 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from iterator objects: In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be ... [truncated] (2 shared statement(s))
- [[javascriptallonge-program]] - shared statements: Program shares source evidence from iterator objects: In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
