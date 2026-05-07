# Banks D1-D5 Overworld Sprite Run

## Status

The overworld sprite graphics run spans all of `D1-D4` and the front of `D5`.
Together these banks cover `1023` raw graphics payloads, `SPRITE_0000` through
`SPRITE_1145`.

| Bank | Reference bank | Sprite range | Asset count | Coverage boundary |
| --- | --- | --- | ---: | --- |
| `D1` | `11` | `SPRITE_0000..SPRITE_0122` | `123` | full bank, no gaps |
| `D2` | `12` | `SPRITE_0123..SPRITE_0353` | `231` | full bank, no gaps |
| `D3` | `13` | `SPRITE_0354..SPRITE_0692` | `339` | full bank, no gaps |
| `D4` | `14` | `SPRITE_0693..SPRITE_1027` | `335` | full bank, no gaps |
| `D5` | `15` | `SPRITE_1028..SPRITE_1145` | `118` | `D5:0000..D5:45BF` |

Primary artifacts:

- `notes/bank-d1-d4-overworld-sprite-closure.md`
- `notes/bank-d5-first-pass.md`
- `notes/bank-d5-asset-data-map.md`
- `build/asset-bank-d1.json` through `build/asset-bank-d5.json`

## Source-Code Readiness

The sprite payload portion is source-ready as opaque graphics includes. The bank
configs provide labels and source order, while `earthbound.yml` supplies exact
offsets and sizes.

What is known:

- every byte in `D1-D4` is overworld sprite graphics.
- `D5:0000..D5:45BF` extends the same sprite graphics family.
- locale-specific payloads are resolved for the US build through
  `LOCALEBINARY`.
- group labels identify many sprite families and frame runs.

What remains outside this sprite run:

- palettes
- map/object placement data
- NPC/object config
- runtime animation/frame-selection semantics
- the mixed gameplay/battle/map table region at `D5:5000..D5:FFFF`

## Recommended next move

Continue bank-by-bank from `D6`. If later banks reference sprite palettes,
sprite metadata, or animation/frame selectors, use this run note as the graphics
payload boundary when tying rendering semantics back to raw art.
