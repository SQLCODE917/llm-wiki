---
page_id: javascriptallonge-iterables-out-to-infinity
page_kind: source
summary: iterables out to infinity from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.215-216
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on iterables out to infinity from JavaScript Allongé.

## Key supported claims

- There are useful things we can do with infinite iterables, (raw/javascriptallonge.pdf p.215-216)
- Attempting to spread an infinite iterable into an array fails, (raw/javascriptallonge.pdf p.215-216)
- First and second element of an infinite iterable causes an infinite loop, (raw/javascriptallonge.pdf p.215-216)

## Technical details

### `technical-atom-6afb74908999e9bc` code

Citation: (raw/javascriptallonge.pdf p.215-216)

```javascript
const Numbers = { [Symbol.iterator] () { let n = 0; return { next: () => ({done: false , value: n++}) } } }
```

### `technical-atom-ef48bceaea29f284` code

Citation: (raw/javascriptallonge.pdf p.215-216)

```javascript
['all the numbers', ...Numbers] //=> infinite loop! firstAndSecondElement(...Numbers) //=> infinite loop!
```

### `technical-atom-c38fd21e3f99a4e6` requirement

Citation: (raw/javascriptallonge.pdf p.215-216)

Attempting to spread an infinite iterable into an array is always going to fail.
