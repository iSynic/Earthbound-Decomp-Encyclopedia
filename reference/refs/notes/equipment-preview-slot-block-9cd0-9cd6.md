# Equipment Preview Slot Block `$9CD0..$9CD6`

This note captures the current local picture of the small WRAM block used by the bank-`01` equipment preview renderer around `C1:A1D8`.

See also the consolidation overview at [equipment-preview-and-derived-state-cluster.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/equipment-preview-and-derived-state-cluster.md).

## Main result

The safest current local read is:

- `$9CD6` = selected character id for the preview renderer, stored 1-based
- `$9CD4` = small preview-ready latch cleared before setup and set once a family-specific preview block has been installed
- `$9CD0..$9CD3` = preview equipped-slot indices in the same four-family order as the live equipped-slot block:
  - `$9CD0` = weapon-family preview slot index
  - `$9CD1` = charm/pendant/cloak-family preview slot index
  - `$9CD2` = bracelet/band-family preview slot index
  - `$9CD3` = cap/ribbon/coin-family preview slot index
- `C1:A1D8` = shared bank-`01` preview/status renderer that consumes that block
- `C2:2562/25AC/260D/2673` = four slot-family-specific setup helpers that populate the preview block before calling `C1:A1D8`

So this is not a loose temporary scratch area. It is a small shadow equipped-slot block used for menu/status comparison previews.

## Local producer side

The clearest top-level path is in bank `01` around `C1:A795..A999`.

That family:

- chooses a selected character
- stores `(character id)` to `$9CD6` at `C1:A93C`
- branches on a four-way family code in `$1C`
- dispatches to one of four bank-`C2` setup helpers:
  - `1 -> C2:2562`
  - `2 -> C2:25AC`
  - `3 -> C2:260D`
  - `4 -> C2:2673`

Each of those helpers populates `$9CD0..$9CD3` and then calls `JSL C1:A1D8`.

That makes the family-code meaning strong locally: it is the same four-slot subtype order we already use elsewhere, not a new menu-only enum.

## The four setup helpers

### `C2:2562`

This helper:

- takes the incoming preview slot index and stores it to `$9CD0`
- loads the selected character from `$9CD6`
- copies live equipped-slot bytes `$9A00/$9A01/$9A02` into `$9CD1/$9CD2/$9CD3`
- calls `C1:A1D8`

So this is the weapon-family preview case: candidate weapon slot in `$9CD0`, current live non-weapon slots in the remaining bytes.

### `C2:25AC`

This helper:

- copies live weapon slot `$99FF` into `$9CD0`
- stores the incoming preview slot index to `$9CD1`
- copies live `$9A01/$9A02` into `$9CD2/$9CD3`
- calls `C1:A1D8`

So this is the second-family preview case: candidate charm/pendant/cloak slot in `$9CD1` with the other three families left live.

### `C2:260D`

This helper:

- copies live `$99FF/$9A00` into `$9CD0/$9CD1`
- stores the incoming preview slot index to `$9CD2`
- copies live `$9A02` into `$9CD3`
- calls `C1:A1D8`

So this is the bracelet/band-family preview case.

### `C2:2673`

This helper:

- copies live `$99FF/$9A00/$9A01` into `$9CD0/$9CD1/$9CD2`
- stores the incoming preview slot index to `$9CD3`
- calls `C1:A1D8`

So this is the cap/ribbon/coin-family preview case.

## Local consumer side: `C1:A1D8`

`C1:A1D8` is the shared preview/status renderer that consumes the shadow slot block.

Its structure is now fairly clear:

- it starts from the selected character id passed in `A`
- renders the weapon-side preview first through `$99EA` plus preview slot `$9CD0`
- then renders the three-slot non-weapon side through `$99EB` plus preview slots `$9CD1/$9CD2/$9CD3`
- each preview contribution resolves the referenced inventory item, reads item param byte `+0x1F`, sign-adjusts around `0x80`, and accumulates into a bounded display value

That is exactly the same item-param field and slot-family split we already traced in the live equipment-derived refresh path. The difference is that this family reads the shadow preview slots instead of the live equipped-slot bytes.

## Relationship to the live slot family

The shadow preview block lines up directly with the live equipped-slot block. The neighboring comparison-marker note at [equipment-comparison-markers-9a1d.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/equipment-comparison-markers-9a1d.md) captures the parallel per-character result block written by the menu-side comparator.

The shadow preview block lines up directly with the live equipped-slot block:

- live `$99FF/$9A00/$9A01/$9A02`
- preview `$9CD0/$9CD1/$9CD2/$9CD3`

And the slot-family order is the same one already pinned in [equipment-slot-subtype-dispatch-c19066-c4577d.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/equipment-slot-subtype-dispatch-c19066-c4577d.md):

- weapon
- charm/pendant/cloak
- bracelet/band
- cap/ribbon/coin

So the safest structural interpretation is that `$9CD0..$9CD3` are not generic item ids or text arguments. They are shadow equipped-slot indices for preview purposes.

## Boundaries

Strong locally:

- `$9CD6` is the selected character id feeding the preview helpers
- `$9CD0..$9CD3` are populated in four slot-family-specific ways
- `C1:A1D8` consumes those bytes as preview equipped-slot indices, not raw item ids
- weapon is previewed separately from the grouped three-slot non-weapon side

Still softer:

- the exact user-facing menu text tied to every branch in `C1:A1D8`
- whether the family should be called specifically an equipment-window preview block or a slightly broader status/comparison block

One smaller local piece is strong enough to note even though it is not the main story: `$9CD4` behaves like a preview-ready latch. `C1:A785` clears it before setup, `C1:A996` sets it after the family-specific helper has run, and `C1:A4CE` branches on it before the comparison-display side continues.

So the right current label is structural: equipment preview slot block.

## Confidence

- `$9CD6` as selected character id: high confidence
- `$9CD0..$9CD3` as shadow equipped-slot indices in live slot-family order: high confidence
- `C2:2562/25AC/260D/2673` as the four preview-block setup helpers: high confidence
- `C1:A1D8` as shared equipment preview/status renderer: moderate-to-high confidence
- exact UI label of the preview family: moderate confidence
