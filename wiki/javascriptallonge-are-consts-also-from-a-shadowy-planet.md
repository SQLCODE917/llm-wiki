---
page_id: javascriptallonge-are-consts-also-from-a-shadowy-planet
page_kind: source
summary: are consts also from a shadowy planet? from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.57-60
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter section on const scoping and shadowing in JavaScript.

## Key supported claims

- Const values use lexical scope, just like parameters, and are looked up in the environment where they are declared (raw/javascriptallonge.pdf p.57-60).
- Const statements can appear inside blocks, and they shadow enclosing bindings just like parameters (raw/javascriptallonge.pdf p.57-60).
- Const statements shadow values bound within environments created by blocks, not just functions (raw/javascriptallonge.pdf p.57-60).

## Technical details

### `technical-atom-17a1385c4e7e2cdb` code

Citation: (raw/javascriptallonge.pdf p.57-60)

```javascript
((PI) => (diameter) => diameter * PI )(3.14159265)
```

### `technical-atom-2a49f0058d2569fe` code

Citation: (raw/javascriptallonge.pdf p.57-60)

```javascript
((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)
```

### `technical-atom-6bfbc2e135b7f58a` code

Citation: (raw/javascriptallonge.pdf p.57-60)

```javascript
((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)(2) //=> 6.2831853
```

### `technical-atom-8118892bba58fca4` code

Citation: (raw/javascriptallonge.pdf p.57-60)

```javascript
((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265)
```

### `technical-atom-88fc9101560e4009` code

Citation: (raw/javascriptallonge.pdf p.57-60)

```javascript
((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265)(2) //=> 6.2831853
```

### `technical-atom-2fccf9db6fd344c0` code

Citation: (raw/javascriptallonge.pdf p.57-60)

```javascript
((diameter) => { const PI = 3.14159265; (() => { const PI = 3; })(); return diameter * PI; })(2) //=> 6.2831853
```

### `technical-atom-e06f3c95cf2d188b` code

Citation: (raw/javascriptallonge.pdf p.57-60)

```javascript
if ( true ) { // an immediately invoked block statement (IIBS) } Let's try it: ((diameter) => { const PI = 3; if ( true ) { const PI = 3.14159265; return diameter * PI; } })(2) //=> 6.2831853 ((diameter) => { const PI = 3.14159265; if ( true ) { const PI = 3; } return diameter * PI;
```

### `technical-atom-251a228560047109` code

Citation: (raw/javascriptallonge.pdf p.57-60)

```javascript
})(2) //=> 6.2831853
```

## Related technical details

### From [[javascriptallonge-rebinding]]: `technical-atom-7c21d7d7a5e7d689` exception

Relation: nearby source page; matched terms `bound`, `can`, `const`, `scope`, `shadow`

Citation: (raw/javascriptallonge.pdf p.60-61)

We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

### From [[javascriptallonge-rebinding]]: `technical-atom-3ee28a0dd987831d` exception

Relation: nearby source page; matched terms `bound`, `const`, `javascript`, `not`

Citation: (raw/javascriptallonge.pdf p.60-61)

JavaScript does not permit us to rebind a name that has been bound with const .

### From [[javascriptallonge-const-and-lexical-scope]]: `technical-atom-bd2e48d2cd4ff0f2` code

Relation: nearby source page; matched terms `const`, `lexical`, `scope`

Citation: (raw/javascriptallonge.pdf p.55-57)

```javascript
((diameter_fn) => // ... )( ((PI) => (diameter) => diameter * PI )(3.14159265) )
```

### From [[javascriptallonge-const-and-lexical-scope]]: `technical-atom-6d6230b65912f463` code

Relation: nearby source page; matched terms `const`, `lexical`, `scope`

Citation: (raw/javascriptallonge.pdf p.55-57)

```javascript
((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) //=> 6.2831853
```
