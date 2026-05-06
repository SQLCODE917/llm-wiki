---
title: Recursion
type: concept
tags: []
status: draft
last_updated: 2026-05-06
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L3486
  - js-allonge:normalized:L3731
  - js-allonge:normalized:L3752
  - js-allonge:normalized:L3920
  - js-allonge:normalized:L7402
  - js-allonge:normalized:L8103
---

# Recursion

Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller subproblems.

## Source-backed details

| Claim | Evidence | Locator | Source |
| ----- | -------- | ------- | ------ |
| Linear recursion is a simple form of divide-and-conquer strategy. | "This simpler form of "divide and conquer" is called linear recursion. It's very useful and simple to" | `normalized:L3486` | [JavaScript Allongé](../sources/js-allonge.md) |
| Tail-call optimization occurs when a function's final action is to invoke another function and return its result. | "A "tail-call" occurs when a function's last act is to invoke another function, and then return whatever" | `normalized:L3731` | [JavaScript Allongé](../sources/js-allonge.md) |
| When a function makes a tail call, JavaScript optimizes away the function call overhead and stack space. | "a function makes a call in tail position, JavaScript optimizes away the function call overhead" | `normalized:L3752` | [JavaScript Allongé](../sources/js-allonge.md) |
| Tail-call optimization allows efficient processing of large arrays without memory overhead. | "Brilliant! We can map over large arrays without incurring all the memory and performance overhead" | `normalized:L3920` | [JavaScript Allongé](../sources/js-allonge.md) |
| Recursive enumeration is useful for traversing hierarchical data structures like trees. | "we have to recursively enumerate something." | `normalized:L7402` | [JavaScript Allongé](../sources/js-allonge.md) |
| Generator functions can implement recursive iteration using yield\* syntax. | "function * tree (iterable) {" | `normalized:L8103` | [JavaScript Allongé](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)