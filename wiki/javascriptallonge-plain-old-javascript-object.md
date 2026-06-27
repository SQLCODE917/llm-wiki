---
page_id: javascriptallonge-plain-old-javascript-object
page_kind: concept
summary: Plain Old JavaScript Objects: 30 statement(s) and 30 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-plain-old-javascript-object@93f3b420167c6089a7d9ca4dadc37789
---

# Plain Old JavaScript Objects

What [[javascriptallonge]] covers about plain old javascript objects:

## Statements

- JavaScript has dictionaries, and it calls them “objects.” The word “object” is loaded in programming circles, due to the widespread use of the term “object-oriented programming” that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-83ecb080-01584))_
- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-83ecb080-01590))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-83ecb080-01585))_
- Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-83ecb080-01575))_
- Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary[69] data type, a mapping from a unique set of objects to another set of objects. _(javascriptallonge.pdf (source-range-83ecb080-01582))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-83ecb080-01596))_
- It is very common to associate named function expressions with keys in objects, and there is a “compact method syntax” for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-83ecb080-01618))_
- It is very common to write things like title: title when destructuring objects. _(javascriptallonge.pdf (source-range-83ecb080-01636))_
- But now that we’ve looked at objects, we can use an object instead of a two-element array. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-83ecb080-01579))_
- Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. _(javascriptallonge.pdf (source-range-83ecb080-01579))_
- Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0]. _(javascriptallonge.pdf (source-range-83ecb080-01582))_
- Names needn’t be alphanumeric strings. _(javascriptallonge.pdf (source-range-83ecb080-01602))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-83ecb080-01604))_

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


## Source

- [[javascriptallonge]]
