# Your Sanctuary Location Coordinate Table `C4:DE78`

## Scope

This note classifies the unknown-data include immediately before ebsrc's named
Your Sanctuary display routines.

The bank order is:

- `C4:DE78` = unknown data table
- `C4:DE98` = `INITIALIZE_YOUR_SANCTUARY_DISPLAY`
- `C4:DED0` = `ENABLE_YOUR_SANCTUARY_DISPLAY`
- `C4:DEE9..C4:E369` = the named Your Sanctuary location load/display helpers

## Source status

The full `C4:DE78..C4:E369` Your Sanctuary display corridor is now
source-promoted and byte-equivalent in the C4 scaffold:

- `src/c4/your_sanctuary_location_coordinate_table.asm` covers `C4:DE78..C4:DE98`
- `src/c4/your_sanctuary_display_state_helpers.asm` covers `C4:DE98..C4:DED0`
- `src/c4/your_sanctuary_display_enable_helpers.asm` covers `C4:DED0..C4:DEE9`
- `src/c4/your_sanctuary_palette_data_helpers.asm` covers `C4:DEE9..C4:DF7D`
- `src/c4/your_sanctuary_tile_arrangement_helpers.asm` covers `C4:DF7D..C4:E08C`
- `src/c4/your_sanctuary_tileset_data_helpers.asm` covers `C4:E08C..C4:E13E`
- `src/c4/your_sanctuary_location_data_loader.asm` covers `C4:E13E..C4:E281`
- `src/c4/your_sanctuary_location_lazy_loader.asm` covers `C4:E281..C4:E2D7`
- `src/c4/your_sanctuary_location_display_helpers.asm` covers `C4:E2D7..C4:E366`
- `src/c4/your_sanctuary_display_test_stub.asm` covers `C4:E366..C4:E369`

The next ebsrc frontier after this corridor is the ending cast-scene cluster at
`C4:E369`.

## Main result

`C4:DE78` is an eight-entry table of two-word records. The values are:

| index | word 0 | word 1 |
|---:|---:|---:|
| `0` | `0x0097` | `0x0030` |
| `1` | `0x0183` | `0x03F5` |
| `2` | `0x0023` | `0x01E4` |
| `3` | `0x0058` | `0x029C` |
| `4` | `0x01DF` | `0x0208` |
| `5` | `0x01BD` | `0x030B` |
| `6` | `0x034B` | `0x0258` |
| `7` | `0x02FE` | `0x04CC` |

The local consumer is the Your Sanctuary helper at `C4:E281`. It takes an index
in `A`, checks the matching loaded flag at `$B4BE + index * 2`, and if that
location has not been prepared yet it indexes `C4:DE78 + index * 4`. The first
word is passed in `A`, the second word in `X`, and the pair is consumed by
`C4:E13E`; after that the helper marks the `$B4BE` slot as loaded.

The table therefore behaves as the per-location coordinate/source-position table
for the eight Your Sanctuary location displays. The exact coordinate space still
belongs to the downstream `C4:E13E` and display-loader helpers, but the indexing
contract is byte-true.

## Working Names

- `C4:DE78` = `YourSanctuaryLocationCoordinateTable`
- `C4:DE98` = `InitializeYourSanctuaryDisplayState`
- `C4:DED0` = `EnableYourSanctuaryDisplayBg2State`
- `C4:DEE9` = `PrepareYourSanctuaryLocationPaletteData`
- `C4:DF7D` = `PrepareYourSanctuaryLocationTileArrangementData`
- `C4:E08C` = `PrepareYourSanctuaryLocationTilesetData`
- `C4:E13E` = `LoadYourSanctuaryLocationData`
- `C4:E281` = `LoadYourSanctuaryLocation`
- `C4:E2D7` = `DisplayYourSanctuaryLocation`
- `C4:E366` = `TestYourSanctuaryDisplayStub`

## Still open

- whether the two words should be named X/Y coordinates, source offsets, or
  map-space positions
- exact visual/display role of the `C4:E13E` consumer
