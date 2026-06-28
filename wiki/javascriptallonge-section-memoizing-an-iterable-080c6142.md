---
page_id: javascriptallonge-section-memoizing-an-iterable-080c6142
page_kind: source
summary: memoizing an iterable: 1 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-memoizing-an-iterable-080c6142@6b8798ae7e9f1c87305a86b55c0b97cf
---

# memoizing an iterable

From [[javascriptallonge]].

## Technical atoms

### Technical frame 1: memoizing an iterable

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01960))_

```
function memoize (generator) { const memos = {}, iterators = {}; return function * (...args) { const key = JSON.stringify(args); let i = 0; if (memos[key] == null ) { memos[key] = []; iterators[key] = generator(...args); } while ( true ) { if (i < memos[key].length) { yield memos[key][i++]; } else { const { done, value } = iterators[key].next(); if (done) { return ; } else { yield memos[key][i++] = value;
```
