---
page_id: javascriptallonge-section-we-get-basic-operations-on-iterables-operations-that-transform-an-iterable-into-a-value-7603882e
page_kind: source
summary: We get: / Basic Operations on Iterables / operations that transform an iterable into a value: 1 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-get-basic-operations-on-iterables-operations-that-transform-an-iterable-into-a-value-7603882e@4eeadaecaf5b76c1f5e7ac1dcbedc018
---

# We get: / Basic Operations on Iterables / operations that transform an iterable into a value

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-get-basic-operations-on-iterables-50055b98]] - broader source section: We get: / Basic Operations on Iterables

## Technical atoms

### Technical frame 1: We get: / Basic Operations on Iterables / operations that transform an iterable into a value

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01957))_

```
const reduceWith = (fn, seed, iterable) => {
let accumulator = seed;
for (const element of iterable) {
accumulator = fn(accumulator, element);
}
return accumulator;
};
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
```
