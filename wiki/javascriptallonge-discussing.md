---
page_id: javascriptallonge-discussing
page_kind: concept
summary: Discussing: 4 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-discussing@d13792cf9408737f0831b1a4408604f7
---

# Discussing

What [[javascriptallonge]] covers about discussing:

## Statements

### And also: / Magic Names / magic names and fat arrows

- 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-7239e085-00628))_

### Recipes with Data / mapWith

- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-7239e085-01440))_

### Like this: / ordered collections

- The iterables we're discussing represent ordered collections . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example: _(javascriptallonge.pdf (source-range-7239e085-01579))_

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

### Technical frame 3: Like this: / ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01581))_

> This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01580))_

```
const abc = ["a", "b", "c"];
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
```

### Technical frame 4: Like this: / operations on ordered collections

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


## Related pages

- [[javascriptallonge-idea]] - shared statements and technical atoms: Idea shares source evidence from And also: / Magic Names / magic names and fat arrows: 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the t ... [truncated]; Idea shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-purpose]] - shared statements and technical atoms: Purpose shares source evidence from And also: / Magic Names / magic names and fat arrows: 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the t ... [truncated]; Purpose shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from Recipes with Data / mapWith: const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25] (2 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-operation]] - shared technical atoms: Operation shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
