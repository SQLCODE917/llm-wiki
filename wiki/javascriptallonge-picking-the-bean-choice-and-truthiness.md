---
page_id: javascriptallonge-picking-the-bean-choice-and-truthiness
page_kind: source
summary: Picking the Bean: Choice and Truthiness from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.94-99
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses truthiness and falsiness in JavaScript, logical operators, and control flow.

## Key supported claims

- JavaScript has a notion of truthiness, where every value is either truthy or falsy (raw/javascriptallonge.pdf p.94-99).
- The logical operators !, &&, and || operate on truthiness, not strict boolean values (raw/javascriptallonge.pdf p.94-99).
- The ternary operator (?:) is a control-flow operator that evaluates expressions based on truthiness (raw/javascriptallonge.pdf p.94-99).

## Technical details

### `technical-atom-13128b8fc1556aca` code

Citation: (raw/javascriptallonge.pdf p.94-99)

```javascript
- [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic': 'Quasimodal' //=> 'Pentatonic'
```

### `technical-atom-63d72ad2c1e67d26` code

Citation: (raw/javascriptallonge.pdf p.94-99)

```javascript
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord): 'Forbid den';
```

### `technical-atom-69f71aab863b5fa0` code

Citation: (raw/javascriptallonge.pdf p.94-99)

```javascript
is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user.
```

### `technical-atom-14b2483ccfce7869` code

Citation: (raw/javascriptallonge.pdf p.94-99)

```javascript
const even = (n) => n === 0 || (n !== 1 && even(n - 2))
```

### `technical-atom-f1849007585d2d23` code

Citation: (raw/javascriptallonge.pdf p.94-99)

```
If n === 0, JavaScript does not evaluate (n !== 1 && even(n - 2)). This is very important! Imagine that JavaScript evaluated both sides of the || operator before determining its value. n === 0 would be true. What about (n !== 1 && even(n - 2))? Well, it would evaluate even(n - 2), or even(-2)
```

### `technical-atom-7a5061630755baa4` code

Citation: (raw/javascriptallonge.pdf p.94-99)

```
This leads us to evaluate n === 0 || (n !== 1 && even(n - 2)) all over again, and this time we end up evaluating even(-4). And then even(-6). and so on and so forth until JavaScript throws up its hands and runs out of stack space.
```

### `technical-atom-bd8a5462e95eea45` code

Citation: (raw/javascriptallonge.pdf p.94-99)

```
But that’s not what happens. || and && have short-cut semantics . In this case, if n === 0, JavaScript does not evaluate (n !== 1 && even(n - 2)). Likewise, if n === 1, JavaScript evaluates n !== 1 && even(n - 2) as false without ever evaluating even(n - 2).
```

### `technical-atom-099e333e5e8d5482` code

Citation: (raw/javascriptallonge.pdf p.94-99)

```javascript
const or = (a, b) => a || b
```
