# C2 Battle Sprite Runtime Polish

This note records the byte-neutral C2 battle sprite polish slice. It promotes
the current battle-group sprite loader, enemy row layout, render-order builder,
row renderer wrapper, and enemy sprite palette wave helpers.

Primary source modules:

- `src/c2/c2_eee7_load_battle_group_enemy_sprites.asm`
- `src/c2/c2_f09f_find_loaded_battle_sprite_slot_by_id.asm`
- `src/c2/c2_f0d1_trim_loaded_enemy_sprite_list_to_width_limit.asm`
- `src/c2/c2_f121_assign_enemy_battle_sprite_rows_and_xpositions.asm`
- `src/c2/c2_f8f9_render_and_commit_battle_sprite_rows.asm`
- `src/c2/c2_f917_build_battle_sprite_row_render_order.asm`
- `src/c2/c2_fade_reset_enemy_sprite_color_wave_slot.asm`
- `src/c2/c2_fca6_init_enemy_sprite_color_wave_entry_from_palette.asm`
- `src/c2/c2_fd99_advance_enemy_sprite_color_wave_palettes.asm`
- `src/c2/c2_fef9_load_or_dim_battle_palette_set.asm`

Related evidence notes:

- `notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`
- `notes/battle-sprite-bundle-contracts.md`
- `notes/battle-visual-asset-contracts.md`
- `notes/c2-battle-bg-load-update-runtime-polish.md`
- `notes/c2-psi-animation-runtime-polish.md`

## Load And Layout

`C2:EEE7` loads battle sprite assets for the current battle group. It resolves
`CURRENT_BATTLE_GROUP` at `$4A8C` through the D0 battle-group table, walks the
enemy list, maps each enemy through the D5 enemy configuration table, copies the
selected CE battle sprite palette row into the `$0300` staging buffer, records
loaded sprite ids at `$AABE`, and calls the local `LOAD_BATTLE_SPRITE` family
helper to allocate graphics and spritemap rows.

After the group pass, the staged graphics/map block is transferred to VRAM
`$2000` or `$3000` depending on loaded sprite allocation count `$AAB2`.

`C2:F09F` resolves a battle sprite id to one of the four loaded slots in
`$AABE`. `C2:F121` now calls it by name when writing each active enemy row's
loaded sprite slot at `+0x43`.

`C2:F0D1` trims the staged enemy sprite list `$9F8C[0..$9F8A)` if the
accumulated sprite widths would exceed `0x20`. It now calls `C2:EFFD` /
`GetBattleSpriteWidthBucket` by name while accumulating the row-width budget.

`C2:EFFD` is the shared `GetBattleSpriteWidthBucket` helper. Call-for-help
width budgeting, bomb splash overlap checks, staged enemy-list trimming, and
enemy row/x-position assignment now call it by name at their C2 sites.

`C2:F121` assigns active enemy battlers to rows and x/y render positions:

- row-width accumulators live at `$AEF0/$AEF2`
- loaded sprite slot is stored in battler row `+0x43`
- x/y render positions are stored at row `+0x44/+0x45`
- row flag is stored at row `+0x1F`
- staged enemy rows are sorted before render-order construction

## Render Order

`C2:F917` builds compact render-order arrays for the two enemy sprite rows. It
counts row-0 and row-1 live enemies into `$AD56/$AD58`, selects each next enemy
by increasing x coordinate, and writes:

- row 0: `$AD7A` order, `$AD5A` x tile offset, `$AD62` vertical adjustment
- row 1: `$AD82` order, `$AD6A` x tile offset, `$AD72` vertical adjustment

`C2:F8F9` is the wrapper that renders both rows: it selects WRAM bank `$7E`,
resets renderer state, calls the local row renderer for row `0` and row `1`,
then flushes queued sprite/tile work through C0.

## Palette Wave

The late color-wave helpers operate on four enemy sprite palette groups:

- `$AEF4[group]` = active timer
- `$AEFC/$AEFE/$AF00` = per-component deltas
- `$B07C/$B07E/$B080` = per-component accumulators
- `$B1FC/$B1FE/$B200` = component targets/limits
- `$0380..$03FF` = active battle sprite palette buffer

`C2:FADE` resets one group by storing the duration in `$B37C` and
`$AEF4[group]`, negating the group's component deltas, and clearing matching
accumulators.

`C2:FCA6` initializes one palette entry's wave state from its RGB555 source word
in `$0380`. The high bits of the palette entry select the group timer slot.

`C2:FB35` now names the same `C0:9251` / `SignedDivide16By8` helper used by
`C2:FCA6` while extracting RGB555 components for color-wave comparison/setup.

`C2:FD99` is the per-frame advancer. It decrements active timers, applies
component deltas to palette entries `1..15`, writes updated RGB555 words back
around `$0382`, and commits palette changes with `C0:856B(0x10)`.

`C2:FEF9` either loads one C3 battle palette row into all four sprite palette
slots or builds a dimmed copy from `$0200` into `$0280`. The battle-start
action-presentation controller now calls it by name for its pre-action palette
category branches.

## Decomp Value

This slice connects the CD/CE battle sprite asset contract to runtime:

- enemy configuration sprite/palette fields now have loader consumers
- loaded sprite slot table `$AABE` has a documented lookup and layout use
- row layout and render-order arrays are tied to battler row fields
- width-budget trimming and row/x-position assignment now share the same named
  width-bucket helper used by call-for-help and bomb splash action paths
- palette wave state has clear timer, delta, accumulator, and commit roles
- the battle-background frame lane's call to `C2:FD99` now has a concrete
  enemy sprite palette-wave meaning

## Remaining Soft Spots

- final symbolic names for the local `LOAD_BATTLE_SPRITE` helper family
- detailed field names for row `+0x48/+0x49` transient draw timers
- Evil Eye's documented sprite-id-110 outlier remains a data-contract followup
