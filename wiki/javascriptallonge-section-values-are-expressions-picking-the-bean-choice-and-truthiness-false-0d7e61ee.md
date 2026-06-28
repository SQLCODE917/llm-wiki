---
page_id: javascriptallonge-section-values-are-expressions-picking-the-bean-choice-and-truthiness-false-0d7e61ee
page_kind: source
summary: values are expressions / Picking the Bean: Choice and Truthiness / false: 6 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-picking-the-bean-choice-and-truthiness-false-0d7e61ee@6266a5f11552270d3074c846dcd397fc
---

# values are expressions / Picking the Bean: Choice and Truthiness / false

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-picking-the-bean-choice-and-truthiness-af2f328d]] - broader source section

## Statements

- We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. _(javascriptallonge.pdf (source-range-83ecb080-00761))_
- All values of true are === all other values of true. _(javascriptallonge.pdf (source-range-83ecb080-00761))_
- _//=> false_ true and false are value types. _(javascriptallonge.pdf (source-range-83ecb080-00761))_
- The && and || operators are binary infix operators that perform “logical and” and “logical or” respectively: **false** && **false** _//=> false_ **false** && **true** _//=> false_ **true** && **false** _//=> false_ **true** && **true** _//=> true_ **false** || **false** _//=> false_ **false** || **true** _//=> true_ **true** || **false** _//=> true_ **true** || **true** _//=> true_ _(javascriptallonge.pdf (source-range-83ecb080-00765))_
- Now, note well: We have said what happens if you pass boolean values to !, &&, and ||, but we’ve said nothing about expressions or about passing other values. _(javascriptallonge.pdf (source-range-83ecb080-00766))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00761))_

> _//=> false_ true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. To being with, ! is a unary prefix operator that negates its argument. So:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00764))_

> ! **true** _//=> false_ ! **false** _//=> true_
