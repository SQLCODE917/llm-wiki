---
page_id: javascriptallonge-literal
page_kind: concept
summary: Literal: 9 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-literal@bdee7512f1b71e2e66d81bb6523488a9
---

# Literal

What [[javascriptallonge]] covers about literal:

## Statements

### A Rich Aroma: Basic Numbers

- ## **A Rich Aroma: Basic Numbers**

**==> picture [469 x 352] intentionally omitted <==**

**Mathematics and Coffee**

In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.— Wikipedia[12] JavaScript, like most languages, has a collection of literals. We saw that an expression consisting solely of numbers, like 42, is a literal. It represents the number forty-two, which is 42 base 10. Not

> 12https://en.wikipedia.org/wiki/Literal_(computer_programming) _(javascriptallonge.pdf (source-range-83ecb080-00037))_

- A Rich Aroma: Basic Numbers

2 all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actually 34 base 10.

Internally, both 042 and 34 have the same representation, as double-precision floating point[13] numbers. A computer’s internal representation for numbers is important to understand. The machine’s representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer’s behaviour surprises us if we don’t know a little about what it’s doing “under the hood.” For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1. Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

## **floating**

Most programmers never encounter the limit on the magnitude of an integer. But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers.

It’s tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, “Nooooooooooooooooooooo.” A computer’s internal representation for a floating point number is binary, while our literal number was in base ten. This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2.

One of the most oft-repeated examples is this:

- 1.0 _//=> 1_

- 1.0 + 1.0 _//=> 2_

- 1.0 + 1.0 + 1.0 _//=> 3_ However:

> 13http://en.wikipedia.org/wiki/Double-precision_floating-point_format

> 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. _(javascriptallonge.pdf (source-range-83ecb080-00038))_

### That Constant Coffee Craving

- 27

The first sip: Basic Functions ((diameter) => diameter * 3.14159265)(2) _//=> 6.2831853_

((PI) => (diameter) => diameter * PI )(3.14159265)(2) _//=> 6.2831853_ That works! We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind.[29]

## **inside-out**

There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: (diameter) => ((PI) => diameter * PI)(3.14159265) It produces the same result as our previous expressions for a diameter-calculating function: ((diameter) => diameter * 3.14159265)(2) _//=> 6.2831853_ ((PI) => (diameter) => diameter * PI )(3.14159265)(2) _//=> 6.2831853_ ((diameter) => ((PI) => diameter * PI)(3.14159265))(2) _//=> 6.2831853_ Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A “magic literal” like 3.14159265 is anathema to sustainable software development.

The third one is easiest for most people to read. It separates concerns nicely: The “outer” function describes its parameters:

> 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated “IIFE.” _(javascriptallonge.pdf (source-range-83ecb080-00063))_

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

- [[javascriptallonge-quasi-literal]] - narrower topic: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  180  An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and ope ... [truncated] (5 shared statement(s))
- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  180  An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and ope ... [truncated] (5 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-start]] - shared statements: Start shares source evidence from A Rich Aroma: Basic Numbers: A Rich Aroma: Basic Numbers  2 all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actuall ... [truncated] (1 shared statement(s))
- [[javascriptallonge-string]] - shared statements: String shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  180  An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and ope ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
