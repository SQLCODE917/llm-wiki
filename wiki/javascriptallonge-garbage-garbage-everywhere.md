---
page_id: javascriptallonge-garbage-garbage-everywhere
page_kind: source
summary: Chapter covering tail‑call recursion, array vs. Lisp linked list performance.
sources: raw/javascriptallonge.pdf p.126-140
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter explains tail‑call recursion for array mapping, the memory cost of temporary arrays, and contrasts JavaScript arrays with Lisp linked lists, noting possible performance drawbacks.

## Key supported claims

- Tail‑recursive mapWith runs in constant space but may generate many temporary arrays, making it slower than Array.prototype.map (raw/javascriptallonge.pdf p.126-140).
- Each recursive call copies the prepend array, meaning each element may incur an O(n) copy cost (raw/javascriptallonge.pdf p.126-140).
- JavaScript’s destructuring [first, ...rest] mimics Lisp’s car/cdr but may lead to costly temporary array churn; Lisp’s linked lists avoid this (raw/javascriptallonge.pdf p.126-140).
- The chapter explains that Tail Calls enable constant‑space recursion but the repeated array copy makes the approach inefficient (raw/javascriptallonge.pdf p.126-140).
