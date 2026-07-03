---
page_id: javascriptallonge-fat-arrow
page_kind: concept
page_family: topic-concept
summary: Fat Arrow: 1 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-fat-arrow@5d534bf42f6a8f1b2cd8eaf35b9131e9
---

# Fat Arrow

What [[javascriptallonge]] covers about fat arrow:

## Statements

### And also: / Magic Names / magic names and fat arrows

- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword: _(javascriptallonge.pdf (source-range-7239e085-00625))_


## Technical atoms

### Technical frame 1: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00625))_

> To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00623))_

<a id="atom-technical-atom-733056f2f6551e51"></a>

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

<a id="atom-technical-atom-f66c3ed611303c0d"></a>

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

### Shared technical atoms

- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Magic Names / magic names and fat arrows: (function () { return (() => arguments[0])('inner'); })('outer') //=> "outer" (2 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from And also: / Magic Names / magic names and fat arrows: (function () { return (() => arguments[0])('inner'); })('outer') //=> "outer" (2 shared atom(s))

### Shared claims

- [[javascriptallonge-function-keyword]] - shared statements: the function keyword shares source evidence from And also: / Magic Names / magic names and fat arrows: To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
