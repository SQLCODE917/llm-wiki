---
page_id: javascriptallonge-ah-i-d-like-to-have-an-argument-please-22
page_kind: source
summary: Ah. I'd Like to Have an Argument, Please. 22 from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.39-40
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter 22 of 'JavaScript Allongé' discusses functions with arguments, explaining that arguments are often called 'parameters' and are familiar to most programmers. The chapter provides examples of functions with one and two arguments, and how to apply them.

## Key supported claims

- Most programmers are perfectly familiar with arguments (often called 'parameters'), as discussed in secondary school mathematics (raw/javascriptallonge.pdf p.39-40).
- Up to now, we've looked at functions without arguments, and we haven't even said what an argument is, only that our functions don't have any (raw/javascriptallonge.pdf p.39-40).
- Let's make a function with an argument: (room) => {} (raw/javascriptallonge.pdf p.39-40).
- It's a function for calculating the circumference of a circle given the diameter: (diameter) => diameter * 3.14159265 (raw/javascriptallonge.pdf p.39-40).
- 22 The Argument Sketch from 'Monty Python's Previous Record' and 'Monty Python's Instant Record Collection' (raw/javascriptallonge.pdf p.39-40).

## Technical details

### `technical-atom-94f7721ba9cca54e` code

Citation: (raw/javascriptallonge.pdf p.39-40)

```javascript
(room) => {}
```

### `technical-atom-41216aaff55cd3d2` code

Citation: (raw/javascriptallonge.pdf p.39-40)

```javascript
(room, board) => {}
```

### `technical-atom-d9d74db003dec0ac` code

Citation: (raw/javascriptallonge.pdf p.39-40)

```javascript
(diameter) => diameter * 3.14159265
```

### `technical-atom-f933c060eb803857` code

Citation: (raw/javascriptallonge.pdf p.39-40)

```javascript
((diameter) => diameter * 3.14159265)(2) //=> 6.2831853
```

### `technical-atom-01551029e05d5275` code

Citation: (raw/javascriptallonge.pdf p.39-40)

```javascript
((room, board) => room + board)(800, 150) //=> 950
```

### `technical-atom-e6dd19d4ac7ef05f` code

Citation: (raw/javascriptallonge.pdf p.39-40)

```
Remember that to apply a function with no arguments, we wrote (() => {})() .
```

### `technical-atom-bc6fdea9ceb74d28` exception

Citation: (raw/javascriptallonge.pdf p.39-40)

Up to now, we've looked at functions without arguments.

### `technical-atom-dd665ae074e9887f` exception

Citation: (raw/javascriptallonge.pdf p.39-40)

We haven't even said what an argument is , only that our functions don't have any.

## Related technical details

### From [[javascriptallonge-functions-that-evaluate-to-functions]]: `technical-atom-e3624af5aae576df` procedure

Relation: nearby source page; matched terms `argument`, `functions`, `have`, `how`, `like`, `make`

Citation: (raw/javascriptallonge.pdf p.38)

So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

### From [[javascriptallonge-call-by-sharing]]: `technical-atom-e8199c3947c572cb` requirement

Relation: nearby source page; matched terms `apply`, `argument`, `arguments`, `function`, `our`, `what`

Citation: (raw/javascriptallonge.pdf p.42-43)

When we combine our knowledge of value types, reference types, arguments, and closures, we'll understand why this function always evaluates to true no matter what argument 26 you apply it to:

### From [[javascriptallonge-variables-and-bindings]]: `technical-atom-2a1d586167017e1b` requirement

Relation: nearby source page; matched terms `how`, `know`, `let`, `our`, `them`, `you`

Citation: (raw/javascriptallonge.pdf p.41-42)

In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries').

### From [[javascriptallonge-call-by-value]]: `technical-atom-fbf27e4e62b010d5` code

Relation: nearby source page; matched terms `diameter`

Citation: (raw/javascriptallonge.pdf p.40-41)

```javascript
((diameter) => diameter * 3.14159265)(1 + 1) //=> 6.2831853
```
