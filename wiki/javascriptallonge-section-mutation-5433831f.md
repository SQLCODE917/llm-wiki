---
page_id: javascriptallonge-section-mutation-5433831f
page_kind: source
page_family: section-reference
summary: Mutation: 33 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mutation-5433831f@d3816f91db2e1edb8d910e7d78f50e77
---

# Mutation

From [[javascriptallonge]].

## Statements

- Composing and Decomposing Data 

118 

## **Mutation** 

**==> picture [240 x 321] intentionally omitted <==**

**Cupping Grinds** 

In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =: 

**const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_ 

You can even add a value: _(javascriptallonge.pdf (source-range-af806fb1-00160))_
- 119 

Composing and Decomposing Data 

**const** oneTwoThree = [1, 2, 3]; oneTwoThree[3] = 'four'; oneTwoThree _//=> [ 1, 2, 3, 'four' ]_ 

You can do the same thing with both syntaxes for accessing objects: 

**const** name = {firstName: 'Leonard', lastName: 'Braithwaite'}; name.middleName = 'Austin' name _//=> { firstName: 'Leonard',_ # lastName: 'Braithwaite', # middleName: 'Austin' } 

We have established that JavaScript’s semantics allow for two different bindings to refer to the same value. For example: 

**const** allHallowsEve = [2012, 10, 31] **const** halloween = allHallowsEve; 

Both halloween and allHallowsEve are bound to the same array value within the local environment. And also: 

**const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { _// ..._ 

- })(allHallowsEve); 

There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two _aliases_ for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. 

This is vital. Consider what we already know about shadowing: _(javascriptallonge.pdf (source-range-af806fb1-00161))_
- Composing and Decomposing Data 

120 

**const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; 

})(allHallowsEve); allHallowsEve _//=> [2012, 10, 31]_ 

The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment? 

**const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween[0] = 2013; })(allHallowsEve); allHallowsEve _//=> [2013, 10, 31]_ 

This is different. We haven’t rebound the inner name to a different variable, we’ve mutated the value that both bindings share. Now that we’ve finished with mutation and aliases, let’s have a look at it. 

**==> picture [29 x 29] intentionally omitted <==**

JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value. 

**==> picture [29 x 29] intentionally omitted <==**

Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction. 

## **mutation and data structures** 

Mutation is a surprisingly complex subject. It is possible to compute anything without ever mutating an existing entity. Languages like Haskell[70] don’t permit mutation at all. In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. 

One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let’s recall linked lists from Plain Old JavaScript Objects. While we’re executing the mapWith function, we’re constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith. 

But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example: 

70https://en.wikipedia.org/wiki/Haskell_ _(javascriptallonge.pdf (source-range-af806fb1-00162))_
- Composing and Decomposing Data 

121 

**const** EMPTY = {}; **const** OneToFive = { first: 1, rest: { first: 2, rest: { first: 3, rest: { first: 4, rest: { first: 5, rest: EMPTY } } } } }; 

OneToFive 

_//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\_ r","rest":{"first":"five","rest":{}}}}}} 

const ThreeToFive = OneToFive.rest.rest; 

ThreeToFive 

//=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}} 

ThreeToFive.first = "three"; ThreeToFive.rest.first = "four"; ThreeToFive.rest.rest.first = "five"; 

## ThreeToFive 

//=> {"first":"three","rest":{"first":"four","rest":{"first":"five","rest":{}}\ }} 

OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}} 

Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes. 

Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so: _(javascriptallonge.pdf (source-range-af806fb1-00163))_
- Composing and Decomposing Data 

122 

**const** OneToFive = [1, 2, 3, 4, 5]; 

OneToFive _//=> [1,2,3,4,5]_ **const** [a, b, ...ThreeToFive] = OneToFive; ThreeToFive _//=> [3, 4, 5]_ ThreeToFive[0] = "three"; ThreeToFive[1] = "four"; ThreeToFive[2] = "five"; ThreeToFive _//=> ["three","four","five"]_ OneToFive _//=> [1,2,3,4,5]_ 

The gathering operation [a, b, ...ThreeToFive] is slower, but “safer.” 

So back to avoiding mutation. In general, it’s easier to reason about data that doesn’t change. We don’t have to remember to use copying operations when we pass it as a value to a function, or extract some data from it. We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be “safe.” 

## **building with mutation** 

As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: 

**const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); 

**const** copy = (node) => reverse(reverse(node)); 

If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-af806fb1-00164))_
- 123 

Composing and Decomposing Data 

**const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first, rest }; tail.rest = newNode; **return** copy(node.rest, head, newNode); } } 

This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we’re in the midst of creating a brand new list, we aren’t sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. 

Armed with this basic copy implementation, we can write mapWith: 

**const** mapWith = (fn, node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first: fn(first), rest }; **return** mapWith(fn, rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first: fn(first), rest }; tail.rest = newNode; **return** mapWith(fn, node.rest, head, newNode); } } mapWith((x) => 1.0 / x, OneToFive) _(javascriptallonge.pdf (source-range-af806fb1-00165))_
- Recall that you can access a value from within an array or an object using []. _(javascriptallonge.pdf (source-range-af806fb1-00160))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-af806fb1-00161))_
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-af806fb1-00161))_
- But after returning the new list, we then become conservative about mutation. _(javascriptallonge.pdf (source-range-af806fb1-00162))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-af806fb1-00162))_
- Whereas destructuring an array with [first, ...rest] does make a copy, so: _(javascriptallonge.pdf (source-range-af806fb1-00163))_
