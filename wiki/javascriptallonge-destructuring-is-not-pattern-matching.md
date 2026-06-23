---
page_id: javascriptallonge-destructuring-is-not-pattern-matching
page_kind: source
summary: destructuring is not pattern matching from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.105-106
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Summary of the section 'destructuring is not pattern matching' from javascriptallonge.pdf

## Key supported claims

- But this is not how JavaScript works, as it tries its best to assign things and binds undefined when there isn't a match. (raw/javascriptallonge.pdf p.105-106)
- That match would fail in pattern matching languages, but JavaScript binds undefined instead. (raw/javascriptallonge.pdf p.105-106)
- JavaScript coerces values and passes undefined to keep executing, often requiring custom code to detect failure conditions. (raw/javascriptallonge.pdf p.105-106)

## Technical details

### `technical-atom-89cdabc3cb9e7f9f` code

Citation: (raw/javascriptallonge.pdf p.105-106)

```javascript
const [what] = [];
```

### `technical-atom-1b1f471330642106` code

Citation: (raw/javascriptallonge.pdf p.105-106)

```javascript
const [what] = []; what //=> undefined const [which, what, who //=> undefined
```

### `technical-atom-b77da3ce96a4fb74` code

Citation: (raw/javascriptallonge.pdf p.105-106)

```javascript
const [...they] = []; they //=> [] const [which, what, they //=> []
```

### `technical-atom-880219b3a5b552f7` exception

Citation: (raw/javascriptallonge.pdf p.105-106)

As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing.

### `technical-atom-820341aea79f7af4` exception

Citation: (raw/javascriptallonge.pdf p.105-106)

This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.
