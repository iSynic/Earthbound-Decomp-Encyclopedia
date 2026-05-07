# Battle PSI Table Helpers `C1:C046` and `C1:C165`

This note covers the unknown includes at `C1:C046` and `C1:C165`.

See also [battle-psi-ability-table-d58a50.md](notes/battle-psi-ability-table-d58a50.md).
See also [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md).
See also [battle-psi-category-list-family-c1caf5-c1cb7f.md](notes/battle-psi-category-list-family-c1caf5-c1cb7f.md).

## Main Result

`C1:C046` and `C1:C165` are deeper helpers in the battle PSI menu/list-generation family.

`C1:C165..C452` is now source-backed at `src/c1/c1_c165_current_character_knows_psi.asm`, covering the live PSI-state predicate, category/use-mask predicate, eligible-user helpers, and PSI family-name printer.

They sit immediately before the already-documented `C1:C1BA`, `C1:C32A`, `C1:C367`, `C1:C373`, `C1:C3B6`, `C1:C403`, and `C1:C452` lane. The safest current split is:

- `C1:C046` = PSI menu cursor/category display refresh helper
- `C1:C165` = current-character PSI-known-state predicate over live party PSI bytes

## Working Names

- `C1:C165` = `CurrentCharacterKnowsPsi`
- `C1:C1BA` = `HasPsiEntryForCategoryMask`
- `C1:C32A` = `CanCharacterOpenPsiLane`
- `C1:C367` = `CheckBattlePsiUserEligibility`
- `C1:C373` = `FindFirstEligibleBattlePsiUser`
- `C1:C3B6` = `CountEligibleBattlePsiUsers`
- `C1:C403` = `PrintPsiFamilyName`

## `C1:C046`: PSI Menu Cursor Display Refresh

`C1:C046` takes a selector in `A`.

The first half maintains menu print state:

- if current menu/window state from `C1:04B5` is greater than `0x0E` and the incoming selector is at least `0x20`, it clears/repositions through `C4:38B1`, `C4:5E96`, `C1:04D8`, and `C4:38A5`
- it then indexes `C3:EF26` by `selector - 0x10`
- a zero byte in `C3:EF26` means there is no PSI-list group for this selector, so it optionally clears the previous printed state and prints the raw selector through `C1:0BA1`

The nonzero path treats the table byte as a grouped PSI-list selector:

- sets `$9E29 = 1`
- decrements the `C3:EF26` result to form a group index
- indexes `C3:F016` to get an entry count or slice width
- builds a pointer under `E0:1359`
- prints the first eight bytes of the group through `C4:5C90`
- if the slice is longer than eight bytes, prints the remaining bytes from the next half-row
- flushes the pending `$9D23` scratch rows through `C4:5DDD`
- rotates around `$9E27`, printing labels at `0x0190 + row_index` through `C1:0BA1`
- restores display position through `C1:04B5`, `C1:04D8`, and `C4:38A5`

So this helper is not a generic text printer. It refreshes the compact PSI menu selector/category side using small C3/E0 metadata tables plus the shared C4 text-placement primitives.

## `C1:C165`: Known-PSI State Predicate

`C1:C165` takes a party character id in `A`.

It computes the character's live party block offset with stride `0x5F`, starts at `$99DC`, and scans seven bytes. For each nonzero live PSI byte:

- subtracts `1`
- folds the scan index into a table offset
- indexes `C3:F0B0`
- returns `0` if the table entry is nonzero
- returns `1` if the table entry is zero

If all seven live bytes are zero, it also returns `1`.

This function is only directly called by `C1:C32A`, where it acts as an early eligibility gate before the more specific `C1:C1BA` predicate runs. The surrounding family uses the `D5:8A50` PSI ability table and the party registry at `$986F/$98A4`, so the strongest current wording is:

- `C1:C165` answers whether a character's current live PSI state allows the category/list predicate to continue
- `C1:C1BA` then tests the requested category/use masks against individual `D5:8A50` rows
- `C1:C32A` combines both into the higher-level "can this character open this PSI lane?" predicate

## How This Fits the Existing PSI Notes

The rest of the local family now lines up cleanly:

- `C1:C367`: tiny wrapper over `C1:C32A` for one standard mask pair
- `C1:C373`: first eligible party member for that mask pair
- `C1:C3B6`: count eligible party members for that mask pair
- `C1:C403`: print a PSI family name, including the special favorite-thing/Rockin path
- `C1:C452`: shared PSI entry-list builder over `D5:8A50`
- `C1:CAF5`: battle category-to-mask dispatcher
- `C1:CB7F`: battle category availability predicate
- `C1:CC39..CE73`: ordinary battle PSI menu controller

`C1:C046` and `C1:C165` therefore fill two of the small holes under the same PSI menu subsystem rather than opening a new subsystem.
