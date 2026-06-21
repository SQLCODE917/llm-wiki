---
page_id: javascriptallonge-factorials
page_kind: source
summary: Chapter on factorials from JavaScript Allongé.
sources: raw/javascriptallonge.pdf p.121-123
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses the calculation of factorials in JavaScript, focusing on recursive and tail-recursive approaches.

## Key supported claims

- The naïve function for calcuating the factorial of a positive integer follows directly from the definition: const factorial = (n) => n == 1 ? n : n * factorial(n - 1); (raw/javascriptallonge.pdf p.121-123)
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1). (raw/javascriptallonge.pdf p.121-123)
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. (raw/javascriptallonge.pdf p.121-123)
