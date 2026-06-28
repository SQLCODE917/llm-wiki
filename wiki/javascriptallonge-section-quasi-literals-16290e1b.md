---
page_id: javascriptallonge-section-quasi-literals-16290e1b
page_kind: source
summary: quasi-literals: 11 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-quasi-literals-16290e1b@a0c986521771de0ed99f971964222bef
---

# quasi-literals

From [[javascriptallonge]].

## Statements

- JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-31a4cf47-01505))_
- Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-31a4cf47-01507))_
- Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written: _(javascriptallonge.pdf (source-range-31a4cf47-01510))_
- However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following: _(javascriptallonge.pdf (source-range-31a4cf47-01513))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-31a4cf47-01507))_

## Technical atoms

### Technical frame 1: quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01507))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01506))_

```
`foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz'
```

### Technical frame 2: quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01510))_

> Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01509))_

```
`A popular number for nerds is ${ 40 + 2 } ` //=> 'A popular number for nerds is 42'
```

### Technical frame 3: quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01512))_

```
'A popular number for nerds is ' + (40 + 2) //=> 'A popular number for nerds is 42'
```

### Technical frame 4: quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01514))_

```
'A popular number for nerds is' + (40 + 2) //=> 'A popular number for nerds is42'
```
