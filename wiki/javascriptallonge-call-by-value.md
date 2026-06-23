---
page_id: javascriptallonge-call-by-value
page_kind: source
summary: call by value from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.40-41
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé discusses the call by value evaluation strategy in JavaScript, where expressions are evaluated before functions are applied, and provides an example with the expression 1 + 1 being evaluated to 2 before being applied to a function.

## Key supported claims

- JavaScript uses the 'call by value' evaluation strategy, where expressions are evaluated before functions are applied (raw/javascriptallonge.pdf p.40-41).
- In the example ((diameter) => diameter * 3.14159265)(1 + 1), the expression 1 + 1 is evaluated first to 2, then applied to the function (raw/javascriptallonge.pdf p.40-41).
- While JavaScript always calls by value, the notion of a 'value' has additional subtlety, which will be discussed later (raw/javascriptallonge.pdf p.40-41).

## Technical details

### `technical-atom-fbf27e4e62b010d5` code

Citation: (raw/javascriptallonge.pdf p.40-41)

```javascript
((diameter) => diameter * 3.14159265)(1 + 1) //=> 6.2831853
```

### `technical-atom-3041c6b290ab5fda` procedure

Citation: (raw/javascriptallonge.pdf p.40-41)

What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 .

### `technical-atom-9b063541184a3c8d` procedure

Citation: (raw/javascriptallonge.pdf p.40-41)

Then our circumference function was applied to 2 .

### `technical-atom-93ef10ee5b523433` requirement

Citation: (raw/javascriptallonge.pdf p.40-41)

We'll see below that while JavaScript always calls by value, the notion of a 'value' has additional subtlety.
