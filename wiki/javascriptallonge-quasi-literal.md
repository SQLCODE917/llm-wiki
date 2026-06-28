---
page_id: javascriptallonge-quasi-literal
page_kind: concept
summary: Quasi Literal: 8 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-quasi-literal@58ec7dcca248c8f854f1f3c620a1a594
---

# Quasi Literal

What [[javascriptallonge]] covers about quasi literal:

## Statements

- Special characters can be included in a string literal by means of an _escape sequence_ . _(javascriptallonge.pdf (source-range-83ecb080-02320))_
- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-83ecb080-02325))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02348))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- A quasi-literal is computationally equivalent to an expression using +. _(javascriptallonge.pdf (source-range-83ecb080-02332))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-83ecb080-02338))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- However, there is a big semantic difference between a quasi-literal and an expression. _(javascriptallonge.pdf (source-range-83ecb080-02338))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02328))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02326))_

> `foobar` _//=> 'foobar'_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02328))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02327))_

> `fizz` + `buzz` _//=> 'fizzbuzz'_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02329, source-range-83ecb080-02332))_

> For example: A quasi-literal is computationally equivalent to an expression using +. So the above expression could also be written:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02330))_

> - `A popular number for nerds is **${** 40 + 2 **}** `

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02338))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02336))_

> - 'A popular number for nerds is ' + (40 + 2)

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02338))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02339))_

> - 'A popular number for nerds is' + (40 + 2)


## Related pages

- [[javascriptallonge-literal]] - broader topic (5 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-warm-cup-string]] - shared statements and technical atoms (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
