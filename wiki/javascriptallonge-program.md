---
page_id: javascriptallonge-program
page_kind: concept
summary: Program: 23 statement(s) and 14 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-program@f363aec7d79623119ac3204e3788475e
---

# Program

What [[javascriptallonge]] covers about program:

## Statements

### why the 'six' edition?

- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-8eb13d6b-00022))_

- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write: _(javascriptallonge.pdf (source-range-8eb13d6b-00028))_

### michael fogus

- As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you'll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-8eb13d6b-00087))_

### A Rich Aroma: Basic Numbers

- In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.Wikipedia 12 _(javascriptallonge.pdf (source-range-8eb13d6b-00145))_

### void

- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

### Ah. I'd Like to Have an Argument, Please. 22

- Most programmers are perfectly familiar with arguments (often called 'parameters'). Secondary school mathematics discusses this. So you know what they are, and I know that you know what they are, but please be patient with the explanation! _(javascriptallonge.pdf (source-range-8eb13d6b-00274))_

### it's always the environment

- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-8eb13d6b-00369))_

### which came first, the chicken or the egg?

- The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-8eb13d6b-00386))_

### That Constant Coffee Craving

- Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-8eb13d6b-00388))_

### inside-out

- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-8eb13d6b-00407))_

### higher-order functions

- This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-8eb13d6b-00568))_

### Maybe

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-8eb13d6b-00695))_

### truthiness and operators

- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-8eb13d6b-00779))_

### Garbage, Garbage Everywhere

- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today's standards. Although the 704 used core memory, it still used vacuum tubes for its logic. Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-8eb13d6b-01033))_

### Reassignment

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. We saw this earlier in rebinding: _(javascriptallonge.pdf (source-range-8eb13d6b-01161))_

### bonus

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-8eb13d6b-01315))_

### a look back at functional iterators

- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-8eb13d6b-01542))_

### iterator objects

- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-8eb13d6b-01546))_

### generators are coroutines

- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-8eb13d6b-01685))_

- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-8eb13d6b-01690))_

- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-8eb13d6b-01695))_


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

### Technical frame 3: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00032))_

> The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn't to explain how to work around JavaScript's missing features: The intention was to explain why the style of programming exemplified by the missing features is important.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00031))_

```
function foo () { var first = arguments[0], rest = [].slice.call(arguments, 1); // ... }
```

### Technical frame 4: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00036))_

> And i is scoped to the for loop. We can also write:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00035))_

```
for ( let i = 0; i < array.length; ++i) { // ... }
```

### Technical frame 5: A Rich Aroma: Basic Numbers

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00149))_

> For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00148))_

> The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing 'under the hood.'

### Technical frame 6: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00250))_

```
(() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined
```

### Technical frame 7: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00251))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 8: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00368))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00367))_

```
(x, y, z) => x + y + z
```

### Technical frame 9: which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00386))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00385))_

```
// top of the file (() => { // ... lots of JavaScript ... })(); // bottom of the file
```

### Technical frame 10: inside-out

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00409))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00408))_

```
(diameter) => // ...
```

### Technical frame 11: higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00568))_

> This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00567))_

```
const compose = (a, b) => (c) => a(b(c)) Let's say we have: const addOne = (number) => number + 1; const doubleOf = (number) => number * 2; With compose , anywhere you would write const doubleOfAddOne = (number) => doubleOf(addOne(number)); You could also write: const doubleOfAddOne = compose(doubleOf, addOne);
```

### Technical frame 12: truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00779))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00778))_

```
!5 //=> false ! undefined //=> true
```

### Technical frame 13: bonus

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01318))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01317))_

```
const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);
```

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00239))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00237))_

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

- [[javascriptallonge-programmer]] - shared statements and technical atoms: Programmer shares source evidence from why the 'six' edition?: Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did ... [truncated]; Programmer shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (8 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Javascript shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (5 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-language]] - shared statements and technical atoms: Language shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Language shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (8 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-programming]] - shared statements and technical atoms: Programming shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Programming shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (10 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Function shares technical record from why the 'six' edition?: def foo (first, *rest) # ... end (4 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Write shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-code]] - shared statements and technical atoms: Code shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Code shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from it's always the environment: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial applicatio ... [truncated]; Evaluate shares technical record from it's always the environment: (x, y, z) => x + y + z (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-behaviour]] - shared statements and technical atoms: Behaviour shares source evidence from truthiness and operators: Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is ... [truncated]; Behaviour shares technical record from truthiness and operators: !5 //=> false ! undefined //=> true (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared technical atoms: Ecmascript shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (3 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from why the 'six' edition?: for ( let i = 0; i < array.length; ++i) { // ... } (3 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from truthiness and operators: !5 //=> false ! undefined //=> true (2 shared atom(s))
- [[javascriptallonge-block]] - shared technical atoms: Block shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (2 shared atom(s))
- [[javascriptallonge-follow]] - shared technical atoms: Follow shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-alway]] - shared technical atoms: Alway shares technical record from truthiness and operators: !5 //=> false ! undefined //=> true (1 shared atom(s))
- [[javascriptallonge-evaluating]] - shared technical atoms: Evaluating shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-literal]] - shared technical atoms: Literal shares technical record from A Rich Aroma: Basic Numbers: The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the comp ... [truncated] (1 shared atom(s))
- [[javascriptallonge-pattern]] - shared technical atoms: Pattern shares technical record from inside-out: (diameter) => // ... (1 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (1 shared atom(s))
- [[javascriptallonge-rest]] - shared statements: Rest shares source evidence from generators are coroutines: The rest of the program continues along its way until it makes another call to iterator.next() . (3 shared statement(s))
- [[javascriptallonge-functional]] - shared statements: Functional shares source evidence from michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated] (2 shared statement(s))
- [[javascriptallonge-algorithm]] - shared statements: Algorithm shares source evidence from Garbage, Garbage Everywhere: Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-allong]] - shared statements: Allong shares source evidence from michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated] (1 shared statement(s))
- [[javascriptallonge-collection]] - shared statements: Collection shares source evidence from iterator objects: In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be ... [truncated] (1 shared statement(s))
- [[javascriptallonge-different]] - shared statements: Different shares source evidence from That Constant Coffee Craving: Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, wher ... [truncated] (1 shared statement(s))
- [[javascriptallonge-functional-iterator]] - shared statements: Functional Iterators shares source evidence from a look back at functional iterators: If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an ... [truncated] (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from iterator objects: In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be ... [truncated] (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from Maybe: A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'some ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
