---
page_id: javascriptallonge-section-truthiness-and-operators-d856360c
page_kind: source
summary: **truthiness and operators**: 9 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-truthiness-and-operators-d856360c@5b0e5ac7702a222da0f706e2e48b8d23
---

# **truthiness and operators**

From [[javascriptallonge]].

## Statements

- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-83ecb080-01123))_
- Our logical operators !, &&, and || are a little more subtle than our examples above implied. _(javascriptallonge.pdf (source-range-83ecb080-01123))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. _(javascriptallonge.pdf (source-range-83ecb080-01128))_
- First, and unlike !, && and || do not necessarily evaluate to true or false. _(javascriptallonge.pdf (source-range-83ecb080-01133))_
- First, and unlike !, && and || do not necessarily evaluate to true or false. _(javascriptallonge.pdf (source-range-83ecb080-01133))_
- If we look at our examples above, we see that when we pass true and false to && and ||, we do indeed get true or false as a result. _(javascriptallonge.pdf (source-range-83ecb080-01140))_
- They don’t operate strictly on logical values, and they don’t commute: a || b is not always equal to b || a, and the same goes for &&. _(javascriptallonge.pdf (source-range-83ecb080-01146))_
- This is not a subtle distinction. _(javascriptallonge.pdf (source-range-83ecb080-01147))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01140))_

> But when we pass other values, we no longer get true or false:
