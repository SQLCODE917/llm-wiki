---
page_id: javascriptallonge-call-by-sharing
page_kind: source
summary: Chapter on call by sharing in JavaScriptAllonge
sources: raw/javascriptallonge.pdf p.42-43
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

JavaScriptAllonge discusses call by sharing semantics, where JavaScript passes references as arguments, making it a specialization of call by value.

## Key supported claims

- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement 'call by sharing' semantics (raw/javascriptallonge.pdf p.42-43).
- Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types (raw/javascriptallonge.pdf p.42-43).
- When we combine our knowledge of value types, reference types, arguments, and closures, we'll understand why this function always evaluates to true no matter what argument you apply it to: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (raw/javascriptallonge.pdf p.42-43).
- Unless the argument is NaN, which isn't equal to anything, including itself (raw/javascriptallonge.pdf p.42-43).
