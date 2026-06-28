---
page_id: javascriptallonge-section-recursive-iterators-d5442e37
page_kind: source
summary: recursive iterators: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recursive-iterators-d5442e37@f33efb7bd7303f699812a7258fcb45f6
---

# recursive iterators

From [[javascriptallonge]].

## Statements

- Iterators maintain state, that's what they do. Generators have to manage the exact same amount of state, but sometimes, it's much easier to manage that state in a generator. One of those cases is when we have to recursively enumerate something. _(javascriptallonge.pdf (source-range-31a4cf47-01637))_
- For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-31a4cf47-01638))_

## Technical atoms

### Technical frame 1: recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01638))_

> For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01637))_

> One of those cases is when we have to recursively enumerate something.

### Technical frame 2: recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01638))_

> For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01639))_

```
// Generation const isIterable = (something) => !!something[Symbol.iterator]; const generate = (iterable) => { for ( let element of iterable) { if (isIterable(element)) { generate(element) } else { console.log(element) } } } generate([1, [2, [3, 4], 5]]) //=> 1 2 3 4 5
```
