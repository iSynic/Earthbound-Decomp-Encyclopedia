# EF Runtime Semantic Polish Plan

Primary queue context: `notes/source-readiness-triage.md` and
`notes/project-status.md`.

## Current State

`EF` is byte-complete but still coarse. The handoff in
`notes/bank-ef-source-scaffold-handoff.md` describes the bank as exact source
corridors for mixed save/map/text/debug content, mostly explicit `db` source
blocks rather than decoded 65816 routines. The next work is to split and name
runtime-facing helpers and payloads only where consumers prove semantics.

## Subsystem Slices

- Save/SRAM helpers: SRAM signature, save block flags, checksum/save helpers,
  file-select save/load callers.
- Debug/menu runtime: debug sound menu, graphics state init, overlays, cursor
  tilemap data, color math reset.
- Map/text/glyph data corridors: map tileset/sprite grouping tables, text
  payload runs, glyph mask tables, menu option strings.
- Sound Stone and presentation tables: Sound Stone table data and late visual
  presentation payloads shared with C0/C4 landing or presentation notes.
- C1/C2 battle-text payload joins: EF substitution payloads and battle text
  data consumed by C1 display wrappers and C2 action result lanes.

## First Pass Order

1. Start with save/SRAM helpers because C1 file-select already supplies stable
   caller evidence.
2. Split debug/menu runtime after save helpers, keeping executable helpers
   separate from font/cursor/table payloads.
3. Map C1/C2 battle-text substitution payload joins before broad text-run
   decoding, so runtime consumers drive the first names.
4. Defer wide map/text/glyph corridor splitting until D5/C1 consumers or text
   script tooling need concrete source assets.
5. Promote Sound Stone and presentation tables with C0/C4 evidence, not as
   isolated EF data labels.

## Evidence Inputs

- `notes/bank-ef-source-scaffold-handoff.md`
- `notes/bank-ef-first-pass.md`
- `notes/bank-ef-asset-data-map.md`
- `notes/ef-readable-source-split-queue.md`
- `notes/sram-template-contracts.md`
- `notes/debug-menu-reachability-c0-c1-ef.md`
- `notes/c2-ef-battle-text-contract-workahead.md`

## Expected Outputs

- A split queue that distinguishes executable EF helpers from opaque data/text
  corridors before any source promotion.
- Save/SRAM and debug/menu contract notes with C1 caller names and byte ranges.
- Battle-text substitution payload notes tied to C1 display wrappers and C2
  action-table message lanes.
- Deferred text/data corridor tasks for D5/C1/text-script follow-up work.

## Validation

Future implementation passes should use:

```powershell
python tools\promote_asset_bank_to_source_scaffold.py EF
python tools\build_source_bank_scaffold.py --bank EF
python tools\validate_source_bank_byte_equivalence.py --bank EF --module all --combined --scaffold src\ef\bank_ef_helpers_asar.asm --strict
python tools\build_source_bank_candidate_ranges_doc.py --bank EF
python tools\build_source_bank_residual_map.py --bank EF
```

This planning pass does not split EF source corridors or regenerate the bank.

## Implementation Notes

- 2026-05-01: EF save/SRAM helper polish landed as byte-neutral source
  aliases/constants plus `notes/ef-save-sram-runtime-polish.md`. The promoted
  contracts name the 0x500-byte save-block layout, primary/backup save-slot
  pair sizing, checksum/complement fields, live game-state/party/event-flag
  copy spans, `$9F79` missing-save mask, `EF:05A6` missing-save slot bit masks,
  `$30:7FFE` SRAM integrity marker, and the C0 multiply helper used to scale
  slot and block indices into SRAM offsets.
- 2026-05-01: EF debug sound-menu controller polish landed as byte-neutral
  source aliases. The promoted contracts name the controller row/window
  scratch, `$0069/$006D` input masks, `$B54B/$B54D/$B54F` BGM/SE/effect
  selectors, `$B545` temporary BGM restore slot, row cursor writeback through
  `$0BCA`, and wrap ranges for the BGM, SE, and effect selector rows.
- 2026-05-01: EF debug graphics/state initializer polish landed as byte-neutral
  source aliases. The promoted contracts name the `$B559` debug menu mode,
  `EF:EB5F` debug-font load, `EF:EF9F` mode-3 extra block, `EF:F1BB` late tile
  source copy, `$B553/$B555/$B557/$B55F` cursor/command/overlay state fields,
  layer clear/fill bands, `$0204` palette marker, and `$4A58/$4A5A`
  presentation flags cleared by debug menu initialization.
- 2026-05-01: EF debug color-math/HDMA tail polish landed as byte-neutral
  source aliases. The promoted contracts name the `EFEAC8` PPU window and
  color-math register setup, DMA channel-4 HDMA table source at `EF:EB1D`,
  HDMA enable shadow bit, and the `EF:EB2A` window/HDMA reset helper.
- 2026-05-01: EF debug runtime loop/cursor command polish landed as
  byte-neutral source aliases. The promoted contracts name `$B559` debug menu
  mode, `$B561/$B563/$B565` saved mode camera/entity state, `$B553` cursor
  sprite slot, `$B555/$B557` command row and input latch, `$B55F` overlay tile
  mode, `$B575` view-character hold flag, the seven visible command rows, and
  the mode-specific view-character/check-position overlay dispatch.
- 2026-05-01: EF battle-text payload split polish landed as ROM-preserving
  data-gap anchors plus `notes/ef-battle-text-payload-runtime-polish.md`. The
  promoted anchors cover HP/PP amount scripts, paralysis/strange/asleep result
  text, shield/timed-substate result pairs, present byte substitution,
  pointer-substitution branches, PP-drain amount text, and battle-start status
  announcements.
- 2026-05-01: EF status-infliction payload follow-up split the adjacent
  `EF:6AFB..6C3A` EBATTLE5 corridor around actual poison `EF:6B18`,
  solidification `EF:6BEF`, and neighboring sick/cold/mushroomized/possessed/
  crying/immobilized/PSI-seal status text anchors.
- 2026-05-01: EF timed shield/reflection payload follow-up split the
  `EF:6F9A..7186` EBATTLE5 corridor into installed/strengthened shield,
  power-shield, psychic-shield, and psychic-power-shield result pairs plus the
  shield-expired, shield-reflection, PSI-name nullify, Neutralizer, and
  Franklin Badge text tail used by the C2 timed-substate and Thunder
  reflection helpers.
- 2026-05-05: EF Spy/metamorphose payload follow-up split the
  `EF:69EA..6AE0` EBATTLE5 corridor into Spy offense/defense amount consumers,
  direct fire/freeze/flash/paralysis/hypnosis/Brain Shock vulnerability
  readouts, metamorphose success/failure text, and the diamondized status text
  adjacent to the existing paralysis/status payload anchors.
- 2026-05-06: EF Spy/metamorphose naming follow-up tightened that corridor:
  `EF:69EA/69FF` now carry Spy `ActionAmount` readout names, `EF:6A0D..6A7F`
  carry direct Spy vulnerability/susceptibility readout names, and
  `EF:6A99/6AB3` carry metamorphose `ResultText` names.
- 2026-05-06: EF HP/PP recovery naming follow-up tightened the EBATTLE5
  recovery front: `EF:69A1` now names HP already-maxed recovery text, while
  `EF:69BA/69D2` carry HP/PP recovered `ActionAmount` names for C2 staged
  delta paths.
- 2026-05-05: EF EBATTLE8 call-for-help/Time Stop follow-up split the
  `EF:77FD..7B77` corridor into the four C2 call-for-help result scripts at
  `EF:77FD`, `EF:7810`, `EF:7824`, and `EF:7830`, the C2 hit-resolution
  Time Stop return script at `EF:7843`, and the then-coarse
  appear/victory/level-up tail at `EF:7858..7B77`.
- 2026-05-05: EF EBATTLE4 damage/miss follow-up split the
  `EF:7186..77FD` corridor around C2-proven damage amount scripts,
  SMAAAASH presentation, shooting/physical dodge, shared no-effect variants,
  physical/shoot miss text, target-gone text, HP/PP drain text, and periodic
  strange/poison/sunstroke/cold damage scripts.
- 2026-05-06: EF EBATTLE4 damage/drain naming follow-up tightened
  `EF:75AB..77DB`: damage/drain/periodic-damage labels now carry
  `ActionAmount`, SMAAAASH carries presentation text, and miss/no-effect/
  target-gone/self-drain labels stay direct text anchors.
- 2026-05-05: EF EBATTLE5 recovery/death follow-up split the
  `EF:6C6B..6F9A` corridor into player collapse, Flying Man/teddy-bear death,
  enemy defeat flavor, affliction recovery/removal, revive success/failure, and
  shield-adjacent recovery payload anchors.
- 2026-05-06: EF death/defeat naming follow-up tightened `EF:6C6B..6E31`:
  player collapse, Flying Man/teddy-bear death payloads, and enemy defeat
  flavor variants now have source names without inherited `MsgBtl`/`MsgSys`
  shells, while Flying Man branch/helper labels remain control-flow anchors.
- 2026-05-05: EF EBATTLE8 present-result follow-up split the
  `EF:7C42..7DD5` continuation behind `MSG_BTL_PRESENT` into
  recipient-cannot-receive, full-inventory, throw-away prompt, abandon
  confirmation, drop-selection, drop-confirmed, and forbidden-drop text
  anchors. This extends the C2/C1 present byte-substitution bridge without
  converting EB text bytes to macro source.
- 2026-05-06: EF EBATTLE8 present-item naming follow-up tightened those source
  anchors: `EF:7BDF/7DD5` now name present item `ByteSubstitutionPayloadText`
  consumers directly, and `EF:7C42..7DBE` separates result text from prompt
  text inside the present continuation.
- 2026-05-06: EF byte-substitution payload suffix follow-up renamed the bare
  `EF:7B77`, `EF:7BDF`, and `EF:7DD5` `19 1F` consumers as
  `ByteSubstitutionPayloadText`, making the staged DD7C payload lane explicit
  without folding it into row-presentation or result-text suffixes.
- 2026-05-05: EF EBATTLE4 status/event prelude follow-up split the
  `EF:7186..75AB` corridor into action-blocking status text, PSI-seal result
  branches, guard/Fly-Honey/homesick flavor, Runaway Five and Poo/Starstorm
  event text, Pokey random talk branches, and companion talk anchors before
  the already split damage pipeline.
- 2026-05-06: EF EBATTLE4 random-talk naming follow-up tightened the tail of
  that corridor: `EF:745F` now marks the Pokey random-talk dispatcher,
  `EF:749D..7548` mark the individual talk branches, and `EF:7569..7593`
  marks the adjacent companion talk text without promoting those flavor/event
  anchors into row-message joins.
- 2026-05-06: EF EBATTLE4 guard/Fly-Honey/homesick naming follow-up tightened
  the front of the same event corridor: `EF:7249` now names guard-on flavor
  text, `EF:725A` names Fly-Honey event text, and `EF:727F..72DB` names the
  homesick random-thought dispatcher plus branches without claiming a row `+4`
  join.
- 2026-05-06: EF EBATTLE8 call-for-help/Time Stop naming follow-up tightened
  the proved direct-result exits: `EF:77FD..7830` now carry call-for-help
  `ResultText` names and `EF:7843` carries the Time Stop return `ResultText`
  name before the encounter-opening island begins.
- 2026-05-06: EF EBATTLE8 encounter/victory naming follow-up tightened
  `EF:7858..7B64`: encounter/surprise variants now use `OpeningText`, the
  victory/loss and level-up announcement labels no longer inherit `MsgBtl`,
  the level-up stat leaves keep C1-staged `ActionAmount` suffixes, and the
  learned-PSI lead-in is separate from the `EF:7B77` byte-substitution text.
- 2026-05-05: EF EBATTLE8 encounter/victory/level-up follow-up split the
  remaining `EF:7858..7B77` tail into encounter-opening variants, group-actor
  helper branches, ordinary/boss/forced victory text, monster-win text,
  level-up/stat-gain amount scripts, and the learned-PSI lead-in before the
  existing `EF:7B77` PSI-name byte-substitution payload.
- 2026-05-05: EF EBATTLE2 action-flavor follow-up split the
  `EF:7E25..843F` island into exact `MSG_BTL_*` payload anchors from
  `MSG_BTL_PPDOWN` through `MSG_BTL_CHOU_ONPA`. The names are intentionally
  symbol-derived pending a later C2 action-table consumer pass.
- 2026-05-06: EF EBATTLE2 proved-row naming follow-up promoted rows `99`,
  `100`, `101`, `102`, `104`, `117`, and `118` to gameplay-facing
  `RowPresentationText` anchors, leaving the remaining unproved EBATTLE2
  action-flavor labels as exact `MSG_BTL_*` symbols.
- 2026-05-06: EF EBATTLE2 row `207` follow-up promoted `EF:83A8` to a
  strange-status `RowPresentationText` anchor, closing the proved status-row
  outlier that reuses the `C2:8D3A -> C2:A056` body.
- 2026-05-06: EF row-message crosswalk consolidation updated proved early
  command/PSI joins and rows `243/244` to show their promoted source labels,
  keeping the exact `MSG_BTL_*` policy only for unproved action islands.
- 2026-05-05: EF EBATTLE1 battle-command front follow-up split
  `EF:848C..8814` into Bash/attack, Shoot, Guard, Metamorphose, flee, Spy,
  shared PSI action text, and the first PSI animation/effect dispatch branches.
- 2026-05-06: EF EBATTLE1 row-presentation naming follow-up tightened that
  front so Bash/Shoot/Spy/shared-PSI/Pray carry `RowPresentationText`,
  `EF:8543` keeps the shared PSI-name `ByteSubstitution` role, and Thunder
  common anchors carry presentation-text names without changing C1/C2 source.
- 2026-05-06: EF EBATTLE0 status naming follow-up tightened `EF:843F..8477`:
  battle-start asleep/PSI-seal/strange text now names the target-context
  `DC1C` status-announcement lane, and random-action strange/mushroom text now
  names the pre-`DD9F` direct status lane without inherited `MsgAtStart` or
  `MsgRandomAct` shells.
- 2026-05-05: EF EBATTLE1 Thunder/effect/Pray follow-up split
  `EF:8814..89FE` into small/large Thunder presentation text, Thunder miss
  sound text, PBFX presentation branches 17-50, and the Pray action opening
  text at `EF:89E0`.
- 2026-05-05: EF EBATTLE3 action-flavor follow-up split the complete
  `EF:89FE..8FAD` enemy-action text include into exact `MSG_BTL_*` anchors
  from `MSG_BTL_JIHIBIKI` through `MSG_BTL_GYIYYIG_3`.
- 2026-05-06: EF EBATTLE3 proved-row naming follow-up promoted rows `159`,
  `228`, `232`, `248`, `273`, and `290`, plus shared rows `140/247`, to
  gameplay-facing `RowPresentationText` anchors while keeping the remaining
  EBATTLE3 action-flavor labels as exact `MSG_BTL_*` symbols.
- 2026-05-05: EF EBATTLE9 field/graveyard follow-up split the complete
  `EF:8FAD..9A47` include into field-monster, graveyard/Paula, boss/girl, and
  Guts tutorial message anchors.
- 2026-05-05: EF EBATTLE1 action-tail follow-up split `EF:9A47..9EF4` into
  action payload anchors from `MSG_BTL_NAKAMA0` through `MSG_BTL_FIRE_BREATH`.
- 2026-05-06: EF EBATTLE1 late-status naming follow-up promoted proved
  action-tail status rows `75`, `76`, `78..87`, and `90` to
  `RowPresentationText` anchors while keeping their behavior-emitted
  success/fallback direct-result scripts separate.
- 2026-05-05: EF EGOODS2 item-use follow-up split `EF:9EF4..A2FA` into Exit
  Mouse, Hieroglyph, Town Map, and traveler-shack payload branches.
- 2026-05-05: EF tail follow-up split `EF:A2FA..C51B` into unknown event,
  command/status window text, name-input keyboard, `UNKNOWN7`, and debug/menu
  runtime payload anchors.
- 2026-05-05: EF front text-payload follow-up split `EF:4E20..69A1` into PSI
  explanation, Dungeon Man/Deep Darkness, and Grapefruit Falls/Threed payload
  anchors.
- 2026-05-05: EF glyph/debug-string follow-up split `EF:C51B..D56F` into the
  text glyph merge mask table, companion carry-mask table, and debug sound-menu
  option/version strings.
- 2026-05-05: EF debug menu string follow-up split `EF:D8B5..D95E` into the
  ROM/version header, title line, and seven selectable debug-menu option rows.
- 2026-05-05: EF debug tail data follow-up aligned `EF:EB1D..EB2A` as the
  debug color-math window HDMA table and added the missing `EF:EB3D` debug
  cursor tilemap anchor before `DEBUG_MENU_FONT`.
- 2026-05-05: EF late-tail follow-up split `EF:F0D7..10000` into the two
  unknown data includes, embedded version string, three unused data blocks,
  debug cursor spritemap pointer/entries, and residual bank padding.
- 2026-05-05: EF debug font-palette follow-up split `EF:EF70..EFB7` into the
  unknown `EFEF70` include and the `DEBUG_FONT_PALETTE` payload.
- 2026-05-06: EF battle-text payload naming follow-up tightened the source
  anchor suffixes for C1/C2 consumer joins: `ActionAmount` for
  `C1:DC66`/`$9D12/$9D14`/`1C 0F` scripts, `ByteSubstitution` for
  `C1:DD7C`/`$9D11`/`19 1F` scripts, and `PointerSubstitution` for `19 1E`
  branches. This was an EF-only label/comment pass over ROM-preserved text
  bytes.
- 2026-05-06: EF action-island consumer frontier follow-up added
  `notes/ef-battle-text-action-island-consumer-frontier.md` and source comments
  at the EBATTLE2, EBATTLE1-front, EBATTLE3, and EBATTLE1-tail action islands.
  The handoff separates `C1:DD9F` row `+4` message pointers, row `+8` C2
  behavior payloads, and direct `DC1C`/`DC66` result scripts.
- 2026-05-06: EF row-message crosswalk follow-up added
  `notes/ef-battle-text-row-message-crosswalk.md`, mapping source-backed
  `D5:7B68` rows onto EF row-message anchors and the secondary result scripts
  emitted by their C2 row `+8` behavior bodies.
- 2026-05-06: EF row-message frontier follow-up tightened that crosswalk around
  evidence boundaries: behavior-known numeric-effect and no-op/flavor rows were
  listed as blocked on row `+4` EF pointer recovery rather than treated as
  nameable action-message joins.
- 2026-05-06: EF special-event row-message follow-up promoted the locally
  proved row `243` and `244` joins into the same crosswalk, keeping their
  `C1:DD9F` row presentation messages separate from the direct event-result
  continuations emitted by their C2 behavior bodies.
- 2026-05-06: EF healing/explosive row-message follow-up promoted rows `99`,
  `101`, and `140` into the row-message crosswalk and marked C9 item/Final
  Prayer row messages as non-EF presentation lanes that should not drive EF
  anchor naming.
- 2026-05-06: EF PSI-status row-message follow-up promoted rows `53` and `58`
  into the crosswalk as shared `EF:8543` PSI presentation rows with separate
  asleep/strange result payloads emitted by their C2 behavior bodies, and
  extended the non-EF C9 item lane to later bomb-family rows `310` and `311`.
  A later pointer-recovery pass resolved the temporary blocker for explosive
  rows `64/65` and PSI-side Lifeup rows `32..35`.
- 2026-05-06: EF row-pointer recovery frontier follow-up added
  `notes/ef-battle-text-row-pointer-recovery-frontier.md`, pinning the initial
  local blocker and recovery commands for remaining row `+4` joins before any
  further EF action-anchor promotion.
- 2026-05-06: EF row-pointer recovery follow-up used the local ROM-backed
  action inspector to promote Lifeup rows `32..35`, PSI offense-up rows
  `48/49`, numeric-effect rows `95..98/233/234`, and explosive rows `64/65`
  into the concrete EF row-message crosswalk. Source labels now carry
  `RowPresentationText` names for those anchors while C8/HP result lanes remain
  separate.
- 2026-05-06: EF no-op/flavor row-pointer follow-up recovered rows
  `119..134`, `251..257`, and `260..266` as EF row-message joins over
  `C2:9033` or tiny no-op tails. Rows `119..134` now carry EBATTLE2
  `FlavorRowPresentationText` source labels; the EBATTLE4/status dual-use
  anchors stay named by event/status/result role.
- 2026-05-06: EF consumer-lane contract follow-up added
  `notes/ef-battle-text-consumer-lane-contracts.md`, a compact EF-side decision
  table for row presentation, direct result, amount, byte/pointer substitution,
  and non-EF row-message lanes.
- 2026-05-06: EF row-pointer recovery triage follow-up expanded
  `notes/ef-battle-text-row-pointer-recovery-frontier.md` with inspector
  command coverage and output buckets for sorting recovered rows before EF
  anchor promotion.
- 2026-05-06: EF source-comment lane follow-up added byte-neutral comments at
  the proved row-message anchors so the EF source distinguishes `DD9F`
  presentation text from `DC1C` continuations and behavior-emitted result
  payloads without requiring a notes lookup.
- 2026-05-06: EF status-result source-comment follow-up added byte-neutral
  comments at `EF:6B81..6C55` and `EF:766E` to keep C2 row `+8` `DC1C`
  result emissions separate from row `+4` presentation messages in the source.
- 2026-05-06: EF negative-guardrail source follow-up added byte-neutral
  comments at Lifeup-looking anchors so `EF:5173..51BB` and `EF:8D4C` remain
  separate from the recovered row `32..35 -> EF:8543` presentation join.
- 2026-05-06: EF amount-result suffix follow-up renamed `EF:7755..77DB`
  PP-loss and periodic damage anchors as `ActionAmount` scripts so their
  `DC66`/`1C 0F` payload contract is visible in source.
- 2026-05-06: EF level-up amount suffix follow-up renamed `EF:7A7D..7B46`
  stat-gain anchors as `ActionAmount` scripts and clarified that C1 level-up
  leaves stage their deltas through `C1:AD0A` before `1C 0F`.
- 2026-05-06: EF byte-substitution suffix follow-up renamed the shield
  PSI-name scripts `EF:70D2/70FA` and shared PSI row text `EF:8543` so their
  `C1:DD7C -> $9D11 -> 19 1F` payload contract is visible at the source
  anchor without changing the row-presentation lane model.
- 2026-05-06: EF pointer-substitution suffix follow-up normalized the
  `EF:7B85/7BA2/7BC1` branch anchors so the lane noun leads the label, and
  documented that the adjacent `EF:7B83/7BA0/7BBF` anchors are branch-state
  separators rather than parsed `19 1E` consumer sites.
- 2026-05-06: EF `C2:9039` default/item-use follow-up completed the broad
  default bucket by row `+4` bank. The EF side now records shared PSI rows
  `60/61`, EGOODS2 item-use rows `259`, `270`, and `271`, flee row `279`, and
  EBATTLE3 flavor rows `309` and `313..317`; C7/C9/C6 rows such as
  `190..200`, `272/276`, `281/282`, `284..289`, `308`, and `312` remain
  consumer-contract notes rather than EF anchor-renaming evidence.
- 2026-05-06: EF neighboring no-op-tail follow-up completed the
  `C2:903C/903F..904E` bank-first classification. Row `9` stays non-EF C7,
  while rows `251..256` remain EF homesick/action-blocked/recovery row-message
  joins with dual-use labels and source comments instead of new anchor names.
- 2026-05-06: EF EBATTLE2 exact-message follow-up promoted the row-backed
  `MSG_BTL_*` anchors for rows `103`, `105..116`, `201..206`, `208..210`, and
  reuse row `238` to `RowPresentationText`, preserving symbol stems while
  removing that EBATTLE2 island from the exact-anchor frontier.
- 2026-05-06: EF EBATTLE3 exact-message follow-up promoted the row-backed
  `MSG_BTL_*` anchors for rows `160/161/176`, `211..227`, `229..231`,
  `241/242`, and `274/300..307` to `RowPresentationText`, with no-op rows
  `235/236` carrying `FlavorRowPresentationText`.
- 2026-05-06: EF EBATTLE1 action-tail exact-message follow-up promoted the
  row-backed `MSG_BTL_*` anchors for rows `62/63`, `66..74`, `77`, `88/89`,
  and `91..94` to `RowPresentationText`, closing the exact battle-action
  anchor frontier while preserving EGOODS2 item-use payload semantics.
- 2026-05-06: EF EGOODS2 item-use guardrail follow-up renamed the remaining
  inherited battle-message shells at `EF:9EF4`, `EF:A0DC`, and `EF:A2AB` as
  `ItemUsePayloadText`, closing the row-backed legacy-shell inventory entirely.
- 2026-05-06: EF status-result label follow-up renamed the proved direct
  `DC1C` status-result anchors across `EF:6AC7..6C55` and shared fallback
  `EF:766E` with `StatusResultText`, keeping them distinct from `DD9F` row
  `+4` presentation anchors.
- 2026-05-06: EF recovery/removal result label follow-up renamed
  `EF:6E4A..6F64` cleanup scripts with `RecoveryResultText` or
  `RemovalResultText` so the C2 affliction-recovery direct-result lane is
  visible in source.
- 2026-05-06: EF revive/shield result label follow-up renamed `EF:6F7C..7160`
  direct result scripts with `ResultText`, preserving `ByteSubstitution` on
  `EF:70D2/70FA` because those PSI shield result scripts consume `19 1F`.
- 2026-05-06: EF EBATTLE4 action-blocked status follow-up renamed
  `EF:7186..720C` with `ActionBlockedStatusText` and marked `EF:7221` as the
  PSI-seal `ByteSubstitutionResultText` consumer behind the player-side branch.
- 2026-05-06: EF special-event lane label follow-up renamed row `243/244`
  anchors so `EF:72F6/7415` are `RowPresentationText` and
  `EF:72F7/733D/743B` are behavior-emitted `ResultText` continuations.
