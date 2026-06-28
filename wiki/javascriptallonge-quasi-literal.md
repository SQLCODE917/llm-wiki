---
page_id: javascriptallonge-quasi-literal
page_kind: concept
summary: Quasi Literal: 6 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-quasi-literal@865d1af246bbc3a6b5dff17bcfb65351
---

# Quasi Literal

What [[javascriptallonge]] covers about quasi literal:

## Statements

### A Warm Cup: Basic Strings and Quasi-Literals

- A Warm Cup: Basic Strings and Quasi-Literals

180

An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and operators[87] Like most programming languages, JavaScript also has string literals, like 'fubar' or 'fizzbuzz'. Special characters can be included in a string literal by means of an _escape sequence_ . For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line'.

There are operators that can be used on strings. The most common is +, it _concatenates_ : 'fu' + 'bar' _//=> 'fubar'_

String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing.

## **quasi-literals**

JavaScript supports _quasi-literal strings_ , a/k/a “Template Strings” or “String Interpolation Expressions.” A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g.

`foobar` _//=> 'foobar'_ `fizz` + `buzz` _//=> 'fizzbuzz'_

Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

For example:

- `A popular number for nerds is **${** 40 + 2 **}** `

- _//=> 'A popular number for nerds is 42'_

A quasi-literal is computationally equivalent to an expression using +. So the above expression could also be written:

> 87https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators _(javascriptallonge.pdf (source-range-83ecb080-00242))_

- A Warm Cup: Basic Strings and Quasi-Literals

181

- 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

- 'A popular number for nerds is' + (40 + 2) - _//=> 'A popular number for nerds is42'_

## **evaluation time**

Like any other expression, quasi-literals are evaluated _late_ , when that line or lines of code is evaluated.

So for example, **const** name = "Harry"; **const** greeting = (name) => `Hello my name is **${** name **}** `; greeting('Arthur Dent') - _//=> 'Hello my name is Arthur Dent'_

JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked.

This is exactly what we’d expect if we’d written it like this: **const** greeting = (name) => 'Hello my name is ' + name; greeting('Arthur Dent') - _//=> 'Hello my name is Arthur Dent'_ _(javascriptallonge.pdf (source-range-83ecb080-00243))_


## Related pages

- [[javascriptallonge-literal]] - broader topic: Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  180  An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and ope ... [truncated] (5 shared statement(s))
- [[javascriptallonge-quasi]] - broader topic: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  180  An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and ope ... [truncated] (5 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-string]] - shared statements: String shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  180  An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and ope ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
