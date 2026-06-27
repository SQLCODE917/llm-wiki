---
page_id: javascriptallonge-section-caveat-8e7d6204
page_kind: source
summary: **caveat**: 3 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-caveat-8e7d6204@faabbda1112762f45413406916be4dac
---

# **caveat**

From [[javascriptallonge]].

## Statements

- There are some important implications of stateful functions. _(javascriptallonge.pdf (source-range-83ecb080-02024))_
- One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. _(javascriptallonge.pdf (source-range-83ecb080-02024))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-02025))_
