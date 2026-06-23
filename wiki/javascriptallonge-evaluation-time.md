---
page_id: javascriptallonge-evaluation-time
page_kind: source
summary: evaluation time from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.204-204
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Summary of the evaluation time section from JavaScript Allongé, focusing on quasi-literals and their evaluation timing.

## Key supported claims

- Like any other expression, quasi-literals are evaluated late, when that line or lines of code is evaluated. (raw/javascriptallonge.pdf p.204-204)
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. (raw/javascriptallonge.pdf p.204-204)
- Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked. (raw/javascriptallonge.pdf p.204-204)

## Technical details

### `technical-atom-b953a8b77eeafa45` code

Citation: (raw/javascriptallonge.pdf p.204)

```javascript
const name = "Harry"; const greeting = (name) => `Hello my name is ${ name } `; greeting('Arthur Dent') //=> 'Hello my name is Arthur Dent'
```

### `technical-atom-2b2624939ec3068f` code

Citation: (raw/javascriptallonge.pdf p.204)

```javascript
const greeting = (name) => 'Hello my name is ' + name; greeting('Arthur Dent') //=> 'Hello my name is Arthur Dent'
```
