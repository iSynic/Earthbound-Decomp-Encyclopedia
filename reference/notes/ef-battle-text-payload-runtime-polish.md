# EF Battle Text Payload Runtime Polish

This note records the first EF text-payload split driven by the C1/C2
battle-text contract work.

## Source Slice

Primary source module:

- `src/ef/ef_4e20_c51b_text_payload_data.asm`

Action-island follow-up:

- `notes/ef-battle-text-consumer-lane-contracts.md`
- `notes/ef-battle-text-action-island-consumer-frontier.md`
- `notes/ef-battle-text-row-message-crosswalk.md`
- `notes/ef-battle-text-row-pointer-recovery-frontier.md`

The module is still ROM-preserved text data, not decoded text macro source. The
new labels are zero-byte scaffold anchors that split the coarse
`EF:4E20..C51B` data gap around battle-text scripts already proved by C1/C2
callers.

## Payload Naming Contract

The EF source comments now separate the three battle-text payload lanes that
C1/C2 callers depend on:

- `ActionAmount` anchors are EF scripts that consume a staged `$9D12/$9D14`
  amount payload through `PRINT_ACTION_AMOUNT (1C 0F)`. C2 action/result paths
  usually stage that payload through `C1:DC66 -> C1:AD0A`; C1 level-up
  narration stages the same slot through `C1:AD0A` before dispatching its fixed
  EF scripts. Callers should keep the staged value type explicit, such as delta
  HP, delta PP, offense, defense, drained HP, drained PP, or stat gain.
- `ByteSubstitutionPayloadText` anchors are EF scripts that consume the
  `C1:DD7C` byte slot through `LOAD_BYTE_SUBSTITUTION (19 1F)`, including
  learned-PSI and Present/Check Present item-name text.
- `PointerSubstitution` anchors are EF branches that consume the staged pointer
  payload through `LOAD_POINTER_SUBSTITUTION (19 1E)`.

These are label/comment-only source anchors over ROM-preserved EB text
bytecode. They do not change payload bytes or convert the scripts to text
macros.

## Promoted Payload Anchors

- `EF:4E20..69A1` now splits the front text-payload corridor into the
  `EEXPLPSI` PSI explanation scripts, the `E16DKFD` Dungeon Man/Deep Darkness
  payloads, and the `E07GPFT` Grapefruit Falls/Threed payloads before EBATTLE5.
- `EF:69A1`, `EF:69BA`, and `EF:69D2` now mark HP already-maxed recovery
  text, HP recovered `ActionAmount`, and PP recovered `ActionAmount`. The two
  `ActionAmount` scripts are consumed through
  `C1:DC66 -> C1:AD0A -> $9D12/$9D14 -> 1C 0F`.
- `EF:69EA` and `EF:69FF` now mark the Spy offense and defense amount
  readouts. Both scripts are `ActionAmount` consumers reached through the C2
  Spy setup and the `C1:DC66` amount-print contract.
- `EF:6A0D`, `EF:6A24`, `EF:6A3C`, `EF:6A54`, `EF:6A6C`, and `EF:6A7F`
  now mark the Spy vulnerability/susceptibility direct readout text for fire,
  freeze, flash, paralysis, hypnosis, and Brain Shock. C2 gates these direct
  scripts from battler resistance bytes before issuing the `DC1C` display call.
- `EF:6A99` and `EF:6AB3` now mark metamorphose success/failure text used by
  the C2 normalization tail, now as `ResultText` anchors. `EF:6AC7` now marks
  the diamondized `StatusResultText` adjacent to the existing
  paralysis/status payload split.
- `EF:6AE0`, `EF:6B18`, `EF:6BEF`, `EF:6C3A`, and `EF:6C55` now mark
  paralysis, poison, solidification, strange, and asleep `StatusResultText`
  anchors. The EF decode shows `EF:6AE0` as the body-numb message
  used by `BTLACT_PARALYSIS_A`, while actual poison remains the separate
  `EF:6B18` script used by the item/status cluster.
- `EF:6AFB..6C0B` is now split around the adjacent sick/cold/mushroomized,
  possessed, crying, immobilized, solidification, and PSI-seal
  `StatusResultText` payloads instead of one broad affliction corridor.
- `EF:6C6B..6E31` now splits the post-status EBATTLE5 death-result corridor:
  player collapse, Flying Man/teddy-bear NPC death payloads, and enemy defeat
  flavor text now have source anchors instead of one anonymous status tail. The
  source labels now name player incapacitated/collapse, Flying Man/teddy-bear
  death, and enemy defeat variants without inherited `MsgBtl`/`MsgSys` shells.
- `EF:6E4A`, `EF:6E67`, `EF:6E81`, `EF:6E97`, `EF:6EBC`, `EF:6ED1`,
  `EF:6EED`, `EF:6F0B`, `EF:6F1E`, `EF:6F38`, `EF:6F54`, and `EF:6F64`
  now mark the EBATTLE5 `RecoveryResultText`/`RemovalResultText` scripts for
  diamondized, paralysis, nausea, poison, cold, crying, immobilized, frozen,
  strange, sunstroke, asleep, and PSI-seal states. These line up with the C2
  affliction-recovery helper families.
- `EF:6F7C` and `EF:6F8E` now mark revive success/failure `ResultText`
  immediately before the shield-result block.
- `EF:6F9A/6FBD`, `EF:6FD3/6FF4`, `EF:700C/7032`, and `EF:7050/707A`
  now mark the installed/strengthened `ResultText` pairs for shield, power
  shield, psychic shield, and psychic power shield.
- `EF:7099`, `EF:70B1`, `EF:70D2`, `EF:70FA`, `EF:7123`, `EF:7142`, and
  `EF:7160` now mark the shield-expired, shield-reflection, PSI-name
  shield `ByteSubstitutionResultText`, Neutralizer result, and Franklin Badge
  result tail used by C2 timed substate and Thunder reflection helpers.
- `EF:7186..7249` now splits EBATTLE4 action-blocking status text for
  diamondized, paralysis, nausea, poison, asleep, immobilized, and PSI-seal
  turns, with `ActionBlockedStatusText` anchors in source. The PSI-seal
  player-side branch leads to a `ByteSubstitutionResultText` script at
  `EF:7221`, which consumes the PSI-name byte through `19 1F`.
- `EF:7249..75AB` now splits EBATTLE4 guard, Fly Honey, homesickness,
  Runaway Five, Poo/Starstorm, Pokey random-talk, and companion event text
  before the central damage block.
- `EF:75AB`, `EF:75C2`, `EF:75D9`, `EF:75F0`, and `EF:7607` now mark the
  `ActionAmount` damage and SMAAAASH damage scripts selected by the C2
  hit-resolution cluster. These consume staged HP damage through `1C 0F`.
- `EF:7624`, `EF:7630`, `EF:763C`, and `EF:7655` now mark the player/monster
  SMAAAASH presentation scripts and shooting/physical dodge scripts used by the
  same C2 hit-resolution lane.
- `EF:766E`, `EF:7696`, and `EF:773F` now mark shared no-effect, no-visible
  effect, and PP-drain amount text. `EF:773F` is another `1C 0F` amount
  consumer.
- `EF:76B3`, `EF:76C7`, `EF:76D8`, `EF:76FD`, `EF:7710`, and `EF:7729`
  now split the adjacent EBATTLE4 no-effect/miss/target-gone/HP-sucker text
  tail. `EF:7729` is an HP-sucker `ActionAmount` consumer.
- `EF:7755`, `EF:7768`, `EF:7787`, `EF:77B1`, and `EF:77DB` now split the
  target-side PP drain and periodic status damage text before EBATTLE8. These
  are now named as `ActionAmount` consumers because their scripts read the
  `C1:DC66` secondary payload through `1C 0F`.
- `EF:77FD`, `EF:7810`, `EF:7824`, and `EF:7830` now mark the four
  call-for-help result scripts selected by the C2 reinforcement prefix/body:
  ordinary success, seed/sprout success, ordinary failure, and seed/sprout
  failure. They are direct `C1:DC1C` text exits and now carry `ResultText`
  suffixes.
- `EF:7843` now marks the Time Stop `ResultText` return used by the C2
  hit-resolution cluster.
- `EF:7858..790B` now splits the EBATTLE8 encounter-opening presentation text
  variants: ordinary attack, blocked-way, came-after-you, trapped-you,
  final-encounter wording, surprise-opening messages, and their group-actor
  helpers.
- `EF:790B..79D7` now splits the group-actor helper branches used by those
  encounter-opening messages.
- `EF:79D7..7A66` now splits ordinary/boss/forced player victory,
  monster-victory, homesick, experience-gain, and level-up announcement text.
- `EF:7A7D..7B64` now splits the level-up stat-gain amount text and the
  learned-PSI lead-in consumed by the C1 level-up narration family. The
  stat-gain anchors are named as `ActionAmount` consumers because C1 stages
  their deltas through `C1:AD0A -> $9D12/$9D14 -> 1C 0F`.
- `EF:7B64` now marks the learned-PSI lead-in that falls through to the
  existing `EF:7B77` PSI-name byte-substitution payload text.
- `EF:7B77`, `EF:7B85`, `EF:7BA2`, `EF:7BC1`, `EF:7BDF`, and `EF:7DD5` now
  mark the byte and pointer substitution examples in `EBATTLE8`: `19 1F` byte
  substitution for PSI/present item names and `19 1E` pointer substitution
  branches.
  The `EF:7B85/7BA2/7BC1` branch labels now keep the lane noun first
  (`PointerSubstitutionSweet/Tears/OhBabyBranch`), while `EF:7B83/7BA0/7BBF`
  remain the small branch-state separators around those consumers.
- `EF:7C42`, `EF:7C73`, `EF:7C89`, `EF:7CB4`, `EF:7CED`, `EF:7CF8`,
  `EF:7D0F`, `EF:7D83`, and `EF:7DBE` now split the `MSG_BTL_PRESENT`
  continuation into present result text, yes/no prompt text, drop-selection
  prompt text, and forbidden-drop result text paths.
- `EF:7E25..843F` now splits EBATTLE2 action-flavor narration into
  symbol-derived `MSG_BTL_*` anchors, covering enemy attack descriptions,
  guard/flavor actions, gases/breath/light/sound effects, and the last
  `MSG_BTL_CHOU_ONPA` payload before EBATTLE0 begins. Proved row-message
  consumers inside this island now carry `RowPresentationText` names for rows
  `99`, `100`, `101`, `102`, `104`, `117`, `118`, and `207`.
- `EF:843F`, `EF:8444`, `EF:8445`, `EF:845D`, and `EF:8477` now mark
  battle-start status announcements and random-action status text used by C2
  direct `DC1C` callers without inherited `MsgAtStart`/`MsgRandomAct` shells.
- `EF:848C..8814` now splits the EBATTLE1 battle-command front into
  Bash/attack and Shoot row presentation, Guard/Metamorphose/flee command
  text, Spy/check row presentation, shared PSI name byte-substitution row
  presentation, and the first PSI animation/effect dispatch branches.
- `EF:8814..89FE` now splits the adjacent EBATTLE1 Thunder/effect/Pray run:
  small and large Thunder presentation scripts, the Thunder miss sound
  presentation script, PSI presentation/effect branches 17-50, and the Pray
  row presentation text at `EF:89E0`.
- `EF:89FE..8FAD` now splits the complete EBATTLE3 enemy-action text include,
  from `MSG_BTL_JIHIBIKI` through `MSG_BTL_GYIYYIG_3`, before the next
  EBATTLE9 include begins. Proved EBATTLE3 row-message consumers now carry
  `RowPresentationText` names for rows `159`, `160`, `161`, `176`, `211..234`,
  `241`, `242`, `248`, `273`, `274`, `290`, and `300..307`, plus
  `FlavorRowPresentationText` for rows `235/236` and `309/313..317`, and the
  shared named-item anchor used by rows `140` and `247`.
- `EF:8FAD..9A47` now splits the complete EBATTLE9 field-monster/graveyard
  include: the party-size helper branch, Sanctuary field-monster payloads,
  Paula/graveyard branches, signpost/boss/girl text, and the Guts tutorial
  system-message branches.
- `EF:9A47..9EF4` now splits the later EBATTLE1 action-tail include into
  row-backed action payload anchors from `MSG_BTL_NAKAMA0` through
  `MSG_BTL_FIRE_BREATH`. The proved action-tail rows now use
  `RowPresentationText` names for rows `62..94` that land in EF, while EGOODS2
  item-use scripts after `EF:9EF4` keep item-use labels.
- `EF:9EF4..A2FA` now splits the EGOODS2 item-use include around the Exit
  Mouse, Hieroglyph, Town Map, and Onett traveler-shack payload branches.
- `EF:A2FA..C51B` now splits the remaining EF text-payload tail into the
  unknown monster-off/Sky Runner event payload, command/status window text
  tables, name-input keyboard layouts, the one-byte `UNKNOWN7` payload, and
  the debug/menu runtime script at `EF:A6EC`.

## Correction

The EF decode corrected one local C2 naming drift: `C2:9FFE` is the
`BTLACT_PARALYSIS_A` body and its success script at `EF:6AE0` prints the
body-numb result text. ebsrc names that path as paralysis
rather than poison. The actual poison-inflicted text remains the separate
`EF:6B18` script used by the item/status cluster.

## Spy Readout Follow-up

The HP/PP recovery front of EBATTLE5 now carries payload-role names before the
Spy readout island begins. `EF:69A1` is the HP-already-maxed recovery text used
when the HP feedback helper has no delta to stage, while `EF:69BA` and
`EF:69D2` are HP/PP recovered `ActionAmount` scripts. That keeps the direct
maxed-out recovery message separate from the `DC66` amount-bearing success
paths.

The C2 Spy refinement proved that the coarse `EF:69EA..6AE0` EBATTLE5 corridor
contains a compact set of distinct scripts, not one generic stat/status
prelude. Offense and defense use the same amount-print path as HP/PP recovery,
while the resistance readouts are direct display scripts selected only when C2
finds a vulnerable/susceptible resistance byte. The metamorphose and diamondized
neighbors were split in the same pass so the late C2 primary-status tail no
longer lands in an anonymous gap.

The source labels now carry the same split directly: `EF:69EA/69FF` are Spy
`ActionAmount` readouts, `EF:6A0D..6A7F` are Spy direct readout text for
vulnerability/susceptibility buckets, and `EF:6A99/6AB3` are metamorphose
success/failure `ResultText` emitted by the normalization tail.

## Call-For-Help And Time Stop Follow-up

The C2 call-for-help polish proved four direct text exits in the front of
`EBATTLE8`: ordinary and seed/sprout success paths at `EF:77FD` and `EF:7810`,
plus ordinary and seed/sprout failure paths at `EF:7824` and `EF:7830`. The
same EBATTLE8 neighborhood also contains the `EF:7843` Time Stop return script
used by the C2 hit-resolution cluster. This split keeps those runtime-facing
messages visible.

Those five anchors now use `ResultText` suffixes in source:
`EF:77FD..7830` for the call-for-help outcomes and `EF:7843` for Time Stop.
That keeps the already-proved `DC1C` exits distinct from the encounter-opening
text that begins at `EF:7858`.

## Encounter, Victory, And Level-Up Follow-up

The `EF:7858..7B77` EBATTLE8 island is now split around exact encounter,
group-actor, victory, and level-up labels. This exposes the encounter-opening
message variants and their `LOAD_SPECIAL 2` group-name helper branches, then
the ordinary/boss/forced victory text and monster-win text. The level-up
announcement starts at `EF:7A66`, while the stat-gain tail at
`EF:7A7D..7B46` lines up directly with the C1 level-up narration note: each
stat leaf stages an amount through `C1:AD0A` before dispatching one of these
`PRINT_ACTION_AMOUNT` scripts. Learned PSI then falls through into the existing
`EF:7B77` PSI-name byte-substitution payload.

The source names now carry that split directly. `EF:7858..78F7` are
`OpeningText` anchors for encounter and surprise presentation variants, while
the `EF:790B..79C6` group-actor helpers stay helper/branch labels rather than
display-lane promotions. `EF:79D7..7A4D` now uses victory/loss narration names,
`EF:7A66` is the level-up announcement, `EF:7A7D..7B46` are C1-staged
`ActionAmount` stat-gain scripts, and `EF:7B64` is the learned-PSI lead-in
before the PSI-name `ByteSubstitution` text at `EF:7B77`.

## Damage And Miss Follow-up

The C2 hit-resolution source names a dense EBATTLE4 result set around
`EF:75AB..77FD`: amount-bearing damage variants, SMAAAASH presentation, dodge,
miss, target-gone, HP/PP drain, and periodic status damage. Splitting those
anchors makes the central damage pipeline visible on the EF side.

The source labels now remove inherited `MsgBtl` shells across that whole
pipeline. `EF:75AB..7607` are damage `ActionAmount` scripts, `EF:7624/7630`
are SMAAAASH presentation text, `EF:763C/7655` are dodge text, `EF:7696..7710`
are no-effect/miss/target-gone/direct HP-sucker text, and `EF:7729..77DB` are
HP/PP drain or periodic damage `ActionAmount` scripts. This keeps staged amount
consumers separate from direct text and presentation-only anchors.

## EBATTLE4 Status And Event Prelude Follow-up

The remaining `EF:7186..75AB` prelude is now split around exact EBATTLE4
labels. The front status run exposes action-blocking result text for
diamondized, paralysis, nausea, poison, sleep, immobilization, and PSI seal.
Those front anchors now use `ActionBlockedStatusText`, while the PSI-seal
player-side branch and `EF:7221` result text keep the byte-substitution payload
visible separately from the blocked-action text.
The event half exposes guard, Fly Honey, homesick flavor, Runaway Five
intervention, Poo/Starstorm, Pokey random talk branches, and companion text
before the damage pipeline begins at `EF:75AB`.

The guard/Fly Honey/homesick front of that event half now drops inherited
`MsgBtl` prose in favor of payload-role anchors: `EF:7249` is guard-on flavor
text, `EF:725A` is Fly Honey mind-loss event text, `EF:727F` is the homesick
random-thought dispatcher, and `EF:72A0..72DB` are the thought-of-mom,
craving-food, and lost-motivation branches. These remain event/flavor anchors,
not row `+4` presentation joins.

The row `243` and `244` special-event split now carries the lane in the source
labels: `EF:72F6` and `EF:7415` are `RowPresentationText` anchors displayed by
`DD9F`, while `EF:72F7`, `EF:733D`, and `EF:743B` are behavior-emitted
`ResultText` continuations.
The crosswalk now uses those source labels too, keeping special-event
presentation text separate from the direct-result continuations.

The random-talk tail is now named by consumer shape rather than inherited
message-symbol prose: `EF:745F` is the Pokey random-talk dispatcher, while
`EF:749D..7548` are its played-dead, pretended-cry, apology,
thought-to-self, innocent-act, sincere-smile, complaint, and edge-closer
branches. The companion tail at `EF:7569..7593` now names My Dog, Pickey,
Tony, and Balmon talk text as adjacent flavor/event anchors. These names do
not claim a row `+4` table join; they keep the source-side text islands
searchable while the C2 caller evidence remains the authority for action/result
lane promotion.

## Recovery And Death Follow-up

The C2 affliction-recovery source and notes repeatedly dispatch into the
`EF:6E4A..6F64` recovery/removal subrange for poison, nausea, crying, strange,
sunstroke, asleep, and PSI-seal cleanup. Splitting the wider `EF:6C6B..6F9A`
island also exposes the adjacent player/NPC/enemy death-result payloads and the
revive success/failure scripts that sit before the shield-result block.

The adjacent death/defeat front now has source names that match its runtime
role: `EF:6C6B` is player incapacitated/collapse text, `EF:6C84..6D4C`
names Flying Man and teddy-bear death payloads while preserving the Flying Man
branch/helper labels, and `EF:6D71..6E31` names enemy defeat flavor variants.
These are death/defeat payload anchors, not row `+4` action presentation
messages.

The source labels now make the cleanup lane explicit: `EF:6E4A..6F64` are
`RecoveryResultText` or `RemovalResultText` anchors, the direct-result mirror of
the earlier `StatusResultText` infliction island. They are C2 cleanup helper
emissions, not row `+4` presentation messages.

The adjacent revive and shield tail now carries the same direct-result contract:
`EF:6F7C/6F8E` are revive `ResultText` scripts, `EF:6F9A..707A` are shield
installed/strengthened `ResultText` pairs, and `EF:7099..7160` covers expiry,
reflection, Neutralizer, and Franklin Badge result scripts. The PSI-name shield
scripts at `EF:70D2/70FA` keep `ByteSubstitution` in the label because they
also consume the `C1:DD7C -> $9D11 -> 19 1F` byte slot.

## Present Result Follow-up

The C2 battle-start and Check Present notes already prove the `$AA10 ->
C1:DD7C -> $9D11 -> 19 1F` byte-substitution bridge into `EF:7BDF` and
`EF:7DD5`. Those source anchors now use present-item and check-present-get
`ByteSubstitutionPayloadText` names without inherited `MsgBtl` prose. Splitting
`EF:7C42..7DD5` exposes the internal present continuation as result and prompt
anchors: recipient-cannot-receive and inventory-full results, throw-away and
abandon prompts, abandon-confirmed and drop-confirmed results, drop-selection
prompt text, and forbidden-drop result text. This keeps the present family
readable without decoding the EB text bytecode into macro source yet.

## EBATTLE2 Action-Flavor Follow-up

The `EF:7E25..843F` EBATTLE2 island is now split around exact listing labels
from `MSG_BTL_PPDOWN` through `MSG_BTL_CHOU_ONPA`. These labels are
intentionally conservative and mostly symbol-derived: the visible English text
shows enemy action narration, but some original symbol names are better kept as
stable anchors until a C2 action-table consumer pass proves narrower runtime
roles. The result is still useful immediately because the large pre-start-battle
blob no longer hides dozens of direct battle-text payload targets.

The current consumer frontier keeps this island as a row-message candidate set
for `D5:7B68` row `+4` pointers. Locally proved rows `99 -> EF:7E88`,
`100 -> EF:7EAC`, `101 -> EF:7ED5`, `102 -> EF:7F02`, `103 -> EF:7F1E`,
`104 -> EF:7F32`, `105..116 -> EF:7F5A..80AC`, `117 -> EF:80C4`,
`118 -> EF:80E4`, `201..206 -> EF:82D7..838A`, `207 -> EF:83A8`,
`208..210 -> EF:83CA..8413`, and `238 -> EF:8010` now use
`RowPresentationText` source names. The remaining exact `MSG_BTL_*` anchors
outside this EBATTLE2 island should stay symbol-derived until row `+8`
behavior bodies are joined.

## EBATTLE0 Status Follow-up

The EBATTLE0 front now names the two direct `DC1C` status corridors that sit
between EBATTLE2 action flavor and EBATTLE1 row presentation text. `EF:843F`,
`EF:8444`, and `EF:8445` are battle-start asleep, PSI-seal, and strange status
announcements emitted after `C2:4F62+` builds target text context through
`C2:3D05`. `EF:845D` and `EF:8477` are random-action strange and mushroom
status text emitted directly before the `D5:7B68` row `+4` message selection.

The labels intentionally name the caller lane rather than the old EBATTLE
symbols: battle-start anchors use `BattleStart...StatusAnnouncementText`, and
the random-action anchors use `RandomAction...StatusText`. This keeps both
families separate from the adjacent EBATTLE1 `RowPresentationText` anchors
displayed through `C1:DD9F`.

## EBATTLE1 Battle Command Front Follow-up

The first slice of `EF:848C..C51B` is now split through `EF:8814`. This is the
runtime-facing battle-command front already tied to the C2 action table notes:
`EF:848C` is the Bash/attack row presentation text pointer for the table's
ordinary attack entry, `EF:84B6` is the Shoot row presentation text, `EF:8530`
is the Spy/check row presentation text, and `EF:8543` is the shared PSI-name
`ByteSubstitution` row presentation text reused by many PSI-shaped action rows.
Guard, Metamorphose, and flee labels in the same front now use command/result
names without claiming additional row evidence. The `EF:857E` dispatch and
`EF:864C..8813` branches remain ROM-preserved text/effect bytecode, but now
have stable anchors for later PSI animation/effect consumer work.

The row-message consumer split is now explicit: `C2:5C66` selects the
`D5:7B68` row `+4` message pointer and displays it through `C1:DD9F`, while
the row `+8` behavior pointer is a separate C2 action payload. The shared
`EF:8543` PSI row message still belongs to that `DD9F` row-presentation lane;
its `ByteSubstitutionRowPresentationText` suffix records both facts: the
displayed row message consumes the `C1:DD7C -> $9D11 -> 19 1F` PSI-name byte,
and the row-message proof remains distinct from row `+8` behavior bodies.
The row-message crosswalk now records those source labels directly so the
proved early `DD9F` joins no longer appear as bare EF pointers.

## Thunder, Effect, And Pray Follow-up

The adjacent `EF:8814..89FE` run is now split around the US listing labels that
continue the EBATTLE1 PSI presentation table. C2 Thunder common already emits
`EF:8814` for the small Thunder presentation and `EF:8823` for the large
Thunder presentation, with `EF:8837` serving the Thunder miss sound
presentation payload.
The `EF:883D..89E0` branch anchors preserve the PBFX 17-50 presentation
dispatch targets without trying to decode the EB text bytecode yet. `EF:89E0`
is the Pray row presentation text pointer used by the action table, so the
first Pray entry is now visible before the following EBATTLE3 enemy-action text
block.

## EBATTLE3 Enemy-Action Follow-up

The complete `EF:89FE..8FAD` EBATTLE3 include is now split around its exact US
listing labels. This is another symbol-derived action-flavor island, similar to
the earlier EBATTLE2 split: the anchors cover rumble/grab/curse/flavor attacks,
physical variants, enemy hesitation branches, HP-sucker and Shield Killer
scripts, and the late lightning/Giygas-flavor scripts. The split keeps the
runtime payloads visible for a later C2 action-table consumer pass while still
leaving the EB text bytecode ROM-preserved.

The proved C2 row joins now split out the EBATTLE3 row-presentation subset:
`EF:8BE8` is the diamondize-bite row message, `EF:8C58/8EBE` are the
bad-smell odor/gas row messages, `EF:8D9F` is the Neutralizer sparkle row
message, `EF:8DDE` is the rainbow-colors event presentation, `EF:8E27` is the
shared named-item row message reused by rows `140` and `247`, and `EF:8E3C`
is the concentration/PSI-seal row message. The rest of the EBATTLE3 include
should remain exact `MSG_BTL_*` anchors until specific `D5:7B68` rows are
mapped.

## EBATTLE9 Field-Monster And Graveyard Follow-up

The `EF:8FAD..9A47` EBATTLE9 include is now split as a coherent field-facing
payload island. The front `_SUB_SOREZORE` branch and its end label are helper
anchors used by the local message scripts, followed by the Moon/Pyramid/Brick
Road/stone-boss field-monster payload families. The tail covers graveyard and
Paula-related branches, the Lilliput Steps boss script, the mushroom girl and
Shinto bridge text, and the long Guts tutorial yes/no branches. These remain
ROM-preserved text bytecode, but the include is no longer one anonymous EF
tail before the later EBATTLE1 action-text block.

## EBATTLE1 Action-Tail Follow-up

The later EBATTLE1 include at `EF:9A47..9EF4` is now split around exact action
payload labels. This covers the join/call-for-help seed text, explosion/burn
and goods-use branches, Time Stop and enemy gaze/wave/breath/status-flavor
messages, coffee/music/discharge/lightning/fire payloads, and the final
`MSG_BTL_FIRE_BREATH` anchor before the next `EGOODS2` include. These are
conservative symbol-derived anchors for later C2 action-table consumer work.

The first strong local row-message join in this tail is action-table row `85 ->
EF:9DA1`, whose row `+8` body applies concentration/PSI seal and then emits
`EF:6C0B` or fallback `EF:766E`. That keeps row-message text separate from the
secondary result scripts emitted by the behavior body.

The follow-up row-message crosswalk now expands this tail into the
source-backed late affliction rows: persistent status rows `75..76`,
temporary-status rows `78..87`, asleep row `90`, and the item-side
concentration row `159` in EBATTLE3. The EBATTLE1 late status rows now carry
`RowPresentationText` source names, while their success/failure result scripts
stay separately named.

The crosswalk also records a stricter unresolved frontier: numeric-effect rows
and no-op/flavor rows may have well-understood C2 row `+8` behavior bodies, but
they should not drive EF row-message renames until their row `+4` EF pointers
are locally recovered. This keeps `C1:DD9F` presentation text separate from
`DC1C`/`DC66` result text and avoids overclaiming from behavior-only evidence.

The special-event rows `243` and `244` are now joined in that crosswalk as
proved EF row-message entries: `243 -> EF:72F6 -> C2:9298` and
`244 -> EF:7415 -> C2:92EE`. Their behavior bodies then emit the already split
continuations at `EF:72F7`, `EF:733D`, and `EF:743B`, so the row presentation
and event-result text stay separate.

The same crosswalk now pulls in the neighboring healing and explosive row
messages that local C2 notes already prove: row `99 -> EF:7E88`, row
`101 -> EF:7ED5`, and row `140 -> EF:8E27`. It also records the non-EF
row-message lanes for C9 item wrappers and Final Prayer so EF anchor work does
not accidentally claim presentation text that lives in another bank.

It also calls out the PSI-side status rows `53` and `58`, which reuse the
shared `EF:8543` PSI `ByteSubstitution` action text while their row `+8`
bodies emit asleep and strange status-result scripts. This keeps shared PSI
presentation text distinct from the later `EF:6C55` and `EF:6C3A`
direct-result payloads.

The non-EF row-message table also includes the later C9 bomb-family item rows
`167`, `168`, `310`, and `311`, keeping those item presentation wrappers out
of EF action-anchor naming while preserving their C2 behavior-body joins.

Rows `64` and `65` are now recovered explosive row-message joins:
`64 -> EF:9A7E -> C2:A821` and `65 -> EF:9A9E -> C2:A821`. Those row `+4`
presentation scripts are separate from row `101 -> EF:7ED5`, which reaches the
same explosive behavior body with fired-missile presentation text.

The same pointer-recovery pass proved PSI-side Lifeup rows `32..35` and
offense-up rows `48/49` reuse the shared `EF:8543` PSI-name
`ByteSubstitution` row-presentation anchor. Their C2 healing/stat wrappers and
HP/C8 amount result lanes remain separate from that `DD9F` presentation text.

The complete `C2:9039` default/item-use pass now has an EF/non-EF split. Rows
`60/61` reuse the shared `EF:8543` PSI-name row text, item-use rows `259`,
`270`, and `271` enter EGOODS2 at `EF:9EF4`, `EF:A0DC`, and `EF:A2AB`, row
`279` reuses the successful flee text at `EF:84F3`, and EBATTLE3 flavor rows
`309` and `313..317` now carry `FlavorRowPresentationText` labels. Rows
`190..200`, `272/276`, `281/282`, `284..289`, `308`, and `312` instead land in
C7/C9/C6 row-message banks, so they document C2 consumer joins without driving
EF anchor renames.

The row-pointer recovery frontier now records the resolved set and the remaining
local frontier. The ROM-backed inspector is available in this checkout, and the
row-backed exact battle-action frontier is now closed. The row-backed EGOODS2
item-use scripts `EF:9EF4`, `EF:A0DC`, and `EF:A2AB` now carry
`ItemUsePayloadText` labels rather than inherited `MsgBtl` shells, keeping their
item-use payload role separate from battle-action row presentation naming.

The neighboring no-op-tail pass is now also complete. `C2:903C` only joins row
`9` to a C7 empty/default message, while `C2:903F`, `9042`, `9045`, `9048`,
`904B`, and `904E` join rows `251..256` to already named EF
homesick/action-blocked/recovery text. The EF source comments now record those
row `+4` joins without renaming the dual-use anchors.

That no-op/flavor pass now proves the main `C2:9033` and tiny-tail frontier:
rows `119..134`, `251..257`, and `260..266` have exact EF row `+4`
presentation pointers. The EBATTLE2 strip at `EF:8109..82D7` now promotes
rows `119..134` from exact `MSG_BTL_*` shells into
`FlavorRowPresentationText` labels. The EBATTLE4/status rows stay under their
event/status/result labels because several recovered row messages are dual-use
scripts rather than pure action flavor.

The consumer-lane contract note now gives the compact decision table for these
joins: `DD9F` row presentation, `DC1C` direct results, `DC66` amount payloads,
`DD7C` byte substitution, pointer substitution, and non-EF C7/C8/C9
row-message lanes.

The EF source comments now carry the strongest row-message lane joins directly
at their anchors: special-event row presentation versus continuations
(`EF:72F6`, `EF:72F7`, `EF:733D`, `EF:7415`, `EF:743B`), healing/explosive row
messages (`EF:7E88`, `EF:7ED5`), shared PSI `ByteSubstitution` presentation
(`EF:8543`), reused named-item/normalization presentation (`EF:8E27`), row
`290` event presentation (`EF:8DDE`), and the late status row-message cluster
in `EF:9C51..9DDA`.

The adjacent direct-result comments now also mark the status/no-effect islands
that C2 row `+8` behavior bodies emit through `DC1C`, not the row `+4`
presentation lane: `EF:6B81..6C55` for status-result text and `EF:766E` for
the shared no-effect fallback. The source labels now carry the
`StatusResultText` suffix across the proved EBATTLE5 status island
(`EF:6AC7..6C55`) and the shared EBATTLE4 no-effect fallback (`EF:766E`).

The EBATTLE4 result tail now applies the same suffix contract to the PP-loss
and periodic damage island: `EF:7755`, `EF:7768`, `EF:7787`, `EF:77B1`, and
`EF:77DB` are `ActionAmount` result scripts, not row-message anchors. The
central damage/drain front now uses the same convention for `EF:75AB..773F`.

The EBATTLE8 level-up gain island carries `ActionAmount` suffixes for
`EF:7A7D..7B46`. These are C1 level-up narration consumers rather than C2
action-row result emissions, but they read the same staged amount slot through
`1C 0F`.

The EF source now also carries negative guardrails at the most tempting
non-row-message Lifeup anchors: Lifeup explanation text `EF:5173..51BB` and
enemy-action Lifeup flavor `EF:8D4C`. Rows `32..35` proved their presentation
text at `EF:8543`, while explosive rows `64/65` proved `EF:9A7E/9A9E`, so those
guards now prevent only adjacent-lane confusion rather than blocking the
recovered row-message joins.

## EGOODS2 Item-Use Follow-up

The `EF:9EF4..A2FA` EGOODS2 include is now split into item-use payload anchors.
The front Exit Mouse script has separate failure and destination branches,
followed by the Hieroglyph payload, Town Map success/failure text, and Onett
traveler-shack receive/end branches. This keeps item/map text payloads separate
from the preceding EBATTLE1 action text and the following unknown event payload
at `EF:A2FA`.

## Tail Event, Window Text, Keyboard, And Debug Follow-up

The final `EF:A2FA..C51B` tail is now split across the listing-visible payload
families. `EF:A2FA` is the unknown monster-off/Sky Runner event script that
sets `FLG_SYS_MONSTER_OFF`, stages Sky Runner and Dr. Andonuts sprites, and
returns into the Jeff/Threed event flow. `EF:A37A` and `EF:A3B6` expose the
command-window and status-window text tables that sit before the keyboard
include. `EF:A460..A6EB` splits the six name-input keyboard layouts, then
`EF:A6EB` and `EF:A6EC` expose the one-byte `UNKNOWN7` end-block payload and
the larger debug/menu runtime script that runs to `EF:C51B`.

## Front PSI And Field-Event Follow-up

The front `EF:4E20..69A1` corridor is now split through the exact includes that
precede EBATTLE5. `EF:4E20..57EB` exposes the PSI explanation text used by PSI
help/menu descriptions, from Rockin through Teleport. `EF:57EB..617B` exposes
the Dungeon Man/Deep Darkness field-event scripts, including Gumi Village
branches and readable-glyph payloads. `EF:617B..69A1` exposes Grapefruit
Falls/Threed event text and boss-grave branches. The result is a fully labeled
front half of the EF text-payload module without converting the EB text bytecode
to macro source.

## Adjacent Glyph And Debug-String Follow-up

The adjacent `EF:C51B..D56F` table corridor is now split around its
listing-visible includes. `EF:C51B..CD1B` names the text glyph merge mask table
used by the C4 token renderer, `EF:CD1B..D51B` names the companion carry-mask
table for row-crossing glyph runs, and `EF:D51B..D56F` exposes the debug
sound-menu option/version strings before the late debug/menu code begins.

## Validation

For an EF-only label/comment pass, validate the EF scaffold and byte
equivalence:

```powershell
python tools\build_source_bank_scaffold.py --bank EF
python tools\validate_source_bank_byte_equivalence.py --bank EF --module all --combined --scaffold src\ef\bank_ef_helpers_asar.asm --strict
```

If a follow-up also edits C2 consumers, validate C2 as well:

```powershell
python tools\build_source_bank_scaffold.py --bank C2
python tools\validate_source_bank_byte_equivalence.py --bank C2 --module all --combined --scaffold src\c2\bank_c2_helpers_asar.asm --strict
```
