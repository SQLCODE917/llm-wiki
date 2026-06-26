---
page_id: sword-world-rpg-complete-edition-4-5-attacks-from-characters-against-monsters-through-4-6
page_kind: source
summary: 4.5 Attacks From Characters Against Monsters through 4.6 Attacks From Monsters Against Characters from raw/Sword World RPG - Complete Edition.pdf.
sources: raw/Sword World RPG - Complete Edition.pdf p.43-45, raw/Sword World RPG - Complete Edition.pdf p.46-47
updated: 2026-06-25
source_id: Sword World RPG - Complete Edition.pdf
---

## Source record

Chapter 4.5-4.6 of Sword World RPG - Complete Edition covers attack mechanics for characters against monsters and monsters against characters.

## Key supported claims

- Characters attack monsters with a hit check using attack power and 2D, where the target is the monster's evasion points (raw/Sword World RPG - Complete Edition.pdf p.43-45).
- Characters can deal critical damage with strike rolls if the 2D roll meets or exceeds the critical target (raw/Sword World RPG - Complete Edition.pdf p.43-45).
- Monsters attack characters using evasion checks with evasion speed and 2D, where the target is the monster's attack points (raw/Sword World RPG - Complete Edition.pdf p.46-47).

## Technical details

### `technical-atom-9aa939d63373c989` code

Citation: (raw/Sword World RPG - Complete Edition.pdf p.43-47)

```
7 (goblin's strike points) – {0 (defense roll) +2 (damage reduction)} = 5
```

### `technical-atom-05a6ec779ca547b8` code

Citation: (raw/Sword World RPG - Complete Edition.pdf p.43-47)

```
7 (goblin's strike points) – {6 (defense roll) +2 (damage reduction)} = -1
```

### `technical-atom-f4d99f3a5732f0ee` formula

Citation: (raw/Sword World RPG - Complete Edition.pdf p.43-47)

**final damage** = base damage + bonus damage - monster's defense points

### `technical-atom-080e0a47a66e866b` formula

Citation: (raw/Sword World RPG - Complete Edition.pdf p.43-47)

**Final damage** = monster's strike points - (defense roll result + damage reduction)

### `technical-atom-03a6f3cbcd58b841` procedure

Citation: (raw/Sword World RPG - Complete Edition.pdf p.43-47)

If your hit check is a success and you’re able to hit your target, the damage dealt to your opponent can be determined next.

### `technical-atom-f5f5bf823ab7effb` procedure

Citation: (raw/Sword World RPG - Complete Edition.pdf p.43-47)

The first step is to determine base damage.

### `technical-atom-92cfbddce5794173` requirement

Citation: (raw/Sword World RPG - Complete Edition.pdf p.43-47)

When a character attacks a monster, they must make a success roll hit check, using _attack power_ as the baseline score.

### `technical-atom-c5fce285f0fb93f0` table

#### Table block 1

Citation: (raw/Sword World RPG - Complete Edition.pdf p.43)

|||Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|
|2D|2|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|
||3|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|
||4|0|0|0|0|0|1|1|1|1|1|1|2|2|2|2|2|2|2|2|2|
||5|0|0|0|1|1|1|1|1|2|2|2|2|2|3|3|3|3|3|3|3|
||6|1|1|1|1|2|2|2|2|2|3|3|3|3|3|4|4|4|4|4|4|
||7|2|2|2|2|2|2|3|3|3|3|3|3|4|4|4|4|4|5|5|5|
||8|2|3|3|3|3|3|3|4|4|4|4|4|4|4|4|5|5|5|6|6|
||9|3|3|4|4|4|4|4|4|4|4|5|5|5|5|5|5|6|6|6|7|
||10|3|3|4|4|4|5|5|5|5|5|5|6|6|6|6|6|7|7|7|7|
||11|4|4|4|4|5|5|5|5|6|6|6|6|6|7|7|7|7|7|7|8|
||12|4|4|4|5|5|5|5|6|6|7|7|7|7|7|8|8|8|8|8|9|

#### Table block 2

Citation: (raw/Sword World RPG - Complete Edition.pdf p.43)

|||Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|
|2D|2|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|**|
||3|1|1|1|2|2|2|2|2|2|2|2|2|3|3|3|3|3|3|3|4|
||4|2|2|2|2|3|3|3|3|3|3|4|4|4|4|4|4|5|5|5|5|
||5|3|3|3|3|4|4|4|4|4|4|4|5|5|5|5|5|5|6|6|6|
||6|4|4|5|5|5|5|5|6|6|6|6|6|6|6|6|7|7|7|7|7|
||7|5|6|6|6|6|6|6|6|6|7|7|7|7|8|8|8|8|8|8|8|
||8|6|6|6|7|7|7|8|8|8|8|8|8|8|8|9|9|9|9|10|10|
||9|7|7|7|7|7|8|8|8|9|9|9|9|10|10|10|10|10|10|10|11|
||10|8|8|8|8|8|8|9|9|9|9|10|10|10|10|10|10|11|11|11|11|
||11|9|9|9|9|9|9|9|9|10|10|10|10|10|10|11|11|11|12|12|12|
||12|10|10|10|10|10|10|10|10|10|10|10|10|10|10|11|12|12|12|13|13|

#### Table block 3

Citation: (raw/Sword World RPG - Complete Edition.pdf p.43)

|||Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number|Key Number||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||40|41|42|43|44|45|46|47|48|49|50|
|2D|2|**|**|**|**|**|**|**|**|**|**|**|
||3|4|4|4|4|4|4|4|4|4|4|4|
||4|5|6|6|6|6|6|6|6|6|6|6|
||5|6|6|7|7|7|7|7|7|7|7|8|
||6|7|7|7|8|8|9|9|9|9|10|10|
||7|9|9|9|9|10|10|10|10|10|10|10|
||8|10|10|10|10|10|10|10|11|12|12|12|
||9|11|11|11|11|11|11|12|12|12|12|12|
||10|11|12|12|12|12|12|13|13|13|13|13|
||11|12|12|13|13|13|13|13|13|13|14|15|
||12|13|13|13|14|14|14|14|15|15|15|15|

## Related technical details

### From [[sword-world-rpg-complete-edition-4-7-attacks-from-characters-against-characters-through-4-9]]: `technical-atom-d03fb604ec5a3ffd` formula

Relation: nearby source page; matched terms `against`, `attacks`, `characters`, `evasion`, `score`, `speed`

Citation: (raw/Sword World RPG - Complete Edition.pdf p.48-50)

**defender's final score** = evasion speed + 2D

### From [[sword-world-rpg-complete-edition-4-7-attacks-from-characters-against-characters-through-4-9]]: `technical-atom-8feb194fca9fc980` formula

Relation: nearby source page; matched terms `against`, `attack`, `attacks`, `characters`, `power`, `score`

Citation: (raw/Sword World RPG - Complete Edition.pdf p.48-50)

**attacker's final score** = attack power + 2D

### From [[sword-world-rpg-complete-edition-4-7-attacks-from-characters-against-characters-through-4-9]]: `technical-atom-6affb20d330bc3d3` requirement

Relation: nearby source page; matched terms `against`, `attacks`, `characters`, `check`, `hit`, `requirement`

Citation: (raw/Sword World RPG - Complete Edition.pdf p.48-50)

To make a hit check, both sides must roll the dice (2D).

### From [[sword-world-rpg-complete-edition-4-3-projectile-restrictions-through-4-4-scores-used-in-weapon]]: `technical-atom-a6c76e65abea03c8` formula

Relation: nearby source page; matched terms `critical`, `target`, `using`

Citation: (raw/Sword World RPG - Complete Edition.pdf p.40-42)

**critical target** = 10 (9 if using thief skill)
