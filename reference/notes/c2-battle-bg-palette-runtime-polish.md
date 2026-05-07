# C2 Battle Background Palette Runtime Polish

This note records the byte-neutral C2 battle-background palette polish slice.
It promotes the dim, restore, single-slot step, and cross-layer fanout helpers
that sit between `LOAD_BATTLE_BG`, the per-frame battle-background updater, and
`SHOW_PSI_ANIMATION`.

Primary source modules:

- `src/c2/c2_de0f_dim_loaded_battle_bg_palettes_and_upload.asm`
- `src/c2/c2_de96_restore_loaded_battle_bg_palettes_and_upload.asm`
- `src/c2/c2_df2e_apply_loaded_battle_bg_palette_step.asm`
- `src/c2/c2_e08e_apply_loaded_battle_bg_palette_step_across_layers.asm`

Related evidence notes:

- `notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`
- `notes/c2-psi-animation-runtime-polish.md`
- `notes/battle-background-scene-bundles.md`
- `notes/battle-visual-asset-contracts.md`

## Loaded Palette State

The promoted helpers operate on the two loaded battle-background layer structs:

- `$ADD4` = layer 1 loaded background struct
- `$AE4B` = layer 2 loaded background struct
- struct `+0x01` = bitdepth
- struct `+0x03..0x07` = palette-shift style and protected cycle ranges
- struct `+0x0C..0x2B` = current palette
- struct `+0x2C..0x4B` = saved/original palette
- struct `+0x4C` = displayed-palette pointer

`C2:DE0F` dims both current palettes in place. For each of 16 RGB555 words, it
applies `LSR` and `AND #$3DEF`, which halves the channel intensity while keeping
the channel bit layout valid. It then mirrors layer 1 through pointer `$AE20`
and mirrors layer 2 through pointer `$AE97` when the layer-2 struct is active.

`C2:DE96` restores both current palettes from their saved/original copies:

- layer 1 `$AE00..AE1F` -> `$ADE0..ADFF` -> displayed pointer `$AE20`
- layer 2 `$AE77..AE96` -> `$AE57..AE76` -> displayed pointer `$AE97`

The layer-2 displayed copy is conditional on `$AE4B` being active.

## Palette Step Commands

`C2:DF2E` applies one command to one palette index in one loaded layer struct:

- A = loaded background struct base (`$ADD4` or `$AE4B`)
- X = palette command/step
- Y = palette index

Command behavior:

- `X = 0` or `X = -1`: write the literal word to current and displayed slots
- `X = 0x0100`: restore the slot from saved/original palette offset `+0x2C`
- other: derive a stepped RGB555 value from the saved/original slot, write the
  current slot, then mirror it to display unless a protected cycle range covers
  the palette index

The protected-window checks use the palette-shift style byte at struct `+0x03`
and the two cycle ranges at `+0x04..0x07`. This keeps broad brightness or flash
steps from overwriting active palette-cycle bands.

## Fanout

`C2:E08E` is the per-frame updater's command fanout wrapper. It receives a
palette command/step in A and forwards it to `C2:DF2E`:

- if layer 1 bitdepth is `4`, it updates layer 1 palette indices `1..15`
- otherwise it updates indices `1..3` on both layer 1 and layer 2

Its direct callers are inside the existing battle-background per-frame update
body and pass values such as `0x0100`, `0`, and `-1` while managing background
brightness and flash timers.

## Decomp Value

This slice gives the visual runtime lane durable names for the palette state
that CoilSnake and asset contracts expose as battle-background editor data:

- current palette versus saved/original palette now has a stable WRAM join
- displayed-palette pointers are separated from the struct-local palette copy
- literal, restore, and stepped palette commands are documented at the byte
  path that actually mutates runtime color state
- palette-cycle protected ranges are now tied to the command mirror decision

## Remaining Soft Spots

- exact user-facing names for each per-frame caller's brightness/flash mode
- final symbol promotion for the loaded-bg struct fields
- C0 palette helper semantics below `C08ED2` and the later display upload path
