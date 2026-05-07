# Bank EE First Pass

## Main result

Bank `EE` is an audio-pack bank with a large unclaimed tail. It contains
forty-six small `INSERT_AUDIO_PACK` payloads from `EE:0000` through `EE:9200`,
then has `28159` bytes of remaining bank space.

Primary artifacts:

- `notes/bank-ee-asset-data-map.md`
- `build/asset-bank-ee.json`

The generated map accounts for:

- binary assets: `46`
- binary asset bytes: `37377`
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `28159`
- missing payload metadata: `0`

## Bank layout

`EE:0000..EE:9200` is a dense run of small audio packs:

- starts with `AUDIO_PACK_136`, `EE:0000..EE:0553`, `1364` bytes.
- includes packs `112`, `163`, `115`, `53`, `67`, `20`, `144`, `63`, `138`,
  `127`, `16`, `148`, `23`, `11`, `142`, `160`, `101`, `103`, `51`, `93`,
  `95`, `164`, `151`, `12`, `135`, `83`, `88`, `31`, `129`, `22`, `17`, `91`,
  `81`, `147`, `152`, `128`, `159`, `49`, `9`, `69`, `167`, `130`, `168`,
  and `137`.
- ends with `AUDIO_PACK_41`, `EE:8FD6..EE:9200`, `258` bytes.
- `EE:9201..EE:FFFF` is unclaimed tail space, `28159` bytes.

## Current EE confidence boundary

High confidence:

- EE is data/assets, not executable code.
- Every byte from `EE:0000` through `EE:9200` belongs to a named audio pack.
- The checked-in common bank configs stop at `bank2e.asm`; no `bank2f.asm`
  exists in the reference tree.

Still intentionally out of scope:

- Whether `EE:9201..EE:FFFF` is intentional free space, unused ROM padding, or
  data not represented by the checked-in bank configs.
- Audio-pack internals.

## Recommended next move

Run a cross-bank closure pass for the `E2-EE` audio pack run, then decide
whether to investigate the `EE` tail slack or move to any remaining configured
banks outside this range.
