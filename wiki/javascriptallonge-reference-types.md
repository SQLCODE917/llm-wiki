---
page_id: javascriptallonge-reference-types
page_kind: source
summary: reference types from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.22-23
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses reference types in JavaScript, particularly arrays, and how they are not identical even when they have the same contents.

## Key supported claims

- This is an expression, and you can combine [] with other expressions (raw/javascriptallonge.pdf p.22-23).
- When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] (raw/javascriptallonge.pdf p.22-23).
- An array looks like this: [1, 2, 3] (raw/javascriptallonge.pdf p.22-23).

## Technical details

### `technical-atom-7e575d3c8c40b76b` code

Citation: (raw/javascriptallonge.pdf p.22-23)

```
[2-1, 2, 2+1] [1, 1+1, 1+1+1]
```

### `technical-atom-0e9f8149ade6173c` code

Citation: (raw/javascriptallonge.pdf p.22-23)

```
[2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3]
```

### `technical-atom-d255ca48e1a9dd4f` requirement

Citation: (raw/javascriptallonge.pdf p.22-23)

Notice that you are always generating arrays with the same contents.
