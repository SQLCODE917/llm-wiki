---
page_id: javascriptallonge-ternary-operator
page_kind: concept
summary: Ternary Operator: 1 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-ternary-operator@6f14c9caf2b3e59aacc053219233527a
---

# Ternary Operator

What [[javascriptallonge]] covers about ternary operator:

## Statements

### truthiness and the ternary operator

- JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-8eb13d6b-00768))_


## Technical atoms

### Technical frame 1: truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00773))_

> The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00772))_

```
true ? 'Hello' : 'Good bye' //=> 'Hello' 0 ? 'Hello' : 'Good bye' //=> 'Good bye' [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' //=> 'Pentatonic'
```


## Related pages

- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from truthiness and the ternary operator: JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
