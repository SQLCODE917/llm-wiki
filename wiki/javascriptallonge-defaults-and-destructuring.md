---
page_id: javascriptallonge-defaults-and-destructuring
page_kind: source
summary: defaults and destructuring from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.124-125
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter covering defaults and destructuring in JavaScript. Destructuring parameters works same as destructuring assignment. Defaults supplied for destructuring assignments. Default parameter arguments can be created.

## Key supported claims

- Destructuring parameters works same as destructuring assignment, (raw/javascriptallonge.pdf p.124-125)
- Defaults supplied for destructuring assignments, (raw/javascriptallonge.pdf p.124-125)
- Default parameter arguments can be created, (raw/javascriptallonge.pdf p.124-125)

## Technical details

### `technical-atom-390ae9487222cc8a` code

Citation: (raw/javascriptallonge.pdf p.124-125)

```javascript
const [first, second = "two"] = ["one"]; ` ${ first } . ${ second } ` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; ` ${ first } . ${ second } ` //=> "primus . secundus"
```

### `technical-atom-c07249979d7963a8` code

Citation: (raw/javascriptallonge.pdf p.124-125)

```
two" const [first, second = "two"] = ["primus", "secundus"]; ` ${ first } .
```
