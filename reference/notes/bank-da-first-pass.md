# Bank DA First Pass

## Main result

Bank `DA` is a map arrangement/palette/audio bank. It starts with three
compressed map arrangements, then contains map palettes `0` through `31`, an
inferred palette pointer table, and an audio pack.

Primary artifacts:

- `notes/bank-da-asset-data-map.md`
- `notes/da-map-palette-subrecord-contracts.md`
- `notes/da-map-palette-subrecord-contracts.json`
- `notes/map-palette-pointer-table-contract.md`
- `notes/map-fts-palette-variant-contract.md`
- `build/asset-bank-da.json`

The generated map accounts for:

- binary assets: `36`
- binary asset bytes: `65422`
- asset mix: `3` compressed arrangements, `32` palettes, and `1` audio pack
- inferred generated table bytes: `96`
- coverage gap bytes: `18`
- missing payload metadata: `0`

## Bank layout

The high-level DA layout is:

- `DA:0000..DA:1341`: `MAP_DATA_TILE_ARRANGEMENT_5`, `4930` bytes.
- `DA:1342..DA:4EA2`: `MAP_DATA_TILE_ARRANGEMENT_6`, `15201` bytes.
- `DA:4EA3..DA:7CA6`: `MAP_DATA_TILE_ARRANGEMENT_7`, `11780` bytes.
- `DA:7CA7..DA:FAA6`: `MAP_DATA_PALETTE_0` through
  `MAP_DATA_PALETTE_31`, `32256` bytes total.
- `DA:FAA7..DA:FB06`: `data/map/unknown_map_palette_pointer_table.asm`,
  inferred as `96` bytes.
- `DA:FB07..DA:FFED`: `AUDIO_PACK_111`, `1255` bytes.
- `DA:FFEE..DA:FFFF`: tail slack, `18` bytes.

## Palette Data

All 32 map palette payloads are present in source order as
`maps/palettes/*.pal` assets. Their individual sizes vary from `192` bytes to
`1536` bytes, and the manifest records exact CPU spans for each payload.

The checked-in source tree does not contain
`data/map/unknown_map_palette_pointer_table.asm`, but the next known asset is
`AUDIO_PACK_111` at `DA:FB07`. The manifest therefore safely infers the pointer
table as `DA:FAA7..DA:FB06`.

The palette payload run now has a consumer/tool-backed subrecord contract:

- `DA:7CA7..DA:FAA6`: `DA_MAP_PALETTE_VARIANT_TABLE`, 168 physical rows of
  192 bytes. Each row contains six 16-colour SNES BGR555 subpalettes for map
  descriptor palettes `2..7`; raw-ROM words `0`, `16`, `32`, and `48` are
  metadata slots named `event_flag`, `event_palette_selector_word`,
  `sprite_palette`, and `flash_effect`.
- `DA:FAA7..DA:FB06`: `MAP_PALETTE_POINTER_TABLE`, 32 three-byte long pointers
  whose targets match `MAP_DATA_PALETTE_0..31`.

`notes/da-map-palette-subrecord-contracts.md` ties this to the `.fts` palette
variant rows, map descriptor palette audit, and parsed `CHANGE_MAP_PALETTE`
script commands. All 168 palette-setting row keys match, all raw-ROM versus
visual-row differences are explained by metadata-word zeroing, and descriptor
palettes `2..7` map to DA subpalettes with zero overflow cells.

The DA palette report now also carries the row-level metadata distributions
needed for source emission without over-naming runtime behavior: 14 physical
rows carry an event-palette selector/payload pair, all 14 payload shapes match
the palette-setting model, 23 rows carry a nonzero sprite-palette metadata word,
and 8 rows carry a nonzero flash-effect metadata word. The parsed script usage
join covers 33 `CHANGE_MAP_PALETTE` hits across 15 palette variants; 5 of those
script-referenced variants are event-palette rows.

## Current DA confidence boundary

High confidence:

- DA is data/assets, not executable code.
- Arrangement, palette, inferred pointer-table, and audio spans are exact for
  the US retail build.
- The palette pointer table and 192-byte palette variant subrecords are now
  contract-backed.
- Metadata-word distributions and script-side palette variant usage are
  summarized for source-emission targeting.
- Only `18` bytes at the end of the bank are unclaimed slack.

Still intentionally out of scope:

- Runtime dispatch semantics for the `event_palette_selector_word` metadata
  slot.
- Decompressing or rendering arrangements `5` through `7`.
- Audio-pack internals.

## Recommended next move

Keep the DA palette contracts regression-tested while future runtime passes
follow the event-palette selector path. Arrangement rendering remains optional
asset polish rather than a blocker for table semantics.
