---
page_id: javascriptallonge-gathering
page_kind: source
summary: gathering from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.104-105
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on gathering and destructuring in JavaScript Allongé.

## Key supported claims

- Common pattern: extracting head and gathering the rest from an array. (raw/javascriptallonge.pdf p.104-105)
- Variables gathered are conventionally called 'rest', and the ... operation is termed 'gather'. (raw/javascriptallonge.pdf p.104-105)
- The ... notation lacks universal pattern-matching capability. (raw/javascriptallonge.pdf p.104-105)
- Destructuring with ... is termed 'gathering', inserting with ... is termed 'spreading'. (raw/javascriptallonge.pdf p.104-105)

## Technical details

### `technical-atom-b773ae15db47fe0f` code

Citation: (raw/javascriptallonge.pdf p.104-105)

```javascript
const [car, ...cdr] = [1, 2, 3, 4, 5]; car //=> 1 cdr //=> [2, 3, 4, 5]
```

### `technical-atom-fdf4ebc731b1361f` code

Citation: (raw/javascriptallonge.pdf p.104-105)

```javascript
const [...butLast, last] = [1, 2, 3, 4, 5]; //=> ERROR const [first, ..., last] = [1, 2, 3, 4, 5]; //=> ERROR Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. So if const wrapped = [something]; Then: const [unwrapped] = something; What is the reverse of gathering? We know that: const [car, ...cdr] = [1, 2, 3, 4, 5]; What is the reverse? It would be: const cons = [car, ...cdr]; oneTwoThree = ["one", "two", "three"];
```

### `technical-atom-51926a473f13950b` code

Citation: (raw/javascriptallonge.pdf p.104-105)

```javascript
Let's try it: const ["zero", ...oneTwoThree] //=> ["zero","one","two","three"]
```

### `technical-atom-ea3503c1ec9e928d` worked-example

Citation: (raw/javascriptallonge.pdf p.104-105)

operation as a 'gather,' following Kyle Simpson's example.

### `technical-atom-05f0023aaf1356dc` exception

Citation: (raw/javascriptallonge.pdf p.104-105)

notation does not provide a universal patten-matching capability.

### `technical-atom-45a32a91780c66eb` worked-example

Citation: (raw/javascriptallonge.pdf p.104-105)

For example, we cannot write

### `technical-atom-b0bd01550daaf9e2` formula

Citation: (raw/javascriptallonge.pdf p.104-105)

So if const wrapped = [something]; Then: const [unwrapped] = something; What is the reverse of gathering?
