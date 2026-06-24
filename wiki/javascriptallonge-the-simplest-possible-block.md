---
page_id: javascriptallonge-the-simplest-possible-block
page_kind: source
summary: the simplest possible block from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.34-34
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

A block has zero or more statements, separated by semicolons.

## Key supported claims

- A block has zero or more statements, separated by semicolons. (raw/javascriptallonge.pdf p.34-34)
- A block returns the result of evaluating a block that has no statements. (raw/javascriptallonge.pdf p.34-34)
- There is another thing we can put to the right of an arrow, a block. (raw/javascriptallonge.pdf p.34-34)

## Technical details

### `technical-atom-b29e6537d7ceea35` code

Citation: (raw/javascriptallonge.pdf p.34)

```javascript
() => {}
```

### `technical-atom-ce22cfd98797d1dc` code

Citation: (raw/javascriptallonge.pdf p.34)

```javascript
(() => {})() //=> undefined
```

## Related technical details

### From [[javascriptallonge-undefined]]: `technical-atom-6824a3dcc31f6880` exception

Relation: nearby source page; matched terms `has`, `separated`, `statements`

Citation: (raw/javascriptallonge.pdf p.34-35)

18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons.

### From [[javascriptallonge-back-on-the-block]]: `technical-atom-3b19860d1c8e63e0` exception

Relation: nearby source page; matched terms `block`, `can`, `more`

Citation: (raw/javascriptallonge.pdf p.35-37)

As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:
