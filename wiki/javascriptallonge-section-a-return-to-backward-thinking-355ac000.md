---
page_id: javascriptallonge-section-a-return-to-backward-thinking-355ac000
page_kind: source
summary: a return to backward thinking: 22 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-return-to-backward-thinking-355ac000@8766b585cf9a53737ae17bbd579c0069
---

# a return to backward thinking

From [[javascriptallonge]].

## Statements

- To make pairs work, we did things backwards , we passed the first and rest functions to the pair, and the pair called our function. As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y) . _(javascriptallonge.pdf (source-range-31a4cf47-01409))_
- But we could have done something completely different. We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-31a4cf47-01410))_
- The exact implementation of a pair is hidden from the code that uses a pair. Here, we'll prove it: _(javascriptallonge.pdf (source-range-31a4cf47-01411))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-31a4cf47-01413))_
- We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-31a4cf47-01416))_
- We won't bother here, but it's easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally not the same thing as this code for the length of a linked list: _(javascriptallonge.pdf (source-range-31a4cf47-01417))_
- The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them. _(javascriptallonge.pdf (source-range-31a4cf47-01419))_
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. This is a fundamental principle of good design. It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. _(javascriptallonge.pdf (source-range-31a4cf47-01420))_
- There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns: _(javascriptallonge.pdf (source-range-31a4cf47-01421))_
- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-31a4cf47-01422))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-31a4cf47-01416))_

## Technical atoms

### Technical frame 1: a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01413))_

> This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01412))_

```
const first = K, second = K(I), pair = (first) => (second) => { const pojo = {first, second}; return (selector) => selector(pojo.first)(pojo.second); }; const latin = pair("primus")("secundus"); latin(first) //=> "primus" latin(second) //=> "secundus"
```

### Technical frame 2: a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01416))_

> We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01415))_

```
const length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) );
```

### Technical frame 3: a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01419))_

> The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01418))_

```
const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);
```
