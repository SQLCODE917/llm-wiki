---
page_id: javascriptallonge-block
page_kind: concept
summary: Block: 10 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-block@9a645052a7df7040e4acd89ffedc0fe4
---

# Block

What [[javascriptallonge]] covers about block:

## Statements

### About JavaScript Allongé

- ii

A Pull of the Lever: Prefaces

## **About JavaScript Allongé**

JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. If those terms seem unfamiliar, don’t worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter.

_JavaScript Allongé_ begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances.

It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms like function combinators and decorators leverage JavaScript’s power to make code easier to read, modify, debug and refactor.

_JavaScript Allongé_ teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down. As a result, _JavaScript Allongé_ is a rich read releasing many of JavaScript’s subtleties, much like the Café Allongé beloved by coffee enthusiasts everywhere.

## **why the “six” edition?**

ECMAScript 2015 (formerly called ECMAScript 6 or “ES6”), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive.

Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features.

For example, block-structured languages allow us to write: **for** ( **int** i = 0; i < array.length; ++i) { _// ..._ } And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00012))_

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

11

## **the simplest possible block**

There’s another thing we can put to the right of an arrow, a _block_ . A block has zero or more _statements_ , separated by semicolons.[18] So, this is a valid function:

## () => {}

It returns the result of evaluating a block that has no statements. What would that be? Let’s try it: (() => {})() _//=> undefined_

What is this undefined?

## **undefined**

In JavaScript, the absence of a value is written undefined, and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type:

## **undefined**

_//=> undefined_

Like numbers, booleans and strings, JavaScript can print out the value undefined.

**undefined** === **undefined**

_//=> true_ (() => {})() === (() => {})() _//=> true_ (() => {})() === **undefined** _//=> true_

No matter how you evaluate undefined, you get an identical value back. undefined is a value that means “I don’t have a value.” But it’s still a value :-)

> 18Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it’s helpful to know it exists. _(javascriptallonge.pdf (source-range-83ecb080-00048))_

### That Constant Coffee Craving

- The first sip: Basic Functions

31

## **nested blocks**

Up to now, we’ve only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this: (n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else return** !even(x - 1); } **return** even(n) } And it works for fairly small numbers: ((n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else return** !even(x - 1); } **return** even(n) })(13) _//=> false_

The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: (n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else** { **const** odd = (y) => !even(y); **return** odd(x - 1); } _(javascriptallonge.pdf (source-range-83ecb080-00067))_

### Building Blocks

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

### Summary

- The first sip: Basic Functions

55

## **Summary**

**==> picture [29 x 29] intentionally omitted <==**

## **Functions**

- Functions are values that can be part of expressions, returned from other functions, and so forth.

- Functions are _reference values_ .

- Functions are applied to arguments.

- The arguments are passed by sharing, which is also called “pass by value.” - Fat arrow functions have expressions or blocks as their bodies.

- function keyword functions always have blocks as their bodies.

- Function bodies have zero or more statements.

- Expression bodies evaluate to the value of the expression.

- Block bodies evaluate to whatever is returned with the return keyword, or to undefined.

- JavaScript uses const to bind values to names within block scope.

- JavaScript uses function declarations to bind functions to names within function scope. Function declarations are “hoisted.” - Function application creates a scope.

- Blocks also create scopes if const statements are within them.

- Scopes are nested and free variable references closed over.

- Variables can shadow variables in an enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00095))_

### Partial Application

- Recipes with Basic Functions

57

## **Partial Application**

In Building Blocks, we discussed partial application, but we didn’t write a generalized recipe for it. This is such a common tool that many libraries provide some form of partial application. You’ll find examples in Lemonad[45] from Michael Fogus, Functional JavaScript[46] from Oliver Steele and the terse but handy node-ap[47] from James Halliday.

These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost.[48] If you want to bind more than one argument, or you want to leave a “hole” in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**const** callFirst = (fn, larg) => **function** (...rest) { **return** fn.call( **this** , larg, ...rest); } **const** callLast = (fn, rarg) => **function** (...rest) { **return** fn.call( **this** , ...rest, rarg); } **const** greet = (me, you) => `Hello, **${** you **}** , my name is **${** me **}** `; **const** heliosSaysHello = callFirst(greet, 'Helios'); heliosSaysHello('Eartha') _//=> 'Hello, Eartha, my name is Helios'_ **const** sayHelloToCeline = callLast(greet, 'Celine'); sayHelloToCeline('Eartha') _//=> 'Hello, Celine, my name is Eartha'_ As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We’d need a different recipe if we wish to create partial applications of object methods.

> 45https://github.com/fogus/lemonad

> 46http://osteele.com/sources/javascript/functional/

> 47https://github.com/substack/node-ap

> 48 callFirst and callLast were inspired by Michael Fogus’ Lemonad. Thanks! _(javascriptallonge.pdf (source-range-83ecb080-00099))_

### Reassignment

- Composing and Decomposing Data

126

JavaScript does not permit us to rebind a name that has been bound with const. We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let: **let** age = 52; age = 53; age _//=> 53_

We took the time to carefully examine what happens with bindings in environments. Let’s take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment.

So let’s consider what happens with a shadowed variable: (() => { **let** age = 49; **if** ( **true** ) { **let** age = 50; } **return** age; })() _//=> 49_

Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. We go from: {age: 49, '..': global-environment} To: {age: 50, '..': {age: 49, '..': global-environment}} Then back to: _(javascriptallonge.pdf (source-range-83ecb080-00178))_

### Making Data Out Of Functions

- 155

Composing and Decomposing Data **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };

OneTwoThree.first _//=> 1_ OneTwoThree.rest.first _//=> 2_

OneTwoThree.rest.rest.first _//=> 3_ **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) _//=> 3_

A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things.

They established that arbitrary computations could be represented a small set of axiomatic components. For example, we don’t need arrays to represent lists, or even POJOs to represent nodes in a linked list. We can model lists just using functions.

To Mock a Mockingbird[76] established the metaphor of songbirds for the combinators, and ever since then logicians have called the K combinator a “kestrel,” the B combinator a “bluebird,” and so forth.

The oscin.es[77] library contains code for all of the standard combinators and for experimenting using the standard notation.

Let’s start with some of the building blocks of combinatory logic, the K, I, and V combinators, nicknamed the “Kestrel”, the “Idiot Bird”, and the “Vireo:” > 76http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422

> 77http://oscin.es _(javascriptallonge.pdf (source-range-83ecb080-00211))_


## Related pages

- [[javascriptallonge-bind]] - shared statements: Bind shares source evidence from Reassignment: Composing and Decomposing Data  126  JavaScript does not permit us to rebind a name that has been bound with const. We can _shadow_ it by using const to declare a ne ... [truncated] (1 shared statement(s))
- [[javascriptallonge-const]] - shared statements: Const shares source evidence from Summary: The first sip: Basic Functions  55  ## **Summary**  **==> picture [29 x 29] intentionally omitted <==**  ## **Functions**  - Functions are values that can be part of ... [truncated] (1 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from Summary: The first sip: Basic Functions  55  ## **Summary**  **==> picture [29 x 29] intentionally omitted <==**  ## **Functions**  - Functions are values that can be part of ... [truncated] (1 shared statement(s))
- [[javascriptallonge-feature]] - shared statements: Feature shares source evidence from About JavaScript Allongé: ii  A Pull of the Lever: Prefaces  ## **About JavaScript Allongé**  JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s writ ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  11  ## **the simplest possible block**  There’s another thing we can put to the right of an arrow, a _block_ . A block has zero or mo ... [truncated] (1 shared statement(s))
- [[javascriptallonge-seen]] - shared statements: Seen shares source evidence from That Constant Coffee Craving: The first sip: Basic Functions  31  ## **nested blocks**  Up to now, we’ve only ever seen blocks we use as the body of functions. But there are other kinds of blocks ... [truncated] (1 shared statement(s))
- [[javascriptallonge-start]] - shared statements: Start shares source evidence from Making Data Out Of Functions: 155  Composing and Decomposing Data **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };  OneTwoThree.f ... [truncated] (1 shared statement(s))
- [[javascriptallonge-statement]] - shared statements: Statement shares source evidence from Summary: The first sip: Basic Functions  55  ## **Summary**  **==> picture [29 x 29] intentionally omitted <==**  ## **Functions**  - Functions are values that can be part of ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
