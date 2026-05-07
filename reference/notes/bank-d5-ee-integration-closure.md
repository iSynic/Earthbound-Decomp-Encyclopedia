# Banks D5-EE Integration Closure

## Status

Banks `D5` through `EE` are now mapped at bank level for the US retail build.
This range is data/assets/audio, not executable code. The only large non-padding
confidence boundary that remains is the named but internally unresolved gameplay
table region in `D5`.

Primary artifacts:

- `notes/bank-d5-ee-asset-bank-rollup.md`
- `build/asset-bank-rollup-d5-ee.json`
- `notes/bank-d1-d5-overworld-sprite-run.md`
- `notes/bank-e2-ee-audio-pack-run.md`
- `build/asset-bank-d5.json` through `build/asset-bank-ee.json`

Rollup totals for `D5-EE`:

- binary assets: `440`
- binary asset bytes: `1523475`
- table/custom-data bytes: `105159`
- reported gap bytes: `75302`

The reported gaps break down into:

- `D5:5000..D5:FFFF`: `45056` bytes of named gameplay/battle/map table data
  whose internal split is blocked by missing generated source files.
- zero-filled slack/padding: `30246` bytes total.

## Bank Families

| Range | Main content | Status |
| --- | --- | --- |
| `D5:0000..D5:45BF` | final overworld sprite graphics tail | source-ready as opaque graphics includes |
| `D5:45C0..D5:4FFF` | explicit zero-filled block | source-ready pad |
| `D5:5000..D5:FFFF` | items, stores, teleport, phone, battle, PSI, enemy, stats, map, timed-item, default-name tables | named but internally unresolved |
| `D6` | map tile chunks `1..6` | source-ready as opaque map tile binaries |
| `D7` | map tile chunks `7..10`, generated palette/sector metadata, arrangement `0` | bank-level closed; generated metadata split unresolved |
| `D8` | generated tile collision data/pointers, warning assets, audio | bank-level closed; collision split unresolved |
| `D9-DC` | map arrangements, map graphics, map palettes, generated map music/palette tables, audio | bank-level closed |
| `DD-DF` | map tileset graphics, animation graphics, palette-animation data, audio | bank-level closed; palette-animation split unresolved |
| `E0` | text-window graphics, fonts, town maps, text/town-map tables, audio | bank-level closed; table split unresolved |
| `E1` | flyover text, fonts, credits, intro/title/ending/town-map assets, audio | bank-level closed; several unknown table/payload splits unresolved |
| `E2-EE` | audio packs | source-ready as opaque audio payloads, with custom E6 block handled |

## EE Tail Check

The large `EE` tail region is very likely padding/free space rather than an
unmodeled live table.

Direct ROM check:

- span: `EE:9201..EE:FFFF`
- size: `28159` bytes
- unique byte count: `1`
- fill byte: `0x00`

This matches the pattern of smaller zero-filled tails throughout the mapped
asset/audio banks. The checked-in reference tree also stops at
`bank2e.asm`; no `bank2f.asm` is present under
`refs/ebsrc-main/ebsrc-main/src/bankconfig/common`.

## Source-Code Readiness

Source-ready now as opaque includes:

- D5 sprite graphics tail.
- D6 map tile chunks.
- D7-D8 known binary payloads and inferred generated blocks.
- D9-DF map arrangement/graphics/palette/audio payloads and inferred generated
  table spans.
- E0-E1 UI/font/intro/ending/town-map/audio payloads and inferred/generated
  spans.
- E2-EE audio pack run, including E6's custom `AUDIO_PACK_1` assembly block.

Still needs format-specific work before it can become pleasant source:

- D5 gameplay/battle/map table region.
- D7 generated global palette/per-sector attribute split.
- D8 tile collision data and pointer-table split.
- DC per-sector music semantics.
- DF palette animation table split and semantics.
- E0 text-window/town-map table split.
- E1 flyover/credits/photographer/town-map icon table semantics and a few
  missing-yml unknown payload splits.

## Tooling Added In This Pass

`tools/summarize_asset_bank_manifests.py` now builds cross-bank rollups from the
per-bank JSON manifests. It records per-bank binary/table/gap totals and samples
gap bytes from the ROM, so large zero-filled tails like `EE:9201..EE:FFFF` can
be distinguished from genuinely mixed unresolved regions.

The asset manifest tool also now handles:

- indented labels inside conditional branches
- missing-yml binary spans bracketed by known assets
- `LOCALEINCLUDE` data anchors
- `EBSTAFF_*` credits macros
- sliced `BINARY "file", offset, length` directives
- unresolved `.INCBIN` spans anchored by the next known binary

## Recommended Next Move

Treat `D6-EE` as bank-level closed for asset/source-layout purposes, with
format-specific splitters deferred until we need semantics. The highest-value
next task is either:

- attack the `D5:5000..D5:FFFF` gameplay table block, because it is the largest
  remaining mixed unresolved region in this range; or
- run a whole-project progress audit to identify the next unmapped banks outside
  the configured `D5-EE` closure.
