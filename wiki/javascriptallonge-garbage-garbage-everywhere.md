---
page_id: javascriptallonge-garbage-garbage-everywhere
page_kind: source
summary: Garbage, Garbage Everywhere from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.126-131
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on garbage collection and memory efficiency in JavaScript, focusing on array operations and linked lists.

## Key supported claims

- Tail calls can optimize space complexity in recursion, but array operations still create temporary arrays that slow performance (raw/javascriptallonge.pdf p.126-131).
- JavaScript engines copy elements from prepend into new arrays one at a time, causing performance issues (raw/javascriptallonge.pdf p.126-131).
- Although maximum memory usage doesn't grow, thrashing from creating short-lived arrays is very bad (raw/javascriptallonge.pdf p.126-131).

## Technical details

### `technical-atom-62490a3bbc959661` code

Citation: (raw/javascriptallonge.pdf p.126-131)

```javascript
const mapWith = (fn, [first, ...rest], prepend = []) => first === undefined
```

### `technical-atom-4932e72b63b0cca4` code

Citation: (raw/javascriptallonge.pdf p.126-131)

```javascript
const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
```

### `technical-atom-717620cb945b2f2b` code

Citation: (raw/javascriptallonge.pdf p.126-131)

```javascript
const oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, null)))));
```

### `technical-atom-3978516b212d960e` code

Citation: (raw/javascriptallonge.pdf p.126-131)

```javascript
const node5 = [5, null], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2];
```

### `technical-atom-8afbe5215498425b` code

Citation: (raw/javascriptallonge.pdf p.126-131)

```javascript
const oneToFive = node1;
```

### `technical-atom-a24d087be687a36f` procedure

Citation: (raw/javascriptallonge.pdf p.126-131)

To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith.

### `technical-atom-e1f6f1e8503dc617` procedure

Citation: (raw/javascriptallonge.pdf p.126-131)

Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend.

### `technical-atom-4551df707589c382` exception

Citation: (raw/javascriptallonge.pdf p.126-131)

Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

## Related technical details

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-b4bbdc6766be3fad` code

Relation: nearby source page; matched terms `but`, `calls`, `can`, `function`, `javascript`, `tail`

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
There are three places it returns. The first two don’t return anything, they don’t matter. But the third is fn.apply(this, args). This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. It isn’t going to do any more work, so it can throw its existing stack frame away.
```

### From [[javascriptallonge-self-similarity]]: `technical-atom-940ab647a8cf16dd` code

Relation: nearby source page; matched terms `array`, `arrays`, `but`, `very`

Citation: (raw/javascriptallonge.pdf p.109-116)

```javascript
> 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. A more robust implementation would be (array) => array.length === 0, but we are doing backflips to keep this within a very small and contrived playground.
```

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-ff6f64bd417071bb` code

Relation: nearby source page; matched terms `calls`, `function`, `tail`

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
const mapWith = function (fn, [first, ...rest]) { if (first === undefined) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; return _temp3; } }
```

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-9465e3814b7a9872` code

Relation: nearby source page; matched terms `calls`, `function`, `tail`

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
A “tail-call” occurs when a function’s last act is to invoke another function, and then return whatever the other function returns. For example, consider the maybe function decorator:
```
