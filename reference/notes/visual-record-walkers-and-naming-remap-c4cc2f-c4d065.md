# Visual Record Walkers And Naming Remap `C4:CC2F..D274`

This span contains two adjacent but semantically separate families:

- `C4:CC2F..CED8` walks the dynamic visual-record table rooted at `$B4AA/$B4AC`.
- `C4:D00F..D274` remaps naming-entry bytes into the committed selector text buffer.

The split matters because `C4:D00F` is caller-dense in the cluster map, but all eight callers are same-routine `JSR`s from `C4:D065`; it is not part of the visual-record walker family.

## Source status

This span is now split into two durable C4 source modules:

- `src/c4/visual_record_walker_helpers.asm` covers `C4:CC2F..C4:D00F`.
- `src/c4/naming_buffer_remap_helpers.asm` covers `C4:D00F..C4:D274`.

Both modules validate byte-for-byte, and the combined C4 scaffold validates with
`0` mismatches.

## Visual-record table contract

The visual walkers consume the 0x14-byte records allocated by the preceding `C4:C91A` family, now documented in `notes/visual-record-constructor-and-latches-c4c8a4-c4cbe3.md`:

- record table long pointer: `$B4AA/$B4AC`
- record count: `$B4A6`
- record stride: `0x14`
- field `+0`: slot/profile id used by `C4:29AE`
- field `+4`: state selector
- fields `+6/+8`: dimensions or span limits
- fields `+0A/+0C`: source or visual-profile pointers consumed by merge helpers
- fields `+10/+12`: per-record progress counters

The same table is also managed nearby by `C4:CB4F`, `C4:CB8F`, and `C4:CBE3`, which clear/set related slot latches for records in state `1`.

## State-2 frame strip walker

`C4:CC2F` walks every record whose state field `+4` is `2`.

For each unfinished matching record:

- it uses `+10` as the current strip/frame cursor
- derives the destination offset from `+6`, `+8`, and the cursor
- calls `C4:28D1` to copy strided words into the `$7F` visual buffer
- calls `C4:29AE` to generate the render DMA strips for the record slot/profile
- advances cursor `+10` by two
- wraps the cursor to `1` and increments completion counter `+12` when the cursor reaches the `+8` limit

The return value is the number of matching state-2 records that are not yet complete: total state-2 matches minus records whose `+12` counter is already `2`.

## State-3 masked-column walker

`C4:CD44` walks records whose state field `+4` is `3`.

It uses the state/progress pair `+10/+12` to alternate which side of the width is being merged:

- it reflects odd/even cursor positions around field `+6`
- calls `C4:28FC` to merge masked `$7F` tile-column rows
- calls `C4:29AE` to rebuild the render DMA strips
- advances `+10`
- when `+10` reaches half of `+6`, increments completion counter `+12` and resets `+10`

Like the state-2 walker, it returns matching state-3 records minus records whose completion counter is already `2`.

## State-4 random tile-mask walker

`C4:CEB0` clears the 64-entry word bitmap at `$7F:7F00`.

`C4:CED8` uses that bitmap as a one-shot occupancy map:

- starts from `C0:8E9A() & 0x3F`
- scans forward modulo 64 until it finds a free word
- marks the selected word occupied
- splits the selected index into an 8-wide grid coordinate
- walks all records whose state field `+4` is `4`
- for every 8-pixel cell covered by fields `+6/+8`, calls `C4:2965`
- calls `C4:29AE` once per matching record after the merge loop

This is best treated as a random/unclaimed tile-mask stepper over state-4 visual records, not as a generic random-number helper.

2026-05-06 walker source contract follow-up: the walker source now names the
shared `$B4AA/$B4AC` table pointer, `$B4A6` record count, `0x14` stride, fields
`+00/+04/+06/+08/+0A/+0C/+10/+12`, state filters `2/3/4`, completion counter
limit `2`, and the `$7F:7F00` 64-word occupancy bitmap used by the state-4
random tile-mask pass. The comments keep the C4-owned cursor/occupancy math
separate from the C4:28xx merge helpers and C4:29AE render-strip generator,
which remain callee-owned.

## Naming remap pair

`C4:D065` has one direct local caller, `C1:EBBF`, in the naming commit path:

- source: `$9C9F`
- destination: `$9801`

It reads a NUL-terminated source buffer, remaps naming bytes, and writes a NUL-terminated destination buffer. It has special handling for `A/I/U/E/O`, broad uppercase-letter handling, repeated-letter handling via emitted byte `$7E`, and a previous-`N` path that emits `$9D`.

`C4:D00F` is a local helper for `C4:D065`. It indexes table `$C3:FB45` by `(letter - 'A') * 10 + vowelIndex * 2`, copies up to two nonzero bytes to the destination pointer, and returns the advanced destination pointer.

Although the entry label is `C4:D065`, the normalizer body runs through
`C4:D274`, where it writes the terminating NUL byte and returns via `RTL`.

## Working Names

- `C4:CC2F` = `StepState2VisualRecordFrameStrips`
- `C4:CD44` = `StepState3VisualRecordMaskedColumns`
- `C4:CEB0` = `ClearVisualRecordOccupancyBitmap7f7f00`
- `C4:CED8` = `StepState4VisualRecordRandomTileMask`
- `C4:D00F` = `AppendNamingVowelRemapBytes`
- `C4:D065` = `NormalizeNamingBufferToCommittedSelectorText`

Constructor-side names live in `notes/visual-record-constructor-and-latches-c4c8a4-c4cbe3.md`:

- `C4:C8A4` = `InitVisualRecordTable7f7c00`
- `C4:C8DB` = `AllocVisualRecordScratchBytes`
- `C4:C8E9` = `ClearVisualRecordScratchSpan7f`
- `C4:C91A` = `AppendDynamicVisualRecord`
- `C4:CB4F` = `ClearVisualRecordSlot4000Flags`
- `C4:CB8F` = `RefreshVisualRecordsAndClearState1Latch`
- `C4:CBE3` = `SetState1VisualRecordLatchFFFF`

## Confidence boundaries

### Locally proved

- `C4:CC2F`, `C4:CD44`, and `C4:CED8` all walk the 0x14-byte record table rooted at `$B4AA/$B4AC`.
- Their state filters are exactly `2`, `3`, and `4`.
- `C4:CEB0` clears 64 words at `$7F:7F00`, and `C4:CED8` uses that area as an occupancy bitmap.
- `C4:D00F` is called only by `C4:D065` locally.
- `C4:D065` is called by the naming commit flow at `C1:EBBF` and writes the normalized committed buffer at `$9801`.

### Still open

- the player-visible name of the visual effect represented by record states `2`, `3`, and `4`
- exact semantic names for the record fields beyond the local table contract
- the exact glyph/phonetic identity of table `$C3:FB45`, beyond its current role as the naming vowel remap table
