---
page_id: javascriptallonge-section-we-get-basic-operations-on-iterables-memoizing-an-iterable-b731679a
page_kind: source
summary: We get: / Basic Operations on Iterables / memoizing an iterable: 1 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-get-basic-operations-on-iterables-memoizing-an-iterable-b731679a@1231c7025dbe6cf8ed2f6c5623d8bab8
---

# We get: / Basic Operations on Iterables / memoizing an iterable

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-get-basic-operations-on-iterables-50055b98]] - broader source section: We get: / Basic Operations on Iterables

## Technical atoms

### Technical frame 1: We get: / Basic Operations on Iterables / memoizing an iterable

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01959))_

```
function memoize (generator) {
const memos = {},
iterators = {};
return function * (...args) {
const key = JSON.stringify(args);
let i = 0;
if (memos[key] == null) {
memos[key] = [];
iterators[key] = generator(...args);
}
while (true) {
if (i < memos[key].length) {
yield memos[key][i++];
}
else {
const { done, value } = iterators[key].next();
if (done) {
return;
} else {
yield memos[key][i++] = value;
```
