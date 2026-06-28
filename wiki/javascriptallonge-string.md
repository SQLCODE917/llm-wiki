---
page_id: javascriptallonge-string
page_kind: concept
summary: String: 6 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-string@11a58e7252de3f41b0f2adb21227ecbc
---

# String

What [[javascriptallonge]] covers about string:

## Statements

- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-83ecb080-01502))_
- For example, the string "2" is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- Like numbers, strings, and arrays, they have a representation. _(javascriptallonge.pdf (source-range-83ecb080-00218))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- String manipulation is extremely common in programming. _(javascriptallonge.pdf (source-range-83ecb080-01500))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00164))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00162))_

> - 2 + 2 === 4 _//=> true_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00164))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00163))_

> - (2 + 2 === 4) === (2 !== 5) _//=> true_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00164))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00165))_

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01504))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01503))_

> `foobar` _//=> 'foobar'_ `fizz` + `buzz` _//=> 'fizzbuzz'_


## Related pages

- [[javascriptallonge-warm-cup-string]] - narrower topic (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-quasi]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-quasi-literal]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms (4 shared atom(s))
- [[javascriptallonge-note]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-type]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms (3 shared atom(s))

## Source

- [[javascriptallonge]]
