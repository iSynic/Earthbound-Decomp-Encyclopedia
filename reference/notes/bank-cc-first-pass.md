# Bank CC First Pass

## Main result

Bank `CC` is an animation/PSI asset bank. It is not a text bank and does not
appear to contain executable routines; its contents are compressed animation
payloads, PSI animation payloads, palette data, generated pointer/config tables,
and one retail audio pack.

Follow-up source-scaffold status:

- durable scaffold: `src/cc/bank_cc_helpers_asar.asm`
- manifest: `build/cc-build-candidate-ranges.json`
- handoff: `notes/bank-cc-source-scaffold-handoff.md`
- protected bytes: `65536 / 65536`
- residual bytes: `0`
- modules: `83`
- byte-equivalence: `OK`, `0` mismatches

Primary artifacts:

- `notes/bank-cc-asset-data-map.md`
- `build/asset-bank-cc.json`

The generated map accounts for:

- binary assets: `79`
- binary asset bytes: `64899`
- asset mix: `6` animation payloads (`anim`), `34` PSI arrangements (`arr`),
  `4` PSI graphics sets (`gfx`), `34` PSI palettes (`pal`), and `1` audio pack
  (`ebm`)
- table includes: `3`
- table bytes: `600`
- coverage gap bytes: `37`
- missing payload metadata: `0`

## Tooling improvements from this pass

`tools/build_asset_bank_manifest.py` now handles patterns that first appear or
matter in CC:

- US retail conditional assembly for `.IF .DEFINED(...)`, `.ELSE`, and `.ENDIF`
  blocks, including simple `||` and `&&` expressions.
- `LOCALEBINARY`, resolved against `US/...` entries in `earthbound.yml`.
- Generated table includes that are referenced by the bank config but absent
  from `src/data`; these are assigned spans by measuring from the current source
  cursor to the next known asset.

These fixes prevent the tool from counting prototype-only `AUDIO_PACK_141`,
ensure `ANIMATIONDATA_THE_END` resolves to the US asset at `CC:2CE1`, and keep
conditional tables from overcounting both retail and prototype branches.

## Bank layout

The high-level CC layout is:

- `CC:0000..CC:2DE0`: six compressed animation payloads.
- `CC:2DE1..CC:2E18`: `ANIMATION_SEQUENCE_POINTERS`, retail table size `56`.
- `CC:2E19..CC:F04C`: compressed PSI arrangements and PSI graphics sets.
- `CC:F04D..CC:F1E4`: inferred generated `data/psi_anim_cfg.asm` span, `408`
  bytes.
- `CC:F1E5..CC:F58E`: remaining PSI arrangements plus `34` eight-byte PSI
  palettes.
- `CC:F58F..CC:F616`: inferred generated `data/psi_anim_pointers.asm` span,
  `136` bytes.
- `CC:F617..CC:FFDA`: retail `AUDIO_PACK_71`, `2500` bytes.
- `CC:FFDB..CC:FFFF`: `37` bytes of tail slack.

## Animation payloads

The six top-of-bank animation payloads are:

- `ANIMATIONDATA_CARPAINTER_LIGHTNING_REFLECT`: `CC:0000..CC:17CA`, `6091`
  bytes.
- `ANIMATIONDATA_CARPAINTER_LIGHTNING_STRIKE`: `CC:17CB..CC:1F5B`, `1937`
  bytes.
- `ANIMATIONDATA_STARMAN_JR_TELEPORT`: `CC:1F5C..CC:22D7`, `892` bytes.
- `ANIMATIONDATA_BOOM`: `CC:22D8..CC:2C88`, `2481` bytes.
- `ANIMATIONDATA_ZOMBIES`: `CC:2C89..CC:2CE0`, `88` bytes.
- `ANIMATIONDATA_THE_END`: `CC:2CE1..CC:2DE0`, `256` bytes.

`refs/ebsrc-main/ebsrc-main/src/data/animation_sequence_pointers.asm`
corroborates these as the animation-sequence pointer targets. The table has a
retail branch for `ANIMATIONDATA_THE_END`, so the US retail table occupies
`56` bytes rather than the `64` bytes that would result from counting both
conditional branches.

## PSI animation data

The PSI block is anchored by `show_psi_animation.asm` references to:

- `PSI_ANIM_GFX_SET_1`
- `PSI_ANIM_CFG`
- `PSI_ANIM_PALETTES`
- `PSI_ANIM_POINTERS`

CC holds all four compressed PSI graphics sets, `34` compressed arrangement
payloads, `34` eight-byte palette entries, and two generated tables:

- `data/psi_anim_cfg.asm`: inferred `CC:F04D..CC:F1E4`, `408` bytes.
- `data/psi_anim_pointers.asm`: inferred `CC:F58F..CC:F616`, `136` bytes.

Those two source files are referenced by the ebsrc bank config but are not
present in the checked-in `src/data` directory, so the manifest treats their
sizes as layout contracts inferred from surrounding asset offsets.

## Audio tail

The final active payload is retail `AUDIO_PACK_71`:

- `AUDIO_PACK_71`: `CC:F617..CC:FFDA`, `2500` bytes.

The prototype branch would insert `AUDIO_PACK_141`, but the US retail condition
selects `AUDIO_PACK_71` only. The remaining `CC:FFDB..CC:FFFF` tail is `37`
bytes.

## Current CC confidence boundary

High confidence:

- CC's bank-level role is animation/PSI assets plus generated pointer/config
  tables and a retail audio pack.
- All binary payload spans are pinned from `earthbound.yml` and sampled from the
  local ROM.
- Locale and conditional assembly behavior is now modeled well enough for the US
  retail bank layout.
- The two absent generated PSI tables are bounded by neighboring asset offsets.

Still intentionally out of scope:

- This pass does not decompress or render animation/PSI payloads.
- It does not interpret the internal PSI arrangement format.
- It does not decode the audio-pack internals.
- The inferred generated tables need semantic field names from `show_psi_animation`
  and related runtime code before they can become source-level structs.

## Recommended next move

Treat CC as structurally complete and byte-protected for the current
bank-coverage phase. Proceed to `CD` with the asset-bank manifest path first.
The tool now covers the major source patterns needed for the next asset-heavy
banks: nested bank configs, normal binaries, locale binaries, conditional
retail/prototype branches, generated table spans, inserted audio packs, and
unlabeled payload fallback naming.
