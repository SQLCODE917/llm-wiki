---
page_id: javascriptallonge-quasi-literal
page_kind: concept
summary: Quasi Literal: 8 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-quasi-literal@ac2c2cba22335d4adad88a1cb53ade72
---

# Quasi Literal

What [[javascriptallonge]] covers about quasi literal:

## Statements

- Special characters can be included in a string literal by means of an _escape sequence_ . _(javascriptallonge.pdf (source-range-83ecb080-01498))_
- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-83ecb080-01502))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-83ecb080-01504))_
- A quasi-literal is computationally equivalent to an expression using +. _(javascriptallonge.pdf (source-range-83ecb080-01508))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-83ecb080-01512))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-01504))_
- 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big semantic difference between a quasi-literal and an expression. _(javascriptallonge.pdf (source-range-83ecb080-01512))_

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


## Related pages

- [[javascriptallonge-literal]] - broader topic (5 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-quasi]] - broader topic (5 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-warm-cup-string]] - shared statements and technical atoms (3 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-string]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements (1 shared statement(s))
- [[javascriptallonge-section-values-are-expressions-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-35067272]] - source section (6 shared statement(s), 3 shared atom(s))

## Source

- [[javascriptallonge]]
