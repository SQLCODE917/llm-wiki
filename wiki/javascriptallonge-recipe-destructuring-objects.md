---
page_id: javascriptallonge-recipe-destructuring-objects
page_kind: recipe
page_family: recipe-pattern
summary: destructuring objects: reusable source-backed pattern with 2 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: destructuring-objects
projection_coverage: recipe-javascriptallonge-recipe-destructuring-objects@269dab194cad94ff066ec8260d919654
---

# destructuring objects

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-destructuring-objects-b7f3e8d1]].
- Evidence roles: decision, example.

## Applicability And Rationale

- When the label is a valid variable name, it's often the most obvious variable name as well. _(javascriptallonge.pdf (source-range-7239e085-01100))_
- It is very common to write things like title: title when destructuring objects. _(javascriptallonge.pdf (source-range-7239e085-01100))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01096)_

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

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01098)_

```
} = us\
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01099)_

```
const description = ({name: { first: given }, occupation: { title: title } }) =>
`${given} is a ${title}`;
description(user)
//=> "Reginald is a Author"
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01101)_

```
const description = ({name: { first }, occupation: { title } }) =>
`${first} is a ${title}`;
description(user)
//=> "Reginald is a Author"
And that same syntax works for literals:
const abbrev = ({name: { first, last }, occupation: { title } }) => {
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01102)_

```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-destructuring-objects-b7f3e8d1]]
