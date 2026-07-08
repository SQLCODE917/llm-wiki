---
page_id: javascriptallonge-recipe-once
page_kind: recipe
page_family: recipe-pattern
summary: Once: The once pattern ensures that a function can only be called once. Once the function is invoked, it will return undefined on subsequent calls.
sources: raw/javascriptallonge.pdf
updated: 2026-07-08
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
projection_coverage: human-article-javascriptallonge-recipe-once@2566bd5eab872357387d36a33fc6d197
---

# Once

## The Once Pattern

The once pattern ensures that a function can only be called once. _(raw/javascriptallonge.pdf (p. 88))_ Once the function is invoked, it will return undefined on subsequent calls. _(raw/javascriptallonge.pdf (p. 88))_ 

## How It Works

The once function takes another function as input and returns a new function that executes the original function only on its first call. _(raw/javascriptallonge.pdf (p. 88))_ 

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
- raw/javascriptallonge.pdf (p. 88) - Once
