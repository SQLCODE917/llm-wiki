---
page_id: javascriptallonge-section-we-ll-keep-it-simple-rewriting-iterable-operations-9606b732
page_kind: source
page_family: section-reference
summary: We'll keep it simple: / rewriting iterable operations: 9 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-rewriting-iterable-operations-9606b732@cf7de06d38b03d8d09320832f1040bbe
---

# We'll keep it simple: / rewriting iterable operations

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-ll-keep-it-simple-1104ef0d]] - broader source section: We'll keep it simple:

## Statements

- Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of: _(javascriptallonge.pdf (source-range-7239e085-01748))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done. _(javascriptallonge.pdf (source-range-7239e085-01752))_
- We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators: _(javascriptallonge.pdf (source-range-7239e085-01753))_

## Technical atoms

### Technical frame 1: We'll keep it simple: / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01752))_

> No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01749))_

<a id="atom-technical-atom-d3cb2e708d5fc1d6"></a>

```
const mapWith = (fn, iterable) =>
({
[Symbol.iterator]: () => {
const iterator = iterable[Symbol.iterator]();
return {
next: () => {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

### Technical frame 2: We'll keep it simple: / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01753))_

> We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01754))_

<a id="atom-technical-atom-f9a92001c0ddb2e7"></a>

```
function * mapWith(fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
function * filterWith (fn, iterable) {
for (const element of iterable) {
if (!!fn(element)) yield element;
}
}
```

### Technical frame 3: We'll keep it simple: / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01753))_

> We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01755))_

<a id="atom-technical-atom-2a19fa1bd258aa5f"></a>

```
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
```
