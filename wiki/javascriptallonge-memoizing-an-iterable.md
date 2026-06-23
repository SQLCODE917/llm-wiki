---
page_id: javascriptallonge-memoizing-an-iterable
page_kind: source
summary: memoizing an iterable from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.286-287
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé – A modular guide to JavaScript fundamentals and advanced techniques, focusing on memoizing iterables.

## Key supported claims

- The memoize function creates a generator that caches results using memos and iterators (raw/javascriptallonge.pdf p.286-287).
- The implementation is served by the Pot: Collections 264 (raw/javascriptallonge.pdf p.286-287).

## Technical details

### `technical-atom-e6b1617bec3d7b48` code

Citation: (raw/javascriptallonge.pdf p.286-287)

```javascript
function memoize (generator) { const memos = {}, iterators = {}; return function * (...args) { const key = JSON.stringify(args); let i = 0; if (memos[key] == null ) { memos[key] = []; iterators[key] = generator(...args); } while ( true ) { if (i < memos[key].length) { yield memos[key][i++]; } else { const { done, value } = iterators[key].next(); if (done) { return ; } else { yield memos[key][i++] = value;
```
