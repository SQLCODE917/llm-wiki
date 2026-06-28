---
page_id: javascriptallonge-string
page_kind: concept
summary: String: 7 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-string@add9f8cbd6ec99e6b5863ea40c41d072
---

# String

What [[javascriptallonge]] covers about string:

## Statements

### values and identity

- First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical: _(javascriptallonge.pdf (source-range-31a4cf47-00122))_

### As Little As Possible About Functions, But No Less

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-31a4cf47-00172))_

### undefined

- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-31a4cf47-00224))_

### call by sharing

- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-31a4cf47-00325))_

### Arrays and Destructuring Arguments

- While we have mentioned arrays briefly, we haven't had a close look at them. Arrays are JavaScript's 'native' representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-31a4cf47-00818))_

### A Warm Cup: Basic Strings and Quasi-Literals

- String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. _(javascriptallonge.pdf (source-range-31a4cf47-01503))_

### quasi-literals

- JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-31a4cf47-01505))_


## Technical atoms

### Technical frame 1: values and identity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00124))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00123))_

```
2 === '2' //=> false true !== 'true' //=> true
```

### Technical frame 2: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00174))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00173))_

```
() => 0
```

### Technical frame 3: A Warm Cup: Basic Strings and Quasi-Literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01503))_

> String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01502))_

```
'fu' + 'bar' //=> 'fubar'
```

### Technical frame 4: quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01507))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01506))_

```
`foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz'
```


## Related pages

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from undefined: Like numbers, booleans and strings, JavaScript can print out the value undefined .; Javascript shares technical record from values and identity: 2 === '2' //=> false true !== 'true' //=> true (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from As Little As Possible About Functions, But No Less: In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represen ... [truncated]; Array shares technical record from As Little As Possible About Functions, But No Less: () => 0 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Literal shares technical record from quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-quasi]] - shared statements and technical atoms: Quasi shares source evidence from quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Quasi shares technical record from quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from As Little As Possible About Functions, But No Less: () => 0 (1 shared atom(s))
- [[javascriptallonge-recall]] - shared statements: Recall shares source evidence from call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated] (1 shared statement(s))
- [[javascriptallonge-type]] - shared statements: Type shares source evidence from call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated] (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
