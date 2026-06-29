---
page_id: javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-literal-object-syntax-205c8f77
page_kind: source
summary: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax: 17 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-literal-object-syntax-205c8f77@d1592491fca84a1cc4fd288db4a143a2
---

# Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-bce9b969]] - broader source section: Composing and Decomposing Data / Plain Old JavaScript Objects

## Statements

- JavaScript has a literal syntax for creating objects. This object maps values to the keys year , month , and day : _(javascriptallonge.pdf (source-range-7239e085-01073))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-7239e085-01077))_
- Names needn't be alphanumeric strings. For anything else, enclose the label in quotes: _(javascriptallonge.pdf (source-range-7239e085-01079))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-7239e085-01081))_
- Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ] : _(javascriptallonge.pdf (source-range-7239e085-01083))_
- It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-7239e085-01091))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-7239e085-01077))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01077))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01074))_

```
{ year: 2012, month: 6, day: 14 }
```

### Technical frame 2: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01077))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01076))_

```
{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 }
//=> false
Objects use [] to access the values by name, using a string:
{ year: 2012, month: 6, day: 14 }['day']
//=> 14
```

### Technical frame 3: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01079))_

> Names needn't be alphanumeric strings. For anything else, enclose the label in quotes:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01078))_

```
const unique = () => [],
x = unique(),
y = unique(),
z = unique(),
o = { a: x, b: y, c: z };
o['a'] === x && o['b'] === y && o['c'] === z
//=> true
```

### Technical frame 4: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01081))_

> If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01080))_

```
{ 'first name': 'reginald', 'last name': 'lewis' }['first name']
//=> 'reginald'
```

### Technical frame 5: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01083))_

> Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ] :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01082))_

```
const date = { year: 2012, month: 6, day: 14 };
date['day'] === date.day
//=> true
```

### Technical frame 6: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01084))_

```
{
["p" + "i"]: 3.14159265
}
//=> {"pi":3.14159265}
```

### Technical frame 7: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01086))_

```
const Mathematics = {
abs: (a) => a < 0 ? -a : a
};
Mathematics.abs(-5)
//=> 5
```

### Technical frame 8: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01088))_

```
const SecretDecoderRing = {
encode: function (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode: function (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```

### Technical frame 9: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01090))_

```
const SecretDecoderRing = {
encode: function encode (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode: function decode (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```

### Technical frame 10: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01092))_

```
const SecretDecoderRing = {
encode (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```
