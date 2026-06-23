---
page_id: javascriptallonge-tail-call-optimization
page_kind: source
summary: tail-call optimization from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.119-119
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Tail-call optimization in JavaScript as described in 'JavaScript Allongé'.

## Key supported claims

- A 'tail-call' occurs when a function's last act is to invoke another function, and then return whatever the other function returns. (raw/javascriptallonge.pdf p.119-119)
- This is a very important characteristic of JavaScript: If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space. (raw/javascriptallonge.pdf p.119-119)
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call. (raw/javascriptallonge.pdf p.119-119)
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe-wrapped call. (raw/javascriptallonge.pdf p.119-119)
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). (raw/javascriptallonge.pdf p.119-119)

## Technical details

### `technical-atom-d96c8d42a851c268` code

Citation: (raw/javascriptallonge.pdf p.119)

```javascript
const maybe = (fn) => function (...args) { if (args.length === 0) { return ; } else { for ( let arg of args) { if (arg == null ) return ; } return fn.apply( this , args); } }
```

### `technical-atom-3ab563ed5ac832bf` code

Citation: (raw/javascriptallonge.pdf p.119)

```javascript
const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest);
```

### `technical-atom-dc519bb9c80f4c66` procedure

Citation: (raw/javascriptallonge.pdf p.119)

A'tail-call' occurs when a function's last act is to invoke another function, and then return whatever the other function returns.

### `technical-atom-624f12a2920dab5a` worked-example

Citation: (raw/javascriptallonge.pdf p.119)

For example, consider the maybe function decorator:

### `technical-atom-7f8f26fdd9419454` exception

Citation: (raw/javascriptallonge.pdf p.119)

And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe -wrapped call.

### `technical-atom-26bbf61b78e17d42` worked-example

Citation: (raw/javascriptallonge.pdf p.119)

Consider this implementation of length :

### `technical-atom-d64971ca777393ea` exception

Citation: (raw/javascriptallonge.pdf p.119)

The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call.
