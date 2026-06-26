---
page_id: javascriptallonge-self-similarity
page_kind: source
summary: Self-Similarity from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.109-116
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter explores self-similarity in JavaScript through recursion, focusing on lists, linear recursion, mapping, and folding.

## Key supported claims

- Recursion is the root of computation since it trades description for time (Alan Perlis) (raw/javascriptallonge.pdf p.109-116).
- Lists can be defined as either empty or as an element concatenated with a list (raw/javascriptallonge.pdf p.109-116).
- Linear recursion follows a divide and conquer strategy, breaking problems into smaller subproblems (raw/javascriptallonge.pdf p.109-116).
- Mapping is a special case of linear recursion where a function is applied to each element of a list (raw/javascriptallonge.pdf p.109-116).
- Folding is a generalization of mapping that can be used to build other functions like length and sumSquares (raw/javascriptallonge.pdf p.109-116).

## Technical details

### `technical-atom-1bcaa516e0bb0550` code

Citation: (raw/javascriptallonge.pdf p.109-116)

```javascript
const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar"]; first //=> "foo" rest //=> ["bar"] const [first, ...rest] = ["foo", "bar", "baz"]; first //=> "foo" rest //=> ["bar","baz"]
```

### `technical-atom-bbbbff6925562544` code

Citation: (raw/javascriptallonge.pdf p.109-116)

```javascript
const isEmpty = ([first, ...rest]) => first === undefined;
```

### `technical-atom-940ab647a8cf16dd` code

Citation: (raw/javascriptallonge.pdf p.109-116)

```javascript
> 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. A more robust implementation would be (array) => array.length === 0, but we are doing backflips to keep this within a very small and contrived playground.
```

### `technical-atom-fd27f878a437c3c1` code

Citation: (raw/javascriptallonge.pdf p.109-116)

```javascript
const length = ([first, ...rest]) => first === undefined ? 0: // ???
```

### `technical-atom-1c64aa708dce3458` code

Citation: (raw/javascriptallonge.pdf p.109-116)

```javascript
const length = ([first, ...rest]) => first === undefined ? 0: 1 + length(rest);
```

### `technical-atom-644dfa73efff0a53` code

Citation: (raw/javascriptallonge.pdf p.109-116)

```javascript
const flatten = ([first, ...rest]) => { if (first === undefined) { return []; } else if (!Array.isArray(first)) { return [first, ...flatten(rest)]; } else { return [...flatten(first), ...flatten(rest)]; } } flatten(["foo", [3, 4, []]]) //=> ["foo",3,4]
```

### `technical-atom-8ee63caa56f79969` code

Citation: (raw/javascriptallonge.pdf p.109-116)

```javascript
const squareAll = ([first, ...rest]) => first === undefined ? []: [first * first, ...squareAll(rest)]; squareAll([1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### `technical-atom-fbaa6ef02dce0699` code

Citation: (raw/javascriptallonge.pdf p.109-116)

```javascript
const truthyAll = ([first, ...rest]) => first === undefined
```

## Related technical details

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-ff6f64bd417071bb` code

Relation: nearby source page; matched terms `const`, `first`, `function`, `rest`, `return`

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
const mapWith = function (fn, [first, ...rest]) { if (first === undefined) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; return _temp3; } }
```

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-616779e4e28069eb` code

Relation: nearby source page; matched terms `const`, `first`, `rest`

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
const mapWith = (fn, [first, ...rest]) => first === undefined ? []: [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-8f8f661f7109191c` code

Relation: nearby source page; matched terms `const`, `first`, `rest`

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined
```

### From [[javascriptallonge-garbage-garbage-everywhere]]: `technical-atom-62490a3bbc959661` code

Relation: nearby source page; matched terms `const`, `first`, `rest`

Citation: (raw/javascriptallonge.pdf p.126-131)

```javascript
const mapWith = (fn, [first, ...rest], prepend = []) => first === undefined
```
