---
page_id: javascriptallonge-literal
page_kind: concept
summary: Literal: 12 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-literal@a29583b35b609ae61034059274c164c0
---

# Literal

What [[javascriptallonge]] covers about literal:

## Statements

- If we start a literal with a zero, it is an octal literal. _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-83ecb080-02325))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02348))_
- In computer science, a literal is a notation for representing a fixed value in source code. _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- So the literal 042 is 42 base 8, which is actually 34 base 10. _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- A “magic literal” like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-83ecb080-00565))_
- Array literals are expressions, and arrays are _reference types_ . _(javascriptallonge.pdf (source-range-83ecb080-01204))_
- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-83ecb080-01299))_
- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-83ecb080-01306))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- A quasi-literal is computationally equivalent to an expression using +. _(javascriptallonge.pdf (source-range-83ecb080-02332))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-83ecb080-02338))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01204))_

> Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01205))_

> [] === [] _//=> false_ [2 + 2] === [2 + 2] _//=> false_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01204))_

> Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01206))_

> **const** array_of_one = () => [1];

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01204))_

> Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01207))_

> array_of_one() === array_of_one() _//=> false_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02328))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02326))_

> `foobar` _//=> 'foobar'_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02328))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02327))_

> `fizz` + `buzz` _//=> 'fizzbuzz'_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02329, source-range-83ecb080-02332))_

> For example: A quasi-literal is computationally equivalent to an expression using +. So the above expression could also be written:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02330))_

> - `A popular number for nerds is **${** 40 + 2 **}** `

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02338))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02336))_

> - 'A popular number for nerds is ' + (40 + 2)

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02338))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02339))_

> - 'A popular number for nerds is' + (40 + 2)


## Related pages

- [[javascriptallonge-quasi-literal]] - narrower topic (5 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-warm-cup-string]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements (1 shared statement(s))
- [[javascriptallonge-rest]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
