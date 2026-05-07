# C2 Party, Inventory, Status Utility Corridor `C216AD..C2307B`

This note covers the next C2 audit gap after the early window/HPPP pass. The corridor sits between the event-flag helpers and the scripted battle/menu includes in `refs/ebsrc-main`, and it mostly acts as connective tissue for:

- text command `0x1F` special handlers
- active party/entity registry changes
- character inventory/equipment-slot maintenance
- small status/affliction table lookups
- temporary save/restore of a live party/state scratch block

## Reference anchors

`refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm` corroborates the ordering:

- `unknown/C2/C216AD.asm`
- `audio/stop_music_redirect.asm`
- `audio/play_sound_and_unknown.asm`
- `unknown/C2/C216DB.asm`
- named postmath/stat/equipment recalculation family
- `text/get_party_character_name.asm`
- `unknown/C2/C22351.asm`
- `unknown/C2/C2239D.asm`
- `unknown/C2/C223D9.asm`
- `unknown/C2/C22474.asm`
- named item subtype helpers
- preview block setup helpers `C22562/C225AC/C2260D/C22673`
- `unknown/C2/C226C5.asm`
- `unknown/C2/C226E6.asm`
- `unknown/C2/C226F0.asm`
- `unknown/C2/C2272F.asm`
- `unknown/C2/C2277C.asm`
- named money/party/save helpers
- `unknown/C2/C22A3A.asm`
- `battle/init_scripted.asm`
- `unknown/C2/C23008.asm`
- `unknown/C2/C2307B.asm`

## `C2:16AD`: music/state latch wrapper

`C2:16AD` takes `A`, calls `C4:FBBD`, then stores the original value into both `$5DD4` and `$5DD6`. The best current local split is:

- `$5DD4` = latched map-music mirror, still soft because it overlaps other staged-transition uses in C0/C4 contexts
- `$5DD6` = current map music track, stronger because C0 current-position music helpers and the ebsrc `change_music_5DD6` include agree

Direct callers:

- `C1:4797`
- `C1:842F`

The clearest caller-side clue is `C1:842F`, reached from the text-command `0x1F 03` branch that the legacy reference comments as "restore default music". That path calls `C0:69F7`, passes `X = 0`, then calls `C2:16AD`. So the safest current name is a behavior-level one: this is a music/audio state latch wrapper, not just a raw store into `$5DD4/$5DD6`.

Working name: `ApplyMusicTrackAndSyncMirror`.

Compatibility alias: `ApplyMusicStateAndMirrorTo5DD4`.

The adjacent tiny audio wrappers are now pinned at the source contract level too:

- `C2:16C9` is `StopMusicRedirect`, a one-call wrapper around `C0:ABC6`.
- `C2:16D0` is `PlaySoundAndTickLightWindow`, a wrapper that sends the sound/effect id in `A` through `C0:ABE0`, then runs `C1:2E42`'s light window tick. This retires the inherited `PLAY_SOUND_AND_UNKNOWN` wording while keeping the older HP/PP-refresh alias as a compatibility clue.

The C1 family-`1F` callers line up with those roles:

- `1F 00` queues or applies a music track through `C2:16AD`.
- `1F 01` stops music through `C2:16C9`.
- `1F 02` plays a sound/effect and ticks the light window through `C2:16D0`.
- `1F 03` restores map music by asking `C0:69F7` for the current-position music track, then applying it through `C2:16AD`.

Follow-up source polish (2026-05-06): the C1 text-command and C2 battle/result
presentation callers now share the same audio vocabulary as C0/C4. C1 names
the deferred music-track queue storage and the `C0:69F7` current-position
music-track getter; C2 instant-win, battle swirl, candidate-pool, rainbow
event, and Final Prayer callers now refer to `C4:FBBD` as `ChangeMusic` rather
than the inherited Sound Stone-specific alias. The instant-win handler also
names its fixed music tracks and the `C0:6A07` current-position music refresh
edge.

## Party overlay and party registry mutations

The previous overlay note already covers `C2:16DB`, `C2:28F8`, and `C2:29BB` in detail. This corridor confirms why they belong in the same local family:

- `C2:28F8` inserts a character/type code into `$986F`, keeping the source array ordered, then calls `C0:369B`, marks the associated sprite/type word with `#$C000`, and for codes `1..4` calls `C2:16DB` and `C3:EBCA`.
- `C2:29BB` removes a code from `$986F`, shifts the remaining entries left, calls `C0:3903`, and for codes `1..4` also calls `C2:16DB` and `C3:EBCA`.

This keeps the existing interpretation strong: `$986F` is the broader active source array, while `$988B` is a derived current-party/type registry layer used by many readers.

`C2:3008` and `C2:307B` are a save/restore pair over a small runtime block that directly touches that same active source array:

### `C2:3008`

This helper:

- copies byte `$983A` to `$9841`
- copies word `$983C` to `$9843`
- copies byte `$983B` to `$9842`
- copies word `$983E` to `$9845`
- removes the byte values in `$983B` and `$983A` from `$986F` through `C2:29BB`
- copies `$9831/$9833` to `$9847/$9849`
- clears `$9831/$9833`

Direct caller: `C1:84FE`, a `0x1F` command leaf.

### `C2:307B`

This helper reverses the above:

- removes the current `$983A/$983B` values from `$986F`
- if `$9841` is nonzero, restores it to `$983A`, reinserts it via `C2:28F8`, and restores `$983C` from `$9843`
- if `$9842` is nonzero, restores it to `$983B`, reinserts it via `C2:28F8`, and restores `$983E` from `$9845`
- restores `$9831/$9833` from `$9847/$9849`

Direct caller: `C1:8505`, the sibling `0x1F` command leaf.

Working names:

- `C2:3008` = `SaveAndClearTemporaryPartySourceState`
- `C2:307B` = `RestoreTemporaryPartySourceState`

The C1 source now names those leaves as text-command `1F 64` and `1F 65`,
respectively, so the caller and callee agree on the temporary party source
save/restore contract instead of leaving raw `JSL $C23008/$C2307B` edges.

The exact user-facing reason for this pair is still soft, but its mechanical role is clear: it temporarily removes up to two active source codes from `$986F`, preserves associated words, and later restores them.

## Character status selector/count helpers

`C2:26F0`, `C2:272F`, and `C2:277C` all scan the party-facing registry at `$988B`, map each code through the `$99CE` character record stride, and inspect byte `$99DC + offset`. Existing notes already identify `$99DC` as the first byte of a seven-byte status/affliction group.

`C2:26F0` returns the first party index whose `$99DC` byte equals `1`, or the loop index after exhausting `$98A4`. This is a "find first state-1 party slot" helper.

`C2:272F` counts party entries whose `$99DC` byte is neither `1` nor `2`. Its direct callers are `C1:51C3` and `C1:5254`, in status/window-facing text command leaves.

`C2:277C` returns the first character code from `$988B` whose `$99DC` byte is neither `1` nor `2`, or `0` if all player-controlled party members have state `1/2`.

Working names:

- `C2:26F0` = `FindFirstPartySlotWithStateOne`
- `C2:272F` = `CountPartySlotsNotStateOneOrTwo`
- `C2:277C` = `FindFirstPartyCodeNotStateOneOrTwo`

The exact enum labels for `$99DC == 1` and `$99DC == 2` remain intentionally unnamed here. The local behavior is pinned; the human-facing ailment/status names still need a tighter cross-reference.

## Status/icon tile lookup helpers

`C2:23D9` and `C2:2474` scan a seven-byte status/affliction slice and convert the first nonzero status byte plus its position into a table value.

Both helpers use this shape:

- start from a pointer in `A`
- inspect the first byte
- otherwise inspect byte `+3`
- otherwise scan bytes `+1..+6`
- derive a small position index
- combine `(status_byte - 1)` and that position index
- read a word from one of the bank-C4 tables

`C2:23D9` has two table modes selected by input `X`:

- `X != 0` uses `C4:5A27`
- `X == 0` uses `C4:5A89`
- if no status byte is found, returns `7` in the nonzero-`X` mode or `#$0020` in the zero-`X` mode

`C2:2474` uses the sibling table `C4:5AEB` and returns `4` if no status byte is found.

Direct callers:

- `C2:23D9` is called by `C2:03C3` twice while composing HP/PP window tilemaps, plus C1 callers at `C1:2180` and `C1:98A6`.
- `C2:2474` is called by `C2:03C3` while building the same HP/PP tilemap family.

The tail of the `C2:2474..2562` source unit also carries two tiny item
subtype classifiers over `D5:5000` item byte `+0x19 & 0x0C`:

- `C2:24E1` returns the four-way equipment slot ordinal
  `weapon/charm/bracelet/headgear -> 1/2/3/4`, or `0` for an unexpected value.
- `C2:2524` returns the grouped non-weapon display ordinal
  `weapon-or-headgear/charm/bracelet -> 1/2/3`, or `0` for an unexpected value.

Those helpers align with the item-byte `+0x19` packed-class and slot-subtype
notes without forcing stronger menu-facing names for the non-weapon families.

Working names:

- `C2:23D9` = `LookupStatusTileValueForHpPpWindow`
- `C2:2474` = `LookupStatusTileWidthOrOffsetForHpPpWindow`
- `C2:24E1` = `ClassifyItemEquipSlotSubtypeOrdinal`
- `C2:2524` = `ClassifyGroupedEquipmentSlotOrdinal`

The "tile value" vs "width/offset" wording is still a little cautious because the final consumer writes both values into layout math before tilemap generation.

## Text-command flag wrappers

`C2:26C5` and `C2:26E6` are small wrappers around the existing event-flag bitfield helpers `C2:165E` and `C2:1628`.

`C2:26C5`:

- takes `A` as set/clear value
- loads flag id from `$9C88`
- calls `C2:165E`
- then calls `C0:C30C` with `$5D64`
- returns the updated flag byte

Direct callers are `C1:85AC` and `C1:85B6`, the `0x1F` command leaves that pass `1` and `0`.

`C2:26E6`:

- loads flag id from `$9C88`
- calls `C2:1628`
- returns the flag state

Direct caller is `C1:85BD`, which then prints/returns the numeric result through the text engine.

The C1 source now names those leaves as text-command `1F A0`, `1F A1`, and
`1F A2`: set current interaction flag, clear current interaction flag, and
return current interaction flag. The set/clear pair intentionally enters the
`C2:26C5` prologue so the incoming boolean in `A` is moved to `X` before the
shared `C2:26D0` tail applies `$9C88` and refreshes the `$5D64` target state.

Working names:

- `C2:26C5` = `SetCurrent9C88FlagAndRefresh5D64`
- `C2:26E6` = `GetCurrent9C88Flag`

## Save-current-game wrapper

`C2:2A2C` is the tiny text-command-facing wrapper for `SAVE_CURRENT_GAME`.
It reads the one-based current save slot at `$B4A1`, decrements it to the
zero-based slot index expected by `EF:0A4D`, and calls the EF save-slot helper.

Direct callers:

- C1 `1F B0` in the dynamic source-selector corridor
- the debug meter/display overlay helper at `C1:2D17`

Working name: `SaveCurrentGame`.

Source polish:

- 2026-05-01: `C2:1628` and `C2:165E` now name the `$9C08`
  event-flag bitfield base, eight-flags-per-byte division, C4 bitmask table,
  and boolean returns.
- 2026-05-01: the `C2:26C5/26D0` and `C2:26E6/26EB` wrapper pairs now call
  out their fall-through prologue/tail structure, `$9C88` current flag id, and
  `$5D64` refresh target.
- 2026-05-01: `C2:26F0`, `C2:272F`, and `C2:277C` now name the `$988B`
  party status registry, player-count bound, character record stride,
  `$99DC` state byte, and state-1/state-2 filter constants.
- 2026-05-01: `C2:3008` and `C2:307B` now name the temporary party source
  save/restore block at `$983A/$983B/$983C/$983E`, its saved mirror at
  `$9841..$9849`, the cleared pair at `$9831/$9833`, and the `C2:28F8` /
  `C2:29BB` active-party overlay insert/remove calls.
- 2026-05-01: `C2:16DB` now names the active entity source array, active
  party-count bound, party-character inventory slots, D5 item-config fields,
  and overlay entity type insert/remove calls used by the arbitration pass.
- 2026-05-01: `C2:23D9` and `C2:2474` now name the seven-byte status-slice
  scan order, C4 status tile tables, no-status fallback values, and table
  index inputs; the `C2:24E1/2524` item-subtype classifier tails now name the
  `D5:5000` item config row, packed class byte `+0x19`, `0x0C` equipment-slot
  subtype mask, and returned slot ordinals.
- 2026-05-06: `C2:16AD` now distinguishes the current map music track at
  `$5DD6` from the softer latched mirror at `$5DD4`; `C2:16D0` now uses the
  source label `PlaySoundAndTickLightWindow`, replacing the inherited
  `PLAY_SOUND_AND_UNKNOWN` name while preserving an HP/PP refresh compatibility
  alias.
- 2026-05-06: the C1 `1F 64/65` dynamic source-selector leaves now call
  `C2:3008` and `C2:307B` by their temporary party source save/restore roles,
  matching the existing C2 source contracts for `$983A..$9849` and `$986F`.
- 2026-05-06: the C1 `1F A0/A1/A2` dynamic source-selector leaves now call
  `C2:26C5` and `C2:26E6` by their current-interaction-flag wrapper roles,
  matching the C2 `$9C88` flag id and `$5D64` refresh contracts.
- 2026-05-06: `C2:2A2C` now names the current-save-slot byte `$B4A1` and the
  EF save-slot callee `EF:0A4D`; the C1 `1F B0` leaf and debug menu command
  caller now call it by its `SaveCurrentGame` role.

## Source Scaffold Promotion

The HP/PP status-tile lookup helpers are now represented as durable source modules:

- `src/c2/c2_23d9_lookup_status_tile_value_for_hp_pp_window.asm` covers `C2:23D9..2474`.
- `src/c2/c2_2474_lookup_status_tile_width_or_offset_for_hp_pp_window.asm` covers `C2:2474..2562`.

Validation after promotion:

- `C2 byte-equivalence: OK, 217 module(s), 0 mismatch(es).`

## Inventory transfer / slot maintenance helper

`C2:2A3A..2F38` is a larger character-inventory transfer helper. Its direct callers are clustered at `C1:39FC`, `C1:3A42`, `C1:3A66`, `C1:3A8A`, `C1:3ACD`, and `C1:3AF0`.

The stable mechanical pieces are:

- input `X` and `Y` behave like source/destination character ids
- input `A` behaves like an item id or staged item byte
- it maps the source character through the `$99F1..$99FE` 14-byte inventory region
- it shifts bytes inside that inventory region and clears the vacated byte
- it calls `C1:8BC6`, the established insertion helper, to insert the transferred/staged item into the destination inventory
- it updates the equipped-slot index bytes `$99FF/$9A00/$9A01/$9A02` when the removed slot position crosses those indices
- it has multiple branches for whether the removed slot matches one of the equipped-slot bytes exactly

That makes the safest current read: `C2:2A3A` is not merely a generic copy helper. It is a transfer/remove/insert helper that preserves the packed inventory plus equipment-slot-index invariants across two character records.

Working name: `TransferInventoryItemBetweenCharactersMaintainingEquipment`.

Source-scaffold promotion split the old broad `C2:2A3A..3008` placeholder into two real source modules:

- `C2:2A3A..2F38` = `TransferInventoryItemBetweenCharactersMaintainingEquipment`
- `C2:2F38..3008` = `InitBattleScripted`, matching `refs/ebsrc-main/ebsrc-main/src/battle/init_scripted.asm`

The exact C1 command labels for the six direct callers remain a separate parser-side naming task.

## Working Names

- `C2:16AD` = `ApplyMusicTrackAndSyncMirror`
- `C2:16C9` = `StopMusicRedirect`
- `C2:16D0` = `PlaySoundAndTickLightWindow`
- `C2:23D9` = `LookupStatusTileValueForHpPpWindow`
- `C2:2474` = `LookupStatusTileWidthOrOffsetForHpPpWindow`
- `C2:24E1` = `ClassifyItemEquipSlotSubtypeOrdinal`
- `C2:2524` = `ClassifyGroupedEquipmentSlotOrdinal`
- `C2:26C5` = `SetCurrent9C88FlagAndRefresh5D64`
- `C2:26E6` = `GetCurrent9C88Flag`
- `C2:26F0` = `FindFirstPartySlotWithStateOne`
- `C2:272F` = `CountPartySlotsNotStateOneOrTwo`
- `C2:277C` = `FindFirstPartyCodeNotStateOneOrTwo`
- `C2:2A2C` = `SaveCurrentGame`
- `C2:2A3A` = `TransferInventoryItemBetweenCharactersMaintainingEquipment`
- `C2:2F38` = `InitBattleScripted`
- `C2:3008` = `SaveAndClearTemporaryPartySourceState`
- `C2:307B` = `RestoreTemporaryPartySourceState`

## Confidence

High confidence:

- `C2:23D9` / `C2:2474` scan the seven-byte `$99DC`-family status slice and feed HP/PP tile layout.
- `C2:26C5` / `C2:26E6` are wrappers over flag id `$9C88`.
- `C2:3008` / `C2:307B` are a matched save/restore pair over `$983A/$983B/$983C/$983E/$9831/$9833` and `$986F`.
- `C2:2A2C` is the save-current-game wrapper over `$B4A1` and `EF:0A4D`.
- `C2:2A3A` maintains both packed inventory bytes and equipped-slot indices.

Medium confidence:

- `C2:16AD` as a music/default-audio state latch wrapper. `$5DD6` is now strong as the current map music track; `$5DD4` remains a softer latched mirror because nearby transition code can reuse it in staged-coordinate contexts.
- the exact semantic names for `$99DC` values `1` and `2`.
- the user-facing reason the `0x1F` command pair needs the temporary `$983A/$983B` source-state save/restore.
