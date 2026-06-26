---
page_id: javascriptallonge-arrays-and-destructuring-arguments
page_kind: source
summary: Arrays and Destructuring Arguments from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.101-108
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Arrays are JavaScript’s “native” representation of lists. JavaScript has a literal syntax for creating an array using square brackets. Array elements can be extracted using bracket notation. Destructuring is a feature for extracting elements from arrays, and gathering allows extracting the head and gathering the rest of an array. Destructuring also works with function parameters, enabling rest parameters.

## Key supported claims

- Arrays are JavaScript’s native representation of lists (raw/javascriptallonge.pdf p.101-108).
- JavaScript has a literal syntax for creating an array using square brackets (raw/javascriptallonge.pdf p.101-108).
- Array elements can be extracted using bracket notation (raw/javascriptallonge.pdf p.101-108).

## Technical details

### `technical-atom-91982e5004e6c9d4` code

Citation: (raw/javascriptallonge.pdf p.101-108)

```javascript
const wrap = (something) => [something];
```

### `technical-atom-5764649a84cab695` code

Citation: (raw/javascriptallonge.pdf p.101-108)

```javascript
[] === [] //=> false [2 + 2] === [2 + 2] //=> false
```

### `technical-atom-e2319f942ab21160` code

Citation: (raw/javascriptallonge.pdf p.101-108)

```javascript
const array_of_one = () => [1];
```

### `technical-atom-ce2f44952fa2ff45` code

Citation: (raw/javascriptallonge.pdf p.101-108)

```javascript
array_of_one() === array_of_one() //=> false
```

### `technical-atom-bf99f948ff811b64` code

Citation: (raw/javascriptallonge.pdf p.101-108)

```javascript
const oneTwoThree = ["one", "two", "three"];
```

### `technical-atom-b7911edd79cd83e5` code

Citation: (raw/javascriptallonge.pdf p.101-108)

```javascript
const x = [], a = [x];
```

### `technical-atom-da49792110b151a4` code

Citation: (raw/javascriptallonge.pdf p.101-108)

```javascript
const wrap = (something) => { const wrapped = [something];
```

### `technical-atom-e87a6882969bf21b` code

Citation: (raw/javascriptallonge.pdf p.101-108)

```
return wrapped; }
```

## Related technical details

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-b4bbdc6766be3fad` code

Relation: nearby source page; matched terms `arguments`, `can`, `function`, `javascript`

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
There are three places it returns. The first two don’t return anything, they don’t matter. But the third is fn.apply(this, args). This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. It isn’t going to do any more work, so it can throw its existing stack frame away.
```

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-ff6f64bd417071bb` code

Relation: nearby source page; matched terms `arguments`, `function`, `rest`

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
const mapWith = function (fn, [first, ...rest]) { if (first === undefined) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; return _temp3; } }
```

### From [[javascriptallonge-garbage-garbage-everywhere]]: `technical-atom-4551df707589c382` exception

Relation: nearby source page; matched terms `array`, `arrays`, `elements`, `one`

Citation: (raw/javascriptallonge.pdf p.126-131)

Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

### From [[javascriptallonge-garbage-garbage-everywhere]]: `technical-atom-e1f6f1e8503dc617` procedure

Relation: nearby source page; matched terms `array`, `creating`, `elements`

Citation: (raw/javascriptallonge.pdf p.126-131)

Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend.
