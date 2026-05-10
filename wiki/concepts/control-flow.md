---
title: Control Flow
type: concept
tags: [javascript, operators, logic]
status: draft
last_updated: 2026-05-09
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2195-L2195
  - js-allonge:normalized:L2207-L2207
  - js-allonge:normalized:L2209-L2210
  - js-allonge:normalized:L2239-L2239
  - js-allonge:normalized:L2261-L2265
  - js-allonge:normalized:L2267-L2271
  - js-allonge:normalized:L2957-L2957
---

# Control Flow

## Summary

Control flow in JavaScript refers to the order in which statements are executed and the mechanisms that alter this order, such as conditional logic and loops. Key operators like &&, ||, and the ternary operator serve dual roles as both logical operators and control-flow mechanisms.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| The logical AND (&&) and OR (\|\|) operators in JavaScript function as control-flow mechanisms, evaluating expressions lazily and returning the value of either the left or right operand based on... | "The && and \|\| operators are binary infix operators that perform "logical and" and "logical or" respectively:" | `normalized:L2195-L2195` | [Source](../sources/js-allonge.md) |
| The logical AND (&&) and OR (\|\|) operators in JavaScript function as control-flow mechanisms, evaluating expressions lazily and returning the value of either the left or right operand based on... | "- && evaluates its left-hand expression. - If its left-hand expression evaluates to something falsy, && returns the value of its lefthand expression without evaluating its right-hand expression. -..." | `normalized:L2261-L2265` | [Source](../sources/js-allonge.md) |
| The logical AND (&&) and OR (\|\|) operators in JavaScript function as control-flow mechanisms, evaluating expressions lazily and returning the value of either the left or right operand based on... | "- \|\| evaluates its left-hand expression. - If its left-hand expression evaluates to something truthy, \|\| returns the value of its lefthand expression without evaluating its right-hand..." | `normalized:L2267-L2271` | [Source](../sources/js-allonge.md) |
| JavaScript's logical operators behave differently from traditional boolean operators due to their handling of truthiness, making them useful for conditional execution and default value assignment. | "Our logical operators !, &&, and \|\| are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is..." | `normalized:L2239-L2239` | [Source](../sources/js-allonge.md) |
| JavaScript's logical operators behave differently from traditional boolean operators due to their handling of truthiness, making them useful for conditional execution and default value assignment. | "The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on _truthiness_ , not on boolean values. This affects the way the !, &&, and..." | `normalized:L2207-L2207` | [Source](../sources/js-allonge.md) |
| The ternary operator serves as a concise alternative to if-else blocks for simple conditional assignments, and is often used in functional programming patterns to express control flow elegantly. | "JavaScript inherited an operator from the C family of languages, the _ternary_ operator. It's the only operator that takes _three_ arguments. It looks like this: first ? second : third. It..." | `normalized:L2209-L2210` | [Source](../sources/js-allonge.md) |
| The ternary operator serves as a concise alternative to if-else blocks for simple conditional assignments, and is often used in functional programming patterns to express control flow elegantly. | "**const** factorial = (n, work) => n === 1 ? work : factorial(n - 1, n * work); factorial(1, 1) _//=> 1_ factorial(5, 1) _//=> 120_" | `normalized:L2957-L2957` | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding control flow is essential for writing expressive and efficient JavaScript code. Logical operators && and || are not just for boolean logic-they act as control structures that enable short-circuit evaluation, allowing developers to write concise conditional expressions. This behavior is fundamental to idiomatic JavaScript programming and supports functional programming techniques.

## Related pages

- [Data Types](../concepts/data-types.md)
- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
