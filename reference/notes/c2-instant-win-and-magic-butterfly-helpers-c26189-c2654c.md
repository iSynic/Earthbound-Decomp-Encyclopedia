# C2 instant-win and Magic Butterfly helpers

This note covers two C2 unknowns that sit next to already named battle/event routines in the ebsrc reference tree:

- `C2:6189`, included immediately before `battle/instant_win_handler.asm`
- `C2:654C`, exposed only through the `EVENT_UNKNOWN_C2654C` action-script macro used by Magic Butterfly script `034`

Both routines are small, but they are useful anchors because they connect C2 battle-side behavior to C0 rendering/upload helpers and to event script control flow.

## Working Names

- `C2:6189` = `FillInstantWinTileBufferAndUpload`
- `C2:654C` = `RunMagicButterflyPpRestoreAnimation`

Source-scaffold promotion:

- `C2:6189..654C` is now decoded source in `src/c2/c2_6189_fill_instant_win_tile_buffer_and_upload.asm`.
- `C2:654C..6BFB` is now decoded source in `src/c2/c2_654c_run_magic_butterfly_pp_restore_animation.asm`.
- Both modules validate in the combined C2 scaffold: `C2 byte-equivalence: OK, 233 module(s), 0 mismatch(es).`
- The `C2:6189` source emission requires forced 16-bit accumulator state at `C2:651F` and `C2:652D`, where external text helpers return into 16-bit local code.
- The `C2:654C` source emission requires forced 16-bit accumulator state at `C2:6ADB` and `C2:6B95`, branch-join labels in helper routines that otherwise inherit the wrong 8-bit accumulator state from neighboring call paths.
- Follow-up polish in `C2:654C` now names the Magic Butterfly PP restore
  amount, party-slot scan count, party PP target/max-PP fields, visual pass
  counts, and the embedded `C2:698B` helper that returns the `D5:7B68` action
  type byte for a caller-provided action id.
- Bounded-random follow-up: the local `C2:69F8` scaler now names the C0
  multiply and 32-bit right-shift helpers it uses to compute
  `floor(random_byte * limit / 256)` for `C2:6A2D` / `GetRandomBelow`.

## `C2:6189` - instant-win tile-buffer fill/upload helper

Suggested working name: `Fill0200WithWordAndUploadInstantWinTileBuffer`

Direct callers:

- `C2:61DD`
- `C2:61E3`
- `C2:61E9`
- `C2:61F9`

All direct callers are inside `INSTANT_WIN_HANDLER` (`C2:61BD`). The routine takes a word in `A`, stores it across the entire 512-byte local buffer at `$0200`, then calls the C0 render/upload helpers used by the sudden-victory transition:

```asm
; A = fill word
STA $06
LDX #$0000
.loop
LDA $06
STA $0200,X
INX
INX
CPX #$0200
BNE .loop

SEP #PROC_FLAGS::ACCUM8
LDA #$18
JSL UNKNOWN_C0856B
REP #PROC_FLAGS::ACCUM8
JSL UNKNOWN_C08756
RTS
```

`INSTANT_WIN_HANDLER` calls this helper with `0x03E0`, `0x001F`, `0x7C00`, and finally `0x0000`. Those are full-buffer word fills used while the instant-win presentation flashes/fades before the handler transitions into its reward flow.

The surrounding named handler also:

- plays the sudden-victory music
- clears battle overlay/layer-effect state through `C2:E9ED` /
  `ClearBattleOverlayAndResetLayerEffects`
- copies graphics/tile data through C0 buffer helpers
- opens the battle text window through `C1:DD47` / `OpenBattleTextWindow`
- caches battle money/EXP/drop scratch values
- exports party-side battle selection snapshots through `C2:B930` /
  `ExportBattleSelectionSnapshot`
- counts filtered second-stage battler rows through `C2:BAC5` /
  `CountFilteredSecondStageBattlerRows`
- converts the reward money through `C2:281D` / `DepositIntoAtm` before adding
  it to `$98B9/$98BB`
- rebuilds/reset battler state
- awards EXP through `C1:D9E9` / `AwardExperienceToCharacter` and handles item
  drops
- restores/returns music

So `C2:6189` should be understood as a presentational subroutine of the instant-win handler, not as independent battle logic.

## `C2:654C` - Magic Butterfly PP restore and animation helper

Suggested working name: `MagicButterflyRestorePartyPpTargetsAndAnimate`

Direct JSL/JSR callers: none found.

Raw/pointer xrefs:

- `C3:DF6A`, as an action-script callroutine pointer

Reference-script xref:

- `refs/ebsrc-main/ebsrc-main/src/data/events/scripts/034.asm`

The reference event macro `EVENT_UNKNOWN_C2654C` expands to `EVENT_CALLROUTINE UNKNOWN_C2654C`, and script `034` is the Magic Butterfly event. The script plays the Magic Butterfly sound effect, moves the butterfly away, invokes this C2 routine, yields to text, and halts.

The helper has two major halves.

First, it performs two visual passes:

- calls `UNKNOWN_C0ABE0` with `0x24`
- copies 512 bytes from `$7F0000` into local `$0200` through `UNKNOWN_C08EED`
- fills `$0200..$03FF` with `0x5D70`
- calls `UNKNOWN_C496E7` with `A=-1`, `Y=0x0C`
- advances twelve frames through `UNKNOWN_C426ED` and `UNKNOWN_C08756`
- calls `UNKNOWN_C49740`

Second, it iterates party slots `$986F[0..5]` and restores PP targets for selected character ids:

- accepts party ids `1`, `2`, and `4`
- computes the `PARTY_CHARACTERS` struct base as `(party_id - 1) * 0x5F`
- adds `0x14` to `char_struct::current_pp_target`
- clamps the new target to `char_struct::max_pp`

Relevant WRAM fields:

- `$99DA` = `PARTY_CHARACTERS + 0x0C`, `max_pp`
- `$9A1B` = `PARTY_CHARACTERS + 0x4D`, `current_pp_target`

The party-id filter is preserved as observed from the ROM/reference disassembly. The routine is therefore best named around its concrete event behavior rather than a generic "restore PP" label: it is the Magic Butterfly event's PP-target restoration plus its accompanying C4/C0 visual sequence.

The source also contains a small local helper at `C2:698B` that converts a
`D5:7B68` action id into the action descriptor type byte at row `+0x02`. That
helper now uses the shared battle-action table vocabulary rather than a raw
`$D57B68` read, keeping this event-facing module aligned with the battle-start
and selected-row action-table consumers.

The bounded-random helper pair at `C2:69F8` and `C2:6A2D` is also now clearer:
`C2:6A2D` draws a random byte, then `C2:69F8` multiplies that byte by the
caller limit and shifts the 32-bit product right by 8. The result is the
bounded value consumed by target selection, item drops, and several status or
damage chance paths that call `GetRandomBelow`.

## Relation to instant-win check

`INSTANT_WIN_CHECK` is already named at `C2:6634`. It is called from the overworld battle initializer in C0:

- `INIT_BATTLE_OVERWORLD` calls `INSTANT_WIN_CHECK`
- if the result is nonzero, it calls `INSTANT_WIN_HANDLER`
- it then clears `BATTLE_MODE`

This confirms the `C2:6189` helper's role as an implementation detail of the named instant-win path.
