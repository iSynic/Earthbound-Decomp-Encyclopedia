# Bank C2 Source Scaffold Handoff

## Status

Bank `C2` is byte-complete for the current source-scaffold phase.

- durable scaffold: `src/c2/bank_c2_helpers_asar.asm`
- manifest: `build/c2-build-candidate-ranges.json`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `233`
- source bytes: `65536`
- preserved data-gap bytes: `0`
- byte-equivalence: `OK`, `0` mismatches

Bank C2 source scaffold with promoted helpers for menu/window, HP/PP roller, front HP/PP tile composition and clearing, current-window tilemap close/clear, managed text event slot snapshot/restore, party overlay registry, party inventory/status utilities, equipped-item derived-cache refresh, inventory transfer/equipment-slot preservation, weapon/charm/bracelet/headgear equipment preview block setup, enemy sunstroke check, scripted battle initialization, battle-start UFO present fallback table, battle-start present/message controller, battle-start candidate controller front/back halves, instant-win presentation, Magic Butterfly PP restore animation, battle selection snapshot export, candidate-pool population passes, second-stage candidate row promotion, battle-start status-message prelude, status-tile HP/PP lookups, reflected-hit text-context swap, bomb and item-side action helpers, early item-side continuation helpers, battler normalization snapshot/restore and enemy battler initialization, battle stat consequence dispatcher and consequence helpers, PP target loss and solidification item-action helpers, call-for-help sprite-width prefix logic, battle-background config/palette helpers, final-prayer/special-event helpers, final-prayer stage/damage/narrative phase helpers, final-prayer finale sequence/tilemap/record-player helpers, battle swirl overlay helpers, PSI animation frame/palette advancement, battle effect busy/allocation helpers, battle-sprite row/palette-wave helpers, enemy sprite color-wave comparison, battle-group enemy sprite loading, and the bank-end tail bytes.

## Regenerate And Validate

Use these commands from the repository root:

```powershell
python tools/build_source_bank_scaffold.py --bank C2
python tools/validate_source_bank_byte_equivalence.py --bank C2 --module all --combined --scaffold src/c2/bank_c2_helpers_asar.asm --strict
python tools/build_source_bank_candidate_ranges_doc.py --bank C2
python tools/build_source_bank_residual_map.py --bank C2
```

Expected validation:

- `C2 byte-equivalence: OK, 233 module(s), 0 mismatch(es).`
- `notes/c2-source-residual-map.md` reports `0` residual bytes and `0` residual ranges.

## Remaining Semantic Work

- C2 has no remaining preserved data gaps in the source scaffold. Remaining work is semantic polish: stronger struct names, better local labels/comments, and cross-bank contract notes for consumers in C0/C1/C3/C4.

## Latest Promotion

- The final C2 closure pass promoted the battle-background update/load corridor and the last small source-adjacent tables:
  - `src/c2/c2_db14_run_battle_bg_per_frame_update_body.asm` (`C2:DB14..DE0F`)
  - `src/c2/c2_d121_load_battle_background_main_body.asm` (`C2:D121..DAE3`)
  - `src/c2/c2_00d1_window_reset_initial_coordinate_data.asm` (`C2:00D1..0266`)
  - `src/c2/c2_0912_name_entry_grid_character_offset_table.asm` (`C2:0912..0958`)
  - `src/c2/c2_0958_menu_or_name_entry_mask_table.asm` (`C2:0958..09A0`)
- C2 now reports `65536` source bytes and `0` preserved data-gap bytes.

## Automation Workahead Folded In

- `notes/c2-source-promotion-candidates-workahead.md` records that the former true byte-corridor targets have been promoted: `C2:C6F0..CFE5`, `C2:0000..00D1`, and `C2:E6B3..E6B6`. The former `source_size=0` data tables at `C2:0912..0958` and `C2:0958..09A0` are now explicit `db` source data.
- `notes/c2-battle-contract-workahead.md` now treats `C2:3109..3B66` as completed source and shifts the item-selection RPC work to struct naming for the shared `$A97D..` action-selection record.
- `notes/c2-ef-battle-text-contract-workahead.md` is the active contract note for `C1:DC1C`, `C1:DC66`, and `C1:DD9F` battle-text caller semantics, including EF substitution payloads and the unique `C2:5C66 -> C1:DD9F` action-table message lane.
