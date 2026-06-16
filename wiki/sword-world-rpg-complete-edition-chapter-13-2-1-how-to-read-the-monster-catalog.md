---
category: source
summary: Chapter 13.2.1 of the Sword World RPG - Complete Edition, explaining how to read the monster catalog data format.
sources: Sword World RPG - Complete Edition.pdf
updated: 2026-06-16
---

This page explains how to read the monster catalog data format as described in Chapter 13.2.1 of the Sword World RPG - Complete Edition.

## Monster Catalog Data Format

Monster data is written in a specific format to provide comprehensive information about each monster. The data includes various attributes such as monster level, rarity, agility, movement speed, number, frequency, intellect, reaction, attack points, strike points, evasion points, defense points, life points/resistance, mental points/resistance, special abilities, habitat, perception, and languages.

## Monster Level

This is a score that corresponds to a character's adventurer level, and represents the general strength of that monster. If it's 1, it's an extremely weak monster. If it's 10, even a seasoned adventurer will have a hard time crossing swords with it. Monster level, similar to a character's adventurer level, indicates how difficult it is for a monster to die. When a monster suffers damage from magic, etc., the damage can be reduced by this monster level score.

## Rarity

This is a score that indicates whether the monster is famous or not. The lower this score, the more well-known the monster is. When using the sage skill's monster check ability (see p. 118), this rarity is the target score for a success roll.

## Agility

Similar to agility, which is a character ability score, this represents the quickness of a monster. It's used to determine the order of actions in a combat round.

## Movement Speed

Indicates the speed at which the monster moves. Similar to a character's agility, monsters can move up to _movement speed_ meters per round during normal movement, or _movement speed x 3_ meters per round during full movement. It's also used to determine whether a character can escape from the monster. If the monster's movement speed is greater than the character's agility, the character will not be able to escape from the monster unless they think of something.

Some monsters fly in the sky, and some travel in water or underground. For such monsters, two types of movement speed are written. The number _before_ the slash (/) is movement speed on the _ground_, and the number _after_ the slash is movement speed when performing _special movements_. In rare cases, there are monsters that do not move on the ground (such as those that are always floating in the air), so in these cases, the movement method is written in parentheses immediately after the movement speed.

## Number

This is the most common number appearing when encountering that monster. Monsters that act in groups are usually encountered in large numbers, while monsters that have a strong sense of territory and really only exist alone in a certain area are unlikely to be encountered in numbers greater than one. This data is not exact, and the game master may change the number appearing depending on the circumstances of the scenario. However, in order to do so, you will need a reason that the players can understand.

## Frequency

This is the frequency at which the monster appears. The types in descending order of frequency are **frequent**, **moderate**, **rare**, and **very rare**. It's a bit unnatural to have _rare_ or _very rare_ monsters repeatedly appear in a scenario. In such cases, it would be best to provide a reason that the players can understand.

## Intellect

Indicates the monster's degree of intellect. There are eight types: **none**, **almost none**, **obeys commands**, **animal**, **low**, **human**, **high**, and **very high**.

If it says _none_, that means it doesn't have intelligence, so to speak. It does not think, nor does it even have instincts. It acts only on reflex. It's similar to how a mimosa closes its leaves when touched. Spells that affect the mind have no effect on these monsters. If you were to convert it to an intelligence score, it would be _0_.

If it says _almost none_, then it has almost no intellect. They have no advanced thinking and have almost no means of communicating their intentions. They only act on instinct. This is the intellectual standard of lower animals such as insects. If you were to convert it to intelligence, it would be _1-2_. Of course, spells that affect the mind cannot be expected to have any effect.

If it says _obeys commands_, it's common among magical creatures created by magic, the undead, etc. If given a command-- the only ones who can give commands are those who directly created the monster or those who used magic to give the command -- they will faithfully carry it out, but they cannot make their own decisions. However, they have a memory comparable to that of humans, and can answer questions accurately if asked (if commanded to _answer the question_). If you were to convert it to intelligence, it would be _1_ for judgment ability, but around _10_ for memory if they're able to remember. Since they do not act on their own judgment, spells that affect the minds are ineffective.

If it says _animal_, it means literally the same degree as an animal. They can distinguish their master and will follow their commands (if they're trained). Also, they have enough judgment ability to quickly run away if their life is in danger. If you were to convert it to intelligence, it would be around _3 to 5_. However, they can sometimes display surprising judgment, although this is something that has been learned as an instinct. There are known stories of parent birds feigning injury to keep predators away from their nests, and predators using intimidation to lure prey to ambush spots for their mates.

If it says _low_, it means that while the intellect is not as high as that of humans, it is still quite high. They can also use primitive tools, words, and a very limited number of written characters. Although they're somewhat slow, they're able to make accurate judgments in normal activities. However, they're not good enough to fight using advanced tactics, and are easily fooled by simple words and tricks. If you were to convert it to intelligence, it would be around _6 to 8_.

If it says _human_, it means an intellect that's almost the same as that of a human. They can handle tools, words, text, etc. freely. If you were to convert it to intelligence, it would be _10 to 15_.

If it says _high_, it means that it has a greater intellect than the average human. For a human, you could even use the adjective _wise_. If you were to convert it to intelligence, it would be _18 to 20_.

If it says _very high_, it means their intellect is beyond the reach of normal humans. A human with this much intellect would probably go down in history as a great genius. If you were to convert it to intelligence, it would be _24 or greater_.

## Reaction

This represents the monster's general reaction when it encounters adventurers. It can be **violent**, **adversarial**, **neutral**, **friendly**, **hunger-based**, or **command-based**.

If it says _violent_, that means it will attack immediately. Examples include undead who have hatred for the living, and plants that act solely on reflex. Many have no concept of running away.

If it says _adversarial_, it means they consider adventurers (human or fae) to be their enemies. The specific actions they'll take will vary depending on the power dynamic (difference in number) between the adventurers and monsters, as well as the intelligence of the monsters. Even if the monster is adversarial, if the adventurers have the superior numbers, it will not attack immediately and may try to use trickery.

If it says _neutral_, it means the monster holds no special feelings of hostility nor allyship towards the adventurers. Depending on the situation, they can be your enemy or your ally. Sometimes they simply avoid interaction and disappear.

If it says _friendly_, it means the monster has friendly feelings towards adventurers (humans and fae). If you don't feel like they're a nuisance to you, they might provide some assistance. However, if an adventurer takes hostile action, they will naturally consider retaliation. In addition, out in the world are also monsters that _get carried away_, who do things that end up causing annoyance even though they mean no harm.

If it says _hunger-based_, it means they're basically neutral. However, for carnivorous (omnivorous) animals, it can be very dangerous when they're hungry. This is because they may attack adventurers, seeing them as food.

_Command-based_ is often seen in magical creatures and lower grade undead that move according to the commands of others. They follow the instructions of their commander. Whether they consider adventurers to be enemies or not depends on the commands given to them.

There are several other reactions as well, but you can understand their meaning by looking at the explanation text after the data.

## Attack Points

This represents the monster's attack method and its accuracy. The higher this score, the more likely the monster will be able to hit you with an attack. A character must make a success roll using their evasion speed as the baseline score and these attack points as the target score. If you fail, you will suffer damage (refer to _Chapter 4: Weapon Combat_).

Some monsters have multiple attack methods. Multiple attack points are also listed for these cases. In this case, if they're written on _one_ line separated by a slash (/), it means that they can attack that number of times in one round. For example, _Horn: 12 (5)/Hoof: 12 (5)_ means that two attacks can be made with horn and hoof. Each targeted character must make a success roll to determine whether they're able to avoid the attack.

If there are multiple attack methods, but they are written on _two_ (or more) lines, the monster may have multiple attack methods, but can only use _one_ of them during a round.

The numbers in parentheses next to each attack point score are used in the optional rule _16.1: Combat in Which Monsters Roll Dice._ (see p. 261).

## Strike Points

This represents the amount of damage dealt by the monster. If a character fails to evade their attack, these strike points become damage and reduce the character's life force. A character can reduce this damage through armor (defense rolls) and adventurer level.

Monsters that have multiple attack methods also have multiple strike points written next to them. The arrangement of attack points also carries over to strike points.

If _Attack Points=Horn:12 (5)/Hoof:12 (5)_ is written as _Strike Points=17/16_, then if the horn attack hits, it'll deal 17 points of damage, and the hoof attack hits, it'll deal 16 points.

## Evasion Points

This represents the degree to which the monster can evade attacks. In order for a character to hit a monster with an attack, they must succeed on a success roll using these evasion points as the target score and their attack power as the baseline score. If you fail, your character's attack will miss.

## Defense Points

Just as characters can reduce damage through armor, monsters also have thick skin, shells, scales, etc. to reduce damage (some fae and youma may wear armor just like humans). This is represented by defense points. When a monster suffers damage from a character's (weapon) attack, they can reduce the damage by the amount of defense points. This is exactly the same as a character's damage reduction due to armor (defense rolls) and adventurer level.

Defense points are only effective against attacks such as weapons, etc. When struck by magic or similar attacks, defense points cannot reduce damage, monster level reduces damage instead. Whether or not a character can reduce damage through armor is the standard for deciding whether to use defense points or monster level.

Monster level, like adventurer level, prevents all damage, but a monster's defense points _already_ include damage reduction due to monster level. Therefore, _only_ defense points should be applied when reducing damage from weapon attacks. Monster level may _not_ be further subtracted from it.

## Life Points/Resistance

There are two numbers written. The number before the slash (/) is life points, and the number after is life point resistance.

**Life points** represents the monster's life force. When a monster suffers damage, it will lose life points. As with a character, when a monster's life points fall to 0 or less, they become disabled and, in some cases, die.

**(Life point) resistance** is a substitute for a character's _life force resistance roll_. When a character is poisoned, etc. a life force resistance roll determines whether they can avoid or reduce the effects of the poison. In the case of monsters, _life point resistance_ is used instead. When a monster is poisoned, etc. compare its resistance score with the strength of the poison (toxicity score). If the life point resistance is greater, the monster will be safe from the effects of the poison. Where a character would make a life _force_ resistance roll, a monster would use their life _point_ resistance. For characters, the resistance roll is successful if the final score of the resistance roll is _equal_ to the toxicity score, etc., but for monsters, the life point resistance must be _greater_ than the toxicity score, etc.

The baseline score when making a judgment by rolling the dice, just like a character, is written in parenthesis next to the life point resistance.

## Mental Points/Resistance

**Mental points** have the same meaning as a character's mental power. When a monster uses magic, it consumes mental points, just like a character. Monsters whose mental points are reduced to 0 (or less) by _Shade_ magic, etc. will fall unconscious.

**Mental point resistance** is a score that's a substitute for a character's _mental power resistance roll_, so when a character casts magic on a monster, this _mental point resistance_ becomes the target score.

When a character casts a spell on a monster, they must make a success roll using their magic power as the baseline score. If the final score is equal to or greater than the monster's mental point resistance, the magic will successfully be cast. Please refer to 5.1.4.4: Procedure When an Adventurer Casts Resistible Magic on a Monster (see p. 57). Conversely, for a monster to resist magic, its mental point resistance must be _greater_ than the magic's final score. A _tie_ means the magic will successfully be cast. Please be careful about this. This is done purely for consistency, so that from the character's perspective, **tied success rolls are always successful**.

## Special Abilities

Monsters may have various **special abilities**. Some breathe fire, and others are not affected by mental attacks. There are some that cannot be hurt by normal weapons, and require magic or magical weapons to defeat them.

When a monster has such special abilities, they are briefly expressed here. Since the amount of text would be enormous, we will avoid explaining each one individually here. When necessary, refer to the main text of the monster catalog and 13.6: Handling Monster Special Abilities (see p. 235).

## Habitat

This is where the monster commonly lives. If you want to have the monster appear in a place other than what's shown here, you'll need a reason that the players can understand.

## Perception

This represents the monster's sensory abilities. There are three types: **five senses**, **pseudo**, and **magic**.

_Five senses_ refer to the same five senses that humans use to perceive the outside world: vision, hearing, smell, taste, and touch. In some cases, some of these senses may be missing. Illusions that deceive monsters which lack these senses will be ineffective. It may also include specialized features such as **darkvision**, **infravision**, **illumination**, **sonar**, and **vibration sense**.

( _Darkvision_ ) means the monster can see completely in the dark. Dwarf player characters have this ability.

( _Infravision_ ) indicates that the monster can see the heat of the target, similar to a shaman's _infravision_, and can perceive it even in places where there is no normal light.

( _Illumination_ ) means the monster can see as clearly as daytime even under very weak light, such as only starlight.

( _Sonar_ ) means the monster can use sound waves or ultrasonic echoes to perceive the outside world. Therefore, they have almost no restrictions on action even in the dark.

( _Vibration sense_ ) means the monster can sense vibrations in the ground and perceive things moving around it. They cannot perceive things that are flying in the air or that are not moving.

Those whose sensory abilities are _pseudo_ have five pseudo-senses through magical means. After all, one part may be missing, or they may have special senses. In such cases, there is an organ that captures the sensation in a pseudo manner. If those organs are destroyed, the pseudo-senses will no longer be usable. For example, skeletons can use their empty eye sockets for pseudo vision. Therefore, if they're blindfolded, they won't be able to see, and they won't be able to see anything approaching from behind. Monsters whose perception is _pseudo_ can experience illusions.

Those whose sensory abilities are _magic_ perceive their surroundings with magical senses. These senses cannot be blocked or deceived by any means. Illusions are ineffective on monsters whose perception is _magic_.

## Languages

This indicates whether the monster speaks, and if so, what kind of language it uses. Only normal languages are described, and runes (except for silent spirit) are omitted. If it says _none_, then the monster does not use language (those with _obeys commands_ intellect may not speak themselves, but may understand what others are saying). For more information on language, please refer to 12.1: Rules Regarding Language (see p. 157).
