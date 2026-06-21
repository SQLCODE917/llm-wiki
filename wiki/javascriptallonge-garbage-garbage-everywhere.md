---
page_id: javascriptallonge-garbage-garbage-everywhere
page_kind: source
summary: Chapter on garbage collection and memory management in JavaScript
sources: raw/javascriptallonge.pdf p.126-128
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter explains tail‑call recursion for array mapping, the memory cost of temporary arrays, and contrasts JavaScript arrays with Lisp linked lists, noting possible performance drawbacks.

## Key supported claims

- In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using (raw/javascriptallonge.pdf p.126-128).
- Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another (raw/javascriptallonge.pdf p.126-128).
- Lather, rinse, repeat: Every time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend (raw/javascriptallonge.pdf p.126-128).
- It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made (raw/javascriptallonge.pdf p.126-128).
