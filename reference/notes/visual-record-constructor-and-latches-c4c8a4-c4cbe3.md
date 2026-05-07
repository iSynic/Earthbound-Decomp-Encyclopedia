# Visual Record Constructor And Latches `C4:C8A4..CBE3`

## Scope

This note documents the constructor/maintenance side of the dynamic visual-record table consumed by `C4:CC2F..CED8` in `notes/visual-record-walkers-and-naming-remap-c4cc2f-c4d065.md`.

## Source status

The constructor/latch span is now promoted as
`src/c4/visual_record_constructor_latch_helpers.asm`, covering
`C4:C8A4..C4:CC2F` byte-for-byte. The promoted range includes the tiny
`C4:CC2C` return stub immediately before the visual-record walker family begins.

The common table contract is now stronger:

- `$B4AA/$B4AC` = long pointer to the 0x14-byte visual-record table
- `$B4A6` = record count
- `$B4A4` = byte allocator cursor for extra per-record scratch spans
- `$B4A8` = lazily allocated handle/id initialized through `C0:92F5`
- default table base = `7F:7C00`
- constructor clears 0x400 bytes at the table base

## `C4:C8A4`

`C4:C8A4` initializes the visual-record table:

- clears `$B4A4` and `$B4A6`
- installs `7F:7C00` into `$B4AA/$B4AC`
- clears 0x400 bytes at `7F:7C00` through `C0:8F15`

It is called by `C4:C91A` on first record append, when `$B4A8 == FFFF`.

## Allocation helpers

`C4:C8DB` is the bump allocator for per-record scratch bytes. It returns the old `$B4A4` cursor in `A` and then adds the caller-supplied byte count to `$B4A4`.

`C4:C8E9` clears a byte span in bank `7F`: caller `A` is the low word offset, `X` is the byte count, and the helper writes zero bytes from `7F:A` for `X` bytes. `C4:C91A` uses it immediately after allocating the per-record span.

## `C4:C91A`

`C4:C91A` appends one visual record unless the request is filtered out:

- rejects state/mode `X == 0`, `1`, or `6`
- rejects profile/slot `A` when `$2ABA[A * 2] == 0`
- lazily initializes the table and `$B4A8` if `$B4A8 == FFFF`
- appends at `recordBase + $B4A6 * 0x14`
- increments `$B4A6` after filling the record

Record fields filled by this constructor:

- `+00` = input `A`, also used to set bit `$4000` in `$116A[A * 2]`
- `+02` = input `X`
- `+04` = initial state selector chosen from input `X`
- `+06` = footprint width from `C4:2A63`
- `+08` = `$2ABA[A * 2] * 8`
- `+0A` = scratch offset allocated by `C4:C8DB`
- `+0C` = `+0A + +0E`
- `+0E` = half-size derived by `C0:9032`
- `+10/+12` = zeroed progress counters

The constructor also copies the starting visual data through `C4:283F` or `C4:2884` depending on the profile id, and it regenerates render DMA strips through the downstream walkers later.

Input `X` controls the initial state/latch side effect:

- `2` or `7` set `$0E5E[$B4A8] = 1` and record state `1`
- `3` or `8` set `$0E9A[$B4A8] = 1` and record state `2`
- `4` or `9` set `$0ED6[$B4A8] = 1` and record state `3`
- `5` or `0A` set `$0F12[$B4A8] = 1` and record state `4`

After the state-specific latch, it sums those four latch words into `$0F4E[$B4A8]`.

Direct callers:

- `C1:6579`
- `C1:67CD`
- `C1:6829`
- `C1:688E`
- `C1:6D04`
- `C1:6D52`

The callers sit in event/text-control paths that resolve a visual slot/profile through C4 entity-resolver helpers (`C4:605A`, `C4:608C`, `C4:6507`, etc.), append this visual effect record, then call matching set/clear helpers around the same target.

## Latch maintenance

`C4:CB4F` walks all records and clears bit `$4000` from `$116A[record[0] * 2]`. This is the broad "records no longer own the high visual flag" cleanup.

`C4:CB8F` walks every record, and for records whose state field `+04` is `1`, clears `$10F2[record[0] * 2]`. It also calls `C0:A48F(record[0])` for every record, refreshing the visual profile after latch changes.

`C4:CBE3` walks every record and, for records whose state field `+04` is `1`, sets `$10F2[record[0] * 2] = FFFF`.

These three routines are maintenance helpers over the records created by `C4:C91A`; they do not allocate or destroy records themselves.

2026-05-06 source contract follow-up: the constructor/latch source now carries
local names for `$B4A4/$B4A6/$B4A8/$B4AA/$B4AC`, the default `7F:7C00` record
table, the `0x14` record stride, fields `+00..+12`, request modes `2..0A`,
state selectors `1..4`, the `$FFFF` unset-handle sentinel, the `$116A/$4000`
visual-profile flag, the four `$0E5E/$0E9A/$0ED6/$0F12` latch lanes, `$0F4E`
latch sum, and the state-1 `$10F2` profile latch. C4 still only records its
local writes and caller joins; `C0:92F5`, `C0:8F15`, and `C0:A48F` remain
external allocation/clear/refresh callees.

## Working Names

- `C4:C8A4` = `InitVisualRecordTable7f7c00`
- `C4:C8DB` = `AllocVisualRecordScratchBytes`
- `C4:C8E9` = `ClearVisualRecordScratchSpan7f`
- `C4:C91A` = `AppendDynamicVisualRecord`
- `C4:CB4F` = `ClearVisualRecordSlot4000Flags`
- `C4:CB8F` = `RefreshVisualRecordsAndClearState1Latch`
- `C4:CBE3` = `SetState1VisualRecordLatchFFFF`

## Open edges

- `$B4A8` is clearly a lazily allocated handle/id used as the index for the four latch words, but the exact owner of the `C0:92F5(#035B)` allocation still needs a C0-side naming pass.
- The player-visible effect names for states `1..4` remain open; the byte contract is solid enough to name the constructor mechanically.
