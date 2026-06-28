---
page_id: javascriptallonge-section-values-are-expressions-be8dc025
page_kind: source
summary: values are expressions: 18 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-be8dc025@d2027045f400332815b6f9e73511134a
---

# values are expressions

From [[javascriptallonge]].

## Statements

- All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, 'I want one of these.' The barista is no fool, she gives it straight back to you, and you get exactly what you want. Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-31a4cf47-00105))_
- The answer is, this is both an expression and a value. 10 The way you can tell that it's both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano: _(javascriptallonge.pdf (source-range-31a4cf47-00109))_
- All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water. _(javascriptallonge.pdf (source-range-31a4cf47-00111))_
- Astute readers will realize we're omitting something. Congratulations! Take a sip of espresso. We'll get to that in a moment. _(javascriptallonge.pdf (source-range-31a4cf47-00112))_
- Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn't a value. 11 Boiling water is a value. Ground coffee is a value. Espresso is a value. Boiling water plus ground coffee is an expression. _(javascriptallonge.pdf (source-range-31a4cf47-00113))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-31a4cf47-00105))_

## Technical atoms

### Technical frame 1: values are expressions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00111))_

> All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00109))_

> 10 The way you can tell that it's both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano:

### Technical frame 2: values are expressions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00111))_

> All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00110))_

```
42 //=> 42
```

### Technical frame 3: values are expressions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00112))_

> Astute readers will realize we're omitting something. Congratulations! Take a sip of espresso. We'll get to that in a moment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00113))_

> And if we hand over the espresso, we get the espresso right back.

### Technical frame 4: values are expressions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00113))_

> Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn't a value. 11 Boiling water is a value. Ground coffee is a value. Espresso is a value. Boiling water plus ground coffee is an expression.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00115))_

```
"JavaScript" + " " + "Allonge" //=> "JavaScript Allonge"
```

### Technical frame 5: values are expressions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00113))_

> Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn't a value. 11 Boiling water is a value. Ground coffee is a value. Espresso is a value. Boiling water plus ground coffee is an expression.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00117))_

> Nowwesee that 'strings' are values, and you can make an expression out of strings and an operator + . Since strings are values, they are also expressions by themselves. But strings with operators are not values, they are expressions. Now we know what was missing with our 'coffee grounds plus hot water' example. The coffee grounds were a value, the boiling hot water was a value, and the 'plus' operator between them made the whole thing an expression that was not a value.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00114))_

> Let's try this as well with something else the computer understands easily:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00116))_

| entry | content |
| --- | --- |
| 10 | Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer. |
| 11 | In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. |

<details>
<summary>Raw table text</summary>

```
10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer.
11 In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values.
```

</details>
