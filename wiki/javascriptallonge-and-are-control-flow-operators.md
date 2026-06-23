---
page_id: javascriptallonge-and-are-control-flow-operators
page_kind: source
summary: || and && are control-flow operators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.97-98
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses how || and && are control-flow operators in JavaScript, not logical operators.

## Key supported claims

- || and && are control-flow operators, not logical operators, (raw/javascriptallonge.pdf p.97-98).
- The ternary operator is a control-flow operator, not a logical operator, (raw/javascriptallonge.pdf p.97-98).
- Short-circuit evaluation in || and && prevents unnecessary function calls, (raw/javascriptallonge.pdf p.97-98).

## Technical details

### `technical-atom-3f2d84afe339533c` code

Citation: (raw/javascriptallonge.pdf p.97-98)

```javascript
const even = (n) => n === 0 || (n !== 1 && even(n - 2)) even(42) //=> true
```

### `technical-atom-301f0784fd80b93c` worked-example

Citation: (raw/javascriptallonge.pdf p.97-98)

Consider this tail-recursive function that determines whether a positive integer is even:

### `technical-atom-fb78d9847d23a268` code

Citation: (raw/javascriptallonge.pdf p.97-98)

```
If n === 0 , JavaScript does not evaluate (n !== 1 && even(n -2)) .
```

### `technical-atom-2ad64c6ec9af7008` code

Citation: (raw/javascriptallonge.pdf p.97-98)

```
This leads us to evaluate n === 0 || (n !== 1 && even(n - 2)) all over again, and this time we end up evaluating even(-4) .
```

### `technical-atom-2fe0c429c64a6e81` code

Citation: (raw/javascriptallonge.pdf p.97-98)

```
In this case, if n === 0 , JavaScript does not evaluate (n !== 1 && even(n -2)) .
```

### `technical-atom-780f70c903b37283` code

Citation: (raw/javascriptallonge.pdf p.97-98)

```
Likewise, if n === 1 , JavaScript evaluates n !== 1 && even(n -2) as false without ever evaluating even(n 2) .
```

### `technical-atom-3b6397aef7b5b591` requirement

Citation: (raw/javascriptallonge.pdf p.97-98)

The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not.
