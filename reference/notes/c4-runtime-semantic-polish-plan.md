# C4 Runtime Semantic Polish Plan

Primary queue context: `notes/source-readiness-triage.md` and
`notes/project-status.md`.

## Current State

`C4` is fully source-backed for the scaffold phase. The handoff in
`notes/bank-c4-source-scaffold-handoff.md` reports byte-equivalence `OK`, while
also noting that many explicit data source blocks are intentionally coarse
asset/table stubs. The next work is renderer-facing semantic polish, not byte
closure.

## Subsystem Slices

- Text tile staging: text tile bitset allocation, glyph mask rendering, dirty
  range tracking, text tile transfer submission.
- Window/color/HDMA helpers: fixed-color math, WH0/WH2 HDMA channel setup,
  window range presets, color math modes, palette interpolation.
- Movement presentation: direction projection, live entity position rebasing,
  visual frame copy helpers, footprint tables.
- File-select and town-map rendering: C1-visible renderer helpers, file-select
  text/window presentation, town-map payload contracts.
- Visual profile tables: entity footprint and secondary visual descriptor table
  rows where C0/C1 consumers prove stable field names.
- Event/presentation payload islands: event script pointer table, event payload
  islands, landing/Sound Stone presentation data.

## First Pass Order

1. Start with text tile staging and window/color/HDMA helpers because they are
   the highest-impact C1 renderer dependencies.
2. Promote movement presentation and visual profile table contracts alongside
   C0 entity/movement consumer evidence.
3. Polish file-select and town-map rendering paths with C1 call-site language.
4. Split or rename event/presentation payload islands only where C3 script or
   landing/Sound Stone notes prove the contract.

## Evidence Inputs

- `notes/bank-c4-source-scaffold-handoff.md`
- `notes/bank-c4-working-name-proposals.md`
- `notes/bank-c4-progress-audit.md`
- `notes/data-contracts-c0-c4.md`
- `notes/ui-font-town-map-asset-contracts.md`
- `notes/landing-cast-visual-contracts.md`
- `notes/landing-hdma-dispatch-family-ef117b-c00d7e.md`

## Expected Outputs

- Stable renderer-facing names/comments for text tile, color/window/HDMA, and
  movement presentation helpers.
- Typed table or row-contract notes for visual profile and footprint data where
  consumers prove field semantics.
- Deferred notes for event payload islands that still need C3 script semantics
  before source-quality naming.

## Implementation Notes

- 2026-05-01 first slice: promoted the early PPU/text tile allocator and
  transfer helpers with byte-neutral aliases for `INIDISP`, the display shadow,
  `$3492` text tile scratch rows, the C0 VRAM transfer parameter block,
  `$9E2B` transfer latch, `$1AD6` text tile bitset, and recovery script id
  `$0A2A`. See `notes/c4-early-ppu-and-text-tile-helpers-0000-0085.md`.
- 2026-05-01 text staging continuation: promoted the menu glyph scratch
  renderer/flush pair with byte-neutral names for the `$9D23` scratch rows,
  `$9E23/$9E25/$9E27` cursors, `$9E2B` transfer latch, `$7900` VRAM base,
  and `C0:8616` transfer-queue tag byte. See
  `notes/text-window-rendering-primitives-c1078d-c10d7c.md`.
- 2026-05-01 active text-token staging: promoted the `$3492` glyph scratch
  renderer and the adjacent `$9D23` reset helper with byte-neutral names for
  scratch-row bases, bit/row/upload cursors, cursor wraps, clear-fill bytes,
  merge masks, and the PSI-menu continuation flag. See
  `notes/text-token-glyph-run-stager-c44b3a-c44e61.md` and
  `notes/text-window-rendering-primitives-c1078d-c10d7c.md`.
- 2026-05-01 window/color touch-up: named the fixed-color `COLDATA`
  component selector bits and channel-4 WOBJSEL clear value in the
  window/color HDMA helper. See
  `notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md`.
- 2026-05-01 movement/presentation start: confirmed the screen-position
  interpolation source already carries the local `$3C22..$3C30` and live-slot
  rebase contracts, then promoted visual-frame helper literals for directional
  frame-list stride, tile-column merge masks, and render-strip source fields.
  See `notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md`.
- 2026-05-01 file-select/town-map start: promoted town-map renderer/load
  constants for the `EF:A70F` sector lookup, E0/E1 asset tables, blink and
  palette timers, input masks, decompressor latch, display latches, and VRAM
  transfer destinations. See `notes/town-map-selection-rendering-c4d274-c4d744.md`.
- 2026-05-01 file-select continuation: promoted table, sentinel, live-entity
  wait-scan, fixed spawn, frame-selector, and tilemap priority-pass constants
  in the file-select entity/script helpers. See
  `notes/file-select-entity-scripts-and-swirl-transition-c4d830-c4d989.md`.
- 2026-05-01 file-select swirl: promoted the transition runner's reset
  callees, auto-sector music latch, camera/display seeds, party scratch clear,
  `C3:FD8D` text pointer table, overlay completion latch, input abort masks,
  busy byte, and return-value sentinels. See
  `notes/file-select-entity-scripts-and-swirl-transition-c4d830-c4d989.md`.
- 2026-05-01 init-intro dispatcher: promoted state ids, session/presentation
  flags, screen-origin reset fields, forced-blank checks, color/display latches,
  Sound Stone melody ids, title still-image arguments, and file-select swirl
  mode values. See
  `notes/file-select-entity-scripts-and-swirl-transition-c4d830-c4d989.md`.
- 2026-05-01 Sound Stone start: promoted the presentation controller's CE
  graphics/palette payloads, 7F work buffer, VRAM transfer sizes, sprite
  resource args, staging tile blocks, eight-Sanctuary state record bases,
  state values, and primary timers. See
  `notes/sound-stone-presentation-data-c4ac57.md`.
- 2026-05-01 Sound Stone continuation: promoted the animation loop's
  phrase/stinger timing, EF payload pointer walk, per-Sanctuary orbit
  angle/phase/glyph fields, spinner frame, battle-visual script ids, input exit
  mask, and closeout fade/busy gates. See
  `notes/sound-stone-presentation-data-c4ac57.md`.
- 2026-05-01 landing display streams: promoted the landing asset stream
  helper's subpiece pointer-table, descriptor-count/table, no-subpiece
  sentinel, source-bank/list offsets, paired-plane VRAM transfer, and the four
  stream pointer families seeded by `C4:B26B`. See
  `notes/landing-display-assembly-cluster-c007b6-c4b26b.md`.
- 2026-05-01 landing child anchors: promoted the child-anchor/spawn helper's
  placement modes, `$B3F8/$B3FA` anchor pair, live entity table families,
  child-definition field offsets, signed-offset masks, spawn descriptor, and
  attached-parent tag. See `notes/child-entity-spawn-c4b3d0-c40de8.md`.
- 2026-05-01 landing child lookup: promoted the attached-child clear/lookup
  wrapper's `$103E` scan table, tagged-parent mask, live-slot loop bounds,
  default base-slot arguments, and resolver-backed spawn call contract. See
  `notes/child-entity-spawn-c4b3d0-c40de8.md`.
- 2026-05-01 landing palette touch-up: promoted RGB555 scale/repack
  thresholds, high-component normalization, WRAM-low selectors, palette
  first-word/fade sentinels, and the existing-work selector bit in the landing
  palette/display helper. See
  `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`.
- 2026-05-01 saved landing setup: promoted the saved landing display
  initializer's init latch, stage cursor/scratch latches, E1 asset pointers, BG
  and VRAM transfer values, palette staging offsets, intro display state, and
  phase staging buffer constants. See
  `notes/saved-landing-display-stage-c4c2de-c4c64d.md`.
- 2026-05-01 saved landing fades: promoted the saved landing fade helpers'
  abort latch, success/abort sentinels, palette restore source/scale/commit
  values, long/short phase frame counts, phase stage ids, text/event gate
  pointers, and no-source fade counters. See
  `notes/saved-landing-display-stage-c4c2de-c4c64d.md`.
- 2026-05-01 saved landing reload: promoted the saved-coordinate reload
  wrapper's snapshot pair, abort transition args, restore fade and sound/counter
  ids, return-to-world display state, map-record cleanup fields, event-loop
  bounds, `$289E` reset table, and final world-refresh fade count. See
  `notes/saved-landing-display-stage-c4c2de-c4c64d.md`.
- 2026-05-01 actionscript camera callbacks: promoted the callback strip's
  current-slot index, callback flag bit, active entity registry scan tables,
  live world/screen/offset coordinate tables, camera origin pair, facing table,
  and half-octant direction rounding constants. See
  `notes/c3-actionscript-callback-contracts.md`.
- 2026-05-01 staged movement pulses: promoted the movement pulse accumulator
  and path-builder's first index, active run flag, minimum delta, signed-word
  inversion mask, direction rounding spans, and repeated-pulse loop sentinel.
  See `notes/staged-movement-pulse-and-tracked-item-registry-c48c59-c48f98.md`.
- 2026-05-01 tracked-item pulse registry: promoted the tracked item pulse
  helpers' active/inactive return values, blocked overworld state, first-slot
  and first-pulse sentinels, low-byte masks, and full-value C1 item pulse
  argument. See
  `notes/staged-movement-pulse-and-tracked-item-registry-c48c59-c48f98.md`.
- 2026-05-01 magic-truffle direction helper: promoted the immediate text
  command helper's truffle pose descriptor, missing-slot sentinel, range and
  minimum-distance gates, result values, live entity/player coordinate fields,
  signed delta inversion mask, and direction octant rounding constants. See
  `notes/text-command-family-1f-deferred-callbacks.md`.
- 2026-05-01 landing profile interpolation: promoted the adjacent landing
  profile color/display helper contracts for the `$7F:7900..7E00` component
  planes, `0x0240` template buffer, RGB555 masks, `EF:10FB` descriptor table,
  row stride, transfer blocks, wait selectors, display cache latch, and busy
  byte. See `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`.
- 2026-05-06 truffle/landing profile follow-up: renamed the local decision
  labels in `GetNearbyMagicTruffleDirection` around slot discovery, range
  gates, absolute-delta normalization, too-close fallback, and octant return.
  The adjacent landing-profile source now marks the $7F:7900..7E00 plane
  initializer/stepper and descriptor runner side effects while keeping C0
  transfer, display-row, tilemap, wait, and busy-byte behavior callee-owned.
  See `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`.
- 2026-05-01 coffee/tea tile buffer: promoted row-mask byte/pass counts,
  token metadata field offsets, dirty-range and scroll sentinels, row-reveal
  and high-byte masks, tile-source plane/trailer offsets, work-bank value, and
  visual tile transfer arguments. See
  `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`.
- 2026-05-01 coffee/tea and flyover tail: promoted the scene interpreters'
  prompt token ids, initial window index, shared command bytes, byte masks,
  flyover pointer offset, display-bracket arguments, clear region,
  busy-complete sentinel, flyover wait count, display modes, and `$10E4`
  state-mask/restore contract. See
  `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`.
- 2026-05-01 gas-station intro loader: promoted the C4-side intro asset
  loader's display mode, clear/upload selectors, pointer bank-field offset,
  tilemap attribute rewrite fields, battle-visual tile-state/chunk staging
  values, script start value, and mask/sentinel literals. See
  `notes/gas-station-intro-asset-loader-c4a377.md`.
- 2026-05-01 battle overlay island: split the adjacent transition data into
  the static wave table and four named open/close script payload blocks, then
  promoted shared `$AEC2..$AEE6` state names, flag bits, script/frame tables,
  record stride/sentinel fields, effect position/size deltas, special-mode
  ladder values, and C0 window/offset helper contracts. See
  `notes/battle-overlay-script-state-c4a67e-c4a7b0.md`.
- 2026-05-06 credits presentation follow-up: tightened the C4 credits queue
  and playback controller around the newly polished C0 command-stream callback.
  The source now names the frame-callback install/reset calls, 9-byte credits
  DMA queue records, `$B4E3/$B4E5/$B4E7..$B4ED` command-stream/scroll fields,
  E1:2F8A photographer record stride/count, photograph render state, and the
  BG3 scroll/progress comparison at `$003B`. See
  `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md` and
  `notes/frame-callback-bodies.md`.
- 2026-05-06 cast-scroll presentation follow-up: tightened the ending cast
  loader/scroll helpers, cast-name tilemap copy/print path, cast entity
  spawn/onscreen helpers, and `PlayCastScene` controller. The source now names
  the event-801 scroll threshold polling contract, `$0BCA` live-Y source,
  `$1002` blank-row upload cursor, `$B4D1` cast-name tile offset, `$9641`
  completion latch, and the C0 cleanup helper calls without assigning those
  per-slot tables a global meaning. See
  `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`.
- 2026-05-06 cast loader presentation follow-up: tightened the C4:E369 loader's
  local setup contract around `$9F2A`, live entity `$0A62`/`$116A` marking,
  `$B4CE` cast-name glyph-width mode, `$7C00` BG3 clear/upload staging,
  E1/C3 low-word asset tuples, and final `$0030/$001A` display seeds while
  leaving C0/C4 callee internals as caller references. See
  `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`.
- 2026-05-06 cast-name tilemap follow-up: tightened
  `PrepareCastNameTilemap`/`PrintCastName` around local template row counts,
  the C3:FDB5 source table, current-bank template lows, E1:2EFA pointer-record
  offsets, `$7F:4000` staging, BG3 `$7C00` wrap math, and the C0 VRAM-transfer
  selector byte without claiming C0/C3/E1 callee internals. See
  `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`.
- 2026-05-06 cast-name wrapper follow-up: carried the same local contracts into
  `CopyCastNameTilemap`, `PrintCastNameParty`, and
  `PrintCastNameEntityVar0`, naming `$7F:4000` row staging, `$B4D1` tile-base
  adjustment, E1:2EFA three-byte pointer rows, C3:FDB5 party lookup, and the
  special source-selector `7 -> 01C0`. See
  `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`.
- 2026-05-06 cast palette/spawn follow-up: tightened the remaining
  `C4:EC52..ED0E` cast presentation helpers around the local `$0E5E` cast-name
  selector role, `$7F:7000 + index*$20 -> $0380` palette transfer,
  `$0030 = #$10` display selector, `$0A38` rotating spawn variant, `$FFFF`
  default parent argument, and word-indexed live-Y onscreen comparison. See
  `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`.
- 2026-05-06 cast controller follow-up: tightened `PlayCastScene` around the
  event-801 driver id, `$9641` completion latch, `$0A62` driver cleanup scan,
  delayed-action restore anchors `$0A4C/$0A4E`, return transition mode, and
  final `$001A = #$17` display mode while leaving frame/update/remove callees
  external. See `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`.
- 2026-05-06 audio tail follow-up: tightened the final C4 audio block around
  the music dataset row fields, audio pack pointer row shape, US bank resolver
  mask reset, cold-start bootstrap shared pack, `ChangeMusic` primary,
  secondary, and sequence pack roles, Sound Stone recording transition
  exception, stereo/mono stream loader, and auto-sector music-change latch. See
  `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md` and
  `notes/audio-pack-format-and-renderer-frontier.md`.
- 2026-05-06 PPU/presentation contract follow-up: added conservative
  side-effect comments for the C4 color-window and WH0/WH2 HDMA helpers,
  clarified that the battle overlay initializer owns the `$AEC2..$AEE6`
  callee-side state layout, attached local movement-presentation WRAM names to
  the current-slot vector/bounds helper corridor, and split the Sound Stone
  presentation data block into labeled EF payload, coordinate, melody,
  phrase-length, and event tables. See
  `notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md`,
  `notes/battle-overlay-script-state-c4a67e-c4a7b0.md`,
  `notes/movement-target-bounds-and-vector-refresh-c46ef8-c47369.md`, and
  `notes/sound-stone-presentation-data-c4ac57.md`.
- 2026-05-06 HDMA register-name follow-up: split the C4 window/color HDMA
  register aliases into mode, B-bus target, table address, table bank, and
  indirect-bank fields for channels 4/5. The entry comments now record that
  caller A feeds both bank registers and caller X feeds the table address,
  while leaving stream payload interpretation to the generating callers.
  See `notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md`.
- 2026-05-06 visual table follow-up: split the coarse
  `C4:2A1F..30EC` footprint / secondary visual descriptor corridor into
  labeled footprint geometry tables, the secondary descriptor pointer table,
  descriptor rows, the preserved callback byte island, map-tile chunk pointers,
  and visual tile-word ladders. Also documented the side effects for the visual
  frame-word copy helpers, render-strip wrapper, and `$212C` main-screen HDMA
  starter. See
  `notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md` and
  `notes/secondary-visual-descriptor-contracts.md`.
- 2026-05-06 visual record table follow-up: promoted the constructor and walker
  sources to the same local contract as their notes by naming `$B4A4/$B4A6`,
  `$B4A8`, `$B4AA/$B4AC`, the `7F:7C00` table, `0x14` record stride, fields
  `+00..+12`, request modes `2..0A`, state filters `1..4`, latch lanes, the
  `$FFFF` unset-handle sentinel, `$116A/$4000` visual-profile flag, `$10F2`
  state-1 latch, and `$7F:7F00` occupancy bitmap while leaving C0
  allocation/refresh and C4 render-strip helper internals callee-owned. See
  `notes/visual-record-constructor-and-latches-c4c8a4-c4cbe3.md` and
  `notes/visual-record-walkers-and-naming-remap-c4cc2f-c4d065.md`.
- 2026-05-06 coffee/tea interpreter follow-up: tightened side-effect comments
  for the shared coffee/tea tile-buffer helpers and scene interpreters, naming
  the local `$3492`, `$7DFE/$7E00`, `$9F2D/$9F2F/$9F31`, and `$3C14..$3C20`
  ownership boundary while leaving C0/C2 transfer and battle-background callee
  behavior to those banks. The flyover text pointer table is now row-split with
  only the three locally corroborated intro-string roles called out. See
  `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`.
- 2026-05-06 window mask / indexed graphics follow-up: tightened the
  C4-local contracts for generated WH0/WH2 mask streams, the `$0E5E`
  toggle-versus-index boundary, the `CC:2DE1` indexed graphics loaders, the
  window graphics cache rebuild, the `$0200` window-flavour palette refresh,
  and the flyover-undraw return-to-world presentation side effects. C0/C2
  transfer and cleanup callees remain documented only as caller joins where C4
  writes their local arguments. See
  `notes/window-mask-and-indexed-gfx-c47501-c47b77.md`.
- 2026-05-06 Event 353 reveal follow-up: tightened the event-specific tile
  reveal contract around the `$3492` glyph scratch rows, `$7F:0000/$0002`
  transfer staging, `$7F:1000/$4000` reveal maps, `$0E5E/$0E9A` current-slot
  reveal state, and the C3 visual-transfer queue arguments. The adjacent Event
  670 landing helper now documents only its C4-owned `$9F41 = 5` and
  `$987F = 2` seeds, leaving destination staging and transition interpretation
  to the owning banks. See
  `notes/event353-message-tile-builders-c4810e-c48a6d.md`.
- 2026-05-06 battle-background / palette-brightness follow-up: tightened the
  movement-script battle-background presentation loader around its C4-owned BG
  mode/base arguments, display bracket calls, and C2 sprite-resource arguments.
  The adjacent palette adapters now name the `$4476 -> $0240` row transform,
  `$0030 = #$18` upload selector, `$0E5E[current]` signed brightness/magnitude
  role, and the fixed-color mode values passed to C4:249A while leaving C0/C2
  queue and battle-background internals to their owning banks. See
  `notes/palette-brightness-row-adjusters-c473b2-c474a8.md`.
- 2026-05-06 landing palette export follow-up: tightened side-effect comments
  for the `$7F:0000` scaled palette builder, `$7F:0200..0C00` interpolation
  plane initializer, `$0200 <-> $7F:0000` mirror/export pair, selector `#$18`
  CGRAM upload queue, and the full fade driver. The parallel
  `$7F:7900..7E00 -> $0240` landing-profile stepper and descriptor-driven
  display/template orchestrator now carry matching source comments, with C0 row
  and tilemap builders still treated as external callees. See
  `notes/landing-palette-interpolation-export-c4958e-c426ed.md` and
  `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`.
- 2026-05-06 landing palette copy-size follow-up: split the `$0200`
  CGRAM-shadow address from the `$0200` copy byte count in the C4 source,
  corrected the palette note's old mirror-direction wording for `C4:9740`, and
  documented the fade driver's count-`1` immediate-export case plus duplicate
  selector `#$18` write. C0 display-selector behavior remains callee-owned.
  See `notes/landing-palette-interpolation-export-c4958e-c426ed.md`.
- 2026-05-06 gas-station intro visual follow-up: tightened side-effect comments
  for the CA:F038 selector, CA:D7A1/CA:D93D asset pointer-table walks,
  `$7F:0000` decompression staging, `$6000/$7C00` VRAM queue arguments,
  tilemap high-byte rewrite, and the C4-owned `$ADD4/$AE20/$AE4B` plus
  `$ADE0/$AE00` battle-visual tail seeds. C0/C2 queue, asset-format, and script
  runner internals remain out of scope. See
  `notes/gas-station-intro-asset-loader-c4a377.md`.
- 2026-05-06 battle-overlay transition follow-up: converted the four local
  C4:A5CE/A5FA/A626/A652 overlay payloads from raw byte blocks into
  row-structured `#$16` records with explicit terminators, optional-field
  `$8000` sentinels, signed deltas, and delta-step fields. The stepper now marks
  its active script-record path, table-driven frame fallback, special-mode
  ladder, and cleanup handoff without assigning C0/C2 renderer internals to C4.
  See `notes/battle-overlay-script-state-c4a67e-c4a7b0.md`.
- 2026-05-06 overlay transition-record follow-up: replaced the remaining raw
  record words in the four C4:A5CE/A5FA/A626/A652 battle-overlay payloads with
  local constants for open/close delays, initial X/Y seeds, size sentinels,
  signed deltas, delta-step words, and zero terminators. See
  `notes/battle-overlay-script-state-c4a67e-c4a7b0.md`.
- 2026-05-06 overlay stepper side-effect follow-up: tightened comments in
  `StepBattleOverlayScriptState` around size-delta accumulation, zero-crossing
  clamps, zero-size long-script completion, `animation parity + 3` frame-tile
  selector, reverse frame-table walking, and the special-mode `CE:DD41` reseed.
  See `notes/battle-overlay-script-state-c4a67e-c4a7b0.md`.
- 2026-05-06 Sound Stone presentation follow-up: converted the C4:AC57 EF
  payload pointer prefix into nine explicit 4-byte row labels and added
  side-effect comments around the Sound Stone controller's setup, Sanctuary
  record initialization, per-frame sequence, render pass, animated EF-payload
  walk, and closeout handoff. C0/C2 renderer, transition, and battle-visual
  internals remain external callee contracts. See
  `notes/sound-stone-presentation-data-c4ac57.md`.
- 2026-05-06 flyover text pointer follow-up: tightened the C4:9EA4 flyover
  intro text pointer table into eight explicit row labels, keeping only the
  three locally corroborated user-facing names and leaving later rows numbered.
  The `C4:9EC4` runner now marks the C4-owned low-word/bank/padding pointer
  walk before handing control to the shared coffee/tea text command grammar.
  See `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`.
- 2026-05-06 coffee/flyover interpreter follow-up: tightened side-effect
  comments for the shared command-stream read points, coffee/tea page-drain
  command, row-reveal byte, compact-token byte, direct-token fallback, flyover
  window-index command, and both cleanup tails. See
  `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`.
- 2026-05-06 coffee tile-buffer contract follow-up: corrected the row-mask
  helper side-effect boundary so `$3C1E/$3C20` dirty-range words are only
  claimed at the visible init/upload reset points, documented `C4:9C56` as an
  every-call tile-buffer commit rather than a wrap-only commit, and demoted the
  script interpreters' `#$000C` token register setup to preserved call-surface
  state while leaving glyph widths owned by `C3:F054` metadata. See
  `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`.
- 2026-05-06 cast-name patch follow-up: split the inline C4:E796 tilemap patch
  bytes into the three local suffix rows used by `PrepareCastNameTilemap`, then
  replaced the raw E796/E79D/E7A4 source lows with row-specific constants and
  callee-argument comments. C0 tilemap-copy internals remain external. See
  `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`.
- 2026-05-06 credits DMA queue follow-up: promoted the shared C4 credits DMA
  ring-record shape into enqueue/drain constants for the 9-byte stride, field
  offsets, and `$007F` index mask, then marked where C4 packs/unpacks the C0
  transfer selector, VRAM destination, long source pointer, and byte count.
  See `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`.
- 2026-05-06 credits scene state follow-up: tightened the credits initializer
  and playback controller around their C4-owned work-buffer, command-stream,
  display selector/mode, post-scroll hold, return-spawn, and scene-clear
  arguments while leaving frame-callback and display internals to C0. See
  `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`.
- 2026-05-06 credits photograph follow-up: tightened the credits photograph
  render/count/slide helpers around the C4-owned `E1:2F8A` record fields,
  `$98CB` optional visual rows, fixed photo palette transfer arguments,
  object/attached-visual loop bounds, and slide angle/frame-count fields. The
  comments keep map load, entity spawn, visual attach, BG3 scroll, and DMA
  queue behavior as caller joins into their owning helpers. See
  `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`.
- 2026-05-06 photo/new-entity producer follow-up: tightened the C4 producer
  side around the photographer scene-record placement helper, staged new-entity
  argument words, teleport destination rows, yield-to-text latch, deferred
  text-pointer record type, staged-position proximity check, and equipment
  comparison `$98C9/$98CB` visual row packing. See
  `notes/current-slot-position-staging-c46b8d-c46d4b.md` and
  `notes/c4-visual-frame-copy-and-footprint-tables-283f-2b0d.md`.
- 2026-05-06 entity visual wrapper follow-up: tightened the prepared-entity
  consumers of `$9E2D/$9E2F/$9E31`, C4-local `$10B6/$116A` flag-word families,
  all-registry fanout paths, wandering-photographer `$9E35` seed, visual-type
  movement-pointer queueing, and current-slot facing/frame-selector refresh
  helpers. See
  `notes/c4-entity-visual-flag-current-slot-wrappers-c4645a-c46a5e.md`.
- 2026-05-06 resolver/frame-selector follow-up: tightened the upstream C4
  resolver and script-runner band around `$2C9A/$2CD6`, the compact
  `$988B/$9897` registry, staged new-entity scratch fills, `C4:C4D4`
  three-byte dispatch records, selector-mode octant helpers, `$2AF6`
  frame-selector updates, registry broadcast cutoff, and `$116A/$8000` marker
  path. See `notes/entity-resolver-script-and-direction-wrappers-c460ce-c4645a.md`.
- 2026-05-06 direction/anchor staging follow-up: tightened the direction
  octant and current-slot anchor helpers around live anchor, cached target,
  staged-position, player position/facing, rounded-octant cache, camera-origin
  placement, and registry recent-slot target contracts. See
  `notes/direction-octant-normalizers-c46a5e-c46b51.md` and
  `notes/current-slot-position-staging-c46b8d-c46d4b.md`.
- 2026-05-06 movement vector/bounds follow-up: tightened the downstream
  movement target helper around cached-target arrival tests, split vector
  high/low writes, sign-extension masks, area-class returns, landing-profile
  dispatch, camera-column refresh arguments, and the C0 movement/facing caller
  joins. The source keeps `$0ED6/$0F12` proximity-threshold aliases separate
  from their area-bound aliases. See
  `notes/movement-target-bounds-and-vector-refresh-c46ef8-c47369.md`.
- 2026-05-06 window-mask/indexed-gfx follow-up: tightened the WH0/WH2 stream
  builders and indexed window graphics loaders around current-slot/base-slot
  indexes, camera-origin shadows, double-buffer roots, `$CC:2DE1` record roots,
  VRAM destinations, block sizes, and `$0030/$003B` presentation-refresh
  arguments. The source continues to treat HDMA install and renderer queue
  behavior as callee-owned. See
  `notes/window-mask-and-indexed-gfx-c47501-c47b77.md`.
- 2026-05-06 window-mask selector/latch follow-up: split the indexed graphics
  loaders' `$0030` display-selector latch from the `#$18` selector value, and
  renamed the local `$003B` write as a presentation-refresh latch instead of a
  BG-scroll shadow. C0/NMI upload and refresh interpretation remains external.
  See `notes/window-mask-and-indexed-gfx-c47501-c47b77.md`.
- 2026-05-06 window-gfx/flyover follow-up: tightened the adjacent window cache
  rebuild and flyover-undraw helper around E0 source rows, `$7F` work blocks,
  tile-state clear/copy sizes, glyph scratch fields, window-flavour palette
  queue arguments, BG2 screen-base restore values, glyph-run reset index, and
  the `$0030 = #$18` display selector. The C2 flyover cleanup remains a
  sequenced callee rather than a C4-owned contract. See
  `notes/window-mask-and-indexed-gfx-c47501-c47b77.md`.
- 2026-05-06 window-gfx selector/latch follow-up: split the flyover-undraw
  path's `$0030` display-selector latch from the `#$18` window-gfx selector
  value, and clarified that C4 only sequences the `C2:038B` cleanup before
  reloading the cache. C2 cleanup side effects and C0/NMI selector
  interpretation remain external. See
  `notes/window-mask-and-indexed-gfx-c47501-c47b77.md`.
- 2026-05-06 battle-background brightness follow-up: tightened the
  movement-script battle-background loader and palette-brightness adapters
  around BG mode/base queue arguments, C2 sprite-resource argument staging,
  signed RGB555 component clamps, saved/work palette row bases, row counts,
  current-slot signed magnitude reads, upload selector writes, and fixed-color
  math modes. See `notes/palette-brightness-row-adjusters-c473b2-c474a8.md`.
- 2026-05-06 battle-background selector/latch follow-up: split the brightness
  row batch wrapper's `#$18` full-CGRAM selector value from the `$0030`
  display-selector latch name, keeping C4's side effect to the `$0240` adjusted
  rows plus latch write while leaving C0/NMI upload interpretation external.
  See `notes/palette-brightness-row-adjusters-c473b2-c474a8.md`.
- 2026-05-06 screen-origin/palette-export follow-up: tightened the tail of the
  window/color note around `$3C22..$3C30` fixed-point screen-origin staging,
  C0 projection/map-refresh caller joins, live-slot screen-relative rebasing,
  7F palette interpolation planes, `$0200` CGRAM shadow export, and `$0030`
  full-CGRAM upload selector writes. See
  `notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md`.
- 2026-05-06 palette selector/rebase follow-up: split the palette stepper's
  `#$18` full-CGRAM-upload selector value from the `$0030` display-selector
  latch name, keeping C0/NMI upload behavior callee-owned, and clarified the
  screen-position live-entity rebase loop as a two-byte slot scan bounded by a
  byte count. See `notes/c4-window-color-math-and-palette-helpers-23dc-26ed.md`.
- 2026-05-06 flyover pointer table follow-up: tightened the C4:9EA4 flyover
  intro text pointer table around its eight low-word payload constants, shared
  E1 bank byte, padding byte, and row shape consumed by `C4:9EC4`, while
  keeping later E1 payload names out of scope. See
  `notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md`.

## Validation

Future implementation passes should use:

```powershell
python tools\build_source_bank_scaffold.py --bank C4
python tools\validate_source_bank_byte_equivalence.py --bank C4 --module all --combined --scaffold src\c4\bank_c4_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank C4
python tools\build_ebsrc_bank_map.py --bank C4
python tools\build_source_bank_residual_map.py --bank C4
python tools\build_working_name_manifest.py --banks C0 C1 C2 C3 C4 --output build\working-names-c0-c4.json
python tools\validate_data_contracts.py
```

This planning pass does not split C4 data stubs or change source files.
