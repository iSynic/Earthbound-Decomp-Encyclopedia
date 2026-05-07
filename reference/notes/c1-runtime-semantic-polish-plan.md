# C1 Runtime Semantic Polish Plan

Primary queue context: `notes/source-readiness-triage.md` and
`notes/project-status.md`.

## Current State

`C1` is ready for semantic promotion rather than corridor closure. The main
navigation layer is `notes/bank-c1-subsystem-and-symbol-synthesis.md`, with
candidate names in `notes/bank-c1-working-name-proposals.md`. Some final names
depend on C2 battle internals, C4 renderer behavior, and EF save/text helpers.

## Subsystem Slices

- Text engine and menu core: text entry/wait gates, window focus, low-level
  rendering primitives, character select prompt, menu open helpers.
- Text command leaves: dispatcher leaves for flags, jumps, work memory,
  inventory/money, recovery, teleport, timed events, and special events.
- Battle front ends: target selection, battle PSI user selection, battle item
  action selection, battle text display, HP/PP window redirects.
- Equipment and file-select flows: equipment menu controller, derived equipment
  caches, naming buffer, window-flavour preview, copy/delete/setup menus.
- Cross-bank joins: C2 battle action/result flow, C4 renderer and text-tile
  helpers, EF save/menu data routines and substitution payloads.

## First Pass Order

1. Start from the C1/C2 battle-facing loop recommended by
   `notes/bank-c1-subsystem-and-symbol-synthesis.md`: `C1:ADB4`,
   `C1:CE85`, `C1:CFC6`, and `C1:DC1C`.
2. Promote battle front-end names only with matching C2 action/status evidence.
3. Tighten text command leaves and menu/file-select names after renderer and EF
   calls are labeled with stable contract wording.
4. Leave parser-only compressed-bank pseudo-opcode and localization macro work
   to the existing text VM follow-up queues unless a concrete C1 source edit
   needs it.

## Evidence Inputs

- `notes/bank-c1-subsystem-and-symbol-synthesis.md`
- `notes/bank-c1-working-name-proposals.md`
- `notes/bank-c1-progress-audit.md`
- `notes/text-command-semantics-manifest.md`
- `notes/text-vm-localization-semantics-closeout.md`
- `notes/c2-ef-battle-text-contract-workahead.md`

## Expected Outputs

- Stable promoted names for high-confidence C1 text/menu/battle/file-select
  routines.
- Cross-bank contract notes for C1 callers into C2, C4, and EF, especially
  battle target/result text and file-select save helper paths.
- Deferred-item notes for names that remain provisional because their callee
  side is not yet semantically polished.

## Validation

Future implementation passes should rerun C1 source scaffold validation after
any source-facing edits:

```powershell
python tools\build_source_bank_scaffold.py --bank C1
python tools\validate_source_bank_byte_equivalence.py --bank C1 --module all --combined --scaffold src\c1\bank_c1_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank C1
python tools\build_source_bank_residual_map.py --bank C1
```

This planning pass is documentation-only.

## Implementation Notes

- 2026-04-30: First C1 battle front-end slice landed as byte-neutral source
  comments plus `notes/c1-battle-front-end-runtime-polish.md`. The promoted
  contracts cover the D5:7B68 target resolver, D5:5000 item action bridge,
  battle item-selection loop, and C1:DC1C battle-text pointer wrapper.
- 2026-04-30: Second C1 battle PSI slice landed as byte-neutral source
  comments plus `notes/c1-battle-psi-runtime-polish.md`. The promoted
  contracts cover the D5:8A50 PSI ability row fields, PSI user/category/entry
  selection helpers, PP guard, target handoff, and final menu-selection
  writeback.
- 2026-04-30: First C1 text/menu-core slice landed as byte-neutral source
  comments plus `notes/c1-text-gates-runtime-polish.md`. The promoted
  contracts cover pointer staging, wait-frame pumping, focus/window drains,
  prompt gates, halt-control handling, text-state waits, and active descriptor
  lookup.
- 2026-04-30: Second C1 text/menu-core slice landed as byte-neutral source
  comments plus `notes/c1-text-entry-runtime-polish.md`. The promoted
  contracts cover `$89D4` active text-entry records, constructors,
  chain count/layout/render helpers, selection update helpers, and active-window
  clear behavior.
- 2026-04-30: Third C1 text/menu-core slice landed as byte-neutral source
  comments plus `notes/c1-selection-prompt-runtime-polish.md`. The promoted
  contracts cover `$AD56/$AD58` candidate counts, `$AD5A/$AD6A` candidate
  bytes, scan/eligibility helpers, two-list prompt control, simple side prompt
  control, and the conservative C1:242E dispatcher boundary.
- 2026-04-30: C1 display-helper slice landed as byte-neutral source comments
  plus `notes/c1-display-helper-runtime-polish.md`. The promoted contracts
  cover item-name, statistic-selector, PSI/small-label, and target-prompt
  display adapters.
- 2026-04-30: C1 equipment-menu slice landed as byte-neutral source comments
  plus `notes/c1-equipment-runtime-polish.md`. The promoted contracts cover
  item byte `+0x19` slot-family dispatch, item parameter `+0x1F` preview and
  comparison use, live slots `$99FF/$9A00/$9A01/$9A02`, shadow slots
  `$9CD0..$9CD3`, comparison markers `$9A1D..$9A20`, shop item selection joins,
  and the top-level party equipment controller.
- 2026-04-30: C1 file-select slice landed as byte-neutral source comments plus
  `notes/c1-file-select-runtime-polish.md`. The promoted contracts cover
  save-slot status bytes `$B49E..$B4A0`, selected slot `$B4A1`, action/copy/delete
  menu results, EF save-copy/delete/setup helper calls, setup bytes
  `$98B6/$98B7/$99CD`, the file-select session wrapper, and the lead-entity
  redraw predicate.
- 2026-04-30: C1 inventory/recovery helper slice landed as byte-neutral source
  comments plus `notes/c1-inventory-recovery-runtime-polish.md`. The promoted
  contracts cover the 14-byte inventory list `$99F1..$99FE`, live equipment-slot
  index maintenance during removal, active-party wildcard scans from `$986F`,
  item-family insertion/removal side effects, and the HP/PP recovery/depletion
  target-selection quartet.
- 2026-04-30: C1/C2 battle action-selection join polish landed as byte-neutral
  source aliases/comments. The promoted contracts name the C1 far-call wrapper
  table entries for menu, character prompt, item selection, and PSI category
  selection, plus the `C1:CFC6/CE85` battle item-selection record and
  `D5:5000` item-row fields consumed by the target/action resolver.
- 2026-05-01: C1 battle-text wrapper contract polish landed as byte-neutral
  source aliases. The promoted contracts name the caller-frame pointer slots,
  `$98B1/$0065` battle-text gate, `$9643` mode latch, prompt-wait and
  mode-1/no-prompt display values, and the primary script versus substitution
  payload argument pairs for `C1:DC1C`, `C1:DC66`, `C1:DD82`, and `C1:DD9F`.
- 2026-05-01: C1 substitution-slot leaf polish landed as byte-neutral source
  aliases. The promoted contracts tighten the `0x19 0x1E/0x1F`
  display-text loaders, `$9D11` byte payload, `$9D12/$9D14` pointer payload,
  DP-frame alias shifts, and the `DD7C/DD82` far wrappers that bridge C2/EF
  battle-text scripts into the local display-text engine.
- 2026-05-01: C1 text-command `0x19` tail polish landed as byte-neutral source
  aliases. The promoted contracts name the `0x19 21..28` helper-pointer tail,
  the mushroomized selector byte loader, item equipment-class return values,
  and the `0x19 27` statistic-selector value staging path through `C3:EE7A`
  and `C1:045D`.
- 2026-05-01: C1 statistic-selector character polish landed as byte-neutral
  source aliases. The promoted contracts name the `0x19 28` `C4:550F`
  selector-table walk, current text-context character index, out-of-range zero
  result, and display-text staging pair used before `C1:045D`.
- 2026-05-01: C1 loaded-string collector polish landed as byte-neutral source
  aliases. The promoted contracts name the `0x19 02` inline byte collector,
  `$97D7/$97CA` loaded-string buffer/count, `$97BA..$97BC` companion-byte queue,
  packed companion metadata path into `C1:13D1`, and the `0x19 14` Escargo
  storage byte staging path.
- 2026-05-01: C1 delivery/pickup queue polish landed as byte-neutral source
  aliases. The promoted contracts name the `0x19 1C/1D` deferred argument
  bytes, three-entry queue rooted at `$97F5`, owner/source and item-byte side
  fields, pending-item versus inventory-removal paths, and primary/secondary
  text-context output staging.
- 2026-05-01: C1 inventory/storage/count text-command polish landed as
  byte-neutral source aliases. The promoted contracts name the `0x19 19`
  character inventory-slot item read, `0x19 1A` Escargo storage item byte read,
  and `0x19 1B` loaded-string count helper, including primary and secondary
  text-context staging outputs.
- 2026-05-01: C1 status/experience text-command polish landed as byte-neutral
  source aliases. The promoted contracts name the `0x19 16` status-group byte
  read through `C4:58AF`, `0x19 05` nonbattle status write through `C4:58FE`,
  and `0x19 18` required-experience remaining helper through `C4:599A`.
- 2026-05-01: C1 character identity text-command polish landed as byte-neutral
  source aliases. The promoted contracts name the `0x19 10` active overworld
  registry type-code read and the `0x19 11` character-name letter lookup
  through `C2:22D3`, including current text-context indexing and primary
  text-context result staging.
- 2026-05-01: C1 battle-text ABI follow-up landed as byte-neutral source
  comments/constants. The promoted contracts now distinguish the one-pointer
  `DC1C` lane, the primary-script plus `$9D12/$9D14` payload lane at `DC66`,
  the pointer-only staging lane at `DD82`, the mode-1/no-prompt action-table
  lane at `DD9F`, and the `19 1E/19 1F/1C 0F` text-command consumers.
- 2026-05-01: C1 display-text payload consumer polish landed as byte-neutral
  comments/constants. The `19 1E` pointer-substitution leaf now names its
  `$9D12/$9D14` source, and the `1C 0F` amount-print branch in the dynamic
  selector corridor now names `C1:AD26`, `$0E/$10` staging, and `C1:0DF6`.
- 2026-05-05: C1 battle item-use bridge follow-up tightened the adjacent
  `C1:AF73..B5B6` lane now that C2 action-table vocabulary is stable. The
  promoted source constants name the `D5:5000` item config row fields,
  `D5:7B68 +0x04/+0x08` action-row text pointers, fixed C7 item-use failure
  text pointers, CF:8985 fallback text lookup, the `$9FAC` handoff row, and the
  `$9FFA` battle selection snapshot copied back into `$99DC`. See
  `notes/battle-targetting-resolver-c1adb4-af50.md`,
  `notes/battle-item-action-selection-c1ce85-c1cfc6.md`, and
  `notes/battle-choice-text-family-c1b2ec-b997.md`.
- 2026-05-05: C1 battle PSI controller/formatter follow-up aligned
  `C1:C8BC` and `C1:CB7F..CE73` with the same D5 action-table vocabulary. The
  promoted constants name `D5:8A50` PSI ability rows, `D5:7B68` action rows,
  action row `+0x03` PP cost, encoded `C3:F124` menu-entry rows, the fixed
  `C3:F11C` tail, the PP guard current-PP mirror, and final battle-menu
  selection record offsets. See `notes/c1-battle-psi-runtime-polish.md`,
  `notes/battle-psi-menu-controller-c1cc39-ce73.md`, and
  `notes/battle-psi-name-builder-family-c1c8bc-ca06-c3f112-f124.md`.
- 2026-05-05: C1 outer battle PSI user-selection follow-up tightened
  `C1:B5B6..BB71` after the lower controller vocabulary stabilized. The
  promoted constants name `$9D16/$9D18/$9D19` as selected-user, fast-path, and
  highlight-row bytes, the PP guard and category-8 blocker/event branch, the
  `D5:8A50` ability-row to `D5:7B68` action-row joins, and the ordinary
  `$9FFA/$A972` snapshot export plus `$99DC` state mirror copyback. See
  `notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md`,
  `notes/c1-battle-psi-runtime-polish.md`, and
  `notes/battle-selection-snapshot-export-c2b930.md`.
- 2026-05-05: C1 battle text/equipment tail follow-up tightened
  `C1:DD9F..E1A2`. The promoted constants name the `D5:7B68` Bash/Shoot
  text and companion-payload offsets, selected-row item/equipment/stat and
  resistance fields, party inventory and equipped-slot bases, C7 equip-ok and
  cannot-use-weapon scripts, D5 item equipment flags, and the C1/C2/C3/C4
  helper calls used to remove items, refresh equipment subtype caches, convert
  resistance bytes, and redraw focused HP/PP rows. See
  `notes/battle-text-entry-tail-dd82-dd9f.md`,
  `notes/battle-text-entry-family-c1dc1c-dd7c.md`, and
  `notes/c2-ef-battle-text-contract-workahead.md`.
- 2026-05-06: C1 text-command `1F 00..03` music/sound polish landed alongside
  the C2 wrapper pass. The promoted constants name the C2 music-track mirror
  applier, stop-music redirect, play-sound/light-window-tick wrapper, and the
  C0 current-position music-track getter used by the restore-current-map-music
  branch. See `notes/text-command-family-1f-deferred-callbacks.md` and
  `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`.
- 2026-05-06: C1/C2 audio-caller vocabulary follow-up normalized the same lane
  against the C0/C4 contracts. C1 now names the deferred `1F 00` queued-byte
  storage and the `1F 03` current-position music-track getter, while file
  select, level-up/Sound Stone display, and the C2 battle/result presentation
  joins use `C4FBBD_ChangeMusic` instead of the narrower inherited Sound Stone
  alias. See `notes/text-command-family-1f-deferred-callbacks.md` and
  `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`.
- 2026-05-06: C1 text-command `1F 64/65` temporary party source polish landed
  in the dynamic source-selector corridor. The promoted constants name the C2
  save-and-clear and restore helpers at `C2:3008/307B`, tying the C1 leaves to
  the existing C2 temporary source block contract. See
  `notes/text-command-family-1f-deferred-callbacks.md` and
  `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`.
- 2026-05-06: C1 text-command `1F A0/A1/A2` current interaction flag polish
  landed in the same corridor. The promoted constants name the C2 set/clear
  and get wrappers at `C2:26C5/26E6`, including the `$9C88` current flag id
  and `$5D64` refresh contract. See
  `notes/text-command-family-1f-deferred-callbacks.md` and
  `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`.
- 2026-05-06: C1 text-command `1F B0` save-game polish landed in the same
  corridor, with the debug-menu save command folded into the same named edge.
  The promoted constant names the C2 save-current-game wrapper at `C2:2A2C`,
  which converts `$B4A1` from one-based current save slot to the zero-based
  `EF:0A4D` save-slot index. See
  `notes/text-command-family-1f-deferred-callbacks.md` and
  `notes/c2-party-inventory-status-utility-corridor-c216ad-c2307b.md`.
- 2026-05-06: C1 file-select loop polish tightened the `F616..FF2C` setup and
  new-file branch source. The promoted constants name the file-select action,
  copy, delete, text-speed, sound, and window-flavour helpers; the C4
  file-select pose/entity helpers; the C3 party-overlay sync tail; and the EF
  `SaveGameSlot` setup-persistence edge. See
  `notes/c1-file-select-runtime-polish.md`,
  `notes/file-select-setup-option-menus-c1f497-c1f616.md`, and
  `notes/ef-save-sram-runtime-polish.md`.
- 2026-05-06: C1 display-text dynamic source selector polish tightened
  `C1:7B56..866D` source edges. The promoted constants cover the `0x1A`
  menu/result staging leaves, `0x1C 0D/0E/0F` battle-name and action-amount
  display payload consumers, text-context snapshot/restore helpers, text input
  lock/wait gates, transition music restore, interaction-flag helpers, and
  save-current-game wrapper. See
  `notes/display-text-dynamic-source-selector-dispatch-c17b56-c1866d.md`,
  `notes/text-command-family-1a-menus.md`, and
  `notes/text-command-family-1c-print-display.md`.
- 2026-05-06 follow-up: the remaining raw-call edges in
  `src/c1/c1_7b56_dispatch_display_text_dynamic_source_selector.asm` are now
  promoted to local contracts. The source names the C0 position-context lookup
  and bicycle-entry helper, C4 auto sector-music latch, Magic Truffle direction
  lookup, selected-mode clear helper, and the C1 active-window glyph-mode flag
  writer at `0FAC`. See
  `notes/display-text-dynamic-source-selector-dispatch-c17b56-c1866d.md` and
  `notes/text-window-rendering-primitives-c1078d-c10d7c.md`.
- 2026-05-06 follow-up: the `C1:0F40..134B` clear-window/value-entry corridor
  now names its C4 tile-release and glyph-scratch reset joins, instant-print
  toggles, active-window cursor setup, decimal formatter, glyph print,
  text/input tick, sound effect, `MULT32`, and divide helper calls. See
  `notes/text-entry-record-builder-neighbors-c10f40-c11887.md` and
  `notes/text-window-rendering-primitives-c1078d-c10d7c.md`.
- 2026-05-06 follow-up: the adjacent `C1:15F4..17E2` direct text-entry
  constructor and active-chain renderer now name their installer, print,
  tile-attribute, window-title upload, text-length, record-marker, glyph-state,
  and glyph-print helper joins. See
  `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`.
- 2026-05-06 follow-up: the `C1:134B..1F8A` setup and active-selection strip
  now names the setup-wrapper, active-entry layout, active-chain render, and
  `C1:196A` selection-loop helper calls. This removes raw helper edges from
  the `134B`, `181B`, and `1887` text-entry modules while preserving byte
  equivalence. See
  `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`.
- 2026-05-06 follow-up: the first half of the adjacent selection-prompt strip
  now names the helper-call surface for `C1:2012`, `2070`, `20D6`, `21B8`,
  and `2362`. The pass covers candidate eligibility scans, candidate text
  refresh, two-list prompt control, simple side prompt control, row highlight
  helpers, enemy flashing toggles, ticks, sound, and close-focus cleanup. See
  `notes/c1-selection-prompt-runtime-polish.md`.
- 2026-05-06 follow-up: the contiguous `C1:242E..2BF3` selection-prompt
  dispatch/core now names its evidence-backed helper-call surface. The pass
  covers dispatch to the two prompt controllers, interaction-context lookup,
  text-event slot snapshot/restore, window binding, character-name staging,
  typed text-entry creation, active-chain refresh, selection-loop control,
  prompt callback install/clear, HP/PP row focus helpers, delayed-action
  payload dispatch, ticks, sound, text printing, VRAM transfer, and the
  terminal text-entry chain counter. The mixed internal local jumps/calls stay
  raw until the corridor is structurally split. See
  `notes/character-selection-prompt-dispatch-c1242e-c12bf3.md`.
- 2026-05-06 follow-up: the adjacent `C1:2BF3..3187` debug/window tick island
  now names its evidence-backed helper-call surface. The pass covers fixed
  debug text printing, active tile attributes, heavy/light window ticks, HP/PP
  redraw helpers, debug menu entry construction, selection-loop control,
  teleport setup, presentation scene launch helpers, debug playback view
  entry/exit, and menu/window cleanup. A later follow-up names the initially
  deferred `C1:3D03`, `C1:3EE7`, and `C1:3E0E` dispatcher calls. See
  `notes/debug-menu-window-tick-helpers-c12bf3-c12d17.md`.
- 2026-05-06 follow-up: the open-menu/debug tail in `C1:33B0..4103` now names
  the reference-backed `OPEN_HPPP_DISPLAY`, `SHOW_TOWN_MAP`,
  `DEBUG_Y_BUTTON_FLAG`, `DEBUG_Y_BUTTON_GUIDE`, `DEBUG_SET_CHAR_LEVEL`, and
  `DEBUG_Y_BUTTON_GOODS` starts. The formerly raw debug dispatcher edges from
  `C1:2E63..3187` now call the flag, guide-count, and goods-grant viewers by
  name, and the C0 overworld button loop now calls the C1 menu/display entries
  through named contracts. See
  `notes/open-menu-prelude-helpers-c1339e-c133b0.md` and
  `notes/debug-menu-reachability-c0-c1-ef.md`.
- 2026-05-06 follow-up: the same `C1:33B0..4103` open-menu source now names
  the evidence-backed helper-call surface inside the record rebuild and menu
  loop. The pass covers text-entry creation/refresh/layout, open-menu
  selection control, target prompts, inventory/equipment row renderers,
  HP/PP focus helpers, party PSI/equipment/teleport branch calls, item-transfer
  joins, window cleanup, debug tail ticks, statistic-selector printing, and
  battle-sprite refresh helpers. A follow-up names the final deferred
  `C1:AF74`, `C1:03DC`, and `C1:0FEA` edges, leaving the source unit with no
  raw helper-call edges. See
  `notes/open-menu-prelude-helpers-c1339e-c133b0.md`.
- 2026-05-06 follow-up: the `C1:33B0..4103` open-menu loop now names the
  local scratch ABI used by its menu/text caller contracts. The pass covers
  top-level Talk/Check fallback text pointers, open-menu text-entry source
  pointers, selected-character value staging, Goods/Talk primary and secondary
  interaction-context installs, active context offsets `+17/+1B/+21`, status
  item text output, and debug decimal/fixed-string display sources. This keeps
  the open-menu caller side aligned with the `0x1A` menu family and
  text-entry helper contracts without changing helper boundaries.
- 2026-05-06 follow-up: small C1 text/window helper cleanup named the local
  helper edges in the interaction-output selectors, the active-window
  descriptor initializer, and the `$89D4` text-entry constructor chain. This
  covers `C1:04B5`, `C1:13D1..1596`, `C1:3187`, and `C1:323B` without
  changing bytes. See `notes/interaction-result-consumers.md` and
  `notes/text-entry-record-builder-neighbors-c10f40-c11887.md`.
- 2026-05-06 follow-up: the low text-command strip at `C1:4103..4558` now
  names the helper-call surface for direct 24-bit jump target assembly,
  `JUMP_MULTI` context reads, event-flag high-byte assembly, flag
  set/clear/check operations, call-text pointer dispatch, number selection,
  context pointer installs, focus/window wrappers, and C4 glyph/cursor staging.
  See `notes/lower-bank01-text-control-strip-00-17.md`,
  `notes/text-command-04-set-event-flag.md`,
  `notes/text-command-05-clear-event-flag.md`,
  `notes/text-command-06-jump-if-flag-set.md`,
  `notes/text-command-07-check-event-flag.md`,
  `notes/text-command-08-call-text.md`,
  `notes/text-command-09-jump-multi.md`, and
  `notes/text-command-0a-24bit-jump.md`.
- 2026-05-06 follow-up: the adjacent `C1:4558..4EAB` low text-command and
  inventory helper strip now names the helper-call surface for `0C/0E`
  workmem/argmem staging, `1A 00/01` character-selection queue builders,
  `1C 05/06/07` print/layout helpers, `1D 00..05/08/09` item, wallet, and
  possession wrappers, early `1E 00..07` HP/PP wrappers, and `1F 20/21`
  teleport joins. The shared current-text-context workmem setter label was
  corrected to `C1:0443`. See
  `notes/lower-bank01-text-control-strip-00-17.md`,
  `notes/text-command-family-1d-inventory-money.md`,
  `notes/text-command-family-1e-stat-recovery.md`,
  `notes/item-category-classifier-c19ee6.md`,
  `notes/party-inventory-room-search-c456e4-c4572b.md`,
  `notes/party-item-possession-search-c45637-c45683.md`, and
  `notes/teleport-menu-wrapper-c1bb71-bcab.md`.
- 2026-05-06 follow-up: the next `C1:4EAB..575D` text-command helper corridor
  now has no raw helper-call edges. The pass names the parameterized pause
  worker, shop/inventory menu front ends, buy/sell price wrappers, item
  compatibility checks, character-name and number/money printers,
  status/ailment get/set helpers, special-selector loaders, queued-value
  comparison helpers, required-experience staging, party-count checks,
  Escargo storage cleanup, inventory row rendering, empty-slot search, item
  insertion, item-slot lookup, and item-slot removal. See
  `notes/text-command-10-parameterized-pause.md`,
  `notes/text-command-family-1c-print-display.md`,
  `notes/text-command-family-1d-inventory-money.md`,
  `notes/text-command-family-19-data-and-substitution.md`, and
  `notes/jeff-repair-item-name-bridge.md`.
- 2026-05-06 follow-up: the same `C1:4EAB..575D` corridor now names the
  remaining caller-frame scratch ABI at the menu/result/display handoffs.
  Shop selection, buy/sell price, item compatibility, ailment checks,
  special selector loaders, window-relative selections, give-item-B,
  remove-by-slot, and numeric/money display now install through named
  text-context or decimal source pointer aliases instead of raw `$0E/$10`.
  The `0x1A 05` inventory-menu leaf also distinguishes its preserved window
  argument from the preserved character argument while leaving descriptor
  field offsets untouched.
- 2026-05-06 follow-up: the adjacent `C1:575D..621F` inventory, money, and
  delivery-helper corridor now has no raw helper-call edges. The pass names
  equipped-item reference checks, inventory-slot item reads, compatibility and
  equipment-subtype dispatch, pending-item queue store/withdraw helpers,
  Escargo storage staging, three-byte money amount assembly, wallet/ATM
  add/take/check helpers, status-window and vertical-string display joins,
  loaded-string count staging, party utility/party-count checks, delivery queue
  removal and info reads, storage enqueue, food/equipment classification, PSI
  name printing, and random-number generation. See
  `notes/text-command-family-1d-inventory-money.md`,
  `notes/text-command-family-19-data-and-substitution.md`,
  `notes/text-command-family-1c-print-display.md`,
  `notes/pending-item-queue-984b.md`, and
  `notes/equipped-item-presence-predicate-c3e9a0.md`.
- 2026-05-06 follow-up: the same `C1:575D..621F` continuation now carries
  source-facing names for its caller-frame result ABI. Equipped-item and
  inventory-usability booleans, deferred item compatibility, Escargo
  store/withdraw handoffs, character inventory-slot reads, wallet/ATM
  predicates and mutations, Escargo storage byte reads, loaded-string counts,
  delivery queue item/owner outputs, equipment-slot classifiers,
  party-count predicates, and random-number output now stage through named
  text-context or money-amount pointer aliases rather than raw `$0E/$10`.
  The Escargo store and status-window display leaves also distinguish their
  preserved caller argument slots.
- 2026-05-06 follow-up: the `C1:621F..7440` mixed callback and event-helper
  tail now names its helper-call surface through the `C1:7274..7440` sibling
  module. The pass covers the `1F C0`/`JUMP_MULTI2` target finalizer, Jeff
  repair result mapping, battle-text mode latch access, `1E 08` level refresh,
  `0x19 22..26` direction/condiment/landing helpers, C0 hotspot and movement
  queue joins, C2 scripted-battle and respawn-warp helpers, C3 battle visual
  effect dispatch, C4 entity frame/flag/script helpers, attached-child helpers,
  wandering photographer dispatch, and the bank-deposit accumulator stager. See
  `notes/text-command-1f-c0-jump-multi2-c1621f.md`,
  `notes/text-command-family-1f-deferred-callbacks.md`,
  `notes/text-command-family-19-data-and-substitution.md`,
  `notes/text-command-family-1e-stat-recovery.md`,
  `notes/bank-deposit-accumulator-98b9-98bb.md`, and
  `notes/respawn-warp-target-snapshot-helper-c230f3.md`.
- 2026-05-06 follow-up: the front half of `C1:621F..7274` now also names its
  local callback-frame and result handoff scratch. The `1F C0`/`JUMP_MULTI2`
  path distinguishes the packed text pointer printed before table adjustment,
  the destination table pointer, the destination-count argument, and the
  scratch copy used while patching the table. The `1F D0` Jeff-repair leaf and
  `0x19 22..24` direction helpers now install their primary or secondary text
  results through named text-context source aliases rather than raw `$0E/$10`.
- 2026-05-06 follow-up: the adjacent `C1:7440..7708` timed-delivery and
  `0x1E 09..0E` experience/stat tail now has no raw helper-call edges. The
  source names the `EF:0EAD` delivery row sprite/placeholder adapter,
  `C0:9246` 32-bit shift/assembly helper, `C1:D9E9` experience award handoff,
  and C2 derived-stat recalculation helpers for IQ, Guts, Speed, Vitality, and
  Luck. See `notes/timed-delivery-row-index-command-1f-d3.md`,
  `notes/timed-event-slot-block-7440-and-c20abc.md`, and
  `notes/text-command-family-1e-stat-recovery.md`.
- 2026-05-06 follow-up: the `C1:78F7..7AE3` loaded-string/window-family
  dispatcher bridge now has no raw helper-call or raw callback-return address
  edges in its `0x18` front half. The source names close/drain/clear window
  helpers, HP/PP hide and text tick helpers, the managed-slot snapshot helper,
  wallet/status refresh, and the callback return targets for open/switch
  window, force alignment, window-relative selection, register comparison, and
  status-window display. See `notes/text-command-family-18-windows-and-selection.md`,
  `notes/text-command-family-19-data-and-substitution.md`, and
  `notes/text-command-load-string-pointer-c17796-c17889.md`.
- 2026-05-06 follow-up: the same `C1:78F7..7AE3` bridge now names the live
  `0x18` and `0x19` selector ladders directly. The pass covers the window
  family selectors `00/01/02/03/04/05/06/07/08/09/0A/0D`, the data-return
  selectors `02/04/05/10/11/14/16/18/19/1A/1B/1C/1D/1E/1F/20..28`, and the
  callback-frame pointer used when the managed-slot snapshot branch marks the
  frame active.
- 2026-05-06 follow-up: the core `C1:86B1..8B2C` nested-text executor and
  callback invoker now names its principal helper-call and callback-root
  surface. The source names the managed-slot initialize/apply helpers,
  active-window parser preflight, line/scroll and line-clear helpers,
  selection and halt-control helpers, compressed-bank text pointer tables for
  pseudo-opcodes `0x15..17`, and the top-level `00..1F` callback roots for the
  low control strip and structured families. See
  `notes/nested-text-pointer-and-callback-invoker-c186b1-c18b2c.md`,
  `notes/bank01-text-command-map-00-1f.md`, and
  `notes/timed-event-callback-invoker-c187cc.md`.
- 2026-05-06 follow-up: the adjacent `C1:8B2C..90E6` inventory/recovery helper
  cluster now names its cross-bank side-effect and mutation workers. The source
  names C2 party-overlay/Teddy Bear hooks, C3 Fresh Egg/Chick/Chicken
  lifecycle hooks, the C3 HP/PP recover/deplete workers, and the C4 equipped
  slot index installers used by insertion/removal and equipment subtype
  dispatch. See `notes/c1-inventory-recovery-runtime-polish.md`,
  `notes/inventory-slot-insertion-helper-c18bc6.md`,
  `notes/inventory-slot-removal-helper-c18c27.md`,
  `notes/equipment-slot-subtype-dispatch-c19066-c4577d.md`, and
  `notes/hp-pp-adjust-helper-quartet-c18f0e-c19010.md`.
- 2026-05-06 follow-up: the adjacent `C1:913D..91B0` pending-item queue bridge
  now names its `C3:E977` inventory-slot accessor edge as
  `C3E977_ReadCharacterInventorySlotByte`. The targeted pending-item queue
  modules now have no raw helper-call edges, and `C1:9183` reads directly as a
  selected-inventory-slot-to-`$984B` queue transfer before the `C1:8C27`
  removal worker. See `notes/pending-item-queue-984b.md` and
  `notes/item-slot-helper-pair-c3e977-c3ee14.md`.
- 2026-05-06 follow-up: the nearby Escargo queue/storage helpers now name their
  local scan and compaction scratch. `C1:90F1` exposes the active requester
  bytes at `$98AB`, packed storage bytes at `$984B`, remaining capacity, and
  scan index; `C1:913D/9183` expose the pending-item scan index, capacity,
  source character, and selected slot; and `C1:91B0` exposes the removed byte,
  shift byte, next index, and compaction window.
- 2026-05-06 follow-up: the `C1:9437..9A11` display/status helper bridge and
  `C1:A795..AA5D` per-character equipment loop now name their remaining
  helper-call edges. This closes the raw helper-call surface in those source
  units, including the C4 required-experience printer, C1 equipped-slot
  dispatcher/display refresh, C2 managed text-event snapshot pair, C3
  window-update helpers, and C4 right-aligned decimal/status printer. See
  `notes/c1-display-helper-runtime-polish.md`,
  `notes/c1-equipment-runtime-polish.md`, and
  `notes/equipment-menu-top-level-flow-c1a778-c1aa5d.md`.
- 2026-05-06 follow-up: the battle targetting and battle PSI helper cluster now
  names its remaining helper-call surface across `C1:ADB4`, `C1:C452`,
  `C1:C853`, `C1:CA06`, `C1:CA72`, `C1:CAF5`, and `C1:CB7F`. The pass covers
  C2 second-stage row counting, C4 random/print/cursor helpers, C3 window
  update/tick helpers, EF battle-sprite row effect clearing, C1 category/menu
  helpers, and the `CA72 -> C853` metadata refresh join. See
  `notes/c1-battle-front-end-runtime-polish.md`,
  `notes/c1-battle-psi-runtime-polish.md`, and
  `notes/battle-psi-selection-refresh-c1ca72.md`.
- 2026-05-06 follow-up: the `C1:D109..DC1C` level-up/stat refresh source unit
  now names its remaining helper-call surface. The pass covers signed
  fixed-point division, IQ/Luck derived-stat recalculation, bounded random
  max HP/PP bumps, battle-text mode/focus/name-buffer helpers, and the
  Sound Stone display tick tail. See `notes/level-up-stat-growth-helper-c1d08b.md`
  and `notes/level-up-stat-gain-text-family-c1d15b-d76d.md`.
- 2026-05-06 follow-up: the `C1:E4BE..EAD6` text-input option strip and dialog
  body source unit now names its remaining helper-call surface. The pass covers
  C3 window update-scope exit/light-tick helpers, active-window tile attributes
  and glyph printing, text-system ticking, movement candidate search helpers,
  menu-cell selection search, sound effects, the local `C1:E48D` row renderer,
  and text-length measurement before committing the input buffer. See
  `notes/text-input-dialog-option-helpers-c1e48d-c1e4be.md`.
- 2026-05-06 follow-up: three small C1 tail edges now use existing stable
  contracts: `C1:DDDA` calls `C1:153B` as `AddSelectionMenuItem`,
  `C1:ECD1` calls `C1:EC8F` as `PreviewWindowFlavourAndRedraw`, and the
  new-file party setup branch calls `C1:D9E9` as `AwardExperienceToCharacter`.
  The remaining raw local numeric edges are fenced to the mixed-decode island
  in `src/c1/c1_242e_dispatch_character_selection_prompt_mode.asm`.
- 2026-05-06 follow-up: the display-text dynamic source selector now names
  its callback-return low words for the stable `1A`, `1C`, `1D`, `1E`, and
  `1F` text-command leaves. This keeps the dispatcher contract table readable
  without changing the byte stream: menu leaves, print/display leaves,
  inventory/money leaves, stat-recovery leaves, and deferred callback/event
  leaves all return through source-facing aliases instead of raw low-word
  literals. Validation was attempted in this worktree, but the local ROM was
  absent from both default lookup paths, so byte-equivalence remains pending
  until `EarthBound (USA).sfc` is supplied.
- 2026-05-06 follow-up: the `C1:621F..7708` deferred-callback tail now names
  the shared `$97BA..$97BE/$97CA` queued-argument ABI and the self-return
  low-word contracts inside the callback leaves themselves. This covers the
  `1F C0` dword jump finalizer, adjacent `1F` event/entity callbacks,
  `1D 24` bank-deposit staging, `1C 13` battle visual-effect staging, and the
  `1E 09..0E` experience/stat-boost leaves. The durable C1 scaffold was
  regenerated from source; byte-equivalence is still pending on the missing ROM
  gate noted above.
- 2026-05-06 follow-up: the lower queued text-command leaves now use the same
  source-facing deferred-byte vocabulary. `C1:48AC..4CEE` names the
  `$97BA/$97CA` queue and callback low words for wallet add/take, early HP/PP
  recover/deplete, and item give/take wrappers; `C1:4EAB..575D` extends the
  same queue names through direct item-use compatibility, ailment checks,
  window-register comparison, print-number/money, inventory display, give-item
  B, and remove-slot leaves. The C1 scaffold was regenerated from source with
  the local ROM still absent from the exact byte-equivalence gate.
- 2026-05-06 follow-up: the `C1:575D..621F` continuation now follows the same
  queued-byte style. The source names `$97BA..$97BC/$97CA`, callback low words,
  wallet/ATM balance words, and active-party count for equipped-item,
  inventory-usability, Escargo transfer, wallet/ATM amount, status-window,
  party utility, delivery/pickup queue, party-count, and random-number leaves.
  The scaffold was regenerated from source; exact byte-equivalence remains
  pending on the same missing-ROM gate.
- 2026-05-06 follow-up: the lower control strip at `C1:4103..4558` now uses
  the same deferred-byte ABI vocabulary inside the callback leaves themselves.
  The source names `$97BA..$97BC/$97CA`, self-return callback low words,
  24-bit target assembly scratch, flag low-byte staging, call-text pointer
  staging, the number-select cancel sentinel, and the `0x18 05` forced
  alignment single-byte queue. The scaffold was regenerated from source; exact
  byte-equivalence remains pending on the same missing-ROM gate.
- 2026-05-06 follow-up: the `[1F 41]` name-entry caller contract now reaches
  through the C1 UI sources. The special-event dispatcher calls `C1:EAA6` by
  name for cases `03/04`, names its zero/one scene arguments and local event
  spans, while `C1:EAA6..EC8F` names the name-entry state flags, the
  `EAA6 -> EB4C` preview-entry handoff, `$9801/$97F5/$9C9F` naming buffers,
  text-input window ids, and commit-flow cleanup flags. The scaffold was
  regenerated from source; exact byte-equivalence remains pending on the same
  missing-ROM gate.
- 2026-05-06 follow-up: the final non-fenced raw local C1 branch/caller aliases
  now use stable contract names. `C1:D109..DC1C` names the shared `D8C7`
  battle-text-mode cleanup tail, `[1F 41]` case `11` calls
  `C1BE4D_AttemptHomesicknessResult` by name, and the naming-buffer commit flow
  calls `C1E57F_RunTextInputDialog` directly. The only remaining raw numeric
  local jumps/calls in checked-in C1 source are the intentionally deferred
  mixed-decode edges in `src/c1/c1_242e_dispatch_character_selection_prompt_mode.asm`.
  The scaffold was regenerated from source; exact byte-equivalence remains
  pending on the same missing-ROM gate.
- 2026-05-06 follow-up: the file-select setup menu wrappers now expose their
  local UI contracts in source. `C1:F497` and `C1:F616` name the text-speed,
  sound, and window-flavour window ids, active-focus and descriptor/table
  lookup fields, `$89D4` text-entry selected-row offsets, setup-state bytes
  `$98B6/$98B7/$99CD`, the setup-stage cancel value, the `C1:EC8F`
  window-flavour preview callback pointer, and the final selected-file text
  speed handoff. The scaffold was regenerated from source; exact
  byte-equivalence remains pending on the same missing-ROM gate.
- 2026-05-06 follow-up: the visible file-select action/copy/delete/setup menu
  builders now name their C4 file-select text pointer contracts in source.
  `C1:F07E`, `C1:F14F`, `C1:F2A8`, `C1:F3C2`, `C1:F568`, and `C1:F6E3` expose
  their prompt/option pointer lows, C4 bank word, window/result ids, row/column
  positions, generated copy-destination label buffer, and setup option entry
  ids. The deeper new-file naming/body text pointer loads inside `C1:F616`
  were left for the follow-up below. The scaffold was regenerated from source;
  exact byte-equivalence remains pending on the same missing-ROM gate.
- 2026-05-06 follow-up: the deferred new-file naming/confirmation tail inside
  `C1:F616` now has caller-side source names. The pass names the `C4:C194`
  prompt table and 0x28-byte prompt stride, party-character record
  stride/base, fixed-width `$9819/$981F/$9829` pet/food/thing commit buffers,
  confirmation windows `0x21..0x24`, centered food/thing display layout, the
  `C4:C2AC..C2D9` confirmation labels/options, and the final yes/no menu
  result contract. C4 data source remains untouched; the C1 scaffold was
  regenerated from source, with exact byte-equivalence still blocked by the
  missing local ROM/asar gates.
- 2026-05-06 follow-up: the new-file initialization and shared start-file tail
  in `C1:F616` now names the C1-facing D5/C0/C3/C5/C7 joins. The promoted
  names cover the `D5:F5F5` initial-stats table pointer and row offsets,
  battle-state and experience-award inputs, HP/PP rolling display fields,
  inventory seed/clear lengths, starting money and start position loads, the
  fixed favorite-thing `"PSI "` prefix seed, `$98B8/$9D1F/$9D21` landing
  snapshot, the C5 start script, initial event flag write, C3 text-speed timing
  table pointer, `$9625/$9627/$9629/$964B` timing state, and final C7
  start-file text pointer. The scaffold was regenerated from source; exact
  byte-equivalence remains pending on the same missing-ROM/asar gates.
- 2026-05-06 follow-up: the front `0x1A` menu dispatcher in
  `C1:7B56..7C34` now names its subselector ids, cancellable/uncancellable
  selection-loop modes, no-follow-up return value, and `$06/$08` menu result
  staging pair before primary text-context installation. This tightens the
  menu/text-entry contract without expanding the pass into the later `0x1B`,
  `0x1C`, `0x1D`, or `0x1F` dispatcher bodies.
- 2026-05-06 follow-up: the adjacent `0x1B` memory/context dispatcher in
  `C1:7C36..7D8D` now names its subselector ids, null primary-context branch
  tests, four-byte jump-target skip, saved parser argument pointer, primary and
  secondary text-context staging pairs, swap temporaries, and `$97CC..$97D4`
  scratch context snapshot. This keeps the source aligned with the existing
  `text-command-family-1b-memory-context` contract while leaving the later
  `0x1C`, `0x1D`, and `0x1F` bodies for separate fenced passes.
- 2026-05-06 follow-up: the front `0x1C` print/display dispatcher in
  `C1:7D94..7F0F` now names its stable subselector ids for `01..0F` and
  `11..15`, plus the battle user/target selector values, `$06/$08/$09`
  name-buffer pointer staging, `$0E/$10` text-context handoff, fixed-string
  preflight length, and no-follow-up return value. This continues the adjacent
  text-command-family sweep while leaving the later `0x1D` inventory/money
  ladder for its own pass.
- 2026-05-06 follow-up: the adjacent `0x1D` inventory/money dispatcher in
  `C1:7F11..811D` now names the live selector ids for `01..15`, `17..19`, and
  `20..24`, preserving the `16` and `1C` gaps as non-live cases. The inline
  `1D 20` and `1D 22` predicate bodies now expose their battle-name-buffer
  comparison, current map-position lookup, map-class mask, exit-mouse class,
  boolean scratch/result staging, `$0E/$10` text-context handoff, and
  no-follow-up return contract.
- 2026-05-06 follow-up: the adjacent `0x1E` recovery/stat dispatcher in
  `C1:811F..81BA` now names its live selector ids for `01..0E`, preserves
  `00` as the zero-branch HP-percent recovery case, and returns the shared
  no-follow-up value for anything outside the live range. This keeps the
  parser-side high `0x1E` artifacts outside the runtime dispatcher contract.
- 2026-05-06 follow-up: the adjacent `0x1F` deferred-callback/event dispatcher
  in `C1:81BB..866D` now names its wide selector ladder from the low
  music/sound strip through `11..23`, `30/31`, `40/41`, `50..69`, `71`,
  `81/83`, `90`, `A0..A2`, `B0`, `C0`, `D0..D3`, `E1`, `E4..F4`, and the
  shared no-follow-up return. The pass leaves the downstream callback and
  immediate helper bodies on their existing contracts.
- 2026-05-06 follow-up: the immediate `0x1F` helper leaves in
  `C1:8518..85ED` now name their C1-side staging. The pass covers
  teleport-position snapshot/refresh workmem, the refresh flag loop, landing
  visual state and sentinel values, phone-contact and Magic Truffle result
  installation through `$06/$08 -> $0E/$10`, and current-interaction flag
  set/clear/get staging values.
- 2026-05-06 follow-up: the late `0x1E` stat-tail callbacks in
  `C1:744B..7706` now name their local staging. The source exposes the
  experience amount dword assembly scratch and `$0E/$10` award handoff for
  `0x1E 09`, plus the one-byte boost payload, byte-add scratch, and queue/apply
  exits for the IQ, Guts, Speed, Vitality, and Luck leaves.
- 2026-05-06 follow-up: the fenced `C1:242E..2BF3` character-selection prompt
  core no longer presents mixed payload bytes as raw local `JMP`/`JSR` edges.
  The byte stream is unchanged, but the unaligned generated decode fragments
  in `src/c1/c1_242e_dispatch_character_selection_prompt_mode.asm` now use
  explicit `db` bytes, keeping raw helper-call scans focused on real C1
  contracts. The structural split and deeper semantic naming remain deferred.
- 2026-05-06 follow-up: the front inventory/possession text-command wrappers
  now finish the local queued-selector vocabulary. `C1:4CEE..4EAB` names
  `$97BA/$97CA`, the one-byte argument limit, and self-return callback low
  words for `0x1D 04`, `0x1D 05`, and adjacent `0x1F 20`, matching the
  already-polished lower queued callback ABI.
- 2026-05-06 follow-up: the lower `0x1F` callback corridor in
  `C1:6DE8..7231` now names its packed-payload staging. `1F 63` exposes the
  movement-record dword before `C0:64E3`, `1F 66` exposes the hotspot selector,
  target selector, and five-byte payload before `C0:72CF`, and `1F F1/F2`
  expose their visual-type or pose-descriptor script selector pairs.
- 2026-05-06 follow-up: the adjacent Escargo/condiment source polish in
  `C1:6F9F..711A` names the `0x19 25` food-condiment result staging and the
  `0x1D 0C` Escargo storage-status classifier. The latter now exposes its
  queued selector, storage-full bit, selected inventory item lookup, item
  storage flag mask, and final two-bit status result path.
- 2026-05-06 follow-up: the adjacent `C1:6FD1..7058` strip now names
  `1F 23` scripted-battle init staging and the `19 26` transition-landing
  snapshot adapter. The source exposes the queued high-byte selector, zero
  fallback to direct text argument, signed result staging, and the explicit
  `C1:7037 -> C2:30F3` handoff label.
- 2026-05-06 follow-up: the dynamic source selector dispatcher now names its
  family-frame offsets for `0x1A`, `0x1B`, `0x1C`, `0x1D`, and `0x1F`, and the
  front `1A/1B` result/context reinstall sites use the shared `$0E/$10`
  text-context source pointer aliases. This closes the last raw frame-offset
  and installer-handoff literals in `C1:7B56..866D` without moving any
  dispatcher boundaries.
- 2026-05-06 follow-up: the `C1:621F..7274` deferred-callback corridor now
  names the entity-helper callback leaves behind `1F 13..1F` and `1F E1/E4..EF`
  at both the callback bodies and the `C1:81BB` dispatcher return table. The
  pass promotes frame-selector updates, dynamic visual entity setup, attached
  child spawn/clear leaves, no-op seven-byte absorbers, landing-profile display,
  C4 entity flag set/clear leaves, registry `8000` mark/clear leaves, and
  visual/pose mode-slot selectors.
- 2026-05-06 follow-up: the remaining generic `0x1F` callback returns now use
  source-facing behavior names. `C1:621F..7274`, `C1:7274..7440`, and the
  `C1:81BB` dispatcher table name the text sound-mode setter, presentation SFX
  queue, scripted-battle init, blinking-triangle state setter, movement-record
  enqueuer, hotspot activate/disable leaves, record-backed visual/pose script
  runners, and pose-descriptor attached-child spawn/clear leaves.
- 2026-05-06 follow-up: the top-level text invoker at `C1:87CC..8B2C` now
  names the central callback ABI and low-strip parser leaves. `$1E`, `$14`,
  `$12`, `$02`, and `$00C0` are exposed as the active same-bank callback low
  word, fetched opcode/argument byte, managed text-event slot pointer, RTS
  low-word scratch, and preserved `A` argument scratch. The same pass names the
  `0x15..17` compressed-bank pseudo-opcode resolver paths and the `0x11`
  selection-menu context installer, and the dispatcher's `0x00..1F` compare
  literals now use `TextOpcode*` aliases. This ties the ordinary parser root
  back to the deferred callback family without touching C2/C4/EF.
- 2026-05-06 follow-up: the UI caller-side callback ABI now has source-facing
  names at its major call sites. `C1:33B0`, `C1:AA5D`, `C1:ADB4`,
  `C1:B5B6`, `C1:BB71`, `C1:CB7F`, `C1:242E`, `C1:9D49`, `C1:A795`,
  `C1:ECD1`, and `C1:F616` now stage `$0E/$10` and `$12/$14` through
  menu-row, prompt-display, prompt-eligibility, or preview-callback aliases
  before calling `C1:1F5A`, `C1:196A`, or `C1:27EF`. This keeps the shared
  menu/selection helper contracts readable without splitting the mixed
  character-prompt core or changing any cross-bank names.
- 2026-05-06 follow-up: the adjacent menu/display builders at
  `C1:9441..9B4E` now expose their local source-pointer and scratch-slot ABI.
  Phone contacts, character status, inventory/equipment rows, the temporary
  focus selector, and the Escargo storage menu now distinguish title, tile,
  text-print, decimal, fixed-string, text-entry metadata, queue index, item id,
  and selection-result handoffs while preserving all existing C1 helper
  boundaries.
- 2026-05-07 follow-up: the shop/equipment menu join at `C1:9D49..9EE6` now
  names its local menu-row and item-row ABI. The status refresh exposes its
  comparison-marker reset index and E0 tile-block source pointer, while the
  shop menu builder distinguishes D5 shop-table selection, visible row index,
  item id, item-row pointer, staged item-name text entry, price-print source,
  comparison callback, and returned selection result.
- 2026-05-07 follow-up: the per-character equipment slot loop at
  `C1:A795..AA18` now uses the same source-facing row vocabulary. The pass
  names the selected family, inventory scan index, visible-row count, default
  row, item id, one-based character id, staged item-name text entry,
  item-selection result, C2 preview callback lane, and wallet decimal-print
  source without altering the C2/C3/C4 helper boundaries.
- 2026-05-07 follow-up: the file-select slot-choice source at
  `C1:ECD1..F07E` now names the save-slot menu caller ABI. The pass covers the
  corrupt-save notice loop, battle-text substitution source, slot-choice mode,
  save-slot row and preview indices, packed row metadata, text-entry
  source/metadata, C4 copy source/destination pairs, level decimal print
  source, preserved print buffer, and active text-entry pointer for selected
  slot redraws.
- 2026-05-07 follow-up: the file-select setup wrappers at `C1:F616..F7F3`
  now name the sound-setting refresh/result ABI and window-flavour
  prompt/option text-entry ABI. The source distinguishes refresh mode, active
  text-entry pointer, redraw source, option text sources, metadata, persisted
  setting pointer, preview callback, and final selection result while leaving
  EF save persistence and C4 text assets untouched.
- 2026-05-07 follow-up: the adjacent new-file naming loop at
  `C1:F902..FAAE` now names the field-index and advance-step ABI used between
  the file-select setup menus and the naming-buffer commit helper. The source
  exposes working/current field slots, retry/advance delta slots, the
  party-name destination index, and C4 prompt-table pointer/stride staging.
