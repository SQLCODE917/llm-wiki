---
title: Closures
type: concept
tags: []
status: draft
last_updated: 2026-05-06
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1275
  - js-allonge:normalized:L1309
  - js-allonge:normalized:L1703
  - js-allonge:normalized:L1740
  - js-allonge:normalized:L1756
  - js-allonge:normalized:L1756
  - js-allonge:normalized:L1775
  - js-allonge:normalized:L1807
  - js-allonge:normalized:L5090
  - js-allonge:normalized:L9473
---

# Closures

A closure is a function that captures and retains access to variables from its outer (enclosing) scope, even after the outer function has finished executing.

## Source-backed details

| Claim | Evidence | Locator | Source |
| ----- | -------- | ------- | ------ |
| A closure is defined by capturing outer scope variables. | "Functions containing one or more free variables are called closures." | `normalized:L1275` | [JavaScript Allongé](../sources/js-allonge.md) |
| When a function is invoked, it maintains a reference to its parent environment. | "the function (y) => x is within (x) => ...'s body. So whenever a function is applied to arguments," | `normalized:L1309` | [JavaScript Allongé](../sources/js-allonge.md) |
| Constants bind values using lexical scope, similar to parameters. | "Yes. Binding values to names with const works just like binding values to names with parameter" | `normalized:L1703` | [JavaScript Allongé](../sources/js-allonge.md) |
| Expressions can access bound values from the nearest parent environment. | "And we can see that our diameter * PI expression uses the binding for PI in the closest parent" | `normalized:L1740` | [JavaScript Allongé](../sources/js-allonge.md) |
| Inner variable bindings can override outer ones. | "We say that when we bind a variable using a parameter inside another binding, the inner binding" | `normalized:L1756` | [JavaScript Allongé](../sources/js-allonge.md) |
| Constants also shadow outer bindings in the same way as parameters. | "Yes, names bound with const shadow enclosing bindings just like parameters." | `normalized:L1775` | [JavaScript Allongé](../sources/js-allonge.md) |
| Block-level bindings can shadow function-level bindings. | "Ah! const statements don't just shadow values bound within the environments created by functions," | `normalized:L1807` | [JavaScript Allongé](../sources/js-allonge.md) |
| Variables accessed by closures retain their values at the time of closure creation. | "is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the" | `normalized:L5090` | [JavaScript Allongé](../sources/js-allonge.md) |
| Closures enable stateful behavior through encapsulation. | "Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function" | `normalized:L9473` | [JavaScript Allongé](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)