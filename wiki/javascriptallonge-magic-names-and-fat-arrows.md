---
page_id: javascriptallonge-magic-names-and-fat-arrows
page_kind: source
summary: Summary of the magic names this and arguments in fat arrow functions.
sources: raw/javascriptallonge.pdf p.75-77
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé – A modular guide to JavaScript fundamentals and advanced techniques.

## Key supported claims

- The magic names this and arguments have a different behaviour when you invoke a function that was defined with a fat arrow: Instead of being bound when the function is invoked, the fat arrow function always acquires the bindings for this and arguments from its enclosing scope, just like any other binding. (raw/javascriptallonge.pdf p.75-77)
- Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax. (raw/javascriptallonge.pdf p.75-77)
- 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword: (raw/javascriptallonge.pdf p.75-77)
- 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. (raw/javascriptallonge.pdf p.75-77)
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. (raw/javascriptallonge.pdf p.75-77)
