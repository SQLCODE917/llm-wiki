---
page_id: javascriptallonge-mapwith
page_kind: concept
summary: Mapwith: 12 statement(s) and 15 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-mapwith@90a629d7d40bc43a37f06946731a6834
---

# Mapwith

What [[javascriptallonge]] covers about mapwith:

## Statements

### And also: / Building Blocks / partial application

- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-7239e085-00597))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments)

- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not 'production-ready' implementations. One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. _(javascriptallonge.pdf (source-range-7239e085-00954))_

- Let's step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] . _(javascriptallonge.pdf (source-range-7239e085-00957))_

- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to hang on to 2 (or 4 , or both, depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]) . _(javascriptallonge.pdf (source-range-7239e085-00961))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere

- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-7239e085-01022))_

### Composing and Decomposing Data / Mutation / mutation and data structures

- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-7239e085-01143))_

### Yes. Consider this variation: / Copy on Write / copy-on-read

- As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy because we won't be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node) . _(javascriptallonge.pdf (source-range-7239e085-01242))_

### Yes. Consider this variation: / Copy on Write / copy-on-write

- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-7239e085-01251))_

### Recipes with Data / mapWith

- Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-7239e085-01444))_

### Like this: / operations on ordered collections

- Let's define some operations on ordered collections. Here's mapWith , it takes an ordered collection, and returns another ordered collection representing a mapping over the original: 89 _(javascriptallonge.pdf (source-range-7239e085-01587))_

- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a collection operation . _(javascriptallonge.pdf (source-range-7239e085-01596))_

- Like mapWith , they preserve the ordered collection semantics of whatever you give them. _(javascriptallonge.pdf (source-range-7239e085-01603))_


## Technical atoms

### Technical frame 1: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00599))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00598))_

```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

### Technical frame 2: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00603))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00601))_

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Technical frame 3: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00603))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00602))_

```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```

### Technical frame 4: Composing and Decomposing Data / Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00957))_

> Let's step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00956))_

```
const mapWith = (fn, [first, ...rest]) =>
first === undefined
? []
: [fn(first), ...mapWith(fn, rest)];
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 5: Composing and Decomposing Data / Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00960))_

> Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00959))_

```
const mapWith = function (fn, [first, ...rest]) {
if (first === undefined) {
return [];
}
else {
const _temp1 = fn(first),
_temp2 = mapWith(fn, rest),
_temp3 = [_temp1, ..._temp2];
return _temp3;
}
}
```

### Technical frame 6: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00986))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00984))_

```
const mapWithDelaysWork = (fn, [first, ...rest], prepend) =>
first === undefined
? prepend
: mapWithDelaysWork(fn, rest, [...prepend, fn(first)]);
const mapWith = callLast(mapWithDelaysWork, []);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
We can use it with ridiculously large arrays:
```

### Technical frame 7: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00986))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00985))_

```
mapWith((x) => x * x, [
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
36,
37,
38,
39,
40,
41,
42,
43,
44,
45,
46,
47,
48,
49,
50,
51,
52,
53,
54,
55,
56,
57,
58,
59,
60,
61,
62,
63,
64,
65,
66,
67,
68,
69,
70,
71,
72,
73,
74,
75,
76,
77,
78,
79,
80,
81,
82,
83,
84,
85,
86,
87,
88,
89,
90,
91,
92,
93,
94,
95,
96,
97,
98,
99,
// ...
2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989,
2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999 ])
//=> [0,1,4,9,16,25,36,49,64,81,100,121,144,169,196, ...
```

### Technical frame 8: Composing and Decomposing Data / Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01019))_

> But when we try it on very large arrays, we discover that it is still very slow. Much slower than the built-in .map method for arrays. The right tool to discover why it's still slow is a memory profiler, but a simple inspection of the program will reveal the following:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01018))_

```
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 9: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01437))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01435))_

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Technical frame 10: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01440))_

> 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01438))_

```
const squaresOf = (list) =>
list.map(x => x * x);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 11: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01442))_

> If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01441))_

```
const squaresOf = mapWith(n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 12: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01444))_

> Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01443))_

```
const squaresOf = callRight(map, (n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 13: Like this: / operations on ordered collections

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

### Technical frame 14: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01593))_

> Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01592))_

```
const Evens = mapWith((x) => 2 * x, Numbers);
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
```

### Technical frame 15: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01596))_

> So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a collection operation .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01594))_

```
const Evens =
{
[Symbol.iterator] () {
const iterator = Numbers[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : 2 *value});
}
}
}
};
```


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Function shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (5 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Composing and Decomposing Data / Tail Calls (and Default Arguments): Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to ... [truncated]; Javascript shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments): const mapWith = function (fn, [first, ...rest]) { if (first === undefined) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_tem ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; partial application shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Return shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Argument shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-rest]] - shared statements and technical atoms: Rest shares source evidence from Composing and Decomposing Data / Tail Calls (and Default Arguments): Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to ... [truncated]; Rest shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments): const mapWith = function (fn, [first, ...rest]) { if (first === undefined) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_tem ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (3 shared atom(s))
- [[javascriptallonge-discussing]] - shared technical atoms: Discussing shares technical record from Recipes with Data / mapWith: const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25] (2 shared atom(s))
- [[javascriptallonge-idea]] - shared technical atoms: Idea shares technical record from Recipes with Data / mapWith: const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25] (2 shared atom(s))
- [[javascriptallonge-important]] - shared technical atoms: Important shares technical record from And also: / Building Blocks / partial application: const safeSquareAll = mapWith(maybe((n) => n * n)); (2 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms: Length shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls: const mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === undefined ? prepend : mapWithDelaysWork(fn, rest, [...prepend, fn(first)]); const mapWith = ca ... [truncated] (2 shared atom(s))
- [[javascriptallonge-operation]] - shared technical atoms: Operation shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-purpose]] - shared technical atoms: Purpose shares technical record from Recipes with Data / mapWith: const squaresOf = mapWith(n => n * n); squaresOf([1, 2, 3, 4, 5]) //=> [1, 4, 9, 16, 25] (2 shared atom(s))
- [[javascriptallonge-version]] - shared technical atoms: Version shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls: const mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === undefined ? prepend : mapWithDelaysWork(fn, rest, [...prepend, fn(first)]); const mapWith = ca ... [truncated] (2 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared atom(s))
- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-read: As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy beca ... [truncated] (2 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-section-recipes-with-data-mapwith-588e9415]] - source section: Recipes with Data / mapWith shares source evidence from Recipes with Data / mapWith: That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return th ... [truncated]; Recipes with Data / mapWith shares technical record from Recipes with Data / mapWith: [1, 2, 3, 4, 5].map(x => x * x) //=> [1, 4, 9, 16, 25] (6 shared statement(s), 6 shared atom(s))

## Source

- [[javascriptallonge]]
