# Bank D4 First Pass

## Main result

Bank `D4` is a pure overworld sprite graphics bank. It continues the
`D1` through `D3` overworld sprite payload run and contains no code, no tables,
and no slack: `335` graphics payloads fill the full bank.

Primary artifacts:

- `notes/bank-d4-asset-data-map.md`
- `notes/bank-d4-source-scaffold-handoff.md`
- `build/asset-bank-d4.json`
- `build/d4-build-candidate-ranges.json`
- `build/d4-byte-equivalence-validation.json`

The generated map accounts for:

- binary assets: `335`
- binary asset bytes: `65536`
- asset mix: `335` graphics payloads (`gfx`)
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `0`
- missing payload metadata: `0`
- source scaffold protected bytes: `65536 / 65536`
- byte-equivalence scaffold validation: `durable-scaffold`, `335` modules,
  `0` non-OK modules, `0` byte mismatches

## Bank layout

The bank is a source-order run of `overworld_sprites/gfx/*.gfx` payloads:

- first asset: `SPRITE_0693`, `D4:0000..D4:00BF`, `192` bytes.
- final asset: `SPRITE_1027`, `D4:FF80..D4:FFFF`, `128` bytes.
- the final byte of `SPRITE_1027` lands exactly on `D4:FFFF`.

The bank starts with `OVERWORLD_SPRITES_BANK4` and includes sprite groups such
as `SPRITE_GROUP_RICH_POKEY`, `SPRITE_GROUP_BUBBLE_MONKEY`,
`SPRITE_GROUP_PICKY`, `SPRITE_GROUP_POKEY`, `SPRITE_GROUP_FLYING_MAN`, ghosted
party member groups, and a later run of small/lil and climbing sprite groups.

## Current D4 confidence boundary

High confidence:

- D4 is a full-bank overworld sprite graphics slab.
- Every byte from `D4:0000` through `D4:FFFF` belongs to one of the `335`
  graphics payloads.
- Locale-specific sprite payloads are resolved for the US build.
- `src/d4/bank_d4_helpers_asar.asm` protects the full bank through the reusable
  source-bank scaffold pipeline.

Still intentionally out of scope:

- This pass does not render the overworld sprite graphics.
- It does not decode sprite group animation/frame semantics beyond source-order
  labels.
- Palette, sprite placement, and NPC/object config data live outside this bank.

## Recommended next move

D4 is now closed for byte-preserving scaffold purposes. The remaining work is
optional rendering/fixture generation and friendlier grouping against overworld
sprite metadata.
