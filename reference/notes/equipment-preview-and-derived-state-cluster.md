# Equipment Preview And Derived-State Cluster

This note is a consolidation pass over the now-stable equipment slot / preview / comparison / derived-stat family.

It does not replace the focused notes. It gives a single top-level map of how they fit together.

Focused notes:

- [item-byte-19-packed-class-and-slot.md](notes/item-byte-19-packed-class-and-slot.md)
- [equipment-slot-subtype-dispatch-c19066-c4577d.md](notes/equipment-slot-subtype-dispatch-c19066-c4577d.md)
- [equipped-item-derived-cache-family-c21857-c21e03.md](notes/equipped-item-derived-cache-family-c21857-c21e03.md)
- [equipment-preview-slot-block-9cd0-9cd6.md](notes/equipment-preview-slot-block-9cd0-9cd6.md)
- [equipment-comparison-markers-9a1d.md](notes/equipment-comparison-markers-9a1d.md)

## At a glance

The safest current end-to-end model is:

1. item byte `+0x19`
- broad class in bits `4-5`
- equipped-slot subtype in bits `2-3`

2. live equipped-slot family
- `$99FF/$9A00/$9A01/$9A02`
- maintained by `C1:9066 -> C4:577D/57CA/5815/5860`
- current best structural slot families:
  - weapon
  - charm/pendant/cloak
  - bracelet/band
  - cap/ribbon/coin

3. equipment-derived refresh family
- `C2:1857..2213`
- recomputes:
  - `$99E3..$99E9` = display-facing derived stats
  - `$9A1F..$9A24` = miss-rate and resistance state

4. shadow preview-slot family
- `$9CD0..$9CD3` plus selected-character byte `$9CD6`
- populated by `C2:2562/25AC/260D/2673`
- consumed by shared preview renderer `C1:A1D8`

5. per-character comparison marker family
- `$9A1D..$9A20`
- initialized by `C1:9CDD`
- written by `C1:9B4E` for a candidate item
- current best marker reads:
  - `0x0C00` = cannot equip / blacked-out equipment-window state
  - `0x1400` = better-than-current / flashing equipment-window state
  - `0x0400` = default or non-improving / normal equipment-window state

## Shared slot-family order

A major consolidation result from this pass is that the same four-family order is now visible at every important layer:

- item subtype bits in `+0x19`
- live equipped-slot bytes `$99FF/$9A00/$9A01/$9A02`
- shadow preview-slot bytes `$9CD0/$9CD1/$9CD2/$9CD3`
- comparison loop in `C1:9B4E..9D49`

That means the equipment-preview side is no longer relying on a guessed correspondence. The menu layer really is mirroring the same slot-family model as the live install/update side.

## Live state versus preview state

The cleanest split is:

### Live state

- `$99FF/$9A00/$9A01/$9A02` = live equipped-slot indices
- updated when inventory items are installed/removed/swapped
- feed the bank-`C2` derived refresh family directly

### Preview state

- `$9CD0/$9CD1/$9CD2/$9CD3` = shadow equipped-slot indices for one candidate preview
- `$9CD6` = selected character id for that preview
- `$9CD4` = small preview-ready latch
- the preview renderer `C1:A1D8` reads these shadow slots instead of the live slots

### Comparison state

- `$9A1D..$9A20` = per-character result markers for a candidate item
- written in active-party order by `C1:9B4E`
- consumed by the equipment-comparison menu family

So the current best mental model is not ?one menu scratch area.? It is three coordinated layers:

- live equipped slots
- shadow preview slots
- per-character comparison markers

## Derived outputs

The derived outputs now split cleanly into two neighboring blocks.

### Display-facing derived stats

`$99E3..$99E9` are the strongest current candidates for the displayed derived stat block.

Safest current player-facing alignment:

- `$99E3` offense
- `$99E4` defense
- `$99E5` speed
- `$99E6` guts
- `$99E7` luck
- `$99E8` vitality
- `$99E9` IQ

This is strongly locally supported, though still phrased a little more cautiously than a fully named struct field table.

### Miss-rate and resistance block

`$9A1F..$9A24` now have a much cleaner local read than they used to:

- `$9A1F` = miss-rate
- `$9A20..$9A23` = packed quartet refreshed from slots `$9A00/$9A02`
- `$9A24` = final single-byte resistance refreshed from slot `$9A01`

The exact resistance names are now good local fits rather than loose inheritance from references.

## What is strong now

Strong locally:

- item byte `+0x19` broad-class and slot-subtype split
- live equipped-slot updater family
- live slot-family identities at a structural level
- shadow preview-slot block and its setup helpers
- per-character comparison marker block
- marker meanings `cannot equip / better / non-improving`
- derived stat block versus miss/resistance block

## What is still slightly softer

Still a little softer:

- the exact human-facing menu labels for the three non-weapon slot families
- the exact normalized row ids and per-party output-byte meanings behind the flash / normal / black marker states (`0x0400/0x0C00/0x1400`)
- a few downstream bank-`C2` helper names where the role is clearer than the final label

So the subsystem is now mostly structurally solved, with only a small amount of presentation-layer naming still softer than the control-flow map.

## Best next targets

If this cluster is revisited later, the best follow-ups are:

1. identify the exact rendered asset/palette names for the three comparison marker states
2. tighten the menu-facing labels for the three non-weapon slot families
3. keep cross-checking the displayed-stat block against more bank-`01` readers so the remaining reference-backed labels become fully local
