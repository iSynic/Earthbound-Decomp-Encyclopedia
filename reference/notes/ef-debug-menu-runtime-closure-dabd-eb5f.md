# EF Debug Menu Runtime Closure, `EF:DABD..EF:EB5F`

This note closes the readable-source split for the EF debug/menu corridor that
sat between the decoded state initializer and the debug font asset.

## Reference Order

The split follows `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank2f.asm`:

- `system/debug/display_menu_options.asm`
- `system/debug/integer_to_hex_debug_tiles.asm`
- `system/debug/integer_to_decimal_debug_tiles.asm`
- `system/debug/integer_to_binary_debug_tiles.asm`
- `system/debug/display_check_position_debug_overlay.asm`
- `system/debug/display_view_character_debug_overlay.asm`
- `unknown/EF/EFDF0B.asm`
- `unknown/EF/EFDFC4.asm`
- `unknown/EF/EFE07C.asm`
- `unknown/EF/EFE133.asm`
- `unknown/EF/EFE175.asm`
- `system/debug/load_debug_cursor_graphics.asm`
- `system/debug/handle_cursor_movement.asm`
- `system/debug/process_command_selection.asm`
- `system/debug/load_menu.asm`
- the small `EFE6CF..EFEB3D` unknown/debug helper tail
- `data/unknown/EFEB1D.asm`
- `unknown/EF/EFEB2A.asm`
- `data/unknown/EFEB3D.asm`

The referenced ebsrc tree gives include names and order here, but not local
file bodies, so the generated source is based on byte-equivalent local decode
plus the include anchors.

## Promoted Source

| Range | File | Role |
| --- | --- | --- |
| `EF:DABD..EF:DCBC` | `src/ef/ef_dabd_dcbc_debug_menu_text_number_helpers.asm` | Debug text row writer plus hex, decimal, and binary tile-buffer formatters. |
| `EF:DCBC..EF:DE1A` | `src/ef/ef_dcbc_de1a_debug_check_position_overlay.asm` | Check-position debug overlay writer. |
| `EF:DE1A..EF:DF0B` | `src/ef/ef_de1a_df0b_debug_view_character_overlay.asm` | View-character debug overlay writer. |
| `EF:DF0B..EF:E175` | `src/ef/ef_df0b_e175_debug_overlay_tile_helpers.asm` | Tile-code resolution and overlay row sweep helpers. |
| `EF:E175..EF:EB1D` | `src/ef/ef_e175_eb1d_debug_menu_runtime_helpers.asm` | Debug menu runtime loop, cursor graphics load, cursor movement, command selection, menu load, input-playback helpers, and color-math DMA setup. |
| `EF:EB2A..EF:EB3D` | `src/ef/ef_eb2a_eb3d_debug_color_math_dma_reset.asm` | Color-math/window DMA register reset helper. |

## Preserved Data Islands

| Range | File | Role |
| --- | --- | --- |
| `EF:EB1D..EF:EB2A` | `src/ef/ef_eb1d_eb2a_debug_color_math_window_table.asm` | `DebugColorMathWindowHdmaTable`, the tiny color-math/window table loaded by the `EFEAC8` DMA setup helper. |
| `EF:EB3D..EF:EB5F` | `src/ef/ef_eb3d_eb5f_debug_cursor_tilemap_data.asm` | `DebugCursorTilemapData`, the debug cursor tilemap data immediately before `DEBUG_MENU_FONT`. |

## Runtime Loop And Command Helpers

The `EF:E175..EF:EB1D` runtime cluster now names the main debug mode byte
`$B559`, saved mode camera/entity state at `$B561/$B563/$B565`, cursor sprite
slot `$B553`, command row `$B555`, command input latch `$B557`, overlay tile
mode `$B55F`, and view-character hold flag `$B575`.

The cursor and command-selection helpers now expose the seven visible debug
menu rows as source constants:

- `0`: game / intro scene path
- `1`: view-map / mode-one menu path
- `2`: view character
- `3`: view attribute
- `4`: show battle
- `5`: check position
- `6`: sound mode

The main mode runtime now names the view-character and check-position mode
checks, the overlay-tile-mode cycle, the saved-camera chord, the party-status
debug chord, and the mode-specific branch into `DISPLAY_VIEW_CHARACTER_DEBUG_OVERLAY`
or `DISPLAY_CHECK_POSITION_DEBUG_OVERLAY`.

## Color Math / HDMA Tail

The `EFEAC8` mode-5 setup path now names the PPU window/color-math registers,
DMA channel-4 source fields, HDMA enable shadow, and the `EF:EB1D` window HDMA
table source. The reset helper at `EF:EB2A` now names the matching HDMA-enable
clear and window-left/right reset values before returning to 16-bit
accumulator mode.

The preserved data islands now expose source anchors at `EF:EB1D` and
`EF:EB3D`, keeping the HDMA table and cursor tilemap payload named without
decoding either island as executable code.

## Cross-Bank Meaning

- `EF:E708`, `EF:E746`, and `EF:E759` are callable from C0-era overworld
  paths; they gate debug/view-character state while normal runtime helpers are
  active.
- `EF:E175` is called by the earlier debug sound/menu controller and by command
  selection cases inside this runtime cluster.
- `EF:EB1D..EF:EB2A` and `EF:EB3D..EF:EB5F` intentionally remain data; decoding
  them as instructions produces false `BRK`, `MVP/MVN`, and branch-looking
  bytes.

## Validation Contract

This corridor is source-bank build-candidate material, not hand-authored source
of record yet. It is accepted because the combined EF scaffold preserves byte
equivalence against the original ROM and the source/data cuts match ebsrc
include boundaries.

Current byte-equivalence result after the runtime/cursor/command semantic alias pass:
`EF byte-equivalence: OK, 28 module(s), 0 mismatch(es).`
