# File Select Window Flavour Refresh `C1:EC8F` and `C1:ECD1`

This note covers the two unknown includes immediately after `intro/name_a_character.asm` and before the save corruption/file-select cluster.

See also [naming-buffer-commit-family-c1ead6-c4d065.md](notes/naming-buffer-commit-family-c1ead6-c4d065.md).

## Main Result

`C1:EC8F` is a scoped current-window-flavour redraw helper, and `C1:ECD1` is a tiny packed-byte wrapper around it.

`C1:ECD1..F07E` is now source-backed at `src/c1/c1_ecd1_preview_packed_high_byte_window_flavour.asm`. The promoted strip also covers the adjacent corrupt-save notice, save-slot choice menu, and selected-slot checksum return tail.

The strongest corroboration comes from the community RAM map:

- `$98B6` = text speed
- `$98B7` = sound setting
- `$99CD` = current window "flavor"

The legacy disassembly confirms the same file-select/name-entry neighborhood and shows `C1:EC8F` reused by the window-style menu body at `C1:F6E3..F804`.

## `C1:EC8F`: Temporary Flavour Apply And Redraw

`C1:EC8F(A)`:

- saves the incoming low byte in a local slot
- saves the previous byte at `$99CD`
- writes the incoming byte into `$99CD`
- calls `C4:7C3F`
- then calls the C4 redraw/update pair ending in `C4:7F87`
- sets `$0030 = 0x18`
- restores the saved `$99CD`
- returns through `RTL`

This is not a permanent preference setter. It temporarily changes the current window flavour, forces the relevant text-window/window-style refresh, then restores the original flavour byte.

There is a width-sensitive decode wrinkle in the middle of the routine: after `C4:7C3F`, the byte stream is consistent with `LDA #$0002; JSL C4:4963` if the callee returns with 16-bit accumulator state. `C4:4963` is now best read as `RefreshTextWindowVramPlanesForMode`; mode `2` submits the fixed `$7F` window/tile source ranges through the queued-transfer path and then includes the `$7F:2000 -> VRAM $7000` block. The surrounding behavior and the legacy disassembly both support treating this as an intentional redraw/update sequence rather than code/data desync.

## `C1:ECD1`: Packed-Byte Adapter

`C1:ECD1(A)` does only:

- `XBA`
- `AND #$00FF`
- `JSL C1:EC8F`

So `C1:ECD1` extracts the high byte of a packed word and previews/applies that value through the same temporary flavour redraw helper.

The direct caller at `C1:F03E..F063` is in the selected-file display/name-entry path, after the save-slot choice is committed. That makes `C1:ECD1` the high-byte adapter for stored setup/profile data rather than a standalone menu.

## Callers

Direct code references found locally:

- `C1:ECD7 -> C1:EC8F`, inside the `C1:ECD1` wrapper
- `C1:F7EF -> C1:EC8F`, inside the window-style/flavour menu cancel path

2026-05-06 source polish names the `C1:ECD7 -> C1:EC8F` wrapper edge directly
as `C1EC8F_PreviewWindowFlavourAndRedraw`, matching the existing runtime
contract and preserving byte equivalence.

## Working Names

- `C1:EC8F` = `PreviewWindowFlavourAndRedraw`
- `C1:ECD1` = `PreviewPackedHighByteWindowFlavour`
- `C1:ECDC` = `ShowCorruptSaveFilesNotice`
- `C1:ED5B` = `OpenFileSelectSlotChoiceMenu`
- `C1:F03E` = `RunFileSelectSlotChoiceAndPreview`
- `C1:F06B` = `ReturnSelectedSaveSlotAfterChecksum`

The exact C4 helper names are still soft, but the state touched by this pair is now clear: `$99CD`, the current text-window flavour byte.
