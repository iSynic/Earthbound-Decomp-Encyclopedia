# File Select Setup Option Menus `C1:F497` and `C1:F616`

This note covers the unknown includes around the named text-speed and sound-menu builders:

- `intro/file_select/open_text_speed_menu.asm`
- `unknown/C1/C1F497.asm`
- `intro/file_select/open_sound_menu.asm`
- `unknown/C1/C1F616.asm`
- `intro/file_select/open_flavour_menu.asm`

See also [file-select-window-flavour-refresh-c1ec8f-ecd1.md](notes/file-select-window-flavour-refresh-c1ec8f-ecd1.md).

## Main Result

`C1:F497` and `C1:F616` are the setter/preview wrappers for the setup menu's text-speed and sound-setting choices.

`C1:F497..F616` is now source-backed at `src/c1/c1_f497_open_or_refresh_text_speed_selection.asm`.
`C1:F616..FF2C` is now promoted into byte-equivalent source at `src/c1/c1_f616_open_or_refresh_sound_setting_selection.asm`. The promoted source also covers the adjacent window-flavour selection builder and the main file-select menu loop that follows the sound-setting wrapper.

The community RAM map gives the key state bytes:

- `$98B6` = text speed, with values `1 = Fast`, `2 = Medium`, `3 = Slow`
- `$98B7` = sound setting, with values `1 = Stereo`, `2 = Mono`

The neighboring named routines build the visible menus:

- `C1:F3C2` opens the text-speed menu in window `0x18`
- `C1:F568` opens the sound-setting menu in window `0x19`
- `C1:F6E3` opens the window-style/flavour menu in window `0x32`

`C1:F497` and `C1:F616` sit between those builders and the larger file-select loop as the common "open or update, accept selection, persist if needed" wrappers.

## Shared Shape

Both routines take an argument in `A`:

- `A == 0`: run the selection loop and commit a new value if the player selects one
- `A != 0`: rebuild/preview the current selection without asking for a new one

Both routines:

- store the relevant window id in `$8958`
- enter the C3 window update scope through `C3:E4D4`
- resolve the active window record through `$88E4`, `$867B`, and a `0x2D`-byte record stride at `$89D4`
- follow the record chain according to the current setting byte
- position the text cursor from record fields `+8` and `+0x0A`
- render the selected row text from record field `+0x13`
- restore cursor/window focus afterward
- call `EF:0A4D(currentSlot - 1)` when a committed selection changes save-file setup state

The source names that EF call as `EF0A4D_SaveGameSlot`, shared with ordinary
save-game writes. In this setup context, C1 has already converted the visible
slot number in `$B4A1` to EF's zero-based slot-pair index.

This is the same renderer skeleton with only the state byte and menu builder changed.

## `C1:F497`: Text Speed Setter

`C1:F497` is bound to window `0x18` and `$98B6`.

When called with `A == 0`, it:

- clears `$5E6E`
- runs `C1:196A(1)`
- stores a nonzero selection into `$98B6`
- calls `EF:0A4D(currentSlot - 1)`
- returns the selected value

When called with `A != 0`, it calls the text-speed menu builder at `C1:F3C2`, follows the `$98B6` selected row, redraws the corresponding text, and returns the current `$98B6` value.

Direct callers found locally:

- `C1:F879`
- `C1:F8C0`
- `C1:F922`

All three are inside the file-select setup flow.

## `C1:F616`: Sound Setting Setter

`C1:F616` is bound to window `0x19` and `$98B7`.

When called with `A == 0`, it:

- runs `C1:196A(1)`
- stores a nonzero selection into `$98B7`
- calls `EF:0A4D(currentSlot - 1)` even if the selection is zero
- returns the selected value

When called with `A != 0`, it calls the sound menu builder at `C1:F568`, follows the `$98B7` selected row, redraws the corresponding text, and returns the current `$98B7` value.

Direct callers found locally:

- `C1:F891`
- `C1:F8D9`
- `C1:F929`

## Relationship To Window Flavour

The third setup stage is the named `C1:F6E3` window-style/flavour menu. It uses `$99CD`, the current window-flavour byte, and calls `C1:EC8F` as its preview redraw callback. That completes the setup triad:

- text speed: `$98B6`, menu window `0x18`, setter `C1:F497`
- sound setting: `$98B7`, menu window `0x19`, setter `C1:F616`
- window flavour: `$99CD`, menu window `0x32`, preview helper `C1:EC8F`

The `C1:F616..FF2C` source now names the shared loop glue around this triad:
the file-action menu at `C1:F07E`, copy menu at `C1:F14F`, delete confirmation
at `C1:F2A8`, slot-choice menu at `C1:ED5B`, close/drain helpers at
`C1:0084/008E`, and the C4 file-select pose/entity helpers used by the new-file
flow.

## Working Names

- `C1:F497` = `OpenOrRefreshTextSpeedSelection`
- `C1:F616` = `OpenOrRefreshSoundSettingSelection`
- `C1:F6E3` = `OpenOrRefreshWindowFlavourSelection`
- `C1:F805` = `RunFileSelectMenuLoop`

These names should remain tied to the file-select setup context; the routines are not general-purpose settings APIs.
