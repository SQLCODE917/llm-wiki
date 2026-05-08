---
title: Recursion
type: concept
tags: []
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
---

# Recursion

Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems. It serves as a fundamental approach in algorithm design, particularly when dealing with data structures that have a linear, nested nature such as lists.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Linear recursion breaks a problem into smaller parts and solves them recursively. | "## **linear recursion**" | normalized:L2639-L2639 | [Source](../sources/js-allonge.md) |
| Linear recursion is a basic building block of algorithms that parallels the construction of linear data structures like lists. | "Linear recursion is a basic building block of algorithms. Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. Its specialized..." | normalized:L2773-L2773 | [Source](../sources/js-allonge.md) |
| Converting a non-tail-call to a tail-call involves pushing computation into the recursive call to avoid accumulating stack frames. | "The obvious solution?" | normalized:L2837-L2837 | [Source](../sources/js-allonge.md) |
| Tail-call optimization prevents memory buildup when recursively processing large data structures. | "This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith:" | normalized:L2873-L2873 | [Source](../sources/js-allonge.md) |
| Factorial calculations can be made tail-recursive by passing accumulated work as an additional parameter. | "Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n - 1). We can do the same conversion, pass..." | normalized:L2933-L2933 | [Source](../sources/js-allonge.md) |

## Why it matters

Recursion provides an elegant way to express algorithms that naturally decompose into similar subproblems. Understanding how to convert recursive calls into tail-recursive forms allows developers to write more efficient code that avoids excessive memory usage, especially when handling large datasets. This optimization is crucial for performance in languages that support tail-call elimination.

## Source pages

- [Source](../sources/js-allonge.md)
```