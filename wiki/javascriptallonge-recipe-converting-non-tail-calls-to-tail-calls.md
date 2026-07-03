---
page_id: javascriptallonge-recipe-converting-non-tail-calls-to-tail-calls
page_kind: recipe
page_family: recipe-pattern
summary: converting non-tail-calls to tail-calls: reusable source-backed pattern with 6 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: converting-non-tail-calls-to-tail-calls
projection_coverage: recipe-javascriptallonge-recipe-converting-non-tail-calls-to-tail-calls@630def3f4561196ba6b75547c64a7a95
---

# converting non-tail-calls to tail-calls

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-converting-non-tail-calls-to-tai-dc131bb9]].
- Evidence roles: decision, constraint, explanation, procedure, example.

## Applicability And Rationale

- The obvious solution is push the 1 + work into the call to length . _(javascriptallonge.pdf (source-range-7239e085-00978))_
- Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. _(javascriptallonge.pdf (source-range-7239e085-00980))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-7239e085-00980))_
- This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. _(javascriptallonge.pdf (source-range-7239e085-00983))_
- We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. _(javascriptallonge.pdf (source-range-7239e085-00986))_
- And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-7239e085-00986))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00979)_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? 0 + numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
lengthDelaysWork(["foo", "bar", "baz"], 0)
//=> 3
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00981)_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
const length = (n) =>
lengthDelaysWork(n, 0);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00982)_

```
Or we could use partial application:
const callLast = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const length = callLast(lengthDelaysWork, 0);
length(["foo", "bar", "baz"])
//=> 3
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00984)_

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

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00985)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-converting-non-tail-calls-to-tai-dc131bb9]]
