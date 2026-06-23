---
page_id: javascriptallonge-nested-blocks
page_kind: source
summary: nested blocks from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.54-55
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on nested blocks in JavaScript Allongé, covering blocks in if statements and their usage in functional programming.

## Key supported claims

- Up to now, we've only ever seen blocks we use as the body of functions (raw/javascriptallonge.pdf p.54-55).
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks (raw/javascriptallonge.pdf p.54-55).
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it (raw/javascriptallonge.pdf p.54-55).
- One of the places you can find blocks is in an if statement (raw/javascriptallonge.pdf p.54-55).
- But there are other kinds of blocks (raw/javascriptallonge.pdf p.54-55).

## Technical details

### `technical-atom-09ccaceb5bc7cd73` code

Citation: (raw/javascriptallonge.pdf p.54-55)

```javascript
(n) => { const even = (x) => { if (x === 0) return true ; else return !even(x - 1); } return even(n) }
```

### `technical-atom-007edf26eb90ab84` code

Citation: (raw/javascriptallonge.pdf p.54-55)

```javascript
((n) => { const even = (x) => { if (x === 0) return true ; else return !even(x - 1); } return even(n) })(13) //=> false
```

### `technical-atom-a083b4343b00d8e8` code

Citation: (raw/javascriptallonge.pdf p.54-55)

```javascript
(n) => { const even = (x) => { if (x === 0) return true ; else { const odd = (y) => !even(y); return odd(x - 1); }
```

### `technical-atom-bade1ca671b07904` code

Citation: (raw/javascriptallonge.pdf p.54-55)

```javascript
} return even(n) } And this also works: ((n) => { const even = (x) => { if (x === 0) return true ; else { const odd = (y) => !even(y); return odd(x - 1); } } return even(n) })(42)
```

### `technical-atom-a424feb387459e07` code

Citation: (raw/javascriptallonge.pdf p.54-55)

```javascript
//=> true
```

### `technical-atom-0ce343f9fe4529d1` exception

Citation: (raw/javascriptallonge.pdf p.54-55)

Up to now, we've only ever seen blocks we use as the body of functions.
