# C2 Window, HPPP, And Menu Selection Helpers `C20266..C2108C`

This pass covers the early bank-`C2` window/HPPP corridor that sits between the global window reset code and the named HP/PP roller includes in `refs/ebsrc-main`.

The useful split is:

- `C2:0266..038A` manages tiny window-title/name buffers and redraws their tile upload copy
- `C2:038B..087B` clears and rebuilds the HP/PP tilemap backing buffer
- `C2:087C..09A0` bridges open text/window redraws and menu cell probing
- `C2:0B65` is the shared directional menu-cursor scanner
- `C2:0F58..108C` is the prelude to the named HP/PP roller: it selects roll deltas, clamps target values, and clears the roll-dirty latch once all party members are settled

## Reference anchors

`refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank02.asm` corroborates the corridor ordering:

- `unknown/C2/C20266.asm`
- `unknown/C2/C20293.asm`
- `unknown/C2/C202AC.asm`
- `text/set_window_title.asm`
- `unknown/C2/C2038B.asm`
- `text/hp_pp_window/draw.asm`
- `unknown/C2/C2077D.asm`
- `unknown/C2/C207B6.asm`
- `text/hp_pp_window/undraw.asm`
- `unknown/C2/C2087C.asm`
- `unknown/C2/C208B8.asm`
- `data/text/name_entry_grid_character_offset_table.asm`
- `data/unknown/C20958.asm`
- `unknown/C2/C209A0.asm`
- `unknown/C2/C20A20.asm`
- `unknown/C2/C20ABC.asm`
- `unknown/C2/C20B65.asm`
- named `text/hp_pp_window/*` digit/tile-buffer helpers
- `unknown/C2/C20F58.asm`
- `misc/reset_hppp_rolling.asm`
- `unknown/C2/C21034.asm`
- `unknown/C2/C2108C.asm`
- `misc/hp_pp_roller.asm`

The community RAM map names `008650-0088DF` as the window statistics table, `0088E4-008957` as the window existence table, `008958` as the current focused window, `0098A4` as the number of player-controlled party members, and `0099CE-009C07` as the character stats table.

## Global Window Reset Prelude

`C2:00D1..00D8` is the small coordinate/config header immediately before the
callable reset routine at `C2:00D9`. The reset body clears the open-window
chain, window-record index table, title-upload slot table, HP/PP tilemap
backing rows, text-entry records, scratch tile rows, text display/sound
latches, and current focus id, then reloads the menu/name-entry mask table
through `C4:3F53` into the `$1AD6` text-tile bitset area.

Follow-up source polish now names those structural tables directly in
`src/c2/c2_00d1_window_reset_initial_coordinate_data.asm`, keeping this
front-door reset path aligned with the later HP/PP, menu-selection, and C4
text-window helper notes.

## Tiny title/name buffer helpers

`C2:0266` copies four 16-bit words from `C3:E40E` into `$8272`. In the ROM bytes those words are `$3A69,$3A6A,$3A6B,$3A6C`, a compact tile-id/attribute run. `C2:0293` clears the same four-word destination. The direct callers match that interpretation: `C2:0266` is reached from `C2:39B4`, while `C2:0293` is called by battle text setup/cleanup paths at `C1:DC46`, `C1:DC98`, and `C2:6175`.

`C2:02AC` is the internal upload/registration side. It maps an input window id through `$88E4` and the selector helper `C0:8FF7` with selector `#$0052`, reaches the window-stat record at `$8650 + offset`, and uses byte `$003B` as a small registered-copy index into the five-word table at `$894E`. If no table slot is assigned, it finds the first `$FFFF` entry, stores the mapped window id there, writes the 1-based slot into `$003B`, and asks `C4:44FB` / `UploadWindowTitleGlyphTiles` to render/upload the source at `$86xx + $3C` to a VRAM destination based on `$7700 + slot * 0x80`.

`C2:032B` writes a nul-terminated string into the mapped window record at `$868C + offset`, capped by the input length in `X`, then calls `C2:02AC` to make the copy visible. Existing notes already hit this through battle PSI/equipment display paths; this note pins the sibling private helper that makes the visible tile upload happen.

## HP/PP tilemap rebuild

`C2:038B` clears the backing tilemap and scratch buffer used by the HP/PP window layer:

- fills `$7E:7DFE..$7E:84FD` with zero through `C0:862E`
- fills `$7E:7F80..$7E:7FBF` from `DATA_C40BE8`, which is all zero in the legacy reference

The only direct callers found by the scanner are `C1:2E37` and `C4:801A`. `C1:2E37` is inside the heavier window tick path, just before `C1:004E`, so this is best read as a reset/rebuild backing-buffer helper rather than a display-list finalizer.

`C2:03C3` is the per-party-member tilemap composer. It takes a party slot in `A`, uses `$986F + slot` to map to a character record at `$99CE`, derives the slot layout from `$98A4`, and writes rows into `$7DFE`. It chooses tile base `$0012` for the current actor stored at `$89CA` and `$0013` for the other party windows, then constructs box edges and the initial HP/PP text tiles around character stats offsets `$43..$4D`.

`C4:3573` is the matching "current actor changed" helper on the bank-`04` side. If `$89CA` already holds a live actor, it first calls `C3:E6F8`, then stores the incoming actor/party index to `$89CA`, waits one frame through `C0:8756`, and clears seven tile words in the window backing range rooted at `$847E`. The offset math uses both the incoming actor and `$98A4`, matching the party-window layout decisions that `C2:03C3` uses. It finishes by setting `$9623 = 1`, so the helper is best read as selecting the focused party HP/PP actor and blanking the old/current actor row region for redraw.

`C2:077D` redraws all dirty party-member windows. It treats `$9647` as a bitmask, scans one bit per player-controlled party member (`$98A4`), and calls `C2:03C3` for each set bit.

`C2:07B6` marks one party-member HP/PP window dirty. It builds a one-bit mask through `C0:923E`, ORs it into `$9647`, immediately redraws that slot through `C2:03C3`, and sets `$9649 = 1` as a global redraw-needed latch. Direct callers include `C1:3032`, `C2:DDA3`, and `C2:E0FE`.

The sibling at `C2:07E1` is the inverse operation: it clears the corresponding `$9647` bit, sets `$9649`, and wipes the 8x7 tile area for that party-member window in `$7DFE`.

`C2:087C` is the frame-facing text/window redraw bridge. If `$89C9` is nonzero it first runs `C2:077D`, then walks the open-window chain rooted at `$88E0`, calling `C1:07AF` on each window id and following each window record's `$8652` next pointer until `$FFFF`.

## Menu cell probing and directional movement

`C2:08B8` classifies a menu cell by reading the current focused window (`$8958`), mapping it through `$88E4` and the `$8650` window record, then computing a tilemap address from row/column inputs. It returns:

- `#$002F` if the tile id masked with `#$03FF` is `#$004F` or `#$0041`
- `#$0040` otherwise

`#$002F` is therefore the "selectable/occupied cell found" response used by the cursor scanner. The ebsrc `NAME_ENTRY_GRID_CHARACTER_OFFSET_TABLE` immediately follows at `C2:0912`; `C2:0958` is a 32-word mask/config table between that grid table and the literal `THE` text data.

`C2:0B65` is the shared directional cursor scanner. It takes the current row/column plus a direction vector in `Y/X/A`-style caller registers, probes candidate cells through `C2:08B8`, wraps according to the current window record dimensions at `$000A/$000C`, and returns either:

- `#$FFFF` when no selectable cell is found
- a packed coordinate where the row/index is in the high byte and the column/index is in the low byte

The xrefs make this role strong: direct callers include the C1 menu directional handlers at `C1:1914`, `C1:192F`, `C1:1CBB`, `C1:1CE8`, `C1:1D12`, `C1:1D3F`, plus file/select-style cursor paths around `C1:E8AE..E914`.

## HPPP roller prelude

`C2:0F58` chooses the HP/PP rolling delta pair. Normally it copies `$9627/$9629` into local `$14/$16`. If byte `$9695` is set, it first runs that pair through `C0:9262` with `Y = 1`, so this is the "scaled/alternate roller step" branch used by `C2:109F`.

`C2:0F9A` clamps pending HP/PP targets for every player-controlled party member. It scans `$986F`, maps each active member to `$99CE + index * 0x5F`, and compares:

- HP-like fields: current `$45`, target `$47`, dirty/status `$43`
- PP-like fields: current `$4B`, target `$4D`, dirty/status `$49`

If a target lags below the live value while the corresponding dirty/status field is active, it raises the target to the live value. It finishes by setting byte `$9696 = 1`, the same latch later tested by `C2:109F`.

`C2:1034` is the "all HPPP rolls settled?" predicate. It returns `1` only when every player-controlled member has both dirty/status fields clear and both current values equal their target values. Any active dirty/status field or mismatched current/target pair returns `0`.

`C2:108C` is the matching latch clearer: it calls `C2:1034` and, if every roll is settled, clears byte `$9696`. Its one direct caller is `C2:609B`.

`C2:109F` is the named HP/PP roller that follows these includes. It is called from `C1:2E14` and `C1:2E44` in the heavier and lighter window tick paths. The early portion picks the current party member from `$986F[$0002 & 3]`, refuses non-party values, then increments/decrements the `$43/$45/$47` and `$49/$4B/$4D` rolling fields using the delta pair from `C2:0F58` or a forced `#$4000/#$0006` pair when `$9696/$9698` demand a fast catch-up.

`C2:0D3F..0F58` is the digit staging layer immediately before that prelude.
It splits a value into three decimal digits at `$8966..$8968`, writes the
three two-row digit tile pairs into the HP/PP tile buffer rooted at `$896D`,
uses `$8975` for the "X" placeholder strip, and exposes the two callable
character wrappers at `C2:0F08` and `C2:0F26` for HP and PP tile-buffer fills.

## Source Polish

2026-05-01 semantic polish promoted the already scaffold-backed source for this
cluster without changing runtime bytes:

- `C2:077D`, `C2:07B6`, `C2:07E1`, and `C2:087C` now name the HP/PP dirty
  party-window mask, global redraw latch, focused party slot, player-count
  bound, and the C2/C1 window redraw/tick helper joins.
- `C2:08B8` and `C2:0B65` now name the current-window record lookup, window
  record stride, tilemap/dimension fields, selectable/blocked menu-cell return
  values, and the no-selection sentinel.
- `C2:09A0` now names the window-record title upload slot, tilemap clear tile,
  C4 free-tile helper, upload-slot table, and redraw-all-window latch.
- `C2:0A20` and `C2:0ABC` now name the managed text-event snapshot layout and
  the window-record fields copied to and from it.
- `C2:0F58`, `C2:0F9A`, `C2:1034`, and `C2:108C` now name the HP/PP roller
  delta pair, scaled-delta flag, roll dirty latch, party slot map, character
  record stride, and HP/PP current/target/dirty fields.
- `C2:0266`, `C2:0293`, `C2:02AC`, `C2:032B`, and `C2:038B` now name the
  default title tile run, registered window-title upload slot, `$8650` window
  record/title-string fields, `$894E` upload-slot table, C4 title glyph upload
  call, and HP/PP tilemap/scratch buffer clear ranges.
- `C2:0D3F..0F58` now names the `$8966..$8968` decimal digit staging bytes,
  HP/PP digit tile-buffer bases, digit tile source offsets, blank/visible digit
  tile offsets, and the HP/PP wrapper entries at `C2:0F08/0F26`.

2026-05-06 follow-up source polish tightened the central composer and its
battle-presentation callers:

- `C2:03C3` now names the party-slot-to-character-id table, character record
  stride/base, HP/PP window option word, current HP/PP and dirty/status fields,
  focused party HP/PP window id, tilemap base, HP/PP tile-buffer row bases, the
  `C0:8F22` text-length helper, and the local `C2:0F08/0F26` HP/PP tile-buffer
  wrappers.
- `C2:DB3F` and `C2:E0E7` now call `C2:07E1` and `C2:07B6` by their HP/PP
  window roles while naming `$ADA4/$ADA6` as the HP/PP box blink
  duration/target pair.
- `C2:00D9` now names the global window/text reset table contracts, including
  the `$88E0/$88E2` open-window chain, `$88E4/$8650` window-record map,
  `$894E` title-upload slots, `$89D4` text-entry records, `$8958` focus id,
  and the `C4:3F53` `$1AD6` mask-table reload.
- `C2:16D0`, just outside this early corridor, now uses the
  `PlaySoundAndTickLightWindow` source label for the text-command sound/effect
  wrapper that queues the sound through `C0:ABE0` and immediately runs the
  shared `C1:2E42` light window tick.
- The battle-start back-half completion loop now calls `C2:108C` by its
  `ClearHpPpRollDirtyLatchIfSettled` contract while waiting for HP/PP rolls to
  settle, then calls `C2:0293` as `ClearDefaultTitleUploadTiles` during the
  display cleanup tail.

## Working Names

These are proposed local names, intentionally phrased as behavior names until we have source-level integration:

- `C2:0266` = `LoadDefaultTitleUploadTiles`
- `C2:0293` = `ClearDefaultTitleUploadTiles`
- `C2:02AC` = `RegisterAndUploadWindowTitleBuffer`
- `C2:032B` = `WriteWindowTitleAndUpload`
- `C2:038B` = `ResetHpPpTilemapBuffers`
- `C2:03C3` = `ComposePartyMemberHpPpWindowTiles`
- `C2:077D` = `RedrawDirtyPartyHpPpWindows`
- `C2:07B6` = `MarkAndRedrawPartyHpPpWindow`
- `C2:07E1` = `ClearPartyHpPpWindowTiles`
- `C2:087C` = `RefreshDirtyHpPpAndOpenTextWindows`
- `C2:08B8` = `ClassifyMenuTileForCursorScan`
- `C2:0958` = `MenuOrNameEntryMaskTable`
- `C2:09A0` = `CloseAndClearCurrentWindowTilemap`
- `C2:0B65` = `FindNextSelectableMenuCell`
- `C2:0D3F` = `SplitValueIntoThreeDecimalDigitsAt8966`
- `C2:0D89` = `FillHpPpTileBufferX`
- `C2:0DC5` = `FillHpPpTileBuffer`
- `C2:0F08` = `FillCharacterHpTileBuffer`
- `C2:0F26` = `FillCharacterPpTileBuffer`
- `C2:0F58` = `SelectHpPpRollDelta`
- `C2:0F9A` = `ClampHpPpRollTargetsToLiveValues`
- `C2:1034` = `AreAllHpPpRollersSettled`
- `C2:108C` = `ClearHpPpRollDirtyLatchIfSettled`
- `C4:3573` = `SelectFocusedPartyHpPpActorAndBlankRow`

## Confidence

High confidence:

- `$88E4/$8650/$8958` are the window existence/current-window/stat structures
- `$98A4` bounds the player-controlled party-member loops
- `$986F` maps visible party slots to character ids
- `$99CE` is the character stats table base
- `$9647` is a per-party-member HP/PP redraw bitmask
- `$9649` is a global redraw-needed latch for this corridor
- `C2:08B8` and `C2:0B65` form a probe/scan pair for menu cursor movement
- `C2:1034` and `C2:108C` are settled-check/latch-clear helpers for the HP/PP roller

Still open:

- the exact semantic names for bytes `$9695/$9696/$9698`
- whether `C2:0958` belongs to name-entry, menu-cell masking, or a shared text-grid config family
- the exact tile meanings of `#$004F`, `#$0041`, `#$002F`, and `#$0040`; the behavior is pinned, but the display vocabulary still needs a tile table cross-reference
