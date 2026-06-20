---
page_id: forewords-to-the-first-edition
page_kind: source
summary: Forewords to the first edition of JavaScript Allongé, including contributions by Michael Fogus and Matthew Knox.
sources: raw/javascriptallonge.pdf p.14-29
updated: 2026-06-19
---

## Forewords to the First Edition

This section contains the forewords to the first edition of *JavaScript Allongé*, written by Michael Fogus and Matthew Knox.

### Michael Fogus

As a life-long bibliophile and long-time follower of Reg’s online work, I was excited when he started writing books. However, I’m very conservative about books – let’s just say that if there was an aftershave scented to the essence of “Used Book Store” then I would be first in line to buy. So as you might imagine I was “skeptical” about the decision to release JavaScript Allongé as an ongoing ebook, with a pay-what-you-want model. However, Reg sent me a copy of his book and I was humbled. Not only was this a great book, but it was also a great way to write and distribute books. Having written books myself, I know the pain of soliciting and receiving feedback. 

The act of writing is an iterative process with (very often) tight revision loops. However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. On more than one occasion I’ve found myself attempting to reify feedback with content that either no longer existed or was changed beyond recognition. However, with the Leanpub model the read-feedback-change process is extremely efficient, leaving in its wake a quality book that continues to get better as others likewise read and comment into infinitude. 

In the case of JavaScript Allongé, you’ll find the Leanpub model a shining example of effectiveness. Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. No matter how much of an expert you think you are, JavaScript Allongé has something to teach you… about coffee. I kid. 

As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you’ll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. 

Enjoy. 

– Fogus, fogus.me[5] 

### Matthew Knox

A different kind of language requires a different kind of book. 

JavaScript holds surprising depths–its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many 

5http://www.fogus.me 

books try to hide most of those capabilities away, giving you recipes for writing JavaScript in a way that approximates class-centric programming in other languages. Not JavaScript Allongé. It starts with the fundamentals of values, functions, and objects, and then guides you through JavaScript from the inside with exploratory bits of code that illustrate scoping, combinators, context, state, prototypes, and constructors. 

Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it’s over too soon. Enjoy! 

–Matthew Knox, mattknox.com[6] 

> 6http://mattknox.com

## About The Sample PDF

This sample edition of the book includes just a portion of the complete book. Buying the book in progress entitles you to free updates, so download it today[7] ! Besides, **there’s really no risk at all** . If you read _JavaScript Allongé, The “six” edition_ and it doesn’t blow your mind, your money will be cheerfully refunded. 

–Reginald “Raganwald” Braithwaite, Toronto, 2015 

> 7http://leanpub.com/javascriptallongesix 

## Prelude: Values and Expressions over Coffee

The following material is extremely basic, however like most stories, the best way to begin is to start at the very beginning. 

Imagine we are visiting our favorite coffee shop. They will make for you just about any drink you desire, from a short, intense espresso ristretto through a dry cappuccino, up to those coffee-flavored desert concoctions featuring various concentrated syrups and milks. (You tolerate the existence of sugary drinks because they provide a sufficient profit margin to the establishment to finance your hanging out there all day using their WiFi and ordering a $3 drink every few hours.) 

You express your order at one end of their counter, the folks behind the counter perform their magic, and deliver the coffee you value at the other end. This is exactly how the JavaScript environment works for the purpose of this book. We are going to dispense with web servers, browsers and other complexities and deal with this simple model: You give the computer an expression[8] , and it returns a value[9] , just as you express your wishes to a barista and receive a coffee in return. 

> 8https://en.wikipedia.org/wiki/Expression_(computer_science) 

> 9https://en.wikipedia.org/wiki/Value_(computer_science) 

### Values are Expressions

All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, “I want one of these.” The barista is no fool, she gives it straight back to you, and you get exactly what you want. Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). 

Let’s try this with something the computer understands easily: 

## 42 

Is this an expression? A value? Neither? Or both? 

The answer is, this is both an expression _and_ a value.[10] The way you can tell that it’s both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano: 

## 42 

_//=> 42_ 

All values are expressions. That’s easy! Are there any other kinds of expressions? Sure! Let’s go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let’s hand over some ground coffee plus some boiling water. 

Astute readers will realize we’re omitting something. Congratulations! Take a sip of espresso. We’ll get to that in a moment. 

Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn’t a value.[11] Boiling water is a value. Ground coffee is a value. Espresso is a value. Boiling water plus ground coffee is an expression. 

Let’s try this as well with something else the computer understands easily: 

> "JavaScript" + " " + "Allonge" 

> _//=> "JavaScript Allonge"_ 

> 10Technically, it’s a _representation_ of a value using Base10 notation, but we needn’t worry about that in this book. You and I both understand that this means “42,” and so does the computer. 

> 11In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. 

### Values and Identity

In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator: 

2 === 2 _//=> true_ 'hello' !== 'goodbye' _//=> true_ 

How does === work, exactly? Imagine that you’re shown a cup of coffee. And then you’re shown another cup of coffee. Are the two cups “identical?” In JavaScript, there are four possibilities: 

First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different _types_ . For example, the string "2" is not the same thing as the number 2. Strings and numbers are different types, so strings and numbers are never identical: 

2 === '2' _//=> false_ **true** !== 'true' _//=> true_ 

Second, sometimes, the cups are of the same type—perhaps two espresso cups— but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. 

**true** === **false** _//=> false_ 2 !== 5 _//=> true_ 'two' === 'five' _//=> false_ 

What if the cups are of the same type _and_ the contents are the same? Well, JavaScript’s third and fourth possibilities cover that. 

### Value Types

Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far. 

- 2 + 2 === 4 _//=> true_ 

- (2 + 2 === 4) === (2 !== 5) _//=> true_ 

Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably. 

We haven’t encountered the fourth possibility yet. Stretching the metaphor somewhat, some types of cups have a serial number on the bottom. So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them. 

### Reference Types

So what kinds of values might be the same type and have the same contents, but not be considered identical to JavaScript? Let’s meet a data structure that is very common in contemporary programming languages, the _Array_ (other languages sometimes call it a List or a Vector). 

An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like: 

[2-1, 2, 2+1] [1, 1+1, 1+1+1] 

Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42? Try these for yourself: 

[2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] 

How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other array also looks like [1, 2, 3]. It’s as if JavaScript is generating new cups of coffee with serial numbers on the bottom. 

They look the same, but if you examine them with ===, you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. As we’ll see, this is true of many other kinds of values, including _functions_ , the main subject of this book.

## A Rich Aroma: Basic Numbers

In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.— Wikipedia[12] 

JavaScript, like most languages, has a collection of literals. We saw that an expression consisting solely of numbers, like 42, is a literal. It represents the number forty-two, which is 42 base 10. Not 

> 12https://en.wikipedia.org/wiki/Literal_(computer_programming) 

### Floating Point Numbers

Most programmers never encounter the limit on the magnitude of an integer. But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers. 

It’s tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, “Noooooo.” A computer’s internal representation for a floating point number is binary, while our literal number was in base ten. This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. 

One of the most oft-repeated examples is this: 

- 1.0 _//=> 1_ 

- 1.0 + 1.0 _//=> 2_ 

- 1.0 + 1.0 + 1.0 _//=> 3_ 

However: 

> 13http://en.wikipedia.org/wiki/Double-precision_floating-point_format 

> 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. 

### Operations on Numbers

As we’ve seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 - 34 or even 6 / 2. These can be combined to make more complex expressions, like 2 * 5 + 1. 

In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: 

2 * 5 + 1 _//=> 11_ 1 + 5 * 2 _//=> 11_ 

JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2), because the * operator has a _higher precedence_ than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus, of course). 

In addition to the common +, -, *, and /, JavaScript also supports modulus, %, and unary negation, -: 

15https://en.wikipedia.org/wiki/IEEE_floating_point 

## The First Sip: Basic Functions



**Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia**
