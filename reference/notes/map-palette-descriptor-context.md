# Map Palette Descriptor Context

This audit compares live-scene descriptor palette bits against the bank DA
map palette payload shape. Each map palette variant is `192` bytes, or
`96` SNES BGR555 colors: six 16-color subpalettes.

The arrangement descriptor exposes a three-bit SNES BG palette field.
Community RAM notes and the local C0 palette loaders split the CGRAM
shadow as text palettes at `$0200..$023F`, map palettes at
`$0240..$02FF`, and sprite palettes after that. This makes the bank DA
map palette payload the six BG palette block for descriptor palettes
`2..7`, with descriptor palette `N` mapping to DA subpalette `N - 2`.

## Summary

- direct scenes sampled: `950`
- cells per scene: `1024`
- pixels per cell: `64`
- map palette variant colors: `96`
- available 16-color subpalettes per variant: `6`
- resolved DA descriptor offset: `-2`
- DA map-palette fit overflow cells: `0`
- descriptor palette 0/1 text-palette cells: `291628`
- descriptor palette 2-7 map-palette cells: `681172`

## Descriptor Palette Counts

| Descriptor Palette | Cell Count | Pixel Count |
| ---: | ---: | ---: |
| 0 | 185419 | 11866816 |
| 1 | 106209 | 6797376 |
| 2 | 121553 | 7779392 |
| 3 | 108496 | 6943744 |
| 4 | 109510 | 7008640 |
| 5 | 75226 | 4814464 |
| 6 | 188674 | 12075136 |
| 7 | 77713 | 4973632 |

## Resolved CGRAM Roles

| Descriptor Palette | CGRAM Shadow Range | Role | DA Subpalette | Cells |
| ---: | --- | --- | ---: | ---: |
| 0 | `$0200..$021F` | `current_text_palette` |  | 185419 |
| 1 | `$0220..$023F` | `current_text_palette` |  | 106209 |
| 2 | `$0240..$025F` | `current_map_palette` | 0 | 121553 |
| 3 | `$0260..$027F` | `current_map_palette` | 1 | 108496 |
| 4 | `$0280..$029F` | `current_map_palette` | 2 | 109510 |
| 5 | `$02A0..$02BF` | `current_map_palette` | 3 | 75226 |
| 6 | `$02C0..$02DF` | `current_map_palette` | 4 | 188674 |
| 7 | `$02E0..$02FF` | `current_map_palette` | 5 | 77713 |

## Historical Candidate Offset Fit

These rows are kept for continuity with earlier audits. Offset `-2` is now
the resolved DA map-palette offset for descriptor palettes `2..7`; its
remaining overflow is exactly descriptor palettes `0..1`, which belong
to the text/common palette block rather than the DA map-palette payload.

| Offset | Overflow Cells | Overflow Pixels | Overflow % |
| ---: | ---: | ---: | ---: |
| -2 | 291628 | 18664192 | 29.978% |
| -1 | 263132 | 16840448 | 27.049% |
| 0 | 266387 | 17048768 | 27.384% |

## Top Raw-Descriptor Overflow Scenes

| Scene | Sector | Tileset | Palette | Overflow Cells |
| --- | --- | ---: | ---: | ---: |
| `map_scene.0277` | `8,21` | 6 | 0 | 1008 |
| `map_scene.0121` | `3,25` | 6 | 1 | 937 |
| `map_scene.0249` | `7,25` | 6 | 1 | 918 |
| `map_scene.0278` | `8,22` | 6 | 0 | 905 |
| `map_scene.0217` | `6,25` | 6 | 1 | 901 |
| `map_scene.0153` | `4,25` | 6 | 1 | 889 |
| `map_scene.1103` | `34,15` | 4 | 0 | 886 |
| `map_scene.0594` | `18,18` | 6 | 0 | 875 |
| `map_scene.0924` | `28,28` | 4 | 1 | 874 |
| `map_scene.1135` | `35,15` | 4 | 0 | 855 |
| `map_scene.0506` | `15,26` | 6 | 1 | 854 |
| `map_scene.0310` | `9,22` | 6 | 0 | 851 |
| `map_scene.1002` | `31,10` | 4 | 0 | 844 |
| `map_scene.0927` | `28,31` | 4 | 1 | 832 |
| `map_scene.0247` | `7,23` | 6 | 0 | 819 |
| `map_scene.0185` | `5,25` | 6 | 1 | 810 |

## Machine-Readable Data

`notes/map-palette-descriptor-context.json` records global, per-tileset,
and per-tileset/palette descriptor counts, resolved CGRAM roles, and
historical offset fit statistics.
