---
page_id: javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-destructuring-objects-b7f3e8d1
page_kind: source
summary: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects: 7 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-destructuring-objects-b7f3e8d1@e7bfb09d19d2f8446ce7e52a14e156a2
---

# Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-bce9b969]] - broader source section: Composing and Decomposing Data / Plain Old JavaScript Objects

## Statements

- Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization: _(javascriptallonge.pdf (source-range-7239e085-01100))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01096))_

```
const user = {
name: { first: "Reginald",
last: "Braithwaite"
},
occupation: { title: "Author",
responsibilities: [ "JavaScript Allongé",
"JavaScript Spessore",
"CoffeeScript Ristretto"
]
}
};
user.name.last
//=> "Braithwaite"
user.occupation.title
//=> "Author"
And we can also write:
const {name: { first: given, last: surname}, occupation: { title: title }
er;
surname
//=> "Braithwaite"
title
//=> "Author"
```

### Technical frame 2: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01098))_

```
} = us\
```

### Technical frame 3: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01099))_

```
const description = ({name: { first: given }, occupation: { title: title } }) =>
`${given} is a ${title}`;
description(user)
//=> "Reginald is a Author"
```

### Technical frame 4: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01101))_

```
const description = ({name: { first }, occupation: { title } }) =>
`${first} is a ${title}`;
description(user)
//=> "Reginald is a Author"
And that same syntax works for literals:
const abbrev = ({name: { first, last }, occupation: { title } }) => {
```

### Technical frame 5: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01102))_

```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```
