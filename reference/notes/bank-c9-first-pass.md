# Bank C9 First Pass

## Main result

Bank `C9` is a pure locale text-data bank. It has no ordinary address-bearing
unknown code/data include frontier and no text-parser unknowns under the current
decoder.

Follow-up source-scaffold status:

- durable scaffold: `src/c9/bank_c9_helpers_asar.asm`
- manifest: `build/c9-build-candidate-ranges.json`
- handoff: `notes/bank-c9-source-scaffold-handoff.md`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `16`
- byte-equivalence: `OK`, `0` mismatches

The US ebsrc bank config has support includes plus fourteen locale text
segments:

| Order | Segment | Bank segment | Role |
| ---: | --- | --- | --- |
| 0 | `ESHOP2` | `BANK09` | shop/service text block |
| 1 | `EEVENT3` | `BANK09` | event/message text block |
| 2 | `E02TWSN2` | `BANK09` | Twoson text block |
| 3 | `E02TWSN1` | `BANK09` | Twoson text block |
| 4 | `E19MOON` | `BANK09` | Moonside text block |
| 5 | `EGOODS0` | `BANK09` | goods/item text block |
| 6 | `E03HAPPY` | `BANK09B` | Happy Happy Village text block |
| 7 | `UNKNOWN_C9992F` | `BANK09B` | door/event-heavy text block with unknown reference name |
| 8 | `EEVENT5` | `BANK09B` | event/message text block |
| 9 | `E12RAMA` | `BANK09B` | Dalaam text block |
| 10 | `E15GUMI` | `BANK09B` | Tenda Village text block |
| 11 | `E14MAKYO` | `BANK09B` | Deep Darkness text block |
| 12 | `EBATTLE7` | `BANK09B` | battle text block |
| 13 | `EGOODS1` | `BANK09B` | goods/item text block |

Generated map:

- `notes/bank-c9-text-data-map.md`
- `build/text-bank-c9.json`

The generated map currently reports:

- text segments: `14`
- total bytes: `65250`
- non-locale/gap bytes: `286` across `2` gaps
- labels: `1177`
- parsed control commands: `21411`
- unknown parsed commands: `0`

The normal bank audit and frontier scorer now also cover C9:

- `notes/bank-c9-progress-audit.md`
- `notes/bank-c9-cluster-map.md`

Both agree that C9 has no address-bearing unknown code/data include frontier.

## About `UNKNOWN_C9992F`

The only address-bearing include path in the C9 bank config is
`text_data/UNKNOWN_C9992F.ebtxt`. The local map classifies it as a normal text
segment:

- CPU span: `C9:992F..C9:B225`
- bytes: `6391`
- labels: `195`, all public in the current `renameLabels` data
- parsed commands: `2047`
- unknown commands: `0`

The first labels make it look door/event-heavy rather than opaque binary data:

- `C9:992F` `MSG_END`
- `C9:9930` `TEXT_DOOR_085`
- `C9:995D` `TEXT_DOOR_069`
- `C9:99A1` `TEXT_DOOR_021`

The snippet at `C9:992F` begins with event-flag gates, a screen reload pointer,
map palette change, and door/event text. So this reference name should be read
as "unnamed text segment in ebsrc," not as an unknown code/data frontier.

## Coverage gaps

The text manifest reports only two small non-locale gaps:

| CPU span | Bytes | Current read |
| --- | ---: | --- |
| `C9:7FB3..C9:7FFF` | `77` | segment-boundary padding/slack before `BANK09B` |
| `C9:FF2F..C9:FFFF` | `209` | tail slack after `EGOODS1` |

## Current C9 confidence boundary

Locally strong:

- C9's bank-level shape is text-only.
- The fourteen text segments line up with `earthbound.yml` offsets/sizes and
  `renameLabels`.
- C9 has no address-bearing unknown code/data include frontier.
- The current text decoder parses C9 with zero unknown command starts.
- The `UNKNOWN_C9992F` include is structurally understood as text data.

Still cautious:

- This pass does not semantically interpret every shop, Twoson, Moonside,
  Happy Happy, door/event, Dalaam, Tenda, Deep Darkness, or battle text branch.
- `UNKNOWN_C9992F` still deserves a better human-facing segment name later, but
  naming it properly should come from script/door context rather than from the
  bank-coverage pass.

## Recommended next move

Treat C9 as structurally complete for the current bank-coverage phase.

C9 is also byte-protected by the durable source scaffold and is the cleanest
text-command regression case in this group because it has zero parser unknowns.
The next bank-wide target after this text-bank run is `CA`; first check whether
it is asset/table-shaped rather than assuming the locale text pattern continues.
