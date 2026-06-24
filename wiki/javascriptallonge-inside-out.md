---
page_id: javascriptallonge-inside-out
page_kind: source
summary: inside-out from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.50-51
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on inside-out function patterns in JavaScript allonge

## Key supported claims

- The inside-out pattern binds names within functions, like (diameter) => ((PI) => diameter * PI)(3.14159265) (raw/javascriptallonge.pdf p.50-51).
- Using magic literals like 3.14159265 is anathema to sustainable software development (raw/javascriptallonge.pdf p.50-51).
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation (raw/javascriptallonge.pdf p.50-51).

## Technical details

### `technical-atom-d9583bd5ee732714` code

Citation: (raw/javascriptallonge.pdf p.50-51)

```javascript
(diameter) => ((PI) => diameter * PI)(3.14159265)
```

### `technical-atom-f53f1a1127cb197d` code

Citation: (raw/javascriptallonge.pdf p.50-51)

```javascript
((diameter) => diameter * 3.14159265)(2) //=> 6.2831853 ((PI) => (diameter) => diameter * PI )(3.14159265)(2) //=> 6.2831853 ((diameter) => ((PI) => diameter * PI)(3.14159265))(2) //=> 6.2831853
```

### `technical-atom-b57edf9bed903da2` code

Citation: (raw/javascriptallonge.pdf p.50-51)

```javascript
(diameter) => // ...
```

### `technical-atom-7a1056807fba7188` code

Citation: (raw/javascriptallonge.pdf p.50-51)

```javascript
((PI) => // ... )(3.14159265)
```

### `technical-atom-c725b0b76758df95` code

Citation: (raw/javascriptallonge.pdf p.50-51)

```javascript
((PI) => (diameter) => diameter * PI )(3.14159265)
```

### `technical-atom-7c02e176bb54dfd2` procedure

Citation: (raw/javascriptallonge.pdf p.50-51)

There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression.

### `technical-atom-328897ffe434b785` procedure

Citation: (raw/javascriptallonge.pdf p.50-51)

We can turn things inside-out by putting the binding inside our diameter calculating function, like this:

### `technical-atom-145681b8d7fb756d` procedure

Citation: (raw/javascriptallonge.pdf p.50-51)

29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments.

## Related technical details

### From [[javascriptallonge-that-constant-coffee-craving]]: `technical-atom-eb6e7ab743e36d4b` code

Relation: nearby source page; matched terms `code`, `diameter`

Citation: (raw/javascriptallonge.pdf p.49-50)

```javascript
((diameter) => diameter * 3.14159265)(2) //=> 6.2831853 ((PI) => (diameter) => diameter * PI )(3.14159265)(2) //=> 6.2831853
```

### From [[javascriptallonge-const]]: `technical-atom-0fff76e11a2f0259` code

Relation: nearby source page; matched terms `code`, `diameter`

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
(diameter, PI) => diameter * PI
```

### From [[javascriptallonge-const]]: `technical-atom-6b1fa159b11f3fdf` code

Relation: nearby source page; matched terms `code`, `diameter`

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
((diameter, PI) => diameter * PI)(2, 3.14159265) //=> 6.2831853
```

### From [[javascriptallonge-const]]: `technical-atom-1b51371583d7be04` code

Relation: nearby source page; matched terms `code`, `diameter`

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
(diameter) => { const PI = 3.14159265; return diameter * PI }
```
