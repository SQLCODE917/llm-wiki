---
page_id: javascriptallonge-function
page_kind: concept
summary: Function: 116 statement(s) and 111 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function@d6d621d8511927d9ac324f03b15d22f4
---

# Function

What [[javascriptallonge]] covers about function:

## Statements

- For example, when this expression’s inner function is defined with function, arguments[0] refers to its only argument, "inner": _(javascriptallonge.pdf (source-range-83ecb080-00881))_
- Every time a function is invoked (“invoked” means “applied to zero or more arguments”), a new _environment_ is created. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-83ecb080-00291))_
- It’s a function that when applied, evaluates to a function that when applied, evaluates to 0. _(javascriptallonge.pdf (source-range-83ecb080-00378))_
- Functions containing no free variables are called _pure functions_ . _(javascriptallonge.pdf (source-range-83ecb080-00488))_
- The first function is the result of currying _[a]_ the second function. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- First, function declarations are _hoisted_ to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- Function declarations are formally only supposed to be made at what we might call the “top level” of a function. _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00819))_
- The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- When a function is applied to arguments (or “called”), JavaScript binds the values of arguments to the function’s argument names in an environment created for the function’s execution. _(javascriptallonge.pdf (source-range-83ecb080-00863))_
- Sometimes, a function is meant to be used as a Big-F function. _(javascriptallonge.pdf (source-range-83ecb080-00896))_
- But sometimes, a function is a small-f function. _(javascriptallonge.pdf (source-range-83ecb080-00897))_
- Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-00898))_
- Functions are values that can be part of expressions, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-00905))_
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: _(javascriptallonge.pdf (source-range-83ecb080-01007))_
- A _variadic function_ is a function that is designed to accept a variable number of arguments.[52] In JavaScript, you can make a variadic function by gathering parameters. _(javascriptallonge.pdf (source-range-83ecb080-01039))_
- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters _from the left_ , instead of from the right. _(javascriptallonge.pdf (source-range-83ecb080-01072))_
- Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-83ecb080-01176))_
- Functions can take functions as arguments, so let’s “extract” the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together. _(javascriptallonge.pdf (source-range-83ecb080-01362))_
- And now we supply a function that does slightly more than our mapping functions: _(javascriptallonge.pdf (source-range-83ecb080-01380))_
- Our foldWith function is a generalization of our mapWith function. _(javascriptallonge.pdf (source-range-83ecb080-01382))_
- And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-83ecb080-01459))_
- As before, we wrote a factorialWithDelayedWork function, then used partial application (callLast) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-83ecb080-01479))_
- A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. _(javascriptallonge.pdf (source-range-83ecb080-01802))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-02033))_
- A _constant function_ is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- The _identity function_ is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-83ecb080-02056))_
- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-83ecb080-02076))_
- It says, “take these two values and apply them to this function.” There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-83ecb080-02198))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-83ecb080-02310))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02348))_
- Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-02523))_
- It works, but as we’ve just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object:[93] _(javascriptallonge.pdf (source-range-83ecb080-02689))_
- JavaScript idioms like function combinators and decorators leverage JavaScript’s power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. _(javascriptallonge.pdf (source-range-83ecb080-00049))_
- As a staunch advocate of functional programming, much of what Reg has written rings true to me. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- Functions represent computations to be performed. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- “Function” is a reference type. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] _(javascriptallonge.pdf (source-range-83ecb080-00346))_
- We haven’t even said what an argument _is_ , only that our functions don’t have any. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- This function has one argument, room, and an empty body. _(javascriptallonge.pdf (source-range-83ecb080-00395))_
- When you apply the function to the arguments, an entry is placed in the dictionary for each argument. _(javascriptallonge.pdf (source-range-83ecb080-00438))_
- The expression ‘x’ (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-83ecb080-00448))_
- Functions containing one or more free variables are called _closures_ . _(javascriptallonge.pdf (source-range-83ecb080-00489))_
- Pure functions are easiest to understand. _(javascriptallonge.pdf (source-range-83ecb080-00490))_
- The first function doesn’t have any variables, therefore doesn’t have any free variables. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-83ecb080-00495))_
- Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. _(javascriptallonge.pdf (source-range-83ecb080-00498))_
- As we’ve said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. _(javascriptallonge.pdf (source-range-83ecb080-00527))_
- All of our “functions” are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- Another way to write our “circumference” function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-83ecb080-00582))_
- Amazing how such an important idea–naming functions–can be explained _en passant_ in just a few words. _(javascriptallonge.pdf (source-range-83ecb080-00605))_
- This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-83ecb080-00696))_
- Now, the function’s actual name has no effect on the environment in which it is used. _(javascriptallonge.pdf (source-range-83ecb080-00729))_
- Here’s a function that determines whether a positive integer is even or not. _(javascriptallonge.pdf (source-range-83ecb080-00733))_
- We haven’t actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-83ecb080-00755))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Functions are _reference values_ . _(javascriptallonge.pdf (source-range-83ecb080-00906))_
- Functions are applied to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00907))_
- Fat arrow functions have expressions or blocks as their bodies. _(javascriptallonge.pdf (source-range-83ecb080-00909))_
- function keyword functions always have blocks as their bodies. _(javascriptallonge.pdf (source-range-83ecb080-00910))_
- Function bodies have zero or more statements. _(javascriptallonge.pdf (source-range-83ecb080-00911))_
- But some functions have optional second or even third arguments. _(javascriptallonge.pdf (source-range-83ecb080-00961))_
- Naturally, there’s a function decorator recipe for that, borrowed from Haskell’s maybe monad[50] , Ruby’s andand[51] , and CoffeeScript’s existential method invocation: _(javascriptallonge.pdf (source-range-83ecb080-01009))_
- It ensures that a function can only be called, well, _once_ . _(javascriptallonge.pdf (source-range-83ecb080-01026))_
- All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. _(javascriptallonge.pdf (source-range-83ecb080-01064))_
- Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. _(javascriptallonge.pdf (source-range-83ecb080-01074))_
- In contrast to the behaviour of the ternary operator, ||, and &&, function parameters are always : _eagerly evaluated_ _(javascriptallonge.pdf (source-range-83ecb080-01161))_
- Our length function is _recursive_ , it calls itself. _(javascriptallonge.pdf (source-range-83ecb080-01325))_
- Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. _(javascriptallonge.pdf (source-range-83ecb080-01365))_
- A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-83ecb080-01369))_
- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not “production-ready” implementations. _(javascriptallonge.pdf (source-range-83ecb080-01398))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). _(javascriptallonge.pdf (source-range-83ecb080-01424))_
- While we’re executing the mapWith function, we’re constructing a new linked list. _(javascriptallonge.pdf (source-range-83ecb080-01716))_
- But it’s not like const and let in that it’s function scoped, not block scoped. _(javascriptallonge.pdf (source-range-83ecb080-01818))_
- However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-83ecb080-01820))_
- But at the time we _call_ one of the functions, i has the value 3, which is why the loop terminated. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- Our mapWith function would be very expensive if we make a copy every time we call rest(node). _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-83ecb080-01894))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-01900))_
- The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable. _(javascriptallonge.pdf (source-range-83ecb080-01949))_
- The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01976))_
- A function that starts with a seed and expands it into a data structure is called an _unfold_ . _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-02025))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-83ecb080-02085))_
- Functions are a fundamental building block of computation. _(javascriptallonge.pdf (source-range-83ecb080-02166))_
- Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). _(javascriptallonge.pdf (source-range-83ecb080-02266))_
- } function, and that’s where this is bound to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-02376))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-02377))_
- Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-83ecb080-02393))_
- Iteration for functions and objects has been around for many, many decades. _(javascriptallonge.pdf (source-range-83ecb080-02396))_
- Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-83ecb080-02400))_
- And if we assign a function to a property, we’ve created a method. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- As you recall, functions are mutable objects. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02531))_
- Generator functions can take an argument. _(javascriptallonge.pdf (source-range-83ecb080-02599))_
- Our generator function oneTwoThree is not an iterator. _(javascriptallonge.pdf (source-range-83ecb080-02651))_
- This object declares a [Symbol.iterator] function that makes it iterable. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- We’ve writing a function that returns an iterator, but we used a generator to do it. _(javascriptallonge.pdf (source-range-83ecb080-02681))_
- “The hasCycle function, a/k/a Tortoise and Hare, requires two separate iterators to do its job. _(javascriptallonge.pdf (source-range-83ecb080-02912))_
- Let’s start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- But the generator function allows us to maintain state implicitly. _(javascriptallonge.pdf (source-range-83ecb080-03043))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00260))_

> This is a function that is applied to no values and returns 0. Let’s verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00262))_

> If you try the same thing in a browser, you may see something else.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00262))_

> What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a 

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00263))_

> > 16 The simplest possible function is () => {}, we’ll see that later.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00285))_

> Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00287))_

> (() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00291))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00292))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00301))_

> We can use commas with functions to create functions that evaluate multiple expressions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00302))_

> (() => (1 + 1, 2 + 2))() _//=> 4_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00301))_

> We can use commas with functions to create functions that evaluate multiple expressions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00303))_

> This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later.

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00349, source-range-83ecb080-00351))_

> There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00350))_

> () => { 2 + 2 } () => { 1 + 1; 2 + 2 }

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00351))_

> As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00352))_

> () => { 1 + 1; 2 + 2 }

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00364))_

> The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00362))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00364))_

> The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00365))_

> (() => { 1 + 1; **return** 2 + 2 })() _//=> 4_

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00366, source-range-83ecb080-00368))_

> And also: The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00367))_

> (() => { **return** 1 + 1; 2 + 2 })() _//=> 2_

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00397))_

> I’m sure you are perfectly comfortable with the idea that this function has two arguments, room, and board. What does one do with the arguments? Use them in the body, of course. What do you think this is?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00398))_

> (diameter) => diameter * 3.14159265

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00400))_

> Remember that to apply a function with no arguments, we wrote (() => {})(). To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00401))_

> ((diameter) => diameter * 3.14159265)(2)

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00429))_

> Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. And we’re going to work our way up from (diameter) => diameter * 3.14159265 to functions like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00430))_

> - (x) => (y) => x

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00438))_

> How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00439))_

> ((x) => x)(2) _//=> 2_

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00490, source-range-83ecb080-00494))_

> Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we’ve already seen: The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The 

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00493))_

> - (x) => (y) => x

### Technical atom 17

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00498))_

> Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00497))_

> If pure functions can contain closures, can a closure contain a pure function?

### Technical atom 18

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00503))_

> To understand how closures are evaluated, we need to revisit environments. As we’ve said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let’s fill in the blanks!

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00504))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical atom 19

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00509))_

> Functions can have grandparents too:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00510))_

> (x) => (y) => (z) => x + y + z

### Technical atom 20

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00511))_

> This function does much the same thing as:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00512))_

> (x, y, z) => x + y + z

### Technical atom 21

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00531))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': _global environment_ }.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00532))_

> If you don’t want your code to operate directly within the global environment, what can you do?

### Technical atom 22

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00548))_

> In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. If we put our function expression in parentheses, we can apply it to the argument of 3.14159265:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00549))_

> ((PI) => _// ????_ )(3.14159265)

### Technical atom 23

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00550))_

> What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00551))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)

### Technical atom 24

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00561, source-range-83ecb080-00563))_

> There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: It produces the same result as our previous expressions for a diameter-calculating function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00562))_

> (diameter) => ((PI) => diameter * PI)(3.14159265)

### Technical atom 25

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00582))_

> Another way to write our “circumference” function would be to pass PI along with the diameter argument, something like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00583))_

> (diameter, PI) => diameter * PI

### Technical atom 26

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00602))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00604))_

> This underscores what we’ve said: if we have an expression that evaluates to a function, we apply it with ().

### Technical atom 27

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00625))_

> Here’s the second formulation of our diameter function, bound to a name using an IIFE:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00626))_

> ((diameter_fn) => _// ..._ )( ((PI) => (diameter) => diameter * PI )(3.14159265) )

### Technical atom 28

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00653))_

> This still evaluates to a function that calculates diameters:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00654))_

> ((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)(2) _//=> 6.2831853_

### Technical atom 29

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00655, source-range-83ecb080-00657))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the “outer” environment? Let’s rewrite things slightly differently: Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00656))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)

### Technical atom 30

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00657))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00658))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)(2) _//=> 6.2831853_

### Technical atom 31

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00674))_

> ((diameter) => { **const** PI = 3.14159265;

### Technical atom 32

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00675))_

> **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; })(2) _//=> would return 6 if const had function scope_

### Technical atom 33

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00673))_

> This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00676))_

> If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.

### Technical atom 34

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00676))_

> If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00678))_

> **if** ( **true** ) { **const** PI = 3.14159265; } **return** diameter * PI; })(2) _//=> would return 6.2831853 if const had function scope_

### Technical atom 35

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00694, source-range-83ecb080-00696))_

> Let’s get right to it. This code does _not_ name a function: It doesn’t name the function “repeat” for the same reason that const answer = 42 doesn’t name the number 42. This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00695))_

> **const** repeat = (str) => str + str

### Technical atom 36

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00699))_

> Here’s our repeat function written using a “fat arrow”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00700))_

> (str) => str + str

### Technical atom 37

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00709))_

> If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00710))_

> (n) => (1.618**n - -1.618**-n) / 2.236

### Technical atom 38

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00718))_

> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00719))_

> **const double** = **function** repeat (str) { **return** str + str; }

### Technical atom 39

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00729))_

> Now, the function’s actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00730))_

> **const** bindingName = **function** actualName () { _//..._

### Technical atom 40

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00729))_

> Now, the function’s actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00731))_

> }; bindingName _//=> [Function: actualName]_

### Technical atom 41

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00729))_

> Now, the function’s actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00732))_

> actualName _//=> ReferenceError: actualName is not defined_

### Technical atom 42

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00751))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00754))_

> **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> undefined is not a function (evaluating 'fizzbuzz()')_

### Technical atom 43

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00760))_

> Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00761))_

> ( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })()

### Technical atom 44

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00817, source-range-83ecb080-00819))_

> Or we could write: not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. You’ll see other function decorators in the recipes, like once and maybe. Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00818))_

> **const** nothing = not(something);

### Technical atom 45

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00828))_

> It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00829))_

> **const** compose = (a, b) => (c) => a(b(c));

### Technical atom 46

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00828))_

> It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00830))_

> **const** cookAndEat = compose(eat, cook);

### Technical atom 47

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00828))_

> It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00831))_

> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical atom 48

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00831))_

> If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00833))_

> Of course, you needn’t use combinators to implement either of these ideas, you can use if statements.

### Technical atom 49

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00840, source-range-83ecb080-00843))_

> Code is easier than words for this. The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this: This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00841))_

> _.map([1, 2, 3], (n) => n * n) _//=> [1, 4, 9]_

### Technical atom 50

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00843))_

> This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00844))_

> **const** squareAll = (array) => map(array, (n) => n * n);

### Technical atom 51

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00845))_

> The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00846))_

> **const** mapWith = (fn) => (array) => map(array, fn);

### Technical atom 52

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00845))_

> The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00847))_

> **const** squareAll = mapWith((n) => n * n);

### Technical atom 53

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00845))_

> The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00848))_

> squareAll([1, 2, 3]) _//=> [1, 4, 9]_

### Technical atom 54

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00866))_

> The first magic name is this, and it is bound to something called the function’s context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it’s called arguments, and the most interesting thing about it is that it contains a list of arguments passed to a function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00867))_

> **const** plus = **function** (a, b) { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_

### Technical atom 55

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00868, source-range-83ecb080-00870))_

> Although arguments looks like an array, it isn’t an array: It’s more like an object[43] that happens to bind some values to properties with names that look like integers starting with zero: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00869))_

> **const** args = **function** (a, b) { **return** arguments; } args(2,3) _//=> { '0': 2, '1': 3 }_

### Technical atom 56

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00885))_

> But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function. And thus arguments[0] will refer to "outer", not to "inner":

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00886))_

> ( **function** () { **return** (() => arguments[0])('inner'); })('outer') _//=> "outer"_

### Technical atom 57

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00956))_

> The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00957))_

> ['1', '2', '3'].map(parseFloat) _//=> [1, 2, 3]_

### Technical atom 58

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00959, source-range-83ecb080-00963))_

> Let’s try it: This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00961))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments.

### Technical atom 59

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00961, source-range-83ecb080-00963))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example: This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00962))_

> ['1', '2', '3'].map(parseInt) _//=> [1, NaN, NaN]_

### Technical atom 60

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00963))_

> This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00964))_

> We could write ['1', '2', '3'].map((s) => parseInt(s)), or we could come up with a decorator to do the job for us:

### Technical atom 61

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01002))_

> This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01003))_

> **const** isSomething = (value) => value !== **null** && value !== **void** 0;

### Technical atom 62

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01002))_

> This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01004))_

> **const** checksForSomething = (value) => { **if** (isSomething(value)) {

### Technical atom 63

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01007))_

> Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01008))_

> **var** something = isSomething(value) ? doesntCheckForSomething(value) : value;

### Technical atom 64

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01028))_

> Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let’s try it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01029))_

> **const** askedOnBlindDate = once( () => "sure, why not?" ); askedOnBlindDate() _//=> 'sure, why not?'_

### Technical atom 65

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01028))_

> Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let’s try it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01030))_

> askedOnBlindDate() _//=> undefined_

### Technical atom 66

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01039))_

> A _variadic function_ is a function that is designed to accept a variable number of arguments.[52] In JavaScript, you can make a variadic function by gathering parameters. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01040))_

> **const** abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5]

### Technical atom 67

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01074))_

> Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01075))_

> **const** [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];

### Technical atom 68

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01074))_

> Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01076))_

> first _//=> 'why'_ butFirst _//=> ["hello","there","little","droid"]_

### Technical atom 69

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01319))_

> First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01320))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : _// ???_

### Technical atom 70

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01319))_

> First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01322))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

### Technical atom 71

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01323, source-range-83ecb080-01325))_

> Let’s try it! Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01324))_

> length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_

### Technical atom 72

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01365))_

> We can write it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01367))_

> mapWith((x) => !!x, [ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_

### Technical atom 73

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01369))_

> With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01372))_

> **const** sumSquares = ([first, ...rest]) => first === **undefined**

### Technical atom 74

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01380))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01381))_

> foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5]) _//=> 55_

### Technical atom 75

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01382))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01383))_

> **const** squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\ [], array); squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_

### Technical atom 76

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01422, source-range-83ecb080-01424))_

> That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length: The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest).

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01423))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

### Technical atom 77

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01436))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01437))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

### Technical atom 78

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01436))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01439))_

> **const** length = (n) => lengthDelaysWork(n, 0);

### Technical atom 79

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01467, source-range-83ecb080-01470))_

> The naïve function for calcuating the factorial of a positive integer follows directly from the definition: Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n - 1). We can do the same conversion, pass in the work to be done:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01468))_

> **const** factorial = (n) => n == 1 ? n : n * factorial(n - 1); factorial(1) _//=> 1_ factorial(5) _//=> 120_

### Technical atom 80

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01802))_

> But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. Note this example of a function that uses a helper:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01803))_

> **const** factorial = (n) => {

### Technical atom 81

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01831, source-range-83ecb080-01833))_

> Again, so far, so good. Let’s try one of our functions: What went wrong? Why didn’t it give us ‘Hello, Raganwald, my name is Friedrich’? The answer is that pesky var i. Remember that i is bound in the surrounding environment, so it’s as if we wrote:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01832))_

> introductions[1]('Raganwald') _//=> 'Hello, Raganwald, my name is undefined'_

### Technical atom 82

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01987))_

> Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01988))_

> **const** NumberIterator = (number = 0) => () => ({ done: **false** , value: number++ })

### Technical atom 83

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01987))_

> Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01989))_

> fromOne = NumberIterator(1);

### Technical atom 84

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01987))_

> Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01990))_

> fromOne().value; _//=> 1_ fromOne().value; _//=> 2_ fromOne().value; _//=> 3_ fromOne().value; _//=> 4_ fromOne().value; _//=> 5_

### Technical atom 85

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02009))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02011))_

> **const** oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);

### Technical atom 86

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02009))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02012))_

> toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) _//=> [1, 9, 25, 49, 81]_

### Technical atom 87

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02033))_

> For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02036))_

> **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };

### Technical atom 88

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02061))_

> Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02062))_

> Therefore, K(I)(x)(y) => y:

### Technical atom 89

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02070))_

> If we are not feeling particularly academic, we can name our functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02071))_

> **const** first = K, second = K(I);

### Technical atom 90

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02070))_

> If we are not feeling particularly academic, we can name our functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02072))_

> first("primus")("secundus") _//=> "primus"_

### Technical atom 91

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02070))_

> If we are not feeling particularly academic, we can name our functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02073))_

> second("primus")("secundus") _//=> "secundus"_

### Technical atom 92

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02076))_

> Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we’d write them like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02079))_

> **const** first = ([first, second]) => first, second = ([first, second]) => second;

### Technical atom 93

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02096))_

> For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02097))_

> (first, second) => (selector) => selector(first)(second)

### Technical atom 94

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02098))_

> For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02099))_

> (first) => (second) => (selector) => selector(first)(second)

### Technical atom 95

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02100))_

> Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default):

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02101))_

> **const** first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second);

### Technical atom 96

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02100))_

> Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default):

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02102))_

> **const** latin = pair("primus")("secundus");

### Technical atom 97

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02119))_

> We can write length and mapWith functions over it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02122))_

> **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair));

### Technical atom 98

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02126))_

> Can we do the same with the linked lists we build out of functions? Yes:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02127))_

> **const** first = K, rest = K(I), pair = V, EMPTY = (() => {}); **const** l123 = pair(1)(pair(2)(pair(3)(EMPTY))); l123(first) _//=> 1_ l123(rest)(first)

### Technical atom 99

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02190))_

> We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02191))_

> **const** length = (node, delayed = 0) =>

### Technical atom 100

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02190))_

> We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02192))_

> node === EMPTY

### Technical atom 101

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02266))_

> Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We _could_ make that into flip:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02268))_

> Now if we write mapWith = flip(map), we can call mapWith(fn, list) or mapWith(fn)(list), our choice.

### Technical atom 102

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02378))_

> And here’s a sum function implemented as a fold over a functional iterator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02379))_

> **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0;

### Technical atom 103

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02378))_

> And here’s a sum function implemented as a fold over a functional iterator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02380))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }

### Technical atom 104

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02389))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();

### Technical atom 105

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02390))_

> **let** eachIteration, sum = 0;

### Technical atom 106

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02391))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }

### Technical atom 107

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02508))_

> One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in Array class already has one:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02509))_

> Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_

### Technical atom 108

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02531))_

> Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02532))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical atom 109

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02651))_

> Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02652))_

> If we call our generator function more than once, we get new iterators.

### Technical atom 110

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02658))_

> Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02656))_

> **const** iterator = ThreeNumbers[Symbol.iterator]();

### Technical atom 111

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02662, source-range-83ecb080-02664))_

> generator methods for objects: This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02663))_

> **const** ThreeNumbers = { *[Symbol.iterator] () { **yield** 1; **yield** 2; **yield** 3 } }


## Related pages

- [[javascriptallonge-iterator]] - shared statements and technical atoms (6 shared statement(s), 14 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms (5 shared statement(s), 14 shared atom(s))
- [[javascriptallonge-length]] - shared statements and technical atoms (3 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms (6 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (7 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms (1 shared statement(s), 10 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms (2 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms (1 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms (2 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms (3 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements and technical atoms (5 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-code]] - shared statements and technical atoms (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-second]] - shared statements and technical atoms (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-combinator]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms (4 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-program]] - shared statements (4 shared statement(s))
- [[javascriptallonge-language]] - shared statements (3 shared statement(s))
- [[javascriptallonge-block]] - shared statements (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements (1 shared statement(s))
- [[javascriptallonge-quasi-literal]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
