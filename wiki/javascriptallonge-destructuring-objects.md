---
page_id: javascriptallonge-destructuring-objects
page_kind: source
summary: destructuring objects from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.136-137
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter covers object destructuring in JavaScript, including how to destructure nested objects and how to use syntactic optimizations for cleaner code. It also shows how destructuring can be used with function parameters to extract values from objects.

## Key supported claims

- It is very common to write things like title: title when destructuring objects (raw/javascriptallonge.pdf p.136-137).
- When the label is a valid variable name, it's often the most obvious variable name as well, so JavaScript supports a further syntactic optimization (raw/javascriptallonge.pdf p.136-137).

## Technical details

### `technical-atom-2fa843b604012360` code

Citation: (raw/javascriptallonge.pdf p.136-137)

```javascript
const user = { name: { first: "Reginald", last: "Braithwaite" }, occupation: { title: "Author", responsibilities: [ "JavaScript Allongé", "JavaScript Spessore", "CoffeeScript Ristretto" ] } }; user.name.last //=> "Braithwaite" user.occupation.title //=> "Author" And we can also write: const {name: { first: given, last: surname}, occupation: { title: title } er; surname //=> "Braithwaite" title //=> "Author"
```

### `technical-atom-7f7056559d90c083` code

Citation: (raw/javascriptallonge.pdf p.136-137)

```
} = us\
```

### `technical-atom-79d50a479bf3cca0` code

Citation: (raw/javascriptallonge.pdf p.136-137)

```javascript
const description = ({name: { first: given }, occupation: { title: title } }) => ` ${ given } is a ${ title } `; description(user) //=> "Reginald is a Author"
```

### `technical-atom-5d1c487ec919df2a` code

Citation: (raw/javascriptallonge.pdf p.136-137)

```javascript
const description = ({name: { first }, occupation: { title } }) => ` ${ first } is a ${ title } `; description(user) //=> "Reginald is a Author" And that same syntax works for literals: {
```

### `technical-atom-21cec3cded0f0590` code

Citation: (raw/javascriptallonge.pdf p.136-137)

```javascript
const abbrev = ({name: { first, last }, occupation: { title } }) => return { first, last, title}; } abbrev(user) //=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```
