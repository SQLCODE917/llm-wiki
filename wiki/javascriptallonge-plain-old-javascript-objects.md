---
page_id: javascriptallonge-plain-old-javascript-objects
page_kind: source
summary: Plain Old JavaScript Objects from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.132-132
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé explores the fundamentals and advanced techniques of JavaScript, with a focus on functional programming and the manipulation of objects.

## Key supported claims

- JavaScript has dictionaries, and it calls them 'objects.' The word 'object' is loaded in programming circles, due to the widespread use of the term 'object-oriented programming' that was coined by Alan Kay but has since come to mean many, many things to many different people. (raw/javascriptallonge.pdf p.132-132)
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0, we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. (raw/javascriptallonge.pdf p.132-132)
- Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary data type, a mapping from a unique set of objects to another set of objects. (raw/javascriptallonge.pdf p.132-132)
- In JavaScript, an object is a map from string keys to values. (raw/javascriptallonge.pdf p.132-132)

## Technical details

### `technical-atom-c8c475f5a5275af7` code

Citation: (raw/javascriptallonge.pdf p.132)

```javascript
const remember = ["the milk", "the coffee beans", "the biscotti"]; And they can be used to store heterogeneous things in various levels of structure:
```

### `technical-atom-063ccafb474926a9` code

Citation: (raw/javascriptallonge.pdf p.132)

```javascript
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### `technical-atom-08c736021f08b986` code

Citation: (raw/javascriptallonge.pdf p.132)

```javascript
const NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1; const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### `technical-atom-b91f3af2d19fe2cf` procedure

Citation: (raw/javascriptallonge.pdf p.132)

Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else.

### `technical-atom-d529e9b6bf45d57d` exception

Citation: (raw/javascriptallonge.pdf p.132)

Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer.

### `technical-atom-e68ed5f2813f1fee` exception

Citation: (raw/javascriptallonge.pdf p.132)

So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

## Related technical details

### From [[javascriptallonge-destructuring-objects]]: `technical-atom-2fa843b604012360` code

Relation: nearby source page; matched terms `allong`, `can`, `javascript`, `name`, `objects`

Citation: (raw/javascriptallonge.pdf p.136-137)

```javascript
const user = { name: { first: "Reginald", last: "Braithwaite" }, occupation: { title: "Author", responsibilities: [ "JavaScript Allongé", "JavaScript Spessore", "CoffeeScript Ristretto" ] } }; user.name.last //=> "Braithwaite" user.occupation.title //=> "Author" And we can also write: const {name: { first: given, last: surname}, occupation: { title: title } er; surname //=> "Braithwaite" title //=> "Author"
```

### From [[javascriptallonge-literal-object-syntax]]: `technical-atom-d57202306c2b8fa1` code

Relation: nearby source page; matched terms `access`, `name`, `object`, `objects`, `string`, `use`

Citation: (raw/javascriptallonge.pdf p.133-136)

```javascript
{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } //=> false Objects use [] to access the values by name, using a string: { year: 2012, month: 6, day: 14 }['day'] //=> 14
```

### From [[javascriptallonge-garbage-garbage-everywhere]]: `technical-atom-5d1ebb19d843b288` procedure

Relation: nearby source page; matched terms `array`, `procedure`, `then`, `time`, `use`

Citation: (raw/javascriptallonge.pdf p.126-128)

Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend .

### From [[javascriptallonge-garbage-garbage-everywhere]]: `technical-atom-ff30dd9aed90995c` exception

Relation: nearby source page; matched terms `data`, `structures`

Citation: (raw/javascriptallonge.pdf p.126-128)

64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made.
