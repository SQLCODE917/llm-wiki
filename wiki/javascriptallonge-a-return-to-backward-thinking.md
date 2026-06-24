---
page_id: javascriptallonge-a-return-to-backward-thinking
page_kind: source
summary: a return to backward thinking from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.189-190
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on backward thinking in JavaScript allonge, discussing pairs and lists, and how implementation details can be hidden using functional patterns.

## Key supported claims

- To make pairs work, we did things backwards, we passed the first and rest functions to the pair, and the pair called our function (raw/javascriptallonge.pdf p.189-190).
- But we could have done something completely different; we could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO (raw/javascriptallonge.pdf p.189-190).
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO (raw/javascriptallonge.pdf p.189-190).

## Technical details

### `technical-atom-73474c33e6da544f` code

Citation: (raw/javascriptallonge.pdf p.189-190)

```javascript
const first = K, second = K(I), pair = (first) => (second) => { const pojo = {first, second}; return (selector) => selector(pojo.first)(pojo.second); }; const latin = pair("primus")("secundus"); latin(first) //=> "primus" latin(second) //=> "secundus"
```

### `technical-atom-2293d28cd2f82e8a` code

Citation: (raw/javascriptallonge.pdf p.189-190)

```javascript
const length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) );
```

### `technical-atom-67256d6ad598a7e1` code

Citation: (raw/javascriptallonge.pdf p.189-190)

```javascript
const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);
```

### `technical-atom-38a0d6a5974cfdca` procedure

Citation: (raw/javascriptallonge.pdf p.189-190)

We then ask list to do it, and provide a way for list to call the code we pass in.

### `technical-atom-e2b2c0d8e3d358fe` requirement

Citation: (raw/javascriptallonge.pdf p.189-190)

It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both.

## Related technical details

### From [[javascriptallonge-lists-with-functions-as-data]]: `technical-atom-1facdd66430f4b84` code

Relation: nearby source page; matched terms `can`, `first`, `functions`, `lists`, `pair`, `rest`

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
const length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair)); length(l123) //=> 3 const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(rest(aPair), pair(first(aPair), delayed)); const mapWith = (fn, aPair, delayed = EMPTY) => aPair === EMPTY ? reverse(delayed) : mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed)); const doubled = mapWith((x) => x * 2, l123); first(doubled) //=> 2 first(rest(doubled)) //=> 4 first(rest(rest(doubled))) //=> 6 Can we do the same with the linked lists we build out of functions? Yes: const first = K, l123 = pair(1)(pair(2)(pair(3)(EMPTY)));
```

### From [[javascriptallonge-lists-with-functions-as-data]]: `technical-atom-7fbeb05554d21b25` code

Relation: nearby source page; matched terms `first`, `functions`, `lists`, `pair`, `rest`

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
const first = ({first, rest}) => first, rest = ({first, rest}) => rest, pair = (first, rest) => ({first, rest}), EMPTY = ({}); const l123 = pair(1, pair(2, pair(3, EMPTY))); first(l123) //=> 1 first(rest(l123)) //=> 2 first(rest(rest(l123))) //=3
```

### From [[javascriptallonge-lists-with-functions-as-data]]: `technical-atom-21a61344f2e84d80` code

Relation: nearby source page; matched terms `backwards`, `but`, `first`, `functions`, `how`, `lists`

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
//=> 2 return l123(rest)(rest)(first) //=> 3 We write them in a backwards way, but they seem to work. How about
```

### From [[javascriptallonge-lists-with-functions-as-data]]: `technical-atom-b43850c16ef07986` code

Relation: nearby source page; matched terms `first`, `functions`, `lists`, `pair`, `rest`

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
rest = K(I), pair = V, EMPTY = (() => {}); const l123(first) //=> 1 l123(rest)(first)
```
