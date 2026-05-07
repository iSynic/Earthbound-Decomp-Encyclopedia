# Battle PSI Category List Family `C1:CAF5 .. C1:CB7F`

This note captures the current best local model for the battle PSI menu helpers `C1:CAF5` and `C1:CB7F`.

See also [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md).
See also [battle-psi-ability-table-d58a50.md](notes/battle-psi-ability-table-d58a50.md).
See also [battle-choice-text-family-c1b2ec-b997.md](notes/battle-choice-text-family-c1b2ec-b997.md).
See also [battle-psi-menu-controller-c1cc39-ce73.md](notes/battle-psi-menu-controller-c1cc39-ce73.md).

## Main result

These are not generic menu helpers.

`C1:C452..C853` is now source-backed at `src/c1/c1_c452_build_shared_battle_psi_entry_list.asm`, which makes the shared list-builder side concrete instead of byte-preserved.
`C1:CAF5..CB7F` is now source-backed at `src/c1/c1_caf5_build_battle_psi_category_entry_list.asm`, closing the category-specific list builder.
`C1:CB7F..CE85` is also source-backed at `src/c1/c1_cb7f_has_battle_psi_category_entries.asm`, covering the category predicate and ordinary battle PSI controller strip above it.
The predicate family underneath it, `C1:C165..C452`, is source-backed at `src/c1/c1_c165_current_character_knows_psi.asm`.

Source polish follow-up (2026-05-06): the shared list builder and
category/predicate helpers now name their remaining menu/window helper edges in
source. `C1:C452` names the active text-entry chain clear, window update scope,
and cursor-position helper calls; `C1:CAF5` names the focus/window tick calls;
and `C1:CB7F` names the category-window focus setter.

The strongest current local-plus-reference-backed read is:

- `C1:CAF5` builds the second-stage battle PSI entry list for the currently chosen battle PSI category
- `C1:CB7F` tests whether the chosen category has at least one valid entry for the current acting character
- both sit directly under the battle PSI menu controller in `C1:CC39 .. CE73`

## Working Names

- `C1:C452` = `BuildSharedBattlePsiEntryList`
- `C1:C1BA` = `HasPsiEntryForCategoryMask`
- `C1:C32A` = `CanCharacterOpenPsiLane`
- `C1:CAF5` = `BuildBattlePsiCategoryEntryList`
- `C1:CB7F` = `HasBattlePsiCategoryEntries`
- `C1:CBCD` = `OpenBattlePsiCategorySelectionStage`
- `C1:CC39` = `OpenBattlePsiMenuController`
- `C1:CE73` = `ExitBattlePsiMenuController`

## Category Helper Split

That matches the reference battle PSI menu lane unusually well.

## `C1:CAF5` builds the category-specific entry list

`C1:CAF5` currently has one pinned direct caller:

- `C1:CC77 -> C1:CAF5`

The strongest current local model is:

- input `A` is the selected battle PSI category number
- it resolves the current acting character through `$89CA -> $986F`
- category values `1`, `2`, and `3` each install a different small mask pair into `$0E/$0F`
- it then forwards the acting character and those masks into `C1:C452`

So the safest current read is that `CAF5` is a category-to-mask dispatcher over the shared battle PSI list generator at `C1:C452`.

The strongest current mapping is now:

- category `1` -> usability mask `2`, category mask `1` = battle offense PSI
- category `2` -> usability mask `2`, category mask `2` = battle recover PSI
- category `3` -> usability mask `2`, category mask `4` = battle assist PSI
- category `4` -> usability mask `3`, category mask `8` = other PSI

The first three are the live ordinary battle-menu cases. The fourth branch exists locally but has no pinned current direct caller in the ordinary battle PSI menu path.

## `C1:CB7F` is the category availability predicate

`C1:CB7F` currently has one pinned direct caller:

- `C1:CC67 -> C1:CB7F`

The strongest current local model is:

- input `A` is the selected battle PSI category number
- input `X` is the current acting character id
- the helper maps categories `1`, `2`, and `3` into the same battle-usability and PSI-category masks
- it then calls `C1:C1BA` and returns a nonzero result when that category has at least one usable PSI entry for the acting character

So this is best treated as the battle PSI category validation gate that runs before the second-stage PSI entry window is opened.

## How this connects to `C1:C452`

The common generator `C1:C452` is now much healthier in context.

The strongest current local-plus-reference-backed read is that it is the shared PSI entry-list builder underneath these battle-menu helpers, parallel to the reference `GENERATE_PSI_LIST` lane.

Useful local anchors:

- it consumes the same usability and category masks staged by `CAF5` and `CB7F`
- it reads row bytes from `D5:8A50`
- it uses byte `+10` as menu `y`
- it uses byte `+0` through `C1:C403` for PSI family naming
- it uses byte `+1` through the `C3:F112` suffix side for rank naming
- it uses byte `+9` through `C1:153B` while building the printed PSI menu entry rows

That makes the current family picture much cleaner:

- `CB7F` = can this battle PSI category be opened for this character right now?
- `CAF5` = build the entry list for the chosen category
- `C452` = shared battle PSI entry-list builder over the battle PSI ability table
- `CC39 .. CE73` = ordinary battle PSI menu controller above both helpers

## Safest current interpretation

The safest current summary is:

- `CAF5` and `CB7F` are battle PSI category helpers, not generic menu routines
- `CAF5` dispatches battle category selection into the shared PSI list generator
- `CB7F` validates category availability for the acting character
- both sit directly under the ordinary battle PSI menu controller at `CC39 .. CE73`

The remaining soft edge is mostly naming polish, not runtime shape. This family is now in good condition.
