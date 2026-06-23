---
page_id: javascriptallonge-operations-that-compose-two-or-more-iterables-into-an-iterable
page_kind: source
summary: operations that compose two or more iterables into an iterable from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.285-286
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section describes functions that compose two or more iterables into an iterable, specifically zip and zipWith.

## Key supported claims

- The function *zip* composes two or more iterables into an iterable by mapping over the iterables and yielding arrays of values (raw/javascriptallonge.pdf p.285-286).
- Note: zip is also the following special case of zipWith (raw/javascriptallonge.pdf p.285-286).
- The const zip = callFirst(zipWith, (...values) => values) expresses zip as a special case of zipWith (raw/javascriptallonge.pdf p.285-286).

## Technical details

### `technical-atom-bea88b2b1d9ec37b` code

Citation: (raw/javascriptallonge.pdf p.285-286)

```javascript
function * zip (...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]()); while ( true ) { const pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); if (dones.indexOf( true ) >= 0) break ; yield values; } }; function * zipWith (zipper, ...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]()); while ( true ) { const pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); if (dones.indexOf( true ) >= 0) break ; yield zipper(...values); } };
```

### `technical-atom-e8edac7970de02f5` code

Citation: (raw/javascriptallonge.pdf p.285-286)

```javascript
const zip = callFirst(zipWith, (...values) => values);
```
