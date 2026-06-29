---
page_id: javascriptallonge-section-composing-and-decomposing-data-mutation-d77e57e8
page_kind: source
summary: Composing and Decomposing Data / Mutation: 49 source-backed entries and 19 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-mutation-d77e57e8@50f72d058152dccf70fba33bf2caa3cd
---

# Composing and Decomposing Data / Mutation

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-6f7d7870]] - broader source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-mutation-mutation-and-data-structures-5828e27e]] - narrower source section: Composing and Decomposing Data / Mutation / mutation and data structures
- [[javascriptallonge-section-composing-and-decomposing-data-mutation-building-with-mutation-bd1adba2]] - narrower source section: Composing and Decomposing Data / Mutation / building with mutation
- [[javascriptallonge-mutation]] - topic hub: opens the topic page for Mutation

## Statements

- In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = : _(javascriptallonge.pdf (source-range-7239e085-01121))_
- Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example: _(javascriptallonge.pdf (source-range-7239e085-01127))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. And also: _(javascriptallonge.pdf (source-range-7239e085-01129))_
- There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two aliases for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-7239e085-01131))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we mutate the value in the inner environment? _(javascriptallonge.pdf (source-range-7239e085-01134))_
- This is different. We haven't rebound the inner name to a different variable, we've mutated the value that both bindings share. Now that we've finished with mutation and aliases, let's have a look at it. _(javascriptallonge.pdf (source-range-7239e085-01136))_
- JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value. _(javascriptallonge.pdf (source-range-7239e085-01138))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction. _(javascriptallonge.pdf (source-range-7239e085-01140))_
- Recall that you can access a value from within an array or an object using [] . _(javascriptallonge.pdf (source-range-7239e085-01121))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-7239e085-01129))_
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-7239e085-01131))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. _(javascriptallonge.pdf (source-range-7239e085-01134))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-7239e085-01140))_

## Statements by subsection

### Composing and Decomposing Data / Mutation / mutation and data structures

- Mutation is a surprisingly complex subject. It is possible to compute anything without ever mutating an existing entity. Languages like Haskell 70 don't permit mutation at all. In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-7239e085-01142))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-7239e085-01143))_
- The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. ' _(javascriptallonge.pdf (source-range-7239e085-01150))_
- So back to avoiding mutation. In general, it's easier to reason about data that doesn't change. We don't have to remember to use copying operations when we pass it as a value to a function, or extract some data from it. We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be 'safe.' _(javascriptallonge.pdf (source-range-7239e085-01151))_

### Composing and Decomposing Data / Mutation / building with mutation

- As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-7239e085-01153))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-7239e085-01155))_
- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-7239e085-01157))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01121))_

> In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01119))_

> [Figure] (p.141)

### Technical frame 2: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01122))_

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[0] = 'one';
oneTwoThree
//=> [ 'one', 2, 3 ]
```

### Technical frame 3: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01124))_

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[3] = 'four';
oneTwoThree
//=> [ 1, 2, 3, 'four' ]
```

### Technical frame 4: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01126))_

```
const name = {firstName: 'Leonard', lastName: 'Braithwaite'};
name.middleName = 'Austin'
name
//=> { firstName: 'Leonard',
#
lastName: 'Braithwaite',
#
middleName: 'Austin' }
```

### Technical frame 5: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01129))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01128))_

```
const allHallowsEve = [2012, 10, 31]
const halloween = allHallowsEve;
```

### Technical frame 6: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01131))_

> There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two aliases for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01130))_

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
// ...
})(allHallowsEve);
```

### Technical frame 7: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01134))_

> The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we mutate the value in the inner environment?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01133))_

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
halloween = [2013, 10, 31];
})(allHallowsEve);
allHallowsEve
//=> [2012, 10, 31]
```

### Technical frame 8: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01136))_

> This is different. We haven't rebound the inner name to a different variable, we've mutated the value that both bindings share. Now that we've finished with mutation and aliases, let's have a look at it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01135))_

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
halloween[0] = 2013;
})(allHallowsEve);
allHallowsEve
//=> [2013, 10, 31]
```

### Technical frame 9: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01138))_

> JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01137))_

> [Figure] (p.143)

### Technical frame 10: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01140))_

> Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01139))_

> [Figure] (p.143)

### Technical frame 11: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01144))_

> But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:

### Technical frame 12: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01146))_

```
const EMPTY = {};
const OneToFive = { first: 1,
rest: {
first: 2,
rest: {
first: 3,
rest: {
first: 4,
rest: {
first: 5,
rest: EMPTY } } } } };
OneToFive
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\
r","rest":{"first":"five","rest":{}}}}}}
const ThreeToFive = OneToFive.rest.rest;
ThreeToFive
//=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}}
ThreeToFive.first = "three";
ThreeToFive.rest.first = "four";
ThreeToFive.rest.rest.first = "five";
ThreeToFive
//=> {"first":"three","rest":{"first":"four","rest":{"first":"five","rest":{}}\
}}
OneToFive
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\
r","rest":{"first":"five","rest":{}}}}}}
Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we
wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of {"first":3,"rest":{"firs
we were getting a reference to the same chain of nodes.
Structure sharing like this is what makes linked lists so fast for taking everything but the first item
```

### Technical frame 13: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01148))_

```
const OneToFive = [1, 2, 3, 4, 5];
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] = OneToFive;
```

### Technical frame 14: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01149))_

```
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] =
ThreeToFive
//=> [3, 4, 5]
ThreeToFive[0] = "three";
ThreeToFive[1] = "four";
ThreeToFive[2] = "five";
ThreeToFive
//=> ["three","four","five"]
OneToFive
//=> [1,2,3,4,5]
```

### Technical frame 15: Composing and Decomposing Data / Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01150))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01151))_

> We don't have to remember to use copying operations when we pass it as a value to a function, or extract some data from it.

### Technical frame 16: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01155))_

> If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01154))_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const copy = (node) => reverse(reverse(node));
```

### Technical frame 17: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01157))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01156))_

```
const copy = (node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first, rest };
return copy(rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first, rest };
tail.rest = newNode;
return copy(node.rest, head, newNode);
}
}
```

### Technical frame 18: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01157))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01159))_

```
const mapWith = (fn, node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
return mapWith(fn, rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
tail.rest = newNode;
return mapWith(fn, node.rest, head, newNode);
}
}
mapWith((x) => 1.0 / x, OneToFive)
```

### Technical frame 19: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01157))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01160))_

```
//=> {"first":1,"rest":{"first":0.5,"rest":{"first":0.3333333333333333,"rest":\
{"first":0.25,"rest":{"first":0.2,"rest":{}}}}}}
```
