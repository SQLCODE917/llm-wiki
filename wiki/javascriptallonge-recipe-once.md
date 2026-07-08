---
page_id: javascriptallonge-recipe-once
page_kind: recipe
page_family: recipe-pattern
summary: Once: The Once recipe is an extremely helpful combinator that ensures a function can only be called once.
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
projection_coverage: human-article-javascriptallonge-recipe-once@435428656a9f061ebd606dbec8b95041
---

# Once

## Overview

The Once recipe is an extremely helpful combinator that ensures a function can only be called once. _(raw/javascriptallonge.pdf (p. 88))_ 

## Implementation

When you pass a function to Once, you get a function back that will call your function once, and thereafter will return undefined whenever it is called. _(raw/javascriptallonge.pdf (p. 88))_ 

## Behavior

The implementation of Once is demonstrated by the example where askedOnBlindDate is called multiple times, returning the result on the first call and undefined on subsequent calls. _(raw/javascriptallonge.pdf (p. 88))_ 

## Evidence Details

### raw/javascriptallonge.pdf (p. 88)

```text
const askedOnBlindDate = once(
() => "sure, why not?"
);
askedOnBlindDate()
//=> 'sure, why not?'
askedOnBlindDate()
//=> undefined
askedOnBlindDate()
//=> undefined
```

- raw/javascriptallonge.pdf (p. 88): `once is an extremely helpful combinator.`
- raw/javascriptallonge.pdf (p. 88): `It ensures that a function can only be called, well, once .`
- raw/javascriptallonge.pdf (p. 88): `You pass it a function, and you get a function back.`
- raw/javascriptallonge.pdf (p. 88): `That function will call your function once, and thereafter will return undefined whenever it is called.`
- raw/javascriptallonge.pdf (p. 88): `It seems some people will only try blind dating once.`
- raw/javascriptallonge.pdf (p. 88): `We'll look at that again in stateful method decorators.)`

## Related pages

- [[javascriptallonge]] - source: A book about JavaScript programming patterns and techniques.

## Source Trail

- Source manifest: [[javascriptallonge]]
- raw/javascriptallonge.pdf (p. 88)
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
