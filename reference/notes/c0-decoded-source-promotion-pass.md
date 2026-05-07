# C0 Decoded Source Promotion Pass

This note records the C0 source-promotion closure pass. C0 is now fully
source-backed for the current Asar scaffold: every byte in the bank is emitted
from checked-in source, and the generated bank scaffold validates byte-for-byte
against the protected reference bytes.

## Result

- Source-backed C0 modules: `504 / 504`
- Source-backed C0 bytes: `65536 / 65536`
- Remaining protected byte-corridor bytes: `0`
- Remaining protected byte-corridor modules: `0`
- Module files containing decoded 65816 mnemonic lines: `485`
- Decoded mnemonic lines in `src/c0`: `28622`
- Full C0 byte-equivalence: `OK`
- Mismatches: `0`

Validation command:

```powershell
python tools/validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src/c0/bank_c0_helpers_asar.asm --strict
```

`source-backed` means the byte range is represented by checked-in Asar source.
That includes decoded executable 65816 code, mixed code/data units, and explicit
`db` source for tables, headers, and vector payloads. It does not mean every C0
byte is executable code.

## Main Promotion Sweeps

The first two linear promotion sweeps decoded the runtime-heavy C0 ranges:

- `C0:0085..C0:329F`: landing display, scroll setup, entity allocation,
  visual allocation, spawn placement, and early map-strip helpers.
- `C0:329F..C0:6BFF`: party condition, mushroomized walking, bicycle,
  interaction, collision, surface, movement-trigger, and staged movement
  helpers.
- `C0:6E1A..C0:8ED2`: staged movement continuation, NMI/PPU queue handling,
  input playback/recording, frame callbacks, display renderer queues, and
  register update helpers.
- `C0:8FE6..C0:9558`: hardware multiply/division helpers plus delayed action
  and task/actionscript setup.
- `C0:9AC5..C0:A1AE`: action-script target mutation handlers, script opcodes,
  task allocation/list helpers, projection helpers, and cached map-property
  lookup code.
- `C0:A1CE..C0:A60B`: packed map-property selectors, task data rendering,
  physics comparison helpers, position update helpers, and visual profile
  refresh code.
- `C0:A643..C0:B2FF`: action-script wrappers, SPC/APU helpers, battle
  background DMA setup, color math/window helpers, and battle background offset
  table generation.
- `C0:B65F..C0:CEBE` and `C0:CF97..C0:F41E`: intro overworld setup,
  pathfinding, direction/encounter gates, movement-vector helpers, NPC
  attention coordination, delayed actions, teleport state machines, and
  title/intro loop control.

## Final Mixed/Data Closure

The remaining C0 corridors were promoted with explicit table/data source or
split-aware mixed source:

- `C0:0000..C0:0085`: clear draw-sorting table and overworld VRAM setup
  prefix, now promoted to decoded source instead of raw bank-prefix bytes.
- `C0:6BFF..C0:6E1A`: deferred script transition helper, split as code
  `C0:6BFF..C0:6E02` plus data `C0:6E02..C0:6E1A`.
- `C0:8ED2..C0:8FC2`: copy helper, split as code `C0:8ED2..C0:8F9A` plus
  data `C0:8F9A..C0:8FC2`.
- `C0:8FC2..C0:8FE6`: VRAM port triple table tail.
- `C0:9558..C0:9ABD`: script opcode pointer table.
- `C0:9ABD..C0:9AC5`: script target mutation table.
- `C0:9AF9..C0:9B09`: entity script variable pointer table.
- `C0:A1AE..C0:A1CE`: cached map-property shift dispatch table.
- `C0:A20C..C0:A21C`: map buffer page source pointer table.
- `C0:A2AB..C0:A2B7`: physics callback threshold table A.
- `C0:A30B..C0:A317`: physics callback threshold table B.
- `C0:A350..C0:A360`: physics callback comparison dispatch table.
- `C0:A60B..C0:A623`: visual profile direction offset table.
- `C0:A623..C0:A643`: visual profile secondary offset table.
- `C0:AE16..C0:AE1D`: DMA channel flag table.
- `C0:AE1D..C0:AE26`: battle background DMA B-bus register table.
- `C0:AE26..C0:AE34`: battle background DMA source descriptor templates.
- `C0:AE44..C0:AFCD`: inverse DMA channel mask table.
- `C0:B0A6..C0:B0AA`: window mask nibble lookup table.
- `C0:B2FF..C0:B65F`: battle background offset clamp lookup table.
- `C0:C4CF..C0:C4F7`: player direction remap table.
- `C0:CEBE..C0:CF97`: arc-phase turn helper, split as code
  `C0:CEBE..C0:CF58` plus data `C0:CF58..C0:CF97`.
- `C0:F41E..C0:10000`: command-stream frame callback/interpreter payload,
  split as code `C0:F41E..C0:F8C2` plus bank-tail data/header/vector bytes
  `C0:F8C2..C0:10000`.

The `C0:F41E` unit uses explicit accumulator-width entry hints at several
alternate entries and post-`jsl` decode points so the source stays readable:
`C0:F581`, `C0:F61D`, `C0:F668`, `C0:F67A`, `C0:F696`, `C0:F6C3`,
`C0:F6D8`, `C0:F6ED`, `C0:F705`, `C0:F7E9`, `C0:F831`, and `C0:F89A`.
The 2026-05-06 source polish follow-up also names its reference-backed
`C4:EFC4` credits-DMA enqueue calls and final `C0:AD9F` BG3 vertical-scroll
commit.

## Tooling

Added `tools/promote_mixed_range_to_source.py` to promote one manifest range
into explicit source made from ordered code and data spans. The tool verifies
that the supplied spans exactly cover the original range, emits decoded code
with the same external-contract block as the linear source emitter, writes data
spans as `db` lines, and updates the build-candidate manifest so the range has
no protected `data_gaps`.

Example:

```powershell
python tools/promote_mixed_range_to_source.py --bank C0 --module c0_cebe_turn_arc_phase_toward_target_angle --subsystem movement-mixed-source --code C0:CEBE,C0:CF58,TurnArcPhaseTowardTargetAngle --data C0:CF58,C0:CF97,TurnArcPhaseStepTable
python tools/build_source_bank_scaffold.py --bank C0
python tools/validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src/c0/bank_c0_helpers_asar.asm --strict
```

The earlier linear-only helper remains useful for pure-code corridors:
`tools/promote_linear_range_to_decoded_source.py`.

## Follow-up

C0's remaining work is no longer byte-corridor closure. The best follow-up is
polish: tighten symbolic labels inside mixed units, replace raw table bytes
with structured `dw`/`dl`/named constants where safe, and align names with the
cross-bank contracts discovered from C1+.
