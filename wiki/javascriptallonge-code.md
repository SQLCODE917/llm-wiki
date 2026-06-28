---
page_id: javascriptallonge-code
page_kind: concept
summary: Code: 17 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-code@ce3da8e1a686f532c98eb712b789058e
---

# Code

What [[javascriptallonge]] covers about code:

## Statements

### What JavaScript Allongé is. And isn't.

- vi

A Pull of the Lever: Prefaces

Choices in software development must also consider the question of consistency. If a particular codebase is written with lots of helper functions that place the subject first, like this: **const** mapWith = (iterable, fn) => ({ [Symbol.iterator]: **function** * () { **for** ( **let** element **of** iterable) { **yield** fn(element); } } }); Then it can be jarring to add new helpers written that place the verb first, like this: **const** filterWith = (fn, iterable) => ({ [Symbol.iterator]: **function** * () { **for** ( **let** element **of** iterable) { **if** (!!fn(element)) **yield** element; } } });

There are reasons why the second form is more flexible, especially when used in combination with partial application, but does that outweigh the benefit of having an entire codebase do everything consistently the first way or the second way?

Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. The use of source-code control systems with integrated diffing rewards making certain types of focused changes. The use of linters[1] makes checking for certain types of undesirable code very cheap. Debuggers encourage the use of functions with explicit or implicit names. Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation of automated test suites.

JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn’t a book about practicing, it’s a book about thinking.

## **how this book is organized**

_JavaScript Allongé_ introduces new aspects of programming with functions in each chapter, explaining exactly how JavaScript works. Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use.

1https://en.wikipedia.org/wiki/Lint_ _(javascriptallonge.pdf (source-range-83ecb080-00017))_

### A Rich Aroma: Basic Numbers

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

### As Little As Possible About Functions, But No Less

- 13

The first sip: Basic Functions

## (() => {})()

_//=> undefined_

We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] Something like: { statement[1] ; statement[2] ; statement[3] ; ... ; statement[n] } We haven’t discussed these _statements_ . What’s a statement?

There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: () => { 1 + 1; 2 + 2 } But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: (() => { 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:

> 21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00050))_

### That Constant Coffee Craving

- 43

The first sip: Basic Functions

( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:

( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })() The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript’s design to facilitate a certain style of programming where you put the main logic up front, and the “helper functions” at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const) is essential for working with production code.

## **function declaration caveats**[34]

Function declarations are formally only supposed to be made at what we might call the “top level” of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea:

34 A number of the caveats discussed here were described in Jyrly Zaytsev’s excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-83ecb080-00079))_

### Combinators and Function Decorators

- The first sip: Basic Functions

46

In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as arguments and return a function. We won’t be strict about using only previously defined combinators in their construction.

Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation:

- **const** compose = (a, b) => (c) => a(b(c)) Let’s say we have: **const** addOne = (number) => number + 1; **const** doubleOf = (number) => number * 2;

With compose, anywhere you would write **const** doubleOfAddOne = (number) => doubleOf(addOne(number));

You could also write: **const** doubleOfAddOne = compose(doubleOf, addOne);

This is, of course, just one example of many. You’ll find lots more perusing the recipes in this book. While some programmers believe “There Should Only Be One Way To Do It,” having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously.

## **a balanced statement about combinators**

Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf, addOne, and compose) while avoiding language keywords and the names of nouns (like number). So one perspective is that combinators are useful when you want to emphasize what you’re doing and how it fits together, and more explicit code is useful when you want to emphasize what you’re working with.

## **function decorators**

A _function decorator_ is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here’s a ridiculously simple decorator:[38] > 37As we’ll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.

> 38 We’ll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) _(javascriptallonge.pdf (source-range-83ecb080-00083))_

### Building Blocks

- The first sip: Basic Functions

48

## **Building Blocks**

When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks.

## **composition**

: One of the most basic of these building blocks is _composition_ **const** cookAndEat = (food) => eat(cook(food));

It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators: **const** compose = (a, b) => (c) => a(b(c)); **const** cookAndEat = compose(eat, cook);

If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument.

Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

- **const** actuallyTransfer= (from, to, amount) => _// do something_ **const** invokeTransfer = once(maybe(actuallyTransfer(...))); _(javascriptallonge.pdf (source-range-83ecb080-00086))_

- The first sip: Basic Functions

49

## **partial application**

Another basic building block is _partial application_ . When a function takes multiple arguments, we “apply” the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can’t get the final value, but we can get a function that represents _part_ of our application.

Code is easier than words for this. The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this:

_.map([1, 2, 3], (n) => n * n) _//=> [1, 4, 9]_ We don’t want to fool around writing _., so we can use it by writing:[41] This code implements a partial application of the map function by applying the function (n) => n * n as its second argument: **const** squareAll = (array) => map(array, (n) => n * n);

The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**const** mapWith = (fn) => (array) => map(array, fn); **const** squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) _//=> [1, 4, 9]_ We’ll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

> 39http://underscorejs.org

> 40Modern JavaScript implementations provide a map method for arrays, but Underscore’s implementation also works with older browsers if you are working with that headache.

> 41If we don’t want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven’t discussed methods yet. const map = _.map; _(javascriptallonge.pdf (source-range-83ecb080-00087))_

### Maybe

- Recipes with Basic Functions

64 **return** fn.apply( **this** , args) } } maybe reduces the logic of checking for nothing to a function call: maybe((a, b, c) => a + b + c)(1, 2, 3) _//=> 6_ maybe((a, b, c) => a + b + c)(1, **null** , 3) _//=> undefined_ As a bonus, maybe plays very nicely with instance methods, we’ll discuss those later: **function** Model () {};

Model.prototype.setSomething = maybe( **function** (value) { **this** .something = value; });

If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-83ecb080-00109))_

### Reassignment

- 134

Composing and Decomposing Data

Now we’re creating a new inner parameter, i and binding it to the value of the outer i. This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification.

In this book, we will use function declarations sparingly, and not use var at all. That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. The purpose of your own code is to get things done. The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-83ecb080-00186))_

### Copy on Write

- Composing and Decomposing Data

140

Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.— Wikipedia[73] Like all strategies, it makes a tradeoff: It’s much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren’t sharing, it’s more expensive.

Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we’re done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write.

> 73https://en.wikipedia.org/wiki/Copy-on-write _(javascriptallonge.pdf (source-range-83ecb080-00193))_

### Functional Iterators

- 147

Composing and Decomposing Data **const** arraySum = (array) => { **let** iter, sum = 0, index = 0; **while** ( (eachIteration = { done: index === array.length, value: index < array.length ? array[index] : **undefined** }, ++index, !eachIteration.done) ) { sum += eachIteration.value; } **return** sum; } arraySum([1, 4, 9, 16, 25]) _//=> 55_

With this code, we make a POJO that has done and value keys. All the summing code needs to know is to add eachIteration.value. Now we can extract the ickiness into a separate function: **const** arrayIterator = (array) => { **let** i = 0; **return** () => { **const** done = i === array.length; **return** { done, value: done ? **undefined** : array[i++] } } } **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0; **while** ((eachIteration = iterator(), !eachIteration.done)) { _(javascriptallonge.pdf (source-range-83ecb080-00202))_

### Making Data Out Of Functions

- Composing and Decomposing Data

154

## **Making Data Out Of Functions**

**==> picture [469 x 352] intentionally omitted <==**

**Coffee served at the CERN particle accelerator**

In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case.

For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-00210))_

### Iteration and Iterables

- Served by the Pot: Collections

188 **const** stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) **const** collectionSum = (collection) => { **const** iterator = collection.iterator(); **let** eachIteration, sum = 0; **while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 2015_

Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object’s scaffolding.

## **iterables**

People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it.

So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator.

To ensure that the method would not conflict with any existing code, JavaScript provides a _symbol_ . Symbols are unique constants that are guaranteed not to conflict with existing strings. Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols.[88] The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.

> 88 You can read more about JavaScript symbols in Axel Rauschmayer’s Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-83ecb080-00252))_

### Generating Iterables

- Served by the Pot: Collections

211 it “suspends” and the producer starts running. When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next().

Of course, generators need not be implemented exactly as coroutines. For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): **const** oneTwoThree = **function** () { **let** state = 'newborn'; **return** { next () { **switch** (state) { **case** 'newborn': state = 1; **return** {value: 1}; **case** 1: state = 2; **return** {value: 2} **case** 2: state = 3; **return** {value: 3} **case** 3: **return** {done: **true** }; } } } }; But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next(), it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded.

## **generators and iterables**

Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.

If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3. Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-83ecb080-00275))_

### Lazy and Eager Collections

- Served by the Pot: Collections

231

Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() This expression begins with a stack containing 30 elements. The top two are 29 and 28. It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter, we get an iterable that can iterate over the even squares, but not an actual stack or array.

Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer.

We can confirm this:

Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => { console.log(`squaring **${** x **}** `); **return** x * x }) .filter((x) => { console.log(`filtering **${** x **}** `); **return** x % 2 == 0 }) .first() _//=>_ squaring 29 filtering 841 squaring 28 filtering 784 784

If we write the almost identical thing with an array, we get a different behaviour: _(javascriptallonge.pdf (source-range-83ecb080-00295))_


## Related pages

- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (3 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (3 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (2 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (2 shared statement(s))
- [[javascriptallonge-combinator]] - shared statements: Combinator shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (1 shared statement(s))
- [[javascriptallonge-const]] - shared statements: Const shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from That Constant Coffee Craving: 43  The first sip: Basic Functions  ( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Althou ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-game]] - shared statements: Game shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from Iteration and Iterables: Served by the Pot: Collections  188 **const** stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) **const** collectionSum = (collection) => { **const** ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-programmer]] - shared statements: Programmer shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-purpose]] - shared statements: Purpose shares source evidence from Reassignment: 134  Composing and Decomposing Data  Now we’re creating a new inner parameter, i and binding it to the value of the outer i. This works, but let is so much simpler a ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Lazy and Eager Collections: Served by the Pot: Collections  231  Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map ... [truncated] (1 shared statement(s))
- [[javascriptallonge-rule]] - shared statements: Rule shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
