---
title: Control Flow
type: concept
tags: [javascript, programming, logic]
status: draft
last_updated: 2026-05-08
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1205-L1205
  - js-allonge:normalized:L1243-L1245
  - js-allonge:normalized:L2203-L2205
  - js-allonge:normalized:L2209-L2217
  - js-allonge:normalized:L2239-L2240
  - js-allonge:normalized:L2259-L2271
  - js-allonge:normalized:L2273-L2283
  - js-allonge:normalized:L2289-L2299
  - js-allonge:normalized:L2315-L2315
  - js-allonge:normalized:L2327-L2333
---

# Control Flow

## Summary

Control flow refers to the order in which individual statements, instructions, or function calls are executed or evaluated in a program. In JavaScript, control flow is managed through conditional logic, loops, and operators that influence execution paths based on boolean evaluations.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Blocks in JavaScript can be used in various contexts beyond function bodies, such as within conditional statements, enabling structured code organization. | "We use the const keyword in a _const statement_ . const statements occur inside blocks, we can't use them when we write a fat arrow that has an expression as its body." | `normalized:L1205-L1205` | [Source](../sources/js-allonge.md) |
| Blocks in JavaScript can be used in various contexts beyond function bodies, such as within conditional statements, enabling structured code organization. | "Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if..." | `normalized:L1243-L1245` | [Source](../sources/js-allonge.md) |
| JavaScript's logical operators && and \|\| serve dual purposes as both logical operators and control-flow mechanisms, returning values based on truthiness rather than just boolean outcomes. | "In JavaScript, there is a notion of "truthiness." Every value is either "truthy" or "falsy." Obviously, false is falsy. So are null and undefined, values that semantically represent "no value."..." | `normalized:L2203-L2205` | [Source](../sources/js-allonge.md) |
| JavaScript's logical operators && and \|\| serve dual purposes as both logical operators and control-flow mechanisms, returning values based on truthiness rather than just boolean outcomes. | "Our logical operators !, &&, and \|\| are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is..." | `normalized:L2239-L2240` | [Source](../sources/js-allonge.md) |
| JavaScript's logical operators && and \|\| serve dual purposes as both logical operators and control-flow mechanisms, returning values based on truthiness rather than just boolean outcomes. | "First, and unlike !, && and \|\| do not necessarily evaluate to true or false. To be precise: - && evaluates its left-hand expression. - If its left-hand expression evaluates to something falsy,..." | `normalized:L2259-L2271` | [Source](../sources/js-allonge.md) |
| JavaScript's logical operators && and \|\| serve dual purposes as both logical operators and control-flow mechanisms, returning values based on truthiness rather than just boolean outcomes. | "If we look at our examples above, we see that when we pass true and false to && and \|\|, we do indeed get true or false as a result. But when we pass other values, we no longer get true or false:..." | `normalized:L2273-L2283` | [Source](../sources/js-allonge.md) |
| JavaScript's logical operators && and \|\| serve dual purposes as both logical operators and control-flow mechanisms, returning values based on truthiness rather than just boolean outcomes. | "## **\|\| and && are control-flow operators** We've seen the ternary operator: It is a _control-flow_ operator, not a logical operator. The same is true of && and \|\|. Consider this..." | `normalized:L2289-L2299` | [Source](../sources/js-allonge.md) |
| The ternary operator and logical operators && and \|\| are classified as control-flow operators because they can alter the execution path of a program based on evaluation results. | "JavaScript inherited an operator from the C family of languages, the _ternary_ operator. It's the only operator that takes _three_ arguments. It looks like this: first ? second : third. It..." | `normalized:L2209-L2217` | [Source](../sources/js-allonge.md) |
| The ternary operator and logical operators && and \|\| are classified as control-flow operators because they can alter the execution path of a program based on evaluation results. | "## **\|\| and && are control-flow operators** We've seen the ternary operator: It is a _control-flow_ operator, not a logical operator. The same is true of && and \|\|. Consider this..." | `normalized:L2289-L2299` | [Source](../sources/js-allonge.md) |
| The ternary operator and logical operators && and \|\| are classified as control-flow operators because they can alter the execution path of a program based on evaluation results. | "In contrast to the behaviour of the ternary operator, \|\|, and &&, function parameters are always : _eagerly evaluated_" | `normalized:L2315-L2315` | [Source](../sources/js-allonge.md) |
| The ternary operator and logical operators && and \|\| are classified as control-flow operators because they can alter the execution path of a program based on evaluation results. | "If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and, but to demonstrate the technique: 76 Picking..." | `normalized:L2327-L2333` | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding control flow is essential for writing dynamic and responsive code. It allows developers to make decisions, repeat actions, and manage program execution paths effectively, especially when dealing with complex logic involving truthiness and operator behavior.

## Related pages

- [Arrays](../concepts/arrays.md)
- [Data Types](../concepts/data-types.md)
- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
