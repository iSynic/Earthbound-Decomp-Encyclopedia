# C2 battle sprite render and palette-effect tail

This note covers the remaining unknowns from the battle sprite loader/layout/render corridor and the late palette-effect tail:

- `C2:EEE7`
- `C2:F09F`
- `C2:F0D1`
- `C2:F121`
- `C2:F8F9`
- `C2:F917`
- `C2:FADE`
- `C2:FCA6`
- `C2:FD99`
- `C2:FEF9`
- `C2:FF9A`

The reference include map places this cluster around named routines:

- `battle/load_battle_sprite.asm`
- `battle/get_battle_sprite_width.asm`
- `battle/get_battle_sprite_height.asm`
- `battle/render_battle_sprite_row.asm`

That neighboring code gives strong subsystem context: these helpers load battle enemy sprite assets, cap total sprite width, assign enemy rows/x positions, render both rows, and animate palette effects used by PSI/battle visuals.

## `C2:EEE7` - load the enemy sprites required by the current battle group

Suggested working name: `LoadBattleGroupEnemySprites`

Direct callers:

- `C1:E40B`
- `C2:4922`
- `C2:C2C7`

Observed behavior:

- clears `CURRENT_BATTLE_SPRITEMAPS_ALLOCATED` at `$AAB4`
- clears `CURRENT_BATTLE_SPRITES_ALLOCATED` at `$AAB2`
- loads the current battle group pointer from the battle-group table at `D0:C60D + CURRENT_BATTLE_GROUP * 8`
- iterates enemy entries until the `0xFF` terminator
- uses the enemy config table at `D5:9589` and battle sprite tables around `CE:6514` / `CE:62EE`
- copies `0x20`-byte graphics/map chunks into the staging buffer at `$0300 + CURRENT_BATTLE_SPRITEMAPS_ALLOCATED * 0x20`
- records loaded sprite ids in `$AABE[...]`
- calls the local `LOAD_BATTLE_SPRITE` family helper at `C2:EAEA` to initialize spritemap allocation rows/counts
- after the load pass, copies the staged spritemap/graphics data to VRAM `$2000` or `$3000` depending on whether `$AAB2 >= 0x10`

This is not the single-sprite decompressor itself; it is the current battle group loader that gathers all required enemy battle sprites before layout/rendering.

## `C2:F09F` - find a loaded battle sprite slot by id

Suggested working name: `FindLoadedBattleSpriteSlotById`

Direct callers:

- `C2:C101`
- `C2:C1A0`
- `C2:F15E`

Observed behavior:

- input `A` is a battle sprite id
- scans four entries in the loaded sprite id table at `$AABE`
- returns the matching slot index when found
- returns `0` when no slot matches

The call from `C2:F121` uses the returned slot as the battler's loaded sprite index, which anchors this helper in the enemy sprite layout path.

## `C2:F0D1` - trim the staged enemy sprite list to the width budget

Suggested working name: `TrimLoadedEnemySpriteListToWidthLimit`

Direct caller:

- `C2:4A00`

Observed behavior:

- loops the staged loaded sprite id list at `$9F8C[0..$9F8A)`
- maps each enemy/sprite id through `D5:9589`
- calls `GET_BATTLE_SPRITE_WIDTH`
- accumulates the total width
- if the total would exceed `0x20`, truncates `$9F8A` to the current index

This is a pre-layout guard: it keeps the current encounter's visible enemy sprite set inside the total horizontal battle sprite budget.

## `C2:F121` - assign enemy battle sprite rows and x positions

Suggested working name: `AssignEnemyBattleSpriteRowsAndXPositions`

Direct callers:

- `C1:E465`
- `C2:4A32`

Observed behavior:

- clears row-width accumulators at `$AEF0` and `$AEF2`
- scans enemy battler slots `8..31`
- skips battlers that are absent or not conscious
- resolves each enemy battler's loaded sprite slot through `C2:F09F`
- stores that loaded slot in the battler sprite field around `$9FEF`
- calls `GET_BATTLE_SPRITE_WIDTH`
- accumulates row widths and assigns battler row state around `$9FBC`
- moves enemies to the opposite row when the front row would exceed the `0x1E` practical layout width
- computes x positions around `$9FF0`, using the row total widths to center the group around battle-screen center `0x20`
- uses the local `C2:69EF` / `GetRandomByte` helper for tie/placement
  variation when left/right x-position choices are exactly balanced

The downstream render helpers consume the row and x-position fields this routine writes.

## `C2:F8F9` - render and commit both battle sprite rows

Suggested working name: `RenderAndCommitBattleSpriteRows`

Direct callers:

- `C2:4A36`
- `C2:7BE3`
- `C2:C2D2`
- `C2:C536`
- `C2:C551`
- `C2:C7D8`
- `C2:C7F3`
- `C2:DCD8`

Observed behavior:

- primes C0 palette/DMA setup with `C0:88A5(0x7E)` and `C0:88B1`
- calls the row renderer at `C2:F724` for row `0`
- calls the row renderer at `C2:F724` for row `1`
- commits the prepared transfer through `C0:8B26`

The named neighbor `RENDER_BATTLE_SPRITE_ROW` handles one row at a time. `C2:F8F9` is the wrapper that renders both rows and submits the transfer.

## `C2:F917` - build battle sprite row render order

Suggested working name: `BuildBattleSpriteRowRenderOrder`

Direct callers:

- `C2:44C3`
- `C2:4FD1`

Observed behavior:

- counts live enemy battlers by row into `$AD56` and `$AD58`
- builds row-0 ordered enemy id and offset lists in `$AD7A`, `$AD5A`, and `$AD62`
- builds row-1 ordered enemy id and offset lists in `$AD82`, `$AD6A`, and `$AD72`
- repeatedly selects enemies by increasing x-position field around `$9FF0`
- calls `GET_BATTLE_SPRITE_HEIGHT`
- derives per-row vertical offsets such as `0x12 - height` and `0x10 - height`

This is the ordering/staging step before row rendering, separating the logical battler table from the compact render-order arrays consumed by `RENDER_BATTLE_SPRITE_ROW`.

## `C2:FADE` - reset one enemy sprite color-wave slot

Suggested working name: `ResetEnemySpriteColorWaveSlot`

Direct caller:

- `C2:E8B4`

Observed behavior:

- input `A` is a duration/timer value
- input `X` selects one color-wave group/slot
- stores the duration in `$B37C` and `$AEF4[slot]`
- loops the slot's `0x30` bytes/words of color-wave component state
- negates the delta table around `$AEFC`
- clears the accumulator table around `$B07C`

The only direct caller is in the PSI animation visual update path, so this is part of the enemy sprite palette wave/flash engine.

## `C2:FCA6` - initialize an enemy sprite color-wave entry from palette RGB

Suggested working name: `InitEnemySpriteColorWaveEntryFromPalette`

Direct callers:

- none found by direct-call scan

Observed behavior:

- input `A` selects a palette entry
- stores `$B37C` into the active group timer at `$AEF4[...]`
- reads the source color word from `$0380 + A * 2`
- extracts the RGB555 red, green, and blue components, using the shared
  `C0:9251` / `SignedDivide16By8` helper for the blue/high-component path
- initializes per-component delta/target state in `$AEFC`, `$AEFE`, `$AF00`, `$B1FC`, `$B1FE`, and `$B200`
- clears matching accumulators at `$B07C`, `$B07E`, and `$B080`

This helper appears adjacent to the known `C2:FB35` color-effect setup path and writes the same palette wave tables. `C2:FB35` now uses the same named signed-divide helper for its RGB555 component extraction. No direct `JSL/JSR` caller was found, so it may be reached by local branch/fallthrough or an indirect table path.

## `C2:FD99` - advance enemy sprite color-wave palettes

Suggested working name: `AdvanceEnemySpriteColorWavePalettes`

Direct caller:

- `C2:DDAB`

Observed behavior:

- loops four color-wave groups
- decrements each active `$AEF4[group]` timer
- for active groups, iterates 16 palette entries
- applies per-component deltas through the `$AEFC/$B07C/$B1FC` color-wave tables
- writes updated RGB555 words back into the battle palette buffer around `$0382`
- uploads the changed sprite palette through `C0:856B(0x10)`

The call from the battle visual per-frame updater marks this as the runtime step for the enemy sprite palette wave engine initialized by the nearby helpers.

## `C2:FEF9` - load or dim a battle palette set

Suggested working name: `LoadOrDimBattlePaletteSet`

Direct callers:

- `C2:312E`
- `C2:5BBD`
- `C2:5BC6`
- `C2:5BCF`

Observed behavior:

- if input `A != 0`:
  - treats `A - 1` as a palette-set index
  - copies four `0x20`-byte palette rows from `C3:F8F1 + index * 0x20`
  - writes them to `$0380`, `$03A0`, `$03C0`, and `$03E0`
  - uploads with `C0:856B(0x10)`
- if input `A == 0`:
  - reads palette words from the `$0200` palette buffer range
  - writes a dimmed/transformed copy into `$0280`
  - uses `LSR`, `LSR`, and `AND #$1CE7` to preserve legal RGB555 channel bits after darkening
  - uploads with `C0:856B(0x10)`

The `C2:5BBD` callers use modes `1`, `2`, and `3` inside a battle action/effect path. The `C2:312E` caller uses mode `0`, matching the dim-copy branch used by menu/equipment-style rendering.

## `C2:FF9A` - check an overworld position hash threshold

Suggested working name: `CheckOverworldPositionHashThreshold3Of8`

Direct callers:

- none found by direct-call scan

Observed behavior:

- loads position/state words from `$9877` and `$987B`
- calls the C0 math/hash helper at `C0:0AA1`
- masks the result with `0x0007`
- returns true when the masked value is `>= 3`
- returns false otherwise

With no direct callers, this may be pointer-called, dead, or reached only by a reference path not covered by the direct-call scan. The position inputs suggest an overworld coordinate/random threshold helper rather than a battle sprite routine, despite its placement at the end of the bank.

## Working Names

- `C2:EEE7` = `LoadBattleGroupEnemySprites`
- `C2:F09F` = `FindLoadedBattleSpriteSlotById`
- `C2:F0D1` = `TrimLoadedEnemySpriteListToWidthLimit`
- `C2:F121` = `AssignEnemyBattleSpriteRowsAndXPositions`
- `C2:F8F9` = `RenderAndCommitBattleSpriteRows`
- `C2:F917` = `BuildBattleSpriteRowRenderOrder`
- `C2:FADE` = `ResetEnemySpriteColorWaveSlot`
- `C2:FCA6` = `InitEnemySpriteColorWaveEntryFromPalette`
- `C2:FD99` = `AdvanceEnemySpriteColorWavePalettes`
- `C2:FEF9` = `LoadOrDimBattlePaletteSet`
- `C2:FF9A` = `CheckOverworldPositionHashThreshold3Of8`

## Source Scaffold Promotion

Most of the battle-sprite layout and palette-wave tail is now represented as durable source modules:

- `src/c2/c2_f09f_find_loaded_battle_sprite_slot_by_id.asm` covers `C2:F09F..F0D1`.
- `src/c2/c2_f0d1_trim_loaded_enemy_sprite_list_to_width_limit.asm` covers `C2:F0D1..F121`.
- `src/c2/c2_f121_assign_enemy_battle_sprite_rows_and_xpositions.asm` covers `C2:F121..F8F9`.
- `src/c2/c2_f8f9_render_and_commit_battle_sprite_rows.asm` covers `C2:F8F9..F917`.
- `src/c2/c2_f917_build_battle_sprite_row_render_order.asm` covers `C2:F917..FADE`.
- `src/c2/c2_fade_reset_enemy_sprite_color_wave_slot.asm` covers `C2:FADE..FB35`, with `C2:FB35..FCA6` preserved as `EnemySpriteColorWaveComparisonHelper`.
- `src/c2/c2_fca6_init_enemy_sprite_color_wave_entry_from_palette.asm` covers `C2:FCA6..FD99`.
- `src/c2/c2_fd99_advance_enemy_sprite_color_wave_palettes.asm` covers `C2:FD99..FEF9`.
- `src/c2/c2_fef9_load_or_dim_battle_palette_set.asm` covers `C2:FEF9..FF9A`.

Validation after promotion:

- `C2 byte-equivalence: OK, 217 module(s), 0 mismatch(es).`
