---
page_id: javascriptallonge-section-values-are-expressions-functional-iterators-caveat-40b5f947
page_kind: source
summary: values are expressions / Functional Iterators / caveat: 3 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-functional-iterators-caveat-40b5f947@ffee870ecfd84554d542245a00056438
---

# values are expressions / Functional Iterators / caveat

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-functional-iterators-a4bbe212]] - broader source section

## Statements

- There are some important implications of stateful functions. _(javascriptallonge.pdf (source-range-83ecb080-01311))_
- One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. _(javascriptallonge.pdf (source-range-83ecb080-01311))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-01312))_
