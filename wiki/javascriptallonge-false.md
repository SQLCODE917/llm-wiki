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
