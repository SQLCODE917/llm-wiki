---
page_id: javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-a1ab40aa
page_kind: source
summary: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: 11 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-a1ab40aa@ba6633154466648925f56a91cd1e3e6e
---

# A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-d5c66d04]] - broader source section: A Warm Cup: Basic Strings and Quasi-Literals
- [[javascriptallonge-quasi-literal]] - topic hub: opens the topic page for Quasi Literal

## Statements

- JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-7239e085-01505))_
- Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-7239e085-01507))_
- Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written: _(javascriptallonge.pdf (source-range-7239e085-01510))_
- However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following: _(javascriptallonge.pdf (source-range-7239e085-01513))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-7239e085-01507))_

## Technical atoms

### Technical frame 1: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01507))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01506))_

```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```

### Technical frame 2: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01510))_

> Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01509))_

```
`A popular number for nerds is ${40 + 2}`
//=> 'A popular number for nerds is 42'
```

### Technical frame 3: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01512))_

```
'A popular number for nerds is ' + (40 + 2)
//=> 'A popular number for nerds is 42'
```

### Technical frame 4: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01514))_

```
'A popular number for nerds is' + (40 + 2)
//=> 'A popular number for nerds is42'
```
