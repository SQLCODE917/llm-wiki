---
page_id: javascriptallonge-reference
page_kind: concept
summary: Reference: 5 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-reference@4541928a4c853099000cbd6129fc042f
---

# Reference

What [[javascriptallonge]] covers about reference:

## Statements

- JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-83ecb080-00359))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-83ecb080-00360))_
- Reference types do not. _(javascriptallonge.pdf (source-range-83ecb080-00227))_
- Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-83ecb080-01050))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-83ecb080-01062))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00355, source-range-83ecb080-00360))_

> We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally unders

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00358))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.


## Related pages

- [[javascriptallonge-type]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-copy]] - shared statements (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements (1 shared statement(s))
- [[javascriptallonge-structure]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
