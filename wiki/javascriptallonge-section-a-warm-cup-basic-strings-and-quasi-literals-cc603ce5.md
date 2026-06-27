---
page_id: javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-cc603ce5
page_kind: source
summary: A Warm Cup: Basic Strings and Quasi-Literals: 27 source-backed entries and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-cc603ce5@47e98d60b28dfc22ae09f1427c0f21e2
---

# A Warm Cup: Basic Strings and Quasi-Literals

From [[javascriptallonge]].

## Statements

- An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and operators[87] _(javascriptallonge.pdf (source-range-83ecb080-02319))_
- Special characters can be included in a string literal by means of an _escape sequence_ . _(javascriptallonge.pdf (source-range-83ecb080-02320))_
- For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line'. _(javascriptallonge.pdf (source-range-83ecb080-02320))_
- Special characters can be included in a string literal by means of an _escape sequence_ . _(javascriptallonge.pdf (source-range-83ecb080-02320))_
- There are operators that can be used on strings. _(javascriptallonge.pdf (source-range-83ecb080-02321))_
- String manipulation is extremely common in programming. _(javascriptallonge.pdf (source-range-83ecb080-02323))_
- Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. _(javascriptallonge.pdf (source-range-83ecb080-02323))_
- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-83ecb080-02325))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- A quasi-literal is computationally equivalent to an expression using +. _(javascriptallonge.pdf (source-range-83ecb080-02332))_
- However, there is a big semantic difference between a quasi-literal and an expression. _(javascriptallonge.pdf (source-range-83ecb080-02338))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-83ecb080-02338))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02348))_
- Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-83ecb080-02348))_
- Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-83ecb080-02348))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02348))_

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

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02329, source-range-83ecb080-02332))_

> For example: A quasi-literal is computationally equivalent to an expression using +. So the above expression could also be written:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02330))_

> - `A popular number for nerds is **${** 40 + 2 **}** `

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02338))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02336))_

> - 'A popular number for nerds is ' + (40 + 2)

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02338))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02339))_

> - 'A popular number for nerds is' + (40 + 2)

### Technical atom 7

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02344))_

> **const** name = "Harry";

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02345))_

> **const** greeting = (name) => `Hello my name is **${** name **}** `;

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02349))_

> This is exactly what we’d expect if we’d written it like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02350))_

> **const** greeting = (name) => 'Hello my name is ' + name;
