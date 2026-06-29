---
page_id: javascriptallonge-code
page_kind: concept
summary: Code: 15 statement(s) and 14 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-code@437d5c80d9b5bea03b2aca3fa0289519
---

# Code

What [[javascriptallonge]] covers about code:

## Statements

### A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

- Choices in software development must also consider the question of consistency. If a particular codebase is written with lots of helper functions that place the subject first, like this: _(javascriptallonge.pdf (source-range-7239e085-00057))_

### A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't. / how this book is organized

- JavaScript Allongé introduces new aspects of programming with functions in each chapter, explaining exactly how JavaScript works. Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use. _(javascriptallonge.pdf (source-range-7239e085-00065))_

### Or even: / back on the block

- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-7239e085-00246))_

### And also: / Naming Functions / function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-7239e085-00548))_

### And also: / Combinators and Function Decorators / a balanced statement about combinators

- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf , addOne , and compose ) while avoiding language keywords and the names of nouns (like number ). So one perspective is that combinators are useful when you want to emphasize what you're doing and how it fits together, and more explicit code is useful when you want to emphasize what you're working with. _(javascriptallonge.pdf (source-range-7239e085-00568))_

### And also: / Building Blocks / partial application

- Code is easier than words for this. The Underscore 39 library provides a higher-order function called map . 40 It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-7239e085-00592))_

### Recipes with Basic Functions / Maybe

- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-7239e085-00708))_

### Yes. Consider this variation:

- In this book, we will use function declarations sparingly, and not use var at all. That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. The purpose of your own code is to get things done. The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-7239e085-01221))_

### Yes. Consider this variation: / Copy on Write / copy-on-write

- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-7239e085-01255))_

### Yes. Consider this variation: / Making Data Out Of Functions

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-7239e085-01328))_

### Like this: / iterables

- So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-7239e085-01555))_

### We'll keep it simple: / generators are coroutines

- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-7239e085-01706))_

### We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

- This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-7239e085-01791))_

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

- Christine interrupted. 'To save time, we have written a template of the solution for you in ECMASCript 2015 notation. Fill in the blanks. Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. You may use babeljs.io 95 , or ES6Fiddle 96 to check your work. ' _(javascriptallonge.pdf (source-range-7239e085-01821))_


## Technical atoms

### Technical frame 1: A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00059))_

> Then it can be jarring to add new helpers written that place the verb first, like this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00058))_

```
const mapWith = (iterable, fn) =>
({
[Symbol.iterator]: function* () {
for (let element of iterable) {
yield fn(element);
}
}
});
```

### Technical frame 2: Or even: / back on the block

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

### Technical frame 3: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00248))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 4: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00593))_

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Technical frame 5: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00596))_

```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Technical frame 6: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00700))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00699))_

```
var something =
isSomething(value)
? doesntCheckForSomething(value)
: value;
```

### Technical frame 7: Yes. Consider this variation: / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01280))_

> What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01279))_

```
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const foldArrayWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldArrayWith(fn, terminalValue, rest));
const foldArray = (array) => callRight(foldArrayWith, array);
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
sumFoldable(foldArray([1, 4, 9, 16, 25]))
//=> 55
```

### Technical frame 8: Yes. Consider this variation: / Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01330))_

> A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01329))_

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest.first
//=> 2
OneTwoThree.rest.rest.first
//=> 3
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

### Technical frame 9: Yes. Consider this variation: / Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01333))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01336))_

```
const K = (x) => (y) => x;
const I = (x) => (x);
const V = (x) => (y) => (z) => z(x)(y);
```

### Technical frame 10: Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01413))_

> This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01412))_

```
const first = K,
second = K(I),
pair = (first) => (second) => {
const pojo = {first, second};
return (selector) => selector(pojo.first)(pojo.second);
};
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Technical frame 11: Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01416))_

> We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01415))_

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
```

### Technical frame 12: Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01419))_

> The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01418))_

```
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
```

### Technical atom 13

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

### Technical atom 14

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00152))_

| entry | content |
| --- | --- |
| 13 | http://en.wikipedia.org/wiki/Double-precision_floating-point_format |
| 14 | Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 . But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. |

<details>
<summary>Raw table text</summary>

```
13 http://en.wikipedia.org/wiki/Double-precision_floating-point_format
14 Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 . But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.
```

</details>


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated]; Function shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Javascript shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-language]] - shared statements and technical atoms: Language shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Language shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-follow]] - shared statements and technical atoms: Follow shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Follow shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-program]] - shared statements and technical atoms: Program shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Program shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-rule]] - shared statements and technical atoms: Rule shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Rule shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Write shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from And also: / Building Blocks / partial application: Code is easier than words for this. The Underscore 39 library provides a higher-order function called map . 40 It applies another function to each element of an array, like this:; partial application shares technical record from And also: / Building Blocks / partial application: _.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-programmer]] - shared statements and technical atoms: Programmer shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Programmer shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from We'll keep it simple: / Lazy and Eager Collections / lazy collection operations: This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iterati ... [truncated]; Return shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (3 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms: Length shares technical record from Yes. Consider this variation: / Making Data Out Of Functions: const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest.first //=> 2 One ... [truncated] (3 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Building Blocks / partial application: _.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9] (2 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking: const length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) ); (2 shared atom(s))
- [[javascriptallonge-allong]] - shared technical atoms: Allong shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-different]] - shared technical atoms: Different shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared technical atoms: Ecmascript shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-evaluating]] - shared technical atoms: Evaluating shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-functional]] - shared technical atoms: Functional shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared technical atoms: Functional Iterators shares technical record from Yes. Consider this variation: / Functional Iterators: const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === unde ... [truncated] (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-pair]] - shared technical atoms: Pair shares technical record from Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking: const first = K, second = K(I), pair = (first) => (second) => { const pojo = {first, second}; return (selector) => selector(pojo.first)(pojo.second); }; const latin ... [truncated] (1 shared atom(s))
- [[javascriptallonge-programming]] - shared technical atoms: Programming shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-software]] - shared technical atoms: Software shares technical record from A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.: const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function* () { for (let element of iterable) { yield fn(element); } } }); (1 shared atom(s))
- [[javascriptallonge-type]] - shared technical atoms: Type shares technical table: 13 http://en.wikipedia.org/wiki/Double-precision_floating-point_format 14 Implementations of JavaScript are free to handle larger numbers. For example, if you type 9 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-writing]] - shared technical atoms: Writing shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-combinator]] - shared statements: Combinator shares source evidence from And also: / Combinators and Function Decorators / a balanced statement about combinators: Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf , addOne , and compose ) while avoiding language keywords and the names of nou ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from And also: / Naming Functions / function declaration caveats 34: Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the fol ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from Like this: / iterables: So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict wi ... [truncated] (1 shared statement(s))
- [[javascriptallonge-operation]] - shared statements: Operation shares source evidence from Recipes with Basic Functions / Maybe: If some code ever tries to call model.setSomething with nothing, the operation will be skipped. (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-purpose]] - shared statements: Purpose shares source evidence from Yes. Consider this variation:: In this book, we will use function declarations sparingly, and not use var at all. That does not mean that you should follow the exact same practice in your own code ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
