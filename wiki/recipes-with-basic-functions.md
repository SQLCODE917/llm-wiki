---
page_id: recipes-with-basic-functions
page_kind: source
summary: Chapter on basic function recipes including partial application, unary, tap, maybe, once, and left-variadic functions.
sources: raw/javascriptallonge.pdf p.79-93
updated: 2026-06-19
---

## **Partial Application**

Partial application is a technique where a function is created by fixing some arguments of an existing function. This is useful for creating specialized versions of general functions.

The chapter introduces several functions for partial application:
- `callFirst`: Fixes the first argument of a function
- `callLast`: Fixes the last argument of a function
- `callLeft`: Fixes multiple arguments from the left side
- `callRight`: Fixes multiple arguments from the right side

Example:
```javascript
const greet = (me, you) => `Hello, ${ you }, my name is ${ me }`;

const heliosSaysHello = callFirst(greet, 'Helios');
heliosSaysHello('Eartha') //=> 'Hello, Eartha, my name is Helios'

const sayHelloToCeline = callLast(greet, 'Celine');
sayHelloToCeline('Eartha') //=> 'Hello, Celine, my name is Eartha'
```

These recipes are designed to be reusable and context-agnostic, helping solve common problems in functional programming.

## **Unary**

"Unary" is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

The most common use case is to fix a problem. JavaScript's `.map` method calls each function with three arguments (element, index, array), but some functions like `parseInt` have optional arguments. Using unary ensures that functions are called with only one argument:

```javascript
['1', '2', '3'].map(unary(parseInt)) //=> [1, 2, 3]
```

## **Tap**

The "tap" function performs side effects with a value and then returns the value. It's useful for debugging or performing operations without changing the flow of data.

```javascript
const tap = (value) => (fn) => ( typeof (fn) === 'function' && fn(value), value )
```

Example:
```javascript
tap('espresso')((it) => { console.log(`Our drink is '${ it }'`) }); //=> Our drink is 'espresso'
'espresso'
```

## **Maybe**

The "maybe" pattern prevents a function from being called if any of its arguments are null or undefined. It's borrowed from Haskell's maybe monad, Ruby's andand, and CoffeeScript's existential method invocation.

```javascript
const maybe = (fn) => function (...args) { 
if (args.length === 0) { return } 
else { 
for ( let arg of args) { 
if (arg == null ) return ; 
} 
return fn.apply( this , args) 
} 
}
```

Example:
```javascript
maybe((a, b, c) => a + b + c)(1, 2, 3) //=> 6
maybe((a, b, c) => a + b + c)(1, null, 3) //=> undefined
```

## **Once**

The "once" decorator ensures that a function can only be called once. After the first call, it returns undefined for any subsequent calls.

```javascript
const once = (fn) => { 
let done = false; 
return function () { 
return done ? void 0 : ((done = true ), fn.apply( this , arguments)) 
} 
}
```

Example:
```javascript
const askedOnBlindDate = once( () => "sure, why not?" );
askedOnBlindDate() //=> 'sure, why not?'
askedOnBlindDate() //=> undefined
```

## **Left-Variadic Functions**

Left-variadic functions gather arguments from the left side of the parameter list, which is not natively supported in JavaScript. The chapter provides a decorator `leftVariadic` to achieve this functionality.

```javascript
const leftVariadic = (fn) => { 
if (fn.length < 1) { return fn; } 
else { 
return function (...args) { 
const gathered = args.slice(0, args.length - fn.length + 1), 
spread = args.slice(args.length - fn.length + 1); 
return fn.apply( this , [gathered].concat(spread) 
); 
} 
} 
};
```

Example:
```javascript
const butLastAndLast = leftVariadic((butLast, last) => [butLast, last]); 
butLastAndLast('why', 'hello', 'there', 'little', 'droid') //=> [["why","hello","there","little"],"droid"]
```

## **Key Concepts**

- **Partial Application**: Creating new functions by fixing some arguments of existing functions.
- **Unary**: A function decorator that ensures a function only accepts one argument.
- **Tap**: A function that performs side effects with a value and then returns the value.
- **Maybe**: A function decorator that prevents a function from being called if any of its arguments are null or undefined.
- **Once**: A function decorator that ensures a function can only be called once.
- **Left-Variadic Functions**: Functions that gather arguments from the left side of the parameter list.

## **Key Entities**

- **callFirst**: Function for partial application with the first argument.
- **callLast**: Function for partial application with the last argument.
- **callLeft**: Function for partial application with multiple left arguments.
- **callRight**: Function for partial application with multiple right arguments.
- **unary**: Function decorator for ensuring a function only accepts one argument.
- **tap**: Function for performing side effects with a value and returning it.
- **maybe**: Function decorator for preventing function calls with null or undefined arguments.
- **once**: Function decorator for ensuring a function is only called once.
- **leftVariadic**: Function decorator for creating left-variadic functions.
- **leftGather**: Function for gathering array elements from the left side.

## **Page-Map Navigation**

- [[javascriptallonge]]
- [[as-little-as-possible-about-functions-but-no-less]]
- [[closures-and-scope]]
