# Equipped-Item Derived Cache Family `C2:1857..2351`

This note captures the current local picture of the bank-`C2` helper family that sits behind the equipped-slot updater paths.

See also the consolidation overview at [equipment-preview-and-derived-state-cluster.md](notes/equipment-preview-and-derived-state-cluster.md).

## Working Names

- `C2:1857` = `RecalculateCharacterDerivedOffense`
- `C2:192B` = `RecalculateCharacterDerivedDefense`
- `C2:1AEB` = `RecalculateCharacterDerivedSpeed`
- `C2:1BA4` = `RecalculateCharacterDerivedGuts`
- `C2:1C5D` = `RecalculateCharacterDerivedLuck`
- `C2:1D65` = `RecalculateCharacterDerivedVitality`
- `C2:1D7D` = `RecalculateCharacterDerivedIq`
- `C2:1D95` = `RecalculateCharacterDerivedMissRate`
- `C2:1E03` = `RecalculateCharacterDerivedResistanceFields`
  - internal labels `C2:1F38`, `C2:2028`, `C2:20C7`, and `C2:21B7` refresh `$9A21..$9A24`

Source-scaffold promotion note: `C2:1F38`, `C2:2028`, `C2:20C7`, and `C2:21B7` have no direct `JSL` callers in the current ROM scan. They are internal continuation labels in the `C2:1E03..2351` resistance-field refresh, not independent callable routine starts.

## Main result

The helpers at `C2:1857`, `C2:192B`, `C2:1AEB`, `C2:1BA4`, `C2:1C5D`, `C2:1D65`, `C2:1D7D`, `C2:1D95`, and `C2:1E03` are best read as a shared equipped-item derived-cache family over the character record. Within `C2:1E03`, the internal labels `C2:1F38`, `C2:2028`, `C2:20C7`, and `C2:21B7` mark the later resistance-field phases.

The strongest local pattern is:

- read one or more equipped-slot index bytes at `$99FF..$9A02`
- follow those indices back into the 14-byte inventory region at `$99F1..$99FE`
- resolve the equipped item through `D5:5000`
- pull one-byte item params from offsets `+0x1F`, `+0x21`, or `+0x22`
- combine them with nearby one-byte character fields
- clamp when needed
- store the result into adjacent derived bytes at `$99E3..$99E9` or `$9A1F..$9A24`

So this is no longer just a bag of side effects behind inventory removal. It looks like the shared refresh layer for equipment-derived one-byte state in the character record, with the `$99E3..$99E9` side behaving like a clean display-facing derived stat block, and the later `$9A1F..$9A24` side now reading much more specifically as miss-rate and resistance state refreshed from equipment.

## Family shape

### `C2:1857 -> $99E3`

`C2:1857`:

- reads base byte `$99EA`
- reads equipped-slot index byte `$99FF`
- if that slot is populated, resolves the item in the referenced inventory slot
- reads item param byte `+0x1F`
- applies a small special case when the character id is `4`
- combines that item contribution with the base byte
- clamps to `0..255`
- stores the result to `$99E3`

### `C2:192B -> $99E4`

`C2:192B` is the broader three-slot version.

It:

- starts from base byte `$99EB`
- accumulates item param byte `+0x1F` from equipped slots `$9A00`, `$9A01`, and `$9A02`
- applies the same `character id == 4` adjustment on each contributing item path
- clamps to `0..255`
- stores the final result to `$99E4`

### `C2:1AEB -> $99E5`

`C2:1AEB`:

- starts from base byte `$99EC`
- reads equipped slot `$9A00`
- resolves the equipped item and reads item param byte `+0x21`
- adds that contribution to the base byte
- clamps to `0..255`
- stores the result to `$99E5`

### `C2:1BA4 -> $99E6`

`C2:1BA4`:

- starts from base byte `$99ED`
- reads equipped slot `$99FF`
- resolves item param byte `+0x21`
- adds that contribution to the base byte
- clamps to `0..255`
- stores the result to `$99E6`

This helper is also reused directly from the `0x1E` stat-recovery family after byte additions into `$9A26`.

### `C2:1C5D -> $99E7`

`C2:1C5D`:

- starts from base byte `$99EE`
- accumulates item param byte `+0x21` from equipped slots `$9A01` and `$9A02`
- adds those contributions to the base byte
- clamps to `0..255`
- stores the result to `$99E7`

This helper is also reused directly from the `0x1E` stat-recovery family after byte additions into `$9A29`.

### `C2:1D65 -> $99E8`

`C2:1D65` is simpler.

It:

- reads byte `$99EF`
- adds byte `$9A27`
- stores the result to `$99E8`

### `C2:1D7D -> $99E9`

`C2:1D7D` is the same shape one byte later.

It:

- reads byte `$99F0`
- adds byte `$9A28`
- stores the result to `$99E9`

## Reference-backed crosswalk

The local structural map is now strong enough to support a cautious crosswalk against the named bank-`02` postmath family in `ebsrc`.

The strongest reference-backed and locally consistent assignments are:

- `C2:1AEB -> $99E5` = strongest fit for postmath `SPEED`
- `C2:1BA4 -> $99E6` = strongest fit for postmath `GUTS`
- `C2:1C5D -> $99E7` = strongest fit for postmath `LUCK`
- `C2:1D65 -> $99E8` = strongest fit for postmath `VITALITY`
- `C2:1D7D -> $99E9` = strongest fit for postmath `IQ`

That crosswalk is not just coming from include-order inheritance. The local `0x1E` stat-boost leaves at `C1:7523..76A7` update `$9A28/$9A26/$9A25/$9A27/$9A29` respectively, then immediately call `C2:1D7D/1BA4/1AEB/1D65/1C5D`, and the community control-code docs name those leaves as `BOOST_IQ/GUTS/SPEED/VITALITY/LUCK`.

The earlier two helpers remain a step softer but still look good as a pair:

- `C2:1857 -> $99E3` = strongest candidate for postmath `OFFENSE`
- `C2:192B -> $99E4` = strongest candidate for postmath `DEFENSE`

Those last two are still a step softer than the `VITALITY/IQ` pair, but the local support is better than before. In the bank-`01` equipment/status menu family:

- `C1:A1F0..A2FF` uses base byte `$99EA` together with equipped-slot index `$99FF` and item param `+0x1F` to build and display a preview value
- `C1:A4D0..A63F` uses base byte `$99EB` together with the defensive equipment side and the same item param field to build the sibling preview value
- the nearby menu family at `C1:9BA0..9D49` iterates the same four slot families directly and writes per-slot comparison markers into `$9A1D` after comparing signed item-param-`+0x1F` contributions
- the shared preview renderer at `C1:A1D8` uses the shadow slot block `$9CD0..$9CD3` to mirror the same split: one weapon-side preview rooted in `$99EA`, then a grouped three-slot non-weapon preview rooted in `$99EB` as documented in [equipment-preview-slot-block-9cd0-9cd6.md](notes/equipment-preview-slot-block-9cd0-9cd6.md)

So the safest current read is no longer just "reference order says offense/defense." It is: `$99EA/$99E3` behave like the offense base/derived pair, and `$99EB/$99E4` behave like the defense base/derived pair, with the exact human-facing label still kept a little cautious.

A stronger local bridge has now emerged for the late pair. In the bank-`01` growth/status family around `C1:D622..D77E`:

- `$99E8` feeds an HP-growth-style formula before the result is added into both `$99D8` and `$9A15`
- `$99E9` feeds a PP-growth-style formula before the result is added into both `$99DA` and `$9A1B`

That makes the `VITALITY` / `IQ` assignments for `$99E8/$99E9` materially stronger than the broader display-order inference alone.

### `C2:1D95 -> $9A1F`

`C2:1D95`:

- reads equipped slot `$99FF`
- resolves item param byte `+0x22`
- sign-adjusts that byte around `0x80`
- stores the final one-byte result into `$9A1F` for the selected character

Given the now-stable character-record base, `$9A1F` sits at offset `+0x51`, which matches `char_struct::miss_rate` in `ebsrc`.

So the safest current read is that `C2:1D95` refreshes the selected character's equipment-derived miss-rate byte.

### `C2:1E03 -> $9A20`

`C2:1E03` is the first of a packed resistance quartet.

It:

- reads equipped slots `$9A00` and `$9A02`
- resolves item param byte `+0x22` for each equipped item
- masks each contribution with `0x03`
- sums the two masked contributions
- caps the result at `3`
- stores the final one-byte value into `$9A20`

Given the character-record base, `$9A20` sits at offset `+0x52`, which matches `char_struct::fire_resist` in `ebsrc`.

### `C2:1F38 -> $9A21` internal label

`C2:1F38` is the same two-slot pattern one bit-pair later.

It:

- reads equipped slots `$9A00` and `$9A02`
- resolves item param byte `+0x22` for each equipped item
- masks each contribution with `0x0C`
- shifts those masked values down through `C0:925B`
- sums the two contributions
- caps the result at `3`
- stores the final one-byte value into `$9A21`

That places `$9A21` at offset `+0x53`, matching `char_struct::freeze_resist`.

### `C2:2028 -> $9A22` internal label

`C2:2028` repeats the same shape again:

- read the same equipped slots `$9A00` and `$9A02`
- resolve item param byte `+0x22`
- mask each contribution with `0x30`
- shift through `C0:925B`
- sum, cap at `3`, and store to `$9A22`

That places `$9A22` at offset `+0x54`, matching `char_struct::flash_resist`.

### `C2:20C7 -> $9A23` internal label

`C2:20C7` is the fourth packed two-bit member:

- read the same equipped slots `$9A00` and `$9A02`
- resolve item param byte `+0x22`
- mask each contribution with `0xC0`
- shift through `C0:925B`
- sum, cap at `3`, and store to `$9A23`

That places `$9A23` at offset `+0x55`, matching `char_struct::paralysis_resist`.

### `C2:21B7 -> $9A24` internal label

`C2:21B7` returns to the single-slot full-byte pattern.

It:

- reads equipped slot `$9A01`
- resolves item param byte `+0x22`
- sign-adjusts that byte around `0x80`
- stores the final one-byte result into `$9A24`

That places `$9A24` at offset `+0x56`, matching `char_struct::hypnosis_brainshock_resist`.

So the current strongest local model for item param byte `+0x22` is:

- one full-byte contribution path for `$9A1F` from equipped slot `$99FF`
- four packed 2-bit resistance fields contributed by equipped slots `$9A00` and `$9A02`
- one final full-byte contribution path for `$9A24` from equipped slot `$9A01`

The slot-side updater family now sharpens that split further:

- `$99FF` = weapon-family slot, feeding offense/guts/miss-rate
- `$9A00` = charm/pendant/cloak-family slot, feeding defense, speed, and the packed `$9A20..$9A23` resistance quartet
- `$9A01` = bracelet/band-family slot, feeding defense, luck, and the final full-byte `$9A24` resistance path
- `$9A02` = cap/ribbon/coin-family slot, feeding defense, luck, and the packed `$9A20..$9A23` resistance quartet

That does not yet give us final menu-label certainty for the three non-weapon slots, but it is a much better local role split than treating them as anonymous equipment bytes.

## Reuse and subsystem boundary

This family is clearly shared beyond one inventory code path.

Direct reuse already shows up in at least three places:

- the equipped-slot subtype installer family in [equipment-slot-subtype-dispatch-c19066-c4577d.md](notes/equipment-slot-subtype-dispatch-c19066-c4577d.md)
- larger bank-`01` equipment/menu families around `C1:D1xx..D9xx`
- the `0x1E` stat-recovery leaf block, which updates bytes in `$9A25..$9A29` and then immediately calls some of these same `C2` helpers

One especially useful local anchor is `C1:D8D0`, which seeds the nearby base/input fields before immediately running the whole `C2:1857..1D7D` refresh chain. That strengthens the reading that `$99EA..$99F0`, `$99D8/$9A15`, and `$99DA/$9A1B` are part of the same stable character-record stat family rather than unrelated scratch state.

That is strong local evidence that these outputs are not temporary scratch values. But the two halves do not look equally "cache-like" anymore:

- `$99E3..$99E9` have the cleaner display-facing profile. The bank-`01` path at `C1:9660` reads them sequentially through `C1:0DF6` / `C4:3D75`, which is exactly what we would expect from a stable derived-stat display block.
- `$9A1F..$9A24` now look much less anonymous than before. Their offsets line up exactly with `char_struct::miss_rate`, `fire_resist`, `freeze_resist`, `flash_resist`, `paralysis_resist`, and `hypnosis_brainshock_resist`, and the producer logic matches that layout unusually well. They should still be treated as active runtime state refreshed from equipment, but they are no longer best described as a vague busier side-block.

## Safest current interpretation

A useful local base-address cross-check now makes the late-byte identification much safer. Since the 14-byte inventory block at `$99F1..$99FE` is already pinned as `char_struct::items`, the character-record base for this family is `$99CE`. That means:

- `$99E3..$99E9` = offsets `+0x15..+0x1B`, the main displayed stat region
- `$99EA..$99F0` = offsets `+0x1C..+0x22`, the corresponding base/input stat region
- `$99F1..$99FE` = offsets `+0x23..+0x30`, the 14-byte inventory region
- `$99FF..$9A02` = offsets `+0x31..+0x34`, the four equipped-slot bytes
- `$9A1F..$9A24` = offsets `+0x51..+0x56`, the miss-rate and resistance region

That offset map is what lets the late family read cleanly as miss/resistance refresh rather than generic busier derived state.

The strongest safe statement is:

- `$99EA..$99F0` and `$9A25..$9A29` are one-byte base/input fields in the character record
- `$99FF..$9A02` are equipped-slot indices into the inventory region
- `D5:5000 +0x1F/+0x21/+0x22` are one-byte equipment contribution fields
- `C2:1857..2213` recompute adjacent derived one-byte outputs at `$99E3..$99E9` and `$9A1F..$9A24`

The safer split is:

- `$99E3..$99E9` are strong candidates for display-facing derived bytes refreshed from equipment and nearby one-byte stat state
- `$9A1F..$9A24` are the adjacent miss-rate and resistance state bytes refreshed from the same equipment family, with the packed quartet coming from `$9A00/$9A02` and the final single-byte path coming from `$9A01`

One local display-side detail is now strong enough to promote: the bank-`01` path at `C1:9660` prints `$99E3,$99E4,$99E5,$99E6,$99E8,$99E9,$99E7` in that exact order. Combined with the postmath crosswalk above, the safest current player-facing alignment is:

- `$99E3` = strongest candidate for displayed offense
- `$99E4` = strongest candidate for displayed defense
- `$99E5` = displayed speed
- `$99E6` = displayed guts
- `$99E8` = displayed vitality
- `$99E9` = displayed IQ
- `$99E7` = displayed luck

That ordering is still best treated as reference-backed and locally consistent rather than fully proved from a named label table. But it is now a much stronger read than a generic "seven derived bytes" sketch.

The exact player-facing names of every byte are still one step softer than the structural map. But the refresh-family interpretation itself is now strong.

## Confidence

- family-level interpretation as equipped-item derived-state refresh helpers: high confidence
- output-byte mapping `$99E3..$99E9`, `$9A1F..$9A24`: high confidence
- reuse from both equipment and `0x1E` stat-update families: high confidence
- `$99E3..$99E9` as the cleaner display-facing derived block: high confidence
- `$9A1F..$9A24` as equipment-refreshed miss-rate and resistance state: moderate-to-high confidence
- `C2:1AEB/1BA4/1C5D/1D65/1D7D` as postmath `SPEED/GUTS/LUCK/VITALITY/IQ`: high confidence for `VITALITY/IQ`, moderate-to-high for the others
- `C2:1857/192B` as postmath `OFFENSE/DEFENSE`: moderate-to-high confidence
- display-order alignment `$99E3,$99E4,$99E5,$99E6,$99E8,$99E9,$99E7` from `C1:9660`: high confidence
- player-facing stat-name alignment for `$99E3..$99E9`: moderate-to-high confidence
- exact human-facing names of each derived byte beyond that display-facing block: moderate confidence
