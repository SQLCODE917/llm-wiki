---
page_id: javascriptallonge-needn
page_kind: concept
summary: Needn: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-needn@5b2029bb718ffd64deef09f386b7e6d7
---

# Needn

What [[javascriptallonge]] covers about needn:

## Statements

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

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

104

Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious.[64] The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend.

We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

**Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded.

So here’s a question: If this is such a slow approach, why do some examples of “functional” algorithms work this exact way?

> 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript’s built-in arrays work. _(javascriptallonge.pdf (source-range-83ecb080-00153))_

### Plain Old JavaScript Objects

- Composing and Decomposing Data

110

## **literal object syntax**

JavaScript has a literal syntax for creating objects. This object maps values to the keys year, month, and day:

- { year: 2012, month: 6, day: 14 } Two objects created with separate evaluations have differing identities, just like arrays:

- { year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } _//=> false_

Objects use [] to access the values by name, using a string:

- { year: 2012, month: 6, day: 14 }['day'] _//=> 14_

Values contained within an object work just like values contained within an array, we access them by reference to the original: **const** unique = () => [], - x = unique(), - y = unique(), - z = unique(), o = { a: x, b: y, c: z };

- o['a'] === x && o['b'] === y && o['c'] === z _//=> true_

Names needn’t be alphanumeric strings. For anything else, enclose the label in quotes:

- { 'first name': 'reginald', 'last name': 'lewis' }['first name'] _//=> 'reginald'_

If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-83ecb080-00160))_

### Iteration and Iterables

- 193

Served by the Pot: Collections ['all the numbers', ...Numbers] _//=> infinite loop!_

firstAndSecondElement(...Numbers) _//=> infinite loop!_

Attempting to spread an infinite iterable into an array is always going to fail.

## **ordered collections**

The iterables we’re discussing represent _ordered collections_ . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example: **const** abc = ["a", "b", "c"]; **for** ( **const** i **of** abc) { console.log(i) } _//=>_ a b c **for** ( **const** i **of** abc) { console.log(i) } _//=>_ a b c

This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator], and ensuring that our iterators start at the beginning and work forward. Iterables needn’t represent ordered collections. We could make an infinite iterable representing random numbers: _(javascriptallonge.pdf (source-range-83ecb080-00257))_


## Related pages

- [[javascriptallonge-alway]] - shared statements: Alway shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  104  Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious. ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterable]] - shared statements: Iterable shares source evidence from Iteration and Iterables: 193  Served by the Pot: Collections ['all the numbers', ...Numbers] _//=> infinite loop!_  firstAndSecondElement(...Numbers) _//=> infinite loop!_  Attempting to spr ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Building Blocks: The first sip: Basic Functions  48  ## **Building Blocks**  When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-rest]] - shared statements: Rest shares source evidence from Building Blocks: The first sip: Basic Functions  48  ## **Building Blocks**  When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
