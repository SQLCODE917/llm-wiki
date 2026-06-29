---
page_id: javascriptallonge-different
page_kind: concept
summary: Different: 5 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-different@6509631c869d00f3223f187488898ccf
---

# Different

What [[javascriptallonge]] covers about different:

## Statements

### matthew knox

- A different kind of language requires a different kind of book. _(javascriptallonge.pdf (source-range-8eb13d6b-00091))_

### That Constant Coffee Craving

- Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-8eb13d6b-00388))_

### are consts also from a shadowy planet?

- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-8eb13d6b-00469))_

### Mutation

- This is different. We haven't rebound the inner name to a different variable, we've mutated the value that both bindings share. Now that we've finished with mutation and aliases, let's have a look at it. _(javascriptallonge.pdf (source-range-8eb13d6b-01135))_

### Served by the Pot: Collections

- Some different sized and coloured coffee pots by Antti Nurmesniemi, perhaps his most known design. _(javascriptallonge.pdf (source-range-8eb13d6b-01523))_


## Technical atoms

### Technical frame 1: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00478))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00477))_

```
((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265)
```

### Technical frame 2: Mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01128))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01127))_

```
const allHallowsEve = [2012, 10, 31] const halloween = allHallowsEve;
```


## Related pages

- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Bind shares technical record from are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-binding]] - shared statements and technical atoms: Binding shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Binding shares technical record from are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms: Environment shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Environment shares technical record from are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Value shares technical record from Mutation: const allHallowsEve = [2012, 10, 31] const halloween = allHallowsEve; (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Mutation: const allHallowsEve = [2012, 10, 31] const halloween = allHallowsEve; (1 shared atom(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from matthew knox: A different kind of language requires a different kind of book. (2 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated] (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements: Program shares source evidence from That Constant Coffee Craving: Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, wher ... [truncated] (1 shared statement(s))
- [[javascriptallonge-programming]] - shared statements: Programming shares source evidence from That Constant Coffee Craving: Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, wher ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
