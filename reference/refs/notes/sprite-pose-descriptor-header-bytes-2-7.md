# Sprite Pose Descriptor Header Bytes (`+2..+7`)

This note captures the current best local read for the still-unresolved pose descriptor header bytes after the already-identified fields `+0`, `+1`, and `+8`.

See also [sprite-pose-descriptor-cache-2a06-2cd6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/sprite-pose-descriptor-cache-2a06-2cd6.md).
See also [overlay-init-descriptor-fields.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/overlay-init-descriptor-fields.md).

## Main result

The local write and consumer paths now give a useful partial split for pose descriptor bytes `+2..+7`.

The strongest current local read is:

- byte `+2` = a small geometry/footprint category index cached in `2B6E`
- `2B6E` is mapped through lookup tables at `C42A1F`, `C42A41`, and `C42AEB`
- the `C42AEB` result is cached in `332A` and gates later checks
- byte `+3` = a shared base attribute byte passed into `C01D38`
- bytes `+4..+7` = two alternate parameter pairs copied into `3366/33A2` and `33DE/1A4A`

That is much better than treating the whole `+2..+7` range as one unresolved lump.

## Byte `+2` is a geometry-like category index

After the writer stores the already-known pose fields, it:

- points at descriptor offset `+2`
- reads one byte
- stores that byte to `2B6E`
- doubles it and indexes `DATA_C42AEB`
- stores the resulting word to `332A`

Later consumers do more with the same category:

- `2B6E` indexes `DATA_C42A1F`
- `2B6E` indexes `DATA_C42A41`
- `2B6E` indexes `DATA_C42AEB`

Those tables all contain small word values like `0008`, `000C`, `0010`, `0018`, `0020`, `0028`, `0038`, `0048`, and `0041`, which makes them look much more like geometry/extent tables than text or state enums.

So the safest current statement is:

- byte `+2` selects a geometry or footprint class for the pose

## Why `332A` now looks like a derived geometry gate

The writer stores `DATA_C42AEB[byte+2]` into `332A`.

Later code in the `C06014+` family immediately does:

- `LDA $332A,X`
- if zero, skip the whole later check path

That makes `332A` look like a derived geometry/range parameter whose zero value disables the relevant check outright.

So the safest current statement is:

- `332A` is a derived geometry/range word computed from pose descriptor byte `+2`

## Sample byte `+2` values from representative pose records

Using the legacy labels as a guide, representative headers look like this:

- `NessWalking` = `03 20 05 1A 08 08 08 08`
- `SweatDrops` = `02 20 01 1E 00 00 00 00`
- `Mushroom` = `02 20 01 1A 00 00 00 00`
- `SmallWaterRipples` = `02 20 00 1A 00 00 00 00`
- `BigWaterRipples` = `02 40 03 1A 00 00 00 00`
- `Shadow` = `02 20 00 1A 00 00 00 00`
- `SmokeCloud` = `04 40 08 14 00 00 00 00`
- `ATM` = `04 40 08 1E 0C 08 0C 08`

So the current category split looks plausibly like:

- `0` for shadow/small-ripple-style simple cases
- `1` for mushroom/sweat-drop style cases
- `3` for big-ripple style cases
- `5` for party walking poses
- `8` for smoke/ATM style larger object cases

That is still descriptive rather than final, but it is useful progress.

## Bytes `+4..+7` now look like two alternate extent pairs

The writer copies:

- byte `+4` -> `3366`
- byte `+5` -> `33A2`
- byte `+6` -> `33DE`
- byte `+7` -> `1A4A`

Later code in the `C06032+` / `C060A6+` family selects between those pairs based on pose state:

- for states `2` and `6`, it uses `33DE` and `1A4A`
- otherwise, it uses `3366` and `33A2`

Those selected values are then subtracted from cached positions and used in overlap/range checks.

So the safest current statement is:

- bytes `+4..+7` are two alternate geometry/extents pairs, not arbitrary payload bytes

The sample values support that nicely:

- walking poses use `08 08 08 08`
- many effect/simple poses use `00 00 00 00`
- `ATM` uses `0C 08 0C 08`

## Byte `+3` now looks like a shared base attribute byte

This byte is no longer just an unresolved header mystery.

At the `C01EF8` setup call site:

- pose descriptor byte `+3` is read
- zero-extended
- passed in `Y` to `C01D38`

Inside `C01D38`:

- the passed-in value is saved to `$18`
- then OR-ed into runtime byte `2` for every generated 5-byte piece record

Combined with the later `C0:A3A4+` patch loop, the safest current statement is:

- byte `+3` is a shared base attribute byte for the whole pose-driven piece set
- its low bits look more like common OAM-style attributes than geometry data
- the later draw patch then rewrites the priority field, while the per-entry raw byte contributes flip/orientation bits

Representative values are still useful:

- `1A` in walking, mushroom, shadow, and ripple cases
- `1E` in sweat-drops and ATM
- `14` in smoke-cloud

That makes byte `+3` feel much more like a palette/base-attribute selector than a size or range field.

## Best next target

The best next move is to tighten the exact unresolved top bit behavior in the generated attribute byte, while continuing to follow the geometry-family routines that use `2B6E`, `332A`, `3366`, `33A2`, `33DE`, and `1A4A`. That should turn the current descriptive read into real symbolic field names instead of just better structural roles.
