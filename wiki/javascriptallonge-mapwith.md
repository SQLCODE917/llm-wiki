---
page_id: javascriptallonge-mapwith
page_kind: concept
summary: Mapwith: 13 statement(s) and 15 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-mapwith@2005b4a657c29237a6ee3201317e5336
---

# Mapwith

What [[javascriptallonge]] covers about mapwith:

## Statements

- Next, JavaScript invokes mapWith(fn, rest), which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]). _(javascriptallonge.pdf (source-range-83ecb080-01405))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- Let’s rewrite mapWith so that we can use it to sum squares. _(javascriptallonge.pdf (source-range-83ecb080-01378))_
- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not “production-ready” implementations. _(javascriptallonge.pdf (source-range-83ecb080-01398))_
- First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- While we’re executing the mapWith function, we’re constructing a new linked list. _(javascriptallonge.pdf (source-range-83ecb080-01716))_
- Our mapWith function would be very expensive if we make a copy every time we call rest(node). _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-83ecb080-01894))_
- mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-83ecb080-02231))_
- Here’s mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original:[89] _(javascriptallonge.pdf (source-range-83ecb080-02469))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- Like mapWith, they preserve the ordered collection semantics of whatever you give them. _(javascriptallonge.pdf (source-range-83ecb080-02496))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00845))_

> The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00846))_

> **const** mapWith = (fn) => (array) => map(array, fn);

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00845))_

> The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00847))_

> **const** squareAll = mapWith((n) => n * n);

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00845))_

> The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00848))_

> squareAll([1, 2, 3]) _//=> [1, 4, 9]_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01378))_

> Let’s rewrite mapWith so that we can use it to sum squares.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01379))_

> **const** foldWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldWith(fn, terminalValue, rest));

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01382))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01383))_

> **const** squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\ [], array); squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01384))_

> And if we like, we can write mapWith using foldWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01387))_

> **const** mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\ ], array), squareAll = (array) => mapWith((x) => x * x, array);

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01444))_

> This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01447))_

> **const** mapWithDelaysWork = (fn, [first, ...rest], prepend) =>

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01507))_

> We have now seen how to use Tail Calls to execute mapWith in constant space:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01508))_

> **const** mapWith = (fn, [first, ...rest], prepend = []) => first === **undefined**

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02215, source-range-83ecb080-02219))_

> **const** map = (list, fn) => list.map(fn); That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02217))_

> **const** mapWith = (fn) => (list) => list.map(fn);

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02219))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02220))_

> **const** squaresOf = (list) => list.map(x => x * x);

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02223, source-range-83ecb080-02228))_

> > 82Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02226))_

> **const** squaresOf = mapWith(n => n * n);

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02228))_

> If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02227))_

> squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02228))_

> If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02229))_

> **const** squaresOf = callRight(map, (n => n * n);

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02228))_

> If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02230))_

> squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02475))_

> Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02476))_

> **const** Evens = mapWith((x) => 2 * x, Numbers);


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (5 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-copy]] - shared statements (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements (1 shared statement(s))
- [[javascriptallonge-iterable]] - shared statements (1 shared statement(s))
- [[javascriptallonge-rest]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
