---
page_id: javascriptallonge-commas
page_kind: source
summary: commas from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.33-33
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument.

## Key supported claims

- The comma operator evaluates two expressions and returns the value of the second. (raw/javascriptallonge.pdf p.33-33)
- The comma operator is useful for side-effect operations. (raw/javascriptallonge.pdf p.33-33)
- The comma operator can be used in function expressions. (raw/javascriptallonge.pdf p.33-33)

## Technical details

### `technical-atom-41bdeebe23d314dc` code

Citation: (raw/javascriptallonge.pdf p.33)

```javascript
//=> 2 (1 + 1, 2 + 2)
```

### `technical-atom-346ed18993a44cfc` code

Citation: (raw/javascriptallonge.pdf p.33)

```javascript
(() => (1 + 1, 2 + 2))() //=> 4
```

### `technical-atom-d0f583e178e95918` code

Citation: (raw/javascriptallonge.pdf p.33)

```javascript
() => (1 + 1, 2 + 2)
```

### `technical-atom-cf1b8b8f03cb1b27` exception

Citation: (raw/javascriptallonge.pdf p.33)

In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks.

## Related technical details

### From [[javascriptallonge-back-on-the-block]]: `technical-atom-3b19860d1c8e63e0` exception

Relation: nearby source page; matched terms `can`, `comma`, `does`, `operator`

Citation: (raw/javascriptallonge.pdf p.35-37)

As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:

### From [[javascriptallonge-undefined]]: `technical-atom-6727b9042bd2575a` requirement

Relation: nearby source page; matched terms `can`, `javascript`, `most`

Citation: (raw/javascriptallonge.pdf p.34-35)

This works because JavaScript has a feature that can infer where the semi-colons should be most of the time.
