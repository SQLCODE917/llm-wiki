---
page_id: javascriptallonge-section-prelude-values-and-expressions-over-coffee-3ba31fb1
page_kind: source
page_family: section-reference
summary: Prelude: Values and Expressions over Coffee: 47 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-prelude-values-and-expressions-over-coffee-3ba31fb1@bd1828008ccb9ed7b701462bc26e755a
---

# Prelude: Values and Expressions over Coffee

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-and-identity-7389665c]] - narrower source section: Prelude: Values and Expressions over Coffee / values and identity
- [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-are-expressions-439d7791]] - narrower source section: Prelude: Values and Expressions over Coffee / values are expressions

## Statements by subsection

### Prelude: Values and Expressions over Coffee / values are expressions

- All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, 'I want one of these.' The barista is no fool, she gives it straight back to you, and you get exactly what you want. Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-7239e085-00101))_
- The answer is, this is both an expression and a value. 10 The way you can tell that it's both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano: _(javascriptallonge.pdf (source-range-7239e085-00105))_
- All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water. _(javascriptallonge.pdf (source-range-7239e085-00107))_
- Astute readers will realize we're omitting something. Congratulations! Take a sip of espresso. We'll get to that in a moment. _(javascriptallonge.pdf (source-range-7239e085-00108))_
- Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn't a value. 11 Boiling water is a value. Ground coffee is a value. Espresso is a value. Boiling water plus ground coffee is an expression. _(javascriptallonge.pdf (source-range-7239e085-00109))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-7239e085-00101))_

### Prelude: Values and Expressions over Coffee / values and identity

- First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical: _(javascriptallonge.pdf (source-range-7239e085-00118))_
- Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-7239e085-00120))_
- For example, the string "2" is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-7239e085-00118))_
- This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-7239e085-00120))_

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

### Technical frame 1: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00107))_

> All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00106))_

<a id="atom-technical-atom-51c8d8435d99be90"></a>

```
42
//=> 42
```

### Technical frame 2: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00108))_

> Astute readers will realize we're omitting something. Congratulations! Take a sip of espresso. We'll get to that in a moment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00109))_

<a id="atom-technical-atom-eec8b1329c6317b1"></a>

> And if we hand over the espresso, we get the espresso right back.

### Technical frame 3: Prelude: Values and Expressions over Coffee / values and identity / value types

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

### Technical frame 4: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00129))_

> Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00127))_

<a id="atom-technical-atom-cb35e8520be9c9a9"></a>

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical frame 5: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00129))_

> Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00128))_

<a id="atom-technical-atom-4738eb9ff674c3cd"></a>

> [Figure] (p.22)

### Technical atom 6

<a id="atom-technical-atom-0f636362d664d880"></a>

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00099))_

```text
Prelude: Values and Expressions over Coffee
The following material is extremely basic, however like most stories, the best way to begin is to start at the very beginning.
Imagine we are visiting our favourite coffee shop. They will make for you just about any drink you desire, from a short, intense espresso ristretto through a dry cappuccino, up to those coffee-flavoured desert concoctions featuring various concentrated syrups and milks. (You tolerate the existence of sugary drinks because they provide a sufficient profit margin to the establishment to finance your hanging out there all day using their WiFi and ordering a $3 drink every few hours.)
You express your order at one end of their counter, the folks behind the counter perform their magic, and deliver the coffee you value at the other end. This is exactly how the JavaScript environment works for the purpose of this book. We are going to dispense with web servers, browsers and other complexities and deal with this simple model: You give the computer an expression 8 , and it returns a value 9 , just as you express your wishes to a barista and receive a coffee in return.
8 https://en.wikipedia.org/wiki/Expression_
9 https://en.wikipedia.org/wiki/Value_
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 8 | https://en.wikipedia.org/wiki/Expression_ |
| 9 | https://en.wikipedia.org/wiki/Value_ |

</details>

### Technical atom 7

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
