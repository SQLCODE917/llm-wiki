---
page_id: javascriptallonge-and-also
page_kind: source
summary: And also: from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.37-38
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses return statements and the distinction between statements and expressions in JavaScript.

## Key supported claims

- The return statement is the first statement we've seen, and it behaves differently than an expression. (raw/javascriptallonge.pdf p.37-38)
- Statements belong inside blocks and only inside blocks. (raw/javascriptallonge.pdf p.37-38)
- For example, you can't use one as the expression in a simple function, because it isn't an expression: (() => return 0)() //=> ERROR (raw/javascriptallonge.pdf p.37-38)

## Technical details

### `technical-atom-3512c9be9f7c9cf4` code

Citation: (raw/javascriptallonge.pdf p.37-38)

```javascript
(() => { return 1 + 1; 2 + 2 })() //=> 2
```

### `technical-atom-df6eb1f9823e475b` code

Citation: (raw/javascriptallonge.pdf p.37-38)

```javascript
(() => return 0)() //=> ERROR
```

### `technical-atom-59883faf926228a6` worked-example

Citation: (raw/javascriptallonge.pdf p.37-38)

For example, you can't use one as the expression in a simple function, because it isn't an expression:

### `technical-atom-82593adf34b86763` exception

Citation: (raw/javascriptallonge.pdf p.37-38)

Statements belong inside blocks and only inside blocks.
