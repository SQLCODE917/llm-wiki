---
page_id: javascriptallonge-tail-call-optimization
page_kind: source
summary: Tail-call optimization in JavaScript as described in 'JavaScript Allongé'.
sources: raw/javascriptallonge.pdf p.119-119
updated: 2026-06-20
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
