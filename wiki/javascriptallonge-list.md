---
page_id: javascriptallonge-list
page_kind: concept
summary: List: 21 statement(s) and 35 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-list@d579b9e49795d394cf8c1bbd3021a0a7
---

# List

What [[javascriptallonge]] covers about list:

## Statements

### Recipes with Basic Functions / Partial Application

- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic. _(javascriptallonge.pdf (source-range-7239e085-00660))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments

- While we have mentioned arrays briefly, we haven't had a close look at them. Arrays are JavaScript's 'native' representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-7239e085-00818))_

### Composing and Decomposing Data / Self-Similarity

- Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-7239e085-00886))_

- Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list , [e, ...list] is a list. We can test this manually by building up a list: _(javascriptallonge.pdf (source-range-7239e085-00890))_

### Composing and Decomposing Data / Self-Similarity / folding

- With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn't. A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-7239e085-00936))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

- Lists were represented as linked lists of cons cells, with each cell's head pointing to an element and the tail pointing to another cons cell. _(javascriptallonge.pdf (source-range-7239e085-01033))_

- Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-7239e085-01047))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

- Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it. _(javascriptallonge.pdf (source-range-7239e085-01055))_

### Composing and Decomposing Data / Plain Old JavaScript Objects

- Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list: _(javascriptallonge.pdf (source-range-7239e085-01062))_

- Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-7239e085-01065))_

### Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-7239e085-01111))_

- Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous values. Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-7239e085-01117))_

### Composing and Decomposing Data / Mutation / building with mutation

- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-7239e085-01157))_

### Yes. Consider this variation: / Copy on Write

- We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: _(javascriptallonge.pdf (source-range-7239e085-01225))_

- This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-7239e085-01232))_

### Yes. Consider this variation: / Copy on Write / copy-on-read

- So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-7239e085-01239))_

### Yes. Consider this variation: / Copy on Write / copy-on-write

- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other: _(javascriptallonge.pdf (source-range-7239e085-01249))_

### Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking

- We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-7239e085-01416))_

- Having a list know itself whether it is empty hides implementation information from the code that uses lists. This is a fundamental principle of good design. It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. _(javascriptallonge.pdf (source-range-7239e085-01420))_


## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00662))_

> As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe if we wish to create partial applications of object methods.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00661))_

```
const callFirst = (fn, larg) =>
function (...rest) {
return fn.call(this, larg, ...rest);
}
const callLast = (fn, rarg) =>
function (...rest) {
return fn.call(this, ...rest, rarg);
}
const greet = (me, you) =>
`Hello, ${you}, my name is ${me}`;
const heliosSaysHello = callFirst(greet, 'Helios');
heliosSaysHello('Eartha')
//=> 'Hello, Eartha, my name is Helios'
const sayHelloToCeline = callLast(greet, 'Celine');
sayHelloToCeline('Eartha')
//=> 'Hello, Celine, my name is Eartha'
```

### Technical frame 2: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00892))_

> Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00891))_

```
[]
//=> []
["baz", ...[]]
//=> ["baz"]
["bar", ...["baz"]]
//=> ["bar","baz"]
["foo", ...["bar", "baz"]]
//=> ["foo","bar","baz"]
```

### Technical frame 3: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00895))_

```
const [first, ...rest] = [];
first
//=> undefined
rest
//=> []:
const [first, ...rest] = ["foo"];
first
//=> "foo"
rest
//=> []
const [first, ...rest] = ["foo", "bar"];
first
//=> "foo"
rest
//=> ["bar"]
const [first, ...rest] = ["foo", "bar", "baz"];
first
//=> "foo"
rest
//=> ["bar","baz"]
For the purpose of this exploration, we will presume the following:61
const isEmpty = ([first, ...rest]) => first === undefined;
```

### Technical frame 4: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00902))_

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
Let’s try it!
length([])
//=> 0
length(["foo"])
//=> 1
length(["foo", "bar", "baz"])
```

### Technical frame 5: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00903))_

```
//=> 3
```

### Technical frame 6: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00930))_

> This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00927))_

```
const squareAll = ([first, ...rest]) => first === undefined
? []
: [first * first, ...squareAll(rest)\
];
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 7: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00930))_

> This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00929))_

```
const truthyAll = ([first, ...rest]) => first === undefined
? []
: [!!first, ...truthyAll(rest)];
truthyAll([null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

### Technical frame 8: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00943))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00937))_

```
const sumSquares = ([first, ...rest]) => first === undefined
? 0
: first * first + sumSquares(rest);
sumSquares([1, 2, 3, 4, 5])
//=> 55
```

### Technical frame 9: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01038))_

```
const oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, null)))));
```

### Technical frame 10: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01039))_

```
oneToFive
//=> [1,[2,[3,[4,[5,null]]]]]
```

### Technical frame 11: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01041))_

```
const node5 = [5,null],
node4 = [4, node5],
node3 = [3, node4],
node2 = [2, node3],
node1 = [1, node2];
const oneToFive = node1;
```

### Technical frame 12: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01044))_

> car is very fast, it simply extracts the first element of the cons cell.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01043))_

```
car(oneToFive)
//=> 1
```

### Technical frame 13: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01047))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01046))_

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

### Technical frame 14: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01056))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01055))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

### Technical frame 15: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01057))_

> Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation).

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01056))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.

### Technical frame 16: Composing and Decomposing Data / Plain Old JavaScript Objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01065))_

> Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01063))_

```
const remember = ["the milk", "the coffee beans", "the biscotti"];
And they can be used to store heterogeneous things in various levels of structure:
```

### Technical frame 17: Composing and Decomposing Data / Plain Old JavaScript Objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01065))_

> Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01064))_

```
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\
vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### Technical frame 18: Composing and Decomposing Data / Plain Old JavaScript Objects

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01067))_

> Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0] . Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary 69 data type, a mapping from a unique set of objects to another set of objects.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01066))_

```
const NAME = 0,
FIRST = 0,
LAST = 1,
OCCUPATION = 1,
TITLE = 0,
RESPONSIBILITIES = 1;
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\
vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### Technical frame 19: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01106))_

> In essence, this simple implementation used functions to create an abstraction with named elements. But now that we've looked at objects, we can use an object instead of a two-element array. While we're at it, let's use contemporary names. So our linked list nodes will be formed from { first, rest }

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01105))_

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Technical frame 20: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01109))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01107))_

```
In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first:
2, rest: { first: 3, rest: EMPTY } } }.
We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

### Technical frame 21: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01109))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01108))_

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest
//=> {"first":2,"rest":{"first":3,"rest":{}}}
OneTwoThree.rest.rest.first
//=> 3
Taking the length of a linked list is easy:
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

### Technical frame 22: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01111))_

> The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01110))_

```
const slowcopy = (node) =>
node === EMPTY
? EMPTY
: { first: node.first, rest: slowcopy(node.rest)};
slowcopy(OneTwoThree)
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{}}}}
```

### Technical frame 23: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01116))_

> Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01115))_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
And now, we can make a reversing map:
const reverseMapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
reverseMapWith((x) => x * x, OneTwoThree)
//=> {"first":9,"rest":{"first":4,"rest":{"first":1,"rest":{}}}}
And a regular mapWith follows:
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const mapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? reverse(delayed)
: mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
mapWith((x) => x * x, OneTwoThree)
//=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}
```

### Technical frame 24: Composing and Decomposing Data / Mutation / building with mutation

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

### Technical frame 25: Composing and Decomposing Data / Mutation / building with mutation

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

### Technical frame 26: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01228))_

> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

### Technical frame 27: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01229))_

> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

### Technical frame 28: Yes. Consider this variation: / Copy on Write / a few utilities

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01237))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01235))_

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
const first = ({first, rest}) => first;
const rest = ({first, rest}) => rest;
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(rest(node), { first: first(node), rest: delayed });
const mapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? reverse(delayed)
: mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed });
const at = (index, list) =>
index === 0
? first(list)
: at(index - 1, rest(list));
const set = (index, value, list, originalList = list) =>
index === 0
? (list.first = value, originalList)
: set(index - 1, value, rest(list), originalList)
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
```

### Technical frame 29: Yes. Consider this variation: / Copy on Write / a few utilities

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01237))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01236))_

```
const childList = rest(parentList);
set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\
{},"rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

### Technical frame 30: Yes. Consider this variation: / Copy on Write / copy-on-read

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01241))_

> This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01240))_

```
const rest = ({first, rest}) => copy(rest);
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 31: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01249))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01246))_

```
const rest = ({first, rest}) => rest;
const set = (index, value, list) =>
index === 0
? { first: value, rest: list.rest }
: { first: list.first, rest: set(index - 1, value, list.rest) };
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
const newChildList = set(0, "two", childList);
```

### Technical frame 32: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01249))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01248))_

```
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{"first":{},"rest":\
{}}}}}
childList
//=> {"first":2,"rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 33: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01251))_

> And now functions like mapWith that make copies without modifying anything, work at full speed.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01250))_

```
newParentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
newChildList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 34: Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01416))_

> We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01415))_

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
```

### Technical frame 35: Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01419))_

> The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01418))_

```
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
```


## Related pages

- [[javascriptallonge-copy-write]] - shared statements and technical atoms: Copy on Write shares source evidence from Yes. Consider this variation: / Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them:; Copy on Write shares technical record from Yes. Consider this variation: / Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (4 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-copy]] - shared statements and technical atoms: Copy shares source evidence from Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists: The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the ca ... [truncated]; Copy shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Composing and Decomposing Data / Self-Similarity: Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e ... [truncated]; Element shares technical record from Composing and Decomposing Data / Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (3 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-rest]] - shared statements and technical atoms: Rest shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-read: So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy.; Rest shares technical record from Composing and Decomposing Data / Self-Similarity: const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar ... [truncated] (1 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Composing and Decomposing Data / Self-Similarity / folding: With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn't. A function to compu ... [truncated]; Function shares technical record from Composing and Decomposing Data / Self-Similarity: const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); Let’s try it! length([]) //=> 0 length(["foo"]) //=> 1 length(["foo", "bar", "baz"]) (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-length]] - shared statements and technical atoms: Length shares source evidence from Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists: Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous value ... [truncated]; Length shares technical record from Composing and Decomposing Data / Self-Similarity: const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); Let’s try it! length([]) //=> 0 length(["foo"]) //=> 1 length(["foo", "bar", "baz"]) (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; Argument shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; Bind shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-data]] - shared statements and technical atoms: Data shares source evidence from Composing and Decomposing Data / Self-Similarity: Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some ... [truncated]; Data shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: car(oneToFive) //=> 1 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; partial application shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-structure]] - shared statements and technical atoms: Structure shares source evidence from Composing and Decomposing Data / Self-Similarity: Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some ... [truncated]; Structure shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-reference]] - shared technical atoms: Reference shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: const node5 = [5,null], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1; (3 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical record from Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking: const length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) ); (2 shared atom(s))
- [[javascriptallonge-instead]] - shared technical atoms: Instead shares technical record from Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists: In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } }. We can then perform th ... [truncated] (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: const node5 = [5,null], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1; (2 shared atom(s))
- [[javascriptallonge-literal]] - shared technical atoms: Literal shares technical record from Composing and Decomposing Data / Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (2 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists: In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } }. We can then perform th ... [truncated] (2 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from Composing and Decomposing Data / Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (2 shared atom(s))
- [[javascriptallonge-algorithm]] - shared technical atoms: Algorithm shares technical record from Composing and Decomposing Data / Mutation / building with mutation: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node)); (1 shared atom(s))
- [[javascriptallonge-note]] - shared technical atoms: Note shares technical record from Composing and Decomposing Data / Mutation / building with mutation: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node)); (1 shared atom(s))
- [[javascriptallonge-problem]] - shared technical atoms: Problem shares technical record from Yes. Consider this variation: / Copy on Write / copy-on-read: const rest = ({first, rest}) => copy(rest); const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); ... [truncated] (1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared atom(s))
- [[javascriptallonge-seen]] - shared statements: Seen shares source evidence from Yes. Consider this variation: / Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: (1 shared statement(s))

## Source

- [[javascriptallonge]]
