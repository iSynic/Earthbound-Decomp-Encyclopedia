# Battle PSI Ability Table `D5:8A50`

This note captures the current best local model for the row family rooted at `D5:8A50`.

See also [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md).
See also [battle-psi-category-list-family-c1caf5-c1cb7f.md](notes/battle-psi-category-list-family-c1caf5-c1cb7f.md).
See also [battle-psi-menu-controller-c1cc39-ce73.md](notes/battle-psi-menu-controller-c1cc39-ce73.md).
See also [battle-choice-text-family-c1b2ec-b997.md](notes/battle-choice-text-family-c1b2ec-b997.md).
See also [battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md](notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md).

## Main result

`D5:8A50` is no longer best treated as an anonymous sibling metadata blob.

The strongest current local-plus-reference-backed read is that this is the battle PSI ability table, with 15-byte rows.

That promotion now rests on four independent anchors:

- local battle PSI menu readers like `C1:BB21 -> C1:C8BC`
- the battle PSI entry-list helpers `C1:CAF5` and `C1:CB7F`
- deeper helper use through `C1:C853`
- the direct reference-side bridge from `refs/ebsrc-main/.../src/data/battle/psi_abilities.asm`, whose row layout matches the local bytes exactly

## Row stride and boundary

The 15-byte split is the healthiest current layout.

With `stride = 0x0F`, the rows become coherent and repeat in stable PSI id and level groups:

- row `0` is a zeroed dummy
- rows `1 .. 52` behave like live PSI ability rows
- the data stops behaving like coherent 15-byte ability rows immediately after that

That is much healthier than the older misleading 12-byte split.

## Strongest current field map

The currently strongest row map is:

- byte `+0` = `PSI_ID`
  - examples from the local row order now line up cleanly with the reference table: Rockin, Fire, Freeze, Thunder, Flash, Starstorm, Lifeup, Healing, Shield, PSI Shield, Offense Up, Defense Down, Hypnosis, Magnet, Paralysis, Brainshock, Teleport
  - value `1` is now safely the Rockin or favorite-thing PSI-name family, because `C1:C403` routes it straight to `$9825`
  - `C1:C8BC` also uses this byte for the explicit Thunder special case
- byte `+1` = `PSI_LEVEL`
  - values now line up cleanly as alpha, beta, gamma, sigma, omega
  - `C1:CA06` reads this byte and routes through `C3:F112` into the suffix formatting table
- byte `+2` = `PSI_CATEGORY`
  - locally matches the battle-menu category families cleanly as offense, recover, assist, and other
  - rows `51` and `52` are now the strongest current local-plus-reference-backed `OTHER` anchors, and both belong to the Teleport pair
- byte `+3` = `PSI_TARGET`
  - locally matches enemy, ally, and nobody-style targeting classes
- word `+4` = associated battle action id
  - proven by `C1:CCB6`, `C1:CD49`, `C1:C9D6`, and the battle PSI menu front end
  - this is the field the battle PSI menu stores into `battle_menu_selection::selected_action`
  - it is also the field used when the menu compares against the associated `D5:7B68` row for PP-availability and targeting behavior
  - `C1:C8BC` normally uses this field to reach the ordinary action-row-derived menu-entry naming path
  - the controller at `C1:CC39 .. CE73` also uses this field to drive its PP guard and final targetting-resolution handoff
  - source constants in `C1:C8BC` and `C1:CB7F` now name this field as
    `BattlePsiAbilityAssociatedActionWord`
- bytes `+6..+8` = Ness, Paula, and Poo learn levels
  - the raw values line up exactly with the reference battle PSI ability rows
  - this is also reinforced by the parallel field usage in `refs/ebsrc-main/.../src/battle/generate_psi_list.asm`
  - the CoilSnake `psi-ness-omega-level-probe` changed ability row 4 byte `+6`
    at `D5:8A92`, and `C1:C1BA` reads the character-specific learn-level byte
    before comparing it against the party member's current level
- byte `+9` = menu `x` position
  - consumed by `C1:C452`
  - passed into `C1:153B` while building the printed PSI menu entries
  - the repeated values `9, 11, 13, 15` fit menu-column spacing exactly
- byte `+10` = menu `y` position
  - consumed directly by `C1:C452`
  - passed to `C4:38A5` before the category and suffix print steps
  - the grouped values `0, 1, 2` fit menu-row placement exactly
- bytes `+11..+13` = description or help text pointer
  - proven by `C1:BB34 .. BB67`, which displays that pointer through `C1:86B1`

The remaining weak field is much narrower now:

- byte `+14` still behaves like padding or an unused trailing byte in the current table
- the older PP-cost reading for the middle bytes is now retired
  - the battle PSI menu actually checks current PP against the associated `D5:7B68` action row, not against the `D5:8A50` middle bytes

## Description pointers are clearly PSI help text

The description-side pointer field is especially healthy.

Examples:

- early rows point into `EF:4E20 .. 4F1C`, which match the offensive PSI explanation block
- later rows point into `EF:5049 .. 5777`, which continue the recovery, assist, and other PSI help-text families

So the row family is not just behavior metadata. It really does carry the menu-side PSI description layer too.

## Safest current interpretation

The safest current summary is:

- `D5:8A50` is the battle PSI ability table
- the healthiest row size is 15 bytes
- the row layout now locally matches the reference `psi_ability` structure almost field-for-field
- the important fields are PSI id, level, category, target, battle action id, learn levels, menu position, and description pointer
- the PSI-name side is now split more cleanly: `C1:CA06` uses `PSI_ID` and `PSI_LEVEL` directly, while `C1:C8BC` usually routes through the associated action row and only bypasses that path explicitly for Thunder

The remaining soft edge is mostly just whether byte `+14` deserves a stronger name than padding or trailing unused byte. The table identity itself is now in very good condition.


