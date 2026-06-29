---
page_id: javascriptallonge-section-recipes-with-data-178f0a89
page_kind: source
summary: Recipes with Data: 53 source-backed entries and 31 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-178f0a89@069069f2d82afe62fe4034efb3b65472
---

# Recipes with Data

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-data-disclaimer-92143eef]] - narrower source section: Recipes with Data / Disclaimer
- [[javascriptallonge-section-recipes-with-data-mapwith-588e9415]] - narrower source section: Recipes with Data / mapWith
- [[javascriptallonge-section-recipes-with-data-flip-2cae94c7]] - narrower source section: Recipes with Data / Flip
- [[javascriptallonge-section-recipes-with-data-object-assign-c62f7bb5]] - narrower source section: Recipes with Data / Object.assign
- [[javascriptallonge-section-recipes-with-data-why-d85ef4c4]] - narrower source section: Recipes with Data / Why?

## Statements by subsection

### Recipes with Data / Disclaimer

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-7239e085-01428))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-7239e085-01428))_
- The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-7239e085-01428))_

### Recipes with Data / mapWith

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map : _(javascriptallonge.pdf (source-range-7239e085-01437))_
- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-7239e085-01440))_
- If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result: _(javascriptallonge.pdf (source-range-7239e085-01442))_
- Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-7239e085-01444))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-7239e085-01437))_

### Recipes with Data / Flip

- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry : _(javascriptallonge.pdf (source-range-7239e085-01462))_
- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-7239e085-01462))_

### Recipes with Data / Flip / self-currying flip

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip : _(javascriptallonge.pdf (source-range-7239e085-01466))_

### Recipes with Data / Flip / flipping methods

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done: _(javascriptallonge.pdf (source-range-7239e085-01470))_

### Recipes with Data / Object.assign

- Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object: _(javascriptallonge.pdf (source-range-7239e085-01477))_

### Recipes with Data / Why?

- Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names. _(javascriptallonge.pdf (source-range-7239e085-01489))_
- So again, why include the recipe? Well, besides all of the practical applications that combinators provide, there is this little thing called The joy of working things out. _(javascriptallonge.pdf (source-range-7239e085-01490))_
- There are many explanations of the Y Combinator's mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. Use it as an excuse to get familiar with your environment's debugging facility. _(javascriptallonge.pdf (source-range-7239e085-01491))_
- One tip is to use JavaScript to name things. For example, you could start by writing: _(javascriptallonge.pdf (source-range-7239e085-01492))_
- What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-7239e085-01494))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-7239e085-01494))_

## Technical atoms

### Technical frame 1: Recipes with Data

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01425))_

> [Figure] (p.191)

### Technical frame 2: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01437))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01430))_

> In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:

### Technical frame 3: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01437))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01431))_

```
[1, 2, 3, 4, 5].map(x => x * x)
//=> [1, 4, 9, 16, 25]
```

### Technical frame 4: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01437))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01433))_

```
const map = (list, fn) =>
list.map(fn);
```

### Technical frame 5: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01437))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01435))_

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Technical frame 6: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01440))_

> 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01438))_

```
const squaresOf = (list) =>
list.map(x => x * x);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 7: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01442))_

> If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01441))_

```
const squaresOf = mapWith(n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 8: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01444))_

> Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01443))_

```
const squaresOf = callRight(map, (n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 9: Recipes with Data / Flip

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01449))_

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Technical frame 10: Recipes with Data / Flip

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01451))_

```
const mapWith = (fn) => (list) => map(list, fn);
```

### Technical frame 11: Recipes with Data / Flip

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01452))_

> You can see that if we simplify it:

### Technical frame 12: Recipes with Data / Flip

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01453))_

```
const mapWith = (fn, list) => map(list, fn);
```

### Technical frame 13: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01455))_

```
const mapper = (list) => (fn) => map(list, fn);
```

### Technical frame 14: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01457))_

```
const mapWith = (fn) => (list) => map(list, fn);
```

### Technical frame 15: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01459))_

```
const mapWith = (first) => (second) => map(second, first);
```

### Technical frame 16: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01461))_

```
const wrapper = (fn) =>
(first) => (second) => fn(second, first);
```

### Technical frame 17: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01464))_

```
const flipAndCurry = (fn) =>
(first) => (second) => fn(second, first);
Sometimes you want to flip, but not curry:
const flip = (fn) =>
(first, second) => fn(second, first);
This is gold. Consider how we define mapWith now:
var mapWith = flipAndCurry(map);
Much nicer!
```

### Technical frame 18: Recipes with Data / Flip / self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01467))_

```
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn(second, first);
}
else {
return function (second) {
return fn(second, first);
};
};
};
```

### Technical frame 19: Recipes with Data / Flip / self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01468))_

> Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

### Technical frame 20: Recipes with Data / Flip / flipping methods

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01470))_

> When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01471))_

```
const flipAndCurry = (fn) =>
(first) =>
function (second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn.call(this, second, first);
}
else {
return function (second) {
return fn.call(this, second, first);
};
};
};
```

### Technical frame 21: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01474))_

```
const inventory = {
apples: 12,
oranges: 12
};
inventory.bananas = 54;
inventory.pears = 24;
```

### Technical frame 22: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01476))_

```
for (let fruit in shipment) {
inventory[fruit] = shipment[fruit]
}
```

### Technical frame 23: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01478))_

```
Object.assign({}, {
apples: 12,
oranges: 12
})
//=> { apples: 12, oranges: 12 }
```

### Technical frame 24: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01480))_

```
const inventory = {
apples: 12,
oranges: 12
};
const shipment = {
bananas: 54,
pears: 24
}
Object.assign(inventory, shipment)
```

### Technical frame 25: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01481))_

```
//=> { apples: 12,
//
oranges: 12,
//
bananas: 54,
//
pears: 24 }
```

### Technical frame 26: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01483))_

```
const Queue = function () {
this.array = [];
this.head = 0;
this.tail = -1
};
Queue.prototype.pushTail = function (value) {
// ...
};
Queue.prototype.pullHead = function () {
// ...
};
Queue.prototype.isEmpty = function () {
// ...
}
Into this:
const Queue = function () {
Object.assign(this, {
array: [],
head: 0,
tail: -1
})
};
Object.assign(Queue.prototype, {
pushTail (value) {
// ...
},
pullHead () {
// ...
},
isEmpty () {
// ...
```

### Technical frame 27: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01484))_

```
Recipes with Data
}
});
```

### Technical frame 28: Recipes with Data / Why?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01489))_

> Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01487))_

```
This is the canonical Y Combinator86:
const Y = (f) =>
( x => f(v => x(x)(v)) )(
x => f(v => x(x)(v))
);
You use it like this:
const factorial = Y(function (fac) {
return function (n) {
return (n == 0 ? 1 : n * fac(n - 1));
```

### Technical frame 29: Recipes with Data / Why?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01489))_

> Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01488))_

```
return function (n) {
return (n == 0 ? 1
}
});
factorial(5)
//=> 120
```

### Technical frame 30: Recipes with Data / Why?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01494))_

> What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01493))_

```
const Y = (f) => {
const something = x => f(v => x(x)(v));
return something(something);
};
```

### Technical atom 31

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01463))_

| entry | content |
| --- | --- |
| 84 | https://github.com/raganwald/allong.es |
| 85 | http://underscorejs.org |

<details>
<summary>Raw table text</summary>

```
84 https://github.com/raganwald/allong.es
85 http://underscorejs.org
```

</details>
