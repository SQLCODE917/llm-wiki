---
page_id: javascriptallonge-language
page_kind: concept
summary: Language: 15 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-language@74f24304d5921376dff85fe5bebbaa0b
---

# Language

What [[javascriptallonge]] covers about language:

## Statements

### Forewords to the First Edition

- ix

A Pull of the Lever: Prefaces

## **Forewords to the First Edition**

## **michael fogus**

As a life-long bibliophile and long-time follower of Reg’s online work, I was excited when he started writing books. However, I’m very conservative about books – let’s just say that if there was an aftershave scented to the essence of “Used Book Store” then I would be first in line to buy. So as you might imagine I was “skeptical” about the decision to release JavaScript Allongé as an ongoing ebook, with a pay-what-you-want model. However, Reg sent me a copy of his book and I was humbled. Not only was this a great book, but it was also a great way to write and distribute books. Having written books myself, I know the pain of soliciting and receiving feedback.

The act of writing is an iterative process with (very often) tight revision loops. However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. On more than one occasion I’ve found myself attempting to reify feedback with content that either no longer existed or was changed beyond recognition. However, with the Leanpub model the read-feedback-change process is extremely efficient, leaving in its wake a quality book that continues to get better as others likewise read and comment into infinitude.

In the case of JavaScript Allongé, you’ll find the Leanpub model a shining example of effectiveness. Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. No matter how much of an expert you think you are, JavaScript Allongé has something to teach you… about coffee. I kid.

As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you’ll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time.

Enjoy.

– Fogus, fogus.me[5]

## **matthew knox**

A different kind of language requires a different kind of book.

JavaScript holds surprising depths–its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many

5http://www.fogus.me _(javascriptallonge.pdf (source-range-83ecb080-00022))_

### values are expressions

- xiv

Prelude: Values and Expressions over Coffee

## **values are expressions**

All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, “I want one of these.” The barista is no fool, she gives it straight back to you, and you get exactly what you want. Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista).

Let’s try this with something the computer understands easily:

## 42

Is this an expression? A value? Neither? Or both?

The answer is, this is both an expression _and_ a value.[10] The way you can tell that it’s both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano:

## 42

_//=> 42_

All values are expressions. That’s easy! Are there any other kinds of expressions? Sure! let’s go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let’s hand over some ground coffee plus some boiling water.

Astute readers will realize we’re omitting something. Congratulations! Take a sip of espresso. We’ll get to that in a moment.

Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn’t a value.[11] Boiling water is a value. Ground coffee is a value. Espresso is a value. Boiling water plus ground coffee is an expression.

Let’s try this as well with something else the computer understands easily:

> "JavaScript" + " " + "Allonge"

> _//=> "JavaScript Allonge"_

> 10Technically, it’s a _representation_ of a value using Base10 notation, but we needn’t worry about that in this book. You and I both understand that this means “42,” and so does the computer.

> 11In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. _(javascriptallonge.pdf (source-range-83ecb080-00030))_

### A Rich Aroma: Basic Numbers

- ## **A Rich Aroma: Basic Numbers**

**==> picture [469 x 352] intentionally omitted <==**

**Mathematics and Coffee**

In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.— Wikipedia[12] JavaScript, like most languages, has a collection of literals. We saw that an expression consisting solely of numbers, like 42, is a literal. It represents the number forty-two, which is 42 base 10. Not

> 12https://en.wikipedia.org/wiki/Literal_(computer_programming) _(javascriptallonge.pdf (source-range-83ecb080-00037))_

### As Little As Possible About Functions, But No Less

- 13

The first sip: Basic Functions

## (() => {})()

_//=> undefined_

We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] Something like: { statement[1] ; statement[2] ; statement[3] ; ... ; statement[n] } We haven’t discussed these _statements_ . What’s a statement?

There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: () => { 1 + 1; 2 + 2 } But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: (() => { 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:

> 21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00050))_

### Closures and Scope

- The first sip: Basic Functions

24

The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them.

> _a_ https://en.wikipedia.org/wiki/Currying

> _b_ https://en.wikipedia.org/wiki/Partial_application

## **shadowy variables from a shadowy planet**

An interesting thing happens when a variable has the same name as an ancestor environment’s variable. Consider:

- (x) => (x, y) => x + y

The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of: (x) => (x, y) => (w, z) => (w) => x + y + z

When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both ws. When a variable has the same name as an ancestor environment’s binding, it is said to _shadow_ the ancestor.

This is often a good thing.

## **which came first, the chicken or the egg?**

This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state.

But before we do so, there’s one final question: Where does the ancestry start? If there’s no other code in a file, what is (x) => x’s parent environment? _(javascriptallonge.pdf (source-range-83ecb080-00059))_

### That Constant Coffee Craving

- The first sip: Basic Functions

26

## **That Constant Coffee Craving**

Up to now, all we’ve really seen are _anonymous functions_ , functions that don’t have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we’ve seen so far is how to name arguments.

There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. Let’s revisit a very simple example: (diameter) => diameter * 3.14159265

What is this “3.14159265” number? PI[28] , obviously. We’d like to name it so that we can write something like: (diameter) => diameter * PI

In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. If we put our function expression in parentheses, we can apply it to the argument of 3.14159265:

((PI) => _// ????_ )(3.14159265) What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course:

((PI) => (diameter) => diameter * PI )(3.14159265) This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our “functions” are expressions. This one has a few more moving parts, that’s all. But we can use it just like (diameter) => diameter * 3.14159265.

Let’s test it:

28https://en.wikipedia.org/wiki/Pi _(javascriptallonge.pdf (source-range-83ecb080-00062))_

### Maybe

- Recipes with Basic Functions

63

## **Maybe**

A common problem in programming is checking for null or undefined (hereafter called “nothing,” while all other values including 0, [] and false will be called “something”). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing.

This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing: **const** isSomething = (value) => value !== **null** && value !== **void** 0; **const** checksForSomething = (value) => { **if** (isSomething(value)) { _// function's true logic_ } } Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: **var** something = isSomething(value) ? doesntCheckForSomething(value) : value;

Naturally, there’s a function decorator recipe for that, borrowed from Haskell’s maybe monad[50] , Ruby’s andand[51] , and CoffeeScript’s existential method invocation: **const** maybe = (fn) => **function** (...args) { **if** (args.length === 0) { **return** } **else** { **for** ( **let** arg **of** args) { **if** (arg == **null** ) **return** ; } > 50https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad > 51https://github.com/raganwald/andand _(javascriptallonge.pdf (source-range-83ecb080-00108))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

106

In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.

Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp’s basic data type is often said to be the list, but in actuality it was the “cons cell,” the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells.

Lists were represented as linked lists of cons cells, with each cell’s head pointing to an element and the tail pointing to another cons cell.

Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today’s standards. Although the 704 used core memory, it still used vacuum tubes for its logic. Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance.

Here’s the scheme in JavaScript, using two-element arrays to represent cons cells: **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;

We can make a list by calling cons repeatedly, and terminating it with null: **const** oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, **null** )))));

## oneToFive

_//=> [1,[2,[3,[4,[5,null]]]]]_ Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like: _(javascriptallonge.pdf (source-range-83ecb080-00155))_

- Composing and Decomposing Data

108

## **so why arrays**

If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation).

For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases.

## **summary**

Although we showed how to use tail calls to map and fold over arrays with [first, ...rest], in reality this is not how it ought to be done. But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-00157))_

### Reassignment

- Composing and Decomposing Data

125

## **Reassignment**

Like some imperative programming languages, JavaScript allows you to re-assign the value bound : to parameters. We saw this earlier in rebinding

By default, JavaScript permits us to _rebind_ new values to names bound with a parameter. For example, we can write: **const** evenStevens = (n) => { **if** (n === 0) { **return true** ; } **else if** (n == 1) { **return false** ; } **else** { n = n - 2; **return** evenStevens(n); } } evenStevens(42) _//=> true_

The line n = n - 2; _rebinds_ a new value to the name n. We will discuss this at much greater length in Reassignment, but long before we do, let’s try a similar thing with a name bound using const. We’ve already bound evenStevens using const, let’s try rebinding it: evenStevens = (n) => { **if** (n === 0) { **return true** ; } **else if** (n == 1) { **return false** ; } **else** { **return** evenStevens(n - 2); } } _//=> ERROR, evenStevens is read-only_ _(javascriptallonge.pdf (source-range-83ecb080-00177))_

### Functional Iterators

- Composing and Decomposing Data

152 **const** odds = () => { **let** number = 1; **return** () => { **const** value = number; number += 2; **return** {done: **false** , value}; } } **const** squareOf = callLeft(mapIteratorWith, (x) => x * x) toArray(take(squareOf(odds()), 5)) _//=> [1, 9, 25, 49, 81]_ We could also write a filter for iterators to accompany our mapping function: **const** filterIteratorWith = (fn, iterator) => () => { **do** { **const** {done, value} = iterator(); } **while** (!done && !fn(value)); **return** {done, value}; } **const** oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1); toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) _//=> [1, 9, 25, 49, 81]_ Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

## **bonus**

Many programmers coming to JavaScript from other languages are familiar with three “canonical” operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect, select, and detect.

We haven’t written anything that finds the first element of an iteration that meets a certain criteria. Or have we? _(javascriptallonge.pdf (source-range-83ecb080-00207))_

### Making Data Out Of Functions

- 165

Composing and Decomposing Data **const** reverse = (list, delayed = EMPTYLIST) => list( () => delayed, (aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed)) ); print(reverse(l123)); _//=> 3 2 1_ **const** mapWith = (fn, list, delayed = EMPTYLIST) => list( () => reverse(delayed), (aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed)) ); print(mapWith(x => x * x, reverse(l123))) _//=> 941_

We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else.

## **functions are not the real point**

There are lots of similar texts explaining how to construct complex semantics out of functions. You can establish that K and K(I) can represent true and false, model magnitudes with Church Numerals[79] or Surreal Numbers[80] , and build your way up to printing FizzBuzz.

The superficial conclusion reads something like this:

Functions are a fundamental building block of computation. They are “axioms” of combinatory logic, and can be used to compute anything that JavaScript can compute.

However, that is not the interesting thing to note here. Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. Knowing how to make a linked list out of functions is not really necessary for the working programmer. (Knowing that it can be done, on the other hand, is very important to understanding computer science.) Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons[81] of the electromagnetic force. It’s the QED of physics that underpins the Maxwell’s Equations of programming. Deeply important, but not practical when you’re building a bridge.

> 79https://en.wikipedia.org/wiki/Church_encoding

> 80https://en.wikipedia.org/wiki/Surreal_number

> 81https://en.wikipedia.org/wiki/Gauge_boson _(javascriptallonge.pdf (source-range-83ecb080-00221))_

### Iteration and Iterables

- Served by the Pot: Collections

188 **const** stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) **const** collectionSum = (collection) => { **const** iterator = collection.iterator(); **let** eachIteration, sum = 0; **while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 2015_

Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object’s scaffolding.

## **iterables**

People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it.

So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator.

To ensure that the method would not conflict with any existing code, JavaScript provides a _symbol_ . Symbols are unique constants that are guaranteed not to conflict with existing strings. Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols.[88] The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.

> 88 You can read more about JavaScript symbols in Axel Rauschmayer’s Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-83ecb080-00252))_

- Served by the Pot: Collections

200

## **summary**

Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. _Iterable_ ordered collections can be iterated over or gathered into another collection.

Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-00264))_


## Related pages

- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (6 shared statement(s))
- [[javascriptallonge-programming]] - shared statements: Programming shares source evidence from A Rich Aroma: Basic Numbers: ## **A Rich Aroma: Basic Numbers**  **==> picture [469 x 352] intentionally omitted <==**  **Mathematics and Coffee**  In computer science, a literal is a notation f ... [truncated] (5 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (2 shared statement(s))
- [[javascriptallonge-different]] - shared statements: Different shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (2 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Closures and Scope: The first sip: Basic Functions  24  The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its argument ... [truncated] (2 shared statement(s))
- [[javascriptallonge-programmer]] - shared statements: Programmer shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (2 shared statement(s))
- [[javascriptallonge-algorithm]] - shared statements: Algorithm shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  106  In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and ret ... [truncated] (1 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from Closures and Scope: The first sip: Basic Functions  24  The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its argument ... [truncated] (1 shared statement(s))
- [[javascriptallonge-expression]] - shared statements: Expression shares source evidence from values are expressions: xiv  Prelude: Values and Expressions over Coffee  ## **values are expressions**  All values are expressions. Say you hand the barista a café Cubano. Yup, you hand ov ... [truncated] (1 shared statement(s))
- [[javascriptallonge-functional]] - shared statements: Functional shares source evidence from Iteration and Iterables: Served by the Pot: Collections  200  ## **summary**  Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection fr ... [truncated] (1 shared statement(s))
- [[javascriptallonge-game]] - shared statements: Game shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from Iteration and Iterables: Served by the Pot: Collections  188 **const** stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) **const** collectionSum = (collection) => { **const** ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Iteration and Iterables: Served by the Pot: Collections  200  ## **summary**  Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection fr ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
