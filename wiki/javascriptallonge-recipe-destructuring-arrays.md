---
page_id: javascriptallonge-recipe-destructuring-arrays
page_kind: recipe
page_family: recipe-pattern
summary: destructuring arrays: reusable source-backed pattern with 5 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: destructuring-arrays
projection_coverage: recipe-javascriptallonge-recipe-destructuring-arrays@7ca8e35e1485aa1f35bec3067dbe6bcf
---

# destructuring arrays

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-arrays-6ab61a91]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-7239e085-00841))_
- The line const wrapped = [something]; is interesting. _(javascriptallonge.pdf (source-range-7239e085-00844))_
- In JavaScript, we can actually reverse the statement and place the template on the left and a value on the right: _(javascriptallonge.pdf (source-range-7239e085-00845))_
- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . _(javascriptallonge.pdf (source-range-7239e085-00847))_
- We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-7239e085-00849))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00842)_

```
const wrap = (something) => [something];
Let’s expand it to use a block and an extra name:
const wrap = (something) => {
const wrapped = [something];
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00843)_

```
const wrap = (something) => {
const wrapped = [something]
return wrapped;
}
wrap("package")
//=> ["package"]
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00846)_

```
const unwrap = (wrapped) => {
const [something] = wrapped;
return something;
}
unwrap(["present"])
//=> "present"
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00848)_

```
const surname = (name) => {
const [first, last] = name;
return last;
}
surname(["Reginald", "Braithwaite"])
//=> "Braithwaite"
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00851)_

```
const description = (nameAndOccupation) => {
const [[first, last], occupation] = nameAndOccupation;
return `${first} is a ${occupation}`;
}
description([["Reginald", "Braithwaite"], "programmer"])
//=> "Reginald is a programmer"
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-arrays-6ab61a91]]
