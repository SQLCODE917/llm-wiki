---
page_id: javascriptallonge-warm-cup-string
page_kind: concept
summary: Warm Cup String: 6 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-warm-cup-string@9842926cda901899044a9b21436dc75f
---

# Warm Cup String

What [[javascriptallonge]] covers about warm cup string:

## Statements

- Special characters can be included in a string literal by means of an _escape sequence_ . _(javascriptallonge.pdf (source-range-83ecb080-02320))_
- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-83ecb080-02325))_
- String manipulation is extremely common in programming. _(javascriptallonge.pdf (source-range-83ecb080-02323))_
- There are operators that can be used on strings. _(javascriptallonge.pdf (source-range-83ecb080-02321))_
- Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. _(javascriptallonge.pdf (source-range-83ecb080-02323))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-02328))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02321))_

> There are operators that can be used on strings. The most common is +, it _concatenates_ :

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02322))_

> 'fu' + 'bar' _//=> 'fubar'_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02328))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02326))_

> `foobar` _//=> 'foobar'_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02328))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02327))_

> `fizz` + `buzz` _//=> 'fizzbuzz'_


## Related pages

- [[javascriptallonge-quasi-literal]] - shared statements and technical atoms (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))

## Source

- [[javascriptallonge]]
