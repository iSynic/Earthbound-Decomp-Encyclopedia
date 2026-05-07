# Bank D2 First Pass

## Main result

Bank `D2` is a pure overworld sprite graphics bank. It continues the `D1`
overworld sprite payload run and contains no code, no tables, and no slack:
`231` graphics payloads fill the full bank.

Primary artifacts:

- `notes/bank-d2-asset-data-map.md`
- `notes/bank-d2-source-scaffold-handoff.md`
- `build/asset-bank-d2.json`
- `build/d2-build-candidate-ranges.json`
- `build/d2-byte-equivalence-validation.json`

The generated map accounts for:

- binary assets: `231`
- binary asset bytes: `65536`
- asset mix: `231` graphics payloads (`gfx`)
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `0`
- missing payload metadata: `0`
- source scaffold protected bytes: `65536 / 65536`
- byte-equivalence scaffold validation: `durable-scaffold`, `231` modules,
  `0` non-OK modules, `0` byte mismatches

## Bank layout

The bank is a source-order run of `overworld_sprites/gfx/*.gfx` payloads:

- first asset: `SPRITE_0123`, `D2:0000..D2:00BF`, `192` bytes.
- final asset: `SPRITE_0353`, `D2:FF80..D2:FFFF`, `128` bytes.
- the final byte of `SPRITE_0353` lands exactly on `D2:FFFF`.

Locale-resolved groups in this bank include the Saturn Valley ATM, Department
Store Mook, and Runaway Five musician sprite groups.

## Sprite groups

The source labels in
`refs/ebsrc-main/ebsrc-main/src/bankconfig/common/bank12.asm` group these
payloads into overworld sprite families. This bank includes main party member
groups such as `SPRITE_GROUP_POO`, `SPRITE_GROUP_JEFF`, and
`SPRITE_GROUP_PAULA`, plus a long run of NPC/object/enemy overworld groups.

The bank contains the raw graphics payloads only. Pointer/config data that tells
the engine which sprite group to use for a map object lives outside this bank.

## Current D2 confidence boundary

High confidence:

- D2 is a full-bank overworld sprite graphics slab.
- Every byte from `D2:0000` through `D2:FFFF` belongs to one of the `231`
  graphics payloads.
- Locale-specific sprite payloads are resolved for the US build.
- `src/d2/bank_d2_helpers_asar.asm` protects the full bank through the reusable
  source-bank scaffold pipeline.

Still intentionally out of scope:

- This pass does not render the overworld sprite graphics.
- It does not decode sprite group animation/frame semantics beyond source-order
  labels.
- Palette, sprite placement, and NPC/object config data live outside this bank.

## Recommended next move

D2 is now closed for byte-preserving scaffold purposes. The remaining work is
optional rendering/fixture generation and friendlier grouping against overworld
sprite metadata.
