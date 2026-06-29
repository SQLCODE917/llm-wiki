---
page_id: javascriptallonge-section-the-function-keyword-b50ba16e
page_kind: source
summary: the function keyword: 10 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-function-keyword-b50ba16e@cbc8d7264a57ddf9d71f0de2513945fa
---

# the function keyword

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-function-keyword]] - topic hub: opens the topic page for Function Keyword
- [[javascriptallonge-section-the-function-keyword-332556f0]] - same source heading: another source section with the same heading, the function keyword

## Statements

- There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arrows.' We'll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-8eb13d6b-00608))_
- The first magic name is this , and it is bound to something called the function's context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-8eb13d6b-00609))_
- arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this: _(javascriptallonge.pdf (source-range-8eb13d6b-00613))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-8eb13d6b-00618))_

## Technical atoms

### Technical frame 1: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00610))_

```
const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5
```

### Technical frame 2: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00612))_

```
const args = function (a, b) { return arguments; } args(2,3) //=> { '0': 2, '1': 3 }
```

### Technical frame 3: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00618))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00615))_

```
const plus = function () { return arguments[0] + arguments[1]; } plus(2,3) //=> 5
```

### Technical frame 4: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00618))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00617))_

```
const howMany = function () { return arguments['length']; } howMany() //=> 0 howMany('hello') //=> 1 howMany('sharks', 'are', 'apex', 'predators') //=> 4
```

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00614))_

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

<details>
<summary>Raw table text</summary>

```
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

</details>
