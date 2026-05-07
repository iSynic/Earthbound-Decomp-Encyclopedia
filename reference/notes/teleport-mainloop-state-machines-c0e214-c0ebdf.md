# Teleport Mainloop State Machines (`C0:E214-C0:EBDF`)

This note continues the teleport/freezing frontier from `notes/teleport-freeze-vector-frontier-c0dd0f-c0e196.md`.

Reference corroboration:

- `refs/ebsrc-main/ebsrc-main/include/symbols/bank00.inc.asm` gives the semantic name `TELEPORT_MAINLOOP` for this strip's main dispatcher at `C0:EA99`.
- `refs/ebsrc-main/ebsrc-main/src/bankconfig/common/ram.asm` labels `$9F3F+` as the `PSI_TELEPORT_*` state block: destination/style/state at `$9F3F/$9F41/$9F43`, fixed-point speed at `$9F45`, speed X/Y at `$9F49/$9F4D`, next X/Y at `$9F51/$9F55`, success-screen motion at `$9F59-$9F5F`, and beta arc fields at `$9F61-$9F69`.
- Reference callers include `battle/init_overworld.asm` and `battle/init_scripted.asm`, which `JSL TELEPORT_MAINLOOP` after battle/scripted transitions.

## Ring Cursor And Object Speed Helpers

`C0:E214` updates the per-object cursor byte stored inside the object metadata block at `$99CE + object*$5F + $3D`. It takes the old cursor in `X`, a slot-like value in `A`, and compares against the party count byte at `$988B`. If teleport phase high word `$9F47` is clear, it returns the original `Y`; otherwise it calls `C0:3EC3` with `A=slot`, `X=6`, and `$0E=2`, which matches the surrounding entity-position machinery. The returned low byte becomes the next `$5156` ring index used by the restore callbacks below.

`C0:E254` writes a countdown-like value to `$0F12` for transition object slots `$18-$1C`. It computes `max(1, #$000C - $9F47)` and stores that same value into each slot's `$0F12`, so the visible object cadence tightens as the teleport speed/phase high word grows.

`C0:E44D` is the manual success-screen adjustment helper. Unless teleport style `$9F41` is `4`, it reads input mirror `$0065` and nudges `$9F67/$9F69` one unit for the four directional bits `#$0100/#$0200/#$0400/#$0800`. In the `PSI_TELEPORT_*` label set those are the beta X/Y adjustment fields, so this is user steering for the beta-style travel path.

`C0:E48A` seeds `$9F4B/$9F4F` with a small signed vector (`+/-5`) from facing `$987F`. This is called when the beta progress terminal condition sets state `$9F43 = 1`, giving the post-success screen drift direction.

## Teleport Movement Callbacks

`C0:E28F` is the alpha/straight-style movement callback installed by the mainloop for styles `1` and `5`. It:

- Sets `$9885=1`, refreshes facing through `C0:404F`, and avoids immediately reversing the previous facing `$987F` when possible.
- Calls `C0:DF22` to derive `$9F49/$9F4B` and `$9F4D/$9F4F` from current facing and `$9F45/$9F47`.
- Computes next player fixed-point coordinates into `$9F51/$9F53` and `$9F55/$9F57`.
- Uses `C0:5FF6` and the two-point footprint check `C0:DED9`; collision sets teleport state `$9F43=2`.
- Commits `$9875/$9877/$9879/$987B` only while state is not failure `2`.
- Calls `C0:400E` to recenter/refresh screen coordinates, snapshots the state through `C0:E196`, and updates the object cadence through `C0:E254`.
- Marks success `$9F43=1` after `$9F47` grows past `9`.

`C0:E516` is the beta/curved-style movement callback installed for styles `2` and `4`. It uses `C4:1FFF` with `$9F61/$9F63` to derive a trigonometric offset, sign-extends the high bytes into target map coordinates `$9F53/$9F57`, then runs the same collision gates as the alpha callback. For style `2`, `$9F61 += #$0A00` and `$9F63 += #$000C`; otherwise `$9F65 += #$0020`, `$9F61 += $9F65`, and `$9F63 += #$0010`. Style `2` succeeds once `$9F63 > #$1000`; the other beta path succeeds once `$9F65 > #$1800`.

`C0:E674` is the post-success drift callback. It applies the current direction-derived speed vector to both live player fixed-point coordinate pairs (`$9875/$9877` and `$9879/$987B`), separately applies `$9F59/$9F5D` to the success-screen coordinate pair `$9F5B/$9F5F`, calls `C0:400E`, and records another `$5156` ring snapshot through `C0:E196`.

`C0:E776` is a faster straight-line exit callback. It mirrors the live-coordinate vector update from `C0:E674`, then uses `C0:9086` on `$9F45/$9F47` with scale `2` and subtracts the result from the screen Y coordinate passed to `C0:400E`. It also snapshots via `C0:E196` and refreshes object cadence through `C0:E254`.

## Ring Restore Callbacks

`C0:E3C1` and `C0:E6FE` are close siblings. Both locate the current object metadata block via `$0E9A[current] * $5F + $99CE`, read the ring cursor stored at metadata offset `$3D`, scale it by 12 bytes into the `$5156` snapshot ring, and restore position/state fields:

- `$0B8E/$0BCA` from ring bytes `0/2`.
- `$2BAA` footprint mask from ring byte `4`.
- Entity draw/sprite state through `C0:7A56` from ring byte `6`.
- `$2AF6` facing from ring byte `8`.

After restoring, they call `C0:E214` and write the returned low byte back to metadata offset `$3D`. `C0:E3C1` keeps a copy of `$0E5E[current]` in `$10`; `C0:E6FE` is the same restore path with slightly different temporary-register arrangement and is paired with `C0:E776` by the success/failure setup.

`C0:E979` is an empty `REP #$31; RTL` callback. `C0:E97C` is a small refresh callback for the current slot: it recomputes `$2BAA[current]` from live `$0B8E/$0BCA` via `C0:5F33`, then calls `C0:7A56` with sprite-state X set to `FFFF`. `C0:E9BA` installs `C0:E979/C0:E97C` as a short-lived task pair after marking transition object flags.

## Success And Failure Setup

`C0:E815` handles successful arrival setup unless style `$9F41` is `3`. It marks slots `$18-$1D` by writing `#$8000` into `$289E`, installs `C0:E674` as the active callback with `C0:E3C1` as its restore callback via `C4:2F45`, copies the current `$9F4B/$9F4F` vector words into `$9F59/$9F5D`, copies player screen coordinates into `$9F5B/$9F5F`, starts a short visual/sound cue through `C0:887A`, then blocks in `C0:DD0F` until the frame pump catches up.

`C0:E897` handles the post-arrival or failure branch. For style `3`, it recenters on `$9877/$987B`, triggers `C0:886C(1)`, waits through `C0:DD0F`, and jumps to the common tail. For other styles it clears six object metadata words at `$9A05 + index*$5F`, rebinds party object draw state through `C0:7A56`, seeds `$9F45=0`, `$9F47=8`, `$987F=6`, and `$9F43=3`, installs `C0:E776/C0:E3C1`, calls `C0:DE16`, plays cue `#$87`, waits 30 frames, then pumps frames until `$9F47` decays to zero.

`C0:E9BA` is the failure pause/hold path used when the mainloop sees state `$9F43=2`. It sets `$B4B6=1`, plays cue `#$0E`, sets bit `#$8000` in `$1002` for transition slots `$18-$1D`, installs the no-op/refresh pair `C0:E979/C0:E97C`, sets byte `$9840=1`, pumps 180 frames through the standard wait helpers, then clears `$9840` and `$B4B6`.

`C0:EA3E` unconditionally ORs `#$C000` into `$10B6` for slots `0-$16`; `C0:EA68` does the same only when those high bits are not already both set. The mainloop uses `C0:EA3E` for one-time entry and `C0:EA68` inside the active frame pump, so these are party/NPC interaction suppression helpers during teleport.

## Main Dispatcher

`TELEPORT_MAINLOOP` at `C0:EA99` is the top-level teleport state machine. It starts with `C0:ABC6`, one frame tick via `C0:8756`, global interaction suppression (`C0:EA3E`), sets `$5DBA=1`, clears `$9F45/$9F47/$9F43`, calls `C0:7C5B`, and initializes transition objects with `C0:DE46`.

It dispatches by style `$9F41`:

- Style `1` and `5`: install `C0:E28F/C0:E3C1`.
- Style `2`: install `C0:E516/C0:E3C1`.
- Style `3`: skip movement and force success state `$9F43=1`.
- Style `4`: install `C0:E516/C0:E3C1`.

For styles other than `3`, it plays cue `#$0D`, then pumps frames with `C0:88B1`, `C0:9466`, `C0:EA68`, `C0:8B26`, and `C0:8756` until `$9F43` becomes nonzero. State `1` runs the success setup (`C0:E815`), prepares the destination via `C0:DD79`, then runs `C0:E897`; state `2` runs the failure hold (`C0:E9BA`) and waits ten more pumped frames via `C0:DD2C`.

The common tail reinstalls the normal overworld callbacks `C0:5200/C0:4D78` through `C4:2F45`, unfreezes transition slots with `C0:DE7C`, calls `C0:9451`, and clears `$5DBA`, `$9F45`, `$9F47`, `$5D58`, and `$9F3F`.

## Working Names

- `C0:E214` = `AdvanceTeleportObjectSnapshotRingCursor`
- `C0:E254` = `UpdateTeleportTransitionObjectCadence`
- `C0:E28F` = `TickTeleportStraightMovementCallback`
- `C0:E3C1` = `RestoreTeleportObjectFromSnapshotRing`
- `C0:E44D` = `ApplyTeleportBetaManualSteering`
- `C0:E48A` = `SeedTeleportPostSuccessDriftVector`
- `C0:E516` = `TickTeleportCurvedMovementCallback`
- `C0:E674` = `TickTeleportPostSuccessDriftCallback`
- `C0:E6FE` = `RestoreTeleportExitObjectFromSnapshotRing`
- `C0:E776` = `TickTeleportStraightExitCallback`
- `C0:E815` = `SetupTeleportSuccessfulArrival`
- `C0:E897` = `FinalizeTeleportArrivalOrFailure`
- `C0:E979` = `TeleportNoOpCallback`
- `C0:E97C` = `RefreshTeleportCurrentSlotPose`
- `C0:E9BA` = `HoldTeleportFailureState`
- `C0:EA3E` = `SuppressInteractionsForTeleportSlots`
- `C0:EA68` = `EnsureTeleportSlotInteractionSuppression`
- `C0:EA99` = `TeleportMainloopStateMachine`
