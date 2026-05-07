# Bank D5 First Pass

## Main result

Bank `D5` is a mixed asset/data bank. The front of the bank closes the
overworld sprite graphics run that started in `D1`; the middle has an explicit
empty pad; the remainder is gameplay/battle/map table data. The first pass
originally stopped at the missing generated-source boundary, but the follow-up
D5 splitter now reconciles the complete `D5:5000..D5:FFFF` table region.

Primary artifacts:

- `notes/bank-d5-asset-data-map.md`
- `notes/d5-table-splits.md`
- `notes/d5-timed-delivery-row-contracts.md`
- `notes/bank-d5-source-scaffold-handoff.md`
- `build/asset-bank-d5.json`
- `build/d5-table-splits.json`
- `build/d5-build-candidate-ranges.json`
- `build/d5-byte-equivalence-validation.json`

The generated map accounts for:

- binary assets: `118`
- binary asset bytes: `17856`
- asset mix: `118` graphics payloads (`gfx`)
- table bytes with exact source-order placement: `2624`
- exact post-pad table/tail region: `45056` bytes
- source scaffold protected bytes: `65536 / 65536`
- byte-equivalence scaffold validation: `durable-scaffold`, `139` modules,
  `0` non-OK modules, `0` byte mismatches
- missing payload metadata: `0`

## Bank layout

The high-level D5 layout is:

- `D5:0000..D5:45BF`: overworld sprite graphics tail, `118` payloads.
- `D5:45C0..D5:4FFF`: `UNKNOWN_D545C0`, an explicit zero-filled block,
  `2624` bytes in the US retail build.
- `D5:5000..D5:FFFF`: exact gameplay/battle/map table and zero-tail region,
  `45056` bytes.

The sprite tail runs from `SPRITE_1028` through `SPRITE_1145`, starting with
`SPRITE_GROUP_TONY_IN_BED` and ending at `SPRITE_GROUP_RICH_POKEY_HEAD`.
Unlike `D1-D4`, D5 does not dedicate the entire bank to sprite graphics.

## Post-Pad Data Sequence

The checked-in bank config names this source-order sequence after the empty
block:

- `data/items.asm`
- `data/store_inventories.asm`
- `data/psi_teleport_destinations.asm`
- `data/telephone_contacts.asm`
- `data/battle/action_table.asm`
- `data/battle/psi_abilities.asm`
- `data/battle/psi_names.asm`
- `data/battle/npc_ai_table.asm`
- `data/exp_table.asm`
- `data/battle/enemies.asm`
- `data/stats_growth_vars.asm`
- `data/condiment_table.asm`
- `data/map/teleport_destinations.asm`
- `data/map/hotspot_coordinates.asm`
- `data/timed_item_transformation_table.asm`
- `data/dont_care_names.asm`
- `data/initial_stats.asm`
- `data/timed_delivery_table.asm`

Several later source files exist in the reference tree, including battle action
data, PSI ability data, enemy data, condiment data, PSI names, and default
player/favorite-food names. The missing generated files are now accounted for
with YAML row counts from `refs/eb-decompile-4ef92`, source order from ebsrc,
and ROM zero-fill checks.

The exact split table is maintained in `notes/d5-table-splits.md` and
`build/d5-table-splits.json`. Important correction: `ITEM_CONFIGURATION_TABLE`
has `254` rows, not `256`, so it ends at `D5:76B1` and `STORE_TABLE` starts at
`D5:76B2`.

## Tooling behavior

`tools/build_asset_bank_manifest.py` now handles the explicit `.REPEAT @AMT`
block in this bank config and evaluates the US retail branch as `$A40` bytes.
It also blocks downstream offsets once a missing include has no later binary
asset anchor. That keeps mixed banks from reporting false precision. For D5,
`tools/build_d5_table_splits.py` supplies the dedicated table splitter that
recovers those downstream offsets exactly.

## Current D5 confidence boundary

High confidence:

- D5 is data/assets, not executable code.
- `D5:0000..D5:45BF` is the final overworld sprite graphics tail.
- `D5:45C0..D5:4FFF` is an explicit zero-filled pad in the US retail build.
- `D5:5000..D5:FFFF` is exactly split into source-order gameplay/battle/map
  table data plus a zero-filled tail.
- The timed-delivery source split at `D5:F649` is now understood as a
  source-order window that begins four bytes into the EF consumer-effective
  controller rows at `D5:F645`.
- `TIMED_DELIVERY_CONTROLLER_TABLE` row fields are consumer-backed by the
  EF timed-delivery helper family and summarized in
  `notes/d5-timed-delivery-row-contracts.md`.
- The timed-delivery contract now records source-emission ownership for the
  split/effective-row overlap: 4 controller bytes come from the `INITIAL_STATS`
  tail, 196 controller bytes come from `TIMED_DELIVERY_TABLE`, and the final 4
  bytes of the source split are zero padding. Selectors are contiguous `1..10`;
  success/failure far pointers target banks `C5`, `C6`, and `C7`; and the three
  observed enter/exit speed pairs are summarized without adding story-specific
  row names.
- `src/d5/bank_d5_helpers_asar.asm` protects the full bank through the reusable
  source-bank scaffold pipeline: `139` data-corridor modules, `65536` protected
  bytes, and `0` byte-equivalence mismatches.

Still intentionally out of scope:

- Story-specific names for every timed-delivery row beyond the script-backed
  family labels.
- Rendering or semantic grouping for the final sprite payloads beyond the
  source labels.

## Recommended next move

D5 is now closed for byte-preserving scaffold purposes. The next D5 work is
semantic rather than coverage: promote the exact table splits into richer data
contracts where useful, keep the corrected `254`-row item table count in
downstream tools, and use the row-family labels in the timed-delivery contract
as the boundary for any later story/script-specific naming pass.
