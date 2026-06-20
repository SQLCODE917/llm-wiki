---
page_id: object-assign
page_kind: source
summary: Chapter on Object.assign function and its usage in JavaScript
sources: raw/javascriptallonge.pdf p.198-205
updated: 2026-06-19
---

## Object.assign

It's very common to want to "extend" an object by assigning properties to it: 

```javascript
const inventory = { apples: 12, oranges: 12 };
inventory.bananas = 54;
inventory.pears = 24;
```

It's also common to want to assign the properties of one object to another: 

```javascript
for (let fruit in shipment) {
  inventory[fruit] = shipment[fruit]
}
```

Both needs can be met with `Object.assign`, a standard function. You can copy an object by extending an empty object: 

```javascript
Object.assign({}, { apples: 12, oranges: 12 }) //=> { apples: 12, oranges: 12 }
```

You can extend one object with another: 

```javascript
const inventory = { apples: 12, oranges: 12 };
const shipment = { bananas: 54, pears: 24 }
Object.assign(inventory, shipment)
//=> { apples: 12, oranges: 12, bananas: 54, pears: 24 }
```

And when we discuss prototypes, we will use `Object.assign` to turn this: 

```javascript
const Queue = function () {
  this.array = [];
  this.head = 0;
  this.tail = -1;
};
Queue.prototype.pushTail = function (value) { /* ... */ };
Queue.prototype.pullHead = function () { /* ... */ };
Queue.prototype.isEmpty = function () { /* ... */ }
```

Into this:

```javascript
const Queue = function () {
  Object.assign(this, { array: [], head: 0, tail: -1 })
};
Object.assign(Queue.prototype, {
  pushTail (value) { /* ... */ },
  pullHead () { /* ... */ },
  isEmpty () { /* ... */ }
});
```

Assigning properties from one object to another (also called "cloning" or "shallow copying") is a basic building block that we will later use to implement more advanced paradigms like mixins.

## Why?

This is the canonical Y Combinator[86] : 

```javascript
const Y = (f) => ( x => f(v => x(x)(v)) )( x => f(v => x(x)(v)) );
```

You use it like this: 

```javascript
const factorial = Y(function (fac) {
  return function (n) {
    return (n == 0 ? 1 : n * fac(n - 1));
  }
});
factorial(5) //=> 120
```

Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names. 

So again, why include the recipe? Well, besides all of the practical applications that combinators provide, there is this little thing called _The joy of working things out._ 

There are many explanations of the Y Combinator's mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. Use it as an excuse to get familiar with your environment's debugging facility. 

One tip is to use JavaScript to name things. For example, you could start by writing: 

```javascript
const Y = (f) => {
  const something = x => f(v => x(x)(v));
  return something(something);
};
```

What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. 

Work things out for yourself! 

> 86https://en.wikipedia.org/wiki/Fixed-point_combinator#Example_in_JavaScript
