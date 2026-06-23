---
page_id: javascriptallonge-mapping
page_kind: source
summary: mapping from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.113-114
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter covers the concept of mapping in JavaScript, demonstrating how to apply a function to every element of an array using linear recursion.

## Key supported claims

- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again (raw/javascriptallonge.pdf p.113-114).
- Wecanwrite it out using a ternary operator (raw/javascriptallonge.pdf p.113-114).
- [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25] mapWith((x) => !!x, [ null , true , 25, false , "foo"]) //=> [false,true,true,false,true] (raw/javascriptallonge.pdf p.113-114).

## Technical details

### `technical-atom-cfcc6305d51418bd` code

Citation: (raw/javascriptallonge.pdf p.113-114)

```javascript
const squareAll = ([first, ...rest]) => first === undefined ? [] : [first * first, ...squareAll(rest)\ ]; squareAll([1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### `technical-atom-43485b5f1b079b2f` code

Citation: (raw/javascriptallonge.pdf p.113-114)

```javascript
const truthyAll = ([first, ...rest]) => first === undefined ? [] : [!!first, ...truthyAll(rest)]; truthyAll([ null , true , 25, false , "foo"]) //=> [false,true,true,false,true]
```

### `technical-atom-1625e1d73a0a819a` code

Citation: (raw/javascriptallonge.pdf p.113-114)

```javascript
const mapWith = (fn, array) => // ...
```

### `technical-atom-3d8deefb3a868377` code

Citation: (raw/javascriptallonge.pdf p.113-114)

```javascript
const mapWith = (fn, [first, ...rest]) => first === undefined ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25] mapWith((x) => !!x, [ null , true , 25, false , "foo"]) //=> [false,true,true,false,true]
```
