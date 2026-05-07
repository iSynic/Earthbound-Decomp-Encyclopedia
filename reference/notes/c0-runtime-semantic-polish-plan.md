# C0 Runtime Semantic Polish Plan

Primary queue context: `notes/source-readiness-triage.md` and
`notes/project-status.md`.

## Current State

`C0` is structurally closed as a working-name anchored source scaffold. The
handoff in `notes/bank-c0-source-scaffold-handoff.md` reports byte-equivalence
as `OK`, but the source surface still preserves byte corridors rather than
claiming decoded source for the overworld/runtime bank. The working-name pool in
`notes/bank-c0-working-name-proposals.md` is the main promotion input.

## Subsystem Slices

- Entity/task lifecycle: entity slot reset, byte-pool allocation, visual state
  reserve/release, spawned entity setup, task callback records.
- Movement runtime: camera steps, map strip refresh, movement record queues,
  surface compatibility, party trail snapshots, scripted movement modes.
- Interaction runtime: directional input, front-facing probes, interactable
  target resolution, post-transition script hooks.
- Collision and terrain: collision byte reads, footprint probes, surface masks,
  cached map-property lookups, collision cache refresh.
- Teleport and transition: teleport selector state, suppression slots, flyover
  and transition staging, post-transition placement.
- Presentation helpers: landing profile rows, PPU/VRAM transfer queues, display
  waits, audio/display frame callbacks, battle-background load bridge.

## First Pass Order

1. Start with movement plus collision because those routines have the clearest
   subsystem boundary and strong local note coverage.
2. Fold in entity/task lifecycle once movement consumers prove stable slot and
   task-field names.
3. Promote interaction and teleport contracts after movement/collision names are
   settled enough to avoid churn.
4. Finish with presentation helpers where C4 and audio-facing side effects need
   cross-bank wording.

## Evidence Inputs

- `notes/bank-c0-source-scaffold-handoff.md`
- `notes/bank-c0-working-name-proposals.md`
- `notes/bank-c0-progress-audit.md`
- `notes/data-contracts-c0-c2.md`
- `notes/data-contracts-c0-c4.md`
- subsystem notes cited from the working-name proposal evidence column

## Expected Outputs

- A per-slice checklist of labels/comments safe to promote from working names.
- Contract notes for WRAM fields, task records, collision masks, and cross-bank
  C2/C4 helper calls when evidence is strong.
- Future source edits that convert byte corridors only after the slice has local
  note evidence, stable naming, and a byte-equivalence validation path.

## Implementation Notes

- 2026-04-30 first slice: added byte-neutral source comments for the movement
  plus collision path centered on `C0:4C45`, `C0:449B`, `C0:54C9`, `C0:5B7B`,
  `C0:5DE7`, and the `$28DA[slot]` collision/terrain cache wrappers. The
  rollup lives in `notes/c0-movement-collision-runtime-polish.md`.
- 2026-04-30 second slice: added byte-neutral source comments for the early
  entity visual lifecycle centered on `$467E` record allocation, `$4A00`
  visual-memory reservations, `EF:133F` sprite-pose descriptors, C0:1E49 slot
  creation, spawn candidate commits, and release paths. The rollup lives in
  `notes/c0-entity-visual-runtime-polish.md`.
- 2026-04-30 third slice: added byte-neutral source comments for interaction
  runtime centered on C0:404F input mapping, C0:4116/C0:42EF single-facing
  probes, C0:41E3/C0:43BC facing-rotation policy, C0:4279/C0:4452 public
  resolvers, and the type-6/C4 door fallback split. The rollup lives in
  `notes/c0-interaction-runtime-polish.md`.
- 2026-04-30 fourth slice: added byte-neutral source comments for teleport
  state/setup centered on `$9F3F..$9F69` PSI teleport state, transition object
  slots `$18..$1D`, `$5156` snapshots, `$10B6` interaction suppression, and
  the C0:EA99 mainloop shell. The rollup lives in
  `notes/c0-teleport-state-runtime-polish.md`.
- 2026-04-30 fifth slice: added byte-neutral source comments for teleport
  movement/restore callbacks centered on C0:E28F, C0:E516, C0:E674, C0:E776,
  C0:E3C1/C0:E6FE snapshot-ring restores, and success/failure setup paths.
  The rollup lives in `notes/c0-teleport-callback-runtime-polish.md`.
- 2026-04-30 sixth slice: added byte-neutral source comments for the C0
  presentation queue/NMI handoff centered on the `$91/$92/$94/$96/$97` transfer
  ABI, `$0400` queued DMA descriptors, `$99` queue byte throttling, `$2C/$2E`
  scroll-buffer flipping, and NMI scroll commits. The rollup lives in
  `notes/c0-presentation-queue-runtime-polish.md`.
- 2026-04-30 seventh slice: added byte-neutral source comments for the task
  allocator/runtime core centered on `$0A50/$0A52/$0A54`, `$0A9E`, `$0ADA`,
  `$125A`, task-slot callbacks, and the C0:DB0F default dispatcher. The rollup
  lives in `notes/c0-task-pool-runtime-polish.md`.
- 2026-05-06 follow-up: the overworld main-loop button edges in
  `src/c0/c0_b67f_initialize_intro_overworld_scene.asm` now name their C1
  menu/display contracts. The pass covers the debug-menu chord, open-menu
  selection loop, HP/PP display shell, town-map display gate, and check/talk
  object handler. See `notes/debug-menu-reachability-c0-c1-ef.md` and
  `notes/open-menu-prelude-helpers-c1339e-c133b0.md`.
- 2026-05-06 follow-up: the C0 landing/profile and movement-strip presentation
  pass named helper-call surfaces across `C0:030F..097B` and
  `C0:0AC5..17EA`. The pass covers landing profile template/row-cache builders,
  HDMA dispatch reloads, C4 stream/child-anchor and palette mirror edges,
  cached map-property lookups, vertical/horizontal map strip uploaders,
  auxiliary strip controllers, companion spawn producers, camera-step refresh
  calls, and transition/music context helpers. See
  `notes/landing-display-assembly-cluster-c007b6-c4b26b.md`,
  `notes/overworld-walking-stutter-producer-split-c01558-c01ca8.md`, and
  `notes/overworld-camera-step-accumulator-c017ea-c018f2.md`.
- 2026-05-06 follow-up: the C0 map-reset/entity visual bridge pass named
  helper-call surfaces across `C0:19E2..2B55`. The pass covers map-strip refresh
  wrappers, sprite-pose descriptor reads, `$4A00` reservation and `$467E`
  byte-pool allocation/release calls, delayed-action slot construction,
  script/full visual release, movement-adjacent spawn producers, placement tile
  probes, spawn-list resolution, and candidate placement probes. See
  `notes/early-entity-map-reset-family-c019e2-c01a86.md`,
  `notes/c0-entity-visual-runtime-polish.md`, and
  `notes/entity-placement-probe-c0263d-c02668.md`.
- 2026-05-06 follow-up: the C0 movement adjustment and mushroomized tail pass
  added local anchors for the merged `C0:2C3E..329F` entries and named caller
  edges into `C0:2C89`, `C0:2D29`, `C0:2D8F`, and `C0:3017`. The pass also
  clarified `C0:449B`'s input, collision, overlap, trigger, and boundary
  helper calls. See `notes/mushroomized-walking-builders-34de-37d0.md`,
  `notes/position-snapshot-and-movement-tick-c0449b-c05200.md`, and
  `notes/intro-overworld-position-init-c0b65f-c0b67f.md`.
- 2026-05-06 follow-up: the C0 intro/battle-overworld initializer pass named
  the helper-call surface in `src/c0/c0_b67f_initialize_intro_overworld_scene.asm`.
  The pass covers delayed-action setup, overworld VRAM/map load setup, EF debug
  predicates, C2 instant-win and battle-common joins, C4 intro/menu-name helpers,
  the continuation-frame snapshot pair, movement-record consumption, the
  get-off-bicycle text exit, Magic Truffle and Your Sanctuary debug helpers,
  teleport mainloop calls, and the party condition-decay gate. See
  `notes/intro-overworld-position-init-c0b65f-c0b67f.md`.
- 2026-05-06 follow-up: the adjacent `C0:B2FF..B65F` corridor is now a mixed
  source/data unit instead of a byte-only blob. The pass splits the battle BG
  offset clamp table, projection helper pair, sine/projection table, and
  `C0:B525` file-select initialization routine; the intro continuation now
  calls `C0B525_FileSelectInit` by name. See
  `notes/file-select-init-and-projection-c0b2ff-c0b65f.md`.
- 2026-05-06 follow-up: the intro logo/gas-station presentation pass fixed
  two state-aware decode artifacts in `C0:EFE1..F41E`, named the logo-screen
  and gas-station entry leaves, and tied the C2 battle-background update hooks,
  C4 gas-station visual loader, CGRAM mirror, palette fade helpers, and entity
  cleanup call into local source contracts. See
  `notes/intro-logo-wait-and-gas-station-helpers-c0efe1-c0f21e.md`.
- 2026-05-06 follow-up: the C0 credits command-stream callback pass restored
  the `CREDITS_SCROLL_FRAME` alias on `C0:F41E`, named its C4 credits-DMA
  enqueue contract and final BG3 vertical-scroll commit, and replaced the stale
  decode-ambiguity note with command-handler roles for `01/02/03/04/FF`.
  See `notes/frame-callback-bodies.md`.
- 2026-05-06 follow-up: the current-position music refresh pass named the
  `C0:68F4..6A1B` track-resolution chain, `$5DD6` current map music track,
  `$5DD4` latched mirror, `$5DDA` cue-suppression latch, `$B549` auto-sector
  music-change gate, bicycle enable/disable calls into `C4:FD45`, and the C0
  APUIO0/APUIO1/APUIO3 command leaves used by C4 `ChangeMusic`. See
  `notes/c0-current-position-music-refresh-c068f4-c069af.md`.

## Validation

Future implementation passes should use:

```powershell
python tools\promote_working_names_to_source_scaffold.py --bank C0 --force
python tools\build_source_bank_scaffold.py --bank C0
python tools\validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src\c0\bank_c0_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank C0
python tools\build_source_bank_residual_map.py --bank C0
```

This planning pass does not run or require those regeneration steps.
