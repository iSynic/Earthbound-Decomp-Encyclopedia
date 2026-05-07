# Current-Position Music Refresh `C0:68F4..C0:6A1B`

This note ties the C0 map-position music refresh chain to the C4 `ChangeMusic`
loader and the small C0 APU command leaves.

## Main Result

The current best source contract is:

- `C0:68F4` = `RefreshCurrentPositionTransitionContext`
- `C0:69AF` = `ApplyCurrentPositionMusicAndSfx`
- `C0:69ED` = `ChangeMusicFromCurrentTrackLatch`
- `C0:69F7` = `Get_CurrentPositionMusicTrack`
- `C0:6A07` = `Apply_CurrentPositionMusicTrack`

`C0:68F4` resolves the active door/destination record for an input position,
stores the selected destination pointer in `$5E38/$5E3A`, stores the current
map music track in `$5DD6`, and queues APUIO1 cue `2` through `C0:AC0C` when
the music track changed and `$5DDA` is not suppressing the cue.

`C0:69AF` commits that resolved context: if `$5DD6 != $5DD4`, it mirrors
`$5DD6 -> $5DD4`, calls C4 `ChangeMusic($5DD6)`, then reads destination-record
byte `+3` and sends it through `C0:AC0C`.

`C0:69F7` is the read-only current-position wrapper used by restore-default
music callers. `C0:6A07` is the sibling that immediately applies the current
position's music through `ChangeMusic`.

## Field Roles

- `$5DD6` is strong as the current map music track.
- `$5DD4` is the latched map-music mirror for duplicate-change suppression.
- `$5DDA` suppresses the pre-change APUIO1 cue during guarded refreshes.
- `$5E38/$5E3A` hold the selected destination record pointer used by the later
  commit helper.
- `$B549` gates auto-sector music refresh from the overworld tick.

## Caller Chain

`C0:5238` runs after the player-position snapshot tick. It compares the high
bytes of `$9877/$987B` against `$5D5C/$5D5E`; when they change and `$B549 != 0`,
it calls `C0:3C25`.

`C0:3C25` sets `$5DDA = 1`, resolves the current-position context through
`C0:68F4`, waits one frame if the track changed, applies the new music/SFX
through `C0:69AF`, then clears `$5DDA`.

The bicycle transition pair uses the same latch deliberately:

- `GET_ON_BICYCLE` plays track `$52` through `ChangeMusic` and disables
  auto-sector refresh through `C4:FD45(0)`.
- `Restore_LeaderEntityFromBicycleMode` reenables auto-sector refresh through
  `C4:FD45(1)` and, when not blocked by transition flags, reapplies the
  current-position music through `C0:6A07`.

## APU Command Leaves

The source now names the tiny C0 audio leaves in the same vocabulary:

- `C0:ABBD` writes the low byte of `A` to APUIO0 as the music/driver command.
- `C0:ABC6` sends command `0`, waits for APUIO0 to acknowledge `0`, and
  invalidates the C4 current-track latch at `$B53B`.
- `C0:ABE0` queues nonzero sound IDs in the toggled `$1AC2` ring, while `A == 0`
  sends fixed APUIO3 cue `$57`; C4 `ChangeMusic` uses this cue before most
  non-Sound-Stone track changes.
- `C0:AC0C` sends APUIO1 commands with a toggling `$80` bit from `$1ACB`.

## Validation

The source-only semantic pass validates with:

```powershell
python tools\build_source_bank_scaffold.py --bank C0
python tools\validate_source_bank_byte_equivalence.py --bank C0 --module all --combined --scaffold src\c0\bank_c0_helpers_asar.asm --strict
```
