---
page_id: javascriptallonge-data
page_kind: concept
summary: Data: 5 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-data@0e5202ec0ee872faeadcffe41715cc60
---

# Data

What [[javascriptallonge]] covers about data:

## Statements

### Composing and Decomposing Data / Self-Similarity

- Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-7239e085-00886))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-7239e085-01032))_

### Yes. Consider this variation: / Functional Iterators

- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-7239e085-01280))_

### Yes. Consider this variation: / Making Data Out Of Functions / backwardness

- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it. _(javascriptallonge.pdf (source-range-7239e085-01358))_

- Our latin data structure is no longer a dumb data structure, it's a function. And instead of passing latin to first or second , we pass first or second to latin . It's exactly backwards of the way we write functions that operate on data. _(javascriptallonge.pdf (source-range-7239e085-01362))_


## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01044))_

> car is very fast, it simply extracts the first element of the cons cell.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01043))_

```
car(oneToFive)
//=> 1
```

### Technical frame 2: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01295))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01296))_

```
const EMPTY = null;
const isEmpty = (node) => node === EMPTY;
const pair = (first, rest = EMPTY) => ({first, rest});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: pair(first, list(...rest))
}
const print = (aPair) =>
isEmpty(aPair)
? ""
: `${aPair.first} ${print(aPair.rest)}`
const listIterator = (aPair) =>
() => {
const done = isEmpty(aPair);
if (done) {
return {done};
}
else {
const {first, rest} = aPair;
aPair = aPair.rest;
```

### Technical frame 3: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01295))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01297))_

```
return { done, value: first }
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
const aListIterator = listIterator(list(1, 4, 9, 16, 25));
iteratorSum(aListIterator)
//=> 55
```

### Technical frame 4: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01303))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01300))_

```
const NumberIterator = (number = 0) =>
() => ({ done: false, value: number++ })
fromOne = NumberIterator(1);
fromOne().value;
//=> 1
fromOne().value;
//=> 2
fromOne().value;
//=> 3
fromOne().value;
//=> 4
fromOne().value;
//=> 5
```

### Technical frame 5: Yes. Consider this variation: / Making Data Out Of Functions / backwardness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01358))_

> In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01355))_

```
const first = ([first, second]) => first,
second = ([first, second]) => second;
const latin = ["primus", "secundus"];
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00857))_

| entry | content |
| --- | --- |
| 57 | https://en.wikipedia.org/wiki/CAR_and_CDR |
| 58 | Kyle Simpson is the author of You Don't Know JS, available here |

<details>
<summary>Raw table text</summary>

```
57 https://en.wikipedia.org/wiki/CAR_and_CDR
58 Kyle Simpson is the author of You Don't Know JS, available here
```

</details>

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01333))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01335))_

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

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01463))_

| entry | content |
| --- | --- |
| 84 | https://github.com/raganwald/allong.es |
| 85 | http://underscorejs.org |

<details>
<summary>Raw table text</summary>

```
84 https://github.com/raganwald/allong.es
85 http://underscorejs.org
```

</details>


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Yes. Consider this variation: / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Function shares technical record from Yes. Consider this variation: / Functional Iterators / unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false, value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne( ... [truncated] (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Yes. Consider this variation: / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Functional Iterators shares technical record from Yes. Consider this variation: / Functional Iterators / iterating: const EMPTY = null; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, .. ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-structure]] - shared statements and technical atoms: Structure shares source evidence from Composing and Decomposing Data / Self-Similarity: Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some ... [truncated]; Structure shares technical record from Yes. Consider this variation: / Functional Iterators / iterating: const EMPTY = null; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, .. ... [truncated] (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Composing and Decomposing Data / Self-Similarity: Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some ... [truncated]; List shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: car(oneToFive) //=> 1 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-second]] - shared statements and technical atoms: Second shares source evidence from Yes. Consider this variation: / Making Data Out Of Functions / backwardness: In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.; Second shares technical record from Yes. Consider this variation: / Making Data Out Of Functions / backwardness: const first = ([first, second]) => first, second = ([first, second]) => second; const latin = ["primus", "secundus"]; first(latin) //=> "primus" second(latin) //=> "secundus" (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-allong]] - shared technical atoms: Allong shares technical table: 84 https://github.com/raganwald/allong.es 85 http://underscorejs.org (1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical table: 57 https://en.wikipedia.org/wiki/CAR_and_CDR 58 Kyle Simpson is the author of You Don't Know JS, available here (1 shared atom(s))
- [[javascriptallonge-gathering]] - shared technical atoms: Gathering shares technical table: 57 https://en.wikipedia.org/wiki/CAR_and_CDR 58 Kyle Simpson is the author of You Don't Know JS, available here (1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from Yes. Consider this variation: / Functional Iterators / unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false, value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical table: 84 https://github.com/raganwald/allong.es 85 http://underscorejs.org (1 shared atom(s))
- [[javascriptallonge-reference]] - shared technical atoms: Reference shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: car(oneToFive) //=> 1 (1 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: 57 https://en.wikipedia.org/wiki/CAR_and_CDR 58 Kyle Simpson is the author of You Don't Know JS, available here (1 shared atom(s))
- [[javascriptallonge-type]] - shared statements: Type shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
