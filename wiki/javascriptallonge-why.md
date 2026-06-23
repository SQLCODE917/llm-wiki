---
page_id: javascriptallonge-why
page_kind: source
summary: Why? from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.201-201
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter Why? from 'JavaScript Allongé' explains the Y Combinator and its role in recursive functions without binding names.

## Key supported claims

- This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names. (raw/javascriptallonge.pdf p.201-201)
- The Y Combinator enables you to make recursive functions without needing to bind a function to a name in an environment. (raw/javascriptallonge.pdf p.201-201)
- It is possible to compute everything computable with fixed-point combinators without binding names. (raw/javascriptallonge.pdf p.201-201)

## Technical details

### `technical-atom-74e1dd29d52c577b` code

Citation: (raw/javascriptallonge.pdf p.201)

```javascript
This is the canonical Y Combinator 86 : const Y = (f) => ( x => f(v => x(x)(v)) )( x => f(v => x(x)(v)) ); You use it like this: const factorial = Y( function (fac) { (n == 0 ? 1 : n * fac(n - 1));
```

### `technical-atom-ae0af9e5d4e859a4` code

Citation: (raw/javascriptallonge.pdf p.201)

```javascript
return function (n) { return } }); factorial(5) //=> 120
```

### `technical-atom-d80a8fd9472e57bd` code

Citation: (raw/javascriptallonge.pdf p.201)

```javascript
const Y = (f) => { const something = x => f(v => x(x)(v)); return something(something); };
```

### `technical-atom-776bae49d78fde36` exception

Citation: (raw/javascriptallonge.pdf p.201)

It enables you to make recursive functions without needing to bind a function to a name in an environment.

### `technical-atom-7fab936335f3084f` exception

Citation: (raw/javascriptallonge.pdf p.201)

This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names.

### `technical-atom-adca9ea1d55f4eb3` worked-example

Citation: (raw/javascriptallonge.pdf p.201)

For example, you could start by writing:
