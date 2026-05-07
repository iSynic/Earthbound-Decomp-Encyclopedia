# EF Battle Text Row-Message Crosswalk

This note is the first concrete crosswalk from the EF action-message islands to
source-backed `D5:7B68` battle-action rows. It expands the frontier note by
recording rows whose `+4` EF message pointer and `+8` C2 behavior pointer are
already joined by focused C2 notes.

Scope:

- EF row-message anchors in `src/ef/ef_4e20_c51b_text_payload_data.asm`
- C1 display lane: `C1:DD9F` row-message display from `C2:5C66`
- C2 behavior lane: `D5:7B68` row `+8` behavior pointers consumed through
  the C2 action-payload path

Pointer-recovery follow-up:

- `notes/ef-battle-text-consumer-lane-contracts.md`
- `notes/ef-battle-text-row-pointer-recovery-frontier.md`

This is a consumer crosswalk, not an EB text macro decode. Exact `MSG_BTL_*`
labels remain stable unless the C2 behavior body proves a narrower result name.

Evidence boundary:

- The local `src/d5/table_battle_action_table.asm` scaffold proves the
  `D5:7B68` action-table span, row count, and `0x0C` stride, while
  `tools/inspect_battle_action.py` can recover exact row bytes from a local
  ROM.
- C2 late-action notes often prove row `+8` behavior bodies. Those bodies are
  enough to document direct result scripts, but not enough to rename an EF
  row-message anchor unless the row `+4` pointer is also known.
- Rows below are promoted only when local notes, source-backed C2 evidence, or
  ROM-backed row inspection already join the row id, row `+4` EF message
  pointer, and row `+8` behavior pointer.

## Status-Action Row Messages

These rows are the highest-value EF/C2 joins because the row message, behavior
body, success text, and fallback text are all visible.

| Row | Row `+4` EF message | Row `+8` C2 body | Behavior result payloads |
| ---: | --- | --- | --- |
| `53` | `EF:8543` shared PSI `ByteSubstitution` text | `C2:9F57 -> C2:9F06` | PSI-side asleep/affliction+2 value `1`; emits `EF:6C55` or `EF:766E` |
| `58` | `EF:8543` shared PSI `ByteSubstitution` text | `C2:A056` | PSI-side strange/affliction+3 value `1`; emits `EF:6C3A` or `EF:766E` |
| `75` | `EF:9C30` `MushroomSporesRowPresentationText` | `C2:8BBE` | Mushroomized/affliction+1 value `1`; emits `EF:6B81` or `EF:766E` |
| `76` | `EF:9C51` `PossessedStatusRowPresentationText` | `C2:8BFD` | Possessed/affliction+1 value `2`; emits `EF:6B98` or `EF:766E` |
| `78` | `EF:9CAD` `CryingMoldSporesRowPresentationText` | `C2:8C69` | Crying/affliction+2 value `2`; emits `EF:6BBB` or `EF:766E` |
| `79..82` | `EF:9CD1/9CF1/9D14/9D3E` immobilizing `RowPresentationText` variants | `C2:8CB8` | Immobilized/affliction+2 value `3`; emits `EF:6BD3` or `EF:766E` |
| `83` | `EF:9D62` `SolidificationScaryWordsRowPresentationText` | `C2:8CF1` | Solidified/affliction+2 value `4`; emits `EF:6BEF` or `EF:766E` |
| `84` | `EF:9D81` `StrangeStatusSuspiciousThingRowPresentationText` | `C2:8D3A -> C2:A056` | Strange/affliction+3 value `1`; emits `EF:6C3A` or `EF:766E` |
| `85` | `EF:9DA1` `ConcentrationPsiSealRowPresentationText` | `C2:8D5A` | Concentration/PSI-seal affliction+4 value `4`; emits `EF:6C0B` or `EF:766E` |
| `86` | `EF:9DBD` `StrangeStatusThoughtRowPresentationText` | `C2:8DBB` | Direct strange/affliction+3 value `1`; emits `EF:6C3A` or `EF:766E` |
| `87` | `EF:9DDA` `CryingBreathRowPresentationText` | `C2:8DFC` | All-target crying-family sibling; grouped with the affliction+2 crying body |
| `90` | `EF:9E47` `AsleepMusicRowPresentationText` | `C2:9F57 -> C2:9F06` | Asleep/affliction+2 value `1`; emits `EF:6C55` or `EF:766E` |
| `159` | `EF:8E3C` `ConcentrationPsiSealRowPresentationText` | `C2:A3D1` | Item-side concentration/PSI-seal; emits `EF:6C0B` or `EF:766E` |
| `207` | `EF:83A8` `StrangeStatusLaughRowPresentationText` | `C2:8D3A -> C2:A056` | Strange-status wrapper reuse; emits `EF:6C3A` or `EF:766E` |

Important modeling point: the row `+4` message is the action presentation text
shown through `C1:DD9F`. The success/failure payloads listed above are separate
result scripts emitted later by the row `+8` behavior body through `DC1C`.

## Physical, Special, Item, And Flavor Row Messages

These rows are also source-backed, but the behavior bodies are damage,
normalization, special-event, or message-only rather than simple affliction
writes.

| Row | Row `+4` EF message | Row `+8` C2 body | Current behavior read |
| ---: | --- | --- | --- |
| `99` | `EF:7E88` `FuelSupplyFullHealRowPresentationText` | `C2:9AD8` | Full-heal reuse over the fixed-amount healing core; fuel-supply presentation text |
| `100` | `EF:7EAC` `PoisonFangsRowPresentationText` | `C2:8F97` | Poison-on-hit physical action; secondary success text `EF:6B18` |
| `101` | `EF:7ED5` `FiredMissileRowPresentationText` | `C2:A821` | Projectile/explosive wrapper over bomb-common splash damage; fired-missile presentation text |
| `102` | `EF:7F02` `AttackContinuouslyRowPresentationText` | `C2:8FF9` | Exact double-bash wrapper over `C2:859F` |
| `104` | `EF:7F32` `FlamingFireballRowPresentationText` | `C2:900B` | One-target fire-damage wrapper |
| `117` | `EF:80C4` `TornadoRowPresentationText` | `C2:902C` | All-target physical wrapper over `C2:8651` |
| `118` | `EF:80E4` `GiganticBlastRowPresentationText` | `C2:902C` | Same all-target physical wrapper reuse |
| `140` | `EF:8E27` `SharedNamedItemRowPresentationText` | `C2:9AD8` | Item-side full-heal reuse over the fixed-amount healing core; named-item presentation wrapper |
| `228` | `EF:8BE8` `DiamondizeBiteRowPresentationText` | `C2:916E` | One-target diamondize action; emits `EF:6AC7` or `EF:7655` |
| `232` | `EF:8C58` `BadSmellOdorRowPresentationText` | `C2:9254` | Odor/offense-reduction family; reports amount through C8 text via `DC66` |
| `243` | `EF:72F6` `RunawayFiveBreakInRowPresentationText` | `C2:9298` | Runaway Five / Clumsy Robot special-event controller; branches to `EF:72F7` or `EF:733D` |
| `244` | `EF:7415` `PooBreakInRowPresentationText` | `C2:92EE` | Master Barf defeat / Poo Starstorm event result; later emits `EF:743B` |
| `247` | `EF:8E27` `SharedNamedItemRowPresentationText` | `C2:90C6` | Battler normalization wrapper; can emit `EF:7142` and queue `EF:7123` |
| `248` | `EF:8D9F` `NeutralizeSparkleRowPresentationText` | `C2:90C6` | Same normalization wrapper reuse |
| `273` | `EF:8EBE` `BadSmellGasRowPresentationText` | `C2:9254` | Odor/offense-reduction family reuse |
| `290` | `EF:8DDE` `RainbowColorsEventRowPresentationText` | `C2:C14E` | Rainbow-colors / Master Belch-side special-event family |

## Numeric, Healing, And Explosive Row Messages

The local ROM-backed inspector recovered the formerly behavior-only row `+4`
joins for the highest-risk amount/healing/explosive rows. Their behavior
bodies still emit separate result or amount text after the `DD9F` presentation.

| Row | Row `+4` EF message | Row `+8` C2 body | Current behavior read |
| ---: | --- | --- | --- |
| `32..35` | `EF:8543` `SharedPsiNameByteSubstitutionRowPresentationText` | `C2:9AC6`, `C2:9ACF`, `C2:9AD8`, `C2:9AE1` | PSI Lifeup alpha/beta/gamma/omega row presentation; HP recovery worker emits result text through `C2:7294` |
| `48` | `EF:8543` `SharedPsiNameByteSubstitutionRowPresentationText` | `C2:9E38` | PSI offense-up row presentation; amount text lives in C8 via `DC66` |
| `49` | `EF:8543` `SharedPsiNameByteSubstitutionRowPresentationText` | `C2:9E7F` | All-target offense-up wrapper over the same amount lane |
| `64` | `EF:9A7E` `ExplosionRowPresentationText` | `C2:A821` | Explosive wrapper over bomb-common splash damage |
| `65` | `EF:9A9E` `BurstIntoFlamesRowPresentationText` | `C2:A821` | Same explosive wrapper over bomb-common splash damage |
| `95` | `EF:7E25` `PpReductionRowPresentationText` | `C2:8E42` | PP reduction family; C8 amount text through `C1:DC66` |
| `96` | `EF:7E3E` `SteamedOffenseUpRowPresentationText` | `C2:9E38` | One-target offense-up family; C8 amount text through `C1:DC66` |
| `97` | `EF:7E55` `DirtyWordsGutsReductionRowPresentationText` | `C2:8EAE` | Guts-cutting family; C8 amount text through `C1:DC66` |
| `98` | `EF:7E70` `MoistureSuckedOffenseDefenseReductionRowPresentationText` | `C2:8F21` | Paired offense/defense reduction family; C8 amount text through `C1:DC66` |
| `233` | `EF:8C75` `LoudVoiceOffenseDefenseReductionRowPresentationText` | `C2:8F21` | Paired offense/defense reduction family; reports amount through C8 text via `DC66` |
| `234` | `EF:8C92` `WarCryOffenseDefenseReductionRowPresentationText` | `C2:8F21` | Same paired offense/defense reduction family |

Rows whose behavior body emits C8/C9 scripts should not force EF result names.
Keep the EF row-message labels presentation-oriented and document the secondary
script bank in the C2-focused note.

`EF:8E27` is intentionally listed twice: row `140` uses it as a named-item
healing presentation wrapper, while row `247` uses the same row-message anchor
with the normalization wrapper. The C2 row `+8` body is what separates those
runtime roles.

## EBATTLE2 Proved Action Row Messages

The EBATTLE2 exact `MSG_BTL_*` subset below now has concrete row `+4/+8`
evidence, so the EF labels use `RowPresentationText` while preserving the
original symbol stem.

| Row | Row `+4` EF message | Row `+8` C2 body | Current behavior read |
| ---: | --- | --- | --- |
| `103` | `EF:7F1E` `MigamaeRowPresentationText` | `C2:889B` | Guard/stance-style row presentation |
| `105` | `EF:7F5A` `GekitotuRowPresentationText` | `C2:85DA` | Collision/charge row presentation |
| `106..116` | `EF:7F7B..80AC` `Karate` through `Konbou` row presentation texts | mostly `C2:8651` | Physical action-flavor row presentations |
| `201..206` | `EF:82D7..838A` `MabusiiHikari` through `HaikiGas` row presentation texts | `C2:99EF`, `987D`, `8A92`, `8CF1`, `8B2C`, `8C69` | Late EBATTLE2 special/status row presentations |
| `208..210` | `EF:83CA..8413` `Fue`, `JumpToFace`, `ChouOnpa` row presentation texts | `C2:8E3B`, `8CF1`, `8CF1` | Late EBATTLE2 special/status row presentations |
| `238` | `EF:8010` `KamitukiRowPresentationText` | `C2:859F` | Reuse of row `111` bite text with a single-target bash body |

## EBATTLE3 Proved Enemy Row Messages

The EBATTLE3 exact `MSG_BTL_*` subset below now has concrete row `+4/+8`
evidence. The no-op rows keep `FlavorRowPresentationText`; the rest use
row-presentation labels with the original symbol stem.

| Row | Row `+4` EF message | Row `+8` C2 body | Current behavior read |
| ---: | --- | --- | --- |
| `160`, `161`, `176` | `EF:8E9E`, `EF:8E5E`, `EF:8E7E` shield/HP-suck row texts | `C2:A422`, `A46B`, `A507` | Shield-kill and HP-suck row presentations |
| `211..227` | `EF:89FE..8BC0` `Jihibiki` through `Skateboard` row texts | mixed physical/status bodies | Main EBATTLE3 enemy-action row presentations |
| `229..231` | `EF:8BFB..8C3A` `Kudamaki`, `Sekkyou`, `Shikaritsuke` row texts | `C2:8EAE` | Guts/stat reduction row presentations |
| `235`, `236` | `EF:8CAC`, `EF:8CC7` `FakeDead` and `Yudan` flavor row texts | `C2:9033` | Flavor-only no-op row presentations |
| `241`, `242` | `EF:8D72`, `EF:8DC1` `NebieBeam` and `Makitsuki` row texts | `C2:8B6D`, `8CB8` | Special/status row presentations |
| `274`, `300..307` | `EF:8F17`, `EF:8EE2`, `EF:8F4A` Lightning row texts | `C2:987D`, `9647`, `99EF` | Lightning alpha/beta/gamma presentation reused across PSI wrappers |

## EBATTLE1 Proved Action-Tail Row Messages

The EBATTLE1 action-tail exact `MSG_BTL_*` subset now has concrete row `+4/+8`
evidence. EGOODS2 item-use scripts retain their item-use labels and remain
outside this battle-action naming set.

| Row | Row `+4` EF message | Row `+8` C2 body | Current behavior read |
| ---: | --- | --- | --- |
| `62`, `63` | `EF:9A47`, `EF:9A5E` `Nakama0` and `Tanemaki0` row texts | `C2:C145`, `C13C` | Late action-tail special row presentations |
| `66..74` | `EF:9ABB..9C02` `Goods` through `TumetaiIki` row texts | mixed item/status bodies | Item/status/action row presentations |
| `77` | `EF:9C7E` `YoiKaoriRowPresentationText` | `C2:8E3B` | Status/recovery row presentation |
| `88`, `89` | `EF:9E05`, `EF:9E22` `Typhoon` and `Coffee` row texts | `C2:99EF`, `95AB` | PSI/special row presentations |
| `91..94` | `EF:9E69..9ED7` `SyoukaEki` through `FireBreath` row texts | `C2:95BD`, `987D`, `95C6`, `95BD` | Elemental/special row presentations |

## Flavor-Only No-Op Row Messages

These rows have no-op or tiny row `+8` behavior tails, so the row `+4` message
is the gameplay-facing payload. Keep these labels presentation-oriented and do
not collapse them into "no effect" result text.

| Row | Row `+4` EF message | Row `+8` C2 body | Current consumer read |
| ---: | --- | --- | --- |
| `119` | `EF:8109` `DefiantSmileFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `120` | `EF:812B` `LoudSmileFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `121` | `EF:814F` `EdgeCloserFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `122` | `EF:81A5` `Mutter3FlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `123` | `EF:8186` `Mutter2FlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `124` | `EF:8167` `Mutter1FlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `125` | `EF:81C4` `FellDownFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `126` | `EF:81D7` `AbsentMindedFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `127` | `EF:81F1` `SteamCloudFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `128` | `EF:8211` `WobblyFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `129` | `EF:8226` `StaggerFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `130` | `EF:8239` `GrinFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `131` | `EF:825C` `DeepBreathFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `132` | `EF:8281` `GreetingFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `133` | `EF:8299` `RoarFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `134` | `EF:82BC` `TeethChatterFlavorRowPresentationText` | `C2:9033` | Flavor-only no-op tail |
| `251` | `EF:727F` `HomesickRandomThoughtDispatcher` | `C2:904E` | Tiny no-op tail; existing EBATTLE4 homesick dispatcher label remains accurate |
| `252` | `EF:7192` `ParalysisActionBlockedStatusText` | `C2:9042` | Tiny no-op tail; dual-use action-blocked status text |
| `253` | `EF:71DF` `AsleepActionBlockedStatusText` | `C2:904B` | Tiny no-op tail; dual-use action-blocked status text |
| `254` | `EF:71F6` `ImmobilizedActionBlockedStatusText` | `C2:903F` | Tiny no-op tail; dual-use action-blocked status text |
| `255` | `EF:6F0B` `FrozenMovementRecoveryResultText` | `C2:9045` | Tiny no-op tail; dual-use recovery/result text |
| `256` | `EF:720C` `PsiSealActionBlockedStatusText` | `C2:9048` | Tiny no-op tail; dual-use PSI-seal action-blocked text |
| `257` | `EF:725A` `FlyHoneyMindLostEventText` | `C2:9033` | Flavor-only no-op tail; event/flavor row message |
| `260` | `EF:745F` `PokeyRandomTalkDispatcher` | `C2:9033` | Flavor-only no-op tail; random-talk dispatcher |
| `261` | `EF:749D` `PokeyRandomTalkPlayedDeadBranch` | `C2:9033` | Flavor-only no-op tail |
| `262` | `EF:74B0` `PokeyRandomTalkPretendedCryBranch` | `C2:9033` | Flavor-only no-op tail |
| `263` | `EF:74C9` `PokeyRandomTalkApologyBranch` | `C2:9033` | Flavor-only no-op tail |
| `264` | `EF:7569` `CompanionMyDogHowlingText` | `C2:9033` | Flavor-only no-op tail |
| `265` | `EF:7579` `CompanionPickeyTalkText` | `C2:9033` | Flavor-only no-op tail |
| `266` | `EF:7591` `CompanionTonyTalkText` | `C2:9033` | Flavor-only no-op tail |

Rows `251..257` and `260..266` prove `DD9F` row-message joins, but their source
labels already encode useful event/status/result roles. Keep those labels until
a narrower caller split proves that one role should dominate the other.

The neighboring no-op-tail sweep is now complete: `C2:903C` is only row `9`
with a C7 empty/default message, while `C2:903F`, `9042`, `9045`, `9048`,
`904B`, and `904E` are the EF row `251..256` entries above. No additional EF
anchor promotion is implied by the address-distinct tail bodies.

## Early Row-Message Anchors

The early row-message joins remain the cleanest `DD9F` examples:

| Row | Row `+4` EF message | Row `+8` C2 body | Current behavior read |
| ---: | --- | --- | --- |
| `4` | `EF:848C` `BashAttackRowPresentationText` | `C2:859F` | Bash |
| `5` | `EF:84B6` `ShootRowPresentationText` | `C2:8740` | Shoot |
| `6` | `EF:8530` `SpyCheckRowPresentationText` | `C2:8770` | Spy |
| `7` | `EF:89E0` `PrayRowPresentationText` | `C2:AD1B` | Pray |
| `10..35`, `48`, `49`, `53`, `58`, `60`, `61` | `EF:8543` `SharedPsiNameByteSubstitutionRowPresentationText` | PSI wrapper/status/offense families plus `C2:9039` default rows | Shared PSI row message; `ByteSubstitution` PSI name |

## How To Use This Crosswalk

For future EF payload work:

- If a row `+4` message has a row-specific C2 body and a result script, name the
  EF row-message anchor conservatively around the proved presentation role and
  document the behavior/result split in this crosswalk.
- If the C2 body emits a separate EF script through `DC1C` or `DC66`, keep that
  result payload named independently from the row-message text.
- If only table order or reference names are known, keep the anchor
  symbol-derived and leave it in the action-island frontier.

## Next Crosswalk Frontier

The immediate frontier has narrowed again: Lifeup, numeric-effect, explosive,
the main no-op/flavor rows, and the complete `C2:9039` default/item-use bucket
now have recovered row `+4` joins. The `C2:9039` body is not an EF naming
signal by itself: rows whose `+4` pointers land in C7/C9/C6 remain non-EF
presentation consumers, while the EF rows below can be named or guarded
according to their actual payload family.

### EF Rows With `C2:9039` Default Bodies

| Row | Row `+4` EF message | Row `+8` C2 body | Current behavior read |
| ---: | --- | --- | --- |
| `60`, `61` | `EF:8543` `SharedPsiNameByteSubstitutionRowPresentationText` | `C2:9039` | Shared PSI-name row presentation with default/no-op behavior |
| `259` | `EF:9EF4` `EGoods2ExitMouseItemUsePayloadText` | `C2:9039` | Exit Mouse item-use payload; keep EGOODS2 item-use naming |
| `270` | `EF:A0DC` `EGoods2HieroglyphItemUsePayloadText` | `C2:9039` | Hieroglyph item-use payload; keep EGOODS2 item-use naming |
| `271` | `EF:A2AB` `EGoods2TownMapItemUsePayloadText` | `C2:9039` | Town Map item-use payload; keep EGOODS2 item-use naming |
| `279` | `EF:84F3` `PlayerFleeSuccessText` | `C2:9039` | Successful flee text reused as a row `+4` presentation; also known from direct battle-start/result paths |
| `309` | `EF:8F91` `Gyiyyig3FlavorRowPresentationText` | `C2:9039` | Giygas/Gyiyg flavor row presentation; calls the C9 repeated-line helper before its own text |
| `313` | `EF:8D4C` `EnemyLifeupFlavorRowPresentationText` | `C2:9039` | Enemy Lifeup flavor row presentation, not PSI Lifeup rows `32..35` |
| `314..317` | `EF:8CDD`, `EF:8CFB`, `EF:8D17`, `EF:8D2F` `Yudan*FlavorRowPresentationText` | `C2:9039` | Yudan/off-guard flavor row presentations |

### Remaining Special-Event Rows

Rows `243`, `244`, and `290` are now concrete EF row-message joins because the
local special-event notes prove their row `+4` EF message pointers and row `+8`
C2 bodies.

Final Prayer rows `291..299` remain a separate frontier. Many of their row
messages live outside EF, while secondary result scripts still affect the
battle-text contract through C8/C9 direct-result lanes. Keep them out of EF
row-message rename work unless a local row `+4` EF pointer is proved.

## Non-EF Row-Message Lanes

Some source-backed action rows are important to the C1/C2 display contract but
do not name EF anchors at all. Keep them visible here so they do not get
mistaken for missing EF text splits.

| Rows | Row-message bank | Row `+8` C2 body | EF naming impact |
| --- | --- | --- | --- |
| `139`, `141` | `C9:7B6B` item-use wrapper | `C2:9AC6`, `C2:9AE1` | Item-side healing reuses; not EF row messages |
| `166` | `C9:7F56` item strike wrapper | `C2:A5EC` | Damage-plus-solidification item action; success/failure results still emit `EF:6BEF` or `EF:766E` |
| `167`, `168` | `C9:7EB7` item thrown/fired wrapper | `C2:A818`, `C2:A821` | Bomb-family item rows; not EF row messages |
| `186..188` | `C9:FD82`, `C9:FDBB`, `C9:7F72` item/narrative wrappers | `C2:9033` | No-op item/flavor rows; not EF row messages |
| `0..3`, `9`, `258`, `272`, `276` | `C7:*` or `C9:FEFD` default/no-op wrappers | `C2:9039` or `C2:903C` | Default and isolated no-op rows; not EF row messages |
| `190..200`, `308`, `312` | C9 item/narrative wrappers | `C2:9039` | Default item/narrative row messages outside EF; classify C2 join only |
| `281`, `282`, `284..289` | C6 row-message wrappers | `C2:9039` | Default item/map/event presentation rows outside EF; classify C2 join only |
| `310`, `311` | `C9:7E9E` item fired wrapper | `C2:A818`, `C2:A821` | Bomb-family item rows; not EF row messages |
| `291..299` | C9 prayer message family, including `C9:F0B8` and `C9:F3EC` | `C2:C572..C2:C6F0` | Final Prayer ladder; row presentation and C8/C9 narrative results stay outside EF action-anchor naming |

Modeling rule: non-EF row messages still travel through the same row `+4`
presentation lane, but they should not create or rename EF anchors. Only their
secondary direct-result EF scripts belong in the EF payload map.

## Next Evidence To Add

The fastest way to expand this crosswalk is to add or derive local
action-table row evidence with the recovery process in
`notes/ef-battle-text-row-pointer-recovery-frontier.md`. Record, per row:

- row id and row `+0..+3` metadata
- row `+4` EF message pointer
- row `+8` C2 behavior pointer
- secondary EF/C8/C9 result scripts emitted by the behavior body

Once that exists, promote rows family by family. Numeric-effect rows should be
first because their C2 behavior bodies and amount-result lanes are already well
documented; no-op/flavor rows should follow because they need stricter
separation between presentation text and behavior effects.
