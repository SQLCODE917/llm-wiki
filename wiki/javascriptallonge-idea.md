---
page_id: javascriptallonge-idea
page_kind: concept
summary: Idea: 6 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-idea@9ea8e840070fcdd34ab1133444bdf6bc
---

# Idea

What [[javascriptallonge]] covers about idea:

## Statements

### About JavaScript Allongé

- iv

A Pull of the Lever: Prefaces **function** foo (first, ...rest) { _// ..._ } And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments. Not having to work around these kinds of missing features makes JavaScript Allongé a _better book_ , because it can focus on the _why_ to do something and _when_ to do it, instead of on the how to make it work

JavaScript Allongé, The “Six” Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript.

## **that’s nice. is that the only reason?**

Actually, no.

If it were just a matter of updating the syntax, the original version of JavaScript Allongé could have simply iterated, slowly replacing old syntax with new. It would have continued to say much the same things, only with new syntax.

_But there’s more to it than that_ . The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. Thus, the focus on things like writing decorators.

As noted above, JavaScript was chosen as the language for Allongé because it hit a sweet spot of having a large audience of programmers and having certain language features that happen to work well with this style of programming.

ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things and help us avoid warts. It makes a number of interesting programming techniques easy to explain and easy to use. And these techniques dovetail nicely with Allongé’s focus on composing entities and working with functions.

Thus, the “six” edition introduces classes and mixins. It introduces the notion of implementing private properties with symbols. It introduces iterators and generators. But the common thread that runs through all these things is that since they are all simple objects and simple functions, we can use the same set of “programming with functions” techniques to build programs by composing small, flexible, and decoupled entities.

We just call some of those functions constructors, others decorators, others functional mixins, and yet others, policies.

Introducing so many new ideas did require a major rethink of the way the book was organized. And introducing these new ideas did add substantially to its bulk. But even so, in a way it is still explaining the exact same original idea that programs are built out of small, flexible functions composed together. _(javascriptallonge.pdf (source-range-83ecb080-00014))_

### What JavaScript Allongé is. And isn't.

- A Pull of the Lever: Prefaces v

## **What JavaScript Allongé is. And isn’t.**

**==> picture [468 x 275] intentionally omitted <==**

**JavaScript Allongé is a book about thinking about programs**

JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions.

The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. The intention is to improve the way we think about programs. That’s a good thing.

But while JavaScript Allongé attempts to be provocative, it is not _prescriptive_ . There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others.

Software development is a complex field. Choices in development are often driven by social considerations. People often say that software should be written for people to read. Doesn’t that depend upon the people in question? Should code written by a small team of specialists use the same techniques and patterns as code maintained by a continuously changing cast of inexperienced interns?

Choices in software development are also often driven by requirements specific to the type of software being developed. For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-83ecb080-00016))_

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

### mapWith

- Recipes with Data

170

## **mapWith**

In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:

[1, 2, 3, 4, 5].map(x => x * x) _//=> [1, 4, 9, 16, 25]_ We could write a function that behaves like the .map method if we wanted: **const** map = (list, fn) => list.map(fn);

This recipe isn’t for map: It’s for mapWith, a function that wraps around map and turns any other function into a mapper. mapWith is very simple:[82] **const** mapWith = (fn) => (list) => list.map(fn); mapWith differs from map in two ways. It reverses the arguments, taking the function first and the list second. It also “curries” the function: Instead of taking two arguments, it takes one argument and returns a function that takes another argument.

That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map: **const** squaresOf = (list) => list.map(x => x * x); squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_ We can call mapWith in one step:

> 82Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-00228))_

### Iteration and Iterables

- 194

Served by the Pot: Collections **const** RandomNumbers = { [Symbol.iterator]: () => ({ next () { **return** {value: Math.random()}; } }) } **for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.494052127469331 0.835459444206208 0.1408337657339871 ...

**for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.7845381607767195 0.4956772483419627 0.20259276474826038 ...

Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection.

Right now, we’re just looking at ordered collections. To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. Every time we get an iterator from an ordered collection, we start iterating from the beginning.

## **operations on ordered collections**

Let’s define some operations on ordered collections. Here’s mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original:[89] > 89Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-00258))_


## Related pages

- [[javascriptallonge-purpose]] - shared statements: Purpose shares source evidence from mapWith: Recipes with Data  170  ## **mapWith**  In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the ... [truncated] (2 shared statement(s))

## Source

- [[javascriptallonge]]
