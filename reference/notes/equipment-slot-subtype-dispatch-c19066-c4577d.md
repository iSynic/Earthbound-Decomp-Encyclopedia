# Equipment Slot Subtype Dispatch `C1:9066 -> C4:577D/57CA/5815/5860`

This note captures the current local picture of the shared equipment-slot subtype dispatch rooted at `C1:9066`.

See also the consolidation overview at [equipment-preview-and-derived-state-cluster.md](notes/equipment-preview-and-derived-state-cluster.md).

## Main result

`C1:9066` is best read as a shared selected-inventory-item subtype dispatcher for the four equipped-slot index bytes in the character record.

The safest current local sketch is:

- input `A` = 1-based character id
- input `X` = 1-based inventory slot index inside that character's 14-byte inventory
- resolve the item currently stored in that slot
- read item byte `+0x19 & 0x0C`
- dispatch to one of four slot-specific bank-`C4` helpers
- return the previous value of the selected equipped-slot byte

## Working Names

- `C1:9066` = `DispatchEquippedSlotSubtypeUpdate`

Source-scaffold promotion:

- `C1:9066..90E6` is now decoded source in `src/c1/c1_9066_dispatch_equipped_slot_subtype_update.asm`.
- The combined C1 scaffold validates byte-for-byte after promotion: `C1 byte-equivalence: OK, 172 module(s), 0 mismatch(es).`

Source polish follow-up (2026-05-06): `C1:9066` now calls the four C4 slot
installers by their derived-state refresh contract names instead of raw
addresses. The same names are now also used by the `C1:8C27` inventory removal
slot-index maintenance path.

## Dispatch Role

So this is no longer just a loose side effect family reached from inventory removal. It looks like the shared subtype-to-equipped-slot bridge behind several menu/text/equipment flows, and the subtype groups are now strong enough to describe in item-family terms instead of only as slot `0/1/2/3`.

## Local behavior of `C1:9066`

The body at `C1:9066`:

1. maps `(character id - 1)` through `C0:8FF7` with stride `0x5F`
2. lands on the selected inventory byte at `99F1 + (slot - 1)`
3. resolves that byte as an item id
4. maps the item through `D5:5000 + 0x19`
5. masks with `0x0C`
6. dispatches:
   - `0x00 -> C4:577D`
   - `0x04 -> C4:57CA`
   - `0x08 -> C4:5815`
   - `0x0C -> C4:5860`
   - anything else -> `0`

The four source names are
`C4577D_InstallWeaponSlotIndexAndRefreshDerivedStats`,
`C457CA_InstallBodySlotIndexAndRefreshDerivedStats`,
`C45815_InstallArmsSlotIndexAndRefreshDerivedStats`, and
`C45860_InstallOtherSlotIndexAndRefreshDerivedStats`.

That lines up exactly with the packed-slot reading from [item-byte-19-packed-class-and-slot.md](notes/item-byte-19-packed-class-and-slot.md): bits `2-3` of item byte `+0x19` are the four-way equipped-slot subtype selector.

The item-record cross-check is now strong enough to sketch the four subtype families locally:

- `0x00` = weapon family (`bat`, `gun`, `fry pan`, `sword`, `yoyo`, `slingshot`)
- `0x04` = charm/pendant/cloak family
- `0x08` = bracelet/band family
- `0x0C` = cap/ribbon/coin family

Those names are still intentionally structural rather than fully promoted menu labels, but they are much stronger than anonymous slot numbers.

## The four slot-specific leaves

Each bank-`C4` leaf has the same high-level shape.

### `C4:577D`

This leaf targets character-record byte `$99FF`, the weapon-family equipped-slot index.

It:

- reads the current byte at `$99FF`
- writes the incoming inventory slot index into that byte
- calls three bank-`C2` helpers:
  - `C2:1857`
  - `C2:1BA4`
  - `C2:1D95`
- returns the previous `$99FF` value

### `C4:57CA`

This leaf targets `$9A00`, the charm/pendant/cloak-family equipped-slot index.

It:

- reads the current byte at `$9A00`
- writes the incoming inventory slot index into that byte
- calls:
  - `C2:192B`
  - `C2:1AEB`
  - `C2:1E03`
- returns the previous `$9A00` value

The last call should now be read as the entry into the wider resistance refresh chain documented in [equipped-item-derived-cache-family-c21857-c21e03.md](notes/equipped-item-derived-cache-family-c21857-c21e03.md), not as a single-byte `$9A20` refresh only. In the current local split, this slot is the one that uniquely feeds `C2:1AEB` and also contributes to the packed `$9A20..$9A23` resistance quartet.

### `C4:5815`

This leaf targets `$9A01`, the bracelet/band-family equipped-slot index.

It:

- reads the current byte at `$9A01`
- writes the incoming inventory slot index into that byte
- calls:
  - `C2:192B`
  - `C2:1C5D`
  - `C2:1E03`
- returns the previous `$9A01` value

This slot shares the broader defense-side refresh with the other non-weapon slots, but it is also the one that uniquely feeds `C2:21B7`, the final full-byte resistance-style refresh at `$9A24`.

### `C4:5860`

This leaf targets `$9A02`, the cap/ribbon/coin-family equipped-slot index.

It:

- reads the current byte at `$9A02`
- writes the incoming inventory slot index into that byte
- calls:
  - `C2:192B`
  - `C2:1C5D`
  - `C2:1E03`
- returns the previous `$9A02` value

This slot shares the broader defense/luck side and contributes to the packed `$9A20..$9A23` resistance quartet, but it does not feed the final single-byte `$9A24` refresh.

## Best current interpretation

The strongest current read is:

- `$99FF..$9A02` are the four equipped-slot index bytes inside the character record
- `C1:9066` chooses which one to touch based on item byte `+0x19 & 0x0C`
- those four slots now read best as weapon, charm/pendant/cloak, bracelet/band, and cap/ribbon/coin families
- the downstream refresh calls also separate their roles: weapon uniquely feeds offense/guts/miss-rate; the charm/pendant/cloak slot uniquely feeds speed plus the packed resistance quartet; the bracelet/band and cap/ribbon/coin slots share the defense/luck side, with the bracelet/band slot also uniquely feeding the final hypnosis/brainshock-style resistance byte
- the bank-`C4` leaves install the new inventory-slot index and run downstream bank-`C2` refresh logic

That makes this family look like shared equipment-slot installation/update machinery rather than a removal-only cleanup path. The downstream cache side now has its own structural note at [equipped-item-derived-cache-family-c21857-c21e03.md](notes/equipped-item-derived-cache-family-c21857-c21e03.md).

The direct caller set reinforces that. `C1:9066` is reached both from inventory/text-family code and from larger menu/status-family code, which is exactly what we would expect if it is the central subtype bridge for equipped-slot index maintenance.

One extra local anchor now comes from the bank-`01` menu family around `C1:9BA0..9D49`. That code iterates the four subtype families in the same `0x00/0x04/0x08/0x0C` order, resolves the currently equipped item in each slot, compares its signed item-param-`+0x1F` contribution against the comparison item, and writes a per-slot marker into `$9A1D`. The new focused note at [equipment-comparison-markers-9a1d.md](notes/equipment-comparison-markers-9a1d.md) captures that block in more detail. The exact UI semantics of the marker values are still a little soft, but the structural point is strong: the menu layer is using the same four subtype families directly, not some alternate slot model.

The later bank-`01` preview readers reinforce the same split another way. Around `C1:A1F0..A772`, weapon is handled first as a one-slot `+0x1F` preview path rooted in `$99EA/$99FF`, while `$9A00/$9A01/$9A02` are then walked as a three-slot family rooted in `$99EB`, each contributing signed item-param-`+0x1F` values into one broader non-weapon preview total. The new shadow-slot note at [equipment-preview-slot-block-9cd0-9cd6.md](notes/equipment-preview-slot-block-9cd0-9cd6.md) shows that the menu layer mirrors the live slot families directly through `$9CD0..$9CD3` before calling the shared preview renderer. That is good local support for the current structural wording: weapon is a distinct slot family, while the other three are variations inside a shared defense-side equipment group even if their exact menu labels remain slightly soft.

## Boundaries

Two things are strong here, and two things are still a little softer.

Strong locally:

- `C1:9066` dispatches by item byte `+0x19 & 0x0C`
- each `C4:57xx` leaf targets one of `$99FF..$9A02`
- each leaf returns the previous byte value after installing the new one
- the family is shared beyond just `C1:8C27` inventory removal

Still somewhat softer:

- the exact player-facing menu labels of the second-through-fourth slots
- the exact semantic names of every downstream bank-`C2` refresh helper

So the right current label is still structural: equipment-slot subtype dispatch and equipped-slot index updater. But the item-family names above are now locally strong enough to use as descriptive shorthand.

## Confidence

- `C1:9066` as subtype dispatcher over item byte `+0x19 & 0x0C`: high confidence
- `$99FF..$9A02` as four equipped-slot index bytes: high confidence
- `C4:577D/57CA/5815/5860` as slot-specific installers returning the previous value: high confidence
- weapon slot identity for `$99FF`: high confidence
- charm/pendant/cloak, bracelet/band, and cap/ribbon/coin readings for `$9A00..$9A02`: moderate-to-high confidence
- exact human-facing menu labels of those three non-weapon slots and each downstream `C2` helper: moderate confidence
