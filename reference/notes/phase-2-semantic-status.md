# Phase-2 Semantic Status

Phase 2 is the current semantic refinement layer after first-pass bank coverage
and readable source closure. Its goal is not to prove that every byte exists in a
scaffold; that is already tracked elsewhere. Its goal is to state how well the
repo understands behavior, data contracts, and port-facing meaning.

The execution roadmap for this phase is `notes/phase-2-semantic-closure-plan.md`.

## Baseline

- Bank first-pass coverage is complete for `C0..EF`; those notes are historical
  inventory.
- Source scaffolds are byte-equivalent for the configured banks.
- Readable-source closure is complete for the audited source-heavy banks:
  `C0`, `C1`, `C2`, `C4`, and `EF`.
- Current semantic work is organized by subsystem, VM, data contract, and
  reference-alignment lane rather than by first-pass bank note.
- Ghidra-SNES `v1.0.0-rc1` is installed in the dedicated pilot worktree as a
  supporting visual/decode oracle only; local source, traces, and manifests
  remain authoritative for names and behavior. The refreshed pilot kept the
  successful EarthBound HiROM import but did not materially change sampled
  memory blocks, labels, or lane decodes versus `v0.2.0`.

## Live Semantic Lanes

| Lane | Current Confidence | What Is Strong | What Still Needs Work |
| --- | --- | --- | --- |
| C0 overworld/runtime | Medium-high | Many entity, movement, interaction, collision, teleport, task, input, audio-bridge, and presentation routines have caller-backed names and byte-equivalence validation. | Large subsystem surface; some names are intentionally side-effect-oriented and should keep gaining comments/tests around WRAM contracts. |
| C1 text/menu/UI | Medium-high | Text VM dispatch, menu/front-end corridors, file-select joins, and many text command leaves have manifests and local evidence. | Some final names depend on C2 battle semantics, C4 renderer behavior, and EF text/data payload joins. |
| C2 battle runtime | Medium-high | Action dispatch, target/status/effect families, PSI/common handlers, Final Prayer, and battle visual tails have substantial polish. `notes/c2-runtime-proof-promotion-closeout.md` is now the compact index for evidence promoted from runtime traces into source-facing contracts. Strong promoted lanes include `C2:8125` damage ABI, selected-row HP mutation, amount-text joins, HP-to-zero collapse entry, PSI Magnet transfer routing, Mad Duck loss-only PP reduction, natural Fresh Egg `C1:B3DB -> C2:B930` snapshot export, Flash numb, crying, poison writer paths, and Large Pizza/healing item effects. | Remaining work is narrower: source/status polish for proven lanes, optional broader `C2:B930` item-family coverage, careful status-gate wording without broad unobserved enum promotion, C1/EF battle-text joins, optional collapse-tail timing, and broader caller-family coverage for the damage ABI. |
| C3 event/actionscript VM | Medium | Raw frontier is closed and opcode/operand audit exists. The durable C3 scaffold now includes the event/actionscript source-pilot scaffold for `C3:0000..E450`; that pilot includes 141 source files, 183 spans, and 56,650 validated bytes after promoting the C3:0100/C3:0142 system-screen helpers, while the full bank remains at `12` protected ranges with `0` mismatches. | VM operand semantics, callback contracts, and script-source emission are not yet as mature as the source-heavy runtime banks. |
| C4 presentation/PPU | Medium-high | Text tile staging, window/color/HDMA helpers, town-map/file-select, credits/photo, and presentation islands have local source and contracts. | PPU/color side effects benefit from more subsystem-level comments and emulator probes. |
| C5..C9 text banks | Medium | Text-bank structure and command usage are decoded enough for regression and extraction. | Port-ready text still depends on complete text-command VM and authoring macro semantics. |
| Data/table banks | Medium-high by shape, medium by gameplay label | CF/D0/D5/D7/D8/DA/DC/DF/E0/E1 have table/subrecord contracts, value counts, and source-emission policies. D5 battle-action rows now have a generated crosswalk that separates row `+4` presentation pointers from row `+8` behavior pointers. | Some second planes, selector meanings, and human-facing labels remain numeric until consumer evidence proves names. |
| Audio/SPC700 | Medium-high for source labels, medium for exact duration | Sound-driver source now backs VCMD labels, arg lengths, and reader paths. | Exact duration promotion remains blocked for commands whose runtime timing/effect is not locally proven. |
| EF mixed runtime/data/text | Medium | Save/SRAM, debug/menu, battle-text, map/text/glyph corridors, and late helper regions have improved source closure. | Large text/help/menu runs and some payload joins still need stronger script/data semantics. |
| ebsrc/community alignment | Medium-high as crosswalk, selective as source | Exact-address ebsrc names are integrated or crosswalked with alias-first policy. | Community-preferred names should be added as compatibility aliases only when exact-address and role-compatible. |

## C2 Resource-Lane Update

`notes/psi-magnet-drain-amount.md` records the detailed PP resource evidence:
Paula's PSI Magnet against a Stonehenge Mook proves natural
`C2:9F5E -> C2:721D -> C2:7191` target loss plus capped caster recovery
routing, and Mad Duck proves natural `C2:8E42 -> C2:721D -> C2:7191`
loss-only PP reduction with no caster-side recovery. The remaining work there
is source-facing polish and optional broader coverage, not initial proof
acquisition.

## Confidence Language

- `High`: byte-equivalent, exact-address, local callers and side effects are
  understood, and external references corroborate or do not conflict.
- `Medium-high`: byte-equivalent and locally well explained, but more comments,
  tests, or edge-case proofs would still improve port confidence.
- `Medium`: structure and key consumers are known, but not every operand,
  table field, timing effect, or gameplay-facing label is proven.
- `Low`: reference vocabulary, macro-only evidence, payload-only labels, or
  names without a local reader-path proof.

## Note Ownership

Use these starting points instead of adding new material to first-pass notes:

- Runtime source banks: `notes/runtime-semantic-polish-plans.md`.
- Phase 2 execution roadmap: `notes/phase-2-semantic-closure-plan.md`.
- C-port feedback: `notes/c-port-feedback-intake.md` and
  `notes/c2-battle-trace-oracle-plan.md`, with generated queue
  `notes/c2-battle-trace-oracle-index.md` and execution packet
  `notes/c2-battle-trace-oracle-packet.md`; real-runner setup starts at
  `notes/c2-battle-trace-oracle-emulator-handoff.md` and
  `notes/c2-battle-trace-oracle-mesen-runner.md`, and result intake lives in
  `notes/c2-battle-trace-oracle-results-summary.md`.
- C3 VM: `notes/c3-actionscript-semantics-audit.md` and
  `notes/c3-actionscript-semantics-roadmap.md`; validate the current
  complete-decode/value-readiness contract with
  `tools/validate_c3_actionscript_semantics_audit.py`.
- Text/localization VM: `notes/text-command-semantics-manifest.md` and
  `notes/text-vm-localization-semantics-closeout.md`.
- Data/assets: `notes/asset-data-contract-frontier.md`,
  `notes/battle-action-row-crosswalk.md`, and the bank-specific contract notes
  linked from them.
- Audio: `notes/audio-sequence-command-semantics.md`,
  `notes/audio-exact-duration-triage.md`, and
  `notes/audio-duration-readiness-rollup.md`.
- ebsrc alignment: `notes/ebsrc-community-crosswalk.md` and
  `notes/ebsrc-knowns-integration-candidates.md`.

## Practical Rule

First-pass notes are inventory. Phase-2 notes are evidence. If new work changes
our understanding of behavior, write or update the relevant phase-2 subsystem
note and leave the first-pass note alone unless its original inventory is wrong.
