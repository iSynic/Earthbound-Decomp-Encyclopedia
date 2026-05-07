# Landing And Coffee Tea Visual Helpers `C4:92D2-C4:9FE0`

## Scope

This note promotes the caller-dense unknown-code cluster after
`initialize_map_palette_fade.asm` and before the named `coffee_tea_scene.asm`
include. The cluster is not one subsystem. It is a shared visual-helper run:

- `C4:92D2-C4:981F` extends the landing/display palette and template machinery
  already described in the landing profile notes.
- `C4:9841-C4:9D1E` prepares and drives the coffee/tea or flyover-style
  screen transition helpers that are consumed by the named `COFFEETEA_SCENE`
  interpreter just after this cluster.
- `C4:9EA4-C4:9FE0` is the sibling flyover/intro text scene runner. It shares
  the coffee/tea tile-buffer helpers, but selects scripts through the
  `FLYOVER_TEXT_POINTERS` table and runs a fixed cleanup/fade tail.

The ebsrc order, existing landing notes, and direct callers are the main
corroboration. The coffee/tea side is also corroborated by the named
`text/coffee_tea_scene.asm` include at `C4:9D6A`, which dispatches through the
helpers promoted here. The flyover side is corroborated by the named
`data/text/flyover_text_pointers.asm` include immediately before `C4:9EC4` and
by the legacy comments for the `Year199X`, `Onett`, and `NessHouse` strings.

## Landing palette and display helpers

`C4:92D2` steps the parallel `7F:7900..7E00` color-work family described in the
landing palette note. It adds the three delta planes into the current component
planes, repacks the result into the `0x0240` work block, loops for `0x60`
entries, and queues selector `#$08`.

`C4:939C` is a landing-profile display orchestrator. It resolves an
`EF:10FB` profile pointer from caller A, applies an optional copy-through path
through `$7F:7800`, repeatedly waits a frame and calls `C4:92D2`, restores the
selected `0x0240` template, copies a `C3:0000` source block to `0x0300`, runs
the landing row/template builders at `C0:0480` and `C0:0778`, and queues
selector `#$18`.

Source polish: `src/c4/nearby_truffle_and_landing_profile_interpolation_helpers.asm`
now names the parallel `$7F:7900..7E00` component delta/base planes, the
`0x0240` template buffer, RGB555 component masks and high-channel normalize
denominator, `EF:10FB` profile descriptor table, profile row stride, static
`C3:0000 -> 0x0300` transfer block, display cache latch, wait selectors, and
transfer-busy byte.

`C4:9496` converts one packed RGB555 color word through the C0 fixed-point
helpers. The caller supplies a step or scale in X; the routine extracts low,
middle, and high 5-bit color components, scales each component, clamps overflow
to `#$1F00`, and repacks the color.

`C4:954C` applies `C4:9496` across `0x100` source words and writes the scaled
palette block to `$7F:0000`.

`C4:958E`, `C4:96E7`, `C4:96F0`, `C4:96F9`, `C4:9740`, and `C4:978E` are the
same palette-family surface already pinned in the landing palette note:

- `C4:958E` builds the six `7F:0200..0C00` interpolation planes.
- `C4:96E7` calls that builder with source base `0x0200`.
- `C4:96F0` calls it with source base `$4476`.
- `C4:96F9` mirrors the `7E:0200` CGRAM shadow to `$7F:0000`.
- `C4:9740` performs that mirror and queues the direct CGRAM upload selector.
- `C4:978E` copies the `7E:0200` palette shadow into `$4476`.

`C4:97C0` ties the landing palette pieces together: it builds a scaled palette
block into `$7F:0000`, initializes the six-plane interpolation state from
`0x0200`, steps `C4:26ED` for the requested number of frames with frame waits,
then exports and queues the palette upload through `C4:9740`.

Source polish: `src/c4/landing_palette_display_helpers.asm` now names the
full-scale `#$0032` RGB555 step, repack byte masks, high-component normalize
denominator, WRAM-low bank selector, palette first-word/fade sentinels, and the
existing-work selector bit used by `C4:958E`.

2026-05-06 landing palette polish: `landing_palette_display_helpers.asm` now
documents the side effects of the scale/build/export lane rather than only
listing working names. `C4:954C` is bounded as the `$7F:0000` scaled palette
builder, `C4:958E` as the six-plane `$7F:0200..0C00` initializer, `C4:96F9` as
the `$0200 -> $7F:0000` staging mirror, `C4:9740` as the `$7F:0000 -> $0200`
export plus selector `#$18` queue, and `C4:97C0` as the full fade driver. The
parallel `nearby_truffle_and_landing_profile_interpolation_helpers.asm` comments
now similarly mark `C4:92D2` as the `$7F:7900..7E00 -> $0240` frame stepper and
`C4:939C` as the descriptor-driven landing display/template orchestrator. The
visible CGRAM upload claim remains limited to the `$0200` shadow plus selector
`#$18`; the `$7F:0000` copy is still treated as C4 staging/backup work.

2026-05-06 landing palette copy-size follow-up: the same source now gives the
`$0200` CGRAM-shadow address and `$0200` copy byte count separate names in the
mirror/export helpers. The fade driver comment also documents the count-`1`
immediate-export case and the duplicate selector `#$18` write after `C4:9740`,
leaving the C0 display-selector semantics callee-owned.

2026-05-06 landing profile source follow-up: the adjacent
`nearby_truffle_and_landing_profile_interpolation_helpers.asm` source now names
the local landing-plane builder and stepper loop labels, marks
`C4:9208` as a `$7F:7900..7E00` plane initializer with no visible transfer by
itself, and keeps `C4:92D2` bounded to the 7F component planes, `$0240`
template repack, and selector-wait call surface. The `C4:939C` descriptor
runner now explicitly separates C4-owned EF:10FB row selection and 7F/$0240
staging from the C0 transfer, display-row, tilemap, and busy-byte callees.

`C4:0BE8` is the shared blank source block immediately after the footstep sound
table. The ROM bytes from `C4:0BE8..0DE7` are all zero, and the next named data
family begins at `C4:0DE8`. Multiple setup paths use this as a fixed bank-`C4`
source for clearing or seeding graphics/tile memory.

`C4:981F` copies that static `C4:0BE8` data block to `$7C00`. It is grouped with
the visual setup helpers because the downstream coffee/tea init path consumes
`$7C00` as a source for a VRAM/tile-buffer transfer.

## Coffee tea and flyover visual helpers

`C4:9841` starts battle-background visual state with `C2:EA15(1)`. The C2 note
names that callee as `BeginBattleBgVisualState`; here it functions as a small
visual-mode wrapper for the coffee/tea transition family.

`C4:984B` inverts `0x0340` words starting at `$3492`. The only direct caller is
`C4:9B6E`, so this is best treated as a tile-buffer preconditioning helper.

`C4:9875` applies an 8-row byte mask into the destination tile buffer. Its
callers set up `$3492` as the destination and feed it source bytes, row counts,
and stride-like values; the routine uses C0 bit-scaling helpers to AND generated
masks into paired destination bytes. In this helper family it advances the
row-pixel/base cursors as masks cross tile rows, but `$3C1E/$3C20` are only
initialized/reset by the surrounding init/upload helpers.

`C4:999B` draws or composites a token-driven run into the `$3492` tile buffer.
It indexes data rooted at `$C3:F054`, maps the incoming token through table
metadata, and repeatedly delegates to `C4:9875` for 8-row chunks.

`C4:9A4B` is a one-frame visual wait helper that waits through `C0:8756` and
then updates the battle-background visual state through `C2:DB3F`.

`C4:9A56` initializes the coffee/tea tile-buffer and transfer state. It clears
or stages `$7F:0000`, transfers `$7C00` toward VRAM destination `$6000`, queues
or copies the `$3492` tile data into the `$7DFE`/`$7E00` buffer family, seeds
tile IDs starting near `#$2000`, clears `$3C14/$3C16/$9F2F/$9F31`, and enters
the C0 visual transfer bracket.

`C4:9B6E` uploads or slides a window of the `$3492` tile buffer according to
the current `$9F2D` position. It clips transfers at the `$3400` boundary,
computes source/destination spans around `$6150`, clears `$3C1E/$3C20`, and
waits a frame.

`C4:9C56` advances the coffee/tea tile-scroll state. It accumulates caller A
into `$3C16`, derives the next `$9F2D` position, wraps at `#$20`, commits the
`$3492` tile block through `C0:8EFC` on each call, keeps only the pixel
remainder in `$3C16`, and resets `$9F2F/$9F31`.

`C4:9CA8` advances the 8-pixel row cursor stored at `$9F2F/$9F31`. It adds
caller A plus 8, stores the raw position, then aligns the derived row base to a
16-byte boundary.

`C4:9CC3` reads up to five token bytes from a compact table and dispatches
token values below `#$50` through `C4:999B`. It is the small token-string
renderer used by the coffee/tea script parser.

`C4:9D16` is the single-token wrapper for `C4:999B`.

`C4:9D1E` advances a VRAM/tile offset by `#$40`, detects high-byte crossings,
adjusts BG scroll word `$003B` through a C0 interpolation helper, calls
`C0:8B26`, and returns the advanced offset.

Source polish: `src/c4/coffee_tea_tile_buffer_helpers.asm` now names the
coffee/tea battle-bg visual state id, row-mask byte/pass counts, token metadata
field offsets, dirty-range reset sentinel, scroll remainder mask, row-reveal
bias, offset high-byte mask, tile-source plane/trailer offsets, work-bank value,
and the visual tile transfer source/destination arguments.

2026-05-06 source polish: the same tile-buffer source now documents side
effects for the C2 visual-state starter, tile-buffer inversion, row-mask merge,
token draw path, one-frame C2 updater, buffer initializer, visible-window
upload, scroll-state advance, row cursor advance, compact-token renderer, and
VRAM-offset/BG-scroll helper. The ownership boundary is intentionally narrow:
C4 owns `$3492`, `$7DFE/$7E00`, `$9F2D/$9F2F/$9F31`, and `$3C14..$3C20`, while
C0/C2 own the bracket, transfer, and battle-background callees.

2026-05-06 tile-buffer contract follow-up: the source now limits the row-mask
helper to `$3492` writes plus row-cursor advancement and leaves `$3C1E/$3C20`
dirty-range changes to the init/upload reset points visible in this family.
The scroll-state helper is also documented as committing through `C0:8EFC` on
each call, not only on wrap, and the token-render entry comments now treat the
`#$000C` register setup in the script interpreters as preserved call-surface
state while the actual glyph width remains owned by the `C3:F054` metadata.

## Flyover intro text runner

`C4:9EA4` is an eight-entry long-pointer table for the flyover/intro text
scripts. The legacy reference names its first three targets as the "Year 199X",
"Onett location", and "Ness house" intro strings, and ebsrc groups it as
`FLYOVER_TEXT_POINTERS`.

`C4:9EC4` accepts a table index in `A`, temporarily marks `$10E4` with
`#$C000`, initializes the coffee/tea tile-buffer state through `C4:9A56`, then
interprets the selected script as byte commands:

| command | behavior |
|---|---|
| `00` | end script and run the fixed fade/cleanup tail |
| `02 xx` | set `$9F2D = xx`, the coffee/tea tile-window position |
| `09` | upload/scroll one `#$18` step through `C4:9B6E`, wait one frame, then advance `C4:9C56` |
| `01 xx` | advance the row reveal cursor through `C4:9CA8(xx)` |
| `08 xx` | render compact token string `xx` through `C4:9CC3`; the preserved `#$000C` register setup is not the glyph-width source |
| other nonzero byte | render it as a single tile token through `C4:9D16` |

The end tail changes display mode `$001A` to `#$04`, calls the C0 display
transition helper at `C0:87CE`, waits `#$00B4` frames through
`Wait_OneFrameAndPollInput`, restores via `C0:8814`, clears `$7DFE..$84FE`
(`#$0380` words), sets `$5E6E = #$00FF`, calls the C0/C4 visual restore pair
`C0:8726` and `C4:800B`, restores `$10E4`, then closes the display bracket with
`C0:8744`.

Source polish: `src/c4/coffee_tea_and_flyover_scene_interpreters.asm` now names
the coffee/tea prompt token ids, initial window index, shared command bytes,
script byte masks, flyover pointer-bank offset, display-bracket arguments,
scene clear region, busy-complete sentinel, flyover wait count, display modes,
and `$10E4` state-mask/restore contract.

2026-05-06 interpreter polish: the source now states the side effects of the
coffee/tea scene selector and flyover scene runner, and splits the flyover text
pointer table into one long pointer per row with comments limiting the
user-facing names to the three locally corroborated intro strings.

2026-05-06 interpreter side-effect follow-up: the shared source now marks the
command-stream read points, coffee/tea command `09` page-drain loop, command
`01` row-reveal byte, command `08` compact token-string byte, direct-token
fallback, flyover command `02` window-index byte, and both cleanup tails. These
comments keep the bytecode grammar local to C4 while treating tile rendering,
display brackets, and C2 visual ticking as callee contracts.

2026-05-06 flyover pointer follow-up: the `C4:9EA4` table rows now have
address-stable labels for all eight entries. The first three retain the local
`Year199X`, `Onett`, and `NessHouse` roles; entries `3..7` remain numbered
until the E1 text payload names are settled. The source also makes the row
shape explicit as low word plus bank byte plus padding byte, matching the
`C4:9EC4` indexed pointer walk.

2026-05-06 flyover pointer table follow-up: the same source now names the E1
low-word payload addresses, shared bank byte, and padding byte as row constants.
This keeps the C4-owned table shape stable while leaving the underlying E1 text
payload identities outside this pass, except for the three locally corroborated
intro strings.

The routine has no direct `JSL`/same-bank `JSR` callers in the split-bank scan,
so the current best read is that it is reached through a pointer/script/event
path rather than a direct code reference.

## Working Names

- `C4:92D2` = `StepLandingProfile7900ColorPlanesTo0240`
- `C4:939C` = `RunLandingProfileDisplayBuildAndFade`
- `C4:9496` = `ScalePackedRgb555ColorByStep`
- `C4:954C` = `BuildScaledPaletteBlockTo7f0000`
- `C4:958E` = `BuildLandingPaletteInterpolationPlanes`
- `C4:96E7` = `InitLandingPalettePlanesFrom0200`
- `C4:96F0` = `InitLandingPalettePlanesFrom4476`
- `C4:96F9` = `MirrorCgramShadow0200To7f0000`
- `C4:9740` = `ExportLandingPaletteAndQueueCgramUpload`
- `C4:978E` = `CopyCgramShadow0200To4476`
- `C4:97C0` = `RunLandingPaletteFadeToScaledBlock`
- `C4:0BE8` = `BlankCommonTileSourceBlock`
- `C4:981F` = `CopyStaticVisualBlock0be8To7c00`
- `C4:9841` = `BeginCoffeeTeaBattleBgVisualState`
- `C4:984B` = `InvertCoffeeTeaTileBufferWords`
- `C4:9875` = `ApplyCoffeeTeaTileRowMask`
- `C4:999B` = `DrawCoffeeTeaTileTokenRun`
- `C4:9A4B` = `WaitFrameAndUpdateBattleBgVisualState`
- `C4:9A56` = `InitCoffeeTeaTileBufferAndTransferState`
- `C4:9B6E` = `UploadCoffeeTeaTileBufferWindow`
- `C4:9C56` = `AdvanceCoffeeTeaTileScrollState`
- `C4:9CA8` = `AdvanceCoffeeTeaRowRevealCursor`
- `C4:9CC3` = `RenderCoffeeTeaTokenString`
- `C4:9D16` = `RenderSingleCoffeeTeaTileToken`
- `C4:9D1E` = `AdvanceCoffeeTeaVramOffsetByTileRow`
- `C4:9EA4` = `FlyoverIntroTextPointerTable`
- `C4:9EA4` = `FlyoverIntroTextYear199xPointer`
- `C4:9EA8` = `FlyoverIntroTextOnettPointer`
- `C4:9EAC` = `FlyoverIntroTextNessHousePointer`
- `C4:9EB0` = `FlyoverIntroTextPointer3`
- `C4:9EB4` = `FlyoverIntroTextPointer4`
- `C4:9EB8` = `FlyoverIntroTextPointer5`
- `C4:9EBC` = `FlyoverIntroTextPointer6`
- `C4:9EC0` = `FlyoverIntroTextPointer7`
- `C4:9EC4` = `RunFlyoverIntroTextSceneByIndex`

## Confidence boundaries

### Locally proved

- the landing half uses the same `7F:` component-plane and `7E:0200` CGRAM
  shadow contracts already pinned in the landing palette note
- `C4:9496` extracts, scales, clamps, and repacks RGB555 component fields
- `C4:9D6A`, the named `COFFEETEA_SCENE`, dispatches through the helper family
  from `C4:9A56` through `C4:9D1E`
- `C4:9EC4` dispatches through the `C4:9EA4` flyover text pointer table and
  reuses the same tile-buffer/text-token helpers as the coffee/tea scene parser
- the coffee/tea side manipulates `$3492`, `$7C00`, `$7DFE`, `$7E00`,
  `$9F2D`, `$9F2F`, `$9F31`, and `$3C14/$3C16/$3C1E/$3C20` as a coordinated
  tile/VRAM transition state

### Still open

- exact user-facing names for individual coffee/tea visual commands
- exact user-facing names for the five later flyover text pointers after the
  locally corroborated `Year199X`, `Onett`, and `NessHouse` entries
- exact layout of the `$C3:F054` token metadata table consumed by `C4:999B`
- exact distinction between the named `COFFEETEA_SCENE` path and the related
  flyover text pointer include that follows it
