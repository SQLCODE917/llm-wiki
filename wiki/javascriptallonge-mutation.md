---
page_id: javascriptallonge-mutation
page_kind: concept
summary: Mutation: 28 statement(s) and 15 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-mutation@16b34c91ed59186461090c5deb3a94c4
---

# Mutation

What [[javascriptallonge]] covers about mutation:

## Statements

- Mutation is a surprisingly complex subject. _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-83ecb080-01740))_
- Now that we’ve finished with mutation and aliases, let’s have a look at it. _(javascriptallonge.pdf (source-range-83ecb080-01709))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. _(javascriptallonge.pdf (source-range-83ecb080-01716))_
- As noted, one pattern is to be more liberal about mutation when building a data structure. _(javascriptallonge.pdf (source-range-83ecb080-01740))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-83ecb080-01743))_
- But when we’re in the midst of creating a brand new list, we aren’t sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-83ecb080-01747))_
- Recall that you can access a value from within an array or an object using []. _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- Specifically, arrays and objects can mutate. _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- In JavaScript, almost every type of value can _mutate_ . _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- We have established that JavaScript’s semantics allow for two different bindings to refer to the same value. _(javascriptallonge.pdf (source-range-83ecb080-01696))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-83ecb080-01698))_
- There are two nested environments, and each one binds a name to the exact same array value. _(javascriptallonge.pdf (source-range-83ecb080-01701))_

## Technical atoms

> Context: In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =:
_(context: javascriptallonge.pdf (source-range-83ecb080-01688))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01689))_

> Context: You can even add a value:
_(context: javascriptallonge.pdf (source-range-83ecb080-01690))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[3] = 'four'; oneTwoThree _//=> [ 1, 2, 3, 'four' ]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01693))_

> Context: You can do the same thing with both syntaxes for accessing objects:
_(context: javascriptallonge.pdf (source-range-83ecb080-01694))_

> **const** name = {firstName: 'Leonard', lastName: 'Braithwaite'}; name.middleName = 'Austin' name _//=> { firstName: 'Leonard',_ # lastName: 'Braithwaite', # middleName: 'Austin' }
_(source: javascriptallonge.pdf (source-range-83ecb080-01695))_

> Context: We have established that JavaScript’s semantics allow for two different bindings to refer to the same value. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01696))_

> **const** allHallowsEve = [2012, 10, 31] **const** halloween = allHallowsEve;
_(source: javascriptallonge.pdf (source-range-83ecb080-01697))_

> Context: Both halloween and allHallowsEve are bound to the same array value within the local environment. And also: There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two _aliases_ for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.
_(context: javascriptallonge.pdf (source-range-83ecb080-01698, source-range-83ecb080-01701))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { _// ..._
_(source: javascriptallonge.pdf (source-range-83ecb080-01699))_

> Context: This is vital. Consider what we already know about shadowing: The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?
_(context: javascriptallonge.pdf (source-range-83ecb080-01702, source-range-83ecb080-01707))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31];
_(source: javascriptallonge.pdf (source-range-83ecb080-01705))_


## Source

- [[javascriptallonge]]
