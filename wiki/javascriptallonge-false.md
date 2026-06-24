---
page_id: javascriptallonge-false
page_kind: source
summary: false from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.94-95
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé discusses the boolean values true and false, focusing on their behavior with logical operators.

## Key supported claims

- In JavaScript, true and false are value types (raw/javascriptallonge.pdf p.94-95).
- All values of true are strictly equal to all other values of true (raw/javascriptallonge.pdf p.94-95).
- The ! operator negates its argument (raw/javascriptallonge.pdf p.94-95).
- The && and || operators perform logical AND and OR (raw/javascriptallonge.pdf p.94-95).
- Behavior of false with logical operators is demonstrated (raw/javascriptallonge.pdf p.94-95).

## Technical details

### `technical-atom-532b9080737cfab8` code

Citation: (raw/javascriptallonge.pdf p.94-95)

```javascript
! true //=> false ! false //=> true
```

### `technical-atom-fca6abba09d65cf5` code

Citation: (raw/javascriptallonge.pdf p.94-95)

```javascript
false && false //=> false false && true //=> false true && false //=> false true && true //=> true false || false //=> false false || true //=> true true || false //=> true true || true //=> true
```

## Related technical details

### From [[javascriptallonge-truthiness-and-operators]]: `technical-atom-4242c29147b55336` requirement

Relation: nearby source page; matched terms `argument`, `false`, `its`, `operators`, `true`

Citation: (raw/javascriptallonge.pdf p.96-97)

It always returns false if its argument is truthy, and true is its argument is not truthy:

### From [[javascriptallonge-truthiness-and-operators]]: `technical-atom-db1a2dfcc5799e60` code

Relation: nearby source page; matched terms `false`, `operators`, `true`

Citation: (raw/javascriptallonge.pdf p.96-97)

```javascript
!5 //=> false ! undefined //=> true
```

### From [[javascriptallonge-truthiness-and-the-ternary-operator]]: `technical-atom-bb41af449e0cdc69` exception

Relation: nearby source page; matched terms `false`, `javascript`, `operator`, `other`, `value`

Citation: (raw/javascriptallonge.pdf p.95-96)

Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' .

### From [[javascriptallonge-truthiness-and-operators]]: `technical-atom-dbc76303af6bafa8` requirement

Relation: nearby source page; matched terms `equal`, `logical`, `operators`, `strictly`, `values`

Citation: (raw/javascriptallonge.pdf p.96-97)

They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .
