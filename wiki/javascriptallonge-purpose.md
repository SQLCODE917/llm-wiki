---
page_id: javascriptallonge-purpose
page_kind: concept
summary: Purpose: 5 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-purpose@a003546bf290ba6a388e322b666328d4
---

# Purpose

What [[javascriptallonge]] covers about purpose:

## Statements

### And also: / Magic Names / magic names and fat arrows

- 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-7239e085-00628))_

### Yes. Consider this variation:

- In this book, we will use function declarations sparingly, and not use var at all. That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. The purpose of your own code is to get things done. The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-7239e085-01221))_

### Yes. Consider this variation: / Functional Iterators / caveat

- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-7239e085-01324))_

### Recipes with Data / mapWith

- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-7239e085-01440))_

### Like this: / operations on ordered collections

- 89 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-7239e085-01588))_


## Technical atoms

### Technical frame 1: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00631))_

> Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00629))_

```
const row = function () {
return mapWith(
function (column) { return column * arguments[0] },
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [1,4,9,16,25,36,49,64,81,100,121,144]
```

### Technical frame 2: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01442))_

> If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01441))_

```
const squaresOf = mapWith(n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 3: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01590))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01589))_

```
const mapWith = (fn, collection) =>
({
[Symbol.iterator] () {
const iterator = collection[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00570))_

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) |

<details>
<summary>Raw table text</summary>

```
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

</details>


## Related pages

- [[javascriptallonge-discussing]] - shared statements and technical atoms: Discussing shares source evidence from And also: / Magic Names / magic names and fat arrows: 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the t ... [truncated]; Discussing shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-idea]] - shared statements and technical atoms: Idea shares source evidence from And also: / Magic Names / magic names and fat arrows: 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the t ... [truncated]; Idea shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Yes. Consider this variation: / Functional Iterators / caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change.; Function shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Yes. Consider this variation: / Functional Iterators / caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change.; Iterator shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from Recipes with Data / mapWith: const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25] (2 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-operation]] - shared technical atoms: Operation shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Yes. Consider this variation:: In this book, we will use function declarations sparingly, and not use var at all. That does not mean that you should follow the exact same practice in your own code ... [truncated] (1 shared statement(s))
- [[javascriptallonge-functional-iterator]] - shared statements: Functional Iterators shares source evidence from Yes. Consider this variation: / Functional Iterators / caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. (1 shared statement(s))

## Source

- [[javascriptallonge]]
