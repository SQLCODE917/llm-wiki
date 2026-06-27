---
page_id: javascriptallonge-section-plain-old-javascript-objects-c5b21e2a
page_kind: source
summary: Plain Old JavaScript Objects: 69 source-backed entries and 30 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-plain-old-javascript-objects-c5b21e2a@7c0958e763e0670c229eb64ec2f9b7f5
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

> Context: Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01575))_

> **const** remember = ["the milk", "the coffee beans", "the biscotti"];
_(source: javascriptallonge.pdf (source-range-83ecb080-01576))_

> Context: And they can be used to store heterogeneous things in various levels of structure:
_(context: javascriptallonge.pdf (source-range-83ecb080-01577))_

> **const** user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];
_(source: javascriptallonge.pdf (source-range-83ecb080-01578))_

> Context: Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:
_(context: javascriptallonge.pdf (source-range-83ecb080-01579))_

> **const** NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1;
_(source: javascriptallonge.pdf (source-range-83ecb080-01580))_

> Context: Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:
_(context: javascriptallonge.pdf (source-range-83ecb080-01579))_

> **const** user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];
_(source: javascriptallonge.pdf (source-range-83ecb080-01581))_

> Context: Two objects created with separate evaluations have differing identities, just like arrays:
_(context: javascriptallonge.pdf (source-range-83ecb080-01592))_

> - { year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } _//=> false_
_(source: javascriptallonge.pdf (source-range-83ecb080-01593))_

> Context: Objects use [] to access the values by name, using a string:
_(context: javascriptallonge.pdf (source-range-83ecb080-01594))_

> - { year: 2012, month: 6, day: 14 }['day'] _//=> 14_
_(source: javascriptallonge.pdf (source-range-83ecb080-01595))_

> Context: Values contained within an object work just like values contained within an array, we access them by reference to the original:
_(context: javascriptallonge.pdf (source-range-83ecb080-01596))_

> - x = unique(),
_(source: javascriptallonge.pdf (source-range-83ecb080-01598))_

> Context: Values contained within an object work just like values contained within an array, we access them by reference to the original:
_(context: javascriptallonge.pdf (source-range-83ecb080-01596))_

> - y = unique(),
_(source: javascriptallonge.pdf (source-range-83ecb080-01599))_

> - z = unique(), o = { a: x, b: y, c: z };
_(source: javascriptallonge.pdf (source-range-83ecb080-01600))_

> - o['a'] === x && o['b'] === y && o['c'] === z _//=> true_
_(source: javascriptallonge.pdf (source-range-83ecb080-01601))_

> Context: If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values:
_(context: javascriptallonge.pdf (source-range-83ecb080-01604))_

> **const** date = { year: 2012, month: 6, day: 14 };
_(source: javascriptallonge.pdf (source-range-83ecb080-01607))_

> date['day'] === date.day _//=> true_
_(source: javascriptallonge.pdf (source-range-83ecb080-01608))_

> Context: Expressions can be used for keys as well. The syntax is to enclose the key’s expression in [ and ]:
_(context: javascriptallonge.pdf (source-range-83ecb080-01609))_

> { ["p" + "i"]: 3.14159265 } _//=> {"pi":3.14159265}_
_(source: javascriptallonge.pdf (source-range-83ecb080-01610))_

> Context: All containers can contain any value, including functions or other containers, like a fat arrow function:
_(context: javascriptallonge.pdf (source-range-83ecb080-01611))_

> **const** Mathematics = { abs: (a) => a < 0 ? -a : a }; Mathematics.abs(-5) _//=> 5_
_(source: javascriptallonge.pdf (source-range-83ecb080-01612))_

> Context: And we can also write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01627))_

> surname _//=> "Braithwaite"_ title _//=> "Author"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01629))_

> Context: Terrible grammar and capitalization, but let’s move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it’s often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:
_(context: javascriptallonge.pdf (source-range-83ecb080-01636))_

> **const** description = ({name: { first }, occupation: { title } }) => ` **${** first **}** is a **${** title **}** `;
_(source: javascriptallonge.pdf (source-range-83ecb080-01637))_

> Context: And that same syntax works for literals:
_(context: javascriptallonge.pdf (source-range-83ecb080-01640))_

> **const** abbrev = ({name: { first, last }, occupation: { title } }) => { **return** { first, last, title}; } abbrev(user)
_(source: javascriptallonge.pdf (source-range-83ecb080-01641))_

> Context: Earlier, we used two-element arrays as nodes in a linked list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01644))_

> **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
_(source: javascriptallonge.pdf (source-range-83ecb080-01645))_

> Context: We can then perform the equivalent of [first, ...rest] with direct property accessors:
_(context: javascriptallonge.pdf (source-range-83ecb080-01648))_

> **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };
_(source: javascriptallonge.pdf (source-range-83ecb080-01651))_

> OneTwoThree.first _//=> 1_ OneTwoThree.rest _//=> {"first":2,"rest":{"first":3,"rest":{}}}_
_(source: javascriptallonge.pdf (source-range-83ecb080-01652))_

> OneTwoThree.rest.rest.first _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-01653))_

> Context: Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-01655))_

> Context: Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> length(OneTwoThree) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-01656))_

> Context: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01657))_

> **const** slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)};
_(source: javascriptallonge.pdf (source-range-83ecb080-01658))_

> Context: We could follow the strategy of delaying the work. Let’s write that naively:
_(context: javascriptallonge.pdf (source-range-83ecb080-01662))_

> **const** copy2 = (node, delayed = EMPTY) => node === EMPTY
_(source: javascriptallonge.pdf (source-range-83ecb080-01665))_

> Context: Well, well, well. We have unwittingly _reversed_ the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. This isn’t a bad thing by any stretch of the imagination. Let’s call it what it is:
_(context: javascriptallonge.pdf (source-range-83ecb080-01669))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });
_(source: javascriptallonge.pdf (source-range-83ecb080-01670))_

> Context: And now, we can make a reversing map:
_(context: javascriptallonge.pdf (source-range-83ecb080-01671))_

> **const** reverseMapWith = (fn, node, delayed = EMPTY) => node === EMPTY
_(source: javascriptallonge.pdf (source-range-83ecb080-01672))_

> Context: And a regular mapWith follows:
_(context: javascriptallonge.pdf (source-range-83ecb080-01674))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });
_(source: javascriptallonge.pdf (source-range-83ecb080-01675))_

> Context: And a regular mapWith follows:
_(context: javascriptallonge.pdf (source-range-83ecb080-01674))_

> **const** mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
_(source: javascriptallonge.pdf (source-range-83ecb080-01676))_

> Context: And a regular mapWith follows:
_(context: javascriptallonge.pdf (source-range-83ecb080-01674))_

> mapWith((x) => x * x, OneTwoThree) _//=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}_
_(source: javascriptallonge.pdf (source-range-83ecb080-01677))_
