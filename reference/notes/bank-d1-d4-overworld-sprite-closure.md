# Banks D1-D4 Overworld Sprite Closure

## Status

Banks `D1` through `D4` are pure overworld sprite graphics banks. Together they
cover `905` raw graphics payloads, `SPRITE_0000` through `SPRITE_1027`, with no
code, no tables, and no unclaimed bytes inside the four banks.

| Bank | Reference bank | Sprite range | Asset count | Coverage boundary |
| --- | --- | --- | ---: | --- |
| `D1` | `11` | `SPRITE_0000..SPRITE_0122` | `123` | full bank, no gaps |
| `D2` | `12` | `SPRITE_0123..SPRITE_0353` | `231` | full bank, no gaps |
| `D3` | `13` | `SPRITE_0354..SPRITE_0692` | `339` | full bank, no gaps |
| `D4` | `14` | `SPRITE_0693..SPRITE_1027` | `335` | full bank, no gaps |

Primary artifacts:

- `notes/bank-d1-first-pass.md`, `build/asset-bank-d1.json`
- `notes/bank-d2-first-pass.md`, `build/asset-bank-d2.json`
- `notes/bank-d3-first-pass.md`, `build/asset-bank-d3.json`
- `notes/bank-d4-first-pass.md`, `build/asset-bank-d4.json`

## Source-Code Readiness

These banks are source-ready as opaque graphics includes. The bank configs
already provide the labels and source order, and `earthbound.yml` supplies the
exact offsets/sizes.

What is known:

- every byte in `D1-D4` is part of an `overworld_sprites/gfx/*.gfx` payload.
- locale-specific payloads are resolved for the US build through `LOCALEBINARY`.
- group labels in the bank configs identify sprite families for many contiguous
  frame runs.

What remains outside this bank range:

- palette data
- map/object placement data
- NPC/object config
- runtime animation/frame-selection semantics

## Recommended Next Move

Proceed to `D5`. The next bank should be checked with the asset manifest first;
if the overworld sprite graphics run has ended, let the bankconfig and manifest
summary decide whether the next helper should target palettes, map/object data,
or another generated-table family.
