# Bank E0 First Pass

## Main result

Bank `E0` is a mixed UI/font/town-map/audio data bank. It contains text-window
graphics, font data, a compressed SRAM save-template payload, a split
text-window/town-map table span, six compressed town maps, and two audio packs.

Primary artifacts:

- `notes/bank-e0-asset-data-map.md`
- `notes/bank-e0-source-scaffold-handoff.md`
- `build/asset-bank-e0.json`
- `build/e0-build-candidate-ranges.json`
- `build/e0-byte-equivalence-validation.json`

The generated map accounts for:

- binary assets: `14`
- binary asset bytes: `64964`
- asset mix: `8` binary blobs, `4` graphics payloads, and `2` audio packs
- inferred generated table bytes: `495`
- coverage gap bytes: `77`
- source scaffold protected bytes: `65536 / 65536`
- byte-equivalence scaffold validation: `durable-scaffold`, `16` modules,
  `0` non-OK modules, `0` byte mismatches
- missing payload metadata: `1`

## Bank layout

The high-level E0 layout is:

- `E0:0000..E0:0753`: `TEXT_WINDOW_GFX`, `1876` bytes.
- `E0:0754..E0:079F`: `FLAVOURED_TEXT_GFX`, `76` bytes.
- `E0:07A0..E0:09B3`: `MOTHER2_ROMAJI_FONT`, `532` bytes.
- `E0:09B4..E0:1358`: `COMPRESSED_SRAM`, a compressed SRAM save-block
  initialization template inferred as `2469` bytes because
  `mystery_sram.bin.lzhal` is missing from `earthbound.yml`.
- `E0:1359..E0:13B8`: `MRSATURN_FONT_DATA`, `96` bytes.
- `E0:13B9..E0:1FB8`: `MRSATURN_FONT_GFX`, `3072` bytes.
- `E0:1FB9..E0:21A7`: generated text-window/town-map table span, `495` bytes.
- `E0:21A8..E0:ED02`: town maps `0` through `5`, `52059` bytes total.
- `E0:ED03..E0:FCE0`: `AUDIO_PACK_110`, `4062` bytes.
- `E0:FCE1..E0:FFB2`: `AUDIO_PACK_6`, `722` bytes.
- `E0:FFB3..E0:FFFF`: tail slack, `77` bytes.

## Generated Table Span

The bank config names four generated/source-table includes between font data and
town map graphics:

- `data/text_window_properties.asm`
- `data/text_window_flavour_palettes.asm`
- `data/movement_text_string_palette.asm`
- `data/map/town_map_gfx_pointers.asm`

Those files are absent from the checked-in reference tree. Because the next
known binary asset starts at `E0:21A8`, the manifest safely treats
`E0:1FB9..E0:21A7` as one combined generated table span. The span is now split
semantically by `notes/text-window-skin-bundle-contracts.md` into the flavour
selector table, window palette blocks, movement-text palette row, and six-entry
town-map graphics pointer tail. `notes/ui-font-town-map-asset-contracts.md`
now carries the source-emission rows for that split: text-window selectors,
palette blocks, movement text palette, and the E0 town-map graphics pointer
table are emit-ready, while non-consumer-backed palette row labels remain
numeric/preserved.

## Tooling behavior

`tools/build_asset_bank_manifest.py` now infers a missing-yml binary span when a
bank-config binary payload lacks metadata but is bracketed by known assets. This
recovers `COMPRESSED_SRAM` as `E0:09B4..E0:1358` while still reporting
`mystery_sram.bin.lzhal` as missing payload metadata. Separately,
`notes/sram-template-contracts.md` resolves the decompressed payload as eight
0x500-byte `save_block` records with three primary/backup user save-slot pairs
and two preserved reserve template blocks. The UI/font/town-map contract uses
that evidence as the E0 SRAM source-emission policy: emit the compressed source
payload with decoded block inventory available to tooling, and keep reserve
blocks 6 and 7 as reserve records until narrower owner evidence appears.

The parser also now accepts indented labels, which resolves labels inside
conditional blocks such as `MOTHER2_ROMAJI_FONT`, `COMPRESSED_SRAM`,
`MRSATURN_FONT_DATA`, and `MRSATURN_FONT_GFX`.

## Current E0 confidence boundary

High confidence:

- E0 is data/assets, not executable code.
- UI graphics, fonts, the SRAM save-template payload, generated text/town-map
  tables, town map graphics, and audio spans are exact for the US retail build.
- Only `77` bytes at the end of the bank are unclaimed slack.
- `src/e0/bank_e0_helpers_asar.asm` protects the full bank through the reusable
  source-bank scaffold pipeline. The inferred `COMPRESSED_SRAM` payload remains
  byte-exact; its checked-in semantic contract is the SRAM save-template model,
  while the original yml payload metadata remains absent.

Still intentionally out of scope:

- Deciding whether future installers emit `COMPRESSED_SRAM` as one compressed
  template blob or as eight decoded save-block records.
- Naming reserve SRAM template block provenance beyond the retail save-slot
  loops.
- Naming the remaining presentation-specific rows inside each text-window
  palette block beyond the currently consumer-backed row roles.
- Rendering town maps or text-window graphics.
- Audio-pack internals.

## Recommended next move

E0 is now closed for byte-preserving scaffold purposes. The remaining work is
semantic polish: use `notes/ui-font-town-map-asset-contracts.md` for the E0
text-window, town-map pointer, and SRAM template source-emission rows; preserve
the missing-yml metadata note for provenance; and optionally add render fixtures
for UI graphics, fonts, and town maps.
