---
page_id: javascriptallonge-caveat
page_kind: source
summary: caveat from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.176-176
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section discusses the stateful nature of iterators and important implications of stateful functions in JavaScript Allongé.

## Key supported claims

- One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator (raw/javascriptallonge.pdf p.176-176).
- Please note that unlike most of the other functions discussed in this book, iterators are stateful (raw/javascriptallonge.pdf p.176-176).
- So as you traverse the new decorator, you're changing the state of the original! (raw/javascriptallonge.pdf p.176-176).
