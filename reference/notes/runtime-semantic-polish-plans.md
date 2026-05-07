# Runtime Semantic Polish Plans

This is the queue-level index for the first runtime semantic polish lane called
out by `notes/source-readiness-triage.md` and `notes/project-status.md`.

## Scope

- Priority banks: `C0`, `C1`, `C2`, `C4`, and `EF`.
- Outcome: one small execution plan per bank before source edits begin.
- Non-goals: no scaffold regeneration, no symbol promotion, no runtime source
  changes, and no generated manifest updates in this planning pass.

## Plan Set

| Bank | Plan | Runtime focus |
| --- | --- | --- |
| `C0` | `notes/c0-runtime-semantic-polish-plan.md` | overworld entity/task, movement, interaction, collision, teleport, presentation |
| `C1` | `notes/c1-runtime-semantic-polish-plan.md` | text engine, menus, battle front ends, file select, C2/C4/EF joins |
| `C2` | `notes/c2-runtime-semantic-polish-plan.md` | battle action dispatch, targeting, status/effects, PSI, Final Prayer, visuals |
| `C4` | `notes/c4-runtime-semantic-polish-plan.md` | renderer contracts, text tiles, HDMA/color/window helpers, presentation |
| `EF` | `notes/ef-runtime-semantic-polish-plan.md` | save/SRAM, debug menus, text/glyph/data corridors, battle-text payload joins |

## Shared Execution Rules

- Treat existing notes as evidence, not as a replacement for local source
  review when implementation starts.
- Promote names and comments subsystem by subsystem; do not run bank-wide
  semantic churn as one monolith.
- Record cross-bank contracts where the caller and callee semantics are both
  understood enough to hold a stable name.
- Keep byte-equivalence validation as the backstop after any future source
  conversion or source-facing semantic edit.

## Shared Documentation Checks

- Each bank plan links back to the primary queue/status docs and the bank
  handoff or synthesis notes that define current state.
- Each bank plan identifies first-pass order, evidence inputs, expected outputs,
  and validation gates.
- This index remains a planning document only; source and manifest changes
  belong to later implementation passes.

## Implementation Status

- 2026-04-30: C0 movement/collision first slice landed as byte-neutral source
  comments plus `notes/c0-movement-collision-runtime-polish.md`.
- 2026-04-30: C0 entity/visual lifecycle second slice landed as byte-neutral
  source comments plus `notes/c0-entity-visual-runtime-polish.md`.
- 2026-04-30: C0 interaction runtime third slice landed as byte-neutral source
  comments plus `notes/c0-interaction-runtime-polish.md`.
- 2026-04-30: C0 teleport state/setup fourth slice landed as byte-neutral
  source comments plus `notes/c0-teleport-state-runtime-polish.md`.
- 2026-04-30: C0 teleport callback fifth slice landed as byte-neutral source
  comments plus `notes/c0-teleport-callback-runtime-polish.md`.
- 2026-04-30: C0 presentation queue/NMI sixth slice landed as byte-neutral
  source comments plus `notes/c0-presentation-queue-runtime-polish.md`.
- 2026-04-30: C0 task allocator/runtime seventh slice landed as byte-neutral
  source comments plus `notes/c0-task-pool-runtime-polish.md`.
- 2026-05-06: C0 intro/battle-overworld initializer follow-up named the
  helper-call surface across `C0:B67F..B967`: delayed-action setup, map/VRAM
  setup, EF debug predicates, C2 instant-win and battle-common joins, C4
  intro/menu-name helpers, continuation-frame snapshots, movement queue
  consumption, bicycle text exit, Magic Truffle/Sanctuary debug helpers,
  teleport mainloop calls, and the party condition-decay gate. See
  `notes/intro-overworld-position-init-c0b65f-c0b67f.md`.
- 2026-05-06: C0 projection/file-select follow-up split the byte-only
  `C0:B2FF..B65F` corridor into the battle BG offset clamp table,
  `C0:B400/C0:B40B` projection helper pair, `C0:B425` sine/projection table,
  and `C0:B525` file-select initialization routine. The intro continuation now
  calls `C0B525_FileSelectInit` by name. See
  `notes/file-select-init-and-projection-c0b2ff-c0b65f.md`.
- 2026-05-06: C0 intro logo/gas-station follow-up regenerated the
  `C0:EFE1..F41E` source with corrected accumulator-width force points, named
  the logo and gas-station entry leaves, and closed the raw helper-call surface
  for C2 battle-bg updates, C4 gas-station/palette helpers, and entity cleanup.
  See `notes/intro-logo-wait-and-gas-station-helpers-c0efe1-c0f21e.md`.
- 2026-05-06: C0 credits command-stream follow-up restored the
  `CREDITS_SCROLL_FRAME` alias, named `C4:EFC4` credits-DMA enqueues and the
  `C0:AD9F` BG3 vertical-scroll commit, and refreshed the `01/02/03/04/FF`
  command-handler interpretation. See `notes/frame-callback-bodies.md`.
- 2026-05-06: C4 credits presentation follow-up connected that C0 callback to
  the installer/playback side by naming the frame-callback install/reset calls,
  credits DMA queue record contract, command-stream WRAM fields, E1:2F8A
  photograph record stride/count, and the `$003B` BG3 scroll progress gate.
- 2026-05-06: C4 cast-scroll presentation follow-up named the event-801
  threshold polling contract, cast BG3 scroll tick callback, `$0BCA` live-Y
  source, `$1002` blank-row upload cursor, `$B4D1` cast-name tile offset,
  `$9641` completion latch, and cast controller cleanup calls.
- 2026-05-06: C4 audio tail follow-up named the music dataset row fields,
  audio pack pointer row shape, US bank resolver mask reset, cold-start
  bootstrap shared pack, `ChangeMusic` primary/secondary/sequence load roles,
  Sound Stone recording transition exception, stereo/mono stream loader, and
  auto-sector music-change latch.
- 2026-04-30: C1 battle front-end first slice landed as byte-neutral source
  comments plus `notes/c1-battle-front-end-runtime-polish.md`.
- 2026-04-30: C1 battle PSI second slice landed as byte-neutral source
  comments plus `notes/c1-battle-psi-runtime-polish.md`.
- 2026-04-30: C1 text gate third slice landed as byte-neutral source comments
  plus `notes/c1-text-gates-runtime-polish.md`.
- 2026-04-30: C1 text entry fourth slice landed as byte-neutral source comments
  plus `notes/c1-text-entry-runtime-polish.md`.
- 2026-04-30: C1 selection prompt fifth slice landed as byte-neutral source
  comments plus `notes/c1-selection-prompt-runtime-polish.md`.
- 2026-05-06: C1 selection-prompt dispatch/core follow-up landed as
  byte-neutral named helper-call polish plus
  `notes/character-selection-prompt-dispatch-c1242e-c12bf3.md`.
- 2026-05-06: C1 debug/window tick follow-up landed as byte-neutral named
  helper-call polish plus
  `notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md`.
- 2026-05-06: C1 open-menu/debug tail follow-up named the reference-backed
  `OPEN_HPPP_DISPLAY`, `SHOW_TOWN_MAP`, debug flag/guide/level/goods helpers,
  and the C0 overworld button edges into those C1 contracts. See
  `notes/open-menu-prelude-helpers-c1339e-c133b0.md` and
  `notes/debug-menu-reachability-c0-c1-ef.md`.
- 2026-05-06: C1 open-menu helper-call follow-up named the main
  `C1:33B0..4103` text-entry, selection, target-prompt, item-transfer,
  HP/PP focus, PSI/equipment/teleport, tick, and cleanup helper edges, with a
  follow-up closing the final AF74/03DC/0FEA raw edges. See
  `notes/open-menu-prelude-helpers-c1339e-c133b0.md`.
- 2026-05-06: C1 small helper cleanup named local edges in the
  interaction-output selectors, active-window descriptor initializer, and
  `$89D4` text-entry constructor chain. See
  `notes/interaction-result-consumers.md` and
  `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`.
- 2026-05-06: C1 low text-command strip follow-up named helper-call edges
  across `C1:4103..4558`: 24-bit target assembly, `JUMP_MULTI` context reads,
  event-flag high-byte assembly, flag set/clear/check, call-text dispatch,
  number selection, context installs, focus/window wrappers, and C4
  glyph/cursor staging. See
  `notes/lower-bank01-text-control-strip-00-17.md`.
- 2026-05-06: C1 adjacent low text-command/inventory follow-up named helper
  edges across `C1:4558..4EAB`, covering workmem/argmem staging,
  character-selection queue builders, print/layout helpers, item-class tests,
  wallet mutations, HP/PP wrappers, inventory give/take/search helpers, and
  preset teleport joins. The current text-context workmem setter label is now
  corrected to `C1:0443`. See
  `notes/lower-bank01-text-control-strip-00-17.md` and
  `notes/text-command-family-1d-inventory-money.md`.
- 2026-05-06: C1 `C1:4EAB..575D` text-command corridor follow-up named the
  helper-call surface for parameterized pause, shop/inventory menus, item
  buy/sell price wrappers, item compatibility, character-name and
  number/money printing, status/ailment helpers, special-selector loaders,
  required-experience staging, Escargo storage cleanup, item insertion, and
  inventory-slot removal. See `notes/text-command-10-parameterized-pause.md`,
  `notes/text-command-family-1c-print-display.md`, and
  `notes/text-command-family-1d-inventory-money.md`.
- 2026-05-06: C1 `C1:575D..621F` inventory/money/delivery corridor follow-up
  named the helper-call surface for equipped-item checks, Escargo pending-item
  queue movement, wallet/ATM amount assembly and mutation, delivery/pickup
  queue storage and reads, food/equipment classification, PSI-name printing,
  and random-number staging. See
  `notes/text-command-family-1d-inventory-money.md`,
  `notes/text-command-family-19-data-and-substitution.md`, and
  `notes/pending-item-queue-984b.md`.
- 2026-05-06: C1 `C1:621F..7440` mixed callback/event tail follow-up named
  helper-call edges for `1F C0`, Jeff repair, level refresh, direction and
  landing snapshot helpers, C0 hotspot/movement joins, C2 battle/respawn
  helpers, C3 battle visual effect dispatch, C4 entity frame/flag/script and
  attached-child helpers, wandering photographer dispatch, and the bank-deposit
  accumulator stager. See `notes/text-command-family-1f-deferred-callbacks.md`,
  `notes/text-command-family-19-data-and-substitution.md`, and
  `notes/bank-deposit-accumulator-98b9-98bb.md`.
- 2026-05-06: C1 `C1:7440..7708` timed-delivery/stat tail follow-up named the
  delivery row sprite/placeholder callback edge, experience amount assembly and
  award handoff, and C2 derived-stat recalculation helpers for the
  IQ/Guts/Speed/Vitality/Luck text-command leaves. See
  `notes/timed-delivery-row-index-command-1f-d3.md` and
  `notes/text-command-family-1e-stat-recovery.md`.
- 2026-05-06: C1 `C1:78F7..7AE3` loaded-string/window-family dispatcher
  follow-up named the `0x18` close/drain/clear/window-switch/status-display
  helper surface plus the managed-slot snapshot edge shared with the timed
  event slot notes. See `notes/text-command-family-18-windows-and-selection.md`
  and `notes/text-command-load-string-pointer-c17796-c17889.md`.
- 2026-05-06: C1 `C1:86B1..8B2C` nested-text executor/callback invoker
  follow-up named the managed-slot, parser-preflight, line/scroll,
  halt/selection, compressed-bank pseudo-opcode, and `00..1F` callback-root
  surfaces. See `notes/nested-text-pointer-and-callback-invoker-c186b1-c18b2c.md`
  and `notes/bank01-text-command-map-00-1f.md`.
- 2026-05-06: C1 `C1:8B2C..90E6` inventory/recovery follow-up named the C2
  party-overlay item hooks, C3 egg-family and HP/PP workers, and C4 equipped
  slot index installers used by inventory mutation and subtype dispatch. See
  `notes/c1-inventory-recovery-runtime-polish.md` and
  `notes/equipment-slot-subtype-dispatch-c19066-c4577d.md`.
- 2026-05-06: C1 `C1:913D..91B0` pending-item queue follow-up named the
  `C3:E977` inventory-slot reader edge in the immediate-store bridge, leaving
  the pending-item queue modules raw-helper-call clean. See
  `notes/pending-item-queue-984b.md` and
  `notes/item-slot-helper-pair-c3e977-c3ee14.md`.
- 2026-05-06: C1 display/equipment follow-up named the last raw helper calls in
  `C1:9437..9A11` and `C1:A795..AA5D`, covering required-experience display,
  equipment slot mutation/refresh, managed text-event snapshots, window update
  helpers, and wallet/status printing. See
  `notes/c1-display-helper-runtime-polish.md` and
  `notes/c1-equipment-runtime-polish.md`.
- 2026-05-06: C1 battle/PSI helper follow-up named the remaining helper-call
  surface in `C1:ADB4`, `C1:C452`, `C1:C853`, `C1:CA06`, `C1:CA72`,
  `C1:CAF5`, and `C1:CB7F`, covering target selection, PSI list/menu refresh,
  window/cursor helpers, and battle-sprite row effect clearing. See
  `notes/c1-battle-front-end-runtime-polish.md` and
  `notes/c1-battle-psi-runtime-polish.md`.
- 2026-05-06: C1 level-up/stat refresh follow-up named the remaining helper
  calls in `C1:D109..DC1C`, covering stat refresh recalculators, random/divide
  helpers, battle-text focus/mode helpers, and the Sound Stone display tail.
  See `notes/level-up-stat-growth-helper-c1d08b.md`.
- 2026-05-06: C1 text-input option strip follow-up named the remaining helper
  calls in `C1:E4BE..EAD6`, covering window update/tick helpers, tile
  attributes, glyph printing, text-system ticks, movement and menu-cell
  selection helpers, sound effects, the local row renderer, and input-buffer
  text-length measurement. See
  `notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md`.
- 2026-05-06: C1 small-tail follow-up named the remaining simple helper edges
  in the battle selection-menu setup, packed window-flavour preview, and
  new-file party setup lanes. C1's residual numeric-call map is now only the
  deferred local structural calls in the character-selection dispatcher.
- 2026-05-06: C0 landing/movement presentation follow-up named helper-call
  surfaces across the early landing profile builders and the movement-strip
  refresh chain through the camera-step accumulator. The pass ties profile
  template/row-cache setup, HDMA dispatch reloads, C4 landing display helpers,
  cached map-property lookups, map-strip uploads, companion producers, and
  transition/music refresh calls back to existing C0/C4/EF contracts.
- 2026-05-06: C0 map-reset/entity visual bridge follow-up named helper-call
  surfaces from the map-strip refresh wrappers through sprite-pose entity
  initialization, visual release, movement-adjacent spawn producers, placement
  tile probes, spawn-list resolution, and candidate placement probes.
- 2026-05-06: C0 movement-adjustment follow-up anchored the merged
  `C0:2C3E..329F` tail entries, named the mushroomized movement swap,
  overworld party runtime reset, horizontal/vertical position adjust helpers,
  and clarified the `C0:449B` input/collision/trigger helper edges.
- 2026-05-06: C0 current-position music refresh follow-up named the
  `C0:68F4..6A1B` track-resolution chain, `$5DD6` current map music track,
  `$5DD4` latched mirror, `$5DDA` cue-suppression latch, `$B549` auto-sector
  music gate, bicycle `C4:FD45` enable/disable calls, and the C0 APU command
  leaves used by C4 `ChangeMusic`.
- 2026-05-06: C1/C2 audio-caller follow-up carried those C0/C4 contracts back
  into text-command and battle/result presentation source. The `1F 00..03`
  leaves now use current-position music-track wording, the deferred queue
  storage is named, and C1/C2 callers that route through `C4:FBBD` now use the
  general `ChangeMusic` contract instead of the inherited Sound Stone alias.
- 2026-04-30: C1 display-helper sixth slice landed as byte-neutral source
  comments plus `notes/c1-display-helper-runtime-polish.md`.
- 2026-04-30: C1 equipment-menu seventh slice landed as byte-neutral source
  comments plus `notes/c1-equipment-runtime-polish.md`.
- 2026-04-30: C1 file-select eighth slice landed as byte-neutral source
  comments plus `notes/c1-file-select-runtime-polish.md`.
- 2026-04-30: C1 inventory/recovery ninth slice landed as byte-neutral source
  comments plus `notes/c1-inventory-recovery-runtime-polish.md`.
- 2026-04-30: C2 target-selection first slice landed as byte-neutral source
  comments plus `notes/c2-target-selection-runtime-polish.md`.
- 2026-04-30: C2 action-dispatch second slice landed as byte-neutral source
  comments plus `notes/c2-action-dispatch-runtime-polish.md`.
- 2026-04-30: C2 stat-consequence third slice landed as byte-neutral source
  comments plus `notes/c2-stat-consequence-runtime-polish.md`.
- 2026-04-30: C2 affliction-recovery fourth slice landed as byte-neutral source
  comments plus `notes/c2-affliction-recovery-runtime-polish.md`.
- 2026-04-30: C2 selected-row controller fifth slice landed as byte-neutral
  source comments plus `notes/c2-selected-row-controller-runtime-polish.md`.
- 2026-04-30: C2 late selected-row controller sixth slice landed as byte-neutral
  source comments plus `notes/c2-late-selected-row-runtime-polish.md`.
- 2026-04-30: C2 PSI common-helper seventh slice landed as byte-neutral source
  comments plus `notes/c2-psi-common-runtime-polish.md`.
- 2026-04-30: C2 PSI Flash eighth slice landed as byte-neutral source comments
  plus `notes/c2-psi-flash-runtime-polish.md`.
- 2026-04-30: C2 late status ninth slice landed as byte-neutral source comments
  plus `notes/c2-late-status-runtime-polish.md`.
- 2026-04-30: C2 PSI animation tenth slice landed as byte-neutral source
  comments plus `notes/c2-psi-animation-runtime-polish.md`.
- 2026-04-30: C2 battle overlay eleventh slice landed as byte-neutral source
  comments plus `notes/c2-battle-overlay-runtime-polish.md`.
- 2026-04-30: C2 battle-background palette twelfth slice landed as byte-neutral
  source comments plus `notes/c2-battle-bg-palette-runtime-polish.md`.
- 2026-04-30: C2 battle-background load/update thirteenth slice landed as
  byte-neutral source comments plus
  `notes/c2-battle-bg-load-update-runtime-polish.md`.
- 2026-04-30: C2 Final Prayer fourteenth slice landed as byte-neutral source
  comments plus `notes/c2-final-prayer-runtime-polish.md`.
- 2026-04-30: C2 battle sprite fifteenth slice landed as byte-neutral source
  comments plus `notes/c2-battle-sprite-runtime-polish.md`.
- 2026-04-30: C2 `SHOW_PSI_ANIMATION` sixteenth slice landed as byte-neutral
  source comments plus `notes/c2-show-psi-animation-runtime-polish.md`.
- 2026-04-30: C2 loaded battle-background frame generator seventeenth slice
  landed as byte-neutral source comments plus
  `notes/c2-loaded-bg-frame-generator-runtime-polish.md`.
- 2026-04-30: C2 STEAL helper eighteenth slice landed as byte-neutral source
  comments plus `notes/c2-steal-runtime-polish.md`.
- 2026-04-30: C2 call-for-help nineteenth slice landed as byte-neutral source
  comments plus `notes/c2-call-for-help-runtime-polish.md`.
- 2026-04-30: C2 item/bomb twentieth slice landed as byte-neutral source
  comments plus `notes/c2-item-bomb-runtime-polish.md`.
- 2026-04-30: C2 Lifeup/fixed-amount healing twenty-first slice landed as
  byte-neutral source comments plus `notes/c2-lifeup-healing-runtime-polish.md`.
- 2026-04-30: C2 asleep-status twenty-second slice landed as byte-neutral source
  comments plus `notes/c2-asleep-status-runtime-polish.md`.
- 2026-04-30: C2 offense/defense stat-action twenty-third slice landed as
  byte-neutral source comments plus
  `notes/c2-offense-defense-stat-actions-runtime-polish.md`.
- 2026-04-30: C2 late stat/resource twenty-fourth slice landed as byte-neutral
  source comments plus `notes/c2-late-stat-resource-runtime-polish.md`.
- 2026-04-30: C2 direct-strange embedded-status twenty-fifth slice landed as
  byte-neutral source labels/comments plus
  `notes/c2-direct-strange-embedded-status-runtime-polish.md`.
- 2026-04-30: C2 concentration/PSI-seal twenty-sixth slice landed as
  byte-neutral source comments plus `notes/c2-concentration-seal-runtime-polish.md`.
