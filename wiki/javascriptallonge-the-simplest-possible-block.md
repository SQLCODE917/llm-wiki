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
