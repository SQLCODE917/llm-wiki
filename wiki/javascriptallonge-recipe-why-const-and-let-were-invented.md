---
page_id: javascriptallonge-recipe-why-const-and-let-were-invented
page_kind: recipe
page_family: recipe-pattern
summary: why const and let were invented: reusable source-backed pattern with 11 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: why-const-and-let-were-invented
projection_coverage: recipe-javascriptallonge-recipe-why-const-and-let-were-invented@4fb6461bc1114310b17b427862d2246a
---

# why const and let were invented

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-reassignment-why-const-and-let-were-invented-d21b490b]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-7239e085-01202))_
- For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). _(javascriptallonge.pdf (source-range-7239e085-01202))_
- We haven't looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. _(javascriptallonge.pdf (source-range-7239e085-01203))_
- Hopefully, you can think of a faster way to calculate this sum. _(javascriptallonge.pdf (source-range-7239e085-01205))_
- 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. _(javascriptallonge.pdf (source-range-7239e085-01205))_
- The other kids were adding the numbers like this: 1 + 2 + 3 + . _(javascriptallonge.pdf (source-range-7239e085-01206))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01204)_

```
var sum = 0;
for (var i = 1; i <= 100; i++) {
sum = sum + i
}
sum
#=> 5050
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-reassignment-why-const-and-let-were-invented-d21b490b]]
