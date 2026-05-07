# Battle PSI Menu Metadata Family `C1:C853 .. C1:C8BC`

This note captures the current best local model for the helper pair `C1:C853` and `C1:C8BC`, which sit underneath the battle PSI menu and the `D5:8A50` table family.

See also [battle-choice-text-family-c1b2ec-b997.md](notes/battle-choice-text-family-c1b2ec-b997.md).
See also [battle-psi-user-selection-front-end-c1b5b6-b7c6.md](notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md).
See also [battle-psi-ability-table-d58a50.md](notes/battle-psi-ability-table-d58a50.md).
See also [battle-psi-category-list-family-c1caf5-c1cb7f.md](notes/battle-psi-category-list-family-c1caf5-c1cb7f.md).
See also [battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md](notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md).
See also [battle-psi-menu-controller-c1cc39-ce73.md](notes/battle-psi-menu-controller-c1cc39-ce73.md).

## Main result

The strongest current local read is:

- `C1:C8BC` is the second-stage battle PSI menu entry-row formatter over the `D5:8A50` PSI ability table
- `C1:C853` is a deeper PSI-targeting helper that first consults the same `D5:8A50` PSI ability rows, then conditionally falls back into `D5:7B68`

The upstream shared PSI entry-list builder at `C1:C452..C853` is now source-backed at `src/c1/c1_c452_build_shared_battle_psi_entry_list.asm`, so this lane now has decoded source on both sides of the `C853` handoff.
The `C1:C853..C8BC` metadata resolver and `C1:C8BC..CA06` row formatter are now both source-backed as well.

Source polish follow-up (2026-05-06): `C1:C853` now names its
`C3:E4E0` window tick edge, and `C1:CA72` now names the long `C1:C853` metadata
refresh join used after clearing battle-sprite row effects. This keeps the
outer PSI-user refresh lane tied directly to the same metadata resolver used by
the second-stage menu family.

## Working Names

- `C1:C853` = `ResolveBattlePsiTargetingMetadata`
- `C1:C8BC` = `FormatBattlePsiMenuEntryRow`

## Metadata Helper Split

That is stronger than the older “mystery sibling table” wording around `D5:8A50`.

## `C1:C8BC` is directly on the PSI menu path

There is now a clean local-plus-reference bridge:

- local caller: `C1:BB21 -> C1:C8BC`
- lower-controller caller: `C1:CC7B .. CC88 -> C1:C8BC`
- outer front-end caller: `C1:B65D .. B674 -> C1:C8BC`
- reference-side caller: `refs/ebsrc-main/.../src/battle/battle_psi_menu.asm`

`C1:BB06 .. BB70` behaves like a PSI-menu-side text refresh wrapper:

- it caches the current selection in `$9D19`
- calls `C1:C8BC` when the selection changes
- then indexes `D5:8A50` at `entry * 15 + 0x0B`
- and displays the resulting text through `C1:86B1`

So the simplest safe read is that `D5:8A50` is the battle PSI ability table, including at least one description or help-text pointer field used for the currently highlighted entry.

## `C1:C8BC` is now structurally clearer

The deeper name-building side is now healthier too.

The ordinary path in `C1:C8BC`:

- resolves the current `D5:8A50` row
- reads the associated `D5:7B68` action id from `+4`
- uses the associated action row's first two bytes to compute a coarse encoded-row selector into `C3:F124`
- copies `0x14` bytes from that encoded row through `C1:0EFC`
- copies a fixed `0x08`-byte companion tail from `C3:F11C`
- and appends the action-row PP-cost byte through `C1:C9D6 -> C1:0DF6`

The source now names the concrete table and row contracts:

- `D5:8A50` = `BattlePsiAbilityTable`, stride `0x0F`
- `D5:7B68` = `BattleActionTable`, stride `0x0C`
- `C3:F124` = encoded PSI menu-entry rows, stride `0x14`
- `C3:F11C` = fixed encoded menu-entry tail, size `0x08`
- action row byte `+0x03` = PP cost byte appended at the end of the row

The special path is now sharper too:

- `C1:C8BC` first checks `D5:8A50 + 0`
- when `PSI_ID == THUNDER`, it bypasses the ordinary action-row-derived selector and indexes `C3:F124` directly by current PSI-table row

The best current player-facing explanation is now stronger too:

- the ordinary action-row-derived selector is coarser than a unique PSI family id
- that coarse selector is enough for the ordinary path in general
- but Thunder gets the one explicit direct `PSI_ID` fallback because the coarse action-row-derived path is not specific enough for its intended menu-entry row

## `C1:C853` uses that same metadata family

`C1:C853` is the stronger structural helper underneath the same lane.

The current best local model is:

- input `A` is preserved as a current PSI-menu selection-like value or chosen PSI-user id
- the routine resolves the acting slot through `$99CE`
- it uses `C2:032B` and `C1:C452` after building small local selector values
- `C1:C452` is the deeper battle PSI menu placement and availability helper under the same lane
- `C1:C403` and `C1:CA06` provide the cleaner direct PSI-id and rank printing side on top of that

That makes the relationship much healthier:

- `D5:8A50` is not just another text table
- it is PSI-menu metadata that can shape later target or behavior handling
- `D5:7B68` remains the broader battle-action table used when the entry-row builder defers to ordinary action rows
- the outer front end at `B5B6 .. B7C6` reuses `C1:C853` as its PSI-user-side display helper before the lower direct entry-selection lane starts

## Safest current interpretation

The safest current summary is:

- `D5:8A50` is the battle PSI ability table
- `C1:C8BC` is the second-stage PSI menu entry-row formatter over that table
- `C1:C853` is a deeper PSI-targeting helper that consults the same metadata and may hand off into the ordinary `D5:7B68` action table
- `C1:CC39 .. CE73` is the lower ordinary battle PSI category-plus-entry controller
- `C1:B5B6 .. B7C6` is the outer PSI-user-selection front end that also reuses `C1:C8BC`
- the Thunder special case now has a healthier explanation than before: the ordinary action-row-derived selector appears to be too coarse for Thunder's intended menu-entry row

But this subsystem identity is now much healthier than before.
