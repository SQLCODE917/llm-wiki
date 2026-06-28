---
page_id: javascriptallonge-mapwith
page_kind: concept
summary: Mapwith: 12 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-mapwith@58f8847855a5c9180a0354350b7f3e5f
---

# Mapwith

What [[javascriptallonge]] covers about mapwith:

## Statements

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

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

94

## **Tail Calls (and Default Arguments)**

The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not “production-ready” implementations. One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded.

Let’s look at how. Here’s our extremely simple mapWith function again: **const** mapWith = (fn, [first, ...rest]) => first === **undefined** ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ Let’s step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined, so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest), then evaluate [fn(first), ...mapWith(fn, rest)].

This is roughly equivalent to writing: **const** mapWith = **function** (fn, [first, ...rest]) { **if** (first === **undefined** ) { **return** []; } **else** { **const** _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; **return** _temp3; } } Note that while evaluating mapWith(fn, rest), JavaScript must retain the value first or fn(first), plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1.

Next, JavaScript invokes mapWith(fn, rest), which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]). And the same thing happens: JavaScript has to hang on to 2 (or 4, or both, _(javascriptallonge.pdf (source-range-83ecb080-00141))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

104

Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious.[64] The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend.

We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

**Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded.

So here’s a question: If this is such a slow approach, why do some examples of “functional” algorithms work this exact way?

> 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript’s built-in arrays work. _(javascriptallonge.pdf (source-range-83ecb080-00153))_

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

### Copy on Write

- Composing and Decomposing Data

138 **const** childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ Our new at and set functions behave similarly to array[index] and array[index] = value. The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list.

## **copy-on-read**

So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.

**const** rest = ({first, rest}) => copy(rest); **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = rest(parentList); **const** newParentList = set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}} This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don’t need to make a copy because we won’t be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node).

There’s also a bug: What happens when we modify the first element of a list? But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-00191))_

### mapWith

- Recipes with Data

171 **const** squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_ If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result: **const** squaresOf = callRight(map, (n => n * n); squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_ Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern. _mapWith was suggested by ludicast_[83] > 83http://github.com/ludicast _(javascriptallonge.pdf (source-range-83ecb080-00229))_

### Flip

- Recipes with Data

173 **const** flipAndCurry = (fn) => (first) => (second) => fn(second, first);

Sometimes you want to flip, but not curry: **const** flip = (fn) => (first, second) => fn(second, first);

This is gold. Consider how we define mapWith now: **var** mapWith = flipAndCurry(map);

Much nicer!

## **self-currying flip**

Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We _could_ make that into flip: **const** flip = (fn) => **function** (first, second) { **if** (arguments.length === 2) { **return** fn(second, first); } **else** { **return function** (second) { **return** fn(second, first); }; }; };

Now if we write mapWith = flip(map), we can call mapWith(fn, list) or mapWith(fn)(list), our choice.

## **flipping methods**

When we learn about context and methods, we’ll see that flip throws the current context away, so it can’t be used to flip methods. A small alteration gets the job done: _(javascriptallonge.pdf (source-range-83ecb080-00232))_

### Iteration and Iterables

- 194

Served by the Pot: Collections **const** RandomNumbers = { [Symbol.iterator]: () => ({ next () { **return** {value: Math.random()}; } }) } **for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.494052127469331 0.835459444206208 0.1408337657339871 ...

**for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.7845381607767195 0.4956772483419627 0.20259276474826038 ...

Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection.

Right now, we’re just looking at ordered collections. To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. Every time we get an iterator from an ordered collection, we start iterating from the beginning.

## **operations on ordered collections**

Let’s define some operations on ordered collections. Here’s mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original:[89] > 89Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-00258))_

- 196

Served by the Pot: Collections

Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens. Evens works just as if we’d written this: **const** Evens = { [Symbol.iterator] () { **const** iterator = Numbers[Symbol.iterator](); **return** { next () { **const** {done, value} = iterator.next(); **return** ({done, value: done ? **undefined** : 2 *value}); } } } };

Every time we write for (const i of Evens), JavaScript calls Evens[Symbol.iterator](). That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens), and that means that iterator starts at the beginning of Numbers.

So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a _collection operation_ .

Mind you, we can also map non-collection iterables, like RandomNumbers: **const** ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers); **for** ( **const** i **of** ZeroesToNines) { console.log(i) } _//=>_ 5 1 9 ...

**for** ( **const** i **of** ZeroesToNines) { console.log(i) } _//=>_ 3 _(javascriptallonge.pdf (source-range-83ecb080-00260))_

- 198

Served by the Pot: Collections

Like mapWith, they preserve the ordered collection semantics of whatever you give them.

And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000: **const** Squares = mapWith((x) => x * x, Numbers); **const** EndWithOne = filterWith((x) => x % 10 === 1, Squares); **const** UpTo1000 = untilWith((x) => (x > 1000), EndWithOne);

[...UpTo1000] _//=>_ [1,81,121,361,441,841,961] [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] As we expect from an ordered collection, each time we iterate over UpTo1000, we begin at the beginning.

For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest]: **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **const** rest = (iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **return** iterator; } }); like our other operations, rest preserves the ordered collection semantics of its argument.

## **from**

Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function? No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-83ecb080-00262))_


## Technical atoms

### Technical frame 1: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00147))_

> Composing and Decomposing Data

99

5! = 5 x 4 x 3 x 2 x 1 = 120.

The naïve function for calcuating the factorial of a positive integer follows directly from the definition: **const** factorial = (n) => n == 1 ? n : n * factorial(n - 1); factorial(1) _//=> 1_ factorial(5) _//=> 120_ While this is mathematically elegant, it is computational filigree[63] .

Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n *

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00146))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |
```

</details>

### Technical frame 2: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00149))_

> Composing and Decomposing Data

101 **const** factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) _//=> 1_ factorial(6) _//=> 720_

By writing our parameter list as (n, work = 1) =>, we’re stating that if a second parameter is not provided, work is to be bound to 1. We can do similar things with our other tail-recursive functions: **const** length = ([first, ...rest], numberToBeAdded = 0) => first === **undefined** ? numberToBeAdded : length(rest, 1 + numberToB

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00150))_

> 102 **const** [first, second = "two"] = ["one"];


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Building Blocks: The first sip: Basic Functions  49  ## **partial application**  Another basic building block is _partial application_ . When a function takes multiple arguments, we ... [truncated]; Function shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (4 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from Building Blocks: The first sip: Basic Functions  49  ## **partial application**  Another basic building block is _partial application_ . When a function takes multiple arguments, we ... [truncated]; Argument shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-rest]] - shared statements and technical atoms: Rest shares source evidence from Tail Calls (and Default Arguments): Composing and Decomposing Data  94  ## **Tail Calls (and Default Arguments)**  The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustra ... [truncated]; Rest shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-learn]] - shared technical atoms: Learn shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms: Length shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-recursion]] - shared technical atoms: Recursion shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-const]] - shared statements: Const shares source evidence from Mutation: Composing and Decomposing Data  120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsE ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  104  Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious. ... [truncated] (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  104  Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious. ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterable]] - shared statements: Iterable shares source evidence from Iteration and Iterables: 196  Served by the Pot: Collections  Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens. Evens works just as if we’d written th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Tail Calls (and Default Arguments): Composing and Decomposing Data  94  ## **Tail Calls (and Default Arguments)**  The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustra ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Building Blocks: The first sip: Basic Functions  49  ## **partial application**  Another basic building block is _partial application_ . When a function takes multiple arguments, we ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Flip: Recipes with Data  173 **const** flipAndCurry = (fn) => (first) => (second) => fn(second, first);  Sometimes you want to flip, but not curry: **const** flip = (fn) = ... [truncated] (1 shared statement(s))
- [[javascriptallonge-section-mapwith-dfd947e8]] - source section: mapWith shares source evidence from mapWith: Recipes with Data  170  ## **mapWith**  In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the ... [truncated] (6 shared statement(s))

## Source

- [[javascriptallonge]]
