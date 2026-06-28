---
page_id: javascriptallonge-section-operations-that-compose-two-or-more-iterables-into-an-iterable-87523200
page_kind: source
summary: operations that compose two or more iterables into an iterable: 2 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-operations-that-compose-two-or-more-iterables-into-an-iterable-87523200@7d65c7281e85cf61a2afc593e9cfc930
---

# operations that compose two or more iterables into an iterable

From [[javascriptallonge]].

## Technical atoms

### Technical frame 1: operations that compose two or more iterables into an iterable

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01954))_

```
function * zip (...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]()); while ( true ) { const pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); if (dones.indexOf( true ) >= 0) break ; yield values; } }; function * zipWith (zipper, ...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]()); while ( true ) { const pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); if (dones.indexOf( true ) >= 0) break ; yield zipper(...values); } };
```

### Technical frame 2: operations that compose two or more iterables into an iterable

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01956))_

```
const zip = callFirst(zipWith, (...values) => values);
```
