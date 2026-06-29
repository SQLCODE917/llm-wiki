---
page_id: javascriptallonge-program
page_kind: concept
summary: Program: 23 statement(s) and 16 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-program@c83cdc04582b70632bab93f917483522
---

# Program

What [[javascriptallonge]] covers about program:

## Statements

### A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-7239e085-00022))_

- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write: _(javascriptallonge.pdf (source-range-7239e085-00028))_

### ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus

- As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you'll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-7239e085-00087))_

### A Rich Aroma: Basic Numbers

- In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.Wikipedia 12 _(javascriptallonge.pdf (source-range-7239e085-00141))_

### Or even: / back on the block

- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-7239e085-00246))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22

- Most programmers are perfectly familiar with arguments (often called 'parameters'). Secondary school mathematics discusses this. So you know what they are, and I know that you know what they are, but please be patient with the explanation! _(javascriptallonge.pdf (source-range-7239e085-00271))_

### And also: / Closures and Scope / it's always the environment

- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-7239e085-00366))_

### And also: / Closures and Scope / which came first, the chicken or the egg?

- The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-7239e085-00383))_

### And also: / That Constant Coffee Craving

- Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-7239e085-00385))_

### And also: / That Constant Coffee Craving / inside-out

- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-7239e085-00404))_

### And also: / Combinators and Function Decorators / combinators

- This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-7239e085-00566))_

### Recipes with Basic Functions / Maybe

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-7239e085-00695))_

### Picking the Bean: Choice and Truthiness / truthiness and operators

- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-7239e085-00779))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today's standards. Although the 704 used core memory, it still used vacuum tubes for its logic. Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-7239e085-01034))_

### Composing and Decomposing Data / Reassignment

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. We saw this earlier in rebinding: _(javascriptallonge.pdf (source-range-7239e085-01162))_

### Yes. Consider this variation: / Functional Iterators / bonus

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-7239e085-01316))_

### Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-7239e085-01543))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects

- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-7239e085-01547))_

### We'll keep it simple: / generators are coroutines

- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-7239e085-01686))_

- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-7239e085-01691))_

- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-7239e085-01696))_


## Technical atoms

### Technical frame 1: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00028))_

> Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00026))_

```
var i;
for (i = 0; i < array.length; ++i) {
(function (i) {
// ...
})(i)
}
```

### Technical frame 2: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00030))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00029))_

```
def foo (first, *rest)
# ...
end
```

### Technical frame 3: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00032))_

> The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn't to explain how to work around JavaScript's missing features: The intention was to explain why the style of programming exemplified by the missing features is important.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00031))_

```
function foo () {
var first = arguments[0],
rest
= [].slice.call(arguments, 1);
// ...
}
```

### Technical frame 4: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00036))_

> And i is scoped to the for loop. We can also write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00035))_

```
for (let i = 0; i < array.length; ++i) {
// ...
}
```

### Technical frame 5: A Rich Aroma: Basic Numbers

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00145))_

> For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00144))_

> The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing 'under the hood.'

### Technical frame 6: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00247))_

```
(() => 2 + 2)()
//=> 4
(() => { 2 + 2 })()
//=> undefined
(() => (1 + 1, 2 + 2))()
//=> 4
(() => { 1 + 1; 2 + 2 })()
//=> undefined
```

### Technical frame 7: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00248))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 8: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00365))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00364))_

```
(x, y, z) => x + y + z
```

### Technical frame 9: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00383))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00382))_

```
// top of the file
(() => {
// ... lots of JavaScript ...
})();
// bottom of the file
```

### Technical frame 10: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00406))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00405))_

```
(diameter) =>
// ...
```

### Technical frame 11: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00454))_

> We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00453))_

```
((diameter_fn) =>
diameter_fn(2)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

### Technical frame 12: And also: / Combinators and Function Decorators / combinators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00566))_

> This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00565))_

```
const compose = (a, b) =>
(c) => a(b(c))
Let’s say we have:
const addOne = (number) => number + 1;
const doubleOf = (number) => number * 2;
With compose, anywhere you would write
const doubleOfAddOne = (number) => doubleOf(addOne(number));
You could also write:
const doubleOfAddOne = compose(doubleOf, addOne);
```

### Technical frame 13: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00779))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00778))_

```
!5
//=> false
!undefined
//=> true
```

### Technical frame 14: Yes. Consider this variation: / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01319))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01318))_

```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

### Technical atom 15

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00091))_

| entry | content |
| --- | --- |
| 5 | http://www.fogus.me Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it's over too soon. Enjoy! -Matthew Knox, mattknox.com 6 |
| 6 | http://mattknox.com |

<details>
<summary>Raw table text</summary>

```
matthew knox
A different kind of language requires a different kind of book.
JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many books try to hide most of those capabilities away, giving you recipes for writing JavaScript in a way that approximates class-centric programming in other languages. Not JavaScript Allongé. It starts with the fundamentals of values, functions, and objects, and then guides you through JavaScript from the inside with exploratory bits of code that illustrate scoping, combinators, context, state, prototypes, and constructors.
5 http://www.fogus.me
Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it's over too soon. Enjoy!
-Matthew Knox, mattknox.com 6
6 http://mattknox.com
```

</details>

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00236))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00234))_

| entry | content |
| --- | --- |
| 19 | Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace. |
| 20 | As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea. |

<details>
<summary>Raw table text</summary>

```
back on the block
Back to our function. We evaluated this:
19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace.
20 As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea.
```

</details>


## Related pages

- [[javascriptallonge-programmer]] - shared statements and technical atoms: Programmer shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did ... [truncated]; Programmer shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (8 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Javascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (5 shared statement(s), 10 shared atom(s))
- [[javascriptallonge-language]] - shared statements and technical atoms: Language shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Language shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (8 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-programming]] - shared statements and technical atoms: Programming shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Programming shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (10 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Function shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: def foo (first, *rest) # ... end (4 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-code]] - shared statements and technical atoms: Code shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Code shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Write shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from And also: / Closures and Scope / it's always the environment: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial applicatio ... [truncated]; Evaluate shares technical record from And also: / Closures and Scope / it's always the environment: (x, y, z) => x + y + z (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-functional]] - shared statements and technical atoms: Functional shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Functional shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Yes. Consider this variation: / Functional Iterators / bonus: Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smallta ... [truncated]; Functional Iterators shares technical record from Yes. Consider this variation: / Functional Iterators / bonus: const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1); (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-allong]] - shared statements and technical atoms: Allong shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Allong shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-behaviour]] - shared statements and technical atoms: Behaviour shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and operators: Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is ... [truncated]; Behaviour shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-combinator]] - shared statements and technical atoms: Combinator shares source evidence from And also: / Combinators and Function Decorators / combinators: This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way T ... [truncated]; Combinator shares technical record from And also: / Combinators and Function Decorators / combinators: const compose = (a, b) => (c) => a(b(c)) Let’s say we have: const addOne = (number) => number + 1; const doubleOf = (number) => number * 2; With compose, anywhere yo ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-different]] - shared statements and technical atoms: Different shares source evidence from And also: / That Constant Coffee Craving: Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, wher ... [truncated]; Different shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be ... [truncated]; Object shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared technical atoms: Ecmascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (4 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: for (let i = 0; i < array.length; ++i) { // ... } (4 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (3 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (3 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (2 shared atom(s))
- [[javascriptallonge-block]] - shared technical atoms: Block shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (2 shared atom(s))
- [[javascriptallonge-follow]] - shared technical atoms: Follow shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-alway]] - shared technical atoms: Alway shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from And also: / That Constant Coffee Craving / const and lexical scope: ((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) //=> 6.2831853 (1 shared atom(s))
- [[javascriptallonge-evaluating]] - shared technical atoms: Evaluating shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-literal]] - shared technical atoms: Literal shares technical record from A Rich Aroma: Basic Numbers: The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the comp ... [truncated] (1 shared atom(s))
- [[javascriptallonge-operation]] - shared technical atoms: Operation shares technical record from Yes. Consider this variation: / Functional Iterators / bonus: const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1); (1 shared atom(s))
- [[javascriptallonge-pattern]] - shared technical atoms: Pattern shares technical record from And also: / That Constant Coffee Craving / inside-out: (diameter) => // ... (1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (1 shared atom(s))
- [[javascriptallonge-writing]] - shared technical atoms: Writing shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-rest]] - shared statements: Rest shares source evidence from We'll keep it simple: / generators are coroutines: The rest of the program continues along its way until it makes another call to iterator.next() . (3 shared statement(s))
- [[javascriptallonge-algorithm]] - shared statements: Algorithm shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-collection]] - shared statements: Collection shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be ... [truncated] (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from Recipes with Basic Functions / Maybe: A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'some ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
