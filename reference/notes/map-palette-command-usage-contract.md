# Map Palette Command Usage Contract

This contract joins parsed EBText `CHANGE_MAP_PALETTE` commands to the
resolved `.fts`/DA map palette variant contract.

## Summary

- parsed `CHANGE_MAP_PALETTE` hits: `33`
- unique palette variants referenced: `15`
- palette contract matches: `33`
- missing palette contract matches: `0`
- duration frame values: `0`:2, `1`:7, `30`:2, `60`:18, `120`:2, `180`:1, `255`:1
- text segments: `E18MGKT`:17, `EEVENT2`:7, `UNKNOWN_C9992F`:6, `EEVENT3`:2, `EEVENT4`:1
- palette row status counts: `exact_rom_palette_variant_match`:23, `matches_rom_variant_after_reserved_metadata_zeroing`:10

## Argument Model

The command macro is `1F E1 word byte`. Every parsed hit supports this
model:

- `word = (variant << 8) | palette_id`
- `byte = duration_frames`

The low byte of the word selects the DA `MAP_DATA_PALETTE_N` asset and
the high byte selects that asset's 192-byte variant. This links script
palette changes directly to the visual palette rows decoded in
`notes/map-fts-palette-variant-contract.md`.

## Usage By Palette Variant

| Palette ID | Variant | Word | Row ID | Hits | Durations | Segments | Palette Row Status | Setting |
| ---: | ---: | --- | --- | ---: | --- | --- | --- | --- |
| 1 | 0 | `0x0001` | `10` | 1 | `255`:1 | `UNKNOWN_C9992F`:1 | `matches_rom_variant_after_reserved_metadata_zeroing` | event_flag `422`, sprite `0`, flash `0`, event-palette `True` |
| 5 | 0 | `0x0005` | `50` | 6 | `60`:6 | `E18MGKT`:6 | `exact_rom_palette_variant_match` | event_flag `0`, sprite `0`, flash `0`, event-palette `False` |
| 6 | 3 | `0x0306` | `63` | 1 | `120`:1 | `EEVENT3`:1 | `matches_rom_variant_after_reserved_metadata_zeroing` | event_flag `288`, sprite `4`, flash `0`, event-palette `True` |
| 13 | 0 | `0x000D` | `d0` | 1 | `120`:1 | `UNKNOWN_C9992F`:1 | `matches_rom_variant_after_reserved_metadata_zeroing` | event_flag `287`, sprite `5`, flash `0`, event-palette `True` |
| 16 | 3 | `0x0310` | `g3` | 1 | `30`:1 | `UNKNOWN_C9992F`:1 | `matches_rom_variant_after_reserved_metadata_zeroing` | event_flag `517`, sprite `5`, flash `0`, event-palette `True` |
| 20 | 1 | `0x0114` | `k1` | 5 | `0`:1, `1`:3, `30`:1 | `EEVENT2`:3, `UNKNOWN_C9992F`:2 | `matches_rom_variant_after_reserved_metadata_zeroing` | event_flag `33323`, sprite `0`, flash `0`, event-palette `True` |
| 26 | 2 | `0x021A` | `q2` | 1 | `60`:1 | `EEVENT4`:1 | `matches_rom_variant_after_reserved_metadata_zeroing` | event_flag `0`, sprite `0`, flash `4`, event-palette `False` |
| 27 | 4 | `0x041B` | `r4` | 1 | `180`:1 | `EEVENT3`:1 | `exact_rom_palette_variant_match` | event_flag `0`, sprite `0`, flash `0`, event-palette `False` |
| 31 | 0 | `0x001F` | `v0` | 5 | `0`:1, `1`:4 | `EEVENT2`:4, `UNKNOWN_C9992F`:1 | `exact_rom_palette_variant_match` | event_flag `0`, sprite `0`, flash `0`, event-palette `False` |
| 31 | 2 | `0x021F` | `v2` | 1 | `60`:1 | `E18MGKT`:1 | `exact_rom_palette_variant_match` | event_flag `0`, sprite `0`, flash `0`, event-palette `False` |
| 31 | 3 | `0x031F` | `v3` | 2 | `60`:2 | `E18MGKT`:2 | `exact_rom_palette_variant_match` | event_flag `0`, sprite `0`, flash `0`, event-palette `False` |
| 31 | 4 | `0x041F` | `v4` | 1 | `60`:1 | `E18MGKT`:1 | `exact_rom_palette_variant_match` | event_flag `0`, sprite `0`, flash `0`, event-palette `False` |
| 31 | 5 | `0x051F` | `v5` | 2 | `60`:2 | `E18MGKT`:2 | `exact_rom_palette_variant_match` | event_flag `0`, sprite `0`, flash `0`, event-palette `False` |
| 31 | 6 | `0x061F` | `v6` | 3 | `60`:3 | `E18MGKT`:3 | `exact_rom_palette_variant_match` | event_flag `0`, sprite `0`, flash `0`, event-palette `False` |
| 31 | 7 | `0x071F` | `v7` | 2 | `60`:2 | `E18MGKT`:2 | `exact_rom_palette_variant_match` | event_flag `0`, sprite `0`, flash `0`, event-palette `False` |

## Parsed Hits

| Address | Segment | Word | Palette ID | Variant | Duration | Row ID |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `C7:72C2` | `E18MGKT` | `0x071F` | 31 | 7 | 60 | `v7` |
| `C7:72F9` | `E18MGKT` | `0x071F` | 31 | 7 | 60 | `v7` |
| `C7:7344` | `E18MGKT` | `0x0005` | 5 | 0 | 60 | `50` |
| `C7:7437` | `E18MGKT` | `0x051F` | 31 | 5 | 60 | `v5` |
| `C7:7497` | `E18MGKT` | `0x031F` | 31 | 3 | 60 | `v3` |
| `C7:74BD` | `E18MGKT` | `0x021F` | 31 | 2 | 60 | `v2` |
| `C7:74E6` | `E18MGKT` | `0x061F` | 31 | 6 | 60 | `v6` |
| `C7:750B` | `E18MGKT` | `0x061F` | 31 | 6 | 60 | `v6` |
| `C7:75F7` | `E18MGKT` | `0x0005` | 5 | 0 | 60 | `50` |
| `C7:7633` | `E18MGKT` | `0x031F` | 31 | 3 | 60 | `v3` |
| `C7:767D` | `E18MGKT` | `0x0005` | 5 | 0 | 60 | `50` |
| `C7:7689` | `E18MGKT` | `0x0005` | 5 | 0 | 60 | `50` |
| `C7:76C2` | `E18MGKT` | `0x0005` | 5 | 0 | 60 | `50` |
| `C7:76E8` | `E18MGKT` | `0x0005` | 5 | 0 | 60 | `50` |
| `C7:7868` | `E18MGKT` | `0x051F` | 31 | 5 | 60 | `v5` |
| `C7:7946` | `E18MGKT` | `0x061F` | 31 | 6 | 60 | `v6` |
| `C7:7D91` | `E18MGKT` | `0x041F` | 31 | 4 | 60 | `v4` |
| `C8:9595` | `EEVENT2` | `0x001F` | 31 | 0 | 1 | `v0` |
| `C8:959C` | `EEVENT2` | `0x0114` | 20 | 1 | 1 | `k1` |
| `C8:95A3` | `EEVENT2` | `0x001F` | 31 | 0 | 1 | `v0` |
| `C8:95AA` | `EEVENT2` | `0x0114` | 20 | 1 | 1 | `k1` |
| `C8:95B1` | `EEVENT2` | `0x001F` | 31 | 0 | 1 | `v0` |
| `C8:95CE` | `EEVENT2` | `0x0114` | 20 | 1 | 1 | `k1` |
| `C8:95D5` | `EEVENT2` | `0x001F` | 31 | 0 | 1 | `v0` |
| `C9:2C10` | `EEVENT3` | `0x041B` | 27 | 4 | 180 | `r4` |
| `C9:35B1` | `EEVENT3` | `0x0306` | 6 | 3 | 120 | `63` |
| `C7:C3A9` | `EEVENT4` | `0x021A` | 26 | 2 | 60 | `q2` |
| `C9:994A` | `UNKNOWN_C9992F` | `0x0310` | 16 | 3 | 30 | `g3` |
| `C9:9A81` | `UNKNOWN_C9992F` | `0x0001` | 1 | 0 | 255 | `10` |
| `C9:A049` | `UNKNOWN_C9992F` | `0x0114` | 20 | 1 | 0 | `k1` |
| `C9:A050` | `UNKNOWN_C9992F` | `0x001F` | 31 | 0 | 0 | `v0` |
| `C9:A057` | `UNKNOWN_C9992F` | `0x0114` | 20 | 1 | 30 | `k1` |
| `C9:AE4F` | `UNKNOWN_C9992F` | `0x000D` | 13 | 0 | 120 | `d0` |

## Machine-Readable Data

`notes/map-palette-command-usage-contract.json` records one row per
parsed command hit and one grouped row per referenced palette variant.
