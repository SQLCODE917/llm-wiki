---
page_id: javascriptallonge-section-converting-non-tail-calls-to-tail-calls-5e566cdd
page_kind: source
summary: **converting non-tail-calls to tail-calls**: 19 source-backed entries and 12 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-converting-non-tail-calls-to-tail-calls-5e566cdd@e9bf844d21028ba1b7916896b0f52a24
---

# **converting non-tail-calls to tail-calls**

From [[javascriptallonge]].

## Statements

- The obvious solution is push the 1 + work into the call to length. _(javascriptallonge.pdf (source-range-83ecb080-01430))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-83ecb080-01436))_
- Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. _(javascriptallonge.pdf (source-range-83ecb080-01436))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-83ecb080-01436))_
- This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. _(javascriptallonge.pdf (source-range-83ecb080-01444))_
- We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. _(javascriptallonge.pdf (source-range-83ecb080-01459))_
- And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-83ecb080-01459))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01430))_

> The obvious solution is push the 1 + work into the call to length. Here’s our first cut:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01431))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01436))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01437))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01436))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01439))_

> **const** length = (n) => lengthDelaysWork(n, 0);

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01440))_

> Or we could use partial application:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01441))_

> **const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01440))_

> Or we could use partial application:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01442))_

> **const** length = callLast(lengthDelaysWork, 0);

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01440))_

> Or we could use partial application:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01443))_

> length(["foo", "bar", "baz"]) _//=> 3_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01444))_

> This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01447))_

> **const** mapWithDelaysWork = (fn, [first, ...rest], prepend) =>

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01448))_

> first === **undefined**

### Technical atom 9

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01451))_

> **const** mapWith = callLast(mapWithDelaysWork, []);

### Technical atom 10

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01452))_

> mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01453))_

> We can use it with ridiculously large arrays:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01454))_

> mapWith((x) => x * x, [

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01453))_

> We can use it with ridiculously large arrays:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01455))_

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
```

</details>
