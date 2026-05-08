---
title: Recursion
type: concept
tags: [recursion, linear-recursion, mapping, functional-programming]
status: draft
last_updated: 2026-05-08
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2637-L2637
  - js-allonge:normalized:L2711-L2711
  - js-allonge:normalized:L2773-L2773
---

# Recursion

## Summary

Recursion is a programming technique where a function calls itself to solve a problem. It is particularly useful for handling data structures that have a self-similar or nested nature, such as lists and trees. Linear recursion is a specific form where a function processes one element of a data structure at a time, making it intuitive and easy to understand.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| The length function exemplifies recursion by calling itself, aligning with the recursive definition of a list. | "Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is..." | `normalized:L2637-L2637` | [Source](../sources/js-allonge.md) |
| Linear recursion acts as a core building block for algorithms, mirroring the construction of linear data structures. | "Linear recursion is a basic building block of algorithms. Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable." | `normalized:L2773-L2773` | [Source](../sources/js-allonge.md) |
| Mapping represents a particular application of linear recursion, enabling the transformation of elements within a data structure. | "This specific case of linear recursion is called "mapping," and it is not necessary to constantly write out the same pattern again and again." | `normalized:L2711-L2711` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
