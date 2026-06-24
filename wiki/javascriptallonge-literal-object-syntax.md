---
page_id: javascriptallonge-literal-object-syntax
page_kind: source
summary: literal object syntax from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.133-136
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript has a literal syntax for creating objects. This object maps values to the keys year, month, and day. Two objects created with separate evaluations have differing identities, just like arrays. Values contained within an object work just like values contained within an array, we access them by reference to the original. Names needn't be alphanumeric strings. For anything else, enclose the label in quotes. If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values. Expressions can be used for keys as well. All containers can contain any value, including functions or other containers, like a fat arrow function. Or proper functions. Or named function expressions. It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords.

## Key supported claims

- JavaScript has a literal syntax for creating objects (raw/javascriptallonge.pdf p.133-136).
- Values contained within an object work just like values contained within an array, we access them by reference to the original: (raw/javascriptallonge.pdf p.133-136).
- Two objects created with separate evaluations have differing identities, just like arrays: (raw/javascriptallonge.pdf p.133-136).

## Technical details

### `technical-atom-680343e83ec40350` code

Citation: (raw/javascriptallonge.pdf p.133-136)

```
{ year: 2012, month: 6, day: 14 }
```

### `technical-atom-d57202306c2b8fa1` code

Citation: (raw/javascriptallonge.pdf p.133-136)

```javascript
{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } //=> false Objects use [] to access the values by name, using a string: { year: 2012, month: 6, day: 14 }['day'] //=> 14
```

### `technical-atom-92dedf7638ca2aac` code

Citation: (raw/javascriptallonge.pdf p.133-136)

```javascript
const unique = () => [], x = unique(), y = unique(), z = unique(), o = { a: x, b: y, c: z }; o['a'] === x && o['b'] === y && o['c'] === z //=> true
```

### `technical-atom-a137e62b74538222` code

Citation: (raw/javascriptallonge.pdf p.133-136)

```javascript
{ 'first name': 'reginald', 'last name': 'lewis' }['first name'] //=> 'reginald'
```

### `technical-atom-94a0e83a2a574e9c` code

Citation: (raw/javascriptallonge.pdf p.133-136)

```javascript
const date = { year: 2012, month: 6, day: 14 }; date['day'] === date.day //=> true
```

### `technical-atom-d4b51c202e699d6d` code

Citation: (raw/javascriptallonge.pdf p.133-136)

```javascript
{ ["p" + "i"]: 3.14159265 } //=> {"pi":3.14159265}
```

### `technical-atom-0d3c72f7ee689a10` code

Citation: (raw/javascriptallonge.pdf p.133-136)

```javascript
const Mathematics = { abs: (a) => a < 0 ? -a : a }; Mathematics.abs(-5) //=> 5
```

### `technical-atom-6497fe28005e65d0` code

Citation: (raw/javascriptallonge.pdf p.133-136)

```javascript
const SecretDecoderRing = { encode: function (plaintext) { return plaintext .split('') .map( char => char .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); }, decode: function (cyphertext) { return cyphertext .split('') .map( char => char .charCodeAt() ) .map( code => code - 1 ) .map( code => String.fromCharCode(code) ) .join(''); } }
```

## Related technical details

### From [[javascriptallonge-plain-old-javascript-objects]]: `technical-atom-b91f3af2d19fe2cf` procedure

Relation: nearby source page; matched terms `anything`, `array`, `binding`, `can`, `else`, `javascript`

Citation: (raw/javascriptallonge.pdf p.132)

Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else.

### From [[javascriptallonge-plain-old-javascript-objects]]: `technical-atom-c8c475f5a5275af7` code

Relation: nearby source page; matched terms `can`, `javascript`, `objects`, `used`

Citation: (raw/javascriptallonge.pdf p.132)

```javascript
const remember = ["the milk", "the coffee beans", "the biscotti"]; And they can be used to store heterogeneous things in various levels of structure:
```

### From [[javascriptallonge-destructuring-objects]]: `technical-atom-2fa843b604012360` code

Relation: nearby source page; matched terms `can`, `javascript`, `name`, `objects`

Citation: (raw/javascriptallonge.pdf p.136-137)

```javascript
const user = { name: { first: "Reginald", last: "Braithwaite" }, occupation: { title: "Author", responsibilities: [ "JavaScript Allongé", "JavaScript Spessore", "CoffeeScript Ristretto" ] } }; user.name.last //=> "Braithwaite" user.occupation.title //=> "Author" And we can also write: const {name: { first: given, last: surname}, occupation: { title: title } er; surname //=> "Braithwaite" title //=> "Author"
```

### From [[javascriptallonge-destructuring-objects]]: `technical-atom-5d1c487ec919df2a` code

Relation: nearby source page; matched terms `name`, `objects`, `same`, `syntax`

Citation: (raw/javascriptallonge.pdf p.136-137)

```javascript
const description = ({name: { first }, occupation: { title } }) => ` ${ first } is a ${ title } `; description(user) //=> "Reginald is a Author" And that same syntax works for literals: {
```
