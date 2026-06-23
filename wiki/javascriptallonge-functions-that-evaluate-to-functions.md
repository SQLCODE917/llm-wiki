---
page_id: javascriptallonge-functions-that-evaluate-to-functions
page_kind: source
summary: functions that evaluate to functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.38-38
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on functions that evaluate to functions in JavaScript Allongé.

## Key supported claims

- Function that returns a function that returns zero. (raw/javascriptallonge.pdf p.38-38)
- Function that evaluates to a function that evaluates to 0. (raw/javascriptallonge.pdf p.38-38)
- Next chapter will show practical use of functions. (raw/javascriptallonge.pdf p.38-38)

## Technical details

### `technical-atom-f34d6b48a7f7e7dd` code

Citation: (raw/javascriptallonge.pdf p.38)

```javascript
() => () => 0
```

### `technical-atom-d08ee02e38a00296` code

Citation: (raw/javascriptallonge.pdf p.38)

```javascript
() => () => true
```

### `technical-atom-3c024d8c90300662` code

Citation: (raw/javascriptallonge.pdf p.38)

```javascript
(() => () => true )()() //=> true
```

### `technical-atom-3b50818489707f02` code

Citation: (raw/javascriptallonge.pdf p.38)

```javascript
() => () => { return true ; }
```

### `technical-atom-e3624af5aae576df` procedure

Citation: (raw/javascriptallonge.pdf p.38)

So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.
