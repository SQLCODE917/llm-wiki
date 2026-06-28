---
page_id: javascriptallonge-operation
page_kind: concept
summary: Operation: 4 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-operation@e30912f4aeded095561daffa3eb192c9
---

# Operation

What [[javascriptallonge]] covers about operation:

## Statements

### Maybe

- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-31a4cf47-00708))_

### mutation and data structures

- The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. ' _(javascriptallonge.pdf (source-range-31a4cf47-01150))_

### operations on ordered collections

- Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith : _(javascriptallonge.pdf (source-range-31a4cf47-01591))_

- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-31a4cf47-01609))_


## Technical atoms

### Technical frame 1: operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01590))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01589))_

```
const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: done ? undefined : fn(value)}); } } } });
```

### Technical frame 2: operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01593))_

> Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01592))_

```
const Evens = mapWith((x) => 2 * x, Numbers); for ( const i of Evens) { console.log(i) } //=> 0 2 4 ... for ( const i of Evens) { console.log(i) } //=> 0 2 4 ...
```

### Technical frame 3: operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01603))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01602))_

```
const filterWith = (fn, iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); return { next () { do { const {done, value} = iterator.next(); } while (!done && !fn(value)); return {done, value}; } } } }); const untilWith = (fn, iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); return { next () { let {done, value} = iterator.next(); done = done || fn(value); return ({done, value: done ? undefined : value}); } } } });
```

### Technical frame 4: operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01606))_

> As we expect from an ordered collection, each time we iterate over UpTo1000 , we begin at the beginning.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01605))_

```
const Squares = mapWith((x) => x * x, Numbers); const EndWithOne = filterWith((x) => x % 10 === 1, Squares); const UpTo1000 = untilWith((x) => (x > 1000), EndWithOne); [...UpTo1000] //=> [1,81,121,361,441,841,961] [...UpTo1000] //=> [1,81,121,361,441,841,961]
```


## Related pages

- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-discussing]] - shared technical atoms: Discussing shares technical record from operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-idea]] - shared technical atoms: Idea shares technical record from operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-purpose]] - shared technical atoms: Purpose shares technical record from operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Maybe: If some code ever tries to call model.setSomething with nothing, the operation will be skipped. (1 shared statement(s))
- [[javascriptallonge-gathering]] - shared statements: Gathering shares source evidence from mutation and data structures: The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. ' (1 shared statement(s))
- [[javascriptallonge-rest]] - shared statements: Rest shares source evidence from operations on ordered collections: like our other operations, rest preserves the ordered collection semantics of its argument. (1 shared statement(s))

## Source

- [[javascriptallonge]]
