# Secondary Visual Descriptor (`DATA_C42B0D`)

This note captures the secondary descriptor family selected after the sprite-pose descriptor in the `C01E49` setup path.

See also [sprite-pose-descriptor-cache-2a06-2cd6.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/sprite-pose-descriptor-cache-2a06-2cd6.md).
See also [sprite-pose-descriptor-header-bytes-2-7.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/sprite-pose-descriptor-header-bytes-2-7.md).
See also [visual-frame-selector-update-family-c4-62ff.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/visual-frame-selector-update-family-c4-62ff.md).
See also [child-entity-spawn-c4b3d0-c40de8.md](/F:/Earthbound%20Decomp%20-%20Codex/notes/child-entity-spawn-c4b3d0-c40de8.md).

## Main result

A useful second layer finally surfaced.

After the setup path chooses the sprite-pose descriptor from `EF:133F`, it also computes a smaller index in `$02` and uses that to select a second descriptor through `DATA_C42B0D`.

That second descriptor is the source for `2BE6` and several freshly reset per-entity state words. So it should be treated as a separate visual/placement descriptor layer, not as part of the pose header itself.

## Local selection path

In the main entry around `C01E49`:

1. `$2B` selects the pose descriptor from `EF:133F`.
2. `JSR C01DED` derives a smaller index in `$02`.
3. That index selects a long pointer from `DATA_C42B0D`.
4. The selected record becomes the active `$0A/$0C` descriptor source.

So the safest current statement is:

- `EF:133F` chooses the sprite-pose descriptor
- `DATA_C42B0D` chooses a second visual/placement descriptor tied to the derived subtype in `$02`

## This family really does use the `467E` piece-record path

One ambiguity from the wider entity system is now resolved locally.

The generic entity update path loads `112E` and dispatches through the per-entity handler at `11E2`. A separate handler at `C0:A0FA` treats `112E` as a word table, which initially made the `467E` 5-byte-record interpretation look risky.

But the setup path for this family explicitly installs:

- `11E2 = C0:A3A4`

not `C0:A0FA`.

That matters because `C0:A3A4+` is exactly the draw-side patch helper that walks the 5-byte runtime entries and rewrites byte `+2` across contiguous groups. So the current `467E` record model is still on solid ground for this family even though other entity handlers can reuse `112E` differently.

## Header layout

The current best local header sketch is:

- byte `0` = body entry count copied in each `C01D38` pass
- byte `1` = number of pieces in the first priority band, very likely the upper-section piece count

That corrects an earlier guess: byte `1` does not behave like a second independent entry count inside `C01D38`.

## Why byte `0` is the entry count

The `C01D38` copier:

- reads descriptor byte `0` into `$16`
- advances the record pointer by `2`
- then runs two body-copy passes (`Y = 0` and `Y = 1`)
- in each pass, it copies exactly `$16` entries
- each copied entry advances the input pointer by `5`

This matches the sample record lengths perfectly:

- `DATA_C42B51`: `2 + 1*2*5 = 12` bytes
- `DATA_C42BA9`: `2 + 2*2*5 = 22` bytes
- `DATA_C42BBF`: `2 + 4*2*5 = 42` bytes
- `DATA_C42C29`: `2 + 6*2*5 = 62` bytes

So the strongest current statement is:

- byte `0` is the number of body entries copied in each `C01D38` pass
- total body entries copied by `C01D38` = `2 * byte0`

## Why byte `1` now looks like an upper-section piece count

The strongest local consumer is the `C0:A3A4+` draw-side helper.

That code:

- in 8-bit mode, loads `2BE7` into `X`
- starts with `Y = #$FD`, then advances in 5-byte steps to byte offset `+2` of each runtime entry
- patches runtime byte `2` across the first contiguous group
- then, without resetting the running offset, loads `2BE6` into `X`
- continues patching runtime byte `2` across the next contiguous group

So the safe structural statement is:

- the secondary descriptor header is dividing the copied pieces into two contiguous priority bands

The more useful interpretation is that byte `1` lines up unusually well with the size of the first visible section in the sample layouts.

Examples:

- `DATA_C42BBF`: 4 pieces arranged as `2 x 2`, header `04,02` -> first band = top row (2 pieces)
- `DATA_C42C29`: 6 pieces arranged as `3 x 2`, header `06,03` -> first band = top row (3 pieces)
- `DATA_C42CA5`: 3 pieces arranged as `1 x 3`, header `03,02` -> first band = top two pieces
- `DATA_C42D03`: 9 pieces arranged as `3 x 3`, header `09,06` -> first band = top two rows (6 pieces)
- `DATA_C42D5F`: 12 pieces arranged as `4 x 3`, header `0C,08` -> first band = top two rows (8 pieces)

That fits the existing upper/lower-body split elsewhere in the entity system much better than a generic boundary/count explanation.

So the safest current statement is:

- byte `1` is very likely the piece count in the upper or front priority band
- byte `0 - byte1` is then the piece count in the lower or back priority band

I am still keeping the exact semantic label slightly cautious because I have not yet tied it to the named upper/lower-body RAM fields directly.

## Body layout now looks like repeated 5-byte entries

`C01D38` is the strongest bridge between raw secondary records and live runtime data.

For each entry, it writes 5 bytes into the live `467E` pool, then advances the input pointer by `5`.

So the safest current statement is:

- after the 2-byte header, the secondary descriptor body is a repeated 5-byte entry stream

## What the 5-byte entry fields look like

The per-entry copy logic in `C01D38` behaves like this:

- raw byte `0` is copied directly into runtime byte `0`
- runtime byte `1` is not taken from the raw stream; it is regenerated from `DATA_C4303C` using the caller's base index plus the per-entry ordinal
- raw byte `2` is copied into runtime byte `2` after masking with `#$FE` and OR-ing in:
  - the high byte from the generated `DATA_C4303C` word
  - the pose-descriptor byte `+3` that was passed in through `Y`
- raw byte `3` is copied directly into runtime byte `3`
- raw byte `4` is copied directly into runtime byte `4`

That means the raw second byte visible in samples like `00,02,04,06` is effectively replaced at runtime by the generated tile-word sequence from `DATA_C4303C`.

The best current read is that these 5-byte entries are generic sprite-piece records.

A useful cross-check comes from [entity_overlays.asm](/F:/Earthbound%20Decomp%20-%20Codex/refs/ebsrc-main/ebsrc-main/src/data/events/entity_overlays.asm), where the frame data uses the same practical shape:

- relative Y byte
- tile/attribute word
- relative X byte
- trailing attribute byte

So the safest current 5-byte entry sketch is:

- byte `0` = relative Y position
- byte `1` = tile-word low byte, regenerated at runtime from `DATA_C4303C`
- byte `2` = sprite tile/attribute high byte
- byte `3` = relative X position
- byte `4` = trailing attribute/extension byte

That is materially better than the older "two coordinate-like fields plus flags" wording.

## What runtime byte `2` now looks like

The draw-side patch helper `C0:A3A4+` is the clearest consumer so far.

That code:

- walks directly to byte offset `+2` of each 5-byte runtime entry
- does `AND #$CF`
- then ORs in either `#$20` or `#$30`

So the strongest current statement is:

- runtime byte `2` is the sprite tile/attribute high byte
- bits `4-5` behave like a priority field, because `C0:A3A4+` clears and rewrites exactly those bits

The current best combined bit map is:

- bit `7` = vertical flip
- bit `6` = horizontal flip
- bits `4-5` = priority, patched at draw time by `C0:A3A4+`
- bit `0` = tile-number high bit, regenerated from `DATA_C4303C`
- bits `1-3` = still look palette-like or OAM-subattribute-like, but are not fully split yet

The bit `6` read stays strong because paired second-pass entries often carry `#$40` where first-pass entries carry `#$00`, which matches [entity_overlays.asm](/F:/Earthbound%20Decomp%20-%20Codex/refs/ebsrc-main/ebsrc-main/src/data/events/entity_overlays.asm)'s `ORIENTATION::HORIZONTAL = $4000` usage.

Bit `7` is now better than a vague high-bit guess. The same reference file uses `ORIENTATION::VERTICAL = $8000`, and the local copier/draw path supports that read cleanly:

- `C01D38` only clears raw bit `0` before OR-ing in tile-high plus pose-base-attribute data
- `C0:A3A4+` only clears bits `4-5`
- neither `DATA_C4303C` high bytes nor sampled pose byte `+3` values explain bit `7`

So the safest current statement is:

- bit `7` is very likely the vertical-flip input carried straight through from raw secondary descriptor byte `2`

That is reference-backed and locally consistent rather than purely locally proved, so I am treating it as strong but not absolutely closed.

## The two body-copy passes are facing-direction copies

`C01D38` runs two outer passes. Within each pass it copies `byte0` entries using the same `DATA_C4303C` tile sequence.

Looking at actual descriptor body data:

- pass 0 entries consistently have raw byte `2 = #$00`
- pass 1 entries consistently have raw byte `2 = #$40`

So the safest current statement is:

- pass 0 = unflipped facing-direction copy
- pass 1 = horizontally flipped facing-direction copy

Calling them specifically `right` and `left` is plausible and often likely, but I am keeping that final naming slightly cautious until a tighter local facing consumer is pinned.

## `C02291` spatial test re-read

`C02291` reads descriptor bytes `+2` and `+3` from the live `$0A/$0C` descriptor pointer. Those bytes are also exactly what we would read as the first body entry's byte `0` and byte `1` if the record is treated as `2-byte header + 5-byte entries`.

Locally the code uses them as coarse spatial inputs:

- byte `+2` is shifted right 3 and combined with `$28`
- byte `+3` is shifted right 3 and combined with `$26`
- the result indexes `D7:A800`

So the safest current statement is:

- `C02291` performs a map/collision-style spatial test using the leading piece's placement data
- descriptor bytes `+2/+3` are better read as reused first-entry fields than as standalone header bytes

The awkward part remains that runtime byte `1` is later regenerated from `DATA_C4303C`, so I am still treating the exact role of raw body byte `1` as a dual-use field rather than a cleanly named X offset.

## Why bytes `2` and `3` no longer look like pure header fields

An earlier pass treated descriptor bytes `2` and `3` as if they were dedicated header fields.

The cleaner current view is:

- `C02291` does read bytes `2` and `3` specially
- but those bytes are also exactly the first body's entry `0` bytes `0` and `1` if the record is interpreted as `2-byte header + 5-byte entries`
- so they are better read as the leading entry's placement/index fields, reused by the setup-side spatial test

That is a better fit for the record lengths and the body copier.

## Pose descriptor byte `+3` is now a real shared piece-format field

The local role of pose descriptor byte `+3` is much clearer now.

At the `C01EF8` setup call site:

- the setup path reads pose descriptor byte `+3`
- passes it in `Y` to `C01D38`

Inside `C01D38`:

- that value is saved to `$18`
- then OR-ed into runtime byte `2` for every generated 5-byte piece record

Because runtime byte `2` is also where the high byte of the generated `DATA_C4303C` word lands, the safest current statement is:

- pose descriptor byte `+3` is a shared base attribute byte for the whole secondary piece record family
- in practical terms, it looks like it provides the common low-bit OAM-style attributes while `C0:A3A4+` later rewrites the priority field and the per-entry raw byte contributes flip/orientation bits

That is much better than treating byte `+3` as another geometry mystery.

## Associated state reset

Immediately after `2BE6` is written, the setup path initializes or clears:

- `2D4E = FFFF`
- `2D12 = FFFF`
- `2C9A = FFFF`
- `289E = FFFF`
- `2BAA = 0000`
- `2DC6 = 0000`
- `2D8A = 0000`
- `2C5E = 0000`
- `2B32 = 0000`
- `2AF6 = 0000`
- `28DA = 0000`

So this descriptor clearly participates in the broader visual-state initialization, not just pose selection.

## What still remains open

- The exact semantics of trailing attribute byte `4` in body entries. In the `C4:2BBF` descriptor the last pass-0 and last pass-1 entries carry `#$80` there while other entries carry `#$00`. No direct local consumer of that byte has been traced yet.
- The full bit decomposition of bits `1-3` of runtime byte `2`.
- A direct local bridge from the two priority bands into a named upper/lower-body entity state path.

## What is now settled

- byte `0` = entries copied per pass
- byte `1` = likely first-band or upper-band piece count
- body = repeated 5-byte sprite-piece records
- pass 1 is the horizontally flipped partner of pass 0
- bit `6` = horizontal flip
- bits `4-5` = draw-time priority field
- bit `0` = generated tile-number high bit
- pose byte `+3` = shared base attribute byte

## Best next target

The best next move is to tighten the remaining low-bit attribute split in runtime byte `2` or find a direct consumer of trailing byte `4`, because the high-level struct is now in fairly good shape.
