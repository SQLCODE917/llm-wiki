---
page_id: as-little-as-possible-about-functions-but-no-less
page_kind: source
summary: Chapter covering basic JavaScript functions, their evaluation, and fundamentals of function application.
sources: raw/javascriptallonge.pdf p.30-43
updated: 2026-06-19
---

## As Little As Possible About Functions, But No Less

This chapter introduces JavaScript functions as values, emphasizing their role in computation. It covers the basics of function creation, application, and evaluation, including functions that return values, expressions, and other functions. The chapter also discusses identity of functions, the comma operator, blocks, and the return statement. Additionally, it touches upon call by value and call by sharing semantics in JavaScript.

Key concepts include:
- Functions as values
- Function application and evaluation
- Identity of functions (reference types)
- Return statements and blocks
- Call by value and call by sharing

## Functions as Values

In JavaScript, functions are values. The simplest function is `() => 0`, which takes no arguments and returns 0. Functions are reference types, meaning each evaluation of a function expression produces a new, non-identical function.

## Function Application

Functions are applied to zero or more arguments using parentheses. For example, `(() => 0)()` applies the function `() => 0` to no arguments, returning 0.

## Return Statements and Blocks

Functions can return values using the `return` keyword. Blocks in functions evaluate to `undefined` unless a `return` statement is used. A function that returns a function can be written as `() => () => 0`.

## Call by Value and Call by Sharing

JavaScript uses a call by value evaluation strategy, but with a twist: it implements call by sharing for reference types. This means that while value types are copied when passed to functions, reference types are passed by reference.

## Variables and Bindings

When functions are invoked, a new environment is created. Arguments are bound to names in this environment, and variables are resolved by looking up their values in the environment.
