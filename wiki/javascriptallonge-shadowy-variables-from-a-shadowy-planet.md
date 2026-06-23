---
page_id: javascriptallonge-shadowy-variables-from-a-shadowy-planet
page_kind: source
summary: shadowy variables from a shadowy planet from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.47-47
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. JavaScript searches for a binding starting with the function's own environment and then each parent in turn until it finds one. An interesting thing happens when a variable has the same name as an ancestor environment's variable.

## Key supported claims

- A variable shadows an ancestor when names match, (raw/javascriptallonge.pdf p.47-47).
- JavaScript searches environments from child to parent, (raw/javascriptallonge.pdf p.47-47).
- A function is pure if its x is defined within its own environment, (raw/javascriptallonge.pdf p.47-47).

## Technical details

### `technical-atom-09c4361291d7bd60` code

Citation: (raw/javascriptallonge.pdf p.47)

```javascript
(x) => (x, y) => x + y
```

### `technical-atom-2238642332b0495e` code

Citation: (raw/javascriptallonge.pdf p.47)

```javascript
(x) => (x, y) => (w, z) => (w) => x + y + z
```

### `technical-atom-592864b8cc8594c9` procedure

Citation: (raw/javascriptallonge.pdf p.47)

JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one.
