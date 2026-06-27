---
page_id: javascriptallonge-section-quasi-literals-c4c59894
page_kind: source
summary: **quasi-literals**: 12 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-quasi-literals-c4c59894@e1f0718039ae474b9e62f2469d5bff9f
---

# **quasi-literals**

From [[javascriptallonge]].

## Statements

- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-83ecb080-02325))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- A quasi-literal is computationally equivalent to an expression using +. _(javascriptallonge.pdf (source-range-83ecb080-02332))_
- However, there is a big semantic difference between a quasi-literal and an expression. _(javascriptallonge.pdf (source-range-83ecb080-02338))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-83ecb080-02338))_

## Technical atoms

> Context: Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.
_(context: javascriptallonge.pdf (source-range-83ecb080-02328))_

> `foobar` _//=> 'foobar'_
_(source: javascriptallonge.pdf (source-range-83ecb080-02326))_

> Context: Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.
_(context: javascriptallonge.pdf (source-range-83ecb080-02328))_

> `fizz` + `buzz` _//=> 'fizzbuzz'_
_(source: javascriptallonge.pdf (source-range-83ecb080-02327))_

> Context: For example: A quasi-literal is computationally equivalent to an expression using +. So the above expression could also be written:
_(context: javascriptallonge.pdf (source-range-83ecb080-02329, source-range-83ecb080-02332))_

> - `A popular number for nerds is **${** 40 + 2 **}** `
_(source: javascriptallonge.pdf (source-range-83ecb080-02330))_

> Context: However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:
_(context: javascriptallonge.pdf (source-range-83ecb080-02338))_

> - 'A popular number for nerds is ' + (40 + 2)
_(source: javascriptallonge.pdf (source-range-83ecb080-02336))_

> Context: However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:
_(context: javascriptallonge.pdf (source-range-83ecb080-02338))_

> - 'A popular number for nerds is' + (40 + 2)
_(source: javascriptallonge.pdf (source-range-83ecb080-02339))_
