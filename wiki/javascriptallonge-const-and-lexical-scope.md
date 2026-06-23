---
page_id: javascriptallonge-const-and-lexical-scope
page_kind: source
summary: const and lexical scope from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.55-57
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on const and lexical scope from JavaScript Allongé, covering the semantics of binding names with const and how it relates to closures and lexical scoping.

## Key supported claims

- Const uses lexical scope. (raw/javascriptallonge.pdf p.55-57)
- Understanding const requires understanding lexical scoping. (raw/javascriptallonge.pdf p.55-57)
- Const behaves similarly to parameter invocations in lexical scoping. (raw/javascriptallonge.pdf p.55-57)

## Technical details

### `technical-atom-bd2e48d2cd4ff0f2` code

Citation: (raw/javascriptallonge.pdf p.55-57)

```javascript
((diameter_fn) => // ... )( ((PI) => (diameter) => diameter * PI )(3.14159265) )
```

### `technical-atom-6d6230b65912f463` code

Citation: (raw/javascriptallonge.pdf p.55-57)

```javascript
((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) //=> 6.2831853
```

### `technical-atom-fc4611747fdec015` code

Citation: (raw/javascriptallonge.pdf p.55-57)

```javascript
((diameter_fn) => ((PI) => diameter_fn(2) )(3) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) //=> 6.2831853
```

### `technical-atom-0a73212255b67341` code

Citation: (raw/javascriptallonge.pdf p.55-57)

```javascript
((diameter_fn) => { const PI = 3; return diameter_fn(2) })( (() => { const PI = 3.14159265; return (diameter) => diameter * PI })() ) //=> 6.2831853
```
