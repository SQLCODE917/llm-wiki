---
page_id: javascriptallonge-recursion
page_kind: concept
summary: Recursion: 4 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-recursion@f96b379549ab69ca476722879cf3e3b0
---

# Recursion

What [[javascriptallonge]] covers about recursion:

## Statements

### Composing and Decomposing Data

- ## **Composing and Decomposing Data**

**==> picture [469 x 329] intentionally omitted <==**

**Stacked Cups**

Recursion is the root of computation since it trades description for time.—Alan Perlis, Epigrams in Programming[55] > 55http://www.cs.yale.edu/homes/perlis-alan/quotes.html _(javascriptallonge.pdf (source-range-83ecb080-00122))_

### Arrays and Destructuring Arguments

- 93

Composing and Decomposing Data **const** mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\ ], array), squareAll = (array) => mapWith((x) => x * x, array); squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ And to return to our first example, our version of length can be written as a fold: **const** length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) _//=> 5_

## **summary**

Linear recursion is a basic building block of algorithms. Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. Its specialized cases of mapping and folding are especially useful and can be used to build other functions. And finally, while folding is a special case of linear recursion, mapping is a special case of folding. _(javascriptallonge.pdf (source-range-83ecb080-00139))_

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

98 **const** mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === **undefined**

- ? prepend

- : mapWithDelaysWork(fn, rest, [...prepend, fn(first)]); **const** mapWith = callLast(mapWithDelaysWork, []); mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ We can use it with ridiculously large arrays: mapWith((x) => x * x, [

|0,|1,|2,|3,|4,|5,|6,|7,|8,|9,|

|---|---|---|---|---|---|---|---|---|---|

|10,|11,|12,|13,|14,|15,|16,|17,|18,|19,|

|20,|21,|22,|23,|24,|25,|26,|27,|28,|29,|

|30,|31,|32,|33,|34,|35,|36,|37,|38,|39,|

|40,|41,|42,|43,|44,|45,|46,|47,|48,|49,|

|50,|51,|52,|53,|54,|55,|56,|57,|58,|59,|

|60,|61,|62,|63,|64,|65,|66,|67,|68,|69,|

|70,|71,|72,|73,|74,|75,|76,|77,|78,|79,|

|80,|81,|82,|83,|84,|85,|86,|87,|88,|89,|

|90,|91,|92,|93,|94,|95,|96,|97,|98,|99,|

_// ..._

2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999 ])

_//=> [0,1,4,9,16,25,36,49,64,81,100,121,144,169,196, ..._ Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

## **factorials**

Introductions to recursion often mention calculating factorials:

In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: _(javascriptallonge.pdf (source-range-83ecb080-00145))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

104

Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious.[64] The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend.

We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

**Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded.

So here’s a question: If this is such a slow approach, why do some examples of “functional” algorithms work this exact way?

> 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript’s built-in arrays work. _(javascriptallonge.pdf (source-range-83ecb080-00153))_


## Technical atoms

### Technical frame 1: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00147))_

> Composing and Decomposing Data

99

5! = 5 x 4 x 3 x 2 x 1 = 120.

The naïve function for calcuating the factorial of a positive integer follows directly from the definition: **const** factorial = (n) => n == 1 ? n : n * factorial(n - 1); factorial(1) _//=> 1_ factorial(5) _//=> 120_ While this is mathematically elegant, it is computational filigree[63] .

Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n *

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00146))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |
```

</details>


## Related pages

- [[javascriptallonge-rest]] - shared statements and technical atoms: Rest shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  104  Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious. ... [truncated]; Rest shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
