---
page_id: javascriptallonge-section-factorials-46f54e78
page_kind: source
summary: **factorials**: 10 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-factorials-46f54e78@2f1e2a54342bc776499ac745f7040114
---

# **factorials**

From [[javascriptallonge]].

## Statements

- In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. _(javascriptallonge.pdf (source-range-83ecb080-01462))_
- While this is mathematically elegant, it is computational filigree[63] . _(javascriptallonge.pdf (source-range-83ecb080-01469))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n - 1). _(javascriptallonge.pdf (source-range-83ecb080-01470))_
- As before, we wrote a factorialWithDelayedWork function, then used partial application (callLast) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-83ecb080-01479))_
- As before, we wrote a factorialWithDelayedWork function, then used partial application (callLast) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-83ecb080-01479))_

## Technical atoms

> Context: In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01462))_

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
_(source: javascriptallonge.pdf (source-range-83ecb080-01463))_

> Context: The naïve function for calcuating the factorial of a positive integer follows directly from the definition: Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n - 1). We can do the same conversion, pass in the work to be done:
_(context: javascriptallonge.pdf (source-range-83ecb080-01467, source-range-83ecb080-01470))_

> **const** factorial = (n) => n == 1 ? n : n * factorial(n - 1); factorial(1) _//=> 1_ factorial(5) _//=> 120_
_(source: javascriptallonge.pdf (source-range-83ecb080-01468))_

> **const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01476))_

> **const** factorial = callLast(factorialWithDelayedWork, 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-01477))_

> factorial(1) _//=> 1_ factorial(5) _//=> 120_
_(source: javascriptallonge.pdf (source-range-83ecb080-01478))_
