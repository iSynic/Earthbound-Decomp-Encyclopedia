# Bank CB First Pass

## Main result

Bank `CB` is a mixed asset/data bank. Most of it is battle-background graphics,
arrangements, and palettes; the tail holds the battle-entry background layer
table plus two audio packs.

Follow-up source-scaffold status:

- durable scaffold: `src/cb/bank_cb_helpers_asar.asm`
- manifest: `build/cb-build-candidate-ranges.json`
- handoff: `notes/bank-cb-source-scaffold-handoff.md`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `304`
- byte-equivalence: `OK`, `0` mismatches

Generated map:

- `notes/bank-cb-asset-data-map.md`
- `build/asset-bank-cb.json`

The generated map currently reports:

- binary assets: `302`
- binary asset bytes: `63572`
- asset mix: `98` arrangements (`arr`), `88` graphics (`gfx`), `114` palettes
  (`pal`), and `2` audio packs (`ebm`)
- table includes: `1`
- table bytes: `1936`
- coverage gap bytes: `28`
- missing payload metadata: `0`

## Tooling improvements from this pass

CB extended the asset-bank manifest tool beyond CA's pattern:

- `tools/build_asset_bank_manifest.py` now handles one-extension payloads such
  as `battle_bgs/palettes/113.pal`.
- It now recognizes `INSERT_AUDIO_PACK n` and resolves the generated
  `audiopacks/n.ebm` payload from `earthbound.yml`.
- It now walks source order with a running cursor, which matters because CB
  places `data/battle/background_layer_table.asm` between the battle-background
  assets and the audio packs.

Without that source-order cursor, the table could be mispositioned after the
audio packs. The corrected layout is:

- `CB:0000..CB:D899`: battle-background graphics, arrangements, and palettes
- `CB:D89A..CB:E029`: `BTL_ENTRY_BG_TABLE`
- `CB:E02A..CB:FEE1`: `AUDIO_PACK_66`
- `CB:FEE2..CB:FFE3`: `AUDIO_PACK_59`
- `CB:FFE4..CB:FFFF`: tail slack

## Battle-background payloads

The battle-background payload block contains:

- `98` arrangement assets
- `88` graphics assets
- `114` palette assets

The palette payloads are raw `.pal` data, mostly `32` bytes or `8` bytes each.
The graphics/arrangement payloads are LZHAL-compressed, and many of the tiny
late entries are short sentinel-like compressed payloads:

- several arrangement entries are `5` bytes with first bytes `EB FF 00 20 FF`
- several graphics entries are `3` bytes with first bytes `3F 00 FF`

Those tiny entries are still real referenced assets because they are present in
`earthbound.yml` and in the bank config, not unclassified slack.

## Battle-entry layer table

`data/battle/background_layer_table.asm` occupies `CB:D89A..CB:E029`.

The source table is:

- label: `BTL_ENTRY_BG_TABLE`
- size: `1936` bytes
- shape: `968` WORD values

The source rows are pairs of `BATTLEBG_LAYER::*` values, one pair per battle
entry. This table connects battle entries to background layer IDs; those layer
IDs in turn index the CA pointer/config tables documented in
`notes/bank-ca-first-pass.md`.

## Audio packs

The bank tail contains two audio packs inserted by macro:

- `AUDIO_PACK_66`: `CB:E02A..CB:FEE1`, `7864` bytes
- `AUDIO_PACK_59`: `CB:FEE2..CB:FFE3`, `258` bytes

The ebsrc macro is:

```asm
INSERT_AUDIO_PACK num
```

which expands to a generated `AUDIO_PACK_n` label plus
`audiopacks/n.ebm`. The manifest resolves these through `earthbound.yml`.

## Current CB confidence boundary

Locally strong:

- CB's bank-level shape is assets plus one battle-entry layer table and two
  audio packs.
- All `302` binary payloads are pinned to exact ROM offsets/sizes from
  `earthbound.yml`.
- The table span is pinned from source directive counts and source order.
- The manifest accounts for the whole bank except `28` bytes of tail slack.

Still cautious:

- This pass does not decompress or render the battle backgrounds.
- It does not interpret audio-pack internals.
- The battle-entry layer table is structurally located and counted, but row
  semantics still depend on battle-entry and background-layer naming work.

## Recommended next move

Treat CB as structurally complete and byte-protected for the current
bank-coverage phase.

The next high-value step is `CC`. Since `INSERT_AUDIO_PACK` appears in later
common bank configs too, the asset manifest should already be ready for at
least part of that pattern.
