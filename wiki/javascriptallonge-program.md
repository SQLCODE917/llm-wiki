---
page_id: javascriptallonge-program
page_kind: concept
summary: Program: 25 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-program@e5c3e9efa5b09ca060fa109c4a6a841b
---

# Program

What [[javascriptallonge]] covers about program:

## Statements

- As we’ll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-83ecb080-00538))_
- Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation: _(javascriptallonge.pdf (source-range-83ecb080-00794))_
- Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. _(javascriptallonge.pdf (source-range-83ecb080-00049))_
- As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- As a staunch advocate of functional programming, much of what Reg has written rings true to me. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- > 20As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined. _(javascriptallonge.pdf (source-range-83ecb080-00341))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Most programmers are perfectly familiar with arguments (often called “parameters”). _(javascriptallonge.pdf (source-range-83ecb080-00392))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. _(javascriptallonge.pdf (source-range-83ecb080-00543))_
- > 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- While some programmers believe “There Should Only Be One Way To Do It,” having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-83ecb080-00803))_
- A common problem in programming is checking for null or undefined (hereafter called “nothing,” while all other values including 0, [] and false will be called “something”). _(javascriptallonge.pdf (source-range-83ecb080-01001))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. _(javascriptallonge.pdf (source-range-83ecb080-01128))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Like some imperative programming languages, JavaScript allows you to re-assign the value bound : to parameters. _(javascriptallonge.pdf (source-range-83ecb080-01758))_
- Many programmers coming to JavaScript from other languages are familiar with three “canonical” operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. _(javascriptallonge.pdf (source-range-83ecb080-02393))_
- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02626))_
- The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02631))_
- The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02636))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00051))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00052))_

> **function** foo () { **var** first = arguments[0], rest = [].slice.call(arguments, 1); _// ..._ }

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00055))_

> But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. With ECMASCript 2015, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00056))_

> **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00627, source-range-83ecb080-00632))_

> It’s more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we’ve elided. We can use any expression in there, and that expression can invoke diameter_fn. For example: This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI, we don’t need to know where dia

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00630))_

> ((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00794))_

> Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00795))_

> - **const** compose = (a, b) => (c) => a(b(c))

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01530))_

> > 66Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. 67https://en.wikipedia.org/wiki/IBM_704

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01533))_

> If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.


## Related pages

- [[javascriptallonge-language]] - shared statements and technical atoms (9 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (4 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-combinator]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-function]] - shared statements (4 shared statement(s))
- [[javascriptallonge-rest]] - shared statements (3 shared statement(s))
- [[javascriptallonge-write]] - shared statements (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements (1 shared statement(s))
- [[javascriptallonge-collection]] - shared statements (1 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
