# C3 Tracked Item Sync Source Contract `C3:EBCA`

This note closes the accumulator-width caveat for `C3:EBCA`, the table-wide tracked-item lifecycle sync pass.

## Working Name

- `C3:EBCA` = `SyncPartyOverlayTrackedItemFamilyState`

## Entry Contract

- No meaningful input register is consumed by the caller-facing contract.
- The routine creates a local direct page at `D - 0x10`.
- `Y` / local `$0E` is the current row index into `D5:F4BB`.
- It returns after the first zero `item_id` row terminator.

## Loop Contract

The loop repeatedly rebuilds a long pointer to the timed item transformation table:

- `$06` = low word `F4BB`
- `$08` = bank word `00D5`
- row pointer = `D5:F4BB + index * 5`

It reads byte `+0x00` from each row as the tracked item id. If that byte is zero, the sync is complete.

For each nonzero tracked item id:

1. The item id is masked to one byte and passed in `X`.
2. `A = 0x00FF` is passed to `C4:5683`, which scans active party/entity inventory state for that item.
3. If `C4:5683` returns nonzero, the current row item id is passed to `C3:EAD0` (`RefreshEggFamilyLifecycleOnInsert`).
4. If `C4:5683` returns zero, the same item id is passed to `C3:EB1C` (`RefreshEggFamilyLifecycleOnRemove`).
5. The row index increments and the next row is checked.

So `C3:EBCA` is not an ordinary inventory mutation helper. It is the table-wide reconciliation pass that makes the Fresh Egg / Chick / Chicken timed-transformation registry match the current active party/inventory overlay state.

## Width Check

The previously open caveat was the accumulator width around `C3:EC00`, where the bytes look wrong if decoded in M8:

```asm
C3:EC00  A9 BB F4   lda #$F4BB
C3:EC03  85 06      sta $06
C3:EC05  A9 D5 00   lda #$00D5
C3:EC08  85 08      sta $08
```

This is a real 16-bit pointer setup, not mixed data or a hidden branch. The control-flow reason is:

- entry starts with `REP #$31`, so the first visit to `EC00` is M16
- the dispatch path uses `SEP #$20` only to pass the row item id as an 8-bit `A` input to `C3:EAD0` or `C3:EB1C`
- both callees begin with `REP #$31` and return in M16 on their observed paths
- after the callee returns, `C3:EBFB` increments the row index and falls back to `EC00` in M16

That makes the `D5:F4BB + index * 5` pointer rebuild source-safe as ordinary 16-bit accumulator code.

## Data Contract

`D5:F4BB` is the `TIMED_ITEM_TRANSFORMATION_TABLE`:

| Offset | Field |
| ---: | --- |
| `0x00` | `item_id` |
| `0x01` | `sound_effect` |
| `0x02` | `sound_frequency` |
| `0x03` | `new_item` |
| `0x04` | `delay` |

The rows currently corroborate the egg-family lifecycle:

- item `92` transforms to `168` after delay `50`
- item `168` transforms to `169` after delay `44`
- item `169` has terminal cleanup/effect metadata
- item `0` terminates the table scan

CoilSnake cross-check: `timed-item-transform-delay-probe` changed row 0
`Delay` from `50` to `51` and produced a single rebuilt-ROM byte change at
`D5:F4BF`, which is `D5:F4BB + 0x04`. That proves CoilSnake's editor-facing
`Delay` field is the same row byte consumed by the tracked-item lifecycle
helpers.

## Callers

Direct callers:

- `C1:FEC5`
- `C2:299B`
- `C2:2A10`

The C2 callers sit immediately after active party/source-array insert/remove work, which matches this routine's role as a reconciliation pass after party-composition or overlay-state changes.

## Source Translation Notes

A source version should preserve the row-table contract rather than folding the four current rows into hard-coded branches. The important shape is:

- `for row in TIMED_ITEM_TRANSFORMATION_TABLE until row.item_id == 0`
- if `CheckActiveInventoryForItem(row.item_id)` then refresh/arm the tracked-item lifecycle for that item
- else clear/remove the lifecycle slot, unless another active inventory still contains the item

## Confidence

- Width caveat: closed
- Table pointer/row stride: high confidence
- `C3:EBCA` as table-wide tracked-item lifecycle reconciliation: high confidence
- Exact player-facing naming of the overlay entity layer that triggers the sync: still belongs to the broader party-overlay notes, not to this helper's source contract
