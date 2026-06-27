---
page_id: javascriptallonge-section-mutation-7ccd2c26
page_kind: source
summary: Mutation: 51 source-backed entries and 16 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mutation-7ccd2c26@58b53deb7a9cdeee79756ffd84e44700
---

# Mutation

From [[javascriptallonge]].

## Statements

- Recall that you can access a value from within an array or an object using []. _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- Specifically, arrays and objects can mutate. _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- In JavaScript, almost every type of value can _mutate_ . _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- Recall that you can access a value from within an array or an object using []. _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- We have established that JavaScript’s semantics allow for two different bindings to refer to the same value. _(javascriptallonge.pdf (source-range-83ecb080-01696))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-83ecb080-01698))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-83ecb080-01698))_
- There are two nested environments, and each one binds a name to the exact same array value. _(javascriptallonge.pdf (source-range-83ecb080-01701))_
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-83ecb080-01701))_
- In each of these examples, we have created two _aliases_ for the same value. _(javascriptallonge.pdf (source-range-83ecb080-01701))_
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-83ecb080-01701))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. _(javascriptallonge.pdf (source-range-83ecb080-01707))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. _(javascriptallonge.pdf (source-range-83ecb080-01707))_
- We haven’t rebound the inner name to a different variable, we’ve mutated the value that both bindings share. _(javascriptallonge.pdf (source-range-83ecb080-01709))_
- Now that we’ve finished with mutation and aliases, let’s have a look at it. _(javascriptallonge.pdf (source-range-83ecb080-01709))_
- Mutating existing objects has special implications when two bindings are aliases of the same value. _(javascriptallonge.pdf (source-range-83ecb080-01711))_
- JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. _(javascriptallonge.pdf (source-range-83ecb080-01711))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-83ecb080-01713))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-83ecb080-01713))_
- Mutation is a surprisingly complex subject. _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- It is possible to compute anything without ever mutating an existing entity. _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- While we’re executing the mapWith function, we’re constructing a new linked list. _(javascriptallonge.pdf (source-range-83ecb080-01716))_
- Let’s recall linked lists from Plain Old JavaScript Objects. _(javascriptallonge.pdf (source-range-83ecb080-01716))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. _(javascriptallonge.pdf (source-range-83ecb080-01716))_
- When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes. _(javascriptallonge.pdf (source-range-83ecb080-01731))_
- Changes made to ThreeToFive affect OneToFive, because they share the same structure. _(javascriptallonge.pdf (source-range-83ecb080-01731))_
- Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. _(javascriptallonge.pdf (source-range-83ecb080-01732))_
- We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be “safe.” _(javascriptallonge.pdf (source-range-83ecb080-01738))_
- Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-83ecb080-01740))_
- As noted, one pattern is to be more liberal about mutation when building a data structure. _(javascriptallonge.pdf (source-range-83ecb080-01740))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-83ecb080-01743))_
- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. _(javascriptallonge.pdf (source-range-83ecb080-01747))_
- But when we’re in the midst of creating a brand new list, we aren’t sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-83ecb080-01747))_
- Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. _(javascriptallonge.pdf (source-range-83ecb080-01747))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01688))_

> In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01689))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01690))_

> You can even add a value:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01693))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[3] = 'four'; oneTwoThree _//=> [ 1, 2, 3, 'four' ]_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01694))_

> You can do the same thing with both syntaxes for accessing objects:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01695))_

> **const** name = {firstName: 'Leonard', lastName: 'Braithwaite'}; name.middleName = 'Austin' name _//=> { firstName: 'Leonard',_ # lastName: 'Braithwaite', # middleName: 'Austin' }

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01696))_

> We have established that JavaScript’s semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01697))_

> **const** allHallowsEve = [2012, 10, 31] **const** halloween = allHallowsEve;

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01698, source-range-83ecb080-01701))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also: There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two _aliases_ for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01699))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { _// ..._

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01702, source-range-83ecb080-01707))_

> This is vital. Consider what we already know about shadowing: The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01705))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31];

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01707))_

> The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01706))_

> })(allHallowsEve); allHallowsEve _//=> [2012, 10, 31]_

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01708))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween[0] = 2013; })(allHallowsEve); allHallowsEve _//=> [2013, 10, 31]_

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01716))_

> One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let’s recall linked lists from Plain Old JavaScript Objects. While we’re executing the mapWith function, we’re constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01717))_

> But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:

### Technical atom 10

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01724))_

> const ThreeToFive = OneToFive.rest.rest;

### Technical atom 11

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01727))_

> ThreeToFive.first = "three"; ThreeToFive.rest.first = "four"; ThreeToFive.rest.rest.first = "five";

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01731))_

> Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01730))_

> OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}}

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01732))_

> Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01735))_

> **const** OneToFive = [1, 2, 3, 4, 5];

### Technical atom 14

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01738))_

> We don’t have to remember to use copying operations when we pass it as a value to a function, or extract some data from it.

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01740))_

> As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01741))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01740))_

> As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01742))_

> **const** copy = (node) => reverse(reverse(node));
