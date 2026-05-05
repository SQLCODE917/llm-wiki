---
title: Logical Operators
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# Logical Operators

Logical operators in JavaScript are control-flow operators that operate on truthiness rather than strict boolean values, with short-circuit evaluation behavior.

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Logical operators in JavaScript are based on truthiness and falsiness, not strict boolean values | "Logical operators are based on truthiness and falsiness, not the strict values true and false." | `normalized:L3075` | [JavaScript Allonge](../sources/js-allonge.md) |
| The ! operator is a logical operator that always returns true or false | "The ! operator is a logical operator, it always returns true or false." | `normalized:L3076` | [JavaScript Allonge](../sources/js-allonge.md) |
| The  AND  and  OR  operators are control-flow operators, not logical operators | "The ternary operator (?:),  OR , and  AND  are control flow operators, they do not always return" | `normalized:L3077` | [JavaScript Allonge](../sources/js-allonge.md) |
| The  AND  and  OR  operators perform short-circuit evaluation based on the left-hand operand | "The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not." | `normalized:L3042` | [JavaScript Allonge](../sources/js-allonge.md) |
| The && operator evaluates the right side only if the left side is truthy | "if n !== 1, JavaScript evaluates n !== 1 && even(n - 2) as false without ever evaluating even(n - 2)." | `normalized:L3040` | [JavaScript Allonge](../sources/js-allonge.md) |
| The  OR  operator evaluates the right side only if the left side is falsy | "if n === 1, JavaScript evaluates n !== 1  AND  even(n - 2) as false without ever evaluating even(n - 2)." | `normalized:L3041` | [JavaScript Allonge](../sources/js-allonge.md) |
| The  AND  and  OR  operators don't strictly operate on logical values and don't commute | "In JavaScript,  AND  and  OR  aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a  OR  b is not always equal to b  OR  a, and the same goes for  AND ." | `normalized:L3012` | [JavaScript Allonge](../sources/js-allonge.md) |

Understanding logical operators in JavaScript is crucial because they behave differently from traditional logical operators in mathematics or other programming languages. They're control-flow operators that leverage truthiness/falsiness evaluation and short-circuit behavior, which enables efficient conditional execution and allows developers to write concise code patterns for handling default values, conditional assignments, and early returns. This behavior is fundamental to writing idiomatic JavaScript and understanding how expressions are evaluated in conditional contexts.

- [JavaScript Allonge](../sources/js-allonge.md)