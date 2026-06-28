---
page_id: javascriptallonge-idea
page_kind: concept
summary: Idea: 9 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-idea@94896df36277a7455c34585bb0f601eb
---

# Idea

What [[javascriptallonge]] covers about idea:

## Statements

### that's nice. is that the only reason?

- Introducing so many new ideas did require a major rethink of the way the book was organized. And introducing these new ideas did add substantially to its bulk. But even so, in a way it is still explaining the exact same original idea that programs are built out of small, flexible functions composed together. _(javascriptallonge.pdf (source-range-31a4cf47-00048))_

### What JavaScript Allongé is. And isn't.

- The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. The intention is to improve the way we think about programs. That's a good thing. _(javascriptallonge.pdf (source-range-31a4cf47-00053))_

### functions that return values and evaluate expressions

- Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-31a4cf47-00194))_

### const

- Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-31a4cf47-00436))_

### magic names and fat arrows

- 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-31a4cf47-00629))_

### Self-Similarity

- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-31a4cf47-00885))_

### mapWith

- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-31a4cf47-01440))_

### operations on ordered collections

- 89 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-31a4cf47-01588))_


## Technical atoms

### Technical frame 1: functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00197))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00196))_

```
(() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity
```

### Technical frame 2: magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00632))_

> Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00630))_

```
const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36,49,64,81,100,121,144]
```

### Technical frame 3: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01442))_

> If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01441))_

```
const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25]
```

### Technical frame 4: operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01590))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01589))_

```
const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: done ? undefined : fn(value)}); } } } });
```


## Related pages

- [[javascriptallonge-discussing]] - shared statements and technical atoms: Discussing shares source evidence from magic names and fat arrows: 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the t ... [truncated]; Discussing shares technical record from magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-purpose]] - shared statements and technical atoms: Purpose shares source evidence from magic names and fat arrows: 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the t ... [truncated]; Purpose shares technical record from magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from const: Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really ... [truncated]; Function shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-function-return-value]] - shared statements and technical atoms: Function Return Value shares source evidence from functions that return values and evaluate expressions: Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.; Function Return Value shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from mapWith: const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25] (2 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (2 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-operation]] - shared technical atoms: Operation shares technical record from operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (1 shared atom(s))
- [[javascriptallonge-array]] - shared statements: Array shares source evidence from Self-Similarity: We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. (1 shared statement(s))
- [[javascriptallonge-expression]] - shared statements: Expression shares source evidence from Self-Similarity: We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. (1 shared statement(s))
- [[javascriptallonge-important]] - shared statements: Important shares source evidence from const: Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really ... [truncated] (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements: Literal shares source evidence from Self-Similarity: We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. (1 shared statement(s))

## Source

- [[javascriptallonge]]
