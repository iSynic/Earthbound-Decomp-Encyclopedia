# C2 Battle Background Load And Update Runtime Polish

This note records the byte-neutral C2 battle-background loader/update polish
slice. It promotes the runtime joins that convert battle-background table rows
into loaded layer structs, VRAM/palette setup, frame updates, and letterbox
state.

Primary source modules:

- `src/c2/c2_cfe5_init_loaded_battle_bg_layer_from_config.asm`
- `src/c2/c2_d0ac_build_battle_letterbox_hdma_table.asm`
- `src/c2/c2_d121_load_battle_background_main_body.asm`
- `src/c2/c2_dae3_prime_layer1_battle_bg_distortion_swap.asm`
- `src/c2/c2_db14_run_battle_bg_per_frame_update_body.asm`

Related evidence notes:

- `notes/battle-background-scene-bundles.md`
- `notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`
- `notes/c2-battle-bg-palette-runtime-polish.md`
- `notes/battle-visual-asset-contracts.md`

## Config To Runtime Struct

`C2:CFE5` is the loader's table-row bridge. It receives a destination
`loaded_bg_data` base in A and reads the current `BG_DATA_TABLE` row pointer
from direct-page `$26/$28`.

It clears the 0x77-byte destination struct, then imports:

- config byte `2` -> bitdepth
- config bytes `3..7` -> palette-shift style and cycle ranges
- config byte `8` -> palette-change speed
- config bytes `9..12` -> four scrolling movement row ids
- config bytes `13..16` -> four distortion style row ids

It also seeds the palette, scrolling, and distortion duration counters to `1`.
That makes newly loaded background layers immediately eligible for the
per-frame visual update body.

## Main Loader

`LOAD_BATTLE_BG` receives layer 1 in A, optional layer 2 in X, and letterbox or
layout flags in Y.

The stable table joins are:

- `BG_DATA_TABLE` row byte `0` selects both graphics and arrangement pointers
- row byte `1` selects the palette pointer
- row bytes `2..16` feed `C2:CFE5` and become `loaded_bg_data` runtime fields

The loader builds layer 1 at `$ADD4` and layer 2 at `$AE4B` when enabled. It
handles the standard and four-layer VRAM layouts, copies the selected palette
into both current and saved/original palette blocks, sets each layer's
displayed-palette pointer, queues loaded-bg visual state, then finalizes by
building the battle letterbox HDMA table and clearing stale overlay state.

`C2:D0AC` is the letterbox HDMA builder. It writes the table at `$ADB8` from
visible and nonvisible screen values in `$ADAE/$ADB0` plus top/bottom bounds in
`$ADB2/$ADB4`. Visible spans are chunked at `0x7F` scanlines because HDMA line
counts are byte-sized.

`C2:DAE3` is a small layer-1 distortion primer. It swaps the first and fourth
distortion style bytes, clears the second style byte, and sets distortion
duration left to `1`.

## Per-Frame Update

`C2:DB3F` is the battle-background frame lane. Its responsibilities are now
documented as one shared visual update body:

- convert background darkening and flash timers into `C2:E08E` palette commands
- update vertical shake, horizontal wobble, and short shake offsets
- commit offsets to the active BG register pair based on layer bitdepth
- advance layer 1 and optional layer 2 loaded-bg script state through `C2:C92D`
- tick PSI animation state through `C2:E6B6`
- run screen brightness flashes, HP/PP box blink, and overlay script stepping
- animate letterbox bounds and rebuild the HDMA table when requested

The HP/PP box blink sublane now has source-facing names for its shared window
joins: `$ADA4/$ADA6` are the HP/PP box blink duration/target pair, and the
per-frame update alternates the target through `C2:07E1`
`ClearPartyHpPpWindowTiles` and `C2:07B6`
`MarkAndRedrawPartyHpPpWindow`.

This routine is the frame-time consumer of the runtime structs initialized by
`LOAD_BATTLE_BG`; it is not merely a palette updater.

## Decomp Value

This slice connects the asset-facing battle-background contract to runtime:

- table bytes in `BG_DATA_TABLE` now have documented loader consumers
- loaded layer structs at `$ADD4/$AE4B` are tied to both loader and updater
- letterbox state has a specific HDMA table builder and transition path
- per-frame palette commands are placed in their broader visual update context

## Remaining Soft Spots

- exact labels for the standard versus four-layer layout mode values
- final user-facing names for each shake/wobble/flash timer field
- deeper naming of the `C2:C92D` loaded-bg script interpreter internals
