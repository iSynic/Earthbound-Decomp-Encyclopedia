# C3 Event/Actionscript Semantics Roadmap

This is the front door for the semantic phase after readable source-bank
closure. C3 is byte-equivalent and scaffold-closed, but much of the bank is
interpreted event/actionscript bytecode rather than native 65816 source.

The goal of this phase is to make those scripts understandable, editable, and
eventually reassemblable without guessing.

## Current Baseline

- C3 source scaffold: `src/c3/bank_c3_helpers_asar.asm`
- C3 scaffold coverage: `65536 / 65536` bytes
- C3 residual ranges: `0`
- C3 byte-equivalence: `OK`, `0` mismatches
- Script manifest: `notes/script-payloads-c3.md`
- Source/data map: `notes/c3-source-data-map.md`
- Current promoted script payload labels: `84`
- Current promoted complete event-bytecode decodes: `75`
- Current non-event script-adjacent payloads: `8`
- Current source-form event/actionscript pilots: `140` families, `56518` validated
  bytes
- Current source-pilot labels harvested into the reference index: `1262`
- Source-pilot frontier: `notes/c3-source-pilot-frontier.md` (`0` remaining
  candidate bytes)
- Event/actionscript integration scaffold:
  `src/c3/bank_c3_event_scripts_source_pilot.asar.asm`
- Whole-bank C3 scaffold:
  `src/c3/bank_c3_helpers_asar.asm` (`11` protected ranges, `0` mismatches)

This means the byte layer is stable. The open work is semantic: opcode
contracts, operand meanings, script family roles, and reassembly-friendly source
forms.

## Current Audit

`tools/build_c3_actionscript_semantics_audit.py` regenerates the current
frontier report from `build/c3-source-data-map.json`, `build/ref-index.json`,
and the local ROM. The checked-in report is
`notes/c3-actionscript-semantics-audit.md`.

Current audit result:

- script/actionscript rows audited: `181`
- rows syntactically complete with the current decoder: `181`
- rows with stable non-`UNKNOWN_C3...` names in the audit: `181`
- native `EVENT_CALLROUTINE` byte-count contract seeds: `86`
- installed tick/physics/position callback target seeds: `17`
- rows blocked by unknown native callback argument contracts: `0`
- unknown event opcodes found: `0`
- `tools/build_ref_index.py` now harvests checked-in source-pilot labels from
  `src/c3/event_scripts/*.asm`, so decoded targets and audit row names reuse the
  validated source labels instead of drifting into hand-maintained duplicates
- `tools/decode_event_script.py` now prints first-pass semantic operand fields
  for common VM operands (`script_var=var4`, `frames=$08`,
  `animation_id=$01`, `x_velocity_word=$0200`) and named inline callback
  arguments (`event_flag_word=$000C`,
  `neighbor_cache_callback_long=$C0:64A6 <...>`)
- The decoder now applies high-confidence value labels for the C0 mutation
  operation table (`AND`, `OR`, `ADD`, `EOR`), `$5D9A` queue/special-state
  writes, and signed velocity/delta words while preserving raw hex bytes
- callback semantic groups are now emitted in the audit for both
  `EVENT_CALLROUTINE` bridges and installed callback targets, with local names
  and first-pass contracts for high-value timed-delivery, visual-profile,
  current-slot-state, movement, collision, text/presentation, render, tick, and
  restore callbacks

This shifts the next pass away from opcode discovery and basic operand labeling.
Remaining value semantics should be promoted only when the evidence is local and
strong: which variable slots mean target coordinates in a specific family,
which animation ids/facing values are symbolic constants, and which WRAM fields
should become named contracts.

## Milestone Definition

This milestone is complete when C3 event/actionscript payloads have:

1. an opcode catalog with operand shapes and confidence levels
2. a decoded include-start inventory for every event/actionscript payload row
3. stable labels for branch/call targets used by promoted script families
4. known external callback argument shapes for `EVENT_CALLROUTINE`
5. at least one script family emitted in a reassembly-friendly source form
6. a clear frontier list for unknown opcodes, unknown operands, and VM-adjacent
   payloads that are not event bytecode

Items 1-5 are now satisfied at first-pass quality for the audited C3 rows. Item
6 is also satisfied for milestone purposes: the report has no unknown opcode,
unknown callback, or unknown-name frontier, and the remaining literals are
explicitly a known-limits/value-semantics problem rather than byte discovery.

## Terminology

- `event-bytecode-asset`: a script payload that should be decoded as event VM
  bytecode, not native 65816.
- `event-bytecode-label`: an internal label or branch target inside an event VM
  bytecode stream.
- `event-script-asset`: an ebsrc event include row that is known to be script
  payload, but has not yet been promoted into local decoded labels.
- `movement-pattern-data`: compact movement/pattern data adjacent to event
  scripts, but not decoded by the event VM.
- `effect-script-asset`: a battle visual effect script or other VM-adjacent
  payload that uses a different interpreter contract.

## Opcode Catalog Seed

The current decoder catalog is in `tools/decode_event_script.py`. Operand names
describe byte shape first; semantic names should tighten as C0/C4 callback and
WRAM contracts improve.

| Opcode | Name | Operands | Control-flow role |
| --- | --- | --- | --- |
| `$00` | `EVENT_END` | - | terminal |
| `$01` | `EVENT_LOOP` | `byte` | loop setup |
| `$02` | `EVENT_LOOP_END` | - | loop terminator |
| `$03` | `EVENT_LONGJUMP` | `ptr3` | terminal jump |
| `$04` | `EVENT_LONGCALL` | `ptr3` | subroutine call |
| `$05` | `EVENT_LONG_RETURN` | - | terminal return |
| `$06` | `EVENT_PAUSE` | `byte` | wait |
| `$07` | `EVENT_START_TASK` | `shortptr` | starts concurrent script task |
| `$08` | `EVENT_SET_TICK_CALLBACK` | `ptr3` | callback install |
| `$09` | `EVENT_HALT` | - | terminal halt |
| `$0A` | `EVENT_SHORTCALL_CONDITIONAL` | `shortptr` | conditional call |
| `$0B` | `EVENT_SHORTCALL_CONDITIONAL_NOT` | `shortptr` | inverted conditional call |
| `$0C` | `EVENT_END_TASK` | - | terminal task end |
| `$0E` | `EVENT_SET_VAR` | `byte`, `word` | action/script variable write |
| `$0F` | `EVENT_CLEAR_TICK_CALLBACK` | - | callback clear |
| `$10` | `EVENT_SWITCH_JUMP_TEMPVAR` | `wordlist` | tempvar-indexed jump |
| `$11` | `EVENT_SWITCH_CALL_TEMPVAR` | `wordlist` | tempvar-indexed call |
| `$12` | `EVENT_WRITE_BYTE_WRAM` | `word`, `byte` | WRAM byte write |
| `$13` | `EVENT_END_LAST_TASK` | - | task control |
| `$14` | `EVENT_BINOP` | `byte`, `byte`, `word` | variable operation |
| `$15` | `EVENT_WRITE_WORD_WRAM` | `word`, `word` | WRAM word write |
| `$16` | `EVENT_BREAK_IF_FALSE` | `shortptr` | conditional break |
| `$17` | `EVENT_BREAK_IF_TRUE` | `shortptr` | conditional break |
| `$18` | `EVENT_BINOP_WRAM` | `word`, `byte`, `byte` | WRAM/variable operation |
| `$19` | `EVENT_SHORTJUMP` | `shortptr` | terminal short jump |
| `$1A` | `EVENT_SHORTCALL` | `shortptr` | short call |
| `$1B` | `EVENT_SHORT_RETURN` | - | terminal return |
| `$1C` | `EVENT_SET_ANIMATION_POINTER` | `ptr3` | animation pointer install |
| `$1D` | `EVENT_WRITE_WORD_TEMPVAR` | `word` | tempvar write |
| `$1E` | `EVENT_WRITE_WRAM_TEMPVAR` | `word` | tempvar from WRAM |
| `$1F` | `EVENT_WRITE_TEMPVAR_TO_VAR` | `byte` | variable write from tempvar |
| `$20` | `EVENT_WRITE_VAR_TO_TEMPVAR` | `byte` | tempvar write from variable |
| `$21` | `EVENT_WRITE_VAR_TO_WAIT_TIMER` | `byte` | wait timer write |
| `$22` | `EVENT_SET_DRAW_CALLBACK` | `callbackptr` | C0 callback install |
| `$23` | `EVENT_SET_POSITION_CHANGE_CALLBACK` | `callbackptr` | C0 callback install |
| `$24` | `EVENT_LOOP_TEMPVAR` | - | loop count from tempvar |
| `$25` | `EVENT_SET_PHYSICS_CALLBACK` | `callbackptr` | C0 callback install |
| `$26` | `EVENT_SET_ANIMATION_FRAME_VAR` | `byte` | animation state |
| `$27` | `EVENT_BINOP_TEMPVAR` | `byte`, `word` | tempvar operation |
| `$28` | `EVENT_SET_X` | `word` | position write |
| `$29` | `EVENT_SET_Y` | `word` | position write |
| `$2A` | `EVENT_SET_Z` | `word` | position write |
| `$2B` | `EVENT_SET_X_RELATIVE` | `word` | relative position write |
| `$2C` | `EVENT_SET_Y_RELATIVE` | `word` | relative position write |
| `$2D` | `EVENT_SET_Z_RELATIVE` | `word` | relative position write |
| `$2E` | `EVENT_SET_X_VELOCITY_RELATIVE` | `word` | relative velocity write |
| `$2F` | `EVENT_SET_Y_VELOCITY_RELATIVE` | `word` | relative velocity write |
| `$30` | `EVENT_SET_Z_VELOCITY_RELATIVE` | `word` | relative velocity write |
| `$39` | `EVENT_SET_VELOCITIES_ZERO` | - | velocity clear |
| `$3B` | `EVENT_SET_ANIMATION` | `byte` | animation state |
| `$3C` | `EVENT_NEXT_ANIMATION_FRAME` | - | animation state |
| `$3D` | `EVENT_PREV_ANIMATION_FRAME` | - | animation state |
| `$3E` | `EVENT_SKIP_N_ANIMATION_FRAMES` | `byte` | animation state |
| `$3F` | `EVENT_SET_X_VELOCITY` | `word` | velocity write |
| `$40` | `EVENT_SET_Y_VELOCITY` | `word` | velocity write |
| `$41` | `EVENT_SET_Z_VELOCITY` | `word` | velocity write |
| `$42` | `EVENT_CALLROUTINE` | `callroutine` | native routine bridge |
| `$43` | `EVENT_SET_PRIORITY` | `byte` | priority/state write |
| `$44` | `EVENT_WRITE_TEMPVAR_WAITTIMER` | - | wait timer write from tempvar |

## First Work Packages

### 1. Decoder Coverage Audit

Status: first pass complete in `notes/c3-actionscript-semantics-audit.md`.

Build a report that walks every `event-script-asset`, `event-bytecode-asset`,
and `event-bytecode-label` in `notes/c3-source-data-map.md` and records:

- first opcode
- decoded length before terminal or unknown opcode
- unknown opcode address, if any
- external callback targets
- branch/call targets inside C3
- whether the decode stops by terminal, byte limit, instruction limit, or
  unknown operand shape

This turns the current named-payload manifest into a full C3 script frontier.

### 2. Callback Argument Contracts

`EVENT_CALLROUTINE` is the inline-argument semantic bridge from event bytecode
into native C0/C4/EF helpers. `tools/decode_event_script.py` already has a
`CALL_ARG_COUNTS` seed table; the audit now layers semantic groups and contract
text over those counts. The same audit now also reports installed callback
targets for tick, position-change, draw, and physics callback opcodes. See
[c3-actionscript-callback-contracts.md](notes/c3-actionscript-callback-contracts.md)
for the current callback-contract front door. The next pass should turn generic
inline-byte descriptions into named argument fields where evidence is strong,
and keep promoting callback installer targets out of `UNKNOWN_*`/legacy labels.

High-value callback families:

- C0 current-slot movement and visual profile helpers
- C0 collision/cache wrappers
- C0/C4 installed tick, position, and physics callbacks
- C4 vector, display, and text-yield helpers
- EF timed-delivery row/state helpers

### 3. Reassembly-Friendly Script Family

Status: 140 pilots complete. The current source-pilot frontier reports `0`
remaining candidate bytes.

The integration scaffold is also proven:

- `notes/c3-event-script-source-scaffold.md`: all validated C3 event/actionscript
  source pilots assembled with `3` preserved raw gaps covering non-event or
  source-adjacent data in `C3:0000..E450`.
- `notes/c3-event-script-source-scaffold-validation.md`: the event/script
  scaffold validates `C3:0000..E450` with `0` mismatches.
- `notes/c3-byte-equivalence-validation.md`: the canonical whole-bank scaffold
  validates all `11` C3 protected ranges with `0` mismatches.

- `notes/c3-event-script-source-pilot.md`: movement pulse presets,
  `27` source/data-map rows, `617` validated bytes.
- `notes/c3-timed-delivery-source-pilot.md`: timed-delivery controller proper,
  `C3:43DB..C3:4508`, `301` validated bytes.
- `notes/c3-service-event-movement-source-pilot.md`: adjacent service-event
  movement scripts, `C3:4508..C3:48C4`, `956` validated bytes.
- `notes/c3-service-animation-source-pilot.md`: neighboring service animation
  helpers and events, `C3:48C4..C3:4D39`, `1141` validated bytes.
- `notes/c3-service-presentation-effects-source-pilot.md`: neighboring
  presentation/effect corridor, `C3:4D39..C3:4E73`, `314` validated bytes.
- `notes/c3-itoi-production-intro-source-pilot.md`: first split from the large
  `C3:4E73..C3:5F8B` payload cluster, `C3:4E73..C3:4FC7`, `340` validated
  bytes.
- `notes/c3-intro-presentation-paths-source-pilot.md`: second split from the
  large `C3:4E73..C3:5F8B` payload cluster, `C3:4FC7..C3:51FD`, `566`
  validated bytes.
- `notes/c3-intro-cast-scroll-setup-source-pilot.md`: third split from the
  large `C3:4E73..C3:5F8B` payload cluster, `C3:51FD..C3:5231`, `52`
  validated bytes.
- `notes/c3-intro-cast-member-paths-source-pilot.md`: high-ranked frontier
  seam covering the cast-screen refresh helper task, flat/depth actor
  initializers, and ebsrc scripts 802-803 and 809-825, `C3:5F8B..C3:62C0`,
  `821` validated bytes.
- `notes/c3-teleport-destination-paths-source-pilot.md`: high-ranked frontier
  seam covering the reusable teleport-destination rise/fade helper and ebsrc
  scripts 153-160, `C3:C94E..C3:CC24`, `726` validated bytes.
- `notes/c3-temp-flag-door-close-paths-source-pilot.md`: high-ranked frontier
  seam covering the door-close/temp-flag handoff helpers, ebsrc scripts
  115-119, the shared party-look task, scripts 468-472, and the helper at
  `C3:C143`, `C3:BEA4..C3:C167`, `707` validated bytes.
- `notes/c3-party-look-window-gfx-paths-source-pilot.md`: high-ranked frontier
  seam covering the window-gfx variant loop, ebsrc script 467's random-facing
  idle loop, scripts 465-466 party-look movement paths, and the small
  `$2B32` pulse task at `C3:3DBE`, `C3:3C1D..C3:3DD4`, `439` validated
  bytes.
- `notes/c3-tunnel-ghost-zombie-paths-source-pilot.md`: high-ranked frontier
  seam covering the `C3:B70C` face-target/shake helper plus ebsrc scripts
  73-90, `C3:B70C..C3:BAA3`, `919` validated bytes.
- `notes/c3-tunnel-ghost-follower-paths-source-pilot.md`: high-ranked frontier
  seam covering the tunnel ghost active-area setup helper, party-member tracker,
  event 93, and ebsrc scripts 103-106 follower offset variants,
  `C3:BB5C..C3:BD03`, `423` validated bytes.
- `notes/c3-tunnel-ghost-entity-setup-paths-source-pilot.md`: high-ranked
  frontier seam covering the final tunnel ghost setup corridor after the
  follower variants, including ebsrc scripts 101-102 and 107-114,
  `C3:BD03..C3:BEA4`, `417` validated bytes.
- `notes/c3-vehicle-coordinate-paths-source-pilot.md`: high-ranked frontier
  seam covering the shared obscured vehicle actor initializer and ebsrc scripts
  584-590 taxi/truck/red-car coordinate paths, including the Onett door-close
  gate and Twoson bus-appearance gate, `C3:6A41..C3:6BB4`, `371` validated
  bytes.
- `notes/c3-boogy-tent-city-bus-paths-source-pilot.md`: high-ranked frontier
  seam covering ebsrc scripts 592-596: the Boogy Tent Eye live-area gate, two
  fixed coordinate releases, the city-bus coordinate path, and a
  z-bounce/text-yield visual release, `C3:6BEA..C3:6D18`, `302` validated
  bytes.
- `notes/c3-palette-fade-coordinate-paths-source-pilot.md`: high-ranked
  frontier seam covering the reusable aligned-movement helper at `C3:7439` plus
  ebsrc scripts 633-637: two palette fade/yield loops, a blink-and-release
  path, a coordinate/sound/yield halt path, and a coordinate/text-yield release
  path, `C3:7439..C3:7545`, `268` validated bytes.
- `notes/c3-falling-bounce-yield-paths-source-pilot.md`: high-ranked frontier
  seam covering the shared wait/yield halt at `C3:098B`, ebsrc script 266's
  fixed coordinate move/yield halt, and ebsrc script 267's falling/bounce
  movement release sequence, `C3:098B..C3:0A1F`, `148` validated bytes.
- `notes/c3-pokey-bubble-monkey-paths-source-pilot.md`: high-ranked full-gap
  frontier seam covering the short Z-bounce task and ebsrc scripts 268-283,
  including Pokey staging paths and the first Bubble Monkey route dispatchers,
  `C3:0A1F..C3:0C55`, `566` validated bytes.
- `notes/c3-teleport-destination-prelude-paths-source-pilot.md`: high-ranked
  frontier seam covering teleport-destination prelude helpers before the
  existing `C3:C94E..C3:CC24` pilot: a looping offset jitter task, a pause
  pulse task, ebsrc scripts 147-152, one additional destination-prepare
  variant, and the left-side rise/fade helper at `C3:C90C`,
  `C3:C824..C3:C94E`, `298` validated bytes.
- `notes/c3-bus-tunnel-bridge-paths-source-pilot.md`: high-ranked frontier seam
  covering the bus-tunnel bridge right-side text handoff, ebsrc scripts 453-454
  copied-pose offset party-look halt variants, their shared common tail, and the
  adjacent obscured simple-position actor helper at `C3:DBDB..C3:DBF2`,
  `C3:DB7A..C3:DBF2`, `120` validated bytes.
- `notes/c3-anim-port-flag-switch-source-pilot.md`: high-ranked frontier seam
  covering the tempvar-indexed helper used by ebsrc scripts 688-691 to write
  the two animation-port event flags in all four binary combinations,
  `C3:835D..C3:83BC`, `95` validated bytes.
- `notes/c3-var0-animation-collision-probe-source-pilot.md`: high-ranked
  frontier seam covering the var0-selected animation loop that runs until the
  active entity leaves the live-area window plus the adjacent collision-probe
  refresh task commonly started by movement scripts, `C3:A20E..C3:A271`, `99`
  validated bytes.
- `notes/c3-area-wait-random-wander-helpers-source-pilot.md`: high-ranked
  frontier seam covering common area-aware movement helpers: target-vector
  movement, player active-area leave/enter waits, and a random wander loop,
  `C3:AB67..C3:ABE0`, `121` validated bytes.
- `notes/c3-teleport-flyover-coordinate-helpers-source-pilot.md`: high-ranked
  frontier seam covering two paired coordinate path helpers used by nearby
  teleport/flyover scripts 161 and 164, `C3:CC24..C3:CC94`, `112` validated
  bytes.
- `notes/c3-threed-fight-matent-paths-source-pilot.md`: high-ranked frontier
  seam covering the V3-gated vertical bounce loop at `C3:6BB4` and ebsrc script
  591's `MSG_EVT_THRK_FIGHT_MATENT` text halt, `C3:6BB4..C3:6BEA`, `54`
  validated bytes.
- `notes/c3-position-door-close-helpers-source-pilot.md`: high-ranked frontier
  seam covering paired helpers used by ebsrc scripts 473-475: an opening
  positioning path that starts the party-look task at `C3:C227`, and a
  follow-up coordinate move that plays the door-close sound, `C3:C1E0..C3:C227`,
  `71` validated bytes.
- `notes/c3-position-text-yield-paths-source-pilot.md`: high-ranked frontier
  seam covering the party-look-at-active-entity loop plus ebsrc scripts
  120-132, including text-yield handoffs, fixed coordinate placement helpers,
  temporary-flag wait loops, and short movement releases, `C3:C227..C3:C35D`,
  `310` validated bytes.
- `notes/c3-leftward-bounds-release-paths-source-pilot.md`: high-ranked
  frontier seam covering the shared leftward movement path used by ebsrc scripts
  532-533 plus its concurrent bounds-watch task, `C3:4392..C3:43DB`, `73`
  validated bytes.
- `notes/c3-anim-port-direction-tasks-source-pilot.md`: high-ranked frontier
  seam covering paired tasks used by ebsrc scripts 713-714: a V4/animation-port
  driven direction loop and the adjacent blink animation loop,
  `C3:8978..C3:89BD`, `69` validated bytes.
- `notes/c3-rightward-live-area-bounce-yield-source-pilot.md`: high-ranked
  frontier seam covering the right-facing movement/yield path at `C3:DF90` plus
  its concurrent randomized bounce/downward wait task, `C3:DF90..C3:DFE8`,
  `88` validated bytes.
- `notes/c3-var4-animation-side-step-helpers-source-pilot.md`: high-ranked
  frontier seam covering the V4-controlled animation pulse task used by the
  common `C3:1D4F` setup helper plus paired right/left side-step pulse helpers,
  `C3:1D2D..C3:1D4F` and `C3:1EC1..C3:1EEF`, `80` validated bytes.
- `notes/c3-window-gfx-loader-prologue-source-pilot.md`: high-ranked frontier
  seam closing the compact indexed window-gfx loader prologue immediately before
  the existing party-look/window-gfx pilot, `C3:3BFB..C3:3C1D`, `34` validated
  bytes.
- `notes/c3-tunnel-ghost-warp-text-helpers-source-pilot.md`: high-ranked
  frontier seam covering the compact tunnel-ghost text helpers used by ebsrc
  scripts 87, 88, and 96, `C3:BAA3..C3:BAD7`, `52` validated bytes.
- `notes/c3-movement-vector-core-helpers-source-pilot.md`: high-ranked
  frontier seam covering common movement-vector helpers, including direction
  vector installation, default movement physics/pulse/collision setup, simple
  screen-position callbacks, active-target direction refresh, and movement wait
  completion, `C3:AA1E..C3:AA38` and `C3:AB37..C3:AB67`, `74` validated bytes.
- `notes/c3-facing-pulse-helpers-source-pilot.md`: high-ranked frontier seam
  covering paired two-cycle facing pulse helpers used by nearby scripts 717,
  724, 729, 741, 742, 744, and 755, `C3:7545..C3:756D`, `40` validated bytes.
- `notes/c3-teleport-flyover-pulse-helpers-source-pilot.md`: high-ranked
  frontier seam covering compact teleport/flyover pulse helpers around the
  already-promoted teleport families, `C3:C810..C3:C824` and `C3:CC94..C3:CCB5`,
  `53` validated bytes.
- `notes/c3-sky-runner-electric-effect-helpers-source-pilot.md`: high-ranked
  frontier seam covering the Sky Runner electric-effect spawn/rise helper pair,
  `C3:CEA2..C3:CEC7`, `37` validated bytes.
- `notes/c3-small-terminal-helper-cleanup-source-pilot.md`: high-ranked
  frontier cleanup covering compact terminal helpers: a movement preset/field
  refresh helper, four facing visual countdown pulses, the cast-path release
  tail, the delay-then-release helper, and a single-byte end-task helper,
  `95` emitted bytes, `92` net new frontier bytes after overlap.
- `notes/c3-cast-screen-tenda-king-paths-source-pilot.md`: high-ranked
  frontier seam covering the cast-screen Tenda/King/Ness-posing path cluster
  around ebsrc scripts 845-858, `C3:6834..C3:6A41`, `525` validated bytes.
- `notes/c3-live-area-facing-movement-paths-source-pilot.md`: high-ranked
  frontier seam covering the random facing-cycle helper and ebsrc scripts
  693-695, `C3:83BC..C3:8515`, `345` validated bytes.
- `notes/c3-onett-townhall-movement-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 715-721, including blink/release,
  offset-pose, long Onett town hall movement/dialog, door-sound task, and short
  coordinate movement variants, `C3:89BD..C3:8B7F`, `450` validated bytes.
- `notes/c3-onett-townhall-door-paths-source-pilot.md`: high-ranked frontier
  seam covering the ebsrc script 722-729 continuation: doorway movement paths,
  door open/close sound timing, facing-pulse waits, text-yield handoffs, and the
  longer town hall door-sound movement path, `C3:8B7F..C3:8DB3`, `564`
  validated bytes.
- `notes/c3-position-text-door-sound-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 133-136: the left-facing temp-flag
  movement helper, Kifuya active-area text handoff, random party-following
  movement loop, and door-sound movement/text-yield path, `C3:C35D..C3:C4CF`,
  `370` validated bytes.
- `notes/c3-bubble-monkey-route-paths-source-pilot.md`: high-ranked frontier
  seam covering ebsrc scripts 284-286 and nearby Bubble Monkey route helpers,
  including the shared multi-point coordinate route at `C3:0D3C`,
  `C3:0C67..C3:0DCD`, `358` validated bytes.
- `notes/c3-direction-tracker-townhall-paths-source-pilot.md`: high-ranked
  frontier seam covering the ebsrc script 730-737 prefix, including the
  perpetual direction-tracker task and movement paths that return into it,
  `C3:8DB3..C3:8EF1`, `318` validated bytes.
- `notes/c3-tstage-performance-movement-paths-source-pilot.md`: high-ranked
  frontier seam covering the looping stage-actor vertical bounce helper plus
  ebsrc script 399's long theater-stage performance movement release,
  `C3:2CD2..C3:2DFE`, `300` validated bytes.
- `notes/c3-stage-visual-pulse-paths-source-pilot.md`: high-ranked frontier
  seam covering the stage-facing visual pulse helper, ebsrc script 435's long
  pulse-and-velocity release sequence, and ebsrc script 436's obscured stage
  slide release, `C3:33DD..C3:34FF`, `290` validated bytes.
- `notes/c3-monotoly-coordinate-text-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 699-704, including Monotoly
  movement/dialogue paths and nearby text-yield or wait/release tails,
  `C3:8515..C3:86B2`, `413` validated bytes.
- `notes/c3-tstage-dance-sequence-paths-source-pilot.md`: high-ranked
  frontier seam covering the T-Stage dance helper, ebsrc script 368's staged
  performance sequence, and the paired animation-step helper,
  `C3:1EEF..C3:2138`, `585` validated bytes.
- `notes/c3-gum-machine-flyover-paths-source-pilot.md`: high-ranked frontier
  seam covering the `C3:7559` continuation around ebsrc scripts 638-654,
  including coordinate/text-yield paths and flyover intro text scene dispatches,
  `C3:756D..C3:7A7C`, `1295` validated bytes.
- `notes/c3-flyover-scene-wait-paths-source-pilot.md`: high-ranked frontier
  seam covering the `$0028` low-byte wait helper plus flyover/teleport-adjacent
  scene paths around ebsrc scripts 476-481, `C3:ABE0..C3:AFA3`, `963`
  validated bytes.
- `notes/c3-position-watch-new-entity-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 172-178 through the terminal batch before
  the `C0:A8B3` callback blocker, `C3:D0A4..C3:D1C9`, `293` validated bytes.
- `notes/c3-townhall-direction-common-paths-source-pilot.md`: high-ranked
  frontier seam covering the town hall direction common-tail continuation after
  ebsrc script 737, `C3:8EF1..C3:8FCE`, `221` validated bytes.
- `notes/c3-townhall-coffee-tea-gatekeeper-paths-source-pilot.md`: high-ranked
  frontier seam covering the remaining `C3:899E` town hall continuation,
  coffee/tea battle-overlay transition, and gatekeeper/magic-cake text paths,
  `C3:8FCE..C3:9AC7`, `2809` validated bytes.
- `notes/c3-bus-transition-route-paths-source-pilot.md`: high-ranked frontier
  seam covering the bus/tunnel transition route cluster after the position-watch
  paths, `C3:D1C9..C3:D913`, `1866` validated bytes.
- `notes/c3-twoson-bus-route-paths-source-pilot.md`: high-ranked full-gap
  frontier seam covering ebsrc scripts 64-72: the Twoson bus driver live-area
  dialog loop, bus-to-Threed tunnel routes, return branches, transition snapshot
  handoffs, and short movement/text-yield paths, `C3:B431..C3:B70C`, `731`
  validated bytes.
- `notes/c3-bus-tunnel-desert-route-paths-source-pilot.md`: high-ranked
  full-gap frontier seam covering the bus tunnel/desert/bridge continuation
  around ebsrc scripts 211-220, including route movement, transition snapshot
  handoffs, queued bus text, and recurring driver dialog loops,
  `C3:D913..C3:DB7A`, `615` validated bytes.
- `notes/c3-space-tunnel-crash-paths-source-pilot.md`: high-ranked frontier
  seam covering ebsrc scripts 287-294 plus the brightness task started by
  script 294: Space Tunnel flag/text handoffs, face-target shake paths,
  coordinate routes, Skyrunner crash movement, teleport destination writes, and
  a palette-brightness task, `C3:0DCD..C3:1068`, `667` validated bytes.
- `notes/c3-skyrunner-crash-winter-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 295-302 after the Space Tunnel crash
  batch: Skyrunner crash party tracking, Winters coordinate movement,
  transition releases, teleport destination writes, temp-flag waits, and door
  open/close movement paths, `C3:1068..C3:126E`, `518` validated bytes.
- `notes/c3-party-member-tracker-winter-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 303-310: temp-flag party-member
  tracking, shared party-member/visual-type arrival loops, door-close movement
  release, compact Winters coordinate releases, and the traffic-light wait
  shortcut, `C3:126E..C3:1389`, `283` validated bytes.
- `notes/c3-winters-ride-launch-paths-source-pilot.md`: high-ranked frontier
  seam covering ebsrc scripts 137-139: Winters ride-launch text handoffs,
  launch shake/wander helpers, and coordinate text halt paths,
  `C3:C4CF..C3:C5C6`, `247` validated bytes.
- `notes/c3-early-pose-coordinate-pair-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 225-232: early pose target tracking,
  coordinate-pair movement, and text/yield halt tails, `C3:0295..C3:036F`,
  `218` validated bytes.
- `notes/c3-early-party-look-coordinate-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 233-241: party-member position text
  paths, door-close coordinate release, area-aware follower bounds checks, and
  facing-sequence coordinate movement, `C3:036F..C3:04FA`, `395` validated
  bytes.
- `notes/c3-party-look-meteorite-paths-source-pilot.md`: high-ranked frontier
  seam covering ebsrc scripts 47-49, 53, and 55: party-member tracking/text
  handoffs, a dog-bye active-area text path, and a meteorite/Pokey snapshot
  anchor text release, `C3:AFA3..C3:B06D`, `202` validated bytes.
- `notes/c3-winter-target-release-paths-source-pilot.md`: high-ranked frontier
  seam covering ebsrc scripts 311-316: target visual-type and party-member
  release paths, compact Winters coordinate releases, a direction-common jump,
  and downward transition release, `C3:1389..C3:1452`, `201` validated bytes.
- `notes/c3-onett-door-close-gate-paths-source-pilot.md`: high-ranked frontier
  seam covering the visual-type frame-selector task plus ebsrc scripts 607-613:
  Onett door-close conditional gates, coordinate/text halt paths, and a
  visual-type tracking loop, `C3:6E41..C3:6F08`, `199` validated bytes.
- `notes/c3-onett-door-close-coordinate-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 614-619: chained coordinate/text halt
  paths, a second visual-type tracking loop, and a party-look door-sound
  release path, `C3:6F08..C3:7010`, `264` validated bytes.
- `notes/c3-bus-bridge-obscured-route-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 463-464: a coordinate/text halt and an
  obscured route transition sequence with display-control bit flips,
  `C3:DD4F..C3:DE01`, `178` validated bytes.
- `notes/c3-sky-runner-electric-effect-release-paths-source-pilot.md`:
  high-ranked frontier seam covering ebsrc scripts 163 and 166-169:
  Sky Runner electric-effect reflect/release, rising/fade-out handoffs,
  visual-countdown halt, and downward movement/text release,
  `C3:CEC7..C3:CF76`, `175` validated bytes.
- `notes/c3-window-gfx-sequence-release-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 705-706: window-gfx variant loading
  sequences, a color-math flash task start, sound/text handoffs, and
  flyover-text undraw/restore release paths, `C3:86B2..C3:8751`, `159`
  validated bytes.
- `notes/c3-intro-cast-followup-paths-source-pilot.md`: high-ranked frontier
  seam covering the cast-screen facing pulse helper plus ebsrc scripts 826-829:
  step loops, direction setup halt/release paths, and a leftward movement path
  that waits for cast-screen exit, `C3:62C0..C3:6356`, `150` validated bytes.
- `notes/c3-threed-escaper-appear-paths-source-pilot.md`: high-ranked frontier
  seam covering the stationary var4 pulse helper plus ebsrc scripts 665-666:
  offset-left movement release and the Threed escaper-appear gate,
  `C3:7A7C..C3:7B0B`, `143` validated bytes.
- `notes/c3-bus-bridge-route-terminal-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 455-462: compact bus/bridge coordinate
  moves, recurring driver dialog loops, simple route text halts, and one
  transition snapshot release, `C3:DBF2..C3:DD4F`, `349` validated bytes.
- `notes/c3-battle-swirl-interaction-paths-source-pilot.md`: high-ranked
  frontier seam covering the battle-swirl/enemy-touch wait helper and ebsrc
  scripts 773-778, `C3:9E01..C3:9E8B`, `138` validated bytes.
- `notes/c3-battle-swirl-visual-countdown-paths-source-pilot.md`: high-ranked
  frontier seam covering ebsrc script 776 plus scripts 779-781 visual countdown
  halt variants, `C3:9E8B..C3:9EF2`, `103` validated bytes.
- `notes/c3-npc-attention-path-helpers-source-pilot.md`: high-ranked frontier
  seam covering cached-neighbor setup, NPC attention coordinator gates, and
  terrain/horizontal collision monitor tasks, `C3:A401..C3:A48A`, `137`
  validated bytes.
- `notes/c3-party-member-hop-text-paths-source-pilot.md`: high-ranked frontier
  seam covering the field2B32 vertical oscillation helper and ebsrc script 50
  party-member hop/text release, `C3:B0B6..C3:B13E`, `136` validated bytes.
- `notes/c3-visual-countdown-anchor-followers-source-pilot.md`: high-ranked
  frontier seam covering ebsrc scripts 440-441 plus their shared
  visual-countdown random-wait task, `C3:3549..C3:35B5`, `108` validated bytes.
- `notes/c3-flyover-intro-text-release-paths-source-pilot.md`: high-ranked
  frontier seam covering the battle-swirl footprint visual reset helper and
  ebsrc script 765 flyover intro text release, `C3:9AC7..C3:9AFA`, `51`
  validated bytes.
- `notes/c3-direction-follower-display-reset-paths-source-pilot.md`:
  high-ranked frontier seam covering the compact ebsrc script 4/7 direction
  follower and display reset paths, `C3:A272..C3:A299`, `39` validated bytes.
- `notes/c3-stage-brightness-terminal-helpers-source-pilot.md`: high-ranked
  frontier seam covering three small theater-stage brightness/movement terminal
  helpers, `C3:1D4F..C3:1D6A`, `C3:1DF4..C3:1E14`, and `C3:1E2D..C3:1E4D`,
  `91` validated bytes.

`tools/build_c3_event_script_source_pilot.py` emits these as labeled
macro-source representations while validating against the local ROM bytes.

Candidate/follow-up families for this milestone:

- `C3:A0B2..C3:AB26` movement pulse preset family - pilot complete
- `C3:43DB..C3:4508` timed-delivery controller family - pilot complete
- `C3:4508..C3:48C4` adjacent service-event movement scripts - pilot complete
- `C3:48C4..C3:4D39` neighboring service animation helpers/events - pilot complete
- `C3:4D39..C3:4E73` neighboring service presentation/effect corridor - pilot complete
- `C3:4E73..C3:4FC7` Itoi production intro first split - pilot complete
- `C3:4FC7..C3:51FD` intro/presentation movement paths - pilot complete
- `C3:51FD..C3:5231` intro cast-scroll setup scripts 799-800 - pilot complete
- `C3:5231..C3:5F8B` script 801 cast-scroll/cast-spawn payload - blocked on
  additional native callback contracts and macro coverage before promotion
- `C3:5F8B..C3:62C0` intro cast-member path scripts 802-803 and 809-825 -
  pilot complete
- `C3:3C1D..C3:3DD4` party-look/window-gfx paths scripts 465-467 -
  pilot complete
- `C3:BEA4..C3:C167` temp-flag door-close path scripts 115-119 and 468-472 -
  pilot complete
- `C3:C94E..C3:CC24` teleport-destination paths scripts 153-160 - pilot complete
- `C3:B70C..C3:BAA3` tunnel ghost/zombie paths - pilot complete
- `C3:BB5C..C3:BD03` tunnel ghost follower paths - pilot complete
- `C3:BD03..C3:BEA4` tunnel ghost entity setup paths scripts 101-102 and
  107-114 - pilot complete
- `C3:6A41..C3:6BB4` vehicle coordinate paths scripts 584-590 - pilot complete
- `C3:6BEA..C3:6D18` Boogy Tent/city bus paths scripts 592-596 - pilot complete
- `C3:7439..C3:7545` palette fade/coordinate paths scripts 633-637 - pilot complete
- `C3:098B..C3:0A1F` falling/bounce-yield paths scripts 266-267 - pilot complete
- `C3:0A1F..C3:0C55` Pokey/Bubble Monkey paths scripts 268-283 - pilot complete
- `C3:C824..C3:C94E` teleport-destination prelude paths scripts 147-152 - pilot complete
- `C3:DB7A..C3:DBF2` bus-tunnel bridge paths scripts 453-454 - pilot complete
- `C3:835D..C3:83BC` animation-port flag switch helper - pilot complete
- `C3:4392..C3:43DB` leftward bounds release paths scripts 532-533 - pilot complete
- `C3:8978..C3:89BD` animation-port direction tasks scripts 713-714 - pilot complete
- `C3:DF90..C3:DFE8` rightward live-area bounce/yield helper - pilot complete
- `C3:1D2D..C3:1D4F` and `C3:1EC1..C3:1EEF` V4 animation/side-step helpers - pilot complete
- `C3:3BFB..C3:3C1D` window-gfx loader prologue - pilot complete
- `C3:BAA3..C3:BAD7` tunnel ghost warp/text helpers - pilot complete
- `C3:AA1E..C3:AA38` and `C3:AB37..C3:AB67` movement-vector core helpers - pilot complete
- `C3:7545..C3:756D` facing pulse helpers - pilot complete
- `C3:C810..C3:C824` and `C3:CC94..C3:CCB5` teleport/flyover pulse helpers - pilot complete
- `C3:CEA2..C3:CEC7` Sky Runner electric-effect helpers - pilot complete
- `C3:0C55..C3:0C67`, `C3:3399..C3:33DD`, `C3:6A3E..C3:6A41`,
  `C3:A209..C3:A20E`, and `C3:A271..C3:A272` small terminal helpers - pilot complete
- `C3:6834..C3:6A41` cast-screen Tenda/King paths scripts 845-858 - pilot complete
- `C3:83BC..C3:8515` live-area facing/movement paths scripts 693-695 - pilot complete
- `C3:89BD..C3:8B7F` Onett town hall movement paths scripts 715-721 - pilot complete
- `C3:8B7F..C3:8DB3` Onett town hall door paths scripts 722-729 - pilot complete
- `C3:C35D..C3:C4CF` position/text door-sound paths scripts 133-136 - pilot complete
- `C3:0C67..C3:0DCD` Bubble Monkey route paths scripts 284-286 - pilot complete
- `C3:8DB3..C3:8EF1` direction-tracker/town hall paths scripts 730-737 prefix - pilot complete
- `C3:2CD2..C3:2DFE` theater-stage performance movement path script 399 - pilot complete
- `C3:33DD..C3:34FF` stage visual pulse paths scripts 435-436 - pilot complete
- `C3:A20E..C3:A271` var0 animation/collision-probe helper - pilot complete
- `C3:AB67..C3:ABE0` area-wait/random-wander helpers - pilot complete
- `C3:CC24..C3:CC94` teleport/flyover coordinate helpers - pilot complete
- `C3:6BB4..C3:6BEA` Threed fight Matent paths - pilot complete
- `C3:C1E0..C3:C227` position door-close helpers - pilot complete
- `C3:C227..C3:C35D` position/text-yield paths scripts 120-132 - pilot complete
- `C3:8515..C3:86B2` Monotoly coordinate/text paths scripts 699-704 - pilot complete
- `C3:1EEF..C3:2138` T-Stage dance sequence paths script 368 - pilot complete
- `C3:756D..C3:7A7C` gum-machine/flyover paths scripts 638-654 - pilot complete
- `C3:ABE0..C3:AFA3` flyover scene/wait paths scripts 476-481 - pilot complete
- `C3:D0A4..C3:D1C9` position-watch/new-entity paths scripts 172-178 - pilot complete
- `C3:8EF1..C3:8FCE` town hall direction common paths scripts 738-743 - pilot complete
- `C3:8FCE..C3:9AC7` town hall/coffee-tea/gatekeeper continuation scripts 744-757 - pilot complete
- `C3:D1C9..C3:D913` bus-transition route paths - pilot complete
- `C3:B431..C3:B70C` Twoson bus route paths scripts 64-72 - pilot complete
- `C3:D913..C3:DB7A` bus tunnel/desert route paths scripts 211-220 - pilot complete
- `C3:0DCD..C3:1068` Space Tunnel crash paths scripts 287-294 - pilot complete
- `C3:1068..C3:126E` Skyrunner crash/Winters paths scripts 295-302 - pilot complete
- `C3:126E..C3:1389` party-member tracker Winters paths scripts 303-310 - pilot complete
- `C3:C4CF..C3:C5C6` Winters ride launch paths scripts 137-139 - pilot complete
- `C3:0295..C3:036F` early pose/coordinate-pair paths scripts 225-232 - pilot complete
- `C3:036F..C3:04FA` early party-look coordinate paths scripts 233-241 - pilot complete
- `C3:04FA..C3:069F` early turn-bias/coordinate routes scripts 242-250 - pilot complete
- `C3:069F..C3:0716` early visual-countdown halt scripts 251-254 - pilot complete
- `C3:AFA3..C3:B06D` party-look meteorite paths scripts 47-49, 53, and 55 - pilot complete
- `C3:1389..C3:1452` winter target release paths scripts 311-316 - pilot complete
- `C3:6E41..C3:6F08` Onett door-close gate paths scripts 607-613 - pilot complete
- `C3:6F08..C3:7010` Onett door-close coordinate paths scripts 614-619 - pilot complete
- `C3:DD4F..C3:DE01` bus bridge obscured route paths scripts 463-464 - pilot complete
- `C3:CEC7..C3:CF76` Sky Runner electric-effect release paths scripts 163 and 166-169 - pilot complete
- `C3:86B2..C3:8751` window-gfx sequence release paths scripts 705-706 - pilot complete
- `C3:62C0..C3:6356` intro cast follow-up paths scripts 826-829 - pilot complete
- `C3:7A7C..C3:7B0B` Threed escaper appear paths scripts 665-666 - pilot complete
- `C3:DBF2..C3:DD4F` bus bridge terminal paths scripts 455-462 - pilot complete
- `C3:9E01..C3:9E8B` battle-swirl interaction paths scripts 773-778 - pilot complete
- `C3:9E8B..C3:9EF2` battle-swirl visual countdown paths scripts 776 and 779-781 - pilot complete
- `C3:A401..C3:A48A` NPC attention path helpers - pilot complete
- `C3:B0B6..C3:B13E` party-member hop/text path script 50 - pilot complete
- `C3:3549..C3:35B5` visual-countdown anchor followers scripts 440-441 - pilot complete
- `C3:9AC7..C3:9AFA` flyover intro text release script 765 - pilot complete
- `C3:A272..C3:A299` direction follower/display reset scripts 4 and 7 - pilot complete
- `C3:1D4F..C3:1D6A`, `C3:1DF4..C3:1E14`, and `C3:1E2D..C3:1E4D` stage brightness terminal helpers - pilot complete
- `C3:0295..C3:AB8A` event 222-224 movement helper family
- `C3:2C1C..C3:2CD2` T-Stage long choreography release paths - pilot complete
- `C3:2DFE..C3:2F8D` T-Stage/V-Stage route release paths - pilot complete
- `C3:CF76..C3:CFDE` photo-scene jump release paths - pilot complete
- `C3:A48A..C3:A554` bus-driver attention coordinator paths - pilot complete
- `C3:C15A..C3:C17A` NPC attention wide-distance gate - pilot complete
- `C3:B06D..C3:B35D` meteorite/window party approach paths - pilot complete
- `C3:9AFA..C3:9B4C` bus-driver attention release paths - pilot complete
- `C3:BAD7..C3:BB49` Magic Butterfly PP-restore release paths - pilot complete
- `C3:DB7A..C3:DBF2` Boogy city-bus movement dispatch paths - pilot complete
- `C3:C5C6..C3:C810` Winters ride input and route release paths - pilot complete
- `C3:1452..C3:15F8` winter input/Bubble Monkey routes - pilot complete
- `C3:15F8..C3:176F` winter coordinate/facing routes - pilot complete
- `C3:176F..C3:18D0` winter coordinate transition routes - pilot complete
- `C3:18D0..C3:199E` winter input battle-BG transition paths - pilot complete
- `C3:199E..C3:1B4B` winter battle-BG reload and route release - pilot complete
- `C3:1B4B..C3:1CFB` winter Sanctuary display and pulse release - pilot complete
- `C3:1CFB..C3:1D2D` event 353 message tile reveal - pilot complete
- `C3:A080..C3:A09F` overworld snapshot seed loop - pilot complete
- `C3:A299..C3:A401` traffic-light profile/random-wander paths - pilot complete
- `C3:3DD4..C3:4029` party-look jump and route terminal paths - pilot complete
- `C3:BAEA..C3:BB5C` tunnel-ghost teleport routes - pilot complete
- `C3:3B77..C3:3BFB` photo-scene spin/window-gfx release paths - pilot complete
- `C3:C17A..C3:C1E0` position door-close rotation and target paths - pilot complete
- `C3:A55D..C3:A868` flyover palette/random movement paths - pilot complete
- `C3:4029..C3:4392` party-look registry/random-camera routes - pilot complete
- `C3:0716..C3:098B` early event 255 pose/landing-profile routes - pilot complete
- `C3:5231..C3:5F8B` cast-scroll event 801 spawn sequence - pilot complete
- `C3:7E66..C3:835D` Threed escaper random-text/late-route tails - pilot complete
- `C3:A4AC..C3:AA1E` NPC attention roundwalk/collision/arc-distance tails - pilot complete

The next pilots should emit symbolic event bytecode with labels, opcodes, and
operands while preserving byte-equivalence against the ROM-backed scaffold.
Use `tools/build_c3_source_pilot_frontier.py` to rank ready seams before picking
the next family. At the current checkpoint there are no remaining source-pilot
candidate gaps, so the next work should be semantic polish rather than raw pilot
promotion.

### 4. Non-Event Payload Split

Keep these out of the event VM decoder unless evidence changes:

- intro movement pattern records around `C3:9FF2`
- `C3:F819` battle visual effect-script payload
- `C3:FDBD` delivery placeholder sprite table
- compact raw/frontier data rows in `notes/c3-source-data-map.md`

## Suggested Immediate Target

The movement pulse preset family, timed-delivery controller, adjacent
service-event movement scripts, neighboring service-animation helper/event
cluster, presentation/effect corridor, first Itoi production intro split,
intro/presentation movement paths, cast-scroll setup scripts, intro
cast-member paths, party-look/window-gfx paths, temp-flag door-close paths,
teleport-destination paths, tunnel ghost/zombie paths, tunnel ghost follower
paths, vehicle coordinate paths, Boogy Tent/city bus paths, palette
fade/coordinate paths, falling/bounce-yield paths, teleport-destination prelude
paths, bus-tunnel bridge paths, animation-port flag switch, leftward bounds
release paths, animation-port direction tasks, rightward live-area bounce/yield,
V4 animation/side-step helpers, window-gfx loader prologue, tunnel-ghost warp
text helpers, movement-vector core helpers, facing pulse helpers,
teleport/flyover pulse helpers, Sky Runner electric-effect helpers, small
terminal cleanup helpers, cast-screen Tenda/King paths, live-area facing
movement paths, Onett town hall movement paths, Onett town hall door paths,
position/text door-sound paths, Bubble Monkey route paths, Pokey/Bubble Monkey
paths, direction-tracker town hall paths, theater-stage performance movement
paths, stage visual pulse paths, tunnel ghost entity setup paths, Monotoly
coordinate/text paths, T-Stage dance sequence paths, gum-machine/flyover paths,
flyover scene/wait paths, position-watch/new-entity paths, town hall direction
common paths, town hall/coffee-tea/gatekeeper continuation paths, bus-transition
route paths, Twoson bus route paths, bus tunnel/desert route paths, Space
Tunnel crash paths, Skyrunner crash/Winters paths, party-member tracker Winters
paths, bus bridge terminal routes, Winters ride launch paths, early
pose/coordinate-pair paths, early party-look coordinate paths, party-look
meteorite paths, winter target release paths, Onett door-close gate/coordinate
paths, bus bridge obscured routes, Sky Runner electric-effect release paths,
window-gfx sequence releases, intro cast follow-up paths, Threed
escaper-appear paths, and var0 animation/collision-probe,
area-wait/random-wander, teleport/flyover coordinate, Threed fight Matent,
position door-close helpers, position/text-yield paths, battle-swirl
interaction/visual-countdown paths, NPC attention helpers, party-member hop/text
paths, visual-countdown anchor followers, flyover intro text release,
direction-follower display reset, stage brightness terminal helpers,
animation-port/Pokey paths, battle-swirl recovery paths, Sky Runner
landing/fall handoffs, stage brightness/visual continuations, T-Stage text
continuations, Onett door-close arc/display continuations, cast-screen
orbit/step-spawn continuations, party-member orbit damping, Threed escaper
arc/landing continuations, T-Stage/T-Stage 3 performance corridors, T-Stage
long choreography releases, photo-scene release jumps, meteorite/window party
approach paths, bus-driver attention/Magic Butterfly releases, Winters route
transitions, flyover palette/random movement paths, Winters/Sanctuary
continuations, early turn-bias/visual-countdown halts, traffic-light
random-wander paths, tunnel-ghost teleport routes, party-look jump/route
terminal paths, party-look registry/random-camera routes, cast-scroll event 801,
Threed escaper late-route tails, and NPC-attention roundwalk/collision/arc tails
now have source-form pilots. The refreshed frontier now has `0` remaining gaps
and `0` ready-ranked gaps. The next best C3 work is no longer raw source-pilot
coverage; it is semantic polish: named operand contracts, tighter callback
argument descriptions, source include integration, and stable script-family docs.
