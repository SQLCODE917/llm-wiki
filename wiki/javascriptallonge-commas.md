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
