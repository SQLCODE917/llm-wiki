---
page_id: javascriptallonge-section-values-are-expressions-reassignment-mixing-let-and-const-60770c61
page_kind: source
summary: values are expressions / Reassignment / mixing let and const: 3 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-reassignment-mixing-let-and-const-60770c61@3402f886f83acd11b284e49da4198518
---

# values are expressions / Reassignment / mixing let and const

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-reassignment-de1c3943]] - broader source section

## Statements

- The suggestion is that shadowing a variable is confusing code. _(javascriptallonge.pdf (source-range-83ecb080-01179))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. _(javascriptallonge.pdf (source-range-83ecb080-01181))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01180))_

> If you dislike deliberately shadowing variables, you’ll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable: (() => { **let** age = 49; **if** ( **true** ) { **const** age = 50; } age = 51; **return** age; })() _//=> 51_
