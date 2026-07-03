---
page_id: javascriptallonge-quasi
page_kind: concept
page_family: topic-concept
summary: Quasi: 4 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-quasi@9d7ae5ee84f1ce0c58887e3121fb61b1
---

# Quasi

What [[javascriptallonge]] covers about quasi:

## Statements

### A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

- JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-7239e085-01505))_

- Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-7239e085-01507))_

- However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following: _(javascriptallonge.pdf (source-range-7239e085-01513))_

### A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-7239e085-01519))_


## Technical atoms

### Technical frame 1: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01507))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01506))_

<a id="atom-technical-atom-d1c1badbce303be3"></a>

```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```

### Technical frame 2: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01512))_

<a id="atom-technical-atom-53001ff2df5804aa"></a>

```
'A popular number for nerds is ' + (40 + 2)
//=> 'A popular number for nerds is 42'
```

### Technical frame 3: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01514))_

<a id="atom-technical-atom-9826aa7ca28708d6"></a>

```
'A popular number for nerds is' + (40 + 2)
//=> 'A popular number for nerds is42'
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Literal shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (4 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (3 shared atom(s))
- [[javascriptallonge-string]] - shared statements and technical atoms: String shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; String shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 1 shared atom(s))

### Shared claims

- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))

### Topics

- [[javascriptallonge-quasi-literal]] - narrower topic: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Quasi Literal shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (4 shared statement(s), 3 shared atom(s))

## Source

- [[javascriptallonge]]
