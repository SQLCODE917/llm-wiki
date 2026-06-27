---
page_id: javascriptallonge-section-void-02c6d9f7
page_kind: source
summary: **void**: 6 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-void-02c6d9f7@27ccac11c256dd227c1ad52333502a54
---

# **void**

From [[javascriptallonge]].

## Statements

- We’ve seen that JavaScript represents an undefined value by typing undefined, and we’ve generated undefined values in two ways: _(javascriptallonge.pdf (source-range-83ecb080-00331))_
- void is an operator that takes any value and evaluates to undefined, always. _(javascriptallonge.pdf (source-range-83ecb080-00336))_
- So, when we deliberately want an undefined value, should we use the first, second, or third form?[19] The answer is, use void. _(javascriptallonge.pdf (source-range-83ecb080-00336))_
- The first form works but it’s cumbersome. _(javascriptallonge.pdf (source-range-83ecb080-00337))_
- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we’ll discuss in Reassignment and Mutation. _(javascriptallonge.pdf (source-range-83ecb080-00337))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00334, source-range-83ecb080-00336))_

> There’s a third way, with JavaScript’s void operator. Behold: void is an operator that takes any value and evaluates to undefined, always. So, when we deliberately want an undefined value, should we use the first, second, or third form?[19] The answer is, use void. By convention, use void 0.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00335))_

> **void** 0 _//=> undefined_ **void** 1 _//=> undefined_ **void** (2 + 2) _//=> undefined_
