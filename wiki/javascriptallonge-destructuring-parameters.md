---
page_id: javascriptallonge-destructuring-parameters
page_kind: source
summary: destructuring parameters from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.107-108
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on destructuring parameters in JavaScript Allongé, covering gathering in parameters, pattern matching, and rest parameters.

## Key supported claims

- 59 Gathering in parameters has a long history, and the usual terms are to call gathering 'pattern matching' and to call a name that is bound to gathered values a 'rest parameter.' The term 'rest' is perfectly compatible with gather: 'Rest' is the noun, and 'gather' is the verb. We gather the rest of the parameters. (raw/javascriptallonge.pdf p.107-108)
- Gathering works with parameters! (raw/javascriptallonge.pdf p.107-108)
- It acts like destructuring. (raw/javascriptallonge.pdf p.107-108)
- We gather the rest of the parameters. (raw/javascriptallonge.pdf p.107-108)
- It looks like destructuring. (raw/javascriptallonge.pdf p.107-108)

## Technical details

### `technical-atom-13fa1172de5b9da2` code

Citation: (raw/javascriptallonge.pdf p.107-108)

```
foo() bar("smaug") baz(1, 2, 3)
```

### `technical-atom-e1a9bca53707e54f` code

Citation: (raw/javascriptallonge.pdf p.107-108)

```javascript
const foo = () => ... const bar = (name) => ... const baz = (a, b, c) => ...
```

### `technical-atom-4dcb2c57fbd7f89d` code

Citation: (raw/javascriptallonge.pdf p.107-108)

```javascript
const numbers = (...nums) => nums; numbers(1, 2, 3, 4, 5) //=> [1,2,3,4,5] const headAndTail = (head, ...tail) => [head, tail]; headAndTail(1, 2, 3, 4, 5) //=> [1,[2,3,4,5]]
```

### `technical-atom-d24fe13bc0b13a75` worked-example

Citation: (raw/javascriptallonge.pdf p.107-108)

Consider the way we pass arguments to parameters:

### `technical-atom-b52d8612fcee7742` worked-example

Citation: (raw/javascriptallonge.pdf p.107-108)

And consider how we bind values to parameter names:

### `technical-atom-bbb4bf595f66bdf3` code

Citation: (raw/javascriptallonge.pdf p.107-108)

```
const bar = (name) => ...
```

### `technical-atom-24a7e20951a09223` exception

Citation: (raw/javascriptallonge.pdf p.107-108)

There is only one difference: We have not tried gathering.
