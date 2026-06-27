---
page_id: javascriptallonge-section-operations-that-compose-two-or-more-iterables-into-an-iterable-4939bfa4
page_kind: source
summary: **operations that compose two or more iterables into an iterable**: 2 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-operations-that-compose-two-or-more-iterables-into-an-iterable-4939bfa4@d0f6e3297cd9efa8ee4c3807a450a79e
---

# **operations that compose two or more iterables into an iterable**

From [[javascriptallonge]].

## Technical atoms

> **function** * zip (...iterables) { **const** iterators = iterables.map(i => i[Symbol.iterator]());
_(source: javascriptallonge.pdf (source-range-83ecb080-03061))_

> Context: Note: zip is also the following special case of zipWith:
_(context: javascriptallonge.pdf (source-range-83ecb080-03063))_

> **const** zip = callFirst(zipWith, (...values) => values);
_(source: javascriptallonge.pdf (source-range-83ecb080-03066))_
