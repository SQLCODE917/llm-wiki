---
page_id: javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-destructuring-objects-b7f3e8d1
page_kind: source
page_family: section-reference
summary: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-destructuring-objects-b7f3e8d1@f7f777d1c03388927174f25eedee7a3c
---

# Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-bce9b969]] - broader source section: Composing and Decomposing Data / Plain Old JavaScript Objects

## Statements

- Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization: _(javascriptallonge.pdf (source-range-7239e085-01100))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01096))_

<a id="atom-technical-atom-e83b3741e99adebe"></a>

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

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01101))_

<a id="atom-technical-atom-f52ea4d07eb5b43e"></a>

```
const description = ({name: { first }, occupation: { title } }) =>
`${first} is a ${title}`;
description(user)
//=> "Reginald is a Author"
And that same syntax works for literals:
const abbrev = ({name: { first, last }, occupation: { title } }) => {
```

### Technical frame 3: Composing and Decomposing Data / Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01100))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01102))_

<a id="atom-technical-atom-74bb588b6178e93c"></a>

```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```
