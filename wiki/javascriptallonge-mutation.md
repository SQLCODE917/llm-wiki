---
page_id: javascriptallonge-mutation
page_kind: source
summary: Chapter on building with mutation in JavaScript
sources: raw/javascriptallonge.pdf p.145-147
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter explains how mutation works in JavaScript, covering arrays, objects, aliases, and assignment semantics, with possible nuances. This specific section focuses on building data structures with mutation, particularly in the context of linked lists.

## Key supported claims

- As noted, one pattern is to be more liberal about mutation when building a data structure (raw/javascriptallonge.pdf p.145-147).
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation (raw/javascriptallonge.pdf p.145-147).
- But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time (raw/javascriptallonge.pdf p.145-147).
