---
page_id: javascriptallonge-return
page_kind: concept
summary: Return: 11 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-return@f4b607613eda6bf6b4ef97692faeffff
---

# Return

What [[javascriptallonge]] covers about return:

## Statements

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

9

## **functions that return values and evaluate expressions**

We’ve seen () => 0. We know that (() => 0)() returns 0, and this is unsurprising. Likewise, the following all ought to be obvious: (() => 1)() _//=> 1_ (() => "Hello, JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** )() _//=> Infinity_

Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2. Can we put an expression to the right of the arrow?

(() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)()?

Let’s try it: (() => (() => 0)())() _//=> 0_

Yes we can! Functions can return the value of evaluating another function.

When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out. So we can also write: _(javascriptallonge.pdf (source-range-83ecb080-00046))_

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

- 14

The first sip: Basic Functions (() => 2 + 2)() _//=> 4_ (() => { 2 + 2 })() _//=> undefined_ (() => (1 + 1, 2 + 2))() _//=> 4_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ So how do we get a function that evaluates a block to return a value when applied? With the return keyword and any expression: (() => { **return** 0 })() _//=> 0_ (() => { **return** 1 })() _//=> 1_ (() => { **return** 'Hello ' + 'World' })() _// 'Hello World'_

The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example: (() => { 1 + 1; **return** 2 + 2 })() _//=> 4_ And also: (() => { **return** 1 + 1; 2 + 2 })() _//=> 2_

The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression: _(javascriptallonge.pdf (source-range-83ecb080-00051))_

### Combinators and Function Decorators

- The first sip: Basic Functions

45

## **Combinators and Function Decorators**

## **higher-order functions**

As we’ve seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function.

Here’s a very simple higher-order function that takes a function as an argument: **const** repeat = (num, fn) => (num > 0) ? (repeat(num - 1, fn), fn(num)) : **undefined** repeat(3, **function** (n) { console.log(`Hello **${** n **}** `) }) _//=>_ 'Hello 1' 'Hello 2' 'Hello 3' **undefined**

Higher-order functions dominate _JavaScript Allongé_ . But before we go on, we’ll talk about some specific types of higher-order functions.

## **combinators**

The word “combinator” has a precise technical meaning in mathematics:

“A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.”–Wikipedia[35] If we were learning Combinatorial Logic, we’d start with the most basic combinators like S, K, and I, and work up from there to practical combinators. We’d learn that the fundamental combinators are named after birds following the example of Raymond Smullyan’s famous book To Mock a Mockingbird[36] .

> 35https://en.wikipedia.org/wiki/Combinatory_logic

> 36http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 _(javascriptallonge.pdf (source-range-83ecb080-00082))_

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

### Mutation

- Composing and Decomposing Data

120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsEve _//=> [2012, 10, 31]_ The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?

**const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween[0] = 2013; })(allHallowsEve); allHallowsEve _//=> [2013, 10, 31]_ This is different. We haven’t rebound the inner name to a different variable, we’ve mutated the value that both bindings share. Now that we’ve finished with mutation and aliases, let’s have a look at it.

**==> picture [29 x 29] intentionally omitted <==**

JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value.

**==> picture [29 x 29] intentionally omitted <==**

Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction.

## **mutation and data structures**

Mutation is a surprisingly complex subject. It is possible to compute anything without ever mutating an existing entity. Languages like Haskell[70] don’t permit mutation at all. In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about.

One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let’s recall linked lists from Plain Old JavaScript Objects. While we’re executing the mapWith function, we’re constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith.

But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:

70https://en.wikipedia.org/wiki/Haskell_ _(javascriptallonge.pdf (source-range-83ecb080-00171))_

### Functional Iterators

- 148

Composing and Decomposing Data sum += eachIteration.value; } **return** sum; } iteratorSum(arrayIterator([1, 4, 9, 16, 25])) _//=> 55_

Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true }.

We can write a different iterator for a different data structure. Here’s one for linked lists: **const** EMPTY = **null** ; **const** isEmpty = (node) => node === EMPTY; **const** pair = (first, rest = EMPTY) => ({first, rest}); **const** list = (...elements) => { **const** [first, ...rest] = elements; **return** elements.length === 0 ? EMPTY : pair(first, list(...rest)) } **const** print = (aPair) => isEmpty(aPair) ? "" : ` **${** aPair.first **} ${** print(aPair.rest) **}** ` **const** listIterator = (aPair) => () => { **const** done = isEmpty(aPair); **if** (done) { **return** {done}; } **else** { **const** {first, rest} = aPair; aPair = aPair.rest; _(javascriptallonge.pdf (source-range-83ecb080-00203))_

### Making Data Out Of Functions

- Composing and Decomposing Data

159

Our latin data structure is no longer a dumb data structure, it’s a function. And instead of passing latin to first or second, we pass first or second to latin. It’s _exactly backwards_ of the way we write functions that operate on data.

## **the vireo**

Given that our latin data is represented as the function (selector) => selector("primus")("secundus"), our obvious next step is to make a function that makes data. For arrays, we’d write cons = (first, second) => [first, second]. For objects we’d write: cons = (first, second) => {first, second}. In both cases, we take two parameters, and return the form of the data.

For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters: (first, second) => (selector) => selector(first)(second) For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: (first) => (second) => (selector) => selector(first)(second) Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default): **const** first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second); **const** latin = pair("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_

It works! Now what is this pair function? If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y). That’s the V combinator, the Vireo! So we can write:

78https://en.wikipedia.org/wiki/Currying _(javascriptallonge.pdf (source-range-83ecb080-00215))_

### Iteration and Iterables

- 198

Served by the Pot: Collections

Like mapWith, they preserve the ordered collection semantics of whatever you give them.

And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000: **const** Squares = mapWith((x) => x * x, Numbers); **const** EndWithOne = filterWith((x) => x % 10 === 1, Squares); **const** UpTo1000 = untilWith((x) => (x > 1000), EndWithOne);

[...UpTo1000] _//=>_ [1,81,121,361,441,841,961] [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] As we expect from an ordered collection, each time we iterate over UpTo1000, we begin at the beginning.

For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest]: **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **const** rest = (iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **return** iterator; } }); like our other operations, rest preserves the ordered collection semantics of its argument.

## **from**

Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function? No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-83ecb080-00262))_

### Generating Iterables

- 216

Served by the Pot: Collections

We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use JavaScript’s natural management of state instead of constantly rolling our own.

Of course, we could just as easily write a generator function for Fibonacci numbers: **function** * fibonacci () { **let** a, b; **yield** a = 0; **yield** b = 1; **while** ( **true** ) { [a, b] = [b, a + b] **yield** b; } } **for** ( **const** i **of** fibonacci()) { console.log(i); } _//=>_ 0 1 1 2 3 5 8 13 21 34 55 89 144 ...

## **yielding iterables**

Here’s a first crack at a function that returns an iterable object for iterating over trees: _(javascriptallonge.pdf (source-range-83ecb080-00279))_

### Lazy and Eager Collections

- Served by the Pot: Collections

231

Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() This expression begins with a stack containing 30 elements. The top two are 29 and 28. It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter, we get an iterable that can iterate over the even squares, but not an actual stack or array.

Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer.

We can confirm this:

Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => { console.log(`squaring **${** x **}** `); **return** x * x }) .filter((x) => { console.log(`filtering **${** x **}** `); **return** x % 2 == 0 }) .first() _//=>_ squaring 29 filtering 841 squaring 28 filtering 784 784

If we write the almost identical thing with an array, we get a different behaviour: _(javascriptallonge.pdf (source-range-83ecb080-00295))_


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  45  ## **Combinators and Function Decorators**  ## **higher-order functions**  As we’ve seen, JavaScript functions take values as arg ... [truncated] (4 shared statement(s))
- [[javascriptallonge-argument]] - shared statements: Argument shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  45  ## **Combinators and Function Decorators**  ## **higher-order functions**  As we’ve seen, JavaScript functions take values as arg ... [truncated] (2 shared statement(s))
- [[javascriptallonge-block]] - shared statements: Block shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  11  ## **the simplest possible block**  There’s another thing we can put to the right of an arrow, a _block_ . A block has zero or mo ... [truncated] (1 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Lazy and Eager Collections: Served by the Pot: Collections  231  Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map ... [truncated] (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Iteration and Iterables: 198  Served by the Pot: Collections  Like mapWith, they preserve the ordered collection semantics of whatever you give them.  And here’s a computation performed usin ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterable]] - shared statements: Iterable shares source evidence from Iteration and Iterables: 198  Served by the Pot: Collections  Like mapWith, they preserve the ordered collection semantics of whatever you give them.  And here’s a computation performed usin ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Generating Iterables: 216  Served by the Pot: Collections  We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use ... [truncated] (1 shared statement(s))
- [[javascriptallonge-list]] - shared statements: List shares source evidence from Mutation: Composing and Decomposing Data  120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsE ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Building Blocks: The first sip: Basic Functions  49  ## **partial application**  Another basic building block is _partial application_ . When a function takes multiple arguments, we ... [truncated] (1 shared statement(s))
- [[javascriptallonge-parameter]] - shared statements: Parameter shares source evidence from Making Data Out Of Functions: Composing and Decomposing Data  159  Our latin data structure is no longer a dumb data structure, it’s a function. And instead of passing latin to first or second, w ... [truncated] (1 shared statement(s))
- [[javascriptallonge-statement]] - shared statements: Statement shares source evidence from As Little As Possible About Functions, But No Less: 14  The first sip: Basic Functions (() => 2 + 2)() _//=> 4_ (() => { 2 + 2 })() _//=> undefined_ (() => (1 + 1, 2 + 2))() _//=> 4_ (() => { 1 + 1; 2 + 2 })() _//=> u ... [truncated] (1 shared statement(s))
- [[javascriptallonge-writing]] - shared statements: Writing shares source evidence from Generating Iterables: 216  Served by the Pot: Collections  We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
