---
title: Control Flow
type: concept
tags: [javascript, programming, logic]
status: draft
last_updated: 2026-05-11
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2207-L2207
  - js-allonge:normalized:L2209-L2217
  - js-allonge:normalized:L2239-L2239
  - js-allonge:normalized:L2261-L2266
  - js-allonge:normalized:L2267-L2271
  - js-allonge:normalized:L2311-L2311
  - js-allonge:normalized:L2343-L2343
---

# Control Flow

## Summary

Control flow in programming refers to the order in which individual statements, instructions, or function calls are executed or evaluated. In JavaScript, control flow is managed through conditional statements, loops, and operators that determine the execution path of code based on runtime conditions.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| JavaScript's logical operators && and \|\| implement short-circuit evaluation, where the second operand is only evaluated if necessary based on the truthiness of the first operand. | "- && evaluates its left-hand expression. - If its left-hand expression evaluates to something falsy, && returns the value of its lefthand expression without evaluating its right-hand expression. -..." | `normalized:L2261-L2266` | [Source](../sources/js-allonge.md) |
| JavaScript's logical operators && and \|\| implement short-circuit evaluation, where the second operand is only evaluated if necessary based on the truthiness of the first operand. | "- \|\| evaluates its left-hand expression. - If its left-hand expression evaluates to something truthy, \|\| returns the value of its lefthand expression without evaluating its right-hand..." | `normalized:L2267-L2271` | [Source](../sources/js-allonge.md) |
| JavaScript's logical operators && and \|\| implement short-circuit evaluation, where the second operand is only evaluated if necessary based on the truthiness of the first operand. | "This is more than just an optimization. It's best to think of \|\| and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression..." | `normalized:L2311-L2311` | [Source](../sources/js-allonge.md) |
| The ternary operator in JavaScript provides a concise way to express conditional logic, but unlike traditional control structures, it evaluates expressions rather than statements and has shortcut... | "JavaScript inherited an operator from the C family of languages, the _ternary_ operator. It's the only operator that takes _three_ arguments. It looks like this: first ? second : third. It..." | `normalized:L2209-L2217` | [Source](../sources/js-allonge.md) |
| The ternary operator in JavaScript provides a concise way to express conditional logic, but unlike traditional control structures, it evaluates expressions rather than statements and has shortcut... | "- The ternary operator (?:), \|\|, and && are control flow operators, they do not always return true or false, and they have short-cut semantics." | `normalized:L2343-L2343` | [Source](../sources/js-allonge.md) |
| Control flow constructs in JavaScript, such as if/else statements and logical operators, rely on the concept of truthiness rather than strict boolean values, affecting how expressions are evaluated. | "Our logical operators !, &&, and \|\| are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is..." | `normalized:L2239-L2239` | [Source](../sources/js-allonge.md) |
| Control flow constructs in JavaScript, such as if/else statements and logical operators, rely on the concept of truthiness rather than strict boolean values, affecting how expressions are evaluated. | "The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on _truthiness_ , not on boolean values. This affects the way the !, &&, and..." | `normalized:L2207-L2207` | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding control flow is essential for writing dynamic and responsive programs. It allows developers to make decisions, repeat actions, and manage complex logic within their applications. In JavaScript, control flow is deeply intertwined with concepts like truthiness, lazy evaluation, and functional programming techniques, making it a foundational aspect of the language.

## Related pages

- [Arrays](../concepts/arrays.md)
- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
