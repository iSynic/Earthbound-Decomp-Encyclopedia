# C3 Equipment / Selector Source Contracts `C3:EE14` .. `C3:EF22`

This note captures the source-ready contracts for the three ordinary C3 helpers between the HP/PP adjustment quartet and the battle PSI metadata tables.

## Working Names

- `C3:EE14` = `CheckItemEquipmentSlotCompatibility`
- `C3:EE4D` = `RefreshWorldAndReleaseActiveVisualHandle`
- `C3:EE7A` = `ResolveStatisticSelectorValue`

## `C3:EE14` = `CheckItemEquipmentSlotCompatibility`

Entry contract:

- `A` = 1-based equipment-slot selector
- `X` = 1-based item id

The routine saves the slot selector, moves the item id into `A`, and resolves the item row through the `D5:5000` item table with stride `0x27`. It reads item byte `+0x1C`, then ANDs that byte against one of four slot masks at `C4:58AB + (slot - 1)`.

Source contract:

- return `1` if `(item_table[item_id].byte_1c & equipment_slot_mask[slot - 1]) != 0`
- return `0` otherwise

Known direct callers:

- `C1:3FCA`
- `C1:4FBF`
- `C1:5825`
- `C1:9B66`
- `C1:A84F`
- `C1:DE65`
- `C1:E031`
- `C2:4411`

This keeps the helper's role high confidence without forcing the human-facing names of the four equipment slots yet.

## `C3:EE4D` = `RefreshWorldAndReleaseActiveVisualHandle`

This helper is broader than the older battle-selection name implied.

Body contract:

1. calls `C0:34D6` / `SortAndExport_MushroomizedWalkingEntries`
2. calls `C0:7B52` / `Refresh_VisibleEntityScreenPositions`
3. calls `C1:004E` / `PumpTextWaitFrame`
4. calls `C0:943C` / `MarkWorldObjectChainForSetup`
5. if `$B4A8 != #$FFFF`, clears the high `$C000` bits in `$10B6 + ($B4A8 * 2)`

The last step mirrors the single-handle form of `C0:9451`'s broader `$10B6 &= #$3FFF` chain release, but it only touches the active visual/presentation handle named by `$B4A8`.

Known direct callers:

- `C1:B590`
- `C1:BAF1`
- `C2:2FF1`
- `C4:5955`

The caller spread matters: `C1:BAF1` reaches this after battle PSI row state is copied back into live `$99DC` slot bytes, `C4:5955` reaches it after a character-record byte write in the level/stat update neighborhood, and `C2:2FF1` reaches it from a post-transition/frame path. The shared contract is refresh plus active-handle release, not battle selection itself.

## `C3:EE7A` = `ResolveStatisticSelectorValue`

Entry contract:

- `A` = statistic selector index

Return contract:

- result low word or pointer low word is returned in the caller's `$06`
- result high word or pointer bank/high word is returned in the caller's `$08`

The routine creates a temporary direct page 16 bytes below the caller's direct page. That is why its final local stores to `$16/$18` become the caller's `$06/$08` after `PLD`.

The selector table is `C4:550F`, with fixed 3-byte records:

- byte `0` = kind/shape byte
- bytes `1..2` = payload word

Source contract by kind:

- high bit clear: fixed-width inline string/buffer form; return the payload word and current data bank as a pointer-like result
- `0x81`: indirect byte scalar; dereference the payload word, return the byte zero-extended
- `0x82`: indirect word scalar; dereference the payload word, return the word
- other high-bit forms currently used as `0x84`: pointer/string form; dereference the payload word as a pointer pair and return that pair

Known direct caller:

- `C1:7782`, from the live `0x19 27` statistic-selector text-command leaf

The table is also consumed by the sibling `C1:4819` string-character reader and the `C1:9249` display-side statistic printer, so this helper should stay named around selector-value resolution rather than around any one caller's display format.

## Confidence

- `C3:EE14` slot mask predicate: high confidence
- `C3:EE4D` refresh chain plus `$B4A8`-gated `$10B6 &= #$3FFF`: high confidence
- `C3:EE7A` selector-table record resolver and caller `$06/$08` return convention: high confidence
- final human-facing names for each `C4:550F` selector and each `C4:58AB` equipment slot: still intentionally softer
