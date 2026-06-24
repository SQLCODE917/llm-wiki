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

### `technical-atom-e8199c3947c572cb` requirement

Citation: (raw/javascriptallonge.pdf p.42-43)

When we combine our knowledge of value types, reference types, arguments, and closures, we'll understand why this function always evaluates to true no matter what argument 26 you apply it to:

### `technical-atom-9aa4fc764ee229f5` exception

Citation: (raw/javascriptallonge.pdf p.42-43)

JavaScript does not place copies of reference values in any environment.

### `technical-atom-249c83fa8c40d177` exception

Citation: (raw/javascriptallonge.pdf p.42-43)

26 Unless the argument is NaN , which isn't equal to anything, including itself .

## Related technical details

### From [[javascriptallonge-ah-i-d-like-to-have-an-argument-please-22]]: `technical-atom-dd665ae074e9887f` exception

Relation: nearby source page; matched terms `argument`, `our`, `said`, `what`

Citation: (raw/javascriptallonge.pdf p.39-40)

We haven't even said what an argument is , only that our functions don't have any.

### From [[javascriptallonge-closures-and-scope]]: `technical-atom-6e3151115dfb385f` procedure

Relation: nearby source page; matched terms `apply`, `argument`, `closures`, `function`, `value`

Citation: (raw/javascriptallonge.pdf p.44)

Then we're going to take the value of that function and apply it to the argument 2 , something like this:

### From [[javascriptallonge-call-by-value]]: `technical-atom-9b063541184a3c8d` procedure

Relation: nearby source page; matched terms `call`, `function`, `our`, `value`

Citation: (raw/javascriptallonge.pdf p.40-41)

Then our circumference function was applied to 2 .

### From [[javascriptallonge-closures-and-scope]]: `technical-atom-ab8524c9d5fcc7c0` code

Relation: nearby source page; matched terms `closures`, `function`, `value`

Citation: (raw/javascriptallonge.pdf p.44)

```
becomes {x: 1, ...} , and the result of applying the function is another function value.
```
