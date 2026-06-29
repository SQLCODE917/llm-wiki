---
page_id: javascriptallonge-section-destructuring-objects-7b9d1130
page_kind: source
summary: destructuring objects: 7 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-objects-7b9d1130@96c28ded4c1ad08e4845d8cf20f06acb
---

# destructuring objects

From [[javascriptallonge]].

## Statements

- Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization: _(javascriptallonge.pdf (source-range-8eb13d6b-01099))_

## Technical atoms

### Technical frame 1: destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01099))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01095))_

```
const user = { name: { first: "Reginald", last: "Braithwaite" }, occupation: { title: "Author", responsibilities: [ "JavaScript Allongé", "JavaScript Spessore", "CoffeeScript Ristretto" ] } }; user.name.last //=> "Braithwaite" user.occupation.title //=> "Author" And we can also write: const {name: { first: given, last: surname}, occupation: { title: title } er; surname //=> "Braithwaite" title //=> "Author"
```

### Technical frame 2: destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01099))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01097))_

```
} = us\
```

### Technical frame 3: destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01099))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01098))_

```
const description = ({name: { first: given }, occupation: { title: title } }) => ` ${ given } is a ${ title } `; description(user) //=> "Reginald is a Author"
```

### Technical frame 4: destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01099))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01100))_

```
const description = ({name: { first }, occupation: { title } }) => ` ${ first } is a ${ title } `; description(user) //=> "Reginald is a Author" And that same syntax works for literals: {
```

### Technical frame 5: destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01099))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01101))_

```
const abbrev = ({name: { first, last }, occupation: { title } }) => return { first, last, title}; } abbrev(user) //=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```
