# Phase 2 Semantic Closure Plan

Phase 2 is the semantic closure layer after ROM-wide scaffolding and readable
source-bank closure. The goal is not to prove that the bytes exist in source;
that is already covered by the scaffold and byte-equivalence reports. The goal
is to turn byte-equivalent source, data manifests, traces, and reference
crosswalks into behavior contracts that are reliable enough for romhacking,
review, and future C-port work.

## Baseline

- All configured banks `C0..EF` are scaffold-backed.
- Source-heavy banks `C0`, `C1`, `C2`, `C4`, and `EF` have readable-source
  closure for the current phase.
- C3 has byte-equivalent event/actionscript source-pilot coverage and no
  unexplained raw frontier for this milestone.
- Data, asset, text, and audio banks have generated frontiers and targeted
  contract notes rather than broad unknown-bank inventory.
- ebsrc, EB-M2, and C-port feedback are reference inputs. Local source,
  byte-equivalence, traces, and generated manifests remain the proof layer.

## Workstreams

### 1. C2 Battle Contract Closure

Use `notes/c-port-feedback-intake.md` as the first Phase 2 execution queue.
The concrete trace-oracle queue is `notes/c2-battle-trace-oracle-plan.md`.
Its generated companion is `notes/c2-battle-trace-oracle-index.md` plus
`manifests/c2-battle-trace-oracle-plan.json`, refreshed by
`tools/build_c2_battle_trace_oracle_manifest.py` and checked by
`tools/validate_c2_battle_trace_oracle_manifest.py`.
The execution packet is `notes/c2-battle-trace-oracle-packet.md` plus
`manifests/c2-battle-trace-oracle-packet.json`; it writes ignored local jobs,
traces, and stub results under `build/c2/battle-trace-oracles/` and still
requires a real emulator harness before any behavior claim can be promoted.
Collected result status is summarized in
`notes/c2-battle-trace-oracle-results-summary.md`; schema-only stub results
count as plumbing validation, not trace-observed or proof-grade evidence.
The first real-runner handoff is
`notes/c2-battle-trace-oracle-emulator-handoff.md`; it packages the five
first-pass jobs with SNES CPU-bus breakpoint targets, scenario setup notes,
Mesen address-domain caveats, and exact result/output paths.
Ignored runner assets under
`build/c2/battle-trace-oracles/mesen-runner-assets/` add per-job Mesen Lua
skeletons, operator checklists, command snippets, and unresolved result
templates. These assets are execution plumbing only; they do not count as proof
without a reviewed non-stub result.
`tools/build_c2_battle_trace_oracle_result_from_evidence.py` is the bridge from
reviewed trace evidence into the validated result schema.
`tools/run_c2_battle_trace_oracle_mesen.py` is the local execution wrapper for
those assets; it writes ignored raw traces/run summaries and requires a
local-only battle save state before the first proof capture can be reviewed.
The ignored `build/c2/battle-trace-oracles/local-fixtures.json` config keeps
that local save-state path out of source-controlled notes and commands.
The runner skeletons also accept a small `atom:frames` input pattern, and raw
trace summaries report whether minimum breakpoint hits were actually observed.
The local save-state probe helper can scan ignored or emulator-owned `.mss`
files into `build/c2/battle-trace-oracles/save-state-probes/`; its output ranks
candidate fixtures only and cannot by itself unlock source promotion.
The fixture scout adds a broader local check over ordinary-entry and command
PCs, so existing save states can be ruled in or out before a human spends time
reviewing traces.
The generated D5 row-table crosswalk is
`notes/battle-action-row-crosswalk.md` plus
`manifests/battle-action-row-crosswalk.json`, refreshed by
`tools/build_battle_action_row_crosswalk.py` and checked by
`tools/validate_battle_action_row_crosswalk.py`. It is a navigation artifact
for row `+4` presentation pointers and row `+8` behavior pointers, not a
behavior-promotion source.
Prioritize the contracts that most directly affect a C port:

- C1/C2 target staging and selected action metadata.
- `C2:40A4` current-action payload application.
- `C2:724A` affliction/subgroup writer caller matrix.
- `C2:8125` selected-target damage ABI.
- Healing, PP/resource, stat, and amount-bearing leaves.
- PSI Flash/status gates and EF battle-text result joins.

Expected outputs are refreshed subsystem notes, byte-neutral source comments
where evidence is local, and trace-oracle notes where runtime behavior still
needs proof before source promotion.

### 2. C1/EF Text And Battle-Text Joins

Tighten the contracts where text/menu front ends feed runtime behavior:

- C1 battle menus, item/PSI selection, and target prompts into C2.
- EF battle-text row/pointer payloads back into C2 result text.
- D5 battle-action row `+4` presentation pointers versus row `+8` behavior
  bodies, using the generated crosswalk as the safe join layer.
- Text VM runtime leaves versus localization authoring macros.
- Script/text extraction and reinsertion boundaries for C5..C9 and EF.

Keep localization macro lowering separate from runtime opcode semantics unless
local parser/runtime evidence proves a direct bridge.

### 3. C0/C4 Overworld And Presentation Contracts

Continue subsystem-level polish where static source is strong but side effects
need clearer contracts:

- C0 entity/task, movement, interaction, collision, teleport, input, and audio
  bridge helpers.
- C4 text-tile staging, window/color/HDMA helpers, file-select/town-map
  rendering, credits/photo/cast controllers, and presentation payload islands.
- Cross-bank presentation calls between C0, C1, C2, C4, and EF.

Use emulator probes for PPU, timing, and visual side effects that static source
cannot prove on its own.

### 4. C3 VM, Data, And Source-Emission Semantics

Move C3 and data banks from structural coverage toward source-friendly
contracts:

- Promote event/actionscript operand names, callback argument contracts, and
  control-flow shapes from existing source-pilot evidence.
- Keep bytecode/script source emission conservative until opcode semantics are
  strong enough to round-trip.
- Promote table fields only when consumer evidence proves meaning.
- Preserve unresolved planes and selector bytes numerically with explicit
  source-emission policies.

### 5. Audio Semantics

Keep the source-backed SPC700 work split into two confidence layers:

- Source-backed VCMD labels, argument lengths, and reader paths from the
  checked-in sound-driver source.
- Exact-duration promotion only after local runtime/timing proof.

The priority blockers remain `0x00`, `EF`, `FD`, `FE`, and `0xFF`: distinguish
termination versus return behavior, prove fast-forward timing, and keep `0xFF`
outside the VCMD table unless reader-path evidence proves otherwise.

## Ghidra-SNES Policy

`ghidra-snes v1.0.0-rc1` is installed in the dedicated pilot worktree:
`F:\EB Decomp WT - Ghidra SNES Pilot`.

Use it as a supporting oracle only:

- visual HiROM navigation
- independent `65816:LE:24:snes` decode spot-checks
- confusing cross-bank control-flow inspection
- indirect dispatch/table exploration
- C0/C4/EF presentation/runtime sanity checks

Do not use Ghidra as naming authority, as an automated source replacement path,
or as behavioral proof. Any useful Ghidra observation should be recorded as a
hint in notes/manifests, then confirmed against local source, byte-equivalence,
trace data, or generated manifests before source-facing promotion.

The current pilot result is bounded-positive: EarthBound imports as HiROM with
the SNES ROM Loader, sampled lanes decode sensibly, but the refreshed rc1 dump
did not materially improve EarthBound memory blocks, labels, lane decodes, or
boundaries beyond the prior `v0.2.0` pilot, local source, and crosswalks.

## Validation

- For source-facing edits, run byte-equivalence validation for every touched
  bank.
- For generated manifest/note domains, run the owning builder and validator.
- For roadmap/status changes, rerun source-readiness/readable-source freshness
  checks when the change affects generated dashboards.
- For C2 edge behavior, C4 PPU/timing, and audio duration claims, require local
  trace or emulator evidence before marking behavior as proven.
- Confirm no ROM bytes, scaffold structure, or generated asset payloads change
  unless a task explicitly targets generated artifacts.

## Phase 2 Good-Enough Definition

A subsystem is Phase-2-good-enough when:

- source or data bytes are byte-equivalent and locally navigable
- public names describe stable contracts rather than guesses
- side effects and important WRAM/table fields are documented
- unresolved fields are bounded and preserved numerically
- reference names are crosswalked or aliased without replacing stronger local
  semantics
- future C-port code can identify what is proven, what is inferred, and what
  still needs a runtime oracle
