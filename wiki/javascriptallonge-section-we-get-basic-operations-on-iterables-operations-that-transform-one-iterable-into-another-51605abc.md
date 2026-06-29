---
page_id: javascriptallonge-section-we-get-basic-operations-on-iterables-operations-that-transform-one-iterable-into-another-51605abc
page_kind: source
summary: We get: / Basic Operations on Iterables / operations that transform one iterable into another: 2 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-get-basic-operations-on-iterables-operations-that-transform-one-iterable-into-another-51605abc@3644b63dec3af8ca6d94b78e926537e6
---

# We get: / Basic Operations on Iterables / operations that transform one iterable into another

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-get-basic-operations-on-iterables-50055b98]] - broader source section: We get: / Basic Operations on Iterables

## Technical atoms

### Technical frame 1: We get: / Basic Operations on Iterables / operations that transform one iterable into another

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01950))_

```
function * mapWith(fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
function * mapAllWith (fn, iterable) {
for (const element of iterable) {
yield * fn(element);
}
}
function * filterWith (fn, iterable) {
for (const element of iterable) {
if (!!fn(element)) yield element;
}
}
function * compact (iterable) {
for (const element of iterable) {
if (element != null) yield element;
}
}
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
```

### Technical frame 2: We get: / Basic Operations on Iterables / operations that transform one iterable into another

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01951))_

```
yield * iterator;
}
function * take (numberToTake, iterable) {
const iterator = iterable[Symbol.iterator]();
for (let i = 0; i < numberToTake; ++i) {
const { done, value } = iterator.next();
if (!done) yield value;
}
}
```
