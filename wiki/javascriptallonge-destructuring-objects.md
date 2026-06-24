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

## Related technical details

### From [[javascriptallonge-plain-old-javascript-objects]]: `technical-atom-c8c475f5a5275af7` code

Relation: nearby source page; matched terms `can`, `code`, `javascript`, `objects`, `things`, `used`

Citation: (raw/javascriptallonge.pdf p.132)

```javascript
const remember = ["the milk", "the coffee beans", "the biscotti"]; And they can be used to store heterogeneous things in various levels of structure:
```

### From [[javascriptallonge-literal-object-syntax]]: `technical-atom-d57202306c2b8fa1` code

Relation: nearby source page; matched terms `code`, `name`, `object`, `objects`, `use`, `values`

Citation: (raw/javascriptallonge.pdf p.133-136)

```javascript
{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } //=> false Objects use [] to access the values by name, using a string: { year: 2012, month: 6, day: 14 }['day'] //=> 14
```

### From [[javascriptallonge-plain-old-javascript-objects]]: `technical-atom-08c736021f08b986` code

Relation: nearby source page; matched terms `code`, `javascript`, `name`, `objects`, `title`

Citation: (raw/javascriptallonge.pdf p.132)

```javascript
const NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1; const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### From [[javascriptallonge-plain-old-javascript-objects]]: `technical-atom-b91f3af2d19fe2cf` procedure

Relation: nearby source page; matched terms `can`, `javascript`, `name`, `objects`

Citation: (raw/javascriptallonge.pdf p.132)

Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else.
