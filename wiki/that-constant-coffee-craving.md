---
page_id: that-constant-coffee-craving
page_kind: source
summary: Chapter on naming functions and using const for bindings in JavaScript.
sources: raw/javascriptallonge.pdf p.49-61
updated: 2026-06-19
---

## That Constant Coffee Craving

This chapter explores the concept of naming functions and using the `const` keyword for bindings in JavaScript. It discusses how to bind values to names using function expressions and IIFEs (Immediately Invoked Function Expressions), and how the `const` keyword provides a way to bind names inside blocks without incurring the cost of function invocation.

### Key Concepts

- **Anonymous Functions**: Functions without names, which are common in JavaScript.
- **IIFE (Immediately Invoked Function Expression)**: A pattern where a function is written and immediately invoked with an argument to bind values to names.
- **const Keyword**: A way to bind names inside blocks, providing lexical scoping without function invocation overhead.
- **Lexical Scoping**: The concept that names are looked up in the environment where they are declared, not where they are used.
- **Shadowing**: When a name bound in an inner scope shadows a name in an outer scope, without affecting the outer binding.

### Function Naming and Binding

The chapter starts with a simple example of calculating circumference using anonymous functions, then shows how to bind the value of PI to a name using IIFEs. It demonstrates how to use `const` for binding values inside blocks, which is more efficient than function invocation and provides better readability.

### Lexical Scope and Shadowing

The chapter delves into lexical scoping, showing that `const` bindings work just like parameter bindings in terms of scope. It also explains how `const` variables can shadow outer bindings, demonstrating that the inner binding does not overwrite the outer binding.

### Rebinding

The chapter touches on rebinding, explaining that while parameters can be rebound, names bound with `const` cannot be rebound, which simplifies program analysis.
