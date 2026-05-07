# Bank D1 First Pass

## Main result

Bank `D1` is a pure overworld sprite graphics bank. It contains no code, no
tables, and no slack: `123` raw overworld sprite graphics payloads fill the
entire `D1:0000..D1:FFFF` bank.

Primary artifacts:

- `notes/bank-d1-asset-data-map.md`
- `notes/bank-d1-source-scaffold-handoff.md`
- `build/asset-bank-d1.json`
- `build/d1-build-candidate-ranges.json`
- `build/d1-byte-equivalence-validation.json`

The generated map accounts for:

- binary assets: `123`
- binary asset bytes: `65536`
- asset mix: `123` graphics payloads (`gfx`)
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `0`
- missing payload metadata: `0`
- source scaffold protected bytes: `65536 / 65536`
- byte-equivalence scaffold validation: `durable-scaffold`, `123` modules,
  `0` non-OK modules, `0` byte mismatches

## Bank layout

The bank is a source-order run of `overworld_sprites/gfx/*.gfx` payloads:

- first asset: `SPRITE_0000`, `D1:0000..D1:02FF`, `768` bytes.
- final asset: `SPRITE_0122`, `D1:FF00..D1:FFFF`, `256` bytes.
- the final byte of `SPRITE_0122` lands exactly on `D1:FFFF`.

Several payloads are locale-resolved through `LOCALEBINARY`, including the
Runaway Five bus frames, Pajama Ness frames, Door Surprise, and Truck 2. The
manifest resolves these through the US `earthbound.yml` entries.

## Sprite groups

The bankconfig labels group the raw payloads into overworld sprite families.
Examples in this bank include:

- `SPRITE_GROUP_NESS_BICYCLE`: `SPRITE_0000..SPRITE_0007`
- `SPRITE_GROUP_RUNAWAY_FIVE_BUS`: `SPRITE_0008..SPRITE_0010`
- `SPRITE_GROUP_CITY_BUS`: `SPRITE_0011..SPRITE_0013`
- `SPRITE_GROUP_NESS`: `SPRITE_0095..SPRITE_0103`
- `SPRITE_GROUP_ROBOT`: `SPRITE_0114..SPRITE_0121`
- `SPRITE_GROUP_CAMERA`: `SPRITE_0122`

Those group labels come from
`refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank11.asm` and
`symbols/overworld_sprites.inc.asm`; there are no pointer tables inside this
bank.

## Current D1 confidence boundary

High confidence:

- D1 is a full-bank overworld sprite graphics slab.
- Every byte from `D1:0000` through `D1:FFFF` belongs to one of the `123`
  graphics payloads.
- Locale-specific sprite payloads are resolved for the US build.
- `src/d1/bank_d1_helpers_asar.asm` protects the full bank through the reusable
  source-bank scaffold pipeline.

Still intentionally out of scope:

- This pass does not render the overworld sprite graphics.
- It does not decode sprite group animation/frame semantics beyond source-order
  labels.
- Palette and sprite placement data live outside this bank.

## Recommended next move

D1 is now closed for byte-preserving scaffold purposes. The remaining work is
optional rendering/fixture generation and friendlier grouping against overworld
sprite metadata.
