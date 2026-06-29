---
page_id: javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-and-identity-7389665c
page_kind: source
summary: Prelude: Values and Expressions over Coffee / values and identity: 29 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-and-identity-7389665c@2fe172317503e484a4891e3b62223ac0
---

# Prelude: Values and Expressions over Coffee / values and identity

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-3ba31fb1]] - broader source section: Prelude: Values and Expressions over Coffee
- [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-and-identity-value-types-eb382c99]] - narrower source section: Prelude: Values and Expressions over Coffee / values and identity / value types
- [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-and-identity-reference-types-00ce938b]] - narrower source section: Prelude: Values and Expressions over Coffee / values and identity / reference types

## Statements

- First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical: _(javascriptallonge.pdf (source-range-7239e085-00118))_
- Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-7239e085-00120))_
- For example, the string "2" is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-7239e085-00118))_
- This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-7239e085-00120))_

## Statements by subsection

### Prelude: Values and Expressions over Coffee / values and identity / value types

- Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far. _(javascriptallonge.pdf (source-range-7239e085-00124))_
- Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably. _(javascriptallonge.pdf (source-range-7239e085-00126))_
- We haven't encountered the fourth possibility yet. Stretching the metaphor somewhat, some types of cups have a serial number on the bottom. So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them. _(javascriptallonge.pdf (source-range-7239e085-00127))_
- Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia _(javascriptallonge.pdf (source-range-7239e085-00129))_

### Prelude: Values and Expressions over Coffee / values and identity / reference types

- An array looks like this: [1, 2, 3] . This is an expression, and you can combine [] with other expressions. Go wild with things like: _(javascriptallonge.pdf (source-range-7239e085-00132))_
- Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42 ? Try these for yourself: _(javascriptallonge.pdf (source-range-7239e085-00134))_
- How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . It's as if JavaScript is generating new cups of coffee with serial numbers on the bottom. _(javascriptallonge.pdf (source-range-7239e085-00136))_
- They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. _(javascriptallonge.pdf (source-range-7239e085-00137))_

## Technical atoms

### Technical frame 1: Prelude: Values and Expressions over Coffee / values and identity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00118))_

> First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00116))_

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

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical frame 6: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00129))_

> Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00128))_

> [Figure] (p.22)

### Technical frame 7: Prelude: Values and Expressions over Coffee / values and identity / reference types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00134))_

> Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42 ? Try these for yourself:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00133))_

```
[2-1, 2, 2+1]
[1, 1+1, 1+1+1]
```

### Technical frame 8: Prelude: Values and Expressions over Coffee / values and identity / reference types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00136))_

> How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . It's as if JavaScript is generating new cups of coffee with serial numbers on the bottom.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00135))_

```
[2-1, 2, 2+1] === [1,2,3]
[1,2,3] === [1, 2, 3]
[1, 2, 3] === [1, 2, 3]
```
