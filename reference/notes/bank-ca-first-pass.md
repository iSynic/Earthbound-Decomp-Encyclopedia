# Bank CA First Pass

## Main result

Bank `CA` is a battle-background asset/data bank, not a text bank and not an
ordinary code frontier.

Follow-up source-scaffold status:

- durable scaffold: `src/ca/bank_ca_helpers_asar.asm`
- manifest: `build/ca-build-candidate-ranges.json`
- handoff: `notes/bank-ca-source-scaffold-handoff.md`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `27`
- byte-equivalence: `OK`, `0` mismatches

The US bank config delegates to `bankconfig/common/bank0a.asm`, which contains:

- `20` compressed battle-background binary assets
- `6` battle-background pointer/config/motion table includes
- `1` byte of tail slack

Generated map:

- `notes/bank-ca-asset-data-map.md`
- `build/asset-bank-ca.json`

The generated map currently reports:

- binary assets: `20`
- binary asset bytes: `55201`
- asset mix: `15` graphics (`gfx`) and `5` arrangements (`arr`)
- table includes: `6`
- table bytes: `10334`
- coverage gap bytes: `1`
- missing payload metadata: `0`

## Tooling added

### `tools/build_asset_bank_manifest.py`

CA is the first bank in this run where the text-bank manifest is the wrong
tool. The new asset-bank manifest builder:

- recursively follows `.INCLUDE "bankconfig/common/..."` wrappers
- skips support includes such as `common.asm` and `symbols/...`
- reads `BINARY "..."` asset entries from the bank config source
- resolves asset offsets/sizes/compression from `earthbound.yml`
- samples the local ROM bytes at each asset span
- estimates table sizes from `.BYTE`, `.WORD`, and `.DWORD` directives
- emits JSON and Markdown maps

Example:

```powershell
python tools\build_asset_bank_manifest.py CA --json-out build\asset-bank-ca.json --markdown-out notes\bank-ca-asset-data-map.md
```

This should be reusable for later asset-heavy banks, especially the common
bankconfig banks after `CA`.

### `tools/promote_asset_bank_to_source_scaffold.py`

CA now also has the asset-bank equivalent of the text-bank promoter. It converts
`build/asset-bank-ca.json` into `build/ca-build-candidate-ranges.json`, creates
the checked-in data corridor stubs under `src/ca/`, and feeds the generic source
scaffold and byte-equivalence validators.

Example:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py CA
python tools\build_source_bank_scaffold.py --bank CA
python tools\validate_source_bank_byte_equivalence.py --bank CA --module all --combined --scaffold src\ca\bank_ca_helpers_asar.asm --strict
```

## Binary assets

The asset payloads are all LZHAL-compressed battle background pieces. The source
binary files are referenced by ebsrc but are not present as standalone files in
this refs checkout; `earthbound.yml` still provides exact ROM offsets/sizes.

Graphics assets in CA:

- `BATTLE_BACKGROUND_GFX_63` through `BATTLE_BACKGROUND_GFX_90`, non-contiguous
  by numeric id but contiguous by ROM placement
- largest: `BATTLE_BACKGROUND_GFX_63`, `8258` bytes at `CA:0000..CA:2041`
- smallest: `BATTLE_BACKGROUND_GFX_90`, `3` bytes at `CA:D79E..CA:D7A0`

Arrangement assets in CA:

- `BATTLE_BACKGROUND_ARR_37`
- `BATTLE_BACKGROUND_ARR_38`
- `BATTLE_BACKGROUND_ARR_39`
- `BATTLE_BACKGROUND_ARR_42`
- `BATTLE_BACKGROUND_ARR_100`

The binary asset block occupies `CA:0000..CA:D7A0`.

## Tables

The table block occupies `CA:D7A1..CA:FFFE`:

| Table include | CPU span | Bytes | Current structure |
| --- | --- | ---: | --- |
| `graphics_pointers.asm` | `CA:D7A1..CA:D93C` | `412` | `103` DWORD pointers |
| `arrangement_pointers.asm` | `CA:D93D..CA:DAD8` | `412` | `103` DWORD pointers |
| `palette_pointers.asm` | `CA:DAD9..CA:DCA0` | `456` | `114` DWORD pointers |
| `config_table.asm` | `CA:DCA1..CA:F257` | `5559` | `327` 17-byte layer config records |
| `scrolling_table.asm` | `CA:F258..CA:F707` | `1200` | `600` WORD values |
| `distortion_table.asm` | `CA:F708..CA:FFFE` | `2295` | mixed BYTE/WORD distortion records |

The battle background loader corroborates the table roles in
`refs/ebsrc-main/ebsrc-main/src/battle/load_battlebg.asm`:

- `BATTLEBG_GFX_POINTERS` selects compressed graphics payloads.
- `BATTLEBG_ARR_POINTERS` selects arrangement payloads.
- `BATTLEBG_PALETTE_POINTERS` selects palette data.
- `BG_DATA_TABLE` is indexed with `.SIZEOF(bg_layer_config_entry)` and literal
  `17`.
- `BG_SCROLLING_TABLE` and `BG_DISTORTION_TABLE` provide movement/distortion
  parameters referenced by config entries.

The `eb-decompile-4ef92` refs provide friendlier YAML views for several of
these tables:

- `refs/eb-decompile-4ef92/bg_data_table.yml`
- `refs/eb-decompile-4ef92/bg_scrolling_table.yml`
- `refs/eb-decompile-4ef92/bg_distortion_table.yml`

## Current CA confidence boundary

Locally strong:

- CA's bank-level shape is battle-background assets plus data tables.
- The asset spans and sizes are pinned from `earthbound.yml` and the ROM.
- The table spans are pinned by source directive counts and exact bank
  contiguity.
- The manifest accounts for the whole bank except one tail byte at `CA:FFFF`.
- Loader references corroborate the pointer/config table roles.

Still cautious:

- The standalone `.gfx.lzhal` and `.arr.lzhal` files referenced by ebsrc are
  absent from this refs snapshot, so the manifest validates against ROM slices
  rather than source asset files.
- This pass does not decompress or render the battle backgrounds.
- The distortion table's internal record structure is not fully named here,
  though the existing refs already give a high-level YAML interpretation.

## Recommended next move

Treat CA as structurally complete and byte-protected for the current
bank-coverage phase.

The next high-value step is `CB`, but the tactic should stay asset-oriented:
start by checking `bankconfig/common/bank0b.asm`, then extend
`build_asset_bank_manifest.py` only if CB introduces a new asset/source pattern
that CA did not need.
