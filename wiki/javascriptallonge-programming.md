---
page_id: javascriptallonge-programming
page_kind: concept
summary: Programming: 10 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-programming@cfb8ddde97ad5c5b097ca9591d2c5fed
---

# Programming

What [[javascriptallonge]] covers about programming:

## Statements

### why the 'six' edition?

- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write: _(javascriptallonge.pdf (source-range-8eb13d6b-00028))_

### michael fogus

- As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you'll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-8eb13d6b-00087))_

### A Rich Aroma: Basic Numbers

- In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.Wikipedia 12 _(javascriptallonge.pdf (source-range-8eb13d6b-00145))_

### it's always the environment

- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-8eb13d6b-00369))_

### That Constant Coffee Craving

- Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-8eb13d6b-00388))_

### Maybe

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-8eb13d6b-00695))_

### Garbage, Garbage Everywhere

- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today's standards. Although the 704 used core memory, it still used vacuum tubes for its logic. Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-8eb13d6b-01033))_

### Reassignment

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. We saw this earlier in rebinding: _(javascriptallonge.pdf (source-range-8eb13d6b-01161))_


## Technical atoms

### Technical frame 1: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00028))_

> Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00026))_

```
var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) }
```

### Technical frame 2: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00030))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00029))_

```
def foo (first, *rest) # ... end
```

### Technical frame 3: A Rich Aroma: Basic Numbers

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00149))_

> For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00148))_

> The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing 'under the hood.'

### Technical frame 4: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00368))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00367))_

```
(x, y, z) => x + y + z
```


## Related pages

- [[javascriptallonge-program]] - shared statements and technical atoms: Program shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Program shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (10 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-language]] - shared statements and technical atoms: Language shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Language shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (6 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Function shares technical record from why the 'six' edition?: def foo (first, *rest) # ... end (4 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Javascript shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from it's always the environment: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial applicatio ... [truncated]; Evaluate shares technical record from it's always the environment: (x, y, z) => x + y + z (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-block]] - shared technical atoms: Block shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared technical atoms: Ecmascript shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (1 shared atom(s))
- [[javascriptallonge-literal]] - shared technical atoms: Literal shares technical record from A Rich Aroma: Basic Numbers: The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the comp ... [truncated] (1 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (1 shared atom(s))
- [[javascriptallonge-functional]] - shared statements: Functional shares source evidence from michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated] (2 shared statement(s))
- [[javascriptallonge-algorithm]] - shared statements: Algorithm shares source evidence from Garbage, Garbage Everywhere: Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-allong]] - shared statements: Allong shares source evidence from michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated] (1 shared statement(s))
- [[javascriptallonge-different]] - shared statements: Different shares source evidence from That Constant Coffee Craving: Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, wher ... [truncated] (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from Maybe: A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'some ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
