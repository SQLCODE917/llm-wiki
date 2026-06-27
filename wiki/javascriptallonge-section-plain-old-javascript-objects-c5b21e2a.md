---
page_id: javascriptallonge-section-plain-old-javascript-objects-c5b21e2a
page_kind: source
summary: Plain Old JavaScript Objects: 69 source-backed entries and 30 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-plain-old-javascript-objects-c5b21e2a@dda6a36d78887601bf7f778ffa4b36ae
---

# Plain Old JavaScript Objects

From [[javascriptallonge]].

## Statements

- Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-83ecb080-01575))_
- Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-83ecb080-01575))_
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-83ecb080-01579))_
- Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. _(javascriptallonge.pdf (source-range-83ecb080-01579))_
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-83ecb080-01579))_
- Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0]. _(javascriptallonge.pdf (source-range-83ecb080-01582))_
- Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary[69] data type, a mapping from a unique set of objects to another set of objects. _(javascriptallonge.pdf (source-range-83ecb080-01582))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0, we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-83ecb080-01583))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0, we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-83ecb080-01583))_
- JavaScript has dictionaries, and it calls them “objects.” The word “object” is loaded in programming circles, due to the widespread use of the term “object-oriented programming” that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-83ecb080-01584))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-83ecb080-01585))_
- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-83ecb080-01590))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-83ecb080-01596))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-83ecb080-01596))_
- Names needn’t be alphanumeric strings. _(javascriptallonge.pdf (source-range-83ecb080-01602))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-83ecb080-01604))_
- Expressions can be used for keys as well. _(javascriptallonge.pdf (source-range-83ecb080-01609))_
- It is very common to associate named function expressions with keys in objects, and there is a “compact method syntax” for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-83ecb080-01618))_
- (There are some other technical differences between binding a named function expression and using _(javascriptallonge.pdf (source-range-83ecb080-01620))_
- compact method syntax, but they are not relevant here. _(javascriptallonge.pdf (source-range-83ecb080-01623))_
- It is very common to write things like title: title when destructuring objects. _(javascriptallonge.pdf (source-range-83ecb080-01636))_
- When the label is a valid variable name, it’s often the most obvious variable name as well. _(javascriptallonge.pdf (source-range-83ecb080-01636))_
- But now that we’ve looked at objects, we can use an object instead of a two-element array. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- In essence, this simple implementation used functions to create an abstraction with named elements. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- While we’re at it, let’s use contemporary names. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. _(javascriptallonge.pdf (source-range-83ecb080-01657))_
- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- We could follow the strategy of delaying the work. _(javascriptallonge.pdf (source-range-83ecb080-01662))_
- We have unwittingly _reversed_ the list. _(javascriptallonge.pdf (source-range-83ecb080-01669))_
- This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. _(javascriptallonge.pdf (source-range-83ecb080-01669))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-83ecb080-01680))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-83ecb080-01680))_
- Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. _(javascriptallonge.pdf (source-range-83ecb080-01680))_
- Mind you, this is still much, much faster than making partial copies of arrays. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
- For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
- Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
- Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01575))_

> Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01576))_

> **const** remember = ["the milk", "the coffee beans", "the biscotti"];

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01577))_

> And they can be used to store heterogeneous things in various levels of structure:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01578))_

> **const** user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01579))_

> Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01580))_

> **const** NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1;

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01579))_

> Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01581))_

> **const** user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01592))_

> Two objects created with separate evaluations have differing identities, just like arrays:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01593))_

> - { year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } _//=> false_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01594))_

> Objects use [] to access the values by name, using a string:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01595))_

> - { year: 2012, month: 6, day: 14 }['day'] _//=> 14_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01596))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01598))_

> - x = unique(),

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01596))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01599))_

> - y = unique(),

### Technical atom 9

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01600))_

> - z = unique(), o = { a: x, b: y, c: z };

### Technical atom 10

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01601))_

> - o['a'] === x && o['b'] === y && o['c'] === z _//=> true_

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01604))_

> If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01607))_

> **const** date = { year: 2012, month: 6, day: 14 };

### Technical atom 12

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01608))_

> date['day'] === date.day _//=> true_

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01609))_

> Expressions can be used for keys as well. The syntax is to enclose the key’s expression in [ and ]:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01610))_

> { ["p" + "i"]: 3.14159265 } _//=> {"pi":3.14159265}_

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01611))_

> All containers can contain any value, including functions or other containers, like a fat arrow function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01612))_

> **const** Mathematics = { abs: (a) => a < 0 ? -a : a }; Mathematics.abs(-5) _//=> 5_

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01627))_

> And we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01629))_

> surname _//=> "Braithwaite"_ title _//=> "Author"_

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01636))_

> Terrible grammar and capitalization, but let’s move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it’s often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01637))_

> **const** description = ({name: { first }, occupation: { title } }) => ` **${** first **}** is a **${** title **}** `;

### Technical atom 17

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01640))_

> And that same syntax works for literals:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01641))_

> **const** abbrev = ({name: { first, last }, occupation: { title } }) => { **return** { first, last, title}; } abbrev(user)

### Technical atom 18

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01644))_

> Earlier, we used two-element arrays as nodes in a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01645))_

> **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;

### Technical atom 19

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01648))_

> We can then perform the equivalent of [first, ...rest] with direct property accessors:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01651))_

> **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };

### Technical atom 20

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01652))_

> OneTwoThree.first _//=> 1_ OneTwoThree.rest _//=> {"first":2,"rest":{"first":3,"rest":{}}}_

### Technical atom 21

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01653))_

> OneTwoThree.rest.rest.first _//=> 3_

### Technical atom 22

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01655))_

> **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);

### Technical atom 23

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01656))_

> length(OneTwoThree) _//=> 3_

### Technical atom 24

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01657))_

> What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01658))_

> **const** slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)};

### Technical atom 25

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01662))_

> We could follow the strategy of delaying the work. Let’s write that naively:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01665))_

> **const** copy2 = (node, delayed = EMPTY) => node === EMPTY

### Technical atom 26

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01669))_

> Well, well, well. We have unwittingly _reversed_ the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. This isn’t a bad thing by any stretch of the imagination. Let’s call it what it is:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01670))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });

### Technical atom 27

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01671))_

> And now, we can make a reversing map:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01672))_

> **const** reverseMapWith = (fn, node, delayed = EMPTY) => node === EMPTY

### Technical atom 28

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01674))_

> And a regular mapWith follows:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01675))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });

### Technical atom 29

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01674))_

> And a regular mapWith follows:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01676))_

> **const** mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });

### Technical atom 30

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01674))_

> And a regular mapWith follows:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01677))_

> mapWith((x) => x * x, OneTwoThree) _//=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}_
