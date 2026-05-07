# Bank D0 First Pass

## Main result

Bank `D0` is another generated map/battle-data bank with an audio tail. It
follows the same broad pattern as `CF`: the bank config names many generated
data includes, but most of those generated source files are absent from the
checked-in ref tree, so the safe bank-level boundary is the full pre-audio data
region rather than precise per-table splits. The follow-up D0 splitter now
resolves the full pre-audio generated region into exact source-order spans.

Follow-up source-scaffold status:

- durable scaffold: `src/d0/bank_d0_helpers_asar.asm`
- manifest: `build/d0-build-candidate-ranges.json`
- handoff: `notes/bank-d0-source-scaffold-handoff.md`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `11`
- byte-equivalence: `OK`, `0` mismatches

Primary artifacts:

- `notes/bank-d0-asset-data-map.md`
- `notes/d0-table-splits.md`
- `notes/d0-variable-list-contracts.md`
- `build/asset-bank-d0.json`
- `build/d0-table-splits.json`

The generated map accounts for:

- binary assets: `1`
- binary asset bytes: `8180`
- table/generator region bytes: `57268`
- exact generated-data split bytes: `57268`
- coverage gap bytes: `88`
- missing payload metadata: `0`

## Bank layout

The high-level D0 layout is:

- `D0:0000..D0:DFB3`: generated map/battle-data region, `57268` bytes.
- `D0:DFB4..D0:FFA7`: `AUDIO_PACK_139`, `8180` bytes.
- `D0:FFA8..D0:FFFF`: `88` bytes of tail slack.

The checked-in bank config names this generated-data sequence:

- `data/map/door_pointer_table.asm`
- `data/screen_transition_config_table.asm`
- `data/event_control_ptr_table.asm`
- `data/map/tile_event_control_table.asm`
- `data/map/enemy_placement.asm`
- `data/map/enemy_placement_groups_pointer_table.asm`
- `data/map/enemy_placement_groups.asm`
- `data/map/battle_entry_pointer_table.asm`
- `data/map/battle_groups_table.asm`

`data/event_control_ptr_table.asm` exists in the ref tree and defines a 20-entry
`.WORD` table, but source order places it inside the broader generated block
whose earlier generated files are absent. The dedicated splitter recovers the
source-order boundaries with pointer-table validation, eb-decompile row counts,
and local ROM checks.

The exact split is:

- `D0:0000..D0:13FF`: `DOOR_POINTER_TABLE`, 1280 long pointers into CF.
- `D0:1400..D0:1597`: `SCREEN_TRANSITION_CONFIG_TABLE`, 34 fixed `0x0C`-byte rows.
- `D0:1598..D0:15BF`: `EVENT_CONTROL_PTR_TABLE`, 20 word pointers.
- `D0:15C0..D0:187F`: `MAP_TILE_EVENT_CONTROL_TABLE`, 20 variable chains.
- `D0:1880..D0:B87F`: `MAP_ENEMY_PLACEMENT`, 20480 word entries.
- `D0:B880..D0:BBAB`: `ENEMY_PLACEMENT_GROUPS_PTR_TABLE`, 203 long pointers.
- `D0:BBAC..D0:C60C`: `ENEMY_PLACEMENT_GROUPS_TABLE`, 203 variable lists.
- `D0:C60D..D0:D52C`: `BTL_ENTRY_PTR_TABLE`, 484 fixed `0x08`-byte rows.
- `D0:D52D..D0:DFB3`: `ENEMY_BATTLE_GROUPS_TABLE`, variable battle groups.

`notes/d0-variable-list-contracts.md` now surfaces the source-emission details
for the enemy/battle variable lists: all 203 enemy-placement pointer rows own
one placement list each, 76 placement lists carry a nonzero event-flag gate, and
28 carry a nonzero flagged-spawn chance. All 484 `BTL_ENTRY_PTR_TABLE` rows
target bank `D0`, have zero pointer-padding bytes, and resolve to unique parsed
battle-group slices. The battle-group span has 2668 pointer-owned bytes plus one
27-byte unpointed gap at `D0:D531..D0:D54C`, which source emission should
preserve separately instead of assigning to a battle-entry row.

## Runtime corroboration

The battle runtime references `BTL_ENTRY_PTR_TABLE` using the
`battle_entry_ptr_entry` structure in:

- `refs/ebsrc-main/ebsrc-main/src/battle/main_battle_routine.asm`
- `refs/ebsrc-main/ebsrc-main/src/battle/enemy_select_mode.asm`

That corroborates the presence of battle-entry pointer data in this bank family,
but not the exact internal byte split inside the absent generated source region.

## Tooling behavior

`tools/build_asset_bank_manifest.py` now supports CPU bank labels beyond `C*`
by mapping `D0` to reference bank `10`, `D1` to `11`, and so on. It also avoids
assigning existing include files on top of known binary assets when a previous
missing generated include has already consumed the source-order span up to the
next binary payload.

## Current D0 confidence boundary

High confidence:

- D0 is data/audio, not executable code.
- The generated map/battle-data block runs from `D0:0000` through `D0:DFB3`.
- The internal generated-data spans are exact in `notes/d0-table-splits.md`.
- `ENEMY_PLACEMENT_GROUPS_TABLE` list headers and weighted entries are
  consumer-backed by `C0:2668` and summarized in
  `notes/d0-variable-list-contracts.md`.
- `ENEMY_BATTLE_GROUPS_TABLE` repeat-count enemy entries are consumer-backed by
  C2 battle setup/sprite/help-selection paths and summarized in
  `notes/d0-variable-list-contracts.md`.
- `BTL_ENTRY_PTR_TABLE` row ownership and the unpointed battle-group gap are
  now summarized for source-emission planning.
- `MAP_TILE_EVENT_CONTROL_TABLE` chains now have decoded event-condition
  headers and replacement pairs in `notes/d0-tile-event-contracts.md`.
- The audio tail contains US retail `AUDIO_PACK_139`.
- Only `D0:FFA8..D0:FFFF` remains unclaimed tail slack.

Still intentionally out of scope:

- Human-facing names for individual tile-event chains, event flags, and
  replacement pairs remain open.
- Human-facing names for individual enemy placement groups and battle-group
  pointer slices remain open.
- Audio-pack internals remain opaque.

## Recommended next move

Treat D0 as structurally complete and byte-protected for the current
bank-coverage phase. For D0 itself, the next source step is typed emission for
the tile-event and placement/battle variable-list rows rather than boundary
archaeology.
