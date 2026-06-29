---
page_id: javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-value-ae929990
page_kind: source
summary: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value: 7 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-value-ae929990@6f0ca3e0d9f8214e004440a772015665
---

# And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-f00edd2f]] - broader source section: And also: / Ah. I'd Like to Have an Argument, Please. 22
- [[javascriptallonge-value]] - topic hub: opens the topic page for Value

## Statements

- Like most contemporary programming languages, JavaScript uses the 'call by value' evaluation strategy 23 . That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-7239e085-00291))_
- What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . Then our circumference function was applied to 2 . 24 _(javascriptallonge.pdf (source-range-7239e085-00295))_
- We'll see below that while JavaScript always calls by value, the notion of a 'value' has additional subtlety. But before we do, let's look at variables. _(javascriptallonge.pdf (source-range-7239e085-00296))_
- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-7239e085-00291))_
- Then our circumference function was applied to 2 . _(javascriptallonge.pdf (source-range-7239e085-00295))_

## Technical atoms

### Technical frame 1: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00295))_

> What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . Then our circumference function was applied to 2 . 24

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00294))_

```
((diameter) => diameter * 3.14159265)(1 + 1)
//=> 6.2831853
```
