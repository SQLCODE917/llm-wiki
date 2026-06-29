---
page_id: javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-say-please-4edc5a79
page_kind: source
summary: Yes. Consider this variation: / Making Data Out Of Functions / say 'please': 11 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-say-please-4edc5a79@a83b0e4a1cc40927c3efc38c3d45e3ef
---

# Yes. Consider this variation: / Making Data Out Of Functions / say 'please'

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-f095c99b]] - broader source section: Yes. Consider this variation: / Making Data Out Of Functions

## Statements

- Wekeep using the same pattern in our functions: aPair === EMPTY ? doSomething : doSomethingElse . This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-7239e085-01389))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here's length again: _(javascriptallonge.pdf (source-range-7239e085-01390))_
- Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names: _(javascriptallonge.pdf (source-range-7239e085-01394))_
- We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters: _(javascriptallonge.pdf (source-range-7239e085-01397))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-7239e085-01399))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-7239e085-01390))_

## Technical atoms

### Technical frame 1: Yes. Consider this variation: / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01394))_

> Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01391))_

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(aPair(rest));
```

### Technical frame 2: Yes. Consider this variation: / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01394))_

> Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01393))_

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(rest)))
);
```

### Technical frame 3: Yes. Consider this variation: / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01397))_

> We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01395))_

```
const pairFirst = K,
pairRest
= K(I),
pair = V;
const first = (list) => list(
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairFirst)
);
const rest = (list) => list(
```

### Technical frame 4: Yes. Consider this variation: / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01397))_

> We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01396))_

```
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairRest)
);
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
We’ll also write a handy list printer:
const print = (list) => list(
() => "",
(aPair) => `${aPair(pairFirst)} ${print(aPair(pairRest))}`
);
How would all this work? Let’s start with the obvious. What is an empty list?
const EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty()
And what is a node of a list?
const node = (x) => (y) =>
(whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));
Let’s try it:
const l123 = node(1)(node(2)(node(3)(EMPTYLIST)));
print(l123)
//=> 1 2 3
```

### Technical frame 5: Yes. Consider this variation: / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01399))_

> We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01398))_

```
const reverse = (list, delayed = EMPTYLIST) => list(
() => delayed,
(aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed))
);
print(reverse(l123));
//=> 3 2 1
const mapWith = (fn, list, delayed = EMPTYLIST) =>
list(
() => reverse(delayed),
(aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed))
);
print(mapWith(x => x * x, reverse(l123)))
//=> 941
```
