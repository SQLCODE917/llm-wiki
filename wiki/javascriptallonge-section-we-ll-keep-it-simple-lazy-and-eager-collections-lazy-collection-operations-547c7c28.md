---
page_id: javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-lazy-collection-operations-547c7c28
page_kind: source
summary: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations: 22 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-lazy-collection-operations-547c7c28@1ea8630ad9f56d6fcd594568def0bb47
---

# We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-b2c43c7f]] - broader source section: We'll keep it simple: / Lazy and Eager Collections

## Statements

- 'Laziness' is a very pejorative word when applied to people. But it can be an excellent strategy for efficiency in algorithms. Let's be precise: Laziness is the characteristic of not doing any work until you know you need the result of the work. _(javascriptallonge.pdf (source-range-7239e085-01783))_
- Both expressions evaluate to 220 . And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-7239e085-01786))_
- But it's still illustrative to dissect something important: Array's .map and .filter methods gather their results into new arrays. Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-7239e085-01787))_
- Whereas the .map and .filter methods on Pair work with iterators. They produce small iterable objects that refer back to the original iteration. This reduces the memory footprint. When working with very large collections and many operations, this can be important. _(javascriptallonge.pdf (source-range-7239e085-01788))_
- This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-7239e085-01791))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. _(javascriptallonge.pdf (source-range-7239e085-01792))_
- Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-7239e085-01800))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-7239e085-01786))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-7239e085-01787))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. _(javascriptallonge.pdf (source-range-7239e085-01792))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-7239e085-01800))_

## Technical atoms

### Technical frame 1: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01786))_

> Both expressions evaluate to 220 . And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01785))_

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
```

### Technical frame 2: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01791))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01788))_

> When working with very large collections and many operations, this can be important.

### Technical frame 3: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01791))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01789))_

> The effect is even more pronounced when we use methods like first , until , or take :

### Technical frame 4: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01791))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01790))_

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
```

### Technical frame 5: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01800))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01794))_

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => {
console.log(`squaring ${x}`);
return x * x
})
.filter((x) => {
console.log(`filtering ${x}`);
return x % 2 == 0
})
.first()
//=>
squaring 29
filtering 841
squaring 28
filtering 784
784
```

### Technical frame 6: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01800))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01795))_

> If we write the almost identical thing with an array, we get a different behaviour:

### Technical frame 7: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01800))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01796))_

```
[ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
.reverse()
.map((x) => {
console.log(`squaring ${x}`);
return x * x
})
.filter((x) => {
console.log(`filtering ${x}`);
return x % 2 == 0
})[0]
//=>
squaring 0
squaring 1
squaring 2
squaring 3
...
squaring 28
squaring 29
filtering 0
filtering 1
filtering 4
...
filtering 784
filtering 841
784
```

### Technical frame 8: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01800))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01799))_

```
const Numbers = Object.assign({
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}, LazyCollection);
const firstCubeOver1234 =
Numbers
.map((x) => x * x * x)
.filter((x) => x > 1234)
.first()
//=> 1331
```
