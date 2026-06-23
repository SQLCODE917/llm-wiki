---
page_id: javascriptallonge-destructuring-and-return-values
page_kind: source
summary: destructuring and return values from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.106-107
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses how some languages support multiple return values, and how this can be emulated in JavaScript using destructuring.

## Key supported claims

- Some languages support multiple return values: A function can return several things at once, like a value and an error code. (raw/javascriptallonge.pdf p.106-107)
- This can easily be emulated in JavaScript with destructuring. (raw/javascriptallonge.pdf p.106-107)
- In JavaScript, a function can return multiple values using destructuring. (raw/javascriptallonge.pdf p.106-107)

## Technical details

### `technical-atom-41384d0ebd0a8674` code

Citation: (raw/javascriptallonge.pdf p.106-107)

```javascript
const description = (nameAndOccupation) => { if (nameAndOccupation.length < 2) { return ["", "occupation missing"] } else { const [[first, last], occupation] = nameAndOccupation; return [` ${ first } is a ${ occupation } `, "ok"]; } } const [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]); reg //=> "Reginald is a programmer" status //=> "ok"
```
