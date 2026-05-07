# Bank C3 Decompilation Progress Audit

This report cross-checks the local `notes/*.md` corpus against the quarantined `ebsrc-main` US bank include maps and symbol lists.

Treat reference names as corroboration only: a bank entry is not considered understood here just because a side reference gave it a label.

## Bank `C3` / reference bank `03`

- Reference include entries: `1087`
- Reference named include entries without an address in the path: `894`
- Reference address-bearing include entries: `193`
- Address-bearing unknown include entries: `57`
- Reference symbols: `1194` (`868` semantic-ish, `326` placeholder/redirect/null)
- Local notes mention `293` distinct `C3:xxxx` addresses
- Reference addresses mentioned by local notes: `112` / `332`
- Unknown include entries not directly mentioned in local notes: `0`

### Reference-Named Include Families

These are already semantically grouped by `ebsrc-main`; use them as corroborating names, not as final local proof.

- `eventmacros.asm`
- `common.asm`
- `config.asm`
- `structs.asm`
- `symbols/bank00.inc.asm`
- `symbols/bank01.inc.asm`
- `symbols/bank02.inc.asm`
- `symbols/bank03.inc.asm`
- `symbols/bank04.inc.asm`
- `symbols/bank2f.inc.asm`
- `symbols/globals.inc.asm`
- `symbols/misc.inc.asm`
- `symbols/sram.inc.asm`
- `symbols/text.inc.asm`
- `system/display_antipiracy_screen.asm`
- `system/display_faulty_gamepak_screen.asm`
- `data/event_flag_nocontinue_selected.asm`
- `data/ness_pajama_flag.asm`
- `data/events/scripts/221.asm`
- `data/events/scripts/222.asm`
- `data/events/scripts/223.asm`
- `data/events/scripts/224.asm`
- `data/events/scripts/225+226+227.asm`
- `data/events/scripts/228.asm`
- `data/events/scripts/229.asm`
- `data/events/scripts/230.asm`
- `data/events/scripts/231.asm`
- `data/events/scripts/232.asm`
- `data/events/scripts/228+229+230+231+232_common.asm`
- `data/events/scripts/233+234+235+236+237.asm`
- `data/events/scripts/238.asm`
- `data/events/scripts/239.asm`
- `data/events/scripts/240.asm`
- `data/events/scripts/241.asm`
- `data/events/scripts/242+243.asm`
- `data/events/scripts/244.asm`
- `data/events/scripts/245.asm`
- `data/events/scripts/246.asm`
- `data/events/scripts/247+248.asm`
- `data/events/scripts/249.asm`
- `data/events/scripts/250.asm`
- `data/events/scripts/251.asm`
- `data/events/scripts/252.asm`
- `data/events/scripts/253.asm`
- `data/events/scripts/254.asm`
- `data/events/scripts/255.asm`
- `data/events/scripts/256.asm`
- `data/events/scripts/257.asm`
- `data/events/scripts/258.asm`
- `data/events/scripts/259.asm`
- `data/events/scripts/260.asm`
- `data/events/scripts/261.asm`
- `data/events/scripts/262.asm`
- `data/events/scripts/263.asm`
- `data/events/scripts/264.asm`
- `data/events/scripts/265.asm`
- `data/events/scripts/266.asm`
- `data/events/scripts/267.asm`
- `data/events/scripts/268.asm`
- `data/events/scripts/269.asm`
- `data/events/scripts/270.asm`
- `data/events/scripts/271.asm`
- `data/events/scripts/272.asm`
- `data/events/scripts/273.asm`
- `data/events/scripts/274+275+276.asm`
- `data/events/scripts/277.asm`
- `data/events/scripts/278.asm`
- `data/events/scripts/279.asm`
- `data/events/scripts/280.asm`
- `data/events/scripts/281.asm`
- `data/events/scripts/282.asm`
- `data/events/scripts/283.asm`
- `data/events/scripts/284.asm`
- `data/events/scripts/285.asm`
- `data/events/scripts/286.asm`
- `data/events/scripts/287.asm`
- `data/events/scripts/288.asm`
- `data/events/scripts/289.asm`
- `data/events/scripts/290.asm`
- `data/events/scripts/291.asm`
- ... 814 more

### Locally Corroborated Reference Addresses

- `C3:0188` -> notes/c3-intro-script-frontier-9ff2-a07f.md, notes/reference-first-workflow.md
- `C3:0295` -> notes/c3-event-222-224-movement-helper-cluster.md, notes/reference-first-workflow.md
- `C3:43DB` -> notes/c3-temporary-actor-movement-and-release-scripts.md, notes/c3-timed-delivery-controller-working-names.md
- `C3:443E` -> notes/c3-timed-delivery-controller-working-names.md, notes/delivery-row-helpers-ef0e67-ef0ead.md, notes/timed-delivery-controller-499-500-common.md
- `C3:4457` -> notes/c3-timed-delivery-controller-working-names.md, notes/timed-delivery-controller-499-500-common.md
- `C3:447A` -> notes/c3-timed-delivery-controller-working-names.md
- `C3:4488` -> notes/c3-timed-delivery-controller-working-names.md
- `C3:44A8` -> notes/c3-timed-delivery-controller-working-names.md, notes/delivery-row-helpers-ef0e67-ef0ead.md
- `C3:44D2` -> notes/c3-timed-delivery-controller-working-names.md
- `C3:44DE` -> notes/c3-timed-delivery-controller-working-names.md, notes/delivery-row-helpers-ef0e67-ef0ead.md
- `C3:44FF` -> notes/c3-timed-delivery-controller-working-names.md
- `C3:9FF2` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A010` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A01B` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A026` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A02D` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A038` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A07F` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A09F` -> notes/c3-event-222-224-movement-helper-cluster.md, notes/c3-timed-delivery-controller-working-names.md
- `C3:A0B2` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A0C5` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A0D8` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md, notes/c3-event-222-224-movement-helper-cluster.md
- `C3:A12E` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A15E` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A17B` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A18F` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A1DF` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A1F3` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A209` -> notes/c3-temporary-actor-movement-and-release-scripts.md, notes/entity-resolver-script-and-direction-wrappers-c460ce-c4645a.md
- `C3:A20E` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A22C` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A23D` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A24E` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A25F` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A262` -> notes/c3-c0-callback-binding-correction.md, notes/c3-event-222-224-movement-helper-cluster.md, notes/c3-temporary-actor-movement-and-release-scripts.md, +1 more
- `C3:A3A1` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A3B7` -> notes/c3-c0-callback-binding-correction.md, notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A3C9` -> notes/c3-c0-callback-binding-correction.md, notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A401` -> notes/c3-temporary-actor-movement-and-release-scripts.md, notes/entity-overlap-neighbor-cache-c05ece-c064d3.md
- `C3:A426` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A42D` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A434` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A448` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A45C` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:AA38` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md, notes/c3-c0-callback-binding-correction.md, notes/c3-event-222-224-movement-helper-cluster.md
- `C3:AA46` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:AA5A` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:AA6E` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:AA82` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:AA96` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:AAAA` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:AB12` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:AB26` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md, notes/c3-c0-callback-binding-correction.md
- `C3:AB44` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:AB59` -> notes/c3-event-222-224-movement-helper-cluster.md, notes/reference-first-workflow.md
- `C3:AB8A` -> notes/c3-event-222-224-movement-helper-cluster.md, notes/current-slot-position-staging-c46b8d-c46d4b.md
- `C3:AB9E` -> notes/movement-vector-script-runtime-c0c83b-c0d195.md
- `C3:AFA3` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:DFE8` -> notes/pathfinding-consumers-direction-helpers-c0bd96-c0c7db.md
- `C3:E148` -> notes/bank-c0-first-pass.md, notes/front-interaction-flow.md, notes/input-direction-and-interaction-probes-c0402b-c04116.md
- `C3:E158` -> notes/bank-c0-first-pass.md, notes/front-interaction-flow.md, notes/input-direction-and-interaction-probes-c0402b-c04116.md
- `C3:E168` -> notes/bank-c0-first-pass.md, notes/interaction-result-classes.md, notes/interaction-result-consumers.md
- `C3:E1D8` -> notes/c3-map-movement-parameter-table-e1d8-e240.md
- `C3:E1E0` -> notes/c3-map-movement-parameter-table-e1d8-e240.md
- `C3:E200` -> notes/bank-c0-first-pass.md, notes/c3-map-movement-parameter-table-e1d8-e240.md, notes/delayed-action-timer-callers.md, +3 more
- `C3:E208` -> notes/bank-c0-first-pass.md, notes/c3-map-movement-parameter-table-e1d8-e240.md, notes/delayed-action-timer-callers.md, +3 more
- `C3:E210` -> notes/bank-c0-entry-notes.md, notes/bank-c0-first-pass.md, notes/c3-map-movement-parameter-table-e1d8-e240.md, +2 more
- `C3:E218` -> notes/bank-c0-first-pass.md, notes/c3-map-movement-parameter-table-e1d8-e240.md, notes/staged-movement-wrapper-70cb.md
- `C3:E220` -> notes/bank-c0-entry-notes.md, notes/bank-c0-first-pass.md, notes/c3-map-movement-parameter-table-e1d8-e240.md, +3 more
- `C3:E228` -> notes/bank-c0-first-pass.md, notes/c3-map-movement-parameter-table-e1d8-e240.md, notes/delayed-action-timer-callers.md, +2 more
- `C3:E230` -> notes/bank-c0-first-pass.md, notes/c3-map-movement-parameter-table-e1d8-e240.md, notes/front-interaction-flow.md, +1 more
- `C3:E240` -> notes/bank-c0-first-pass.md, notes/c3-map-movement-parameter-table-e1d8-e240.md, notes/front-interaction-flow.md, +1 more
- `C3:E3F8` -> notes/c3-menu-cursor-tile-data-e3f8-e450.md
- `C3:E406` -> notes/c3-menu-cursor-tile-data-e3f8-e450.md
- `C3:E40E` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md, notes/c3-menu-cursor-tile-data-e3f8-e450.md
- `C3:E41C` -> notes/c3-menu-cursor-tile-data-e3f8-e450.md
- `C3:E44C` -> notes/active-text-entry-chain-layout-c451fa.md, notes/c3-menu-cursor-tile-data-e3f8-e450.md, notes/c3-window-text-source-helper-corridor-e450-e7e3.md
- `C3:E450` -> notes/c3-menu-cursor-tile-data-e3f8-e450.md, notes/c3-window-text-source-helper-corridor-e450-e7e3.md, notes/text-engine-entry-waits-window-gates-c10000-c102d0.md
- `C3:E4EF` -> notes/c3-shared-helper-working-name-promotion.md, notes/c3-window-lifecycle-source-contract-e4ef-e6f7.md, notes/c3-window-text-source-helper-corridor-e450-e7e3.md, +1 more
- `C3:E6F8` -> notes/c2-window-hppp-and-menu-selection-helpers-c20266-c2108c.md, notes/c3-focused-party-hppp-actor-clear-e6f8.md, notes/text-entry-record-builder-neighbors-c10f40-c11887.md
- ... 32 more

### Local-Only Address Mentions

These may be derived local discoveries, cross-bank targets, or address forms absent from the reference include/symbol map.

- `C3:0000` -> notes/landing-and-coffee-tea-visual-helpers-c492d2-c49d1e.md
- `C3:0100` -> notes/c3-intro-script-frontier-9ff2-a07f.md, notes/c4-system-error-screen-render-0b51-0b75.md
- `C3:0142` -> notes/c4-system-error-screen-render-0b51-0b75.md
- `C3:0298` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:029E` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:02A4` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:02A8` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:02AB` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:0E40` -> notes/seam-scout-c0-gap-cluster-329f-3f1e.md
- `C3:43E8` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:444D` -> notes/c3-timed-delivery-controller-working-names.md, notes/timed-delivery-controller-499-500-common.md
- `C3:447D` -> notes/c3-timed-delivery-controller-working-names.md, notes/timed-delivery-controller-499-500-common.md
- `C3:4499` -> notes/c3-timed-delivery-controller-working-names.md
- `C3:44A7` -> notes/c3-timed-delivery-controller-working-names.md
- `C3:44C1` -> notes/c3-timed-delivery-controller-working-names.md
- `C3:44EE` -> notes/c3-timed-delivery-controller-working-names.md
- `C3:99F1` -> notes/inventory-slot-removal-helper-c18c27.md, notes/item-slot-helper-pair-c3e977-c3ee14.md
- `C3:A002` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A043` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A047` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A04A` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A04E` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A052` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A054` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A056` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A057` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A05B` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A05E` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A061` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A064` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A066` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A067` -> notes/bicycle-transition-and-party-registry-c03c25-c03f1e.md, notes/seam-scout-c0-gap-cluster-329f-3f1e.md
- `C3:A06A` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A06E` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A072` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A076` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A07A` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A07C` -> notes/c3-intro-script-frontier-9ff2-a07f.md
- `C3:A0A1` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:A0A3` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:A0A7` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:A0A9` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:A0AB` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:A0AF` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:A0B4` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A0B6` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A0BA` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A0BC` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A0BE` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A0C2` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A0EB` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A0FE` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A111` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md, notes/c3-c0-callback-binding-correction.md, notes/c3-event-222-224-movement-helper-cluster.md, +1 more
- `C3:A113` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A115` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A118` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A11A` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A11E` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A120` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A122` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A125` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A127` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A12B` -> notes/c3-actionscript-movement-pulse-presets-a0b2-ab26.md
- `C3:A204` -> notes/c3-temporary-actor-movement-and-release-scripts.md, notes/entity-resolver-script-and-direction-wrappers-c460ce-c4645a.md
- `C3:A234` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A266` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:A26E` -> notes/c3-event-222-224-movement-helper-cluster.md
- `C3:A2AA` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A381` -> notes/c3-c0-callback-binding-correction.md, notes/c3-temporary-actor-movement-and-release-scripts.md, notes/movement-target-bounds-and-vector-refresh-c46ef8-c47369.md
- `C3:A384` -> notes/c3-c0-callback-binding-correction.md
- `C3:A386` -> notes/c3-c0-callback-binding-correction.md
- `C3:A389` -> notes/c3-c0-callback-binding-correction.md
- `C3:A38C` -> notes/c3-c0-callback-binding-correction.md
- `C3:A390` -> notes/c3-c0-callback-binding-correction.md
- `C3:A396` -> notes/c3-c0-callback-binding-correction.md
- `C3:A39E` -> notes/c3-c0-callback-binding-correction.md
- `C3:A3D6` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A3E7` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:A47C` -> notes/c3-temporary-actor-movement-and-release-scripts.md
- `C3:AA3B` -> notes/c3-c0-callback-binding-correction.md, notes/c3-event-222-224-movement-helper-cluster.md
- ... 101 more

## Suggested Workflow

1. Pick an unmentioned `unknown/...` chunk from this report.
2. Run `tools/decode_snippet.py` or a targeted helper around the address.
3. Cross-check `refs/ebsrc-main` symbols, `refs/earthbound-disasm-legacy`, and any data table in `refs/eb-decompile-4ef92` that the routine touches.
4. Write a focused note that states byte-level evidence, borrowed reference names, remaining uncertainty, and direct callers/xrefs.
5. Rerun this audit and promote the next gap.

