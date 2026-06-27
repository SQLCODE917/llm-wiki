---
page_id: javascriptallonge-section-converting-non-tail-calls-to-tail-calls-5e566cdd
page_kind: source
summary: **converting non-tail-calls to tail-calls**: 19 source-backed entries and 12 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-converting-non-tail-calls-to-tail-calls-5e566cdd@79f834df2170ae200240924dffb0ed32
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

> Context: The obvious solution is push the 1 + work into the call to length. Here’s our first cut:
_(context: javascriptallonge.pdf (source-range-83ecb080-01430))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01431))_

> Context: This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:
_(context: javascriptallonge.pdf (source-range-83ecb080-01436))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01437))_

> Context: This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:
_(context: javascriptallonge.pdf (source-range-83ecb080-01436))_

> **const** length = (n) => lengthDelaysWork(n, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01439))_

> Context: Or we could use partial application:
_(context: javascriptallonge.pdf (source-range-83ecb080-01440))_

> **const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01441))_

> Context: Or we could use partial application:
_(context: javascriptallonge.pdf (source-range-83ecb080-01440))_

> **const** length = callLast(lengthDelaysWork, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01442))_

> Context: Or we could use partial application:
_(context: javascriptallonge.pdf (source-range-83ecb080-01440))_

> length(["foo", "bar", "baz"]) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-01443))_

> Context: This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith:
_(context: javascriptallonge.pdf (source-range-83ecb080-01444))_

> **const** mapWithDelaysWork = (fn, [first, ...rest], prepend) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-01447))_

> first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01448))_

> **const** mapWith = callLast(mapWithDelaysWork, []);
_(source: javascriptallonge.pdf (source-range-83ecb080-01451))_

> mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01452))_

> Context: We can use it with ridiculously large arrays:
_(context: javascriptallonge.pdf (source-range-83ecb080-01453))_

> mapWith((x) => x * x, [
_(source: javascriptallonge.pdf (source-range-83ecb080-01454))_

> Context: We can use it with ridiculously large arrays:
_(context: javascriptallonge.pdf (source-range-83ecb080-01453))_

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
_(source: javascriptallonge.pdf (source-range-83ecb080-01455))_
