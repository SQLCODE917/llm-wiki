---
page_id: javascriptallonge-section-say-please-7214c91b
page_kind: source
summary: say 'please': 11 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-say-please-7214c91b@f493be7d26175ff7c52f5e7b6046c181
---

# say 'please'

From [[javascriptallonge]].

## Statements

- Wekeep using the same pattern in our functions: aPair === EMPTY ? doSomething : doSomethingElse . This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-8eb13d6b-01388))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here's length again: _(javascriptallonge.pdf (source-range-8eb13d6b-01389))_
- Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names: _(javascriptallonge.pdf (source-range-8eb13d6b-01393))_
- We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters: _(javascriptallonge.pdf (source-range-8eb13d6b-01396))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-8eb13d6b-01398))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-8eb13d6b-01389))_

## Technical atoms

### Technical frame 1: say 'please'

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01393))_

> Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01390))_

```
const length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest));
```

### Technical frame 2: say 'please'

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01393))_

> Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01392))_

```
const length = (list) => list( () => 0, (aPair) => 1 + length(aPair(rest))) );
```

### Technical frame 3: say 'please'

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01396))_

> We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01394))_

```
const pairFirst = K, pairRest = K(I), pair = V; const first = (list) => list( () => "ERROR: Can't take first of an empty list", (aPair) => aPair(pairFirst) ); const rest = (list) => list(
```

### Technical frame 4: say 'please'

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01396))_

> We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01395))_

```
() => "ERROR: Can't take first of an empty list", (aPair) => aPair(pairRest) ); const length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) ); We'll also write a handy list printer: const print = (list) => list( () => "", (aPair) => ` ${ aPair(pairFirst) } ${ print(aPair(pairRest)) } ` ); How would all this work? Let's start with the obvious. What is an empty list? const EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty() And what is a node of a list? const node = (x) => (y) => (whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y)); Let's try it: const l123 = node(1)(node(2)(node(3)(EMPTYLIST))); print(l123) //=> 1 2 3
```

### Technical frame 5: say 'please'

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01398))_

> We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01397))_

```
const reverse = (list, delayed = EMPTYLIST) => list( () => delayed, (aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed)) ); print(reverse(l123)); //=> 3 2 1 const mapWith = (fn, list, delayed = EMPTYLIST) => list( () => reverse(delayed), (aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed)) ); print(mapWith(x => x * x, reverse(l123))) //=> 941
```
