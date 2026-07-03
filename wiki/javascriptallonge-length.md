---
page_id: javascriptallonge-length
page_kind: concept
page_family: topic-concept
summary: Length: 6 statement(s) and 17 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-length@975914b3f760a924107d26c8028c57e4
---

# Length

What [[javascriptallonge]] covers about length:

## Statements

### Composing and Decomposing Data / Self-Similarity

- We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-7239e085-00901))_

- Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-7239e085-00904))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-7239e085-00974))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

- This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith : _(javascriptallonge.pdf (source-range-7239e085-00983))_

### Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

- Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous values. Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-7239e085-01117))_

### Yes. Consider this variation: / Making Data Out Of Functions

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-7239e085-01328))_


## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00901))_

> We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length !

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00900))_

<a id="atom-technical-atom-e298cdaa6ee5e32b"></a>

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: // ???
```

### Technical frame 2: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00902))_

<a id="atom-technical-atom-dce776a77328aa08"></a>

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
Let’s try it!
length([])
//=> 0
length(["foo"])
//=> 1
length(["foo", "bar", "baz"])
```

### Technical frame 3: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00903))_

<a id="atom-technical-atom-65ebfed4d2b01ae4"></a>

```
//=> 3
```

### Technical frame 4: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00945))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00937))_

<a id="atom-technical-atom-9feefbdde8f3ed2c"></a>

```
const sumSquares = ([first, ...rest]) => first === undefined
? 0
: first * first + sumSquares(rest);
sumSquares([1, 2, 3, 4, 5])
//=> 55
```

### Technical frame 5: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00945))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00950))_

<a id="atom-technical-atom-ac69df9074b19205"></a>

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
length([1, 2, 3, 4, 5])
//=> 5
```

### Technical frame 6: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00974))_

> The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00973))_

<a id="atom-technical-atom-2634a0aa2029afd4"></a>

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
```

### Technical frame 7: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00980))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00979))_

<a id="atom-technical-atom-d0492cb61af780f2"></a>

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? 0 + numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
lengthDelaysWork(["foo", "bar", "baz"], 0)
//=> 3
```

### Technical frame 8: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00986))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00984))_

<a id="atom-technical-atom-6dcf576313bfb287"></a>

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

### Technical frame 9: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00986))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00985))_

<a id="atom-technical-atom-9b78a5d7d303ca68"></a>

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

### Technical frame 10: Yes. Consider this variation: / Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01330))_

> A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01329))_

<a id="atom-technical-atom-8099f5b267d8f12e"></a>

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest.first
//=> 2
OneTwoThree.rest.rest.first
//=> 3
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

### Technical frame 11: Yes. Consider this variation: / Making Data Out Of Functions / lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01385))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01380))_

<a id="atom-technical-atom-0911e44845c5a8dc"></a>

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(rest(aPair));
length(l123)
//=> 3
const reverse = (aPair, delayed = EMPTY) =>
aPair === EMPTY
? delayed
: reverse(rest(aPair), pair(first(aPair), delayed));
const mapWith = (fn, aPair, delayed = EMPTY) =>
aPair === EMPTY
? reverse(delayed)
: mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed));
const doubled = mapWith((x) => x * 2, l123);
first(doubled)
//=> 2
first(rest(doubled))
//=> 4
first(rest(rest(doubled)))
//=> 6
Can we do the same with the linked lists we build out of functions? Yes:
const first = K,
rest
= K(I),
pair = V,
EMPTY = (() => {});
const l123 = pair(1)(pair(2)(pair(3)(EMPTY)));
```

### Technical frame 12: Yes. Consider this variation: / Making Data Out Of Functions / lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01385))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01381))_

<a id="atom-technical-atom-0231efcf9de2fb7c"></a>

```
rest
= K(I),
pair = V,
EMPTY = (() => {});
const l123 = pair(1)(pair(
l123(first)
//=> 1
l123(rest)(first)
```

### Technical frame 13: Yes. Consider this variation: / Making Data Out Of Functions / lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01385))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01382))_

<a id="atom-technical-atom-ad481489b3763dce"></a>

```
//=> 2
return l123(rest)(rest)(first)
//=> 3
We write them in a backwards way, but they seem to work. How about
```

### Technical frame 14: Yes. Consider this variation: / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01394))_

> Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01391))_

<a id="atom-technical-atom-9a8e65206b0ca894"></a>

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(aPair(rest));
```

### Technical frame 15: Yes. Consider this variation: / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01394))_

> Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01393))_

<a id="atom-technical-atom-d79ac27d8419c233"></a>

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(rest)))
);
```

### Technical frame 16: Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01416))_

> We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01415))_

<a id="atom-technical-atom-7584d0bd3f95e295"></a>

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
```

### Technical frame 17: Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01419))_

> The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01418))_

<a id="atom-technical-atom-f6632ca1ca20da83"></a>

```
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Composing and Decomposing Data / Self-Similarity: Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to c ... [truncated]; Function shares technical record from Composing and Decomposing Data / Self-Similarity: const length = ([first, ...rest]) => first === undefined ? 0 : // ??? (3 shared statement(s), 12 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists: Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous value ... [truncated]; List shares technical record from Composing and Decomposing Data / Self-Similarity: const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); Let’s try it! length([]) //=> 0 length(["foo"]) //=> 1 length(["foo", "bar", "baz"]) (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical record from Yes. Consider this variation: / Making Data Out Of Functions: const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest.first //=> 2 One ... [truncated] (3 shared atom(s))
- [[javascriptallonge-version]] - shared statements and technical atoms: Version shares source evidence from Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls: This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this te ... [truncated]; Version shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls: const mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === undefined ? prepend : mapWithDelaysWork(fn, rest, [...prepend, fn(first)]); const mapWith = ca ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls: const mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === undefined ? prepend : mapWithDelaysWork(fn, rest, [...prepend, fn(first)]); const mapWith = ca ... [truncated] (2 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls: const mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === undefined ? prepend : mapWithDelaysWork(fn, rest, [...prepend, fn(first)]); const mapWith = ca ... [truncated] (2 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization: const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); (1 shared atom(s))
- [[javascriptallonge-seen]] - shared technical atoms: Seen shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls: const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysW ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
