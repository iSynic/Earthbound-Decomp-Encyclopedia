# C2 Battle-Start Payload Join Runtime Polish

Primary queue context: `notes/c2-runtime-semantic-polish-plan.md`,
`notes/c2-ef-battle-text-contract-workahead.md`,
`notes/source-readiness-triage.md`, and `notes/project-status.md`.

## Scope

This pass covers the battle-start controller and instant-win text payload joins
in:

- `src/c2/c2_5024_run_battle_start_candidate_controller_front.asm`
- `src/c2/c2_5afb_run_battle_start_candidate_controller_back.asm`
- `src/c2/c2_4a80_populate_candidate_pool_from_variable_sources.asm`
- `src/c2/c2_311b_run_battle_start_present_and_message_controller.asm`
- `src/c2/c2_6189_fill_instant_win_tile_buffer_and_upload.asm`

The edit is semantic source polish only. It promotes local aliases, constants,
and comments while preserving byte-equivalence.

## Promoted Contracts

- `C1:DC1C` is named as the direct `$0E/$10` battle-text pointer dispatch.
- `C1:DC66` is named as the `$12/$14` substitution-payload display wrapper.
- `C1:DD7C` is named as the byte-substitution setter for `$9D11`.
- The battle-start front half now names `EF:78F7`, `EF:84F3`, and `EF:8511`
  as the Sensei Monster and player-flee result scripts.
- The battle-start back half now names the C8 PSI-cannot script, EF target/
  status/victory scripts, and the `EF:7BDF` present script.
- The instant-win handler now names `EF:7A28` as the forced-win script and
  reuses the `EF:7BDF` present script for the optional present item byte.
- Follow-up action-table polish now names the local `D5:7B68` row root/bank,
  the `0x0C` row size, the `+2/+3/+4/+8` row fields used by battle-start, and
  the `C1:DD9F` primary-message lane versus the later companion-payload lane.
- Result-corridor follow-up now carries source-backed helper names into the
  instant-win handler and battle-start cleanup tail: `C1:DD47` opens the battle
  text window, `C2:B930` exports battle selection snapshots, `C2:BAC5` counts
  filtered second-stage rows, and `C2:BC5C` clears inactive source-entry
  live-slot transient fields.
- Presentation follow-up now names the battle-start back half's pre-action
  `C2:FEF9` palette loader/dimmer calls, `C1:2DD5` frame ticks, `C1:DD3B`
  selected-row presentation refresh, and `C1:DD59` battle-text wait join.
- Variable-source follow-up now carries those same presentation/frame names into
  `C2:4A8A`: candidate-pool confirmation refreshes the selected-row
  presentation through `C1:DD3B`, ticks the window through `C1:2DD5`, runs the
  battle-background frame lane through `C2:DB3F`, enters C1 enemy-select mode
  through `C1:E1A5`, and opens the final present/result text window through
  `C1:DD47`. The `C2:311B` menu/present controller now names its opening
  `C2:FEF9` palette load/dim call as the same `LoadOrDimBattlePaletteSet`
  contract.
- Variable-source overlay follow-up: the same `C2:4A8A` interactive loop now
  calls `C4:A67E` as `StartBattleOverlayScriptState` when `$006D & 0x8000`
  advances the `$AA72/$AA74` overlay mode/profile pair.
- STEAL/result-cleanup follow-up now names the battle-start front/back helper
  joins that were already source-backed elsewhere: `C2:4316` selects a
  stealable candidate for action `0x42`, `C2:4348` guards the pending stolen
  item byte at selected-row `+8`, `C2:437E` applies the pending stolen item slot
  when the end-state route still permits it, `C1:DDCC` selects the party-member
  presentation, `C2:AF1F` snapshots/restores battler normalization context,
  `C2:108C` clears the HP/PP roll dirty latch once settled, and the completion
  cleanup calls `C2:0293` / `C2:E0E7` by their title-tile and visual-flash
  reset contracts.

## Payload Joins

The newly named `BattlePresentItemByte` paths are the concrete C2 side of the
byte-substitution bridge:

- `C2:4A8A` preserves the enemy record dropped-item byte from D5 record
  offset `+0x58`, applies the D5 drop-rate byte at `+0x57`, and falls back to
  the UFO-specific present table at `C2:3109` when the ordinary drop byte is
  empty.
- `BattlePresentItemByte` (`$AA10`) is loaded as an 8-bit value by the
  battle-start and instant-win present paths.
- `C1:DD7C` stages it into `$9D11`.
- `EF:7BDF` (`MSG_BTL_PRESENT`) later consumes it through the `0x19 0x1F`
  byte-substitution command before printing the item name.
- `C2:8881` uses the same byte slot for the Check Present / Spy companion
  script at `EF:7DD5`; that branch first asks the C4 inventory-room helper
  whether fixed recipient id `3` can carry the item, then clears the slot after
  display.

The victory scripts continue to use `C1:DC66` with `$12/$14` populated from the
accumulated result pointer/value pair, keeping them separate from direct
`C1:DC1C` status-result text.

Reward/result follow-up now names the battle-start back and instant-win helper
joins that shape the same result lane: `C2:281D` / `DepositIntoAtm` converts
the money amount before adding it to the `$98B9/$98BB` bank-deposit
accumulator, and `C1:D9E9` / `AwardExperienceToCharacter` applies the computed
EXP amount to each eligible active battler row. The instant-win opening also
names `C2:E9ED` as the battle overlay/layer-effect reset helper before the
forced-victory presentation.

The instant-win forced-victory path now calls the same named
`ExportBattleSelectionSnapshot` and `CountFilteredSecondStageBattlerRows`
helpers used by battle-start and target-selection setup before it builds the
reward pointer/value pair for `EF:7A28`.

## Action-Table Text Lane

`D5:7B68` is now treated consistently as a `0x0C`-byte battle-action row table
inside the C2 battle-start front/back halves and the late selected-row nested
action controller:

- row `+2` gates battle-start action-type/presentation branches;
- row `+3` is the PP-cost byte checked before the C8 PSI-cannot script;
- row `+4` is the primary action text far pointer staged into `$0E/$10` and
  displayed through `C1:DD9F`;
- row `+8` is the companion action payload pointer applied after target
  validation.

This keeps the C1 `DD9F` wrapper as the explicit current-action text lane and
separates it from ordinary direct text (`DC1C`) and substitution payload
(`DC66`) callers.

The pre-action presentation category at row `+2` now dispatches through the
named `C2:FEF9` / `LoadOrDimBattlePaletteSet` helper before the controller
waits the fixed presentation-delay frame count through `C1:2DD5` /
`WindowTick`.

The surrounding candidate-source loop at `C2:4A8A` now uses the same lifecycle
vocabulary when the generated party/enemy candidate pool reaches the
interactive selection frame. This keeps the pool producer, enemy-select C1
join, and post-selection present text setup tied to one battle-start contract
instead of leaving those calls as raw display helpers.

Its overlay branch now uses the C4 source-facing name for `C4:A67E`, making the
`$AA72/$AA74` counters read as overlay script mode/profile state for the
interactive battle-start presentation loop.

The STEAL row (`0x42`) now reads as a full argument lifecycle in the
battle-start front/back sources: select a candidate item into the action
argument, validate that argument against the current stealable-item list before
text/payload work, and run the end-state stolen-slot applicator only on the
cleanup paths that can still commit it.

Front/back controller follow-up: the front half now names the battle-start
present/message menu join (`C2:311B`), the C1 battle-text wait and focused
HP/PP-row clear redirects (`C1:DD59` / `C1:DDD3`), the C1 text-entry helper
redirect at `C1:DD53`, the ranked battler ordinal writer (`C4:A228`), and the
two target-context helper entries `C2:3E32` / `C2:4009`. The back half now
calls `C2:0F9A` as `ClampHpPpRollTargetsToLiveValues` at the monsters-win,
player-win, and cleanup-tail completion branches, keeping battle-start result
flow tied to the HP/PP roller target contract.

Cross-module tail follow-up: the battle-start sources now expose the main
controller re-entry points that earlier appeared only as raw local jumps.
`C2:48E0` is the shared battle-start visual-state and candidate-buffer reset
after the battle group resource pointers have been staged, `C2:4B4A` is the
variable-source scan completion check, `C2:4CEF` begins the reward/present
setup path, and `C2:4FCF` seeds the status-row/render-order prelude. The front
controller now jumps to the back-half result tails by name: `C2:5EF7` resolves
battle-start completion, `C2:6081` either continues result flow or promotes the
next selected row, `C2:6088` waits for text before the shared tail, and
`C2:6093` clamps HP/PP roll targets before waiting for the dirty latch to
settle.

Present/menu follow-up: the `C2:311B` controller now names the EF meter/audio
helpers and C2 title-tile setup it already depended on. Menu entry calls
`EF:0262` as `SetHalfHpPpMeterSpeed`, menu exits call `EF:026E` as
`ResumeMusic`, and the Goods branch calls `C2:0266` as
`LoadDefaultTitleUploadTiles` before entering the battle item-selection loop.
The same controller now names its debug-only C1 joins for the hidden battle
menu shortcuts: `C1:3E7A` / `RunDebugSetCharacterLevelPrompt` and `C1:3EE7` /
`RunDebugGoodsGrantViewer`.

## Evidence Inputs

- `notes/c2-ef-battle-text-contract-workahead.md`
- `notes/class2-ufo-present-message-family.md`
- `notes/class2-battle-text-cluster-overview.md`
- `refs/EB-M2-Listing-v1/US/bank08.txt`
- `refs/EB-M2-Listing-v1/US/bank2F.txt`

## Validation

Future implementation gates remain the normal C2 scaffold and byte-equivalence
checks:

```powershell
python tools\build_source_bank_scaffold.py --bank C2
python tools\validate_source_bank_byte_equivalence.py --bank C2 --module all --combined --scaffold src\c2\bank_c2_helpers_asar.asm --strict
```
