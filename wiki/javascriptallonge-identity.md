---
page_id: javascriptallonge-identity
page_kind: concept
page_family: topic-concept
summary: Identity: 2 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-identity@9e647bfda11efaaf7242c51801f16811
---

# Identity

What [[javascriptallonge]] covers about identity:

## Statements

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

- You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not. _(javascriptallonge.pdf (source-range-7239e085-00176))_


## Technical atoms

### Technical frame 1: Prelude: Values and Expressions over Coffee / values and identity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00118))_

> First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00116))_

<a id="atom-technical-atom-01aacee1aae7ab09"></a>

```
2 === 2
//=> true
'hello' !== 'goodbye'
//=> true
```

### Technical frame 2: Prelude: Values and Expressions over Coffee / values and identity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00120))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00119))_

<a id="atom-technical-atom-b1f3eb55cc75932a"></a>

```
2 === '2'
//=> false
true !== 'true'
//=> true
```

### Technical frame 3: Prelude: Values and Expressions over Coffee / values and identity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00120))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00121))_

<a id="atom-technical-atom-e1c132020e57e6fc"></a>

```
true === false
//=> false
2 !== 5
//=> true
'two' === 'five'
//=> false
```

### Technical frame 4: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00126))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00125))_

<a id="atom-technical-atom-af344335a7478637"></a>

```
2 + 2 === 4
//=> true
(2 + 2 === 4) === (2 !== 5)
//=> true
```

### Technical frame 5: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00129))_

> Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00127))_

<a id="atom-technical-atom-cb35e8520be9c9a9"></a>

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical frame 6: Prelude: Values and Expressions over Coffee / values and identity / reference types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00134))_

> Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42 ? Try these for yourself:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00133))_

<a id="atom-technical-atom-4a0fe9f0a2a815ee"></a>

```
[2-1, 2, 2+1]
[1, 1+1, 1+1+1]
```

### Technical frame 7: Prelude: Values and Expressions over Coffee / values and identity / reference types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00136))_

> How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . It's as if JavaScript is generating new cups of coffee with serial numbers on the bottom.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00135))_

<a id="atom-technical-atom-84f6c6969b1a1da1"></a>

```
[2-1, 2, 2+1] === [1,2,3]
[1,2,3] === [1, 2, 3]
[1, 2, 3] === [1, 2, 3]
```

### Technical frame 8: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00176))_

> You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00178))_

<a id="atom-technical-atom-103065528fb20d67"></a>

```
(() => 0) === (() => 0)
//=> false
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Prelude: Values and Expressions over Coffee / values and identity: 2 === 2 //=> true 'hello' !== 'goodbye' //=> true (6 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same cont ... [truncated]; Value shares technical record from Prelude: Values and Expressions over Coffee / values and identity: 2 === 2 //=> true 'hello' !== 'goodbye' //=> true (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-string]] - shared technical atoms: String shares technical record from Prelude: Values and Expressions over Coffee / values and identity: 2 === '2' //=> false true !== 'true' //=> true (3 shared atom(s))
- [[javascriptallonge-type]] - shared statements and technical atoms: Type shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same cont ... [truncated]; Type shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-note]] - shared technical atoms: Note shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (2 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from Prelude: Values and Expressions over Coffee / values and identity / reference types: [2-1, 2, 2+1] [1, 1+1, 1+1+1] (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: (() => 0) === (() => 0) //=> false (1 shared atom(s))

## Source

- [[javascriptallonge]]
