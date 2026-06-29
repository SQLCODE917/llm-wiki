---
page_id: javascriptallonge-gathering
page_kind: concept
summary: Gathering: 4 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-gathering@7577d065d9cb5f4115ddd0635bdd3d25
---

# Gathering

What [[javascriptallonge]] covers about gathering:

## Statements

### ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus

- The act of writing is an iterative process with (very often) tight revision loops. However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. On more than one occasion I've found myself attempting to reify feedback with content that either no longer existed or was changed beyond recognition. However, with the Leanpub model the read-feedback-change process is extremely efficient, leaving in its wake a quality book that continues to get better as others likewise read and comment into infinitude. _(javascriptallonge.pdf (source-range-7239e085-00085))_

### Recipes with Basic Functions / Left-Variadic Functions

- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do? _(javascriptallonge.pdf (source-range-7239e085-00723))_

### Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this: _(javascriptallonge.pdf (source-range-7239e085-00741))_

### Composing and Decomposing Data / Mutation / mutation and data structures

- The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. ' _(javascriptallonge.pdf (source-range-7239e085-01150))_


## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00719))_

> This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00718))_

```
const abccc = (a, b, ...c) => {
console.log(a);
console.log(b);
console.log(c);
};
abccc(1, 2, 3, 4, 5)
1
2
[3,4,5]
```

### Technical frame 2: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00747))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00742))_

```
const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
first
//=> 'why'
butFirst
//=> ["hello","there","little","droid"]
```

### Technical frame 3: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00749))_

> With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00748))_

```
const leftGather = (outputArrayLength) => {
return function (inputArray) {
return [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\
at(
inputArray.slice(inputArray.length - outputArrayLength + 1)
)
}
};
const [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\
']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```

### Technical frame 4: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00880))_

> Gathering works with parameters! This is very useful indeed, and we'll see more of it in a moment. 59

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00879))_

```
const numbers = (...nums) => nums;
numbers(1, 2, 3, 4, 5)
//=> [1,2,3,4,5]
const headAndTail = (head, ...tail) => [head, tail];
headAndTail(1, 2, 3, 4, 5)
//=> [1,[2,3,4,5]]
```

### Technical atom 5

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


## Related pages

- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this:; Argument shares technical record from Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid']; first //=> 'why' butFirst //=> ["hello","there","little","droid"] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this:; Function shares technical record from Recipes with Basic Functions / Left-Variadic Functions: const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-parameter]] - shared statements and technical atoms: Parameter shares source evidence from Recipes with Basic Functions / Left-Variadic Functions: ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do?; Parameter shares technical record from Recipes with Basic Functions / Left-Variadic Functions: const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Recipes with Basic Functions / Left-Variadic Functions: const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5] (2 shared atom(s))
- [[javascriptallonge-data]] - shared technical atoms: Data shares technical table: 57 https://en.wikipedia.org/wiki/CAR_and_CDR 58 Kyle Simpson is the author of You Don't Know JS, available here (1 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: 57 https://en.wikipedia.org/wiki/CAR_and_CDR 58 Kyle Simpson is the author of You Don't Know JS, available here (1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared statements: Ecmascript shares source evidence from Recipes with Basic Functions / Left-Variadic Functions: ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do? (1 shared statement(s))
- [[javascriptallonge-operation]] - shared statements: Operation shares source evidence from Composing and Decomposing Data / Mutation / mutation and data structures: The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. ' (1 shared statement(s))
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-gathering-91ed37bf]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering: Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:; Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering: const [car, ...cdr] = [1, 2, 3, 4, 5]; car //=> 1 cdr //=> [2, 3, 4, 5] (4 shared statement(s), 4 shared atom(s))

## Source

- [[javascriptallonge]]
