# EarthBound C0-C4 Working-Name And Data-Contract Handoff

This packet collects a C0-C4 documentation pass against the EarthBound US ROM.
It is meant as a review aid for an existing disassembly/decompilation project,
not as a request to bulk-accept every label.

The names here are descriptive working labels. They should be treated as
evidence-backed suggestions with provenance, and renamed freely to match the
target repository's style.

## What's included

| File | Use |
| --- | --- |
| `working-names-c0-c4.tsv` | Full address/name/evidence table for C0-C4. |
| `working-names-c0-c4-high-confidence.tsv` | Smaller first-review subset of corroborated labels. |
| `working-names-c0-c4.ca65.inc` | ca65 constants for prototyping labels. |
| `working-names-c0-c4.asar.inc` | Asar constants for patch/debug experiments. |
| `working-names-c0-c4.sym` | Debugger symbol file. |
| `data-contracts-c0-c4.json` | Machine-readable WRAM/ROM table contract manifest. |
| `data-contracts-c0-c4.md` | Human-readable contract manifest. |
| `data-contract-summary.tsv` | Compact contract list for quick filtering. |
| `C0-C4-subsystem-index.md` | System-level map of how the banks fit together. |
| `C0-C4-evidence-snippets.md` | Short proof examples for the strongest handoff claims. |

## Scope

- Banks covered: `C0`, `C1`, `C2`, `C3`, `C4`
- Address notation: SNES CPU address form, e.g. `C4:7501`
- Full working-name entries: `1399`
- High-confidence working-name entries: `64`
- Data contracts: `32`
- Contract fields: `329`

## Recommended review path

1. Start with `data-contract-summary.tsv` and `data-contracts-c0-c4.md`.
   These are the most portable findings because they capture fixed WRAM roots,
   overlays, and ROM table shapes.
2. Load `working-names-c0-c4.sym` in a debugger or analysis environment to see
   whether the names help navigation.
3. Review `working-names-c0-c4-high-confidence.tsv` before the full TSV.
4. Use `C0-C4-subsystem-index.md` to choose a subsystem slice instead of
   reviewing 1399 names in address order.
5. Promote, rename, or reject labels one subsystem at a time.

## Confidence levels

`corroborated` means the name appeared through more than one local evidence
source in the notes, or the contract was strongly tied to an external reference
plus local consumers.

`proposed` means the name is locally useful and evidence-backed, but should not
be treated as canonical without review. Most entries are intentionally in this
bucket.

## Highest-value first slices

These are the slices most likely to help another project quickly:

- WRAM/data roots: `GAME_STATE`, `PARTY_CHARACTERS`, `BATTLERS_TABLE`,
  `BATTLE_SELECTION_SNAPSHOT`
- fixed D5 tables: `ITEM_CONFIGURATION_TABLE`, `BATTLE_ACTION_TABLE`,
  `PSI_ABILITY_TABLE`, `ENEMY_CONFIGURATION_TABLE`
- battle visual tables: `BATTLE_VISUAL_GRAPHICS_SOURCE_STRIP_OFFSETS`,
  `BATTLE_VISUAL_OAM_TILE_INDEX_GRID`, `BATTLE_PALETTE_SET_ROWS`
- C4 visual/movement tables: `WH_WINDOW_SPAN_RADIUS_RAMP_TABLE`,
  `MOVEMENT_OCTANT_TO_PULSE_SELECTOR_TABLE`,
  `YOUR_SANCTUARY_LOCATION_COORDINATE_TABLE`
- text/window/naming helpers around `C1:E48D`, `C1:E4BE`, and their C4
  rendering support

## Caveats

- This is not source-complete decompilation.
- Names are reviewable working labels, not upstream/community canonical names.
- Some `proposed` labels describe exact behavior but may want shorter or more
  idiomatic source names.
- Some visual helpers are byte-true but still lack final player-facing effect
  names.
- The evidence paths point back to the local notes corpus, not to files in this
  packet unless excerpted in `C0-C4-evidence-snippets.md`.

## Regeneration commands

From the local notes repo:

```powershell
python tools\build_working_name_manifest.py --banks C0 C1 C2 C3 C4 --output build\working-names-c0-c4.json
python tools\emit_source_labels.py --manifest build\working-names-c0-c4.json --output-dir build\labels --banks C0 C1 C2 C3 C4
python tools\build_data_contract_manifest.py
python tools\validate_data_contracts.py
```

