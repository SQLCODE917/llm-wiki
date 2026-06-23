---
page_id: javascriptallonge-call-by-sharing
page_kind: source
summary: call by sharing from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.42-43
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScriptAllonge discusses call by sharing semantics, where JavaScript passes references as arguments, making it a specialization of call by value.

## Key supported claims

- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement 'call by sharing' semantics (raw/javascriptallonge.pdf p.42-43).
- Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types (raw/javascriptallonge.pdf p.42-43).
- When we combine our knowledge of value types, reference types, arguments, and closures, we'll understand why this function always evaluates to true no matter what argument you apply it to: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (raw/javascriptallonge.pdf p.42-43).
- Unless the argument is NaN, which isn't equal to anything, including itself (raw/javascriptallonge.pdf p.42-43).

## Technical details

### `technical-atom-f1c3de428c370aaf` code

Citation: (raw/javascriptallonge.pdf p.42-43)

```javascript
(value) => ((ref1, ref2) => ref1 === ref2)(value, value)
```

### `technical-atom-247ce19e93a86869` requirement

Citation: (raw/javascriptallonge.pdf p.42-43)

There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original.

### `technical-atom-9aa4fc764ee229f5` exception

Citation: (raw/javascriptallonge.pdf p.42-43)

JavaScript does not place copies of reference values in any environment.

### `technical-atom-e8199c3947c572cb` requirement

Citation: (raw/javascriptallonge.pdf p.42-43)

When we combine our knowledge of value types, reference types, arguments, and closures, we'll understand why this function always evaluates to true no matter what argument 26 you apply it to:

### `technical-atom-249c83fa8c40d177` exception

Citation: (raw/javascriptallonge.pdf p.42-43)

26 Unless the argument is NaN , which isn't equal to anything, including itself .
