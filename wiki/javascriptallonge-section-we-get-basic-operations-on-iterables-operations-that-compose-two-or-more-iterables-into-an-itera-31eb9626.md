---
page_id: javascriptallonge-section-we-get-basic-operations-on-iterables-operations-that-compose-two-or-more-iterables-into-an-itera-31eb9626
page_kind: source
summary: We get: / Basic Operations on Iterables / operations that compose two or more iterables into an iterable: 2 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-get-basic-operations-on-iterables-operations-that-compose-two-or-more-iterables-into-an-itera-31eb9626@17652d6cb8fe147e176a890d753710da
---

# We get: / Basic Operations on Iterables / operations that compose two or more iterables into an iterable

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-get-basic-operations-on-iterables-50055b98]] - broader source section: We get: / Basic Operations on Iterables

## Technical atoms

### Technical frame 1: We get: / Basic Operations on Iterables / operations that compose two or more iterables into an iterable

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01953))_

```
function * zip (...iterables) {
const iterators = iterables.map(i => i[Symbol.iterator]());
while (true) {
const pairs = iterators.map(j => j.next()),
dones = pairs.map(p => p.done),
values = pairs.map(p => p.value);
if (dones.indexOf(true) >= 0) break;
yield values;
}
};
function * zipWith (zipper, ...iterables) {
const iterators = iterables.map(i => i[Symbol.iterator]());
while (true) {
const pairs = iterators.map(j => j.next()),
dones = pairs.map(p => p.done),
values = pairs.map(p => p.value);
if (dones.indexOf(true) >= 0) break;
yield zipper(...values);
}
};
```

### Technical frame 2: We get: / Basic Operations on Iterables / operations that compose two or more iterables into an iterable

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01955))_

```
const zip = callFirst(zipWith, (...values) => values);
```
