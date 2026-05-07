# Bank C4 First Pass

## Main result

Bank `C4` is the visual, renderer, text-tile, movement presentation, file-select,
town-map, and scene-display support bank. It is code-heavy, but much of the
former unknown surface has been grouped into coherent visual/runtime clusters:
PPU/display helpers, text tile staging, color/window HDMA, visual frame copy,
entity footprints, movement vector helpers, text-token glyph rendering, landing
and coffee/tea presentation, file-select/town-map rendering, Sound Stone data,
and late scene/script display helpers.

Primary artifacts:

- `notes/bank-c4-progress-audit.md`
- `notes/bank-c4-cluster-map.md`
- `notes/bank-c4-reference-frontier.md`
- `notes/bank-c4-working-name-proposals.md`
- `notes/c4-build-candidate-ranges.md`
- `notes/c4-byte-equivalence-validation.md`
- `notes/cast-scene-scroll-helpers-c4e4da-c4e583.md`
- `notes/c0-c4-integration-pass.md`
- `notes/data-contracts-c0-c4.md`

The audit and cluster map currently report:

- reference include entries: `566`
- reference address-bearing include entries: `365`
- address-bearing unknown include entries: `325`
- local notes mention `543` distinct `C4:xxxx` addresses
- unknown include entries not directly mentioned in local notes: `0`
- local working names represented in include map: `325`
- working-name proposals: `363`

## Bank layout

The current high-level C4 subsystem map is:

- `C4:0000..0085`: early PPU/display and text tile helper entries.
- `C4:0B51..0B75`: system error screen setup/render/halt path.
- `C4:1DB6..2172`: glyph tile staging, direction octant normalization, and
  projection math helpers/tables.
- `C4:23DC..2E7B`: color math, WH-window HDMA, visual frame copy, tile-column
  merge helpers, and entity footprint/landing-display profile tables.
- `C4:30EC..334A`: party-state reset, callback tables, party-record pointer
  rebuild, and `$5D98` latch setter.
- `C4:38A5..54F2`: text tile placement, text input glyph metrics, active
  text-token glyph run staging, metric helpers, and right-aligned decimal
  printing, plus active entry-chain layout and battle row-position text anchors.
- `C4:5C90..74F6`: menu/window mask and indexed graphics helpers, including
  contract-backed WH-window span/radius data.
- `C4:7C3F..9496`: window graphics load/reset, window flavor palette refresh,
  flyover text undraw/display restore, Lumine Hall/Event 353 text payload, Event 353 custom message
  tile reveal, teleport-event landing mode staging, actionscript camera/screen
  callbacks, movement pulse generation, staged movement tables, octant
  unit-delta tables, tracked-item pulse slots, nearby magic-truffle direction
  lookup, and landing profile interpolation setup/stepping.
- `C4:9496..B1B7`: landing, coffee/tea, battle target selection/validity,
  visual transfer, and Sound Stone presentation data corridors.
- `C4:B3D0..E369`: child entity spawn, path-solver support, file-select text
  data, saved coordinate reload, file-select entity scripts, town-map selection
  rendering, name-buffer commit links, and intro visual asset loaders through
  the Your Sanctuary display corridor.
- `C4:E369..FFFF`: ending cast scene, including the promoted cast-scene loader,
  scroll helpers, cast-name tilemap/print helpers, scene controller, and unused
  cast-name scratch renderer, VWF conversion helper, and credits DMA queue
  helpers, credits/photo playback controller, music pack tables, and audio
  helper tail at `C4:E369..C4:FD4B`, plus final bank padding.

## Current C4 confidence boundary

High confidence:

- C4 has no unmentioned address-bearing unknown include starts left in the
  current cluster map.
- The bank's main role is visual/runtime support rather than battle action
  semantics.
- The C0-C4 integration pass has already tied C4 into overworld movement,
  text/window/menu rendering, battle visuals, file-select displays, landing
  scenes, Sound Stone presentation, and sanctuary/town-map flows.
- Several C4 data tables are already contract-backed in
  `data-contracts-c0-c4.md`, including `BLANK_COMMON_TILE_SOURCE_BLOCK`,
  `WH_WINDOW_SPAN_RADIUS_RAMP_TABLE`, movement octant tables, and the Your
  Sanctuary coordinate table.
- The C4 source scaffold pilot is byte-equivalent: `src/c4/bank_c4_helpers_asar.asm`
  currently covers `142` source/data modules and validates with `0` mismatches
  across the full `65536`-byte bank. Covered slices are the early PPU/display and
  text-tile helper prefix plus allocator (`C4:0000..C4:00D4`), system error screen helpers
  (`C4:0B51..C4:0BD4`), text/vector helpers (`C4:1DB6..C4:2172`),
  window/color/HDMA helpers (`C4:23DC..C4:2631`), screen-position interpolation
  helpers (`C4:2631..C4:26ED`), palette component interpolation helpers
  (`C4:26ED..C4:279F`), visual frame copy helpers (`C4:283F..C4:2A1F`),
  party-state reset/callback helpers (`C4:30EC..C4:334A`), the
  front-interaction door destination probe (`C4:334A..C4:343E`), battle/menu
  row highlight and text-window row helpers (`C4:3568..C4:38B1`), active
  window line advance (`C4:38B1..C4:3915`), locked text-tile data
  (`C4:3915..C4:3B15`), and active-window attribute/glyph-state helpers
  plus glyph printing/name-entry cursor reads and text-input option-strip
  metrics/rendering, title/wrap/fixed-string printers, and VRAM plane refresh
  through tile-bitset release, glyph-run scratch-row rendering, tile placement,
  catch-up transfer, safe tile release, active glyph-run staging, byte-run
  pixel measurement, right-aligned decimal printing, active entry-chain layout,
  battle row-position text fragments, and the split battle/inventory/status
  corridor (`C4:3B15..C4:5C90`), plus staged
  menu glyph scratch render/flush helpers and the PSI/RNG/direction bridge
  through the entity-slot, visual-flag, direction/target, current-anchor,
  photo/new-entity preparation, movement-vector, battle-background/palette, and
  WH-window mask/indexed graphics helper corridors (`C4:5C90..C4:7C3F`), the
  window graphics load/reset, flavor-palette refresh, flyover undraw/display
  restore, and Lumine Hall/Event 353 text payload corridor
  (`C4:7C3F..C4:810E`), Event 353 message tile reveal helpers, the teleport
  event-670 landing mode helper, and actionscript camera/screen-position
  callbacks (`C4:810E..C4:8C59`),
  staged movement/tracked-item pulse helpers (`C4:8C59..C4:90EE`), nearby
  magic-truffle direction and landing profile
  interpolation helpers (`C4:90EE..C4:9496`), landing palette and static
  visual-copy helpers (`C4:9496..C4:9841`), and coffee/tea tile-buffer
  helpers (`C4:9841..C4:9D6A`), coffee/tea and flyover text scene interpreters
  (`C4:9D6A..C4:9FE1`), mixed battle target candidate/validity helpers
  (`C4:9FE1..C4:A228`), and the gas-station intro visual loader
  (`C4:A377..C4:A591`), battle overlay transition data corridor
  (`C4:A591..C4:A67E`), and battle overlay script-state initializer
  (`C4:A67E..C4:A7B0`) plus the battle overlay script-state per-frame stepper
  (`C4:A7B0..C4:AC57`), the Sound Stone presentation table block
  (`C4:AC57..C4:ACCE`) and state-aware Sound Stone presentation controller
  (`C4:ACCE..C4:B1B8`), the landing-display asset stream helpers
  (`C4:B1B8..C4:B329`), the landing child-anchor/spawn helpers
  (`C4:B329..C4:B4BE`), the attached-child lookup/clear wrappers
  (`C4:B4BE..C4:B587`), the path-solver support corridor
  (`C4:B587..C4:C05E`), the file-select text data payload
  (`C4:C05E..C4:C2DE`), plus the saved-landing display/fade and
  saved-coordinate landing reload wrapper (`C4:C2DE..C4:C8A4`), dynamic
  visual-record constructor/latch/walker helpers (`C4:C8A4..C4:D00F`),
  naming buffer remap helpers (`C4:D00F..C4:D274`), the complete town-map
  id/render/load/display/viewer pocket (`C4:D274..C4:D7D9`), the ebsrc-named
  animated naming sprite spawner (`C4:D7D9..C4:D830`), the file-select entity
  helper spans (`C4:D830..C4:D989`), the file-select swirl transition runner
  (`C4:D989..C4:DAD2`), and the ebsrc-named init-intro state dispatcher
  (`C4:DAD2..C4:DCF6`), the tilemap-priority pass (`C4:DCF6..C4:DD28`),
  the Itoi/Nintendo intro asset loaders (`C4:DD28..C4:DE78`), and the
  complete Your Sanctuary display corridor (`C4:DE78..C4:E369`), plus the
  ending cast-scene loader, scroll helpers, cast-name tilemap/print helpers,
  scene controller, unused scratch renderer, VWF conversion helper, and credits
  DMA queue helpers, the credits initializer/photo/count/slide/playback
  controller corridor, the music dataset/audio pack pointer table block, the
  compact audio helper tail (`C4:E369..C4:FD4B`), and explicit bank-end zero
  padding (`C4:FD4B..C4:10000`). The text/vector, visual frame copy, movement pulse,
  flyover scene, battle overlay transition, Sound Stone table, file-select text,
  locked text tile, text tile mask/power-of-two table, battle row-position text,
  event script pointer table, early event/overlay payloads, event script
  payload islands, entity footprint/visual profile tables, battle/inventory/
  status text, equipment item usable flags, target/phone text,
  status/equipment window text, homesickness thresholds, direction matrix,
  direction octant tables, equipment visual-state seed rows, ranked-target
  ordinal tables, Lumine Hall/Event 353 text payload, music table slices, and
  bank-end padding preserve intentional source-adjacent data gaps totaling
  `15383` bytes. `notes/c4-source-residual-map.md` now shows `0` residual
  bytes and `0` residual ranges for C4.

Still intentionally out of scope:

- Final source-ready names for every C4 proposed helper.
- Exact high-level semantics for every visual/script payload and scene data
  block.
- Treating all cluster names as final upstream-quality labels.
- Port-ready rendering contracts for every PPU/HDMA/color math side effect.

## Recommended next move

C4 is ready for integration and asset-contract polish rather than more ordinary
source scouting. The highest-value follow-up is to refine the protected
data/script stubs into richer structured asset manifests where useful, while
keeping the reusable source-bank scaffold pipeline as the byte-equivalence
backstop. The current scaffold already covers the early
PPU/display and text-tile helper prefix plus allocator, system error path,
text/vector helpers, window/color HDMA, screen-position
interpolation, palette-component interpolation, visual frame copy/merge helpers,
party-state reset/callback helpers, inventory/equipment/status helper splits,
movement presentation, and the
landing-to-coffee/tea/flyover visual-helper corridor, plus the gas-station intro
visual loader, the battle overlay transition initializer/stepper, the clean
Sound Stone table prefix, the landing-display asset stream helpers, and the
attached landing-display child-anchor/spawn/clear wrapper corridor through
`C4:B587`, plus the path-solver scratch cursor, grid-border blocker,
candidate pointer sorter, candidate footprint marker, route
propagator/trace/compaction tail, and candidate-group orchestration through
`C4:C05E`, the file-select text data payload through `C4:C2DE`, and the
saved-landing display/fade plus saved-coordinate reload wrapper through
`C4:C8A4`, then the dynamic visual-record constructor/latch and
walker families plus naming buffer remap through `C4:D274`, the full
town-map helper pocket through `C4:D7D9`, the window graphics load/palette/
flyover corridor through `C4:810E`, the reference-led animated
naming/file-select/init-intro/Sanctuary corridor through `C4:E369`, and the
ending cast-scene loader/scroll/name-render/tilemap/print/controller corridor
through the credits/audio tail at `C4:FD4B`.
The `C4:C05E..C4:C2DE` span is now preserved as the ebsrc file-select text
payload rather than decoded as code, and `C4:8037..C4:810E` is similarly
preserved as text/event payload adjacent to the window/flyover helpers. The
named ebsrc tail after the ending credits is now covered through `C4:FD4B`; the
remaining bank-end bytes are protected as explicit zero padding. Earlier skipped
data/script regions are now byte-equivalent scaffold inputs; their remaining
work is semantic asset documentation rather than source-byte closure.
