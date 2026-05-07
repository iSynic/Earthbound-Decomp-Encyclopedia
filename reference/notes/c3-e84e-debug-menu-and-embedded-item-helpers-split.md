# C3 `E84E` Debug Menu Data and Embedded Item Helpers Split

`C3:E84E` is a mixed bankconfig row. It starts as debug menu data, then contains two ordinary 65816 helper entry points before the next addressed include at `C3:E9F7`.

## Working Names

- `C3:E977` = `ReadCharacterInventorySlotByte`
- `C3:E9A0` = `CheckEquippedInventorySlotReference`

## Split Result

The source/data split should be:

| Range | Size | Role |
| --- | ---: | --- |
| `C3:E84E..E976` | `0x129` | debug menu data/text payloads from the ebsrc bankconfig neighborhood |
| `C3:E977..E99F` | `0x29` | `ReadCharacterInventorySlotByte` source helper |
| `C3:E9A0..E9F6` | `0x57` | `CheckEquippedInventorySlotReference` source helper |
| `C3:E9F7..` |  | next addressed source include, already split as `unknown/C3/C3E9F7.asm` |

The ebsrc bankconfig corroborates the mixed shape. Between `.INCLUDE "data/unknown/C3E84E.asm"` and `.INCLUDE "unknown/C3/C3E9F7.asm"`, it includes debug menu data files and then `misc/get_character_item.asm` plus `misc/check_item_equipped.asm`. The local `refs/ebsrc-main` checkout does not currently contain those two `misc/*.asm` source files, but the bankconfig names and ROM call sites line up with the local helper boundaries.

## Byte-Level Evidence

`C3:E977` begins with a normal source prologue:

- `REP #$31`
- direct-page frame setup
- calls `C0:8FF7` with `Y = #$005F`
- computes `$99F1 + ((character - 1) * 0x5F) + (slot - 1)`
- returns the selected inventory byte

`C3:E9A0` begins immediately after the `RTL` at `C3:E99F` and has the same direct-page style. It maps the selected character record, reads `$99FF`, `$9A00`, `$9A01`, and `$9A02`, and returns `1` if any byte matches the requested equipped-slot reference value.

## Direct Callers

`C3:E977` has 14 direct control-flow callers:

- `C1:3406`
- `C1:355D`
- `C1:35F0`
- `C1:3634`
- `C1:37A6`
- `C1:387E`
- `C1:572E`
- `C1:581E`
- `C1:59D0`
- `C1:6066`
- `C1:9195`
- `C1:AFA1`
- `C1:CEA4`
- `C2:3998`

`C3:E9A0` has 4 direct control-flow callers:

- `C1:57AE`
- `C1:9956`
- `C1:A0F6`
- `C1:A860`

There are no direct control-flow callers to the `C3:E84E` row start in the current xref scan, which supports treating the row start as data and the two internal labels as the source units.

## Tooling Impact

`tools/build_c3_source_data_map.py` now marks `C3:E84E` as `mixed-data-source-row`, and `tools/build_c3_source_extraction_candidates.py` promotes `C3:E977` and `C3:E9A0` as embedded source units with the correct sizes.

This means a future source emitter should not emit `data/unknown/C3E84E.asm` as one opaque block if it wants C3 helper source. It should preserve the leading debug data payload, then carve the two helper routines as ordinary source.
