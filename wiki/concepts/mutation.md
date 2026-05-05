---
title: Mutation
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# Mutation

Mutation in JavaScript refers to the ability to modify the internal state of arrays and objects after their creation. This process occurs when values are reassigned or new properties are added, changing the structure of the object or array while maintaining its identity.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| JavaScript arrays and objects can be mutated by reassigning values or adding new properties | "In JavaScript, almost every type of value can mutate. Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one';" | normalized:L4549 | [Source](../sources/js-allonge.md) |
| Mutating a shared value through one binding affects all bindings that reference the same value | "We haven't rebound the inner name to a different variable, we've mutated the value that both bindings share." | normalized:L4614 | [Source](../sources/js-allonge.md) |
| When two variables are aliases for the same array, modifying one affects the other | "Changes made to ThreeToFive affect OneToFive, because they share the same structure." | normalized:L4666 | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding mutation is crucial for predicting program behavior in JavaScript. When multiple variables reference the same array or object, changes made through one reference will be visible through all other references. This can lead to unexpected side effects and bugs if developers are not careful about how they manage shared mutable state. Knowing which operations cause mutation versus which create new values helps in writing more predictable and maintainable code.

## Source pages

- [Source](../sources/js-allonge.md)