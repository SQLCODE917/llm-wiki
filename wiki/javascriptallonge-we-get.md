---
page_id: javascriptallonge-we-get
page_kind: source
summary: We get: from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.278-279
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on stateless functions and naughts-and-crosses game implementation in JavaScript.

## Key supported claims

- And from there, a stateless function to play naughts-and-crosses is trivial: (raw/javascriptallonge.pdf p.278-279).
- And if we want to look up what move to make, we can write: (raw/javascriptallonge.pdf p.278-279).

## Technical details

### `technical-atom-cb2eff94e55c00d0` code

Citation: (raw/javascriptallonge.pdf p.278-279)

```
{ "o,x, , , , , , , ":6, "o,x,x, , , ,o, , ":3, "o,x, ,x, , ,o, , ":8, "o,x, , ,x, ,o, , ":3, "o,x, , , ,x,o, , ":3, "o,x, , , , ,o,x, ":3, "o,x, , , , ,o, ,x":3 }
```

### `technical-atom-64bc3261890a798c` code

Citation: (raw/javascriptallonge.pdf p.278-279)

```javascript
moveLookupTable[[ 'o', 'x', ' ', ' ', ' ', ' ', 'o', 'x', ' ' ]] //=> 3
```

### `technical-atom-bf68af0b793b420a` code

Citation: (raw/javascriptallonge.pdf p.278-279)

```javascript
statelessNaughtsAndCrosses([ 'o', 'x', ' ', ' ', ' ', ' ', 'o', 'x', ' ' ]) //=> 3
```
