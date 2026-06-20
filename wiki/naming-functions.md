---
page_id: naming-functions
page_kind: source
summary: Summary of the Naming Functions chapter from JavaScript Allongé.
sources: raw/javascriptallonge.pdf p.62-78
updated: 2026-06-19
---

# Naming Functions

This chapter discusses the different ways to name functions in JavaScript, focusing on the `function` keyword versus fat arrow functions, and how naming affects function behavior and debugging.

## Key Concepts

### Function Expressions vs Function Declarations

JavaScript provides two main syntaxes for defining functions:

1. **Fat Arrow Functions**: `(str) => str + str`
2. **Function Keyword**: `function (str) { return str + str }`

### Named Function Expressions

Functions defined with the `function` keyword can be named, creating a "named function expression":

```javascript
const repeat = function repeat(str) { return str + str; };
```

In this case, `repeat` is the binding name in the environment, but `repeat` is also the function's actual name (accessible via `.name` property). This is useful for debugging and stack traces.

### Function Declarations

Function declarations are statements that are hoisted to the top of their scope:

```javascript
function fizzbuzz() {
  return "Fizz" + "Buzz";
}
```

This behaves similarly to a named function expression but has different scoping rules and cannot be used inside blocks.

### Magic Names

Functions defined with the `function` keyword have access to special variables:
- `this`: The function's context
- `arguments`: An array-like object containing all arguments passed to the function

Fat arrow functions inherit `this` and `arguments` from their enclosing scope, making them behave differently in certain contexts.

## Summary

- Functions can be anonymous or named
- Named functions are useful for debugging and recursion
- Function declarations are hoisted and can be used anywhere in a function scope
- The `arguments` object provides access to all function arguments
- Fat arrow functions behave differently with respect to `this` and `arguments`
