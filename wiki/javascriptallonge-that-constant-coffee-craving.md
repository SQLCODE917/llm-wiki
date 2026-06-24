---
page_id: javascriptallonge-that-constant-coffee-craving
page_kind: source
summary: That Constant Coffee Craving from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.49-50
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

A chapter on naming functions and using function expressions to bind values.

## Key supported claims

- This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. (raw/javascriptallonge.pdf p.49-50)
- Naming things is a critical part of programming, but all we've seen so far is how to name arguments. (raw/javascriptallonge.pdf p.49-50)
- That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. (raw/javascriptallonge.pdf p.49-50)

## Technical details

### `technical-atom-39b04d2e762c08f4` code

Citation: (raw/javascriptallonge.pdf p.49-50)

```javascript
((PI) => // ???? )(3.14159265)
```

### `technical-atom-e9c49a14e573a588` code

Citation: (raw/javascriptallonge.pdf p.49-50)

```javascript
((PI) => (diameter) => diameter * PI )(3.14159265)
```

### `technical-atom-eb6e7ab743e36d4b` code

Citation: (raw/javascriptallonge.pdf p.49-50)

```javascript
((diameter) => diameter * 3.14159265)(2) //=> 6.2831853 ((PI) => (diameter) => diameter * PI )(3.14159265)(2) //=> 6.2831853
```

### `technical-atom-4b6581e8fed543e8` worked-example

Citation: (raw/javascriptallonge.pdf p.49-50)

Let's revisit a very simple example:

## Related technical details

### From [[javascriptallonge-inside-out]]: `technical-atom-d9583bd5ee732714` code

Relation: nearby source page; matched terms `diameter`

Citation: (raw/javascriptallonge.pdf p.50-51)

```javascript
(diameter) => ((PI) => diameter * PI)(3.14159265)
```

### From [[javascriptallonge-inside-out]]: `technical-atom-f53f1a1127cb197d` code

Relation: nearby source page; matched terms `diameter`

Citation: (raw/javascriptallonge.pdf p.50-51)

```javascript
((diameter) => diameter * 3.14159265)(2) //=> 6.2831853 ((PI) => (diameter) => diameter * PI )(3.14159265)(2) //=> 6.2831853 ((diameter) => ((PI) => diameter * PI)(3.14159265))(2) //=> 6.2831853
```

### From [[javascriptallonge-inside-out]]: `technical-atom-b57edf9bed903da2` code

Relation: nearby source page; matched terms `diameter`

Citation: (raw/javascriptallonge.pdf p.50-51)

```javascript
(diameter) => // ...
```

### From [[javascriptallonge-const]]: `technical-atom-0fff76e11a2f0259` code

Relation: nearby source page; matched terms `diameter`

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
(diameter, PI) => diameter * PI
```
