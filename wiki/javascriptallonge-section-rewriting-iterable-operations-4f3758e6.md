---
page_id: javascriptallonge-section-rewriting-iterable-operations-4f3758e6
page_kind: source
summary: rewriting iterable operations: 10 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-rewriting-iterable-operations-4f3758e6@3236c4d2c2bdb6811a601c739cb98126
---

# rewriting iterable operations

From [[javascriptallonge]].

## Statements

- Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of: _(javascriptallonge.pdf (source-range-31a4cf47-01749))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done. _(javascriptallonge.pdf (source-range-31a4cf47-01753))_
- We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators: _(javascriptallonge.pdf (source-range-31a4cf47-01754))_
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-31a4cf47-01757))_

## Technical atoms

### Technical frame 1: rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01753))_

> No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01750))_

```
const mapWith = (fn, iterable) => ({ [Symbol.iterator]: () => { const iterator = iterable[Symbol.iterator](); return { next: () => { const {done, value} = iterator.next(); return ({done, value: done ? undefined : fn(value)}); } } } });
```

### Technical frame 2: rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01753))_

> No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01752))_

```
function * mapWith (fn, iterable) { for ( const element of iterable) { yield fn(element); } }
```

### Technical frame 3: rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01757))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01755))_

```
function * mapWith(fn, iterable) { for ( const element of iterable) { yield fn(element); } } function * filterWith (fn, iterable) { for ( const element of iterable) { if (!!fn(element)) yield element; } }
```

### Technical frame 4: rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01757))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01756))_

```
function * untilWith (fn, iterable) { for ( const element of iterable) { if (fn(element)) break ; yield fn(element); } }
```

### Technical frame 5: rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01757))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01758))_

```
const first = (iterable) => iterable[Symbol.iterator]().next().value; function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next(); yield * iterator; }
```
