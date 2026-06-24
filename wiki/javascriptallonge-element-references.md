---
page_id: javascriptallonge-element-references
page_kind: source
summary: element references from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.102-103
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on element references in JavaScript arrays, covering zero-based indexing and reference storage.

## Key supported claims

- Array elements are extracted using [ and ] postfix operators, with zero-based indexing (raw/javascriptallonge.pdf p.102-103).
- JavaScript arrays are zero-based (raw/javascriptallonge.pdf p.102-103).
- Arrays store references to the things you put in them, not copies (raw/javascriptallonge.pdf p.102-103).

## Technical details

### `technical-atom-ff3a8a2cd1dd583f` code

Citation: (raw/javascriptallonge.pdf p.102-103)

```javascript
const oneTwoThree = ["one", "two", "three"]; oneTwoThree[0] //=> 'one' oneTwoThree[1] //=> 'two' oneTwoThree[2] //=> 'three'
```

### `technical-atom-080c9abe55b63119` code

Citation: (raw/javascriptallonge.pdf p.102-103)

```javascript
const x = [], a = [x]; a[0] === x //=> true, arrays store references to the things you put in them.
```

## Related technical details

### From [[javascriptallonge-and-are-control-flow-operators]]: `technical-atom-fb78d9847d23a268` code

Relation: nearby source page; matched terms `javascript`, `not`, `operators`

Citation: (raw/javascriptallonge.pdf p.97-98)

```
If n === 0 , JavaScript does not evaluate (n !== 1 && even(n -2)) .
```

### From [[javascriptallonge-and-are-control-flow-operators]]: `technical-atom-2fe0c429c64a6e81` code

Relation: nearby source page; matched terms `javascript`, `not`, `operators`

Citation: (raw/javascriptallonge.pdf p.97-98)

```
In this case, if n === 0 , JavaScript does not evaluate (n !== 1 && even(n -2)) .
```

### From [[javascriptallonge-and-are-control-flow-operators]]: `technical-atom-3b6397aef7b5b591` requirement

Relation: nearby source page; matched terms `its`, `not`, `operators`

Citation: (raw/javascriptallonge.pdf p.97-98)

The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not.

### From [[javascriptallonge-destructuring-is-not-pattern-matching]]: `technical-atom-820341aea79f7af4` exception

Relation: nearby source page; matched terms `not`, `own`, `things`

Citation: (raw/javascriptallonge.pdf p.105-106)

This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.
