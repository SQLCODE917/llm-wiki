---
page_id: javascriptallonge-lazy-and-eager-collections
page_kind: source
summary: Lazy vs eager collection designs and the LazyCollection mixin
sources: raw/javascriptallonge.pdf p.246-260
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter explains why JavaScript collections might benefit from lazy evaluation, critiques the fat‑object approach, and presents a reusable LazyCollection mixin that supplies map, reduce, filter, and find via iterator protocols.

## Key supported claims

- Some collection methods are added only to a few types, while others apply to all (raw/javascriptallonge.pdf p.246-260)
- The fat‑object style arises from misunderstanding: a collection should know how to map over itself but not handle every detail (raw/javascriptallonge.pdf p.246-260)
- LazyCollection is a mixin usable with any ordered iterable, adding map, reduce, filter, and find (raw/javascriptallonge.pdf p.246-260)
- Object‑oriented collections should expose mapping, reducing, filtering, and finding, delegating work to helpers such as mapWith (raw/javascriptallonge.pdf p.246-260)
- Each collection implements map, fold, filter, and find, yet duplicated code across methods suggests a higher‑level abstraction might be needed (raw/javascriptallonge.pdf p.246-260)
