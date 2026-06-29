---
page_id: javascriptallonge-fat-arrow
page_kind: concept
summary: Fat Arrow: 3 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-fat-arrow@a12afdc3588a0add48133616f525ed7e
---

# Fat Arrow

What [[javascriptallonge]] covers about fat arrow:

## Statements

### And also: / Magic Names / magic names and fat arrows

- But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . And thus arguments[0] will refer to "outer" , not to "inner" : _(javascriptallonge.pdf (source-range-7239e085-00622))_

- Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax. _(javascriptallonge.pdf (source-range-7239e085-00624))_

- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword: _(javascriptallonge.pdf (source-range-7239e085-00625))_


## Technical atoms

### Technical frame 1: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00624))_

> Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00623))_

```
(function () {
return (() => arguments[0])('inner');
})('outer')
//=> "outer"
```

### Technical frame 2: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00627))_

> This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00626))_

```
const row = function () {
return mapWith(
(column) => column * arguments[0],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [3,6,9,12,15,18,21,24,27,30,33,36]
```


## Related pages

- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Magic Names / magic names and fat arrows: (function () { return (() => arguments[0])('inner'); })('outer') //=> "outer" (2 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from And also: / Magic Names / magic names and fat arrows: (function () { return (() => arguments[0])('inner'); })('outer') //=> "outer" (2 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared statements: the function keyword shares source evidence from And also: / Magic Names / magic names and fat arrows: To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
