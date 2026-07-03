---
page_id: javascriptallonge-needn
page_kind: concept
page_family: topic-concept
summary: Needn: 4 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-needn@4579fea5095d31fb54f0a268e75881d0
---

# Needn

What [[javascriptallonge]] covers about needn:

## Statements

### And also: / Building Blocks

- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-7239e085-00580))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere

- 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript's built-in arrays work. _(javascriptallonge.pdf (source-range-7239e085-01026))_

### Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

- Names needn't be alphanumeric strings. For anything else, enclose the label in quotes: _(javascriptallonge.pdf (source-range-7239e085-01079))_

### Like this: / ordered collections

- Iterables needn't represent ordered collections. We could make an infinite iterable representing random numbers: _(javascriptallonge.pdf (source-range-7239e085-01582))_


## Technical atoms

### Technical frame 1: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00588))_

> Of course, you needn't use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00589))_

<a id="atom-technical-atom-4a47a493fe1f06cd"></a>

```
const actuallyTransfer= (from, to, amount) =>
// do something
const invokeTransfer = once(maybe(actuallyTransfer(...)));
```

### Technical frame 2: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01081))_

> If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01080))_

<a id="atom-technical-atom-36bfd850e76f973d"></a>

```
{ 'first name': 'reginald', 'last name': 'lewis' }['first name']
//=> 'reginald'
```

### Technical frame 3: Like this: / ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01584))_

> Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01583))_

<a id="atom-technical-atom-abc21aecdd5f4a68"></a>

```
const RandomNumbers = {
[Symbol.iterator]: () =>
({
next () {
return {value: Math.random()};
}
})
}
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.494052127469331
0.835459444206208
0.1408337657339871
...
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.7845381607767195
0.4956772483419627
0.20259276474826038
...
```

### Technical atom 4

<a id="atom-technical-atom-08860569e8259d48"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00110))_

> Let's try this as well with something else the computer understands easily:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00112))_

```text
10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer.
11 In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 10 | Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer. |
| 11 | In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. |

</details>


## Related pages

### Shared technical atoms

- [[javascriptallonge-coffee]] - shared technical atoms: Coffee shares technical table: 10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' ... [truncated] (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical table: 10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' ... [truncated] (1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from Like this: / ordered collections: const RandomNumbers = { [Symbol.iterator]: () => ({ next () { return {value: Math.random()}; } }) } for (const i of RandomNumbers) { console.log(i) } //=> 0.49405212 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical table: 10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' ... [truncated] (1 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical table: 10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' ... [truncated] (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical table: 10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' ... [truncated] (1 shared atom(s))

### Shared claims

- [[javascriptallonge-alway]] - shared statements: Alway shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere: 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share c ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from And also: / Building Blocks: When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. Th ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
