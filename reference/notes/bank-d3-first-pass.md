# Bank D3 First Pass

## Main result

Bank `D3` is a pure overworld sprite graphics bank. It continues the
`D1`/`D2` overworld sprite payload run and contains no code, no tables, and no
slack: `339` graphics payloads fill the full bank.

Primary artifacts:

- `notes/bank-d3-asset-data-map.md`
- `notes/bank-d3-source-scaffold-handoff.md`
- `build/asset-bank-d3.json`
- `build/d3-build-candidate-ranges.json`
- `build/d3-byte-equivalence-validation.json`

The generated map accounts for:

- binary assets: `339`
- binary asset bytes: `65536`
- asset mix: `339` graphics payloads (`gfx`)
- table includes: `0`
- table bytes: `0`
- coverage gap bytes: `0`
- missing payload metadata: `0`
- source scaffold protected bytes: `65536 / 65536`
- byte-equivalence scaffold validation: `durable-scaffold`, `339` modules,
  `0` non-OK modules, `0` byte mismatches

## Bank layout

The bank is a source-order run of `overworld_sprites/gfx/*.gfx` payloads:

- first asset: `SPRITE_0354`, `D3:0000..D3:00BF`, `192` bytes.
- final asset: `SPRITE_0692`, `D3:FF80..D3:FFFF`, `128` bytes.
- the final byte of `SPRITE_0692` lands exactly on `D3:FFFF`.

The bank starts with an `OVERWORLD_SPRITES_BANK3` label, then later resumes
explicit sprite group labels such as `SPRITE_GROUP_LADY_IN_VEIL`,
`SPRITE_GROUP_SHIP_CREWMAN`, `SPRITE_GROUP_CAPTAIN_STRONG`, and many generic
NPC/person groups.

## Current D3 confidence boundary

High confidence:

- D3 is a full-bank overworld sprite graphics slab.
- Every byte from `D3:0000` through `D3:FFFF` belongs to one of the `339`
  graphics payloads.
- Locale-specific sprite payloads are resolved for the US build.
- `src/d3/bank_d3_helpers_asar.asm` protects the full bank through the reusable
  source-bank scaffold pipeline.

Still intentionally out of scope:

- This pass does not render the overworld sprite graphics.
- It does not decode sprite group animation/frame semantics beyond source-order
  labels.
- Palette, sprite placement, and NPC/object config data live outside this bank.

## Recommended next move

D3 is now closed for byte-preserving scaffold purposes. The remaining work is
optional rendering/fixture generation and friendlier grouping against overworld
sprite metadata.
