---
page_id: javascriptallonge-section-literal-object-syntax-e81da492
page_kind: source
summary: literal object syntax: 17 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-literal-object-syntax-e81da492@ac7d7b3eb3098737776c2c8bdf368de9
---

# literal object syntax

From [[javascriptallonge]].

## Statements

- JavaScript has a literal syntax for creating objects. This object maps values to the keys year , month , and day : _(javascriptallonge.pdf (source-range-8eb13d6b-01072))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-8eb13d6b-01076))_
- Names needn't be alphanumeric strings. For anything else, enclose the label in quotes: _(javascriptallonge.pdf (source-range-8eb13d6b-01078))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-8eb13d6b-01080))_
- Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ] : _(javascriptallonge.pdf (source-range-8eb13d6b-01082))_
- It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-8eb13d6b-01090))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-8eb13d6b-01076))_

## Technical atoms

### Technical frame 1: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01076))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01073))_

```
{ year: 2012, month: 6, day: 14 }
```

### Technical frame 2: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01076))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01075))_

```
{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } //=> false Objects use [] to access the values by name, using a string: { year: 2012, month: 6, day: 14 }['day'] //=> 14
```

### Technical frame 3: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01078))_

> Names needn't be alphanumeric strings. For anything else, enclose the label in quotes:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01077))_

```
const unique = () => [], x = unique(), y = unique(), z = unique(), o = { a: x, b: y, c: z }; o['a'] === x && o['b'] === y && o['c'] === z //=> true
```

### Technical frame 4: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01080))_

> If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01079))_

```
{ 'first name': 'reginald', 'last name': 'lewis' }['first name'] //=> 'reginald'
```

### Technical frame 5: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01082))_

> Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ] :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01081))_

```
const date = { year: 2012, month: 6, day: 14 }; date['day'] === date.day //=> true
```

### Technical frame 6: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01090))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01083))_

```
{ ["p" + "i"]: 3.14159265 } //=> {"pi":3.14159265}
```

### Technical frame 7: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01090))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01085))_

```
const Mathematics = { abs: (a) => a < 0 ? -a : a }; Mathematics.abs(-5) //=> 5
```

### Technical frame 8: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01090))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01087))_

```
const SecretDecoderRing = { encode: function (plaintext) { return plaintext .split('') .map( char => char .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); }, decode: function (cyphertext) { return cyphertext .split('') .map( char => char .charCodeAt() ) .map( code => code - 1 ) .map( code => String.fromCharCode(code) ) .join(''); } }
```

### Technical frame 9: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01090))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01089))_

```
const SecretDecoderRing = { encode: function encode (plaintext) { return plaintext .split('') .map( char => char .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); }, decode: function decode (cyphertext) { return cyphertext .split('') .map( char => char .charCodeAt() ) .map( code => code - 1 ) .map( code => String.fromCharCode(code) ) .join(''); } }
```

### Technical frame 10: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01090))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01091))_

```
const SecretDecoderRing = { encode (plaintext) { return plaintext .split('') .map( char => char .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); }, decode (cyphertext) { return cyphertext .split('') .map( char => char .charCodeAt() ) .map( code => code - 1 ) .map( code => String.fromCharCode(code) ) .join(''); } }
```
