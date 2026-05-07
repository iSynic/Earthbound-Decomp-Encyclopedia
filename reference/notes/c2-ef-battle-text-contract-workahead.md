# C2 ↔ C1 Battle Text + EF Script Contracts (Workahead)

Scope: scout battle text and EF text-script contracts that should drive **C2 source naming / promotion**, with emphasis on:

- C2 callers into `C1:DC1C`, `C1:DC66`, `C1:DD9F`
- EF battle-text payloads and their control-code structure
- substitution commands (`0x19` family) and amount/status-result text (`0x1C` family)

This is a **workahead contract note** (no source/manifest edits). It consolidates local callers + `refs/ebsrc` text-bank maps + existing note conclusions so manual integration can promote the right C2 corridors with stable semantics.

## Implementation status

- 2026-04-30: first runtime semantic-polish pass landed byte-neutral source
  comments/local aliases for the pinned `C1:DC1C`, `C1:DC66`, `C1:DD9F`,
  `C1:AD0A`, and `C1:AD26` contracts plus the C2 HP/PP amount-message callers
  and the `D5:7B68` action-table mode-1 message lane. The wider 39-call
  `DC66` sweep and remaining status-result callers are still future work.
- 2026-04-30: second pass named the local EF status-result scripts for
  resist-checked crying, solidified, asleep, poison, strange, PP drain, and
  timed shield/substate messages. These source aliases are intentionally local
  to the C2 callers until a wider EF text payload naming pass promotes shared
  script labels.
- 2026-04-30: third pass removed the remaining local
  `C1DC66_DisplayBattleTextWithNumber` aliases from C2 source modules and
  named the C8/EF amount-result scripts for PP, guts, offense, and defense
  stat/resource deltas, plus the C8 IQ-increase amount script.
- 2026-04-30: fourth pass promoted the direct stat-increase consequence leaves
  (`C2:B3D8..B5E3`) and the `C2:A056` 1d4/random stat-up wrappers so their
  selected-row offsets, C8 amount scripts, C8 script bank, and `C1:DC66`
  substitution-payload calls are named at the source sites. The `B3D8..B573`
  direct leaves also name the live character mirror bytes and derived-stat
  refresh helpers used before printing the amount.
- 2026-04-30: fifth pass promoted the `C2:A3D1..A5EC` item-side text surface.
  The source now names direct `DC1C` messages for concentration/PSI-seal,
  shield-expired/clear, solidification, no-effect, and HP-sucker self-drain, and names
  the `DC66` amount-bearing HP-sucker script at `EF:7729`.
- 2026-05-01: sixth pass promoted the `C2:A89D..AF1F` item/status cluster.
  The source now names poison, solidification, asleep, strange, and shared
  no-effect direct-text scripts, the C8 doubled-guts and defense-up amount
  scripts, and the `DC66` amount-bearing calls used by Sudden Guts Pill and the
  item-side defense-up wrapper.
- 2026-05-01: seventh pass promoted the short item/status helper leaves at
  `C2:A39D`, `C2:A630`, `C2:A82A`, and `C2:A86B`. These now name poison-removed
  `EF:6E97`, solidification `EF:6BEF`, no-effect `EF:766E`, the EF text bank,
  and their `DC1C` direct-text calls.
- 2026-05-01: eighth pass promoted the late normalization/odor continuation
  seam. `C2:AF1F` now names the metamorphose success/failure scripts
  (`EF:6A99` / `EF:6AB3`) and `C2:B172` names the condiment spice hit/miss
  scripts (`C9:7C9D` / `C9:7CB1`) plus the shared no-effect fallback
  (`EF:766E`) and their `DC1C` direct-text dispatches.
- 2026-05-01: ninth pass promoted the bottle-rocket item family. The shared
  `C2:A57A` helper now names its zero-hit `EF:766E` no-effect fallback through
  `DC1C`, while the successful-hit path stays damage-only and does not claim an
  amount-bearing battle-text contract.
- 2026-05-01: tenth pass returned to the battle-start payload joins. The
  `C2:5024..6189` controller and `C2:6189..654C` instant-win handler now use
  source aliases for `DC1C`, `DC66`, and `DD7C`, name the EF/C8 battle scripts
  staged by those paths, and mark the `$AA10 -> $9D11 -> EF:7BDF` present-item
  byte-substitution bridge at the source sites.
- 2026-05-01: eleventh pass promoted the call-for-help result text exits.
  `C2:BD13`, `C2:BD5E`, and `C2:BE6C` now name the `DC1C` dispatch ABI and the
  four EF result scripts (`EF:77FD`, `EF:7810`, `EF:7824`, `EF:7830`) used by
  ordinary and seed/sprout-flavored reinforcement outcomes.
- 2026-05-01: twelfth pass promoted the remaining Rainbow Colors / Final
  Prayer direct battle-text exits. `C2:C14E`, `C2:C37A`, `C2:C41F`,
  `C2:C572`, and `C2:C6F0` now name the `DC1C` dispatch ABI plus the C8/C9
  special-event, prayer, finale, and Pokey run-away scripts staged by those
  helpers.
- 2026-05-01: C1-side ABI follow-up tightened the source comments/constants
  around the same joins. `DC1C`, `DC66`, `DD82`, `DD9F`, `ACF8`, `AD02`,
  `AD0A`, and `AD26` now spell out caller-frame aliasing, byte/pointer
  substitution slots, and the `19 1E`, `19 1F`, and `1C 0F` EF text-command
  consumers that C2 callers rely on.
- 2026-05-01: C1 display-text consumer follow-up named the `1C 0F`
  `PRINT_ACTION_AMOUNT` branch in source. The branch now explicitly reloads
  the `DC66`/`AD0A` payload through `C1:AD26`, stages it to `$0E/$10`, and
  prints it through `C1:0DF6`.
- 2026-05-01: EF text-payload split follow-up added source anchors for the
  C2-proven battle scripts and corrected the local `C2:9FFE` naming drift:
  `EF:6AE0` is the body-numb/paralysis result used by `BTLACT_PARALYSIS_A`,
  while poison-inflicted text remains the separate `EF:6B18` script.
- 2026-05-01: EF status-infliction payload follow-up split the neighboring
  EBATTLE5 status text around `EF:6B18` poison and `EF:6BEF` solidification,
  matching the item/status cluster aliases already used by C2.
- 2026-05-01: Present/Check Present source follow-up named `$AA10` as the
  local `BattlePresentItemByte` in the C2 producer and consumer corridors.
  The source now ties D5 enemy dropped-item offset `+0x58`, drop-rate offset
  `+0x57`, the `C2:3109` UFO fallback table, `EF:7BDF`, and `EF:7DD5` to the
  same `$AA10 -> C1:DD7C -> $9D11 -> 19 1F` byte-substitution bridge.
- 2026-05-01: Spy readout source follow-up named the `BTLACT_SPY` target
  battler stat/resistance fields. `EF:69EA` and `EF:69FF` are `DC66`
  amount-payload consumers for offense/defense, while the resistance messages
  are direct `DC1C` scripts gated by `0xFF` vulnerability bytes.
- 2026-05-05: EF payload follow-up added source anchors for the Spy readout
  scripts at `EF:69EA`, `EF:69FF`, `EF:6A0D`, `EF:6A24`, `EF:6A3C`,
  `EF:6A54`, `EF:6A6C`, and `EF:6A7F`, plus the neighboring metamorphose
  and diamondized scripts at `EF:6A99`, `EF:6AB3`, and `EF:6AC7`.
- 2026-05-06: EF Spy/metamorphose naming follow-up removed inherited
  `MsgBtlCheck*` labels from `EF:69EA..6A7F`, keeping Spy offense/defense as
  `ActionAmount` readouts and resistance buckets as direct readout text, then
  named `EF:6A99/6AB3` as metamorphose `ResultText`.
- 2026-05-06: EF HP/PP recovery naming follow-up tightened `EF:69A1..69D2`:
  HP already-maxed stays a recovery text anchor, while HP and PP recovered
  paths carry `ActionAmount` names for the C2 `DC66` staged-delta paths.
- 2026-05-05: EF EBATTLE8 follow-up added source anchors for the four
  call-for-help result scripts (`EF:77FD`, `EF:7810`, `EF:7824`, `EF:7830`)
  and the Time Stop return script at `EF:7843`.
- 2026-05-05: EF EBATTLE8 encounter/victory/level-up follow-up split the
  `EF:7858..7B77` tail into encounter-opening variants, group-actor helper
  branches, victory/loss text, level-up/stat-gain amount scripts, and the
  learned-PSI lead-in before the existing PSI-name byte-substitution payload.
- 2026-05-05: EF EBATTLE2 action-flavor follow-up split `EF:7E25..843F`
  into exact `MSG_BTL_*` anchors. These are intentionally symbol-derived for
  now; the C2 action-table consumer pass can translate or group them once the
  source-side action ids are pinned.
- 2026-05-05: EF EBATTLE1 front follow-up split `EF:848C..8814` around the
  action-table text pointers already proved in
  `notes/class2-d57b68-battle-action-table-match.md`: ordinary Bash/attack
  `EF:848C`, Spy/check `EF:8530`, and shared PSI `ByteSubstitution` text
  `EF:8543`, plus the adjacent PSI animation/effect dispatch branches.
- 2026-05-06: EF EBATTLE1 row-presentation naming follow-up renamed the proved
  Bash/Shoot/Spy/shared-PSI/Pray anchors with `RowPresentationText`, kept
  shared PSI as a `ByteSubstitution` consumer, and converted the adjacent
  Thunder common labels to presentation text without editing C1/C2 source.
- 2026-05-05: C1-side DD9F tail follow-up named the source-side consumer of
  the action-table Bash/Shoot text and companion payload offsets. The
  `C1:DD9F..E1A2` source now keeps `$00BC/$00BE` current text pointers
  distinct from wrapper dispatch staging, names the selected-row equipment and
  stat/resistance mirrors, and ties the hardcoded `C7:7E11` / `C7:7E33`
  equip-ok/fail scripts to the equipment redirect tail.
- 2026-05-05: EF EBATTLE1 Thunder/effect follow-up split `EF:8814..89FE`
  around the C2 Thunder common text pointers (`EF:8814` small Thunder,
  `EF:8823` large Thunder), Thunder miss sound payload `EF:8837`, PBFX
  presentation branches 17-50, and the action-table Pray pointer `EF:89E0`.
- 2026-05-05: EF EBATTLE3 action-flavor follow-up split the complete
  `EF:89FE..8FAD` include into exact `MSG_BTL_*` anchors, from
  `MSG_BTL_JIHIBIKI` through `MSG_BTL_GYIYYIG_3`, ready for a later C2
  action-table consumer pass.
- 2026-05-06: EF EBATTLE3 proved-row naming follow-up promoted the row-message
  anchors for rows `159`, `228`, `232`, `248`, `273`, and `290`, plus shared
  rows `140/247`, into `RowPresentationText` labels while leaving unproved
  EBATTLE3 action-flavor payloads symbol-derived.
- 2026-05-06: EF EBATTLE1 late-status naming follow-up promoted proved
  action-tail status rows `75`, `76`, `78..87`, and `90` from inherited
  `MSG_BTL_*` labels into `RowPresentationText` anchors, keeping their
  behavior-emitted success/fallback result scripts separate.
- 2026-05-06: EF EBATTLE2 row `207` follow-up promoted `EF:83A8` from the
  inherited `MSG_BTL_LAUGH_HEN` shell into a strange-status
  `RowPresentationText` anchor, matching its `C2:8D3A -> C2:A056` behavior
  join.
- 2026-05-06: EF row-message crosswalk consolidation updated the proved early
  command/PSI joins and rows `243/244` to use their promoted source labels
  directly, leaving only unproved action islands under the exact `MSG_BTL_*`
  naming policy.
- 2026-05-06: EF row-pointer recovery follow-up used the local ROM-backed
  action inspector to prove Lifeup rows `32..35`, PSI offense-up rows `48/49`,
  numeric-effect rows `95..98/233/234`, and explosive rows `64/65` as concrete
  EF row `+4` presentation joins. The EF source now promotes those anchors to
  `RowPresentationText` names while keeping C8/HP amount-result lanes separate.
- 2026-05-06: EF no-op/flavor row-pointer follow-up proved rows `119..134`,
  `251..257`, and `260..266` as EF row `+4` presentation joins over
  `C2:9033` or tiny no-op tails. The EBATTLE2 `119..134` strip now uses
  `FlavorRowPresentationText` source labels, while dual-use EBATTLE4/status
  anchors remain named for their event/status/result roles.
- 2026-05-05: EF EBATTLE9 field/graveyard follow-up split the complete
  `EF:8FAD..9A47` include into the `_SUB_SOREZORE` helper, Sanctuary
  field-monster payloads, graveyard/Paula branches, and the Guts tutorial
  yes/no system-message tail.
- 2026-05-05: EF EBATTLE1 action-tail follow-up split `EF:9A47..9EF4` into
  exact `MSG_BTL_*` anchors from `MSG_BTL_NAKAMA0` through
  `MSG_BTL_FIRE_BREATH`, stopping before the next `EGOODS2` item-use include.
- 2026-05-05: EF EGOODS2 item-use follow-up split `EF:9EF4..A2FA` around
  Exit Mouse success/failure branches, Hieroglyph, Town Map, and Onett
  traveler-shack payloads.
- 2026-05-05: EF tail follow-up split `EF:A2FA..C51B` into the unknown
  monster-off/Sky Runner event payload, command/status window text tables,
  name-input keyboard layouts, `UNKNOWN7`, and the debug/menu runtime script.
- 2026-05-05: EF front text-payload follow-up split `EF:4E20..69A1` into
  `EEXPLPSI` PSI explanation scripts, `E16DKFD` Dungeon Man/Deep Darkness
  field-event payloads, and `E07GPFT` Grapefruit Falls/Threed payloads.
- 2026-05-05: EF EBATTLE4 damage/miss follow-up added source anchors for the
  hit-resolution damage amount scripts (`EF:75AB`, `EF:75C2`, `EF:75D9`,
  `EF:75F0`, `EF:7607`), SMAAAASH/dodge scripts (`EF:7624`, `EF:7630`,
  `EF:763C`, `EF:7655`), miss/target-gone and HP-sucker scripts
  (`EF:76C7`, `EF:76D8`, `EF:76FD`, `EF:7710`, `EF:7729`), and periodic
  status damage scripts (`EF:7768`, `EF:7787`, `EF:77B1`, `EF:77DB`).
- 2026-05-06: EF EBATTLE4 damage/drain naming follow-up removed inherited
  `MsgBtl` shells from `EF:75AB..77DB`, keeping HP/PP damage/drain and
  periodic damage anchors as `ActionAmount`, SMAAAASH as presentation text,
  and no-effect/miss/target-gone/HP-sucker self-drain as direct text anchors.
- 2026-05-05: EF EBATTLE4 prelude follow-up added source anchors for the
  preceding `EF:7186..75AB` status/event scripts: action-blocking status
  flavor, PSI-seal result text, guard/Fly-Honey/homesick text, Runaway Five
  and Poo/Starstorm event scripts, Pokey random talk branches, and companion
  talk payloads.
- 2026-05-05: EF EBATTLE5 recovery/death follow-up added source anchors for
  C2-facing recovery scripts including poison removed `EF:6E97`, nausea
  recovered `EF:6E81`, crying recovered `EF:6ED1`, strange recovered
  `EF:6F1E`, sunstroke cured `EF:6F38`, asleep recovered `EF:6F54`, and
  PSI-seal recovered `EF:6F64`, plus adjacent collapse/death/revive result
  payloads in `EF:6C6B..6F9A`.
- 2026-05-06: EF death/defeat naming follow-up removed inherited
  `MsgBtl`/`MsgSys` prose from `EF:6C6B..6E31`, naming player collapse,
  Flying Man/teddy-bear death, and enemy defeat flavor anchors while leaving
  Flying Man branch/helper labels as control-flow anchors.
- 2026-05-06: EF source-only naming follow-up tightened the payload anchor
  suffixes used by C1/C2 joins. `ActionAmount` now names EF scripts that
  consume `C1:DC66` secondary payloads through `$9D12/$9D14 -> 1C 0F`;
  `ByteSubstitution` names `C1:DD7C -> $9D11 -> 19 1F` consumers; and
  `PointerSubstitution` names the `19 1E` payload branches. No C2 source was
  edited in this pass.
- 2026-05-06: EF EBATTLE4 random-talk follow-up renamed the Pokey random-talk
  dispatcher at `EF:745F`, its branch texts through `EF:7548`, and the
  adjacent My Dog/Pickey/Tony/Balmon companion talk anchors through `EF:7593`.
  These remain flavor/event text islands until a C2 caller or row-pointer pass
  proves a stronger consumer lane.
- 2026-05-06: EF EBATTLE0 status naming follow-up removed the inherited
  `MsgAtStart`/`MsgRandomAct` shells from `EF:843F..8477`. Battle-start
  asleep/PSI-seal/strange anchors now name `BattleStart...StatusAnnouncementText`
  direct `DC1C` emissions, while random-action strange/mushroom anchors name
  `RandomAction...StatusText` before the `DD9F` row-message lane.
- 2026-05-06: EF EBATTLE2 proved-row naming follow-up promoted rows `99`,
  `100`, `101`, `102`, `104`, `117`, and `118` from inherited `MSG_BTL_*`
  labels into `RowPresentationText` anchors while leaving unproved EBATTLE2
  action-flavor payloads symbol-derived.
- 2026-05-06: EF EBATTLE4 guard/Fly-Honey/homesick naming follow-up renamed
  `EF:7249..72DB` from inherited `MsgBtl` anchors into guard-on flavor,
  Fly-Honey event, homesick dispatcher, and homesick branch labels. The pass
  deliberately left them as event/flavor anchors rather than row-presentation
  joins.
- 2026-05-06: EF EBATTLE8 call-for-help/Time Stop naming follow-up renamed
  the four proved call-for-help `DC1C` exits at `EF:77FD..7830` and the Time
  Stop return at `EF:7843` with `ResultText` suffixes, leaving the encounter
  opening island at `EF:7858+` separate.
- 2026-05-06: EF EBATTLE8 encounter/victory naming follow-up tightened the
  `EF:7858..7B64` tail: encounter and surprise variants now carry
  `OpeningText`, victory/loss and level-up announcement labels drop inherited
  `MsgBtl` prose, and `EF:7A7D..7B46` keep C1 level-up `ActionAmount`
  semantics before the learned-PSI lead-in.
- 2026-05-06: EF action-island frontier follow-up documented the remaining
  `MSG_BTL_*` row-message islands separately from direct result payloads. The
  handoff note names the `C1:DD9F` row `+4` message lane, the row `+8`
  behavior-payload lane, and the currently proved EF row-message joins for
  Bash/Shoot/Spy/Pray/shared PSI plus late EBATTLE2 and concentration anchors.
- 2026-05-06: EF row-message crosswalk follow-up expanded the proved `DD9F`
  row `+4` joins into source-backed late status, physical/special, and
  normalization/event rows. See
  `notes/ef-battle-text-row-message-crosswalk.md`.
- 2026-05-06: EF row-message frontier follow-up separated behavior-known rows
  from proved EF message joins. This initially kept numeric-effect and
  no-op/flavor rows deferred until local row `+4` pointer recovery could prove
  their EF action-message labels.
- 2026-05-06: EF special-event row-message follow-up promoted rows `243` and
  `244` into the row-message crosswalk: `EF:72F6 -> C2:9298` and
  `EF:7415 -> C2:92EE`, with their behavior continuations kept as separate
  direct-result text.
- 2026-05-06: EF healing/explosive row-message follow-up added rows `99`,
  `101`, and `140` to the proved row `+4` crosswalk and documented C9 item and
  Final Prayer row-message lanes as non-EF presentation consumers.
- 2026-05-06: EF PSI-status row-message follow-up added rows `53` and `58` as
  shared `EF:8543` PSI `ByteSubstitution` presentation joins whose C2 bodies
  emit asleep and strange direct-result scripts separately. The same pass
  extended the non-EF C9 item row-message lane to the later bomb-family rows
  `310` and `311`. The later row-pointer recovery pass resolved the temporary
  blocker for explosive rows `64/65` and PSI-side Lifeup rows `32..35`.
- 2026-05-06: EF row-pointer recovery frontier follow-up added
  `notes/ef-battle-text-row-pointer-recovery-frontier.md`, documenting the
  original local blocker for new row `+4` joins: D5 source preserves the table
  as a data gap and the inspector needs a local ROM. The local ROM is now
  present, so the note tracks recovered joins and the remaining default/item-use
  classification frontier.
- 2026-05-06: EF consumer-lane contract follow-up added
  `notes/ef-battle-text-consumer-lane-contracts.md`, consolidating the
  `DD9F`, `DC1C`, `DC66`, `DD7C`, pointer-substitution, and non-EF C7/C8/C9
  row-message lane rules used by the EF crosswalk.
- 2026-05-06: EF row-pointer recovery triage follow-up expanded the inspector
  command list and output buckets so recovered rows can be sorted into proved
  EF row messages, non-EF row messages, result-only EF emissions, or still
  behavior-only frontier rows before any EF anchor promotion.
- 2026-05-06: EF source-comment lane follow-up copied the strongest proved
  row-message joins back to the EF anchors themselves, including special-event
  row presentation versus direct continuations, shared PSI row text, reused
  `EF:8E27`, healing/explosive row messages, row `290`, and the late status
  row-message cluster.
- 2026-05-06: EF status-result source-comment follow-up marked the nearby
  `EF:6B81..6C55` status payloads and `EF:766E` no-effect fallback as `DC1C`
  direct-result emissions from C2 row `+8` behavior, not row `+4` presentation
  messages.
- 2026-05-06: EF status-result label follow-up extended that source contract
  across the proved EBATTLE5 status island (`EF:6AC7..6C55`) and shared
  EBATTLE4 no-effect fallback (`EF:766E`) with `StatusResultText` anchors.
- 2026-05-06: EF recovery/removal label follow-up applied the same direct
  result-lane contract to `EF:6E4A..6F64`, using `RecoveryResultText` and
  `RemovalResultText` anchors for the C2 affliction-cleanup helper emissions.
- 2026-05-06: EF revive/shield result label follow-up carried `ResultText`
  through `EF:6F7C..7160`, including revive success/failure, shield
  install/strengthen pairs, expiry/reflection, Neutralizer, Franklin Badge, and
  PSI-name shield `ByteSubstitutionResultText` scripts.
- 2026-05-06: EF EBATTLE4 status-block label follow-up renamed
  `EF:7186..720C` as `ActionBlockedStatusText` anchors and kept the PSI-seal
  `EF:7221` branch as `ByteSubstitutionResultText`.
- 2026-05-06: EF special-event lane label follow-up renamed row `243/244`
  event anchors so `EF:72F6/7415` carry `RowPresentationText` and
  `EF:72F7/733D/743B` carry `ResultText` continuation semantics.
- 2026-05-06: EF negative-guardrail source follow-up marked Lifeup explanation
  and enemy-flavor anchors as not row-message joins. The later pointer-recovery
  pass proved `EF:8543` for rows `32..35` and `EF:9A7E/9A9E` for rows `64/65`,
  so those guardrails now only prevent adjacent-lane confusion.
- 2026-05-06: EF amount-result suffix follow-up renamed the `EF:7755..77DB`
  PP-loss and periodic-damage result anchors with `ActionAmount` suffixes,
  matching their `C1:DC66 -> 1C 0F` payload consumption.
- 2026-05-06: EF level-up amount suffix follow-up applied the same
  `ActionAmount` naming contract to `EF:7A7D..7B46`, while documenting that
  these are C1 level-up narration consumers staged through `C1:AD0A`, not C2
  action-row messages.
- 2026-05-06: EF `C2:9039` default/item-use follow-up completed the broad
  default bucket by row `+4` bank. Rows `60/61`, `259`, `270`, `271`, `279`,
  `309`, and `313..317` now have EF joins, with EBATTLE3 flavor anchors
  promoted to `FlavorRowPresentationText`; rows `190..200`, `272/276`,
  `281/282`, `284..289`, `308`, and `312` stay in non-EF C7/C9/C6
  presentation lanes.
- 2026-05-06: EF neighboring no-op-tail follow-up classified `C2:903C` and
  `C2:903F..904E`. Row `9` is the only `C2:903C` non-EF C7 lane, and rows
  `251..256` are the only `903F..904E` EF joins, already named as
  homesick/action-blocked/recovery payloads rather than pure flavor anchors.
- 2026-05-06: EF EBATTLE2 exact-message follow-up promoted row-backed
  `MSG_BTL_*` anchors `103`, `105..116`, `201..206`, `208..210`, and `238` to
  `RowPresentationText`, leaving later exact-anchor passes to discharge the
  other row-backed islands.
- 2026-05-06: EF EBATTLE3 exact-message follow-up promoted row-backed
  `MSG_BTL_*` anchors `160/161/176`, `211..227`, `229..231`, `241/242`, and
  `274/300..307` to `RowPresentationText`, with no-op rows `235/236` using
  `FlavorRowPresentationText`.
- 2026-05-06: EF EBATTLE1 action-tail exact-message follow-up promoted
  row-backed `MSG_BTL_*` anchors `62/63`, `66..74`, `77`, `88/89`, and
  `91..94` to `RowPresentationText`. EGOODS2 item-use payloads stay out of
  battle-action anchor naming.
- 2026-05-06: EF EGOODS2 item-use guardrail follow-up removed the last
  inherited battle-message shells by renaming `EF:9EF4`, `EF:A0DC`, and `EF:A2AB`
  as `ItemUsePayloadText` anchors for Exit Mouse, Hieroglyph, and Town Map.

## Key C1 entrypoints (contracts that drive C2 naming)

Primary family writeup: `notes/battle-text-entry-family-c1dc1c-dd7c.md`, `notes/battle-text-entry-tail-dd82-dd9f.md`.

### Direct-page argument-slot mapping (why C2 stages `$0E/$10` and `$12/$14`)

These battle-text wrappers all use the generated prologue pattern:

- `phd ; tdc ; adc #$FFEE ; tcd`

That means their “argument” direct-page slots alias the **caller’s** frame:

- callee `$20/$22` == caller `$0E/$10` (because `0x20 - 0x12 = 0x0E`)
- callee `$24/$26` == caller `$12/$14` (because `0x24 - 0x12 = 0x12`)

**C2 naming implication:** `$0E/$10` and `$12/$14` are not random scratch here; they are *battle-text argument staging* for `DC1C` / `DC66` / `DD9F`.

### `C1:DC1C` — `DisplayBattleTextFromPointer`

Best current behavior contract:

- **Input**: far pointer staged by the caller in `$0E/$10` (low word / bank word), which aliases callee `$20/$22` under the DP frame shift
- **Effect**: dispatches the pointed EF text script through the generic textbox processor at `C1:86B1`
- **C2 implication**: any C2 routine that stages `$0E/$10` and `JSL C1:DC1C` is a *battle-text emission site* (not “random string data”); name the routine around the message being selected.

Concrete C2 caller example:

- `C2:4F03` (`src/c2/c2_4f00_display_battle_encounter_text.asm`) loads `enemy_data::encounter_text_ptr` into `$0E/$10` then `JSL C1:DC1C`.

### `C1:DC66` — `DisplayBattleTextWithSubstitutionPayload` (amount-bearing wrapper)

Best current behavior contract (from `notes/battle-text-entry-family-c1dc1c-dd7c.md`):

- **Inputs**: two caller-provided far arguments
  - **primary script pointer** staged by the caller in `$0E/$10` (aliases callee `$20/$22`)
  - **secondary payload** staged by the caller in `$12/$14` (aliases callee `$24/$26`), then committed via `C1:AD0A -> $9D12/$9D14`
    - often consumed as an **amount-like payload** by `PRINT_ACTION_AMOUNT` (`0x1C 0x0F`) via `C1:AD26`
    - sometimes consumed as a **pointer substitution payload** by `LOAD_POINTER_SUBSTITUTION` (`0x19 0x1E`) via `C1:7AE3`
- **Why it matters**: the *secondary payload* is later consumed by `PRINT_ACTION_AMOUNT` (`0x1C 0x0F`) via the getter path (`C1:AD26`).
- **C2 implication**: when C2 uses `DC66`, it is **promising** that the chosen EF script will read `PRINT_ACTION_AMOUNT` (or another `$9D12/$9D14` consumer). Name the C2 routine around “apply delta + print amount-bearing battle text”, not around a generic “display string”.

Concrete C2 caller examples:

- `C2:7294` (`src/c2/c2_7294_apply_battler_hp_recovery_feedback.asm`): success path chooses `EF:69BA`, stages `{delta}` as the secondary payload, then `JSL C1:DC66`.
- `C2:7318` (`src/c2/c2_7318_apply_battler_pp_recovery_feedback.asm`): chooses `EF:69D2`, stages `{delta}`, then `JSL C1:DC66`.
- Late action-table numeric effects (`notes/class2-late-stat-and-resource-family-c28e42-c29e38.md`) repeatedly “mutate stat/resource → print `{delta}` via `DC66`”.

### `C1:DD9F` — `DisplayCurrentActionTableTextMode1` (mode-1 wrapper)

Best current behavior contract (from `notes/battle-text-entry-tail-dd82-dd9f.md`):

- **Input**: far pointer staged by the caller in `$0E/$10` (aliases callee `$20/$22`), then it forces display mode `1` via `JSR $0036`, stages pointer to `$0E/$10`, and dispatches via `C1:86B1`.
- **Caller contract**: pinned local caller `C2:5C66` displays a `D5:7B68`-selected action-table message through `DD9F`, then the caller owns the wait/tick loop itself (consistent with the “NO_PROMPT” export mapping).
- **C2 implication**: treat `DD9F` as a specialized “battle action-table text, mode=1” emission path (don’t collapse it into the general `DC1C` naming without evidence).

#### Unique C2 caller (`C2:5C66`) with concrete selection formula

ROM scan for `JSL $C1DD9F` bytes (`22 9F DD C1`) yields exactly one callsite in bank `C2`: `C2:5C66`.

Decoded snippet (`tools/decode_snippet.py C2:5BE8`, trimmed to the selection core):

- loads base long pointer `D5:7B68` into `$0A/$0C`
- reads an action-table index byte from `($A970 + 0x0004)`
- computes `offset = 0x0C * index + 0x0004`
- loads a far pointer at `D5:7B68 + offset + {0,2}` and stages it to `$0E/$10`
- `JSL C1:DD9F`

So the contract is:

- `D5:7B68` is an action-table message table with stride `0x0C`
- the script far pointer field lives at `+0x04` inside each `0x0C` record
- `DD9F` is the “action-table row message, forced mode=1” lane (caller owns the followup tick/wait loop)

This corridor also conditionally emits two hardcoded EF scripts via `DC1C` before selecting the action-table row script:

- `EF:845D` (user-name message: “@… acted unusual.”)
- `EF:8477` (user-name message: “@… felt funky.”)

Action-island handoff: `notes/ef-battle-text-action-island-consumer-frontier.md`
keeps the row `+4` message pointer lane distinct from row `+8` behavior
payloads and from the direct-result `DC1C` scripts emitted by those behavior
bodies.

## Substitution-slot contracts that appear inside EF battle scripts

These are the *script-level* contracts C2 is implicitly relying on when it chooses particular EF pointers.

### Byte substitution: `$9D11` ↔ `0x19 0x1F` (`LOAD_BYTE_SUBSTITUTION`)

Pinned by `notes/class2-c1acf8-substitution-byte-family.md` and `notes/class2-c1-display-text-substitution-handler-7af3.md`:

- `C1:ACF8` stores low 8 bits of `A` to `$9D11` (setter)
- `C1:DD7C` is the far-call wrapper for `C1:ACF8`
- `C1:AD02` reads `$9D11` (getter)
- `C1:7AF3` loads `$9D11` and stages it into the display-text pipeline
- Text control code `0x19 0x1F` dispatches to `C1:7AF3` and is named `LOAD_BYTE_SUBSTITUTION` in `tools/disasm_ebtext_script.py`

**Concrete C2 caller bridge (present/UFO path):**

- `C2:6003` and `C2:8881` (see `notes/class2-ufo-present-message-family.md`) load `$AA10`, call `JSL C1:DD7C`, then dispatch EF scripts (`EF:7BDF`, `EF:7DD5`) through `C1:DC1C`.

EF script evidence (decoded from ROM with `tools/disasm_ebtext_script.py`):

- `EF:7BDF` (`EBATTLE8` `MSG_BTL_PRESENT`) contains:
  - `LOAD_BYTE_SUBSTITUTION` (`19 1F`)
  - `SWAP_WORKING_AND_ARG_MEMORY` (`1B 04`)
  - `PRINT_ITEM_NAME 0x00` (`1C 05 00`)
- `EF:7DD5` (`EBATTLE8` `MSG_BTL_CHECK_PRESENT_GET`) contains:
  - `01 70 1C 0D` = `START_NEW_LINE`, `"@"`, `PRINT_ACTION_USER_NAME`
  - later: `LOAD_BYTE_SUBSTITUTION` (`19 1F`) → `PRINT_ITEM_NAME 0x00`

**C2 promotion guidance:** if a C2 corridor does `JSL C1:DD7C` immediately before `JSL C1:DC1C`, it’s not “mystery pre-text state”; it is **script-argument staging** for an EF message that is about to execute `LOAD_BYTE_SUBSTITUTION`.

### Pointer substitution: `$9D12/$9D14` ↔ `0x19 0x1E` (`LOAD_POINTER_SUBSTITUTION`)

Pinned by `notes/text-command-family-19-data-and-substitution.md` plus the source-backed leaves:

- `C1:AD0A` (`src/c1/c1_ad0a_stage_battle_text_substitution_pointer.asm`) commits a caller-provided payload into `$9D12/$9D14`
- `C1:7AE3` (`src/c1/c1_7ae3_load_display_text_pointer_substitution_slot.asm`) is the display-side loader used by text command `0x19 0x1E`

Concrete script evidence (exact parsed hits via `tools/find_ebtext_command.py 19 1E`):

- `EF:7B85`, `EF:7BA2`, `EF:7BC1` (all in `EBATTLE8`)

These occur in the same decoded script region as the present/UFO byte-substitution examples (see `tools/disasm_ebtext_script.py EF:7B70`):

- `EF:7B77` uses `LOAD_BYTE_SUBSTITUTION` (`19 1F`) and prints a PSI name
  through a `ByteSubstitutionPayloadText` anchor.
- `EF:7B85` / `EF:7BA2` / `EF:7BC1` use `LOAD_POINTER_SUBSTITUTION` (`19 1E`) and branch on active-memory values
  - source labels keep the lane first:
    `PointerSubstitutionSweetBranch`, `PointerSubstitutionTearsBranch`, and
    `PointerSubstitutionOhBabyBranch`
  - `EF:7B83`, `EF:7BA0`, and `EF:7BBF` are the adjacent two-byte branch-state
    separators, so they should not be treated as the parsed `19 1E` sites.

**C2 promotion guidance:** a `DC66` caller is not always “display-with-number.” If the displayed script consumes `19 1E` rather than `1C 0F`, name the C2 corridor around “stage pointer-substitution payload, then display battle script.”

### Amount substitution: `$9D12/$9D14` ↔ `0x1C 0x0F` (`PRINT_ACTION_AMOUNT`)

Pinned in `notes/battle-text-entry-family-c1dc1c-dd7c.md` and summarized in `notes/text-command-family-1c-print-display.md`:

- `PRINT_ACTION_AMOUNT` is control code `1C 0F`
- Its getter side routes through `C1:AD26`, which reloads the staged `$9D12/$9D14` payload
- `C1:DC66` is the high-value wrapper that *commits* that payload before displaying the EF script

**C2 promotion guidance:** when C2 prints `EF:*` scripts that contain `PRINT_ACTION_AMOUNT`, prefer naming the C2 routine around “compute delta + stage + emit amount-bearing battle text” and keep the staged value type explicit (`delta_hp`, `delta_pp`, `delta_offense`, etc.).

## EF battle scripts used as amount/status-result text (concrete addresses + opcode bytes)

These were decoded directly from the local ROM with `tools/disasm_ebtext_script.py` and corroborated with `refs/ebsrc-main/ebsrc-main/earthbound.yml` text-bank bases.

### `EBATTLE5` (base `EF:69A1`, `refs/ebsrc` offset `0x2F69A1`)

These are core “amount/status result” scripts used by C2 feedback helpers.

- `EF:69A1` (“HP maxed out”)
  - starts `01 70 1C 0E` = `START_NEW_LINE`, `"@"`, `PRINT_ACTION_TARGET_NAME`
  - ends with `PLAY_SOUND 0x24` (`1F 02 24`) and `HALT_WITH_PROMPT` (`03`)
- `EF:69BA` (“recovered {delta} HP!”)
  - `01 70 1C 0E` … then `PRINT_ACTION_AMOUNT` (`1C 0F`) … `" HP!"`
  - ends with `PLAY_SOUND 0x24` and `HALT_WITH_PROMPT`
  - **C2 caller**: `C2:7294` (`src/c2/c2_7294_apply_battler_hp_recovery_feedback.asm`) uses `DC66` here.
- `EF:69D2` (“recovered {delta} PP!”)
  - same structure as `EF:69BA`, but prints `" PP!"`
  - **C2 caller**: `C2:7318` (`src/c2/c2_7318_apply_battler_pp_recovery_feedback.asm`) uses `DC66` here.

- `EF:6AE0` (paralysis/body-numb inflicted message)
  - starts `01 70 1C 0E` = `START_NEW_LINE`, `"@"`, `PRINT_ACTION_TARGET_NAME`
  - **C2 caller**: `C2:9FFE` (in `src/c2/c2_9f57_run_asleep_status_wrapper_action.asm`, `RunResistCheckedParalysisStatusAction`) chooses `EF:6AE0` vs `EF:766E`.
- `EF:6C55` (asleep inflicted message)
  - starts `01 70 1C 0E` = `START_NEW_LINE`, `"@"`, `PRINT_ACTION_TARGET_NAME`
  - **C2 caller**: `C2:9F06` (`src/c2/c2_9f06_run_resist_checked_asleep_status_action.asm`) chooses `EF:6C55` vs `EF:766E`.
- `EF:6C3A` (feel strange inflicted message)
  - starts `01 70 1C 0E` = `START_NEW_LINE`, `"@"`, `PRINT_ACTION_TARGET_NAME`
  - **C2 caller**: `C2:A056` (`src/c2/c2_a056_run_resist_checked_strange_status_action.asm`) chooses `EF:6C3A` vs `EF:766E`.

- shield/timed substate messages (paired strengthened/installed scripts)
  - **C2 caller**: `src/c2/c2_9cb8_try_recover_selected_battler_hard_state.asm` dispatches:
    - `EF:6FBD` vs `EF:6F9A` (substate 4: shield strengthened/installed)
    - `EF:6FF4` vs `EF:6FD3` (substate 3: power shield strengthened/installed)
    - `EF:7032` vs `EF:700C` (substate 2: psychic shield strengthened/installed)
    - `EF:707A` vs `EF:7050` (substate 1: psychic power shield strengthened/installed)
  - **C2 timed-substate blocker**: `src/c2/c2_941d_check_selected_battler_timed_substate_blocker.asm`
    emits `EF:70D2` for psychic power shield PSI-name `ByteSubstitution`
    reflection, `EF:70FA` for psychic shield PSI-name `ByteSubstitution`
    nullification, and `EF:7099` when the timed shield expires.
  - **C2 Thunder reflection tail**: `src/c2/c2_97a5_handle_psi_thunder_franklin_badge_reflection.asm`
    emits `EF:7160` when the Franklin Badge reflects Thunder.

### `EBATTLE6` (base `EF:7186`, `refs/ebsrc` offset `0x2F7186`)

- `EF:7696` (“It had no visible effect on {target}!”)
  - starts with `START_NEW_LINE` and prints `PRINT_ACTION_TARGET_NAME` (`1C 0E`)
  - **C2 caller**: `C2:7294` uses `DC1C` to emit this on a blocked-row path.

- `EF:766E` (shared resist/no-effect “didn’t work” message)
  - contains `PRINT_ACTION_TARGET_NAME` (`1C 0E`) and ends with `... 51 03 02`
  - **C2 callers**: `C2:9F06` (asleep), `C2:9FFE` (paralysis), `C2:A056` (strange) all fall back to `EF:766E` via `DC1C`.

### `EBATTLE8` (base `EF:77FD`, `refs/ebsrc` offset `0x2F77FD`)

From `refs/ebsrc-main/ebsrc-main/earthbound.yml`:

- `0x03E2` = `MSG_BTL_PRESENT` → `EF:7BDF`
- `0x05D8` = `MSG_BTL_CHECK_PRESENT_GET` → `EF:7DD5`

These are the canonical “byte substitution” examples:

- `EF:7BDF` uses `LOAD_BYTE_SUBSTITUTION` (`19 1F`) → `PRINT_ITEM_NAME 0`
- `EF:7DD5` uses `PRINT_ACTION_USER_NAME` (`1C 0D`) and later the same `LOAD_BYTE_SUBSTITUTION` → `PRINT_ITEM_NAME 0`

- `EF:773F` (PP drain amount message)
  - contains `PRINT_ACTION_AMOUNT` (`1C 0F`)
  - **C2 caller**: `C2:9F5E` (in `src/c2/c2_9f57_run_asleep_status_wrapper_action.asm`, `RunHpSuckerStylePpDrainAction`) stages `{delta_pp}` and uses `DC66`.

### `EBATTLE0` (base `EF:843F`, `refs/ebsrc` offset `0x2F843F`)

Battle-start status-message cluster used by the `C2:4F62+` path (`notes/class2-concrete-battle-text-call-paths.md`):

- `EF:8445` begins:
  - `01 70 1C 0E` = `START_NEW_LINE`, `"@"`, `PRINT_ACTION_TARGET_NAME`
  - then compressed tokens + punctuation + `HALT_WITH_PROMPT` (`03`)

These are staged as hardcoded EF pointers immediately after `C2:3D05` (target-side context build) and dispatched through `C1:DC1C`.

## Concrete C2 caller examples that should drive promotions/names

These are “good promotion candidates” because the call sites encode real contracts (pointer selection + substitution staging + EF opcode expectations).

### Encounter/death pointer emission (`DC1C` pointer contract)

- `C2:4F03` (`src/c2/c2_4f00_display_battle_encounter_text.asm`)
  - loads `enemy_data::encounter_text_ptr` (`D5:9589 + 0x2D`) into `$0E/$10`
  - `JSL C1:DC1C`
- `C2:7680+` (`src/c2/c2_7680_display_enemy_death_text.asm`)
  - loads `enemy_data::death_text_ptr` (`D5:9589 + 0x31`) into `$0E/$10`
  - `JSL C1:DC1C`

Promotion effect: name these callers as “select enemy record pointer + emit battle text”, not “unknown message handler”.

### HP/PP recovery feedback (paired `DC1C` + `DC66` contract)

- `C2:7294` (`src/c2/c2_7294_apply_battler_hp_recovery_feedback.asm`)
  - chooses among `EF:69A1` (HP already maxed recovery text), `EF:69BA`
    (HP recovered amount-bearing text), `EF:7696` (no visible effect)
  - uses `DC66` only on the path where the EF script prints `PRINT_ACTION_AMOUNT` (`1C 0F`)
- `C2:7318` (`src/c2/c2_7318_apply_battler_pp_recovery_feedback.asm`)
  - emits `EF:69D2` via `DC66` (PP recovered amount-bearing text)

Promotion effect: keep the “amount-bearing EF script requires staged delta” invariant explicit in naming and parameter shaping.

### Start-of-battle status messages (context → emit)

From `notes/class2-concrete-battle-text-call-paths.md`:

- `C2:4F62+` first calls `C2:3D05` (target text context) then emits hardcoded EF pointers (`EF:843F`, `EF:8444`, `EF:8445`) through `DC1C`.

Promotion effect: this should become a clear “battle-start status announcement” routine, not a generic “emit message list”.

Source-scaffold status:

- `C2:4F52..5024` is decoded source in `src/c2/c2_4f52_display_battle_start_status_messages_prelude.asm`.
- `C2:5024..6189` is now decoded source split across `src/c2/c2_5024_run_battle_start_candidate_controller_front.asm` and `src/c2/c2_5afb_run_battle_start_candidate_controller_back.asm`, with the heavier `5540` controller joins forced at the source-module boundaries and known post-call width joins.

### Present/UFO byte-substitution bridge (`DD7C` → `DC1C` → `19 1F`)

From `notes/class2-ufo-present-message-family.md`:

- `C2:4A8A` and `C2:6189` populate `$AA10` from either the D5 enemy dropped
  item byte (`+0x58`) after the D5 drop-rate gate (`+0x57`), or the
  UFO-specific fallback records at `C2:3109`.
- `C2:6003` and `C2:8881`:
  - `$AA10` / local `BattlePresentItemByte` → `JSL C1:DD7C` (sets `$9D11`)
  - then `JSL C1:DC1C` on `EF:7BDF` / `EF:7DD5`
  - those scripts execute `LOAD_BYTE_SUBSTITUTION` (`19 1F`) before `PRINT_ITEM_NAME 0`

Promotion effect: model `$AA10` as “byte substitution argument” for a specific EF script family; don’t let this degenerate into “mystery battle-start flag”.

### Resist-checked affliction actions (paired EF success/fail scripts via `DC1C`)

- `C2:9F06` (`src/c2/c2_9f06_run_resist_checked_asleep_status_action.asm`) chooses `EF:6C55` (success) vs `EF:766E` (no effect)
- `C2:9FFE` (in `src/c2/c2_9f57_run_asleep_status_wrapper_action.asm`, `RunResistCheckedParalysisStatusAction`) chooses `EF:6AE0` vs `EF:766E`
- `C2:A056` (`src/c2/c2_a056_run_resist_checked_strange_status_action.asm`) chooses `EF:6C3A` vs `EF:766E`

Promotion effect: these corridors are stable “status result” emitters; promote with status-specific names rather than generic “display text”.

### PP drain amount text (`DC66` + `PRINT_ACTION_AMOUNT`)

- `C2:9F5E` (in `src/c2/c2_9f57_run_asleep_status_wrapper_action.asm`, `RunHpSuckerStylePpDrainAction`) stages `{delta_pp}` and uses `DC66` with `EF:773F` (script contains `1C 0F`)

Promotion effect: keep the staged value type explicit (delta PP) and preserve the invariant “`DC66` only on `1C 0F` scripts”.

### Shield/timed substate message pairs (EF scripts via `DC1C`)

- `src/c2/c2_9cb8_try_recover_selected_battler_hard_state.asm` dispatches paired strengthened/installed scripts:
  - `EF:6FBD` vs `EF:6F9A` = shield, row `+0x23 == 4`
  - `EF:6FF4` vs `EF:6FD3` = power shield, row `+0x23 == 3`
  - `EF:7032` vs `EF:700C` = psychic shield, row `+0x23 == 2`
  - `EF:707A` vs `EF:7050` = psychic power shield, row `+0x23 == 1`
- `src/c2/c2_941d_check_selected_battler_timed_substate_blocker.asm` and
  `src/c2/c2_94ce_tick_selected_battler_timed_substate_cleanup.asm` now keep
  the shield-expiry and PSI-name reflection/nullify EF pointers local:
  `EF:70D2`, `EF:70FA`, and `EF:7099`.
  The blocker source now also names the `D5:7B68` action type byte and gates
  this branch to PSI-type action descriptors before consulting target-row
  timed-substate bytes.
- `src/c2/c2_97a5_handle_psi_thunder_franklin_badge_reflection.asm` names the
  adjacent Franklin Badge reflection script at `EF:7160`.

Promotion effect: promote as an internally consistent shield/timed-substate
family where each row `+0x23` id has a concrete result-text pair and the shared
PSI blocker owns the reflective/nullifying text tail.

Implementation status: the gameplay names of the timed shield indices are now
known from the EF payload split, so follow-up promotions should keep the row-id
mapping local to the shield/timed-substate family.

## Naming proposals (workahead)

These are the “contracts-first” names that should influence C2 source promotion and call-site signatures:

- `C1:DC1C` → `DisplayBattleTextFromPointer` (consume `$0E/$10` far ptr)
- `C1:DC66` → `DisplayBattleTextWithSubstitutionPayload` (commit `$9D12/$9D14` then display EF script)
  - acceptable narrower alias when used with `1C 0F`: `DisplayBattleTextWithActionAmount`
- `C1:DD9F` → `DisplayCurrentActionTableTextMode1` (action-table message, mode `1`)
- `C1:DD7C` / `C1:ACF8` → `SetBattleTextByteSubstitution` (set `$9D11`)

EF payload anchor suffixes should mirror those wrapper contracts:

- `ActionAmount`: EF script consumes the `C1:DC66` secondary payload through
  `PRINT_ACTION_AMOUNT (1C 0F)`.
- `ByteSubstitutionPayloadText`: EF script consumes the `C1:DD7C` byte slot
  through `LOAD_BYTE_SUBSTITUTION (19 1F)`.
  High-confidence EF consumers now include present item text `EF:7BDF/7DD5`,
  learned/shared PSI text `EF:7B77/8543`, and shield PSI-name scripts
  `EF:70D2/70FA`.
- `PointerSubstitution`: EF script consumes the staged pointer payload through
  `LOAD_POINTER_SUBSTITUTION (19 1E)`.
  Current EF branch consumers are `EF:7B85/7BA2/7BC1`; the nearby
  `EF:7B83/7BA0/7BBF` state anchors only delimit that branch island.

And for the most actionable C2 call-site families:

- `C2:3BCF` → `BuildBattleAttackerTextContext` (ends at `C1:DD70`)
- `C2:3D05` → `BuildBattleTargetTextContext` (ends at `C1:DD76`)
- `C2:4F03` → `DisplayBattleEncounterText` (enemy record pointer → `DC1C`)
- `C2:4F62+` → `DisplayBattleStartStatusMessages` (target context → hardcoded EF pointers)
- `C2:7294` → `ApplyBattlerHpRecoveryFeedback` (chooses maxed/amount/no-effect scripts, uses `DC66` iff `1C 0F`)
- `C2:7318` → `ApplyBattlerPpRecoveryFeedback` (amount-bearing `DC66` path)

## Implemented Promotion Notes

- 2026-05-01: `src/c2/c2_7eaf_run_hit_resolution_and_status_action_cluster.asm`
  now names the `DC1C`/`DC66`/`DD7C` dispatch contracts used by the
  hit-resolution cluster, the EF damage/miss/dodge/SMAAAASH/Spy scripts, the
  `EF:7843` Time Stop return script, and the late
  diamondize/paralyze/nausea/poison/cold status-result scripts. See
  `notes/c2-hit-resolution-status-runtime-polish.md`.
- 2026-05-01: follow-up shield-tail polish aligned `C2:7EAF` and `C2:A3D1`
  with the EF payload split: `EF:70B1` is now named as power-shield physical
  reflection text and `EF:7099` as the shared shield-expired text used by
  timed cleanup and item-side shield clearing.
- 2026-05-01: the same follow-up corrected remaining `C1:DD7C` caller wording
  in `C2:92EE` and `C2:941D`; those calls stage the C1 byte-substitution slot
  rather than running a separate presentation command.
- 2026-05-05: `src/c2/c2_941d_check_selected_battler_timed_substate_blocker.asm`
  now names the selected-row action argument byte staged through `C1:DD7C`,
  the action-table type-byte read, the PSI action type gate, and the
  `$AA94/$AA96` transient flags used by PSI shield reflection/nullification.
- 2026-05-01: `src/c2/c2_5024_run_battle_start_candidate_controller_front.asm`,
  `src/c2/c2_5afb_run_battle_start_candidate_controller_back.asm`, and
  `src/c2/c2_6189_fill_instant_win_tile_buffer_and_upload.asm` now name the
  battle-start/instant-win `DC1C`/`DC66`/`DD7C` payload joins and the EF/C8
  scripts they stage. See
  `notes/c2-battle-start-payload-join-runtime-polish.md`.
- 2026-05-01: `src/c2/c2_bd13_sum_active_enemy_battle_sprite_widths.asm`,
  `src/c2/c2_bd5e_call_for_help_enemy_selection_and_message_body.asm`, and
  `src/c2/c2_be6c_run_call_for_help_enemy_selection_body.asm` now name the
  call-for-help `DC1C` text exits and their four EF outcome scripts. See
  `notes/c2-call-for-help-runtime-polish.md`.
- 2026-05-01: `src/c2/c2_c14e_run_rainbow_colors_special_event.asm`,
  `src/c2/c2_c37a_run_final_prayer_stage_transition.asm`,
  `src/c2/c2_c41f_run_final_prayer_narrative_transition.asm`,
  `src/c2/c2_c572_run_final_prayer_opening_transition.asm`, and
  `src/c2/c2_c6f0_run_final_prayer_finale_opening_sequence.asm` now name the
  Rainbow Colors / Final Prayer `DC1C` text exits and their C8/C9 script
  constants. See `notes/class2-special-event-results-c29298-c2c14e.md` and
  `notes/c2-final-prayer-runtime-polish.md`.
- 2026-05-01: `src/c2/c2_4a80_populate_candidate_pool_from_variable_sources.asm`
  now names the dropped-item/drop-rate offsets and UFO fallback table that
  populate `BattlePresentItemByte`; `src/c2/c2_5afb_run_battle_start_candidate_controller_back.asm`,
  `src/c2/c2_6189_fill_instant_win_tile_buffer_and_upload.asm`, and
  `src/c2/c2_7eaf_run_hit_resolution_and_status_action_cluster.asm` now share
  that local byte-slot name at the `EF:7BDF` and `EF:7DD5` consumers. See
  `notes/c2-battle-start-payload-join-runtime-polish.md` and
  `notes/c2-hit-resolution-status-runtime-polish.md`.
- 2026-05-05: EF present-result follow-up split the `EF:7C42..7DD5`
  continuation behind `MSG_BTL_PRESENT` into inventory-full, abandon/drop, and
  forbidden-drop text anchors. The C2 side still treats `$AA10` as
  `BattlePresentItemByte`; EF now exposes the downstream result branches that
  run after `EF:7BDF` consumes that byte through `19 1F`.
- 2026-05-06: EF present-item naming follow-up removed inherited `MsgBtl`
  prose from the `EF:7BDF` and `EF:7DD5` item `ByteSubstitutionPayloadText`
  anchors,
  and split the `EF:7C42..7DBE` continuation labels into present result versus
  prompt text roles. No C1/C2 source was edited in this pass.
- 2026-05-06: EF byte-substitution payload suffix follow-up renamed the bare
  `EF:7B77`, `EF:7BDF`, and `EF:7DD5` consumers as
  `ByteSubstitutionPayloadText`, separating staged DD7C payload scripts from
  row-presentation and direct-result substitution anchors.
- 2026-05-01: `src/c2/c2_7eaf_run_hit_resolution_and_status_action_cluster.asm`
  now names the Spy readout target battler offsets for offense, defense, fire/
  freeze/flash/paralysis resistance, hypnosis resistance, brainshock
  resistance, and the `0xFF` fully-vulnerable sentinel. See
  `notes/c2-hit-resolution-status-runtime-polish.md`.
- 2026-05-05: follow-up action-table text polish aligned
  `src/c2/c2_5024_run_battle_start_candidate_controller_front.asm`,
  `src/c2/c2_5afb_run_battle_start_candidate_controller_back.asm`, and
  `src/c2/c2_77ca_run_class2_late_selected_row_controller.asm` on the
  `D5:7B68` row vocabulary: `0x0C`-byte rows, row `+2` action-type branches,
  row `+3` PP cost, row `+4` primary `C1:DD9F` text, and row `+8` companion
  payload pointer.

## Integration checklist (manual)

When promoting additional C2 corridors that call into the battle-text cluster:

1. If you see `JSL C1:DC1C`, confirm the caller staged `$0E/$10` (far ptr contract) and annotate the chosen EF pointer(s).
2. If you see `JSL C1:DC66`, verify the EF script(s) contain `PRINT_ACTION_AMOUNT` (`1C 0F`) or another `$9D12/$9D14` consumer; name the staged value accordingly.
3. If you see `JSL C1:DD7C` shortly before a `DC1C` dispatch, decode the EF script and look for `LOAD_BYTE_SUBSTITUTION` (`19 1F`) + downstream printers (`PRINT_ITEM_NAME`, `PRINT_PSI_NAME`, etc.).
4. Treat `DD9F` call sites as a distinct lane (mode forcing + “no prompt” behavior); don’t collapse into the main `DC1C` wrapper without evidence.
