# C2 battle-background load and palette-effect corridor

This note covers the dense unknown corridor between `GENERATE_BATTLEBG_FRAME`, `LOAD_BATTLE_BG`, and `SHOW_PSI_ANIMATION`:

- `C2:CFE5`
- `C2:D0AC`
- `C2:DAE3`
- `C2:DE0F`
- `C2:DE96`
- `C2:DF2E`
- `C2:E08E`
- `C2:E0E7`

The reference include map places these unknowns around:

- `misc/battlebgs/generate_frame.asm`
- `battle/load_battlebg.asm`
- `battle/show_psi_animation.asm`

The named reference sources make the subsystem boundary clear: this region initializes `loaded_bg_data`, updates letterbox/HDMA state, maintains battle-background palettes, and resets battle visual-effect state.

## Working Names

- `C2:CFE5` = `InitLoadedBattleBgLayerFromConfig`
- `C2:D0AC` = `BuildBattleLetterboxHdmaTable`
- `C2:DAE3` = `PrimeLayer1BattleBgDistortionSwap`
- `C2:DE0F` = `DimLoadedBattleBgPalettesAndUpload`
- `C2:DE96` = `RestoreLoadedBattleBgPalettesAndUpload`
- `C2:DF2E` = `ApplyLoadedBattleBgPaletteStep`
- `C2:E08E` = `ApplyLoadedBattleBgPaletteStepAcrossLayers`
- `C2:E0E7` = `ClearBattleVisualFlashStateAndLayerConfig`

## Shared state map

The relevant WRAM block starts at `CURRENT_LAYER_CONFIG` and continues through the two `loaded_bg_data` structs:

- `$AD8A` = `CURRENT_LAYER_CONFIG`
- `$AD8C` = `VERTICAL_SHAKE_DURATION`
- `$AD8E` = `VERTICAL_SHAKE_HOLD_DURATION`
- `$AD90` = `SCREEN_EFFECT_MINIMUM_WAIT_FRAMES`
- `$AD92` = `WOBBLE_DURATION`
- `$AD94` = `SHAKE_DURATION`
- `$AD96` = `SCREEN_EFFECT_HORIZONTAL_OFFSET`
- `$AD98` = `SCREEN_EFFECT_VERTICAL_OFFSET`
- `$AD9A` = `PSI_ANIMATION_X_OFFSET`
- `$AD9C` = `PSI_ANIMATION_Y_OFFSET`
- `$AD9E` = `GREEN_FLASH_DURATION`
- `$ADA0` = `RED_FLASH_DURATION`
- `$ADA4` = `HP_PP_BOX_BLINK_DURATION`
- `$ADA6` = `HP_PP_BOX_BLINK_TARGET`
- `$ADAE` = `LETTERBOX_VISIBLE_SCREEN_VALUE`
- `$ADB0` = `LETTERBOX_NONVISIBLE_SCREEN_VALUE`
- `$ADB2` = `LETTERBOX_TOP_END`
- `$ADB4` = `LETTERBOX_BOTTOM_START`
- `$ADB8` = `LETTERBOX_HDMA_TABLE`
- `$ADD0` = `ENABLE_BACKGROUND_DARKENING`
- `$ADD2` = `BACKGROUND_BRIGHTNESS`
- `$ADD4` = `LOADED_BG_DATA_LAYER1`
- `$AE4B` = `LOADED_BG_DATA_LAYER2`

The `loaded_bg_data` struct comes from `refs/ebsrc-main/ebsrc-main/include/structs.asm`. Important offsets used by this corridor:

- `+0x00` target layer
- `+0x01` bitdepth
- `+0x02` freeze palette scrolling
- `+0x03..0x0B` palette animation fields
- `+0x0C..0x2B` current palette
- `+0x2C..0x4B` backup/original palette
- `+0x4C` displayed palette pointer
- `+0x4E..0x52` scrolling movement fields
- `+0x55..0x60` scroll position/velocity/acceleration
- `+0x61..0x76` distortion fields

## `C2:CFE5` - initialize loaded background layer metadata

Suggested working name: `InitLoadedBattleBgLayerFromConfig`

Direct callers:

- `C2:D3A5`
- `C2:D5FA`
- `C2:D6FF`
- `C2:D7D2`
- `C2:D9D2`
- `C4:A4BA`

`LOAD_BATTLE_BG` calls this helper after selecting a `BG_DATA_TABLE` entry and choosing either `LOADED_BG_DATA_LAYER1` or `LOADED_BG_DATA_LAYER2`.

Observed behavior:

- input `A` is the destination `loaded_bg_data` low word
- source pointer is the selected `bg_layer_config_entry`
- copies config bytes into the destination struct:
  - bitdepth -> `loaded_bg_data::bitdepth`
  - palette-shift style and cycle boundaries -> palette animation fields
  - palette-change speed -> `palette_change_speed`
  - four scrolling movement ids -> `scrolling_movements`
  - four distortion style ids -> `distortion_styles`
- initializes duration/phase fields to `1`:
  - `palette_change_duration_left`
  - `scrolling_duration_left`
  - `distortion_duration_left`

This is not a frame generator itself. It is the config-to-runtime-state bridge used by the battle background loader.

## `C2:D0AC` - build the letterbox HDMA table

Suggested working name: `BuildBattleLetterboxHdmaTable`

Direct callers:

- `C2:DACD`
- `C2:DE09`

`LOAD_BATTLE_BG` calls this near the end of background setup, after choosing `LETTERBOX_VISIBLE_SCREEN_VALUE`, `LETTERBOX_NONVISIBLE_SCREEN_VALUE`, `LETTERBOX_TOP_END`, and `LETTERBOX_BOTTOM_START`.

The routine writes the table at `$ADB8` (`LETTERBOX_HDMA_TABLE`):

- first segment: `LETTERBOX_TOP_END` lines using `LETTERBOX_NONVISIBLE_SCREEN_VALUE`
- middle segment(s): enough chunks of up to `0x7F` lines using `LETTERBOX_VISIBLE_SCREEN_VALUE`
- final segment: one line using `LETTERBOX_NONVISIBLE_SCREEN_VALUE`
- terminator byte: `0`

The repeated `0x7F` chunks exist because SNES HDMA line counts are byte-sized. This routine is therefore the table builder for the battle letterbox window, not a generic copy helper.

## `C2:DAE3` - layer-1 distortion kick/swap helper

Suggested working name: `PrimeLayer1BattleBgDistortionSwap`

Direct caller:

- `C2:C84F`

This small helper touches only a few bytes inside `LOADED_BG_DATA_LAYER1`'s distortion block:

- reads `LOADED_BG_DATA_LAYER1 + loaded_bg_data::distortion_styles[0]` at `$AE35`
- swaps it with the byte at `$AE38`, the fourth distortion-style byte
- clears `$AE36`, the second distortion-style byte
- sets `$AE3A` to `1`, which is `loaded_bg_data::distortion_duration_left`

The caller at `C2:C84F` sits in the high-impact visual sequence around prayer/Giygas-style battle presentation code, immediately before a C0 screen transition. The exact visual reason for swapping endpoints remains less certain than the byte-level behavior, but the writes are clearly confined to layer-1 battle-background distortion state.

## `C2:DE0F` - dim loaded battle-background palettes and upload

Suggested working name: `DimLoadedBattleBgPalettesAndUpload`

Direct callers:

- `C2:E49E`, inside `SHOW_PSI_ANIMATION`
- `C3:F9A2`
- `C3:FA4A`

`SHOW_PSI_ANIMATION` calls this after decompressing PSI frame data and before target/enemy palette setup. C3 also calls it while applying special visual screen effects.

Observed behavior:

- iterates 16 palette words for layer 1
- iterates the same 16-word palette range for layer 2
- transforms each color word with `LSR` and `AND #$3DEF`, which halves the RGB555 channels while preserving the valid channel bit layout
- copies layer 1's current palette to its displayed palette pointer
- if layer 2 is active, copies layer 2's current palette to its displayed palette pointer

This is a palette-darkening pass for loaded battle backgrounds, followed by immediate upload/copy through the C0 memory helper.

## `C2:DE96` - restore/copy loaded battle-background palettes and upload

Suggested working name: `RestoreLoadedBattleBgPalettesAndUpload`

Direct callers:

- `C2:E77E`
- `C4:AC3F`

This helper performs the inverse maintenance path for background palettes:

- copies layer 1 `palette2` into layer 1 `palette`
- copies layer 2 `palette2` into layer 2 `palette`
- copies layer 1 `palette` to its displayed palette pointer
- if layer 2 is active, copies layer 2 `palette` to its displayed palette pointer

The C4 caller uses it after palette/control writes and then restores `CURRENT_LAYER_CONFIG`, which matches a "restore background palettes after an overlay/effect" role.

## `C2:DF2E` - apply one palette-step command to one loaded-background palette slot

Suggested working name: `ApplyLoadedBattleBgPaletteStep`

Direct callers:

- `C2:E0B3`
- `C2:E0CF`
- `C2:E0D9`

`C2:DF2E` is local to `C2:E08E`. Inputs:

- `A` = base of a `loaded_bg_data` struct (`$ADD4` or `$AE4B`)
- `X` = palette command/step
- `Y` = palette index

Special command values:

- `X = 0` or `X = -1`: directly writes that word into the current palette slot and the displayed palette slot
- `X = 0x0100`: restores the slot from `loaded_bg_data::palette2`
- other values: derives a stepped RGB555 color from the current palette entry using C0 color math helpers, writes it back to `loaded_bg_data::palette`, and mirrors it to the displayed palette unless the palette index is inside a protected cycle window

The protected-window tests read `palette_shifting_style` and the two configured palette-cycle ranges. This keeps automatic color stepping from trampling active palette-cycle bands.

## `C2:E08E` - apply a palette-step command across active battle-background slots

Suggested working name: `ApplyLoadedBattleBgPaletteStepAcrossLayers`

Direct callers:

- `C2:DB89`
- `C2:DBA0`
- `C2:DBA8`
- `C2:DBDE`
- `C2:DBE6`

This helper is called only from the existing per-frame battle-background update routine at `C2:DB3F`.

It takes a palette command/step in `A` and forwards it to `C2:DF2E`:

- if layer 1 bitdepth is 4bpp, applies to layer 1 palette indices `1..15`
- otherwise applies to palette indices `1..3` for both layer 1 and layer 2

The callers pass values such as `0x0100`, `0`, and `-1` while handling background brightness/flash timers. This makes `C2:E08E` the fan-out wrapper for global battle-background palette stepping.

## `C2:E0E7` - clear battle visual flash state and restore base layer config

Suggested working name: `ClearBattleVisualFlashStateAndLayerConfig`

Direct callers:

- `C2:4905`, during battle setup
- `C2:6181`, at the end of the instant-win path

Observed behavior:

- clears `GREEN_FLASH_DURATION`
- clears `RED_FLASH_DURATION`
- clears `$AEC2`, a nearby battle visual/sprite-effect byte outside the named `loaded_bg_data` structs
- if `HP_PP_BOX_BLINK_DURATION` is nonzero:
  - calls `C2:07B6` / `MarkAndRedrawPartyHpPpWindow` with `HP_PP_BOX_BLINK_TARGET`
  - clears `HP_PP_BOX_BLINK_DURATION`
- calls C0 layer/palette helpers with zeroed arguments
- sets `CURRENT_LAYER_CONFIG` to `1`

Because this runs both at battle setup and after instant-win cleanup, it is best understood as a battle visual-state reset helper rather than as part of one specific animation.

## Source Scaffold Promotion

The following battle-background helpers are now represented as durable source modules:

- `src/c2/c2_cfe5_init_loaded_battle_bg_layer_from_config.asm` covers `C2:CFE5..D0AC`.
- `src/c2/c2_d0ac_build_battle_letterbox_hdma_table.asm` covers `C2:D0AC..D121`.
- `src/c2/c2_d121_load_battle_background_main_body.asm` covers `C2:D121..DAE3`.
- `src/c2/c2_dae3_prime_layer1_battle_bg_distortion_swap.asm` covers `C2:DAE3..DB14`.
- `src/c2/c2_db14_run_battle_bg_per_frame_update_body.asm` covers `C2:DB14..DE0F`.
- `src/c2/c2_de0f_dim_loaded_battle_bg_palettes_and_upload.asm` covers `C2:DE0F..DE96`.
- `src/c2/c2_de96_restore_loaded_battle_bg_palettes_and_upload.asm` covers `C2:DE96..DF2E`.
- `src/c2/c2_df2e_apply_loaded_battle_bg_palette_step.asm` covers `C2:DF2E..E08E`.
- `src/c2/c2_e08e_apply_loaded_battle_bg_palette_step_across_layers.asm` covers `C2:E08E..E0E7`.
- `src/c2/c2_e0e7_clear_battle_visual_flash_state_and_layer_config.asm` covers `C2:E0E7..E116`.
- `src/c2/c2_e116_run_battle_visual_flash_and_bg_effect_body.asm` covers `C2:E116..E6B3`.

Follow-up source polish names the per-frame HP/PP blink joins in
`C2:DB3F..DE0F` as the same `$ADA4/$ADA6`
`HP_PP_BOX_BLINK_DURATION/TARGET` pair documented above. The source now calls
`C2:07E1` as `ClearPartyHpPpWindowTiles` during the blink-off phase and
`C2:07B6` as `MarkAndRedrawPartyHpPpWindow` during the blink-on/cleanup phase.

Validation after promotion:

- `C2 byte-equivalence: OK, 233 module(s), 0 mismatch(es).`
