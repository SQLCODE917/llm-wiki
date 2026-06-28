---
page_id: javascriptallonge-language
page_kind: concept
summary: Language: 14 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-language@20ec650dbf620e3afe7dd610f2d2fb2f
---

# Language

What [[javascriptallonge]] covers about language:

## Statements

### why the 'six' edition?

- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write: _(javascriptallonge.pdf (source-range-31a4cf47-00028))_

### matthew knox

- A different kind of language requires a different kind of book. _(javascriptallonge.pdf (source-range-31a4cf47-00091))_

### A Rich Aroma: Basic Numbers

- In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.Wikipedia 12 _(javascriptallonge.pdf (source-range-31a4cf47-00145))_

### void

- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

### it's always the environment

- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-31a4cf47-00369))_

### That Constant Coffee Craving

- Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-31a4cf47-00388))_

### Maybe

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-31a4cf47-00695))_

### Garbage, Garbage Everywhere

- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today's standards. Although the 704 used core memory, it still used vacuum tubes for its logic. Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-31a4cf47-01033))_

### so why arrays

- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. _(javascriptallonge.pdf (source-range-31a4cf47-01057))_

### Reassignment

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. We saw this earlier in rebinding: _(javascriptallonge.pdf (source-range-31a4cf47-01162))_

### bonus

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-31a4cf47-01316))_

### functions are not the real point

- However, that is not the interesting thing to note here. Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. Knowing how to make a linked list out of functions is not really necessary for the working programmer. (Knowing that it can be done, on the other hand, is very important to understanding computer science.) _(javascriptallonge.pdf (source-range-31a4cf47-01404))_

### iterables

- So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-31a4cf47-01555))_

### summary

- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-31a4cf47-01621))_


## Technical atoms

### Technical frame 1: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00025))_

> And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00024))_

```
for ( int i = 0; i < array.length; ++i) { // ... }
```

### Technical frame 2: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00028))_

> Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00026))_

```
var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) }
```

### Technical frame 3: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00030))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00029))_

```
def foo (first, *rest) # ... end
```

### Technical frame 4: A Rich Aroma: Basic Numbers

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00149))_

> For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00148))_

> The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing 'under the hood.'

### Technical frame 5: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00250))_

```
(() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined
```

### Technical frame 6: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00251))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 7: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00368))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00367))_

```
(x, y, z) => x + y + z
```

### Technical frame 8: bonus

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01319))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01318))_

```
const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);
```

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00114))_

> Let's try this as well with something else the computer understands easily:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00116))_

| entry | content |
| --- | --- |
| 10 | Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer. |
| 11 | In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. |

<details>
<summary>Raw table text</summary>

```
10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer.
11 In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values.
```

</details>

### Technical atom 10

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00571))_

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) |

<details>
<summary>Raw table text</summary>

```
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

</details>


## Related pages

- [[javascriptallonge-program]] - shared statements and technical atoms: Program shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Program shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (8 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Javascript shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (6 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-programming]] - shared statements and technical atoms: Programming shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Programming shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (6 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Function shares technical record from why the 'six' edition?: def foo (first, *rest) # ... end (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-programmer]] - shared statements and technical atoms: Programmer shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Programmer shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-code]] - shared statements and technical atoms: Code shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Code shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Write shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from it's always the environment: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial applicatio ... [truncated]; Evaluate shares technical record from it's always the environment: (x, y, z) => x + y + z (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-block]] - shared technical atoms: Block shares technical record from why the 'six' edition?: for ( int i = 0; i < array.length; ++i) { // ... } (2 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-follow]] - shared technical atoms: Follow shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared technical atoms: Ecmascript shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (1 shared atom(s))
- [[javascriptallonge-evaluating]] - shared technical atoms: Evaluating shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-literal]] - shared technical atoms: Literal shares technical record from A Rich Aroma: Basic Numbers: The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the comp ... [truncated] (1 shared atom(s))
- [[javascriptallonge-needn]] - shared technical atoms: Needn shares technical table: 10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' ... [truncated] (1 shared atom(s))
- [[javascriptallonge-purpose]] - shared technical atoms: Purpose shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-statement]] - shared technical atoms: Statement shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical table: 10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' ... [truncated] (1 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-different]] - shared statements: Different shares source evidence from matthew knox: A different kind of language requires a different kind of book. (2 shared statement(s))
- [[javascriptallonge-algorithm]] - shared statements: Algorithm shares source evidence from Garbage, Garbage Everywhere: Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-functional]] - shared statements: Functional shares source evidence from summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (1 shared statement(s))
- [[javascriptallonge-functional-iterator]] - shared statements: Functional Iterators shares source evidence from summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from iterables: So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict wi ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
