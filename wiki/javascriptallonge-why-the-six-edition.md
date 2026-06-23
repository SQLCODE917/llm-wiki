---
page_id: javascriptallonge-why-the-six-edition
page_kind: source
summary: why the 'six' edition? from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.7-9
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

A comprehensive modular guide to JavaScript fundamentals and advanced techniques, spanning 20 chapters.

## Key supported claims

- ECMAScript 2015 introduces block-structured variables and other features that make JavaScript programming more expressive, (raw/javascriptallonge.pdf p.7-9).
- Prior to ECMAScript 2015, JavaScript lacked block-structured variables, leading to workarounds like IIFEs, (raw/javascriptallonge.pdf p.7-9).
- JavaScript lacked support for collecting a variable number of arguments into a parameter, leading to workarounds involving arguments and slice, (raw/javascriptallonge.pdf p.7-9).

## Technical details

### `technical-atom-b22825d53a7940b6` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```
for ( int i = 0; i < array.length; ++i) { // ... }
```

### `technical-atom-9c143b3b20dadd27` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```javascript
var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) }
```

### `technical-atom-6503617905632e6f` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```
def foo (first, *rest) # ... end
```

### `technical-atom-4f112602192e34f4` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```javascript
function foo () { var first = arguments[0], rest = [].slice.call(arguments, 1); // ... }
```

### `technical-atom-1ca98b0a0d1476b8` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```javascript
for ( let i = 0; i < array.length; ++i) { // ... }
```

### `technical-atom-abffd2e5e3ffc275` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```javascript
function foo (first, ...rest) { // ... }
```

### `technical-atom-4a46581d403c3e4f` worked-example

Citation: (raw/javascriptallonge.pdf p.7-9)

For example, JavaScript did not include block-structured variables.

### `technical-atom-5d409b43a1c574f9` worked-example

Citation: (raw/javascriptallonge.pdf p.7-9)

For example, block-structured languages allow us to write:
