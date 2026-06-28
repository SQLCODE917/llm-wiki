---
page_id: sword-world-rpg-complete-edition-final-damage
page_kind: concept
summary: 4.5.5 Final Damage: 11 statement(s) and 8 atom(s) from raw/Sword World RPG - Complete Edition.pdf.
sources: raw/Sword World RPG - Complete Edition.pdf
updated: 2026-06-28
domain: sword-world-rpg-complete-edition
category_path: concepts
projection_coverage: topic-sword-world-rpg-complete-edition-final-damage@a6e3c1f621ff421052c3d1cb11328677
---

# 4.5.5 Final Damage

What [[sword-world-rpg-complete-edition]] covers about 4.5.5 final damage:

## Statements

### 4.6.5 Final Damage

- The final damage your character suffers from a monster equals the monster's strike points minus the result of your defense roll plus your character's damage reduction . _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00909))_

- If the defense roll came up double ones , no such calculation would be made, and the goblin's 7 strike points would be the damage. _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00912))_

- If final damage is 0 or negative , that means you took no damage at all. The monster's attack was completely blocked by your armor. _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00913))_

### Example:

- Ducard II now determines how much damage his armor prevents. His defense roll result is 7 , and his armor's defense power is 7, so the damage that'll be reduced by his armor is 3 . After adding his damage reduction of 2 , 3+2= 5 points is the final amount of damage Ducard II is able to reduce. _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00948))_

- Suppose a sorcerer casts an Energy Bolt on three enemies ( x 3 expansion) with a +1 to his final score ( x 2 expansion) and he makes 4 damage checks for each ( x 4 expansion). In this case, the multiplied rate of mental power consumed is 3 x 2 x 4 = 24! _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-01259))_

### [ Lightning ]

- Base Mental Power Cost=15 Distance=Caster Area=A space 1 meter high and wide and 20 meters long Duration=Instant Effect=Emits strike power 20 lightning Type=Damage (Electric-type) Expansion=Final score, area length (see description), damage certainty Resist=Reduced effect _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-01703))_

### Blizzard ]

- Expansion=Final score, distance, area, damage certainty Resist=Reduced effect This spell creates a sudden storm containing countless pieces of ice the size of pebbles, in a space within a 5 meter radius centered on a point, dealing cold damage to everything within range. Its strike power is 20. _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-01879))_

### [ Shade ] (Shade/Dark Spirit)

- Expansion=Final score, duration, distance, targets, damage certainty Resist=Reduced effect Shade is the spirit of darkness that opposes will-o-wisp, and is also the spirit that controls fear. It is said to have a spherical shape like the will-o-wisp, but this is not certain (because like a crow in the pitch-black night, it cannot be seen). All natural light within a 5 meter radius of this spirit is negated, closing it in complete darkness. The darkness created by a shade has no effect in a space where the ancient magic Light is at work. In addition, if the light emitted by a will-owisp and the darkness produced by a shade overlap, the powers of both will be negated. The shade will fly freely in the air according to the caster's commands, but can no longer be controlled if it moves more than 20 meters away from the caster. The shade is also very fragile and will easily disintegrate with the slightest force. At this time, it emits an energy completely different from a willo-wisp. This has no physical effect, but it impairs mental activity and has the effect of reducing mental power (points). Make a strike power 10 damage check, and subtract the result from mental power (points). The damage is only dealt to mental power (points), the rest of the check is the same as for magic that deals normal damage. If mental power (points) becomes 0 or negative, the target loses consciousness. Furthermore, if an opponent destroys a shade with a weapon they're holding, the one who took that action will also suffer the same damage. _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-02391))_

### [ Ice Storm ] (Fenrir/Greater Ice Spirit)

- Base Mental Power Cost=40 Distance=30 meters Area=A space with a 10 meter radius Duration=Instant Effect=Creates an ice storm, dealing strike power 30 damage to targets within range Type=Damage (Cold-type) Expansion=Final score, distance, area, damage certainty Resist=Reduced effect _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-02765))_

### Chapter 11: Notes on Magic / Damage Poison

- Deals damage to the opponent's life force (points). First, make a strike roll with a strike power of 20. Magic power should be added to damage as usual. Also, your opponent cannot reduce this damage using adventurer level. This poison's damage is not applied immediately, but in the form of 1 point at the end of each round, starting on the round in which the spell is used. The poison then lasts until the final determined damage is dealt. In this case, if the poison is removed by a spell such as Cure Poison , etc. midway, the damage will stop accumulating at that point. However, the damage suffered up to that point will not be recovered. _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-04123))_


## Technical atoms

### Technical frame 1: 4.5.5 Final Damage

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00870))_

> final damage = base damage + bonus damage - monster's defense points

### Technical frame 2: 4.6.5 Final Damage

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00912))_

> If the defense roll came up double ones , no such calculation would be made, and the goblin's 7 strike points would be the damage.

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00910))_

> Final damage = monster's strike points - (defense roll result + damage reduction)

### Technical atom 3

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00871))_

| entry | content |
| --- | --- |
| 4 | (base damage) +4 (bonus damage) -4 (goblin's defense points) = 4 |
| 18 | (base damage) +4 (bonus damage) |
| 4 | (goblin's defense points) = 18 |
| 14 | (base damage) +4 (bonus damage) -4 (goblin's defense points) = 14 If final damage is 0 or negative , it means that no damage was dealt. The attack was prevented by thick skin or hard scales. |
| 4 | 6 |

<details>
<summary>Raw table text</summary>

```
Example:
If the base damage dealt by Ducard II is 4,  18 ,  or 14 ,  respectively,  the  final damage  he  could  deal  to  the  goblin would be:
4 (base damage) +4 (bonus damage) -4 (goblin's defense points) = 4
18 (base damage) +4 (bonus damage)
-4 (goblin's defense points) = 18
14 (base damage) +4 (bonus damage) -4 (goblin's defense points) = 14
If  final  damage  is 0  or  negative ,  it means  that no  damage was  dealt.  The attack  was  prevented  by  thick  skin  or hard scales.
4.6
```

</details>

### Technical atom 4

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00913))_

> If final damage is 0 or negative , that means you took no damage at all. The monster's attack was completely blocked by your armor.

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00911))_

| entry | content |
| --- | --- |
| 7 | (goblin's strike points) - {0 (defense roll) +2 (damage reduction)} = 5 |
| 7 | (goblin's strike points) - {6 (defense roll) +2 (damage reduction)} = -1 |

<details>
<summary>Raw table text</summary>

```
Example:
If  the  result  of  Ducard  II's  defense roll is 0 (roll 3) or 6 (roll 12), respectively, the final damage he will suffer is calculated to be:
7 (goblin's strike points) - {0 (defense roll) +2 (damage reduction)} = 5
7 (goblin's strike points) - {6 (defense roll) +2 (damage reduction)} = -1
```

</details>

### Technical atom 5

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00912))_

> If the defense roll came up double ones , no such calculation would be made, and the goblin's 7 strike points would be the damage.

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-00914))_

| Example: | If final damage is 0 or negative, that |
| --- | --- |
| Suppose Ducard II’s defense roll came | means you took no damage at all. The |
| 7 | up 12 (double sixes!). The number on |
| ** | row 12 under key number column 7 is 6. |
| 0 | Unlike a strike roll, a defense roll is made |

<details>
<summary>Raw table text</summary>

```
Table 4-3: Rating Table, Key Number
                                    Example:                               If final damage is 0 or negative, that
 Column 7
                                      Suppose Ducard II’s defense roll came    means you took no damage at all. The
               7                    up 12 (double sixes!). The number on    monster's attack was completely blocked
               **                   row 12 under key number column 7 is 6.    by your armor.
               0                    Unlike a strike roll, a defense roll is made
```

</details>

### Technical atom 6

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-03701))_

> First of all, climbing, which is a common ability of adventurers, always requires assistance such as rope. Without such a thing, it's not possible to climb using adventurer level as a baseline score calculation. Climbing with the thief skill does not require rope assistance, and if you do have a rope, you can almost certainly climb. As a formality, a success roll should still be made, but a failure only occurs on double ones. For details, please refer to Table 6-1: Climb by Skill.

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-03702))_

| With Rope | Without Rope |
| --- | --- |
| Almost always succeeds (only double | Requires success |
| ones fail) | roll |
| weight of your belongings. Also, if the | Climb with common adventurer |
| Requires success roll | Not possible |

<details>
<summary>Raw table text</summary>

```
Table 6-1: Climb by Skill
 using adventurer level + agility bonus as
                                                                         With Rope             Without Rope
 the baseline score, make a success roll
 against target score 13 (this can be
                                    Climb with thief skill
                                                               Almost always succeeds (only double  Requires success
                                                                         ones fail)               roll
 increased or decreased depending on the
 weight of your belongings. Also, if the    Climb with common adventurer
                                                                     Requires success roll        Not possible
```

</details>

### Technical atom 7

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-03717))_

> However, an adventurer can reduce this damage depending on their adventurer level and armor. Just like when reducing damage in weapon combat, make a defense roll using the armor's defense power as the key number, and add your adventurer level to the result to determine the damage reduced. If the defense roll comes up double ones , all damage reduction is lost, including adventurer level.

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-03718))_

```
Table 6-2: Determining Climb Target Scores
 failure.
                                        Base Target Score = 10
                                      Modifier due to wall and cliff foothold conditions:
  A  check must  be made every 10
                                        *No walls or cliffs, using a vertical rope=                              +4
 meters. If you fail on the way, add 2D-2
```

### Technical atom 8

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-03734))_

> The adventurer has 1 level in the thief skill. Thinking it'd be impossible to jump like this, he takes off his heavy chain mail. This will allow him to utilize his thief skill. The adventurer throws away his luggage and takes on a light outfit with only a short sword strapped to his waist. The target score at this time is 9 + 0 - 2 + 2 + 2 = 11 , taking into account the following conditions: 7 meters wide , no armor , no luggage , insufficient run-up , and danger . The baseline score is 3, so it

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-de1806a5-03736))_

```
Table 6-3: Determining Long Jump Target Scores
 boiling lava. At this time, considering the
                                    Feature Used                         Base Target Score
 following conditions: 7 meter width,
```


## Related pages

- [[sword-world-rpg-complete-edition-final]] - broader topic (8 shared statement(s), 4 shared atom(s))
- [[sword-world-rpg-complete-edition-score]] - shared statements and technical atoms (5 shared statement(s), 2 shared atom(s))
- [[sword-world-rpg-complete-edition-base]] - shared statements and technical atoms (2 shared statement(s), 3 shared atom(s))
- [[sword-world-rpg-complete-edition-defense]] - shared statements and technical atoms (2 shared statement(s), 3 shared atom(s))
- [[sword-world-rpg-complete-edition-strike]] - shared statements and technical atoms (3 shared statement(s), 2 shared atom(s))
- [[sword-world-rpg-complete-edition-target]] - shared statements and technical atoms (2 shared statement(s), 2 shared atom(s))
- [[sword-world-rpg-complete-edition-result]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[sword-world-rpg-complete-edition-damage-reduction]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[sword-world-rpg-complete-edition-character]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[sword-world-rpg-complete-edition-table]] - shared technical atoms (4 shared atom(s))
- [[sword-world-rpg-complete-edition-bonus]] - shared technical atoms (2 shared atom(s))
- [[sword-world-rpg-complete-edition-adventure]] - shared technical atoms (1 shared atom(s))
- [[sword-world-rpg-complete-edition-adventurer]] - shared technical atoms (1 shared atom(s))
- [[sword-world-rpg-complete-edition-agility]] - shared technical atoms (1 shared atom(s))
- [[sword-world-rpg-complete-edition-climb-agility-equipment-restriction]] - shared technical atoms (1 shared atom(s))
- [[sword-world-rpg-complete-edition-fail]] - shared technical atoms (1 shared atom(s))
- [[sword-world-rpg-complete-edition-level]] - shared technical atoms (1 shared atom(s))
- [[sword-world-rpg-complete-edition-skill]] - shared technical atoms (1 shared atom(s))
- [[sword-world-rpg-complete-edition-resist]] - shared statements (4 shared statement(s))
- [[sword-world-rpg-complete-edition-area]] - shared statements (3 shared statement(s))
- [[sword-world-rpg-complete-edition-cast]] - shared statements (2 shared statement(s))
- [[sword-world-rpg-complete-edition-effect]] - shared statements (2 shared statement(s))
- [[sword-world-rpg-complete-edition-meter]] - shared statements (2 shared statement(s))
- [[sword-world-rpg-complete-edition-power]] - shared statements (2 shared statement(s))
- [[sword-world-rpg-complete-edition-table-area-and-size-expansion]] - shared statements (2 shared statement(s))
- [[sword-world-rpg-complete-edition-type]] - shared statements (2 shared statement(s))
- [[sword-world-rpg-complete-edition-caster]] - shared statements (1 shared statement(s))
- [[sword-world-rpg-complete-edition-control-spirit-lesser]] - shared statements (1 shared statement(s))
- [[sword-world-rpg-complete-edition-poison]] - shared statements (1 shared statement(s))
- [[sword-world-rpg-complete-edition-range]] - shared statements (1 shared statement(s))
- [[sword-world-rpg-complete-edition-sorcerer]] - shared statements (1 shared statement(s))
- [[sword-world-rpg-complete-edition-section-4-5-5-final-damage-b58b3174]] - source section (4 shared atom(s))
- [[sword-world-rpg-complete-edition-section-4-6-5-final-damage-e3713cd6]] - source section (4 shared statement(s), 7 shared atom(s))

## Source

- [[sword-world-rpg-complete-edition]]
