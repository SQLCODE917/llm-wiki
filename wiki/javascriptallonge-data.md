---
page_id: javascriptallonge-data
page_kind: concept
summary: Data: 5 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-data@57430cf81eb45261d682249f0bc1080a
---

# Data

What [[javascriptallonge]] covers about data:

## Statements

### Self-Similarity

- Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-31a4cf47-00886))_

### Garbage, Garbage Everywhere

- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-31a4cf47-01031))_

### Functional Iterators

- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-31a4cf47-01280))_

### backwardness

- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it. _(javascriptallonge.pdf (source-range-31a4cf47-01358))_

- Our latin data structure is no longer a dumb data structure, it's a function. And instead of passing latin to first or second , we pass first or second to latin . It's exactly backwards of the way we write functions that operate on data. _(javascriptallonge.pdf (source-range-31a4cf47-01362))_


## Technical atoms

### Technical frame 1: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01043))_

> car is very fast, it simply extracts the first element of the cons cell.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01042))_

```
car(oneToFive) //=> 1
```

### Technical frame 2: backwardness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01358))_

> In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01355))_

```
const first = ([first, second]) => first, second = ([first, second]) => second; const latin = ["primus", "secundus"]; first(latin) //=> "primus" second(latin) //=> "secundus"
```

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01333))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01335))_

| entry | content |
| --- | --- |
| 76 | http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 |
| 77 | http://oscin.es |

<details>
<summary>Raw table text</summary>

```
76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422
77 http://oscin.es
```

</details>


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Function shares technical record from backwardness: const first = ([first, second]) => first, second = ([first, second]) => second; const latin = ["primus", "secundus"]; first(latin) //=> "primus" second(latin) //=> "secundus" (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Self-Similarity: Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some ... [truncated]; List shares technical record from Garbage, Garbage Everywhere: car(oneToFive) //=> 1 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-second]] - shared statements and technical atoms: Second shares source evidence from backwardness: In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.; Second shares technical record from backwardness: const first = ([first, second]) => first, second = ([first, second]) => second; const latin = ["primus", "secundus"]; first(latin) //=> "primus" second(latin) //=> "secundus" (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-reference]] - shared technical atoms: Reference shares technical record from Garbage, Garbage Everywhere: car(oneToFive) //=> 1 (1 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements: Functional Iterators shares source evidence from Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated] (1 shared statement(s))
- [[javascriptallonge-type]] - shared statements: Type shares source evidence from Garbage, Garbage Everywhere: Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
