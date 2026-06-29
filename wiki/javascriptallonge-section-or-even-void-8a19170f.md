---
page_id: javascriptallonge-section-or-even-void-8a19170f
page_kind: source
summary: Or even: / void: 6 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-or-even-void-8a19170f@6a4caf6c09c3758e43de209a60e1f3b2
---

# Or even: / void

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-or-even-6221c0af]] - broader source section: Or even:

## Statements

- We've seen that JavaScript represents an undefined value by typing undefined , and we've generated undefined values in two ways: _(javascriptallonge.pdf (source-range-7239e085-00226))_
- By writing undefined ourselves. _(javascriptallonge.pdf (source-range-7239e085-00228))_
- void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 . _(javascriptallonge.pdf (source-range-7239e085-00231))_
- The first form works but it's cumbersome. The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. The third form is guaranteed to always work, so that's what we will use. 20 _(javascriptallonge.pdf (source-range-7239e085-00232))_

## Technical atoms

### Technical frame 1: Or even: / void

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00231))_

> void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00230))_

```
void 0
//=> undefined
void 1
//=> undefined
void (2 + 2)
//=> undefined
```
