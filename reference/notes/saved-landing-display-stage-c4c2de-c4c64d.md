# Saved Landing Display Stage `C4:C2DE..C8A4`

This note fills in the local visual/display helpers and saved-coordinate landing reload wrapper at `C4:C2DE..C8A4`.

The important caller chain is:

- `C0:B967 -> C4:C718`
- `C4:C718 -> C4:C2DE`
- `C4:C718 -> C4:C64D`
- `C4:C718 -> C4:C58F`
- `C4:C718 -> C4:C60E`
- `C4:C64D -> C4:C519`
- `C4:C519 -> C4:C45F`

That keeps these routines inside the saved landing/reload display seam already described by the saved-coordinate note, rather than a free-standing palette API.

## Source status

The whole `C4:C2DE..C4:C8A4` island is now promoted to the durable C4 source
scaffold as `src/c4/saved_landing_display_stage_helpers.asm`.

Validation:

- `tools/validate_source_bank_byte_equivalence.py --bank C4 --module saved_landing_display_stage --strict`
- `tools/validate_source_bank_byte_equivalence.py --bank C4 --module all --combined --scaffold src/c4/bank_c4_helpers_asar.asm --strict`

Both validations report `0` mismatches.

## Display setup helper

`C4:C2DE` is the setup side of the landing display stage.

Locally it:

- performs a one-time branch when `$4DC4 == 0`, including selector `#$07` through `C4:FBBD` and `C0:8814`
- clears `$4472`, `$4474`, and `$9F2A`
- calls transfer/setup helpers `C0:8D79`, `C0:8D9E`, and `C0:8E1C`
- decompresses asset blocks through `C4:1A9E` from `E1:CFAF`, `E1:D5E8`, and `E1:D4F4`
- sends resulting buffers through `C0:8616`, `C0:8ED2`, and `C0:8EFC`
- calls visible display/landing helpers including `C2:00D9`, `C4:7C3F`, `C4:4963`, and `C4:7F87`
- sets display state byte `$001A = #$05`
- clears `$4DC4`, `$0037`, `$0035`, and `$0031`
- finishes through `C0:886C` and `C0:888B`

The safest current local name is a saved-landing display initializer. It is larger than a palette-only helper and smaller than the whole saved-coordinate reload path.

Source polish: `src/c4/saved_landing_display_stage_helpers.asm` now names
the one-time init latch, stage cursor/scratch latches, saved map selector byte,
E1 graphics/arrangement/palette asset pointers, BG setup values, VRAM
transfer destinations/sizes, palette staging offsets, intro display-state byte,
and the initial transition arguments used by `C4:C2DE`.

## Palette staging helper

`C4:C45F` stages a 0xC0-byte landing palette work region around `$7F:7800`.

It:

- clears/copies a 0xC0-byte block at `$7F:7800`
- uses caller A as a stage index
- copies 0x20-byte slices between `$0240`, `$02C0`, `$02E0`, and `$7F:7800 + stage * 0x20`

Source polish: the source now names the `$7F:7800` stage buffer, source/stage
destination offsets, `0xC0` staging byte count, and `0x20` slice width.

`C4:C519` wraps this staging step into a timed fade phase:

- caller A selects the stage passed to `C4:C45F`
- caller X supplies the frame count
- it calls `C4:9208` to build the interpolation planes from `$7F:7800`
- each frame checks `$006D` and aborts with `#$FFFF` if it is nonzero
- otherwise it steps `C4:92D2`, waits a frame through `C0:8756`, and decrements the frame counter
- after the phase completes, it copies `$7F:7800` back over the 0xC0-byte `$0240` palette work region

`C4:C567` is the smaller wait-loop version of the same abort contract: it waits caller A frames through `C0:8756`, returning `#$FFFF` if `$006D` becomes nonzero.

Source polish: the source now names the `$006D` abort latch, success/abort
return sentinels, phase staging buffer copy-back arguments, and the shared
wait-loop return contract used by `C4:C519` and `C4:C567`.

## Sequence runner

`C4:C64D` chains the landing fade phases used by `C4:C718`:

- waits 0x3C frames through `C4:C567`
- runs a short event/text gate around `C1:86B1`, `C1:DD5F`, and `C2:1628`
- runs `C4:C519` with stages `1`, `2`, `3`, then `4`
- uses 0x5A-frame phases for the first three stages and an 0x08-frame phase for stage 4
- returns nonzero/abort when the wait or fade helpers report interruption

This makes `C4:C64D` the saved-landing fade sequence runner that follows the display setup done by `C4:C2DE`.

Source polish: the fade sequence now names the long pause duration, text/event
gate pointer inputs, long/short phase frame counts, stage ids `1..4`, and the
success return used on interruption after the event gate.

## Post-sequence palette restores

`C4:C58F` is the post-saved-landing palette fade used by `C4:C718` after `C4:C64D` reports success.

Input:

- `A` = frame count

It stages a full-scale palette target from `$7E:0200` through `C4:954C(0x64)`, initializes the landing interpolation planes from `0x0200` through `C4:96E7`, steps `C4:26ED` once per frame with `C0:8756`, then commits the resulting `$0200` palette block through `C0:8EFC`, queues selector `0x18` through `C0:856B`, and waits one more frame.

Source polish: `C4:C58F` now names the `$7E:0200` restore source, `0x64`
scale step, no-source fade index, first-frame counter, CGRAM commit fill/offset,
and restore wait duration; `C4:C60E` shares the named no-source and first-frame
fade counters.

The direct caller is `C4:C752`, immediately after the saved-landing fade sequence returns zero. That makes this the success-side palette restore/settle phase before the broader saved-coordinate reload path resumes world setup.

`C4:C60E` is the matching palette fade with world/display refresh work interleaved. It also takes caller `A` as a frame count, initializes from `0x0200` through `C4:96E7`, then for each frame:

- steps `C4:26ED`
- runs `C0:88B1`
- calls `C0:9466`
- calls `C0:8B26`
- waits one frame through `C0:8756`

After the loop it exports the finished palette through `C4:9740`.

The direct caller is `C4:C89C`, near the tail of the heavy saved-coordinate reload path after object/state cleanup, `C0:64D4`, `C0:6B21`, `C0:88B1`, and `C0:9451`. So `C4:C60E` is the late palette fade that keeps the world/display refresh path alive while the landing palette settles.

## Saved-coordinate landing reload wrapper

`C4:C718` is the wrapper called from `C0:B967`. It snapshots the current saved
coordinates through `C0:943C`, runs the display initializer at `C4:C2DE`, then
runs the fade sequence at `C4:C64D`.

If the sequence aborts, it switches display transition mode `2`, restores the
saved coordinate state through `C0:9451`, and returns the abort result. On the
success path, it runs the restore fade at `C4:C58F`, queues selector `2` through
`C0:AC0C`, updates display state `$001A = #$17`, clears several entity/map
latches, rebuilds party/entity state around the saved coordinate record, clears
30 entries at `$289E`, runs post-transition cleanup (`C0:64D4`, `C0:6B21`,
`C0:88B1`, `C0:9451`), and finishes with the world-refresh fade at `C4:C60E`.

Source polish: `src/c4/saved_landing_display_stage_helpers.asm` now names the
saved coordinate snapshot pair, abort transition arguments, success-side restore
fade and sound/counter ids, return-to-world display state, invalid latch values,
map-selector record stride/base and cleanup fields, object-chain pointer update,
event-flag loop bounds, `$289E` live-slot reset table, and final world-refresh
fade frame count.

## Working Names

- `C4:9208` = `BuildLandingInterpolationPlanesFrom7f7800`
- `C4:C2DE` = `InitializeSavedLandingDisplayState`
- `C4:C45F` = `StageLandingPalettePhaseBlock`
- `C4:C519` = `RunLandingPalettePhaseFadeFrames`
- `C4:C567` = `WaitFramesAbortOnInput006d`
- `C4:C58F` = `RunSavedLandingPaletteRestoreFadeFrames`
- `C4:C60E` = `RunSavedLandingPaletteWorldRefreshFadeFrames`
- `C4:C64D` = `RunSavedLandingFadeSequence`
- `C4:C718` = `RunSavedCoordinateLandingReload`

## Confidence boundaries

### Locally proved

- `C4:C2DE` is called by `C4:C718` immediately after saved coordinates are applied through `C0:943C`.
- `C4:C45F` is called only by `C4:C519` locally.
- `C4:C519` is called four times by `C4:C64D` with stage values `1..4`.
- `C4:C519` and `C4:C567` share the same `$006D` abort contract.
- `C4:9208` builds the landing interpolation planes consumed by `C4:92D2`.
- `C4:C58F` and `C4:C60E` are both called from `C4:C718` with `A = 0x20`; the first runs immediately after `C4:C64D` success, while the second runs at the end of the heavier reload path.
- `C4:C718` is the only direct caller of `C4:C2DE`, `C4:C64D`, `C4:C58F`, and `C4:C60E` in this local landing/reload seam.

### Still open

- the exact player-visible identity of `$006D` in this abort path
- the final semantic split between saved-coordinate reload, landing fade, and post-landing world setup
- whether `$4DC4` is best named as a one-time landing-display initialization latch or as part of a broader display-mode family
- the exact final names for `C0:9466` and the surrounding late-refresh C0 helpers
