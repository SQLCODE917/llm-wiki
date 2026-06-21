---
page_id: javascriptallonge-lazy-and-eager-collections
page_kind: source
summary: Lazy vs eager collection designs and the LazyCollection mixin
sources: raw/javascriptallonge.pdf p.256-260
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter explains why JavaScript collections might benefit from lazy evaluation, critiques the fat‑object approach, and presents a reusable LazyCollection mixin that supplies map, reduce, filter, and find via iterator protocols.

## Key supported claims

- We can make an eager collection out of any collection that is gatherable, meaning it has a .from method: (raw/javascriptallonge.pdf p.256-260)
- We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: (raw/javascriptallonge.pdf p.256-260)
