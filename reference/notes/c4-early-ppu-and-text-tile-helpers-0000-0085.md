# C4 early PPU and text tile helpers (`C4:0000-C4:00D4`)

## Reference context

This pass starts bank `C4` at the first address-bearing unknown include run in the `ebsrc-main` bank map:

- `unknown/C4/C40000.asm`
- `unknown/C4/C40009.asm`
- `unknown/C4/C40015.asm`
- `unknown/C4/C40023.asm`
- `unknown/C4/C4002F.asm`
- `unknown/C4/C40085.asm`

The current refs checkout gives us the bank map, symbols, and legacy labels, but not the `src/unknown/C4/*.asm` leaves themselves. The local proof therefore comes from ROM decoding plus callers, with the refs used only as boundaries and corroborating address anchors.

Source scaffold status: `src/c4/early_ppu_and_text_tile_helpers.asm` preserves
`C4:0000..C4:0085`, and `src/c4/text_tile_bitset_allocator.asm` preserves the
allocator body at `C4:0085..C4:00D4`. The next byte, `C4:00D4`, is the legacy
`ScriptPtrs` table, not part of the allocator routine.

Source polish:

- 2026-05-01: the `C4:0000..00D4` source now names the `INIDISP` write target,
  display-control shadow, current entity/script slot offsets, `$3492` text tile
  scratch rows, C0 VRAM transfer parameter block `$0091..$0097`, `$9E2B`
  transfer latch, `$1AD6` text tile bitset, recovery script id `$0A2A`, and
  bit-index scratch word `$288E`.

## Display brightness wrappers

`C4:0000` is a tiny `INIDISP` write wrapper. It saves flags, switches the accumulator to 8-bit, writes the low byte of `A` to `$00:2100`, restores flags, and returns long. Direct same-bank callers are `C4:2B07`, `C4:5AE7`, `C4:A28D`, `C4:A2AE`, `C4:A2CF`, and `C4:A2F0`.

`C4:0009` is the paired restore helper. It saves flags, switches to 8-bit `A`, loads `$000D`, writes that value to `$00:2100`, restores flags, and returns long. No direct `JSR` or `JSL` caller was found by the current direct-call scan, so it may be reached through a table, macro sequence, or an unscanned path.

The safest local read is that `$000D` is the display-control shadow for `INIDISP`, while `C4:0000` lets callers write an explicit transient display value.

## C3 temporary actor script helpers

`C4:0015` is the C4-side helper behind the C3 `C40015` pulse/release loops. It uses current slot index `$88`, clears `$10F2,X`, refreshes the current slot's visual profile through `C0:A4A8`, then calls `C0:C6B6` (`CheckCurrentSlotInsideLiveAreaWindow`) and returns long.

That matches the C3-side behavior documented in `notes/c3-temporary-actor-movement-and-release-scripts.md`: the scripts pulse a temporary actor until this helper stops taking the loop branch, then release the current visual entity. The best current name is deliberately descriptive rather than scene-specific.

`C4:0023` is another C3 temporary actor helper. With 16-bit `A`, it loads current script/slot index `$8A`, reads `$1A42`, masks the low nibble, and stores that nibble into `$1372,X`. Decoding it as 8-bit `A` falls through into bogus opcodes, so the call contract must enter with 16-bit accumulator state.

## Text tile transfer pair

`C4:002F` prepares two small VRAM transfer submissions through `C0:8643` (`SubmitQueuedOrImmediateVramTransfer`).

Inputs:

- `A`: row/source index, multiplied by `$20`
- `X`: first destination index, multiplied by `$08`
- `Y`: second destination index, multiplied by `$08`

Transfer setup:

- source pointer low word `$0094 = $3492 + A * $20`
- source offset/high staging `$0091 = 0`
- transfer size `$0092 = $0010`
- source bank `$0096 = $007E`
- first target `$0097 = $6000 + X * 8`
- second target `$0097 = $6000 + Y * 8`, after incrementing source by `$10`

After the two submissions, it writes `$9E2B = ($000D & $0080) ^ $0080`. Given the caller context below, this is most likely the text/window tile strip uploader that refreshes two 16-byte halves from the WRAM tile staging area at `7E:3492`.

The only direct callers found are `C4:4DFA` and `C4:4E2D`.

## Text/window tile bitset allocator

`C4:0085` scans the bitset words at `$1AD6,Y`, starting from `Y = $0008`, looking for a word that is not `$FFFF`. If it reaches `Y = $0040` with every word full, it runs a text/window recovery path:

- `C1:0000` (`RunTextDisplaySetupWrapper`)
- `C1:0BF8`
- `C0:9451`
- `C0:8F68` with `A = $0A2A`

After finding a word with an available bit, it shifts the word left until the sign bit is clear, uses the resulting `X` as an offset into the 16-bit mask table at `C4:4C6C`, ORs that mask into `$1AD6,Y`, and returns:

```text
return A = Y * 8 + (X >> 1)
```

That return value is stored by the main caller into text/window record fields and is later passed back into `C4:002F`, so the current best name is a text tile bitset-slot claim helper. Direct callers are `C4:4E06`, `C4:4E10`, `C4:904A`, and `C4:93A7`.

## Main caller proof

`C4:4DCA` ties the allocator and uploader together:

- base record pointer starts at `$9652`
- current text tile progress derives from `$9E23 >> 3`
- if record fields `+2` and `+4` already contain tile indices, the routine calls `C4:002F` directly
- otherwise it calls `C4:0085` twice, stores the two returned tile indices into record fields `+2` and `+4`, calls `C4:002F`, then calls `C4:4C8C`
- it loops until the stored record progress catches up with `$9E23 >> 3`

This makes the early `C4:002F`/`C4:0085` pair part of the text/window tile allocation and refresh path rather than generic map animation code.

`C4:4C8C` is now pinned as the descriptor placement half of this same path. It takes the two tile ids in `A/X`, releases any existing nonblank tile words at the active cursor and the row below it, writes the two replacement tile words into the active descriptor buffer, and advances the descriptor cursor.

## Working Names

- `C4:0000` = `WriteAtoInidisp`
- `C4:0009` = `RestoreInidispFromDisplayShadow`
- `C4:0015` = `ClearCurrentSlot10f2RefreshVisualAndCheckLiveArea`
- `C4:0023` = `StoreLowNibble1a42ToCurrentScriptField1372`
- `C4:002F` = `SubmitTwoTextTileStripTransfers`
- `C4:0085` = `ClaimTextTileBitsetSlot`
- `C4:008F` = `ScanNextTextTileBitsetWord`
- `C4:00A9` = `TestTextTileBitsetWordFull`
- `C4:00B6` = `FindFirstClearTextTileBit`
- `C4:00B9` = `ClaimTextTileBit`
- `C4:4C6C` = `TextTileBitMaskTable`
- `C4:4C8C` = `PlaceTextTilePairAtActiveCursor`
- `C4:4DCA` = `CatchUpTextTileStripTransfers`

## Remaining questions

- `C4:0009` needs a non-direct caller or table reference before we can say whether it is an active restore path or a retained helper.
- `C4:904A` and `C4:93A7`, the other `C4:0085` callers, should be followed later to determine whether the same allocator also supports non-text visual effects.
- The exact user-facing meaning of the `$964D` leading-space/control-token gate in `C4:4C8C` is still softer than the tile-placement mechanics.
