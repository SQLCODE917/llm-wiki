---
page_id: javascriptallonge-string
page_kind: concept
summary: String: 7 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-string@731ae0ca9826e64012fa20d19f39c0ef
---

# String

What [[javascriptallonge]] covers about string:

## Statements

### Prelude: Values and Expressions over Coffee / values and identity

- First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical: _(javascriptallonge.pdf (source-range-7239e085-00118))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-7239e085-00168))_

### Or even: / the simplest possible block / undefined

- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-7239e085-00220))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-7239e085-00322))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments

- While we have mentioned arrays briefly, we haven't had a close look at them. Arrays are JavaScript's 'native' representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-7239e085-00818))_

### A Warm Cup: Basic Strings and Quasi-Literals

- String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. _(javascriptallonge.pdf (source-range-7239e085-01503))_

### A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

- JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-7239e085-01505))_


## Technical atoms

### Technical frame 1: Prelude: Values and Expressions over Coffee / values and identity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00120))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00119))_

```
2 === '2'
//=> false
true !== 'true'
//=> true
```

### Technical frame 2: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00126))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00125))_

```
2 + 2 === 4
//=> true
(2 + 2 === 4) === (2 !== 5)
//=> true
```

### Technical frame 3: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00129))_

> Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00127))_

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical frame 4: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00170))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00169))_

```
() => 0
```

### Technical frame 5: A Warm Cup: Basic Strings and Quasi-Literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01503))_

> String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01502))_

```
'fu' + 'bar'
//=> 'fubar'
```

### Technical frame 6: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01507))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01506))_

```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```


## Related pages

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Or even: / the simplest possible block / undefined: Like numbers, booleans and strings, JavaScript can print out the value undefined .; Javascript shares technical record from Prelude: Values and Expressions over Coffee / values and identity: 2 === '2' //=> false true !== 'true' //=> true (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-type]] - shared statements and technical atoms: Type shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated]; Type shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated]; Value shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Literal shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-quasi]] - shared statements and technical atoms: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Quasi shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-quasi-literal]] - shared statements and technical atoms: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Quasi Literal shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-note]] - shared technical atoms: Note shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (2 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less: () => 0 (1 shared atom(s))

## Source

- [[javascriptallonge]]
