---
page_id: javascriptallonge-section-a-return-to-backward-thinking-71ca1db1
page_kind: source
summary: **a return to backward thinking**: 26 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-return-to-backward-thinking-71ca1db1@e255485ee85b546cd12e942a0595b4c7
---

# **a return to backward thinking**

From [[javascriptallonge]].

## Statements

- As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y). _(javascriptallonge.pdf (source-range-83ecb080-02176))_
- To make pairs work, we did things _backwards_ , we passed the first and rest functions to the pair, and the pair called our function. _(javascriptallonge.pdf (source-range-83ecb080-02176))_
- All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-83ecb080-02177))_
- But we could have done something completely different. _(javascriptallonge.pdf (source-range-83ecb080-02177))_
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. _(javascriptallonge.pdf (source-range-83ecb080-02177))_
- The exact implementation of a pair is hidden from the code that uses a pair. _(javascriptallonge.pdf (source-range-83ecb080-02178))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-83ecb080-02185))_
- We’re passing list what we want done with an empty list, and what we want done with a list that has at least one element. _(javascriptallonge.pdf (source-range-83ecb080-02187))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-02187))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-02187))_
- This is fundamentally _not_ the same thing as this code for the length of a linked list: _(javascriptallonge.pdf (source-range-83ecb080-02190))_
- It presumes there is one canonical empty list value. _(javascriptallonge.pdf (source-range-83ecb080-02195))_
- We can fix this with an isEmpty function, but now we’re pushing even more knowledge about the structure of lists into the code that uses them. _(javascriptallonge.pdf (source-range-83ecb080-02195))_
- It presumes you can compare these things with the === operator. _(javascriptallonge.pdf (source-range-83ecb080-02195))_
- This is a fundamental principle of good design. _(javascriptallonge.pdf (source-range-83ecb080-02196))_
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. _(javascriptallonge.pdf (source-range-83ecb080-02196))_
- It is a tenet of Object-Oriented Programming, but it is **not** exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. _(javascriptallonge.pdf (source-range-83ecb080-02196))_
- There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns: _(javascriptallonge.pdf (source-range-83ecb080-02197))_
- - Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-83ecb080-02198))_

## Technical atoms

> Context: The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02178))_

> **const** first = K, second = K(I), pair = (first) => (second) => { **const** pojo = {first, second};
_(source: javascriptallonge.pdf (source-range-83ecb080-02179))_

> Context: The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02178))_

> **return** (selector) => selector(pojo.first)(pojo.second); };
_(source: javascriptallonge.pdf (source-range-83ecb080-02180))_

> Context: The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02178))_

> **const** latin = pair("primus")("secundus");
_(source: javascriptallonge.pdf (source-range-83ecb080-02181))_

> latin(second) _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02184))_

> Context: This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. The same thing happens with our lists. Here’s length for lists:
_(context: javascriptallonge.pdf (source-range-83ecb080-02185))_

> **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) );
_(source: javascriptallonge.pdf (source-range-83ecb080-02186))_

> Context: We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:
_(context: javascriptallonge.pdf (source-range-83ecb080-02190))_

> **const** length = (node, delayed = 0) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-02191))_

> Context: We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:
_(context: javascriptallonge.pdf (source-range-83ecb080-02190))_

> node === EMPTY
_(source: javascriptallonge.pdf (source-range-83ecb080-02192))_
