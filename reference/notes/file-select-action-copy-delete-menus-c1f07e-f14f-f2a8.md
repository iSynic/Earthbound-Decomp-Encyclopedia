# File Select Action, Copy, And Delete Menus `C1:F07E`, `C1:F14F`, and `C1:F2A8`

This note covers the unknown includes between `intro/file_select_menu.asm` and `intro/file_select/open_text_speed_menu.asm`.

See also [file-select-window-flavour-refresh-c1ec8f-ecd1.md](notes/file-select-window-flavour-refresh-c1ec8f-ecd1.md).

## Main Result

The upstream file-select slot-choice and save-corruption strip `C1:ECD1..F07E` is now source-backed at `src/c1/c1_ecd1_preview_packed_high_byte_window_flavour.asm`, so `C1:F07E` now has a decoded source predecessor rather than a preserved-byte landing edge.
The action/copy/delete setup strip `C1:F07E..F497` is now source-backed through `src/c1/c1_f07e_open_file_select_action_menu.asm`, `src/c1/c1_f14f_open_copy_destination_menu.asm`, and `src/c1/c1_f2a8_open_delete_file_confirmation_menu.asm`.

These three routines are file-select submenu builders:

- `C1:F07E` builds and runs the `Continue / Copy / Delete / Set Up` action menu
- `C1:F14F` builds and runs the `Copy to where?` destination-slot menu
- `C1:F2A8` builds and runs the delete-file confirmation menu

The community `Standard_arguments.txt` corroborates the window ids used here:

- window `0x14`: `Continue/Copy/Delete/Setup`
- window `0x15`: copy menu with two slots available
- window `0x16`: copy menu with one slot available
- window `0x17`: delete-file confirmation

The legacy disassembly also names the local string anchors as `Continue`, `Copy`, `Delete`, `Set Up`, `Copy to where?`, `Are you sure you want to delete?`, `No`, and `Yes`.

## `C1:F07E`: Main File-Action Menu

`C1:F07E`:

- opens window/context `0x14`
- always inserts row `1` with `Continue`
- scans the three save-slot status bytes at `$B49E..$B4A0`
- only inserts `Copy` when at least one non-current slot is empty/available
- inserts `Delete` as row `3`
- inserts `Set Up` as row `4`
- finalizes the menu through `C1:163C`
- sets `$5E6E = 0x00FF`
- runs `C1:196A(1)`
- returns the selected option, with `0` as cancel/close

The caller at `C1:F824` dispatches these return values in menu order:

- `0`: close/reopen
- `1`: continue/start the selected file
- `2`: copy file
- `3`: delete file
- `4`: setup

The caller source in `C1:F805` now names this dispatch edge as
`C1F07E_OpenFileSelectActionMenu` instead of a raw same-bank branch target.

## `C1:F14F`: Copy Destination Slot Menu

`C1:F14F` first counts save slots whose `$B49E + slot` byte is zero.

If exactly one destination is available, it opens window `0x16`; otherwise it opens window `0x15`. In both cases it:

- prints `Copy to where?`
- builds per-slot labels through `$9C9F`
- uses `0x61 + slot` for the visible slot letter
- appends byte `0x6A` and a terminator
- finalizes and runs `C1:196A(1)`

On a nonzero selection, it calls `EF:0C15(currentSlot - 1, selectedRow - 1)`, which is the actual save-copy operation. It then clears `$5E6E`, closes the active window through `C1:0084`, and returns the selection.

The file-select loop source now calls this helper by the
`C1F14F_OpenCopyDestinationMenu` role when the action menu returns `2`.

## `C1:F2A8`: Delete Confirmation Menu

`C1:F2A8..F497` is now source-backed at `src/c1/c1_f2a8_open_delete_file_confirmation_menu.asm`.

`C1:F2A8` opens window `0x17` and builds the selected-file summary before asking for confirmation:

- prints `Are you sure you want to delete?`
- prints the selected file number from `$B4A1`
- prints the current selected-file character/name summary through `C1:931B(1)`
- prints `Level:` and the level byte at `$99D3`
- inserts `No` as option `0`
- inserts `Yes` as option `1`
- finalizes and runs `C1:196A(1)`

On a nonzero selection, it calls `EF:0BFA(currentSlot - 1)`, which is the actual delete-file operation. It then clears `$5E6E`, closes the window, and returns the menu result.

The file-select loop source now calls this helper by the
`C1F2A8_OpenDeleteFileConfirmationMenu` role when the action menu returns `3`.

## Working Names

- `C1:F07E` = `OpenFileSelectActionMenu`
- `C1:F14F` = `OpenCopyDestinationMenu`
- `C1:F2A8` = `OpenDeleteFileConfirmationMenu`
- `C1:F3C2` = `OpenTextSpeedMenu`

These are no longer mystery chunks; they are the file-select action menu's three immediate submenu bodies.
