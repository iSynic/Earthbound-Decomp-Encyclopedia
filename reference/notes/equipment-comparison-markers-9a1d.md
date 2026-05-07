# Equipment Comparison Markers `$9A1D`

This note captures the current local picture of the four-byte marker block at `$9A1D` used by the bank-`01` equipment comparison family around `C1:9B4E..9D49`.

See also the consolidation overview at [equipment-preview-and-derived-state-cluster.md](notes/equipment-preview-and-derived-state-cluster.md).

## Main result

The safest current read is:

- `$9A1D..$9A20` are per-character equipment comparison markers written in active-party order
- `C1:9B4E` builds those markers for one candidate item id
- `C1:9CDD` is the simple initializer that seeds all four bytes to the default marker value `0x0400`
- the comparison family uses the same four slot subtypes already pinned elsewhere, choosing one live equipped-slot family from item byte `+0x19 & 0x0C`

## Working Names

- `C1:9B4E` = `BuildEquipmentComparisonMarkersForItem`
- `C1:9B79` = `ResolveEquippedSlotForItemSubtype`
- `C1:9CDD` = `InitializeEquipmentComparisonMarkersDefault`

Source-scaffold promotion:

- `C1:9B79..9CDD` is decoded source in `src/c1/c1_9b79_resolve_equipped_slot_for_item_subtype.asm`.
- `C1:9CDD..9D49` is decoded source in `src/c1/c1_9cdd_initialize_equipment_comparison_markers_default.asm`.
- The combined C1 scaffold validates byte-for-byte after promotion: `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

So `$9A1D` is no longer just an unexplained UI scratch byte. It is a compact compatibility/comparison result block consumed by the equipment menu family.

## Local writer side

### `C1:9CDD`

`C1:9CDD` is the simple setup helper, now source-backed in `src/c1/c1_9cdd_initialize_equipment_comparison_markers_default.asm`.

It:

- iterates the four active-party entries
- writes `0x0400` to each character's `$9A1D` byte
- then enters the larger rendering path

That makes `0x0400` the default marker state for this family.

### `C1:9B4E`

`C1:9B4E` is the real classifier.

The subtype/comparison continuation at `C1:9B79..9CDD` is now source-backed in `src/c1/c1_9b79_resolve_equipped_slot_for_item_subtype.asm`. It keeps the `C1:9B4E` front entry small while exposing the loop body that selects the live equipped-slot byte, compares signed item-param `+0x1F`, writes `$9A1D`, and jumps back to `C1:9B62` for the next active-party row.

Input shape:

- `A` = candidate item id
- loop over the four active-party characters via `Y = 0..3`

For each character it does three layers of testing:

1. `C3:EE14` equipability check
- if false, marker becomes `0x0C00`

2. `C1:9EE6` broad item class check
- if class is not `2`, marker becomes `0x0400`

3. subtype-specific comparison
- choose the relevant live equipped-slot family from candidate item byte `+0x19 & 0x0C`
- resolve the currently equipped item in that family, if any
- read signed item param `+0x1F` from current item and candidate item
- compare the two contributions
- choose either `0x0400` or `0x1400`

The family then stores the chosen marker into `$9A1D + character_stride_index`.

## Current best interpretation of the marker values

The strongest safe statements are:

- `0x0C00` = hard "cannot equip" state
  - this is directly tied to the failed `C3:EE14` compatibility predicate
- `0x0400` = default/allowed state
  - this is the initializer value from `C1:9CDD`
  - it is also the fallback state for non-class-`2` items and one side of the signed comparison branch
- `0x1400` = alternate comparison state
  - this is the other side of the signed comparison branch after candidate/current item-param `+0x1F` values are compared

The exact user-facing icon or palette tied to `0x0400` versus `0x1400` is still not fully proved from ROM-local code alone, but the arithmetic side is now clearer than before. The signed comparison branch in `C1:9B4E` chooses:

- `0x1400` when the candidate item's signed `+0x1F` contribution is strictly greater than the currently equipped item's contribution in that slot family
- `0x0400` otherwise

Because the code forces a strict compare, `0x0400` is the default/non-improving side, not a separate hard "worse only" state. That means the safest current wording is:

- `0x1400` = better-than-current comparison outcome
- `0x0400` = default or non-improving comparison outcome

The newer renderer-side cross-check makes the presentation layer stronger too. `C4:3D75 -> C4:3D24` clearly treats `0x0400`, `0x0C00`, and `0x1400` as three distinct rendered states chosen by separate high-bit table selections, and the community equipment-help text describes the same shop preview states as:

- flash when the item is equippable and stronger than the current item
- normal when the item is equippable but equal or worse
- black when the item cannot be equipped

Taken together, the best current presentation mapping is:

- `0x1400` = flashing equipment-window state
- `0x0400` = normal equipment-window state
- `0x0C00` = blacked-out equipment-window state

I am still keeping that last step as reference-backed and locally consistent rather than fully local ROM proof, because the renderer path is easier to pin as "distinct rendered states" than as exact human-facing color/effect names.

## Display-side anchor

The bank-`04` renderer around `C4:3D75 -> C4:3D24` now gives one useful local cross-check. The marker word is split into:

- low 3 bits -> temporary byte `$5E72`, later latched to `$5E73`
- high bits -> table selector passed into `C4:3D24` after shifting right three times

For the comparison markers we currently care about (`0x0400`, `0x0C00`, `0x1400`), the low 3 bits are all zero. So the visible distinction between those states is being carried by the high-bit table selector, not by a tiny low-bit variant. That is good local support for treating them as genuinely different rendered comparison states rather than as one state plus incidental flags.

What is still not fully pinned is the exact asset-table identity behind those three table selections. The current ROM evidence says "distinct rendered states" more strongly than it says "this exact glyph/tile row," but with the community equipment-help text in hand the best safe presentation read is now flash / normal / black rather than three anonymous marker states.

## Asset-table layer

The newest local result is that the renderer path is broader than a tiny three-icon picker.

`C4:3D75 -> C4:3D24` first normalizes the marker word into a menu render-state row and writes through the row table rooted at `C4:343E`. That row logic writes:

- the normalized state word into `$98C9 + X`
- a per-party output byte into `$98CB + X`

Those `$98CB` bytes are then consumed later by `C4:F39B..F41A`, which rejects `0` and out-of-range values, masks them to `0x1F`, maps them through `C0:79EC`, and finally instantiates the result through `C0:1E49` plus the standard visual-selector path.

The newly pinned entry behavior for `C4:343E` is:

- input `A` is a 1-based row/state slot; the routine stores `A - 1` as the `$98C9/$98CB` slot index
- it multiplies the 32-bit value at `$00A7/$00A9` by `#$0E10` through `C0:90FF`, clamps the low word at `#$EA5F`, and stores that normalized word at `$98C9 + slot*8`
- it then walks up to six party-related bytes from the `$97F5/$988B/$9891` region, maps live character ids to `$99CE + id*#$005F`, caches the active record pointer in `$4DC6`, and stores a compact status/visual byte at `$98CB + slot*8 + party_index`
- the byte combines the base `$988B+party_index` value with bits derived from party record bytes `+$0E` and `+$0F`

That makes the safest working name `BuildPartyEquipmentComparisonVisualStateRows`: it builds the `$98C9/$98CB` visual-state rows that the later equipment comparison renderer consumes, while the exact human-facing meaning of each bit remains a downstream asset-table question.

So the safest current read is:

- the comparison markers do not select a single standalone glyph in isolation
- they select one of several normalized equipment-window visual states
- those visual states are implemented through the same broader menu/visual descriptor machinery used elsewhere

That is why the strongest current wording is still "flashing / normal / black equipment-window state" instead of a narrower claim like "up-arrow tile / blank tile / X tile." The local ROM path now supports the broader window-state interpretation much better than the tiny-icon interpretation.

## Relationship to the preview slot family

This marker block sits right next to the newer shadow preview-slot block at [equipment-preview-slot-block-9cd0-9cd6.md](notes/equipment-preview-slot-block-9cd0-9cd6.md).

The two families complement each other:

- `$9CD0..$9CD3` = shadow equipped-slot indices used by the preview renderer
- `$9A1D..$9A20` = per-character comparison markers used by the equipment-comparison menu family

Both use the same four slot families pinned in [equipment-slot-subtype-dispatch-c19066-c4577d.md](notes/equipment-slot-subtype-dispatch-c19066-c4577d.md).

## Boundaries

Strong locally:

- `C1:9B4E` writes `$9A1D` in active-party order
- `C1:9B79` is the source-backed subtype resolver/comparison continuation inside that writer
- `0x0C00` is the failed-equipability marker
- `0x0400` is the default marker and one comparison outcome
- `0x1400` is the alternate comparison outcome inside the equipable case
- the family compares signed item-param `+0x1F` contributions in the slot family selected by item byte `+0x19 & 0x0C`

Still softer:

- the exact normalized row ids and per-party output-byte meanings written through `C4:3492` / `$98C9` / `$98CB`
- whether the broad-class-`2` test should be read specifically as the equipment-item class or more cautiously as the only class that enables comparison

So the right current label is structural: equipment comparison markers.

## Confidence

- `$9A1D..$9A20` as per-character comparison markers: high confidence
- `C1:9CDD` as default-marker initializer with `0x0400`: high confidence
- `C1:9B4E` as the candidate-item comparison writer: high confidence
- `0x0C00` = cannot equip: high confidence
- `0x1400` as the strict better-than-current comparison outcome: high confidence
- `0x0400` as the default/non-improving comparison outcome: high confidence
- flash / normal / black presentation mapping for `0x1400 / 0x0400 / 0x0C00`: moderate confidence
- broader window-state interpretation over tiny-icon interpretation: moderate-to-high confidence

## Working Names

- `C4:343E` = `BuildPartyEquipmentComparisonVisualStateRows`
