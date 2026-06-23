---
page_id: javascriptallonge-undefined
page_kind: source
summary: undefined from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.34-35
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter from JavaScript Allongé discusses the concept of undefined in JavaScript, its identity, and its differences from SQL NULL.

## Key supported claims

- In JavaScript, the absence of a value is written undefined, and it means there is no value. (raw/javascriptallonge.pdf p.34-35)
- You might think that undefined in JavaScript is equivalent to NULL in SQL. No. In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. In JavaScript, every undefined is identical to every other undefined. (raw/javascriptallonge.pdf p.34-35)
- No matter how you evaluate undefined, you get an identical value back. (raw/javascriptallonge.pdf p.34-35)
- Like numbers, booleans and strings, JavaScript can print out the value undefined. (raw/javascriptallonge.pdf p.34-35)
- In JavaScript, every undefined is identical to every other undefined. (raw/javascriptallonge.pdf p.34-35)

## Technical details

### `technical-atom-21ab65a3528e24be` code

Citation: (raw/javascriptallonge.pdf p.34-35)

```
undefined
```

### `technical-atom-0046548e28e552b5` code

Citation: (raw/javascriptallonge.pdf p.34-35)

```javascript
//=> undefined
```

### `technical-atom-868845583c49b0d4` code

Citation: (raw/javascriptallonge.pdf p.34-35)

```javascript
undefined === undefined //=> true (() => {})() === (() => {})() //=> true (() => {})() === undefined //=> true
```

### `technical-atom-6824a3dcc31f6880` exception

Citation: (raw/javascriptallonge.pdf p.34-35)

18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons.

### `technical-atom-6727b9042bd2575a` requirement

Citation: (raw/javascriptallonge.pdf p.34-35)

This works because JavaScript has a feature that can infer where the semi-colons should be most of the time.
