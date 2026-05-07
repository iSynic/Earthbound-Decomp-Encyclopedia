# Banks E2-EE Audio Pack Run

## Status

Banks `E2` through `EE` are overwhelmingly audio-pack data. With the exception
of the custom `AUDIO_PACK_1` assembly block at the front of `E6`, the run is
made from source-order `INSERT_AUDIO_PACK` payloads.

| Bank | Reference bank | Main content | Binary assets | Claimed bytes | Gap bytes |
| --- | --- | --- | ---: | ---: | ---: |
| `E2` | `22` | audio packs `108`, `0`, `36`, `18` | `4` | `65533` | `3` |
| `E3` | `23` | audio packs `3`, `70`, `37`, `32` | `4` | `65522` | `14` |
| `E4` | `24` | audio packs `64`, `42`, `126`, `125`, `155` | `5` | `65529` | `7` |
| `E5` | `25` | audio packs `50`, `92`, `56`, `122`, `166` | `5` | `65502` | `34` |
| `E6` | `26` | custom `AUDIO_PACK_1`, packs `74`, `76`, `47`, `73` | `4` | `65525` | `11` |
| `E7` | `27` | audio packs `78`, `82`, `8`, `24` | `4` | `65380` | `156` |
| `E8` | `28` | audio packs `84`, `60`, `153`, `124`, `46`, `7` | `6` | `65517` | `19` |
| `E9` | `29` | audio packs `27`, `80`, `118`, `131`, `2`, `149` | `6` | `65381` | `155` |
| `EA` | `2A` | audio packs `54`, `52`, `72`, `89`, `35`, `140`, `145` | `7` | `65506` | `30` |
| `EB` | `2B` | eight audio packs | `8` | `65535` | `1` |
| `EC` | `2C` | fourteen audio packs | `14` | `65428` | `108` |
| `ED` | `2D` | thirty-six audio packs | `36` | `65534` | `2` |
| `EE` | `2E` | forty-six audio packs plus large tail slack | `46` | `37377` | `28159` |

## Source-Code Readiness

The run is source-ready as opaque audio payloads. The bank configs provide
source order, `earthbound.yml` provides exact spans for normal audio packs, and
the manifest tool now handles E6's custom sliced audio-pack block without
double-counting.

What remains outside this pass:

- audio subpack decoding
- SPC transfer/runtime semantics
- explanation of the large `EE:9201..EE:FFFF` tail region

## Recommended next move

Regenerate the global ref index and then move into a project-level integration
pass for `D5-EE`, because this run closes a very large amount of remaining ROM
as assets/data rather than code.
