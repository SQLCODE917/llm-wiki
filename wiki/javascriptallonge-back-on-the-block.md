---
page_id: javascriptallonge-back-on-the-block
page_kind: source
summary: back on the block from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.35-37
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on functions, blocks, and return statements in JavaScript, discussing how functions return the result of evaluating a block, and that a block is a (possibly empty) list of JavaScript statements separated by semicolons.

## Key supported claims

- We said that the function returns the result of evaluating a block, and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. (raw/javascriptallonge.pdf p.35-37)
- Back to our function. (raw/javascriptallonge.pdf p.35-37)
- As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined. (raw/javascriptallonge.pdf p.35-37)

## Technical details

### `technical-atom-d174442845196315` code

Citation: (raw/javascriptallonge.pdf p.35-37)

```javascript
(() => {})() //=> undefined
```

### `technical-atom-7b2196d9ee9dfcf2` code

Citation: (raw/javascriptallonge.pdf p.35-37)

```javascript
() => { 2 + 2 } () => { 1 + 1; 2 + 2 }
```

### `technical-atom-8680beb89d602598` code

Citation: (raw/javascriptallonge.pdf p.35-37)

```javascript
() => { 1 + 1; 2 + 2 }
```

### `technical-atom-8791ab1ce9e62d63` code

Citation: (raw/javascriptallonge.pdf p.35-37)

```javascript
(() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined
```

### `technical-atom-9d239f08d143e7ce` code

Citation: (raw/javascriptallonge.pdf p.35-37)

```javascript
(() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined
```

### `technical-atom-222f45d93107ecf5` code

Citation: (raw/javascriptallonge.pdf p.35-37)

```javascript
(() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World'
```

### `technical-atom-48745cf48481351c` code

Citation: (raw/javascriptallonge.pdf p.35-37)

```javascript
(() => { 1 + 1; return 2 + 2 })() //=> 4
```

### `technical-atom-3b19860d1c8e63e0` exception

Citation: (raw/javascriptallonge.pdf p.35-37)

As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:
