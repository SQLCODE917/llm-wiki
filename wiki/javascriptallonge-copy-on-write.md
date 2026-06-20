---
page_id: javascriptallonge-copy-on-write
page_kind: source
summary: Copy‑on‑write strategies for array and list mutation in JavaScript.
sources: raw/javascriptallonge.pdf p.158-176
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Copy‑on‑write concepts for arrays and linked lists in JavaScript.

## Key supported claims

- When you destructure an array as `[first, ...rest]`, you receive a copy of the remaining elements (possible copy, raw/javascriptallonge.pdf p.158-176).
- Taking the rest of a linked list via its reference gives the exact same nodes, so modifications affect both lists (possible reference sharing, raw/javascriptallonge.pdf p.158-176).
- Copy‑on‑write strategy copies only when a mutation is attempted, trading performance for safety in JavaScript implementations (possible performance trade‑off, raw/javascriptallonge.pdf p.158-176).
