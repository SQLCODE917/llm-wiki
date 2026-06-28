---
page_id: javascriptallonge-mapwith
page_kind: concept
summary: Mapwith: 12 statement(s) and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-mapwith@fb819a9afa8438658119de61c2aba3ee
---

# Mapwith

What [[javascriptallonge]] covers about mapwith:

## Statements

### partial application

- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-31a4cf47-00598))_

### Tail Calls (and Default Arguments)

- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not 'production-ready' implementations. One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. _(javascriptallonge.pdf (source-range-31a4cf47-00954))_

- Let's step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] . _(javascriptallonge.pdf (source-range-31a4cf47-00957))_

- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to hang on to 2 (or 4 , or both, depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]) . _(javascriptallonge.pdf (source-range-31a4cf47-00961))_

### Garbage, Garbage Everywhere

- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-31a4cf47-01022))_

### mutation and data structures

- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-31a4cf47-01143))_

### copy-on-read

- As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy because we won't be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node) . _(javascriptallonge.pdf (source-range-31a4cf47-01242))_

### copy-on-write

- mapWith This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-31a4cf47-01252))_

### mapWith

- Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-31a4cf47-01444))_

### operations on ordered collections

- Let's define some operations on ordered collections. Here's mapWith , it takes an ordered collection, and returns another ordered collection representing a mapping over the original: 89 _(javascriptallonge.pdf (source-range-31a4cf47-01587))_

- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a collection operation . _(javascriptallonge.pdf (source-range-31a4cf47-01596))_

- Like mapWith , they preserve the ordered collection semantics of whatever you give them. _(javascriptallonge.pdf (source-range-31a4cf47-01603))_


## Technical atoms

### Technical frame 1: partial application

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00600))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00599))_

```
const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9]
```

### Technical frame 2: partial application

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00604))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00602))_

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Technical frame 3: partial application

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00604))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00603))_

```
safeSquareAll([1, null , 2, 3]) //=> [1, null, 4, 9]
```

### Technical frame 4: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00957))_

> Let's step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00956))_

```
const mapWith = (fn, [first, ...rest]) => first === undefined ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### Technical frame 5: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00960))_

> Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00959))_

```
const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; return _temp3; } }
```

### Technical frame 6: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01019))_

> But when we try it on very large arrays, we discover that it is still very slow. Much slower than the built-in .map method for arrays. The right tool to discover why it's still slow is a memory profiler, but a simple inspection of the program will reveal the following:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01018))_

```
const mapWith = (fn, [first, ...rest], prepend = []) => first === undefined ? prepend : mapWith(fn, rest, [...prepend, fn(first)]); mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### Technical frame 7: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01437))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01435))_

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Technical frame 8: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01440))_

> 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01438))_

```
const squaresOf = (list) => list.map(x => x * x); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25]
```

### Technical frame 9: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01442))_

> If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01441))_

```
const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25]
```

### Technical frame 10: mapWith

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01444))_

> Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01443))_

```
const squaresOf = callRight(map, (n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25]
```

### Technical frame 11: operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01590))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01589))_

```
const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: done ? undefined : fn(value)}); } } } });
```

### Technical frame 12: operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01593))_

> Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01592))_

```
const Evens = mapWith((x) => 2 * x, Numbers); for ( const i of Evens) { console.log(i) } //=> 0 2 4 ... for ( const i of Evens) { console.log(i) } //=> 0 2 4 ...
```

### Technical frame 13: operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01596))_

> So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a collection operation .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01594))_

```
const Evens = { [Symbol.iterator] () { const iterator = Numbers[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: done ? undefined : 2 *value}); } } } };
```


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Function shares technical record from partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (4 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Return shares technical record from partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Argument shares technical record from partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Tail Calls (and Default Arguments): Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to ... [truncated]; Javascript shares technical record from Tail Calls (and Default Arguments): const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_te ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-rest]] - shared statements and technical atoms: Rest shares source evidence from Tail Calls (and Default Arguments): Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to ... [truncated]; Rest shares technical record from Tail Calls (and Default Arguments): const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_te ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (3 shared atom(s))
- [[javascriptallonge-discussing]] - shared technical atoms: Discussing shares technical record from mapWith: const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25] (2 shared atom(s))
- [[javascriptallonge-idea]] - shared technical atoms: Idea shares technical record from mapWith: const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25] (2 shared atom(s))
- [[javascriptallonge-important]] - shared technical atoms: Important shares technical record from partial application: const safeSquareAll = mapWith(maybe((n) => n * n)); (2 shared atom(s))
- [[javascriptallonge-operation]] - shared technical atoms: Operation shares technical record from operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-purpose]] - shared technical atoms: Purpose shares technical record from mapWith: const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25] (2 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared atom(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated] (2 shared statement(s))
- [[javascriptallonge-array]] - shared statements: Array shares source evidence from Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from copy-on-write: mapWith This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-section-mapwith-fa334002]] - source section: mapWith shares source evidence from mapWith: That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return th ... [truncated]; mapWith shares technical record from mapWith: [1, 2, 3, 4, 5].map(x => x * x) //=> [1, 4, 9, 16, 25] (6 shared statement(s), 6 shared atom(s))

## Source

- [[javascriptallonge]]
