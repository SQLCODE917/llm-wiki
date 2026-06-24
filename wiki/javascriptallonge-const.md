---
page_id: javascriptallonge-const
page_kind: source
summary: mixing let and const from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.150-151
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

The const keyword in JavaScript provides a way to bind values to names in a block-scoped manner, as described in the chapter on const (pages 51-53). This chunk discusses mixing let and const, including shadowing behavior.

## Key supported claims

- Shadowing a let with a const does not change our ability to rebind the variable in its original scope (raw/javascriptallonge.pdf p.150-151).
- Shadowing a const with a let does not permit it to be rebound in its original scope (raw/javascriptallonge.pdf p.150-151).
- If you dislike deliberately shadowing variables, you'll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable (raw/javascriptallonge.pdf p.150-151).

## Technical details

### `technical-atom-0fff76e11a2f0259` code

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
(diameter, PI) => diameter * PI
```

### `technical-atom-6b1fa159b11f3fdf` code

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
((diameter, PI) => diameter * PI)(2, 3.14159265) //=> 6.2831853
```

### `technical-atom-1b51371583d7be04` code

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
(diameter) => { const PI = 3.14159265; return diameter * PI }
```

### `technical-atom-a812f777ca9db227` code

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
((diameter) => ((PI) =>
```

### `technical-atom-739617cd68c40d01` code

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
diameter * PI)(3.14159265))(2) Or: ((diameter, PI) => diameter * PI)(2, 3.14159265)
```

### `technical-atom-f7c0ca4dee1c6a2e` code

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
//=> 6.2831853
```

### `technical-atom-5795eab603cc5fbc` code

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
((diameter) => { const PI = 3.14159265; return diameter * PI })(2) //=> 6.2831853
```

### `technical-atom-9c45bf60b6768816` code

Citation: (raw/javascriptallonge.pdf p.150-151)

```javascript
(d) => { const calc = (diameter) => { const PI = 3.14159265; return diameter * PI }; return "The circumference is " + calc(d) }
```

## Related technical details

### From [[javascriptallonge-rebinding]]: `technical-atom-3ee28a0dd987831d` exception

Relation: nearby source page; matched terms `const`, `does`, `javascript`, `not`, `permit`, `rebind`

Citation: (raw/javascriptallonge.pdf p.60-61)

JavaScript does not permit us to rebind a name that has been bound with const .

### From [[javascriptallonge-rebinding]]: `technical-atom-7c21d7d7a5e7d689` exception

Relation: nearby source page; matched terms `const`, `rebind`, `scope`

Citation: (raw/javascriptallonge.pdf p.60-61)

We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.
