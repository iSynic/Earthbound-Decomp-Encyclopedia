# Bank C3 closure map

This map consolidates the current bank `C3` documentation state after the reference-first, unknown-include, working-name, and data-contract passes.

The goal is not to replace the focused notes. It is the front door: use this to choose the right subsystem note, then use the focused note for byte-level evidence, reference corroboration, and remaining caveats.

## Closure status

Current audit state:

| Bank | Reference addresses covered | Unknown include entries left | Working names | Main role |
| --- | ---: | ---: | ---: | --- |
| `C3` | `112 / 332` reference addresses directly mentioned by local notes | `0` | `164` | event/actionscript payloads, map/UI data, text/window helpers, battle text tables, battle visual tables |

Supporting reports:

- `notes/bank-c3-progress-audit.md`
- `notes/bank-c3-reference-frontier.md`
- `notes/bank-c3-working-name-proposals.md`
- `notes/c3-build-candidate-ranges.md`
- `notes/c3-byte-equivalence-validation.md`
- `notes/c3-source-residual-map.md`
- `notes/c3-preserved-gap-contracts.md`

Source scaffold status:

- durable scaffold: `src/c3/bank_c3_helpers_asar.asm`
- manifest: `build/c3-build-candidate-ranges.json`
- modules: `11`
- source-backed bytes: `65536 / 65536`
- preserved data-gap bytes: `0`
- byte-equivalence: `OK`, `0` mismatches

This means every C3 byte is now represented by checked-in scaffold source.
Most of `C3:0000..E450` is still event/actionscript or raw data source, not
ordinary 65816 code; the remaining semantic work is VM/script decoding and
table typing rather than byte-corridor closure.

The remaining raw-looking regions in the C3 event/actionscript source-pilot
scaffold are explicitly contracted in `notes/c3-preserved-gap-contracts.md`.
They total `1930` bytes across `3` groups and split into `34` subsegments:
the bank prefix palette/system-screen/data corridor, the intro movement-pattern
and anti-piracy gate corridor, and the late map/interaction/menu table corridor.

Working-name outputs:

- `notes/bank-c3-working-name-proposals.md`
- `build/working-names-c3.json`
- `build/working-names-c0-c3.json`
- `build/labels/working-names-c3.asar.inc`
- `build/labels/working-names-c3.ca65.inc`
- `build/labels/working-names-c3.sym`
- `build/labels/working-names-c3.tsv`

Script-payload outputs:

- `notes/script-payloads-c3.md`
- `build/script-payloads-c3.json`

Source/data split outputs:

- `notes/c3-source-data-map.md`
- `build/c3-source-data-map.json`
- `notes/c3-source-extraction-candidates.md`
- `build/c3-source-extraction-candidates.json`
- `notes/c3-preserved-gap-contracts.md`
- `notes/c3-preserved-gap-contracts.json`

Data-contract outputs:

- `notes/data-contracts-c0-c3.md`
- `build/data-contracts-c0-c3.json`

Important caveat: audit closure means every address-bearing unknown include start from the reference map is directly documented somewhere in `notes/*.md`. It does not mean every event script byte, internal branch target, string pointer, or generated report address has a final source symbol.

## Machine-readable manifests

Build the C3 working-name manifest with:

```powershell
python tools\build_working_name_manifest.py --banks C3 --output build\working-names-c3.json
```

Build the combined C0-C3 working-name manifest with:

```powershell
python tools\build_working_name_manifest.py --banks C0 C1 C2 C3 --output build\working-names-c0-c3.json
```

Emit source labels with:

```powershell
python tools\emit_source_labels.py --manifest build\working-names-c0-c3.json --output-dir build\labels --banks C3
```

Build the C0-C3 data-contract manifest with:

```powershell
python tools\build_data_contract_manifest.py
```

Build the C3 script-payload manifest with:

```powershell
python tools\build_script_payload_manifest.py
```

Build the C3 source/data extraction map with:

```powershell
python tools\build_c3_source_data_map.py
```

Build the C3 preserved-gap contract report with:

```powershell
python tools\build_c3_preserved_gap_contracts.py
```

Build the C3 ordinary-source extraction queue with:

```powershell
python tools\build_c3_source_extraction_candidates.py
```

Validate the contract manifest with:

```powershell
python tools\validate_data_contracts.py
```

Look up C3 contract-backed addresses with:

```powershell
python tools\lookup_data_contract.py C3:E148 C3:F951 BATTLE_VISUAL_TOKEN_23_TO_2D_COLOUR_TRIPLES[3].green_component
```

Use C3 contracts directly in the generic ROM table inspector with:

```powershell
python tools\inspect_table.py --contract BATTLE_PALETTE_SET_ROWS --index 0 --count 1 --raw-bytes 8
```

To refresh the reference-facing reports:

```powershell
python tools\build_ref_index.py --output build\ref-index.json
python tools\build_ref_bank_report.py C3 --output notes\bank-c3-reference-frontier.md --limit 180
python tools\audit_bank_progress.py --bank C3 --output notes\bank-c3-progress-audit.md
python tools\audit_working_name_coverage.py --banks C3 --scope global --min-missing 3
```

Current manifest counts:

- working names: `164` C3 entries, `1049` C0-C3 entries
- script payloads: `80` promoted C3 payload labels, including `72` complete event-bytecode or branch-label decodes and `8` non-event payloads marked `not-applicable`
- source/data map: `193` address-bearing include rows split into `105` reference event-script assets, `30` decoded event bytecode include-start labels, `7` non-event script-adjacent assets, `14` contract-backed table starts, `24` ordinary 65816 source-helper starts, `1` mixed data/source row, `1` null stub, and `11` raw/frontier data rows; it also tracks `82` internal or named-include working labels
- source extraction queue: `26` source units, split into `24` include-start units and `2` embedded helpers inside mixed rows; `15` are priority-1 units
- data contracts: `27` contracts, `323` fields
- C3 data contracts: `17` ROM-table contracts added on top of the C0-C2 shared roots/tables

## Source-readiness buckets

| Bucket | Status | Source expectation |
| --- | --- | --- |
| Event/actionscript payloads | `script-payload` | Split as bytecode/script assets first; source names are useful labels, but interpreter-level source needs event VM contracts. |
| Timed delivery and temporary actor scripts | `script-payload` | Strong behavioral names and control-flow anchors; still not ordinary 65816 routines. |
| C0 callback and movement helper bindings | `source-ready with external proof` | Local C3 entry labels are pinned, but source extraction should preserve C0/C4 caller contracts. |
| Map movement and interaction tables | `data-ready` | Fixed table shapes now exist in `data-contracts-c0-c3.json`. |
| Menu/title cursor tile data | `data-ready` | Tile-word frame tables are byte-pinned and contract-backed where shape is clear. |
| Window/text helper tail | `source-ready` | Routine boundaries and text/window roles are named; some incidental branch labels should remain local labels. |
| Inventory/equipment helper tail | `source-ready with embedded split` | `C3:E977` and `C3:E9A0` need a mixed-row split out of `C3:E84E`; the later include-start helpers are ready as ordinary source units. |
| Battle text and article-token helpers | `source-ready with C4 proof` | C3 labels are strong, but full semantics depend on C4 token formatting. |
| Battle PSI/menu metadata | `data-ready` | Existing note names table families; can be split as source data with consumer comments. |
| Battle visual offset, palette, and token tables | `data-ready` | Table shapes are contract-backed; effect-script payload at `C3:F819` remains interpreter-dependent. |
| Generated reference frontier rows | `classified noise` | Generated reports mention many reference addresses; use them for navigation, not as naming debt by themselves. |

## Subsystem index

### Event and actionscript payloads

Primary notes:

- `notes/c3-intro-script-frontier-9ff2-a07f.md`
- `notes/c3-event-222-224-movement-helper-cluster.md`
- `notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md`
- `notes/c3-temporary-actor-movement-and-release-scripts.md`
- `notes/c3-timed-delivery-controller-working-names.md`

What is covered:

- intro/event script frontier around `C3:9FF2-C3:A07F`
- event scripts `222..224` and their movement helper calls
- reusable movement pulse presets around `C3:A0B2-C3:AB26`
- temporary actor movement/release scripts and timed-delivery controller labels

Source status:

- Treat these as bytecode/script assets with labels, not normal 65816 source.
- Names are useful for labels and comments, but high-confidence source reconstruction depends on event/actionscript VM decoding.

### Map movement and interaction data

Primary notes:

- `notes/c3-map-movement-parameter-table-e1d8-e240.md`
- `notes/input-direction-and-interaction-probes-c0402b-c04116.md`
- `notes/front-interaction-flow.md`
- `notes/staged-movement-wrapper-70cb.md`

Contract-backed data:

- `INPUT_DIRECTION_PERMISSION_MASK_TABLE` at `C3:E12C`
- `INTERACTION_PROBE_DIRECTION_X_OFFSETS` at `C3:E148`
- `INTERACTION_PROBE_DIRECTION_Y_OFFSETS` at `C3:E158`
- `MAP_ENTITY_PLACEMENT_DIRECTION_PARAM_TABLE` at `C3:E1D8`
- staged movement direction/subtile offset tables at `C3:E200-C3:E22F`

Source status:

- The table shapes are ready for source extraction.
- `MAP_ENTITY_PLACEMENT_DIRECTION_PARAM_TABLE` is still marked `proposed` because the exact C0-side packed entity field semantics are softer than the table boundary.

### Menu, title, and cursor tile data

Primary notes:

- `notes/c3-menu-cursor-tile-data-e3f8-e450.md`
- `notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md`

Contract-backed data:

- `TITLE_NAME_BUFFER_CURSOR_TILE_RUN` at `C3:E40E`
- `BLINKING_TRIANGLE_WAIT_FRAME_TILES` at `C3:E41C`

Source status:

- The four-frame blinking triangle family and title/name tile run are data-ready.
- `C3:E3F8-E405` and `C3:E44C` are documented boundaries, but they should stay as cautious data labels until their direct consumers are pinned more tightly.

### Window and text helper tail

Primary notes:

- `notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md`
- `notes/c3-shared-helper-working-name-promotion.md`
- `notes/c3-inventory-equipped-slot-and-egg-refresh-helpers-e977-ebca.md`
- `notes/c3-e84e-debug-menu-and-embedded-item-helpers-split.md`
- `notes/text-engine-entry-waits-window-gates-c10000-c102d0.md`

What is covered:

- C3 window registered-copy cleanup and adjacent text/window routines
- shared helper promotions used by C0/C1/C2 notes
- inventory/equipment source helpers around `C3:E977..EBCA`, including the
  corrected equipped inventory-slot reference contract
- boundaries around the late C3 window and battle visual tail

Source status:

- Routine starts are source-ready.
- Internal branch labels should be created only where they clarify local control flow; they do not need promoted working names by default.

### Battle text and article-token helpers

Primary notes:

- `notes/class2-reflected-hit-side-token-consumers.md`
- `notes/class2-reflected-hit-side-buffer-flags.md`
- `notes/class2-d59589-enemy-data-crosswalk.md`
- `notes/class2-row-position-text-cluster-c454f0.md`

What is covered:

- delayed reflected-hit side-token resolution
- enemy `the_flag` article selection through the `D5:9589` enemy-data domain
- `C3:F054` text-control token metadata table anchor

Source status:

- The C3 branch and table labels are source-ready as local helpers.
- Full user-facing meaning still depends on C4 text-control handling, so comments should reference the C4 proof trail instead of overclaiming.

### Battle PSI, menu, and known-state data

Primary notes:

- `notes/c3-window-and-battle-visual-unknown-tail-e7e3-f981.md`
- `notes/c3-battle-visual-offset-tables-f871-f8f1.md`
- `notes/c3-battle-visual-table-and-token-sublabels.md`

What is covered:

- PSI/menu group and known-state table families around `C3:F016-C3:F0B0`
- bridge into the battle visual tail

Source status:

- Table starts have working names, but only the strongest fixed-shape tables have data contracts.
- If these tables become source assets, add contracts after a consumer pass pins stride/count beyond the current working names.

### Battle visual tables

Primary notes:

- `notes/c3-battle-visual-offset-tables-f871-f8f1.md`
- `notes/c3-battle-visual-table-and-token-sublabels.md`
- `notes/c2-battle-sprite-render-and-palette-tail-c2eee7-c2ff9a.md`
- `notes/c2-battlebg-load-and-palette-effect-corridor-c2cfe5-c2e0e7.md`
- `notes/c2-psi-swirl-overlay-tail-c2e6b3-c2ea74.md`

Contract-backed data:

- `BATTLE_VISUAL_GRAPHICS_SOURCE_STRIP_OFFSETS` at `C3:F871`
- `BATTLE_VISUAL_OAM_TILE_INDEX_GRID` at `C3:F8B1`
- `BATTLE_PALETTE_SET_ROWS` at `C3:F8F1`
- `BATTLE_VISUAL_TOKEN_23_TO_2D_COLOUR_TRIPLES` at `C3:F951`
- `BATTLE_VISUAL_TOKEN_31_TO_35_COLOUR_TRIPLES` at `C3:F972`

Source status:

- These tables are ready to become named source data.
- `C3:F819` is a named battle-swirl overlay mode-2 payload, but its internal format belongs to the `AECC/AECE` effect-script interpreter and should not be split into records yet.

## Remaining work

Near-term useful work:

1. Build an event/actionscript contract layer for C3 payloads, so script bytes can be validated like ROM tables.
2. Add contracts for PSI/menu state tables once their consumer-side stride/count is fully pinned.
3. Push into C4 text-control formatting to close the article-token semantics behind `C3:E75D` and `C3:F054`.
4. Keep generated report rows out of naming debt unless a generated address corresponds to a real source boundary.

Current practical conclusion: C3 is not "fully decompiled as source" yet, but its address-bearing unknown include frontier is closed, its handwritten naming gaps are clean, and its strongest fixed-shape data is now machine-readable. The remaining hard part is interpreter semantics, not ordinary address triage.
