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

### `technical-atom-bc6fdea9ceb74d28` exception

Citation: (raw/javascriptallonge.pdf p.39-40)

Up to now, we've looked at functions without arguments.

### `technical-atom-dd665ae074e9887f` exception

Citation: (raw/javascriptallonge.pdf p.39-40)

We haven't even said what an argument is , only that our functions don't have any.

### `technical-atom-e6dd19d4ac7ef05f` code

Citation: (raw/javascriptallonge.pdf p.39-40)

```
Remember that to apply a function with no arguments, we wrote (() => {})() .
```
