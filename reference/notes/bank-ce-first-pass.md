# Bank CE First Pass

## Main result

Bank `CE` is a mixed battle/swirls/Sound Stone asset-data bank. It continues the
battle-sprite payload run from `CD`, then adds the battle sprite pointer table,
battle sprite palettes, swirl animation data and pointers, Sound Stone graphics
and palette data, and one US retail audio pack.

Follow-up source-scaffold status:

- durable scaffold: `src/ce/bank_ce_helpers_asar.asm`
- manifest: `build/ce-build-candidate-ranges.json`
- handoff: `notes/bank-ce-source-scaffold-handoff.md`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `220`
- byte-equivalence: `OK`, `0` mismatches

Primary artifacts:

- `notes/bank-ce-asset-data-map.md`
- `build/asset-bank-ce.json`

The generated map accounts for:

- binary assets: `216`
- binary asset bytes: `64620`
- asset mix: `56` graphics payloads (`gfx`), `33` palettes (`pal`), `126` swirl
  payloads (`swirl`), and `1` audio pack (`ebm`)
- table includes: `3`
- table bytes: `830`
- coverage gap bytes: `86`
- missing payload metadata: `0`

## Tooling improvements from this pass

`tools/build_asset_bank_manifest.py` now resolves root-level payloads with an
empty `earthbound.yml` subdir, needed for `sound_stone.pal` at `CE:F806`.

## Bank layout

The high-level CE layout is:

- `CE:0000..CE:62ED`: `55` compressed battle sprite graphics payloads,
  `BATTLE_SPRITE_82` through `BATTLE_SPRITE_89` in source order.
- `CE:62EE..CE:6513`: `data/battle/battle_sprites_pointers.asm`, `550` bytes.
- `CE:6514..CE:6913`: `32` battle sprite palettes, `32` bytes each.
- `CE:6914..CE:DC44`: `126` swirl data payloads, `SWIRL_DATA_0` through
  `SWIRL_DATA_125`.
- `CE:DC45..CE:DD40`: `data/battle/swirl_pointers.asm`, `252` bytes.
- `CE:DD41..CE:DD5C`: inline `SWIRL_PRIMARY_TABLE`, `28` bytes.
- `CE:DD5D..CE:F805`: `SOUND_STONE_GFX`, `6825` bytes.
- `CE:F806..CE:F8C5`: `SOUND_STONE_PALETTE`, `192` bytes.
- `CE:F8C6..CE:FFA9`: retail `AUDIO_PACK_102`, `1764` bytes.
- `CE:FFAA..CE:FFFF`: `86` bytes of tail slack.

## Battle sprites

CE contributes the remaining `55` compressed battle sprite graphics payloads and
the canonical battle sprite pointer table:

- `data/battle/battle_sprites_pointers.asm`: `CE:62EE..CE:6513`, `550` bytes.
- The table is `110` entries by structure: each entry is a 24-bit sprite payload
  pointer plus a one-byte `BATTLE_SPRITE_SIZE` value.

This matches the runtime behavior documented in the CD pass:
`LOAD_BATTLE_SPRITE` indexes `BATTLE_SPRITES_POINTERS` as five-byte records,
uses the fifth byte as the size/shape code, then decompresses the selected
payload.

The `32` battle sprite palettes occupy `CE:6514..CE:6913`, one `32`-byte SNES
palette per asset.

## Swirl data

CE also carries the battle transition swirl data:

- `SWIRL_DATA_0`: starts at `CE:6914`.
- `SWIRL_DATA_125`: ends at `CE:DC44`.
- `SWIRL_POINTER_TABLE`: `CE:DC45..CE:DD40`, `126` little-endian word entries.

The source table uses `.LOWORD(SWIRL_DATA_n)` entries, so the swirl payloads and
pointer table are local to this bank.

`SWIRL_PRIMARY_TABLE` in the bank config is an inline `.BYTE` block immediately
after the pointer include. The manifest now accounts for it as
`inline:SWIRL_PRIMARY_TABLE`, so the only remaining CE coverage gap is the final
tail slack.

## Sound Stone and audio

The Sound Stone assets are:

- `SOUND_STONE_GFX`: `CE:DD5D..CE:F805`, locale-resolved compressed graphics.
- `SOUND_STONE_PALETTE`: `CE:F806..CE:F8C5`, `192` bytes.

The US retail conditional then inserts:

- `AUDIO_PACK_102`: `CE:F8C6..CE:FFA9`, `1764` bytes.

The final `86` bytes at `CE:FFAA..CE:FFFF` are tail slack.

## Current CE confidence boundary

High confidence:

- CE is mixed data/assets, not executable code.
- All binary payloads now resolve through `earthbound.yml`, including the
  root-level Sound Stone palette.
- The battle sprite pointer table and swirl pointer table have direct source
  corroboration and exact byte counts.
- The inline `SWIRL_PRIMARY_TABLE` is source-correlated and manifest-accounted.

Still intentionally out of scope:

- This pass does not render battle sprites, swirls, or the Sound Stone graphic.
- It does not decode the internal swirl payload format.
- It does not interpret audio-pack internals.
- Inline bank-config `.BYTE/.WORD/.DWORD` accounting is intentionally basic; it
  records byte spans, not semantic fields.

## Recommended next move

Treat CE as structurally complete and byte-protected for the current
bank-coverage phase. Proceed to `CF`; if it continues the asset/data trend, the
manifest and promotion tools now handle the major patterns seen from `CA`
through `CE`.
