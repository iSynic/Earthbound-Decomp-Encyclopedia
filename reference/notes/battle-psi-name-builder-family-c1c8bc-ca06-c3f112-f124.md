# Battle PSI Name Builder Family `C1:C8BC / C1:CA06 / C3:F112 / C3:F124`

This note captures the current best local model for the battle PSI name-building lane under the bank `01` battle PSI menu.

See also [battle-psi-menu-metadata-family-c1c853-c1c8bc.md](notes/battle-psi-menu-metadata-family-c1c853-c1c8bc.md).
See also [battle-psi-ability-table-d58a50.md](notes/battle-psi-ability-table-d58a50.md).
See also [battle-psi-category-list-family-c1caf5-c1cb7f.md](notes/battle-psi-category-list-family-c1caf5-c1cb7f.md).

## Main result

The battle PSI menu now has two distinct local naming paths:

- `C1:CA06` is the cleaner PSI-id-plus-rank display path
- `C1:C8BC` is the second-stage PSI menu row builder, and it normally derives a coarse encoded name row from the associated `D5:7B68` action row before appending the PP cost
- `PSI_ID == THUNDER` is the one explicit local bypass from that ordinary action-row-derived name-row path

Both local naming paths are now source-backed in `src/c1/c1_ca06_build_psi_rank_name.asm` and `src/c1/c1_c8bc_format_battle_psi_menu_entry_row.asm`.

Source polish follow-up (2026-05-06): `C1:CA06` now names the C4 fixed-string
rank suffix printer as `C447FB_PrintFixedStringWithWrapPreflight`, so the
direct PSI-id-plus-rank path has no raw helper-call edges.

That is stronger than the older wording that only said Thunder had some unexplained special case.

## `C3:F124` is fixed-width encoded menu-entry row data

`C1:C8BC` copies exactly `0x14` bytes from `C3:F124` through `C1:0EFC`.

That gives a strong local structural result:

- `C3:F124` is not a pointer table
- it is not code
- it is a fixed-width encoded row block consumed directly by the battle PSI menu
- the healthiest current row size is `20` bytes

The raw table also behaves like a finite row family:

- coherent 20-byte rows run from `C3:F124` through `C3:F1D8`
- code starts immediately after that at `C3:F1EC`

So the safest current name is: encoded battle PSI menu-name or menu-entry row table.

## `C3:F112` and `C3:F11C` are adjacent companion row tables

Two smaller adjacent `C3` blocks are now healthier too:

- `C3:F112` is a 5-entry, 2-byte suffix-selection table used by `C1:CA06`
- `C3:F11C` is an 8-byte fixed encoded tail copied by `C1:C8BC` after the main `0x14`-byte row copy

`C1:CA06` proves the suffix side directly:

- it reads `D5:8A50 + 0` as `PSI_ID`
- sends that through `C1:C403`
- then reads `D5:8A50 + 1` as the rank byte
- routes that rank through `C3:F112`

The exact human-facing decode of the `C3:F112` and `C3:F11C` bytes is still softer than the control flow, but the table roles are now much healthier than before.

## Ordinary path in `C1:C8BC`

The ordinary `C1:C8BC` path is now locally clear:

1. use the current PSI-menu selection to resolve the chosen `D5:8A50` row
2. read the row's associated `D5:7B68` battle action id from `+4`
3. use that action id to read the associated `D5:7B68` row
4. use the first two action-row bytes to compute a coarse row offset into `C3:F124`
5. copy `0x14` bytes from that encoded row
6. copy the fixed `0x08`-byte companion tail from `C3:F11C`
7. append the action-row PP-cost byte through `C1:C9D6 -> C1:0DF6`

The offset math is now locally pinned:

- first selector byte contributes `selector0 * 100`
- second selector byte contributes `selector1 * 20`
- the resulting sum is added to base `C3:F124`

The source now carries these as explicit formatter constants:

- `EncodedPsiMenuDirectionStride = 0x64`
- `EncodedPsiMenuEntryRowSize = 0x14`
- `EncodedPsiMenuFixedTailSize = 0x08`
- `BattleActionTablePpCostByte = 0x03`

So the ordinary path is not directly keyed by `PSI_ID`. It is keyed by the associated action row.

## Thunder bypass in `C1:C8BC`

`C1:C8BC` first checks `D5:8A50 + 0`.

If that byte is `4`, the routine does not use the ordinary action-row-derived row-selection path. Instead it:

- treats the current PSI-table row index itself as the selector
- multiplies it by `20`
- and indexes `C3:F124` directly

Because `D5:8A50 + 0` now maps strongly to `PSI_ID`, this is a strong local statement:

- `PSI_ID == THUNDER` bypasses the ordinary action-row-derived menu-name-row selection

## Best current explanation for the Thunder bypass

The strongest safe local explanation is now a little better than “for some unknown special reason.”

Local evidence:

- the early PSI action rows for Rockin, Thunder, and Flash all share the same leading action-row byte pair `00 04`
- Freeze uses `00 01`
- Fire uses `00 03`

So the action-row-derived selector bytes are clearly coarser than a unique PSI family id. That makes the Thunder-side direct `PSI_ID` bypass structurally meaningful rather than arbitrary.

The healthiest current player-facing interpretation is:

- the ordinary `C1:C8BC` selector is too coarse to uniquely identify Thunder's intended battle-menu entry row
- so Thunder uses direct PSI-table row selection instead of the associated action-row-derived path

I am still keeping one layer cautious:

- this does not yet prove the exact human-facing encoded-row content in `C3:F124`
- and it does not fully explain why Flash and Rockin are still allowed to stay on the ordinary path
- but it is now the strongest current local reason for the explicit Thunder check

## `C1:CA06` is the cleaner PSI-id-plus-rank display path

`C1:CA06` is much simpler than `C1:C8BC`:

- it reads `PSI_ID` from `D5:8A50 + 0`
- calls `C1:C403`
- reads `PSI_LEVEL` from `D5:8A50 + 1`
- indexes `C3:F112`
- then displays the result

So the safest current split is:

- `C1:CA06` = direct PSI-id-and-rank label builder
- `C1:C8BC` = second-stage battle PSI menu-entry row builder with PP-cost append

## Safest current interpretation

The safest current summary is:

- `C3:F124` is a fixed-width encoded battle PSI menu-entry row table with 20-byte rows
- `C3:F112` is the adjacent suffix-selection table keyed by `PSI_LEVEL`
- `C1:CA06` is the cleaner direct PSI-id-plus-rank display helper
- `C1:C8BC` is the second-stage battle PSI menu row builder and normally uses coarse action-row-derived row selection
- Thunder is the one explicit local case where the routine bypasses that coarse action-row path and indexes the encoded row table directly by `PSI_ID` row
- the strongest current player-facing explanation is that the ordinary action-row-derived selector is too coarse to uniquely pick Thunder's intended battle-menu entry row

The remaining soft edge is narrower now: the exact decoded contents of the encoded `C3:F124` and `C3:F11C` rows, not whether the Thunder bypass itself needs a real user-facing explanation.
