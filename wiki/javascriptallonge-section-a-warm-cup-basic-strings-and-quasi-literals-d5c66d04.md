---
page_id: javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-d5c66d04
page_kind: source
summary: A Warm Cup: Basic Strings and Quasi-Literals: 25 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-d5c66d04@5d3281f97f2a072d5e374f605bf8dea7
---

# A Warm Cup: Basic Strings and Quasi-Literals

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-a1ab40aa]] - narrower source section: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals
- [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-evaluation-time-a314598a]] - narrower source section: A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

## Statements

- Coffee and a Book An expression is any valid unit of code that resolves to a value.-Mozilla Development Network: Expressions and operators 87 _(javascriptallonge.pdf (source-range-7239e085-01499))_
- Like most programming languages, JavaScript also has string literals, like 'fubar' or 'fizzbuzz' . Special characters can be included in a string literal by means of an escape sequence . For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line' . _(javascriptallonge.pdf (source-range-7239e085-01500))_
- There are operators that can be used on strings. The most common is + , it concatenates : _(javascriptallonge.pdf (source-range-7239e085-01501))_
- String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. _(javascriptallonge.pdf (source-range-7239e085-01503))_
- Special characters can be included in a string literal by means of an escape sequence . _(javascriptallonge.pdf (source-range-7239e085-01500))_

## Statements by subsection

### A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

- JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-7239e085-01505))_
- Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-7239e085-01507))_
- Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written: _(javascriptallonge.pdf (source-range-7239e085-01510))_
- However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following: _(javascriptallonge.pdf (source-range-7239e085-01513))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-7239e085-01507))_

### A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-7239e085-01519))_
- Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-7239e085-01519))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. _(javascriptallonge.pdf (source-range-7239e085-01519))_

## Technical atoms

### Technical frame 1: A Warm Cup: Basic Strings and Quasi-Literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01499))_

> Coffee and a Book An expression is any valid unit of code that resolves to a value.-Mozilla Development Network: Expressions and operators 87

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01498))_

> [Figure] (p.202)

### Technical frame 2: A Warm Cup: Basic Strings and Quasi-Literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01503))_

> String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01502))_

```
'fu' + 'bar'
//=> 'fubar'
```

### Technical frame 3: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01507))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01506))_

```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```

### Technical frame 4: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01510))_

> Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01509))_

```
`A popular number for nerds is ${40 + 2}`
//=> 'A popular number for nerds is 42'
```

### Technical frame 5: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01512))_

```
'A popular number for nerds is ' + (40 + 2)
//=> 'A popular number for nerds is 42'
```

### Technical frame 6: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01514))_

```
'A popular number for nerds is' + (40 + 2)
//=> 'A popular number for nerds is42'
```

### Technical frame 7: A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01519))_

> JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01518))_

```
const name = "Harry";
const greeting = (name) => `Hello my name is ${name}`;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```

### Technical frame 8: A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01519))_

> JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01521))_

```
const greeting = (name) => 'Hello my name is ' + name;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```
