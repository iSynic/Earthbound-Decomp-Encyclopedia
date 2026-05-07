# Bank C3 First Pass

## Main result

Bank `C3` is mostly event/actionscript payloads and data tables, with a smaller
set of source-ready window/text, battle-text, and battle-visual helper tails. It
is the bridge between C0/C1/C2 runtime code and many script/table assets: event
scripts, movement presets, map movement parameters, menu/title cursor tile data,
text-control token metadata, and battle visual palettes/offset tables.

Primary artifacts:

- `notes/bank-c3-progress-audit.md`
- `notes/bank-c3-reference-frontier.md`
- `notes/bank-c3-closure.md`
- `notes/bank-c3-working-name-proposals.md`
- `notes/script-payloads-c3.md`
- `notes/c3-source-data-map.md`
- `notes/c3-source-extraction-candidates.md`
- `notes/c3-mixed-source-split-plan.md`
- `notes/c3-source-emission-plan.md`
- `notes/c3-build-candidate-plan.md`
- `notes/c3-build-candidate-ranges.md`
- `notes/c3-build-candidate-range-validation.md`
- `notes/c3-source-residual-map.md`
- `notes/c3-build-candidate-source-conventions.md`
- `notes/c3-source-signature-validation.md`
- `notes/c3-source-prototype-validation.md`
- `notes/source-prototype-policy.md`
- `notes/c3-window-text-source-helper-corridor-e450-e7e3.md`
- `notes/c3-window-lifecycle-source-contract-e4ef-e6f7.md`
- `notes/c3-e84e-debug-menu-and-embedded-item-helpers-split.md`
- `notes/c3-inventory-equipped-slot-and-egg-refresh-helpers-e977-ebca.md`
- `notes/c3-hp-pp-source-contract-quartet-ec1f-ee13.md`
- `notes/c3-equipment-selector-source-contract-ee14-ef22.md`
- `notes/c3-jeff-repair-source-contract-f1ec.md`
- `notes/c3-battle-visual-effect-dispatch-source-contract-f981.md`
- `notes/data-contracts-c0-c3.md`
- `notes/data-contracts-c0-c4.md`

The audit currently reports:

- reference include entries: `1087`
- reference address-bearing include entries: `193`
- address-bearing unknown include entries: `57`
- local notes mention `294` distinct `C3:xxxx` addresses
- unknown include entries not directly mentioned in local notes: `0`
- working-name proposals: `164`
- source-ready emission units: `26` across `6` proposed modules
- source-emission prototypes present: `6`
  (`src/c3/window_text_helpers.asm`,
  `src/c3/inventory_equipment_tracked_items.asm`,
  `src/c3/hp_pp_adjustment_helpers.asm`,
  `src/c3/equipment_battle_selector_helpers.asm`,
  `src/c3/jeff_repair_psi_helpers.asm`,
  `src/c3/battle_visual_effect_helpers.asm`)
- prototype levels: `0` annotated-asm modules,
  `6` build-candidate modules,
  `0` contract-sketch modules
- source signature validation: `6` clean modules, `0` errors
- build-candidate byte ranges: `11` clean ranges, `65536` total protected bytes
  (`3629` source bytes, `61907` data-gap bytes)
- source scaffold residual map: `0` residual bytes; C3 is now `100.0%`
  protected by the source-bank scaffold manifest
- byte-equivalence scaffold validation: `durable-scaffold`, `11` modules,
  `0` non-OK modules, `0` byte mismatches
- open-ended source modules: `0`

## Bank layout

The current high-level C3 subsystem map is:

- Early system/error entries: anti-piracy and faulty Game Pak display entry
  points that share rendering proof with C4 system-error screen work.
- Event/actionscript payloads: intro scripts, event scripts, timed-delivery
  scripts, temporary actor movement/release scripts, and movement pulse presets.
- Map movement and interaction data: direction permission masks, probe offsets,
  placement direction parameters, staged movement direction tables, and subtile
  offset tables.
- Menu/title/cursor tile data: title name cursor tile runs and blinking
  triangle wait-frame tiles.
- Window/text helper tail: registered-copy cleanup, shared helper promotions,
  and late text/window support routines.
- Inventory/equipment helper tail: character inventory-slot access, equipped
  slot-reference checks, equipped-item dereference checks, and egg-family
  lifecycle refresh hooks. The `C3:E84E` row is now explicitly marked as a
  mixed debug-data/source-helper row that must split before emission.
- Battle text and article-token helpers: reflected-hit side-token resolution,
  enemy article selection, and text-control token metadata.
- Battle PSI/menu metadata: table families used by C1/C2 menu construction and
  battle display paths.
- Battle visual data: graphics strip offsets, OAM tile index rows, palette rows,
  and fixed-color triple tables.

## Current C3 confidence boundary

High confidence:

- C3 has full local coverage of every reference address-bearing unknown include
  start.
- Many C3 ranges are data or bytecode/script assets, not ordinary 65816 code.
- `script-payloads-c3.md` and `build/script-payloads-c3.json` separate promoted
  script payload labels from code labels.
- `c3-source-data-map.md` and `build/c3-source-data-map.json` separate reference
  include starts into event script assets, decoded bytecode labels, contract-backed
  tables, raw data frontiers, null stubs, and ordinary 65816 helper candidates.
- `c3-source-extraction-candidates.md` and
  `build/c3-source-extraction-candidates.json` turn those ordinary helper
  candidates into a source-carving queue, including embedded helpers inside mixed
  rows.
- `c3-mixed-source-split-plan.md` and
  `build/c3-mixed-source-split-plan.json` define the mechanical split for
  `C3:E84E`, carving two embedded inventory helpers out of the mixed row.
- `c3-source-emission-plan.md` and `build/c3-source-emission-plan.json` group
  all `26` source-ready helper units into `6` proposed source modules. All six
  modules now have prototype artifacts present.
- `src/c3/window_text_helpers.asm`,
  `src/c3/inventory_equipment_tracked_items.asm`,
  `src/c3/hp_pp_adjustment_helpers.asm`,
  `src/c3/equipment_battle_selector_helpers.asm`,
  `src/c3/jeff_repair_psi_helpers.asm`, and
  `src/c3/battle_visual_effect_helpers.asm` are source prototype artifacts.
  They are intentionally not build-integrated yet; they establish label,
  contract, dependency, pseudocode, and annotated-instruction-flow conventions
  for C3 helper source extraction.
- `c3-source-prototype-validation.md` and
  `tools/validate_c3_source_prototypes.py` enforce the current prototype-file
  invariants against the emission plan.
- `c3-source-signature-validation.md` and
  `tools/validate_c3_source_signatures.py` verify the address-prefixed C3
  prototype instruction streams against ROM decode, including the known
  interprocedural accumulator-width returns in the timed-item and visual-transfer
  helpers.
- `c3-build-candidate-plan.md` and
  `tools/build_c3_build_candidate_plan.py` track the remaining gap between
  build candidates and assembler-ready source: unresolved assembler symbols,
  raw external control-flow targets, local-label resolution metrics, and the
  battle-visual module's adjacent data-table/source-slice integration.
- `c3-assembler-contract-validation.md` and
  `tools/validate_c3_assembler_contract.py` define the first assembler-facing
  pilot gate. `src/c3/window_text_helpers.asm`,
  `src/c3/inventory_equipment_tracked_items.asm`,
  `src/c3/hp_pp_adjustment_helpers.asm`,
  `src/c3/jeff_repair_psi_helpers.asm`,
  `src/c3/equipment_battle_selector_helpers.asm`, and
  `src/c3/battle_visual_effect_helpers.asm` are now
  `pilot-ready` modules: all same-file symbols resolve and all external
  control-flow targets are named absolute aliases while the existing
  source-signature and byte-range gates stay clean.
- `c3-byte-equivalence-validation.md` and
  `tools/validate_source_bank_byte_equivalence.py` define the reusable
  assembler byte-equivalence gate; `tools/validate_c3_byte_equivalence.py`
  remains a C3 compatibility wrapper. The validator translates C3 pilot modules
  into scratch Asar form, preserves manifest-declared source-adjacent data gaps,
  patches a clean ROM copy at the original `org`, and compares the protected
  bytes against the original ROM. `tools/build_source_bank_scaffold.py`
  generates durable source-bank scaffolds from the same range manifest; for C3
  this is `src/c3/bank_c3_helpers_asar.asm`. The scaffold now covers all `65536`
  bytes in the bank through six source-helper modules plus five classified
  data/script corridors: `0` non-OK modules and `0` byte mismatches.
- `c3-build-candidate-ranges.md`,
  `c3-build-candidate-range-validation.md`,
  `c3-build-candidate-source-conventions.md`, and their paired tools establish
  the first build-candidate byte-range gate. The current build candidates are
  `src/c3/script_event_payloads_0000_e450.asm` (`C3:0000..C3:E450`, 58448
  bytes of event/actionscript payloads and source-adjacent data),
  `src/c3/window_text_helpers.asm` (`C3:E450..C3:E84E`, 1022 bytes),
  `src/c3/data_debug_menu_mixed_inventory_prefix.asm`
  (`C3:E84E..C3:E977`, 297 bytes of the mixed debug-menu row before the embedded
  inventory helpers),
  `src/c3/inventory_equipment_tracked_items.asm` (`C3:E977..C3:EC1F`, 680
  bytes), `src/c3/hp_pp_adjustment_helpers.asm` (`C3:EC1F..C3:EE14`, 501 bytes),
  `src/c3/equipment_battle_selector_helpers.asm` (`C3:EE14..C3:EF23`, 271
  bytes), `src/c3/data_battle_menu_tables_ef23_f1ec.asm`
  (`C3:EF23..C3:F1EC`, 713 bytes of battle-menu/PSI data),
  `src/c3/jeff_repair_psi_helpers.asm` (`C3:F1EC..C3:F2B1`, 197 bytes),
  `src/c3/data_battle_visual_tables_f2b1_f5f9.asm`
  (`C3:F2B1..C3:F5F9`, 840 bytes of battle-visual table data),
  `src/c3/battle_visual_effect_helpers.asm`
  (`C3:F5F9..C3:FB1F`, 1318 protected bytes: 958 source bytes and 360
  source-adjacent data-gap bytes), and
  `src/c3/data_battle_tail_and_delivery_payloads_fb1f_10000.asm`
  (`C3:FB1F..C3:10000`, 1249 bytes of battle-tail/delivery payload data); all
  source modules are signature-clean, and all 11 ranges are byte-range-clean.
- `tools/promote_c3_classified_data_to_source_scaffold.py` promotes the
  reference-derived C3 source/data map into scaffold data corridors, preserving
  row boundaries and labels for later event/actionscript decoding instead of
  flattening the bank into one anonymous blob.
- The C0-C4 data contract manifest gives source-ready table shapes for the
  movement, title/cursor, and battle-visual table families.
- The C3 closure map already classifies major regions by source-readiness bucket.

Still intentionally out of scope:

- Reconstructing every event/actionscript payload as high-level source.
- Treating script payload labels as ordinary routine labels.
- Finalizing all generated reference frontier addresses as naming debt.
- Fully modeling the event/actionscript VM semantics needed to port scripts into
  a clean engine.

## Recommended next move

C3 is now closed for byte-preserving source-bank scaffold purposes: helper
routines are source modules, script/data payloads are explicit protected
corridors, and the residual map is empty. The next C3-specific phase is semantic,
not coverage: decode event/actionscript payloads into higher-level script assets,
promote table corridors into richer typed contracts, and decide which data-only
labels should become public symbols for cross-bank source.
