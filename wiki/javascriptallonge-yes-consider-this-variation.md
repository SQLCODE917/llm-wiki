---
page_id: javascriptallonge-yes-consider-this-variation
page_kind: source
summary: Yes. Consider this variation: from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.155-157
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section from JavaScript Allongé explores the pitfalls of using `var` in loops and how `let` provides a cleaner solution, demonstrating closure behavior with a practical example.

## Key supported claims

- So when the function is called, JavaScript looks up i in its enclosing environment (its closure, obviously), and gets the value 3, as cited in (raw/javascriptallonge.pdf p.155-157).
- But at the time we call one of the functions, i has the value 3, which is why the loop terminated, as cited in (raw/javascriptallonge.pdf p.155-157).
- The answer is that pesky var i, as cited in (raw/javascriptallonge.pdf p.155-157).

## Technical details

### `technical-atom-1b3e9b6aed400459` code

Citation: (raw/javascriptallonge.pdf p.155-157)

```javascript
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; for ( var i = 0; i < 3; i++) { introductions[i] = "Hello, my name is " + names[i] } introductions //=> [ 'Hello, my name is Karl', // 'Hello, my name is Friedrich', // 'Hello, my name is Gauss' ]
```

### `technical-atom-91f1657fb684d2b2` code

Citation: (raw/javascriptallonge.pdf p.155-157)

```javascript
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; for ( var i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, ${ soAndSo } , my name is ${ names[i] } ` } introductions //=> [ [Function], // [Function], // [Function] ]
```

### `technical-atom-a7ec6d3b0aa6883a` code

Citation: (raw/javascriptallonge.pdf p.155-157)

```javascript
introductions[1]('Raganwald') //=> 'Hello, Raganwald, my name is undefined'
```

### `technical-atom-fe0fc837e583f22a` code

Citation: (raw/javascriptallonge.pdf p.155-157)

```javascript
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss'], i = undefined ; for (i = 0; i < 3; i++) { introductions[i] = function (soAndSo) { return "Hello, " + soAndSo + ", my name is " + names[i] } } introductions
```

### `technical-atom-da5be0cb552d2548` code

Citation: (raw/javascriptallonge.pdf p.155-157)

```javascript
let introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; for ( let i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, ${ soAndSo } , my name is ${ names[i] } ` } introductions[1]('Raganwald') //=> 'Hello, Raganwald, my name is Friedrich'
```

### `technical-atom-7081d7b0f71c58aa` code

Citation: (raw/javascriptallonge.pdf p.155-157)

```javascript
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; for ( var i = 0; i < 3; i++) { ((i) => { introductions[i] = (soAndSo) => `Hello, ${ soAndSo } , my name is ${ names[i] } ` } })(i) } introductions[1]('Raganwald') //=> 'Hello, Raganwald, my name is Friedrich'
```

### `technical-atom-46a2f302032ad08c` exception

Citation: (raw/javascriptallonge.pdf p.155-157)

That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming.
