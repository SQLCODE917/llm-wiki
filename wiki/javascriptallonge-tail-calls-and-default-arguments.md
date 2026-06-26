---
page_id: javascriptallonge-tail-calls-and-default-arguments
page_kind: source
summary: Tail Calls (and Default Arguments) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.117-125
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on tail calls and default arguments from JavaScript Allongé, covering optimization techniques for recursive functions and the use of default arguments to simplify function calls.

## Key supported claims

- Tail calls optimized by JavaScript engines avoid stack growth (raw/javascriptallonge.pdf p.117-125).
- Non-tail-recursive functions cause memory issues due to stack growth (raw/javascriptallonge.pdf p.117-125).
- Default arguments simplify function calls (raw/javascriptallonge.pdf p.117-125).
- Functions called in tail position allow optimization (raw/javascriptallonge.pdf p.117-125).

## Technical details

### `technical-atom-616779e4e28069eb` code

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
const mapWith = (fn, [first, ...rest]) => first === undefined ? []: [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### `technical-atom-ff6f64bd417071bb` code

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
const mapWith = function (fn, [first, ...rest]) { if (first === undefined) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; return _temp3; } }
```

### `technical-atom-9465e3814b7a9872` code

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
A “tail-call” occurs when a function’s last act is to invoke another function, and then return whatever the other function returns. For example, consider the maybe function decorator:
```

### `technical-atom-19764ec512049c26` code

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
const maybe = (fn) => function (...args) { if (args.length === 0) { return; } else { for ( let arg of args) { if (arg == null) return; } return fn.apply( this, args); } }
```

### `technical-atom-b4bbdc6766be3fad` code

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
There are three places it returns. The first two don’t return anything, they don’t matter. But the third is fn.apply(this, args). This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. It isn’t going to do any more work, so it can throw its existing stack frame away.
```

### `technical-atom-00639a2652e6a8d9` code

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
const length = ([first, ...rest]) => first === undefined ? 0: 1 + length(rest);
```

### `technical-atom-8f8f661f7109191c` code

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined
```

### `technical-atom-5f0992754f41311f` table

Citation: (raw/javascriptallonge.pdf p.98)

|0,|1,|2,|3,|4,|5,|6,|7,|8,|9,|
|---|---|---|---|---|---|---|---|---|---|
|10,|11,|12,|13,|14,|15,|16,|17,|18,|19,|
|20,|21,|22,|23,|24,|25,|26,|27,|28,|29,|
|30,|31,|32,|33,|34,|35,|36,|37,|38,|39,|
|40,|41,|42,|43,|44,|45,|46,|47,|48,|49,|
|50,|51,|52,|53,|54,|55,|56,|57,|58,|59,|
|60,|61,|62,|63,|64,|65,|66,|67,|68,|69,|
|70,|71,|72,|73,|74,|75,|76,|77,|78,|79,|
|80,|81,|82,|83,|84,|85,|86,|87,|88,|89,|
|90,|91,|92,|93,|94,|95,|96,|97,|98,|99,|

## Related technical details

### From [[javascriptallonge-plain-old-javascript-objects]]: `technical-atom-d6ba7e5f33c9f02b` code

Relation: nearby source page; matched terms `allong`, `javascript`

Citation: (raw/javascriptallonge.pdf p.132-140)

```javascript
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### From [[javascriptallonge-left-variadic-functions]]: `technical-atom-a1826ad5eefcc067` code

Relation: nearby source page; matched terms `arguments`, `call`, `function`, `functions`

Citation: (raw/javascriptallonge.pdf p.89-93)

```javascript
function rightVariadic (fn) { if (fn.length < 1) return fn; return function () { var ordinaryArgs = (1 <= arguments.length ? __slice.call(arguments, 0, fn.length - 1): []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ? ordinaryArgs.concat([restOfTheArgsList]): []); return fn.apply( this, args); } }; var firstAndButFirst = rightVariadic( function test (first, butFirst) { return [first, butFirst] }); firstAndButFirst('why', 'hello', 'there', 'little', 'droid') //=> ["why",["hello","there","little","droid"]]
```
