# Title Screen Logo And Palette Event Helpers (`C0:EBE0-C0:EE53`)

This tail sits immediately after `TELEPORT_MAINLOOP` and before the reference-named intro logo loader. It is mostly title-screen asset loading and event-script palette helpers.

Reference corroboration:

- `refs/earthbound-disasm-legacy/Earthbound Decomp/EB/Routine_Macros_EB.asm` labels the assets touched here as `TitleLogoGFX1`, `TitleLogoTilemap`, `TitleLogoGFX2`, `TitleScreenLetterPalettes`, `TitleScreenGlowPalettes`, and `TitleScreenBGPalettes`.
- `refs/ebsrc-main/ebsrc-main/include/eventmacros.asm` exposes event macros for `UNKNOWN_C0EC77`, `UNKNOWN_C0ECB7`, `UNKNOWN_C0ED14`, `UNKNOWN_C0ED39`, `UNKNOWN_C0ED5C`, `UNKNOWN_C0EDD1`, `UNKNOWN_C0EDDA`, `UNKNOWN_C0EE47`, and `UNKNOWN_C0EE53`.
- `refs/ebsrc-main/ebsrc-main/src/data/events/C42235.asm` and `scripts/789.asm` show the normal title flow: load palettes with `C0:EC77`, repeatedly advance frames with `C0:EDDA`, load the title-screen background palettes with `C0:ECB7`, then set `$9641=2` through `C0:EDD1`; the quick/skip path calls `C0:ED5C`.

## Logo Graphics Load

`C0:EBE0` decompresses the title logo graphics and tilemap bundle into work RAM and transfers it to VRAM:

- Decompresses `TitleLogoGFX1` to `$7F:0000`, then copies `$B000` bytes to VRAM destination `$0000` through `C0:8616`.
- Decompresses `TitleLogoTilemap` to the same buffer, then copies `$1000` bytes to VRAM destination `$5800`.
- Decompresses `TitleLogoGFX2`, then copies `$4000` bytes to VRAM destination `$6000`.

The routine uses `C4:1A9E` for decompression and `C0:8616` for the VRAM-facing transfer. The repeated `$06/$08` pair is the staging pointer `$7F:0000`.

## Palette Loaders

`C0:EC77` selects between two compressed title-screen palette blobs based on its `A` argument. `A=0` loads `TitleScreenLetterPalettes`; nonzero loads `TitleScreenGlowPalettes`. Both decompress to `$7F:0000`.

`C0:ECB7` loads the normal title-screen background palette set. It clears `$0030`, decompresses `TitleScreenBGPalettes` to a `$0200` staging buffer, calls `C4:96F9`, clears `$0E`, calls `C0:8EFC` with `A=$0200, X=$0100`, then calls `C4:96E7` with `A=$00A5, X=$00FF`. It finishes by writing `$18` to `$0030`. In the event flow this happens after the animated title letters finish.

`C0:ED14` and `C0:ED39` are short palette fill/install wrappers. Both call `C0:8EFC` with `A=$0200, X=$0100`, then write `$18` to `$0030`; `C0:ED14` passes byte `$0E=FF`, while `C0:ED39` passes `$0E=00`. In `C4220E.asm`, they bracket a two-frame pause, which matches a quick flash/clear transition.

`C0:ED5C` is explicitly called by `EVENT_789` when the title animation is skipped. It performs the `TitleScreenBGPalettes` load, calls `C0:EC77(0)`, copies `$20` bytes from `$7F:01A0` to `$0300`, calls `C0:EC77(1)`, copies `$20` bytes from `$7F:0260` to `$02E0`, then writes `$18` to `$0030`. This builds the final palette state directly instead of playing the full letter/glow sequence.

## Event State Helpers

`C0:EDD1` is a one-word state latch: it stores `2` into `$9641` and returns. In `C42235.asm`, this comes after the title-screen animation and a long pause, so `$9641` is likely a title/control state consumed by the surrounding intro script.

`C0:EDDA` advances the title-screen palette/tile frame for the current event task. It reads the current slot from `$1A42`, uses `$0E5E[current]` as the current frame index, `$0E9A[current]` as a source selector, and `$0ED6[current]` as a frame count. It copies `$20` bytes from `$7F:0000 + frame*$20` into `$0200 + selector*$20` through `C0:8ED2`, increments `$0E5E[current]`, wraps it to zero when it reaches `$0ED6[current]`, then sets `$0030=18`.

`C0:EE47` stores byte `$13` into `$001A`. This is exposed as an event macro and appears near intro-logo event scripts; by neighboring code, `$001A` is a screen/display mode latch.

`C0:EE53` clears bit `#$8000` in `$116A[current]`, where `current` is `$1A42`. `C4220E.asm` calls it immediately after setting an animation pointer, draw callback, priority, and position-change callback, so this is a per-entity flag clear used to make the intro/title object render or update normally.

## Working Names

- `C0:EBE0` = `Load_TitleLogoGraphicsAndTilemap`
- `C0:EC77` = `Load_TitleScreenLetterOrGlowPalettes`
- `C0:ECB7` = `Load_TitleScreenBackgroundPalettes`
- `C0:ED14` = `Install_TitlePaletteFillFF`
- `C0:ED39` = `Install_TitlePaletteFill00`
- `C0:ED5C` = `Build_TitleScreenSkippedAnimationPaletteState`
- `C0:EDD1` = `Set_TitleScreenControlState2`
- `C0:EDDA` = `Advance_TitleScreenPaletteFrame`
- `C0:EE47` = `Set_DisplayMode13`
- `C0:EE53` = `Clear_CurrentTitleObjectHiddenFlag`
