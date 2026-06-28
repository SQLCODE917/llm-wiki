---
page_id: javascriptallonge-section-values-are-expressions-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-35067272
page_kind: source
summary: values are expressions / A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-35067272@619c8de7f5964533a989d1f814b6c921
---

# values are expressions / A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-a-warm-cup-basic-strings-and-quasi-literals-5d3f583e]] - broader source section
- [[javascriptallonge-quasi-literal]] - topic hub

## Statements

- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-83ecb080-01502))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-83ecb080-01504))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-01504))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-01504))_
- A quasi-literal is computationally equivalent to an expression using +. _(javascriptallonge.pdf (source-range-83ecb080-01508))_
- - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big semantic difference between a quasi-literal and an expression. _(javascriptallonge.pdf (source-range-83ecb080-01512))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-83ecb080-01512))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01504))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01503))_

> `foobar` _//=> 'foobar'_ `fizz` + `buzz` _//=> 'fizzbuzz'_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01505, source-range-83ecb080-01508))_

> For example: A quasi-literal is computationally equivalent to an expression using +. So the above expression could also be written:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01506))_

> - `A popular number for nerds is **${** 40 + 2 **}** `

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01512))_

> 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01513))_

> - 'A popular number for nerds is' + (40 + 2) - _//=> 'A popular number for nerds is42'_
