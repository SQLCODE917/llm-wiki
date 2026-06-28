---
page_id: javascriptallonge-string
page_kind: concept
summary: String: 9 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-string@baf45e6d67aa513dcf9174ed0fa62511
---

# String

What [[javascriptallonge]] covers about string:

## Statements

### values are expressions

- xv

Prelude: Values and Expressions over Coffee

Now we see that “strings” are values, and you can make an expression out of strings and an operator +. Since strings are values, they are also expressions by themselves. But strings with operators are not values, they are expressions. Now we know what was missing with our “coffee grounds plus hot water” example. The coffee grounds were a value, the boiling hot water was a value, and the “plus” operator between them made the whole thing an expression that was not a value. _(javascriptallonge.pdf (source-range-83ecb080-00031))_

### values and identity

- xvi

Prelude: Values and Expressions over Coffee

## **values and identity**

In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:

2 === 2 _//=> true_ 'hello' !== 'goodbye' _//=> true_

How does === work, exactly? Imagine that you’re shown a cup of coffee. And then you’re shown another cup of coffee. Are the two cups “identical?” In JavaScript, there are four possibilities:

First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different _types_ . For example, the string "2" is not the same thing as the number 2. Strings and numbers are different types, so strings and numbers are never identical:

2 === '2' _//=> false_ **true** !== 'true' _//=> true_

Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2.

**true** === **false** _//=> false_ 2 !== 5 _//=> true_ 'two' === 'five' _//=> false_

What if the cups are of the same type _and_ the contents are the same? Well, JavaScript’s third and fourth possibilities cover that. _(javascriptallonge.pdf (source-range-83ecb080-00033))_

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

7

## **As Little As Possible About Functions, But No Less**

In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let’s start with the second simplest possible function.[16] In JavaScript, it looks like this:

## () => 0

This is a function that is applied to no values and returns 0. Let’s verify that our function is a value like all others:

- (() => 0) _//=> [Function]_ What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else.

> 16 The simplest possible function is () => {}, we’ll see that later. _(javascriptallonge.pdf (source-range-83ecb080-00044))_

- The first sip: Basic Functions

11

## **the simplest possible block**

There’s another thing we can put to the right of an arrow, a _block_ . A block has zero or more _statements_ , separated by semicolons.[18] So, this is a valid function:

## () => {}

It returns the result of evaluating a block that has no statements. What would that be? Let’s try it: (() => {})() _//=> undefined_

What is this undefined?

## **undefined**

In JavaScript, the absence of a value is written undefined, and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type:

## **undefined**

_//=> undefined_

Like numbers, booleans and strings, JavaScript can print out the value undefined.

**undefined** === **undefined**

_//=> true_ (() => {})() === (() => {})() _//=> true_ (() => {})() === **undefined** _//=> true_

No matter how you evaluate undefined, you get an identical value back. undefined is a value that means “I don’t have a value.” But it’s still a value :-)

> 18Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it’s helpful to know it exists. _(javascriptallonge.pdf (source-range-83ecb080-00048))_

### Arrays and Destructuring Arguments

- Composing and Decomposing Data

78

## **Arrays and Destructuring Arguments**

While we have mentioned arrays briefly, we haven’t had a close look at them. Arrays are JavaScript’s “native” representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality.

## **array literals**

JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: [] _//=> []_ We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. Whitespace is optional:

[1] _//=> [1]_ [2, 3, 4] _//=> [2,3,4]_ Any expression will work:

[ 2, 3, 2 + 2 ] _//=> [2,3,4]_ Including an expression denoting another array: [[[[[]]]]] This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

Any expression will do, including names: _(javascriptallonge.pdf (source-range-83ecb080-00124))_

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


## Related pages

- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  11  ## **the simplest possible block**  There’s another thing we can put to the right of an arrow, a _block_ . A block has zero or mo ... [truncated] (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements: Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  180  An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and ope ... [truncated] (1 shared statement(s))
- [[javascriptallonge-operator]] - shared statements: Operator shares source evidence from values are expressions: xv  Prelude: Values and Expressions over Coffee  Now we see that “strings” are values, and you can make an expression out of strings and an operator +. Since strings ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  180  An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and ope ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi-literal]] - shared statements: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  180  An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and ope ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
