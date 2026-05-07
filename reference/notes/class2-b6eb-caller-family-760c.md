# Class2 B6EB Caller Family 760C

This note captures the current source-backed read on the `C2:760C` caller of
local `C2:B6EB`.

See also [class2-local-enemy-id-to-battler-init-chain.md](notes/class2-local-enemy-id-to-battler-init-chain.md).
See also [class2-b6eb-caller-family-4dxx.md](notes/class2-b6eb-caller-family-4dxx.md).
See also [c2-late-selected-row-runtime-polish.md](notes/c2-late-selected-row-runtime-polish.md).
See also [c2-late-status-runtime-polish.md](notes/c2-late-status-runtime-polish.md).

## Working Names

- `C2:7550` = `StartSelectedBattlerCollapseAfflictionPath`
- `C2:7680` = `DisplayEnemyDeathText`
- `C2:77CA` = `RunClass2LateSelectedRowController`
- `C2:B6EB` = `InitializeEnemyBattlerStatsFromEnemyId`

## Main Result

The `760C` caller is now best treated as the companion rebuild branch inside the
selected-battler collapse/affliction controller, not as battle-start enemy-group
initialization.

The immediate local shape is:

- `C2:7550` receives a selected battler row base in `A`
- the startup path can scan six upstream source entries
- when it finds a matching neighbor affliction byte `+0x1E == 2`, it rebuilds
  scratch battler base `$A180` through `C2:B6EB` with enemy id `0xD5`
- it mirrors the route through `$A18D/$A18F`
- `C2:77CA` later repeats the same D5-tagged cleanup/rebuild pattern from the
  late selected-row controller

That makes the call site a runtime reinitialization helper for the collapse or
companion route rather than an ordinary encounter setup loop.

## Why It Stays Separate From 4Dxx

The `4Dxx -> 4Fxx` family consumes battle-start enemy ids, initializes enemy
battler rows, prints encounter text, and walks start-of-battle status messages.

The `760C` family instead sits after selected-row collapse state has already
been installed:

- it is entered from the selected-row controller around `C2:7550`
- it depends on affliction/substate bytes near `+0x1D/+0x1E`
- it uses the special enemy id `0xD5`
- it writes the companion scratch row at `$A180`
- it immediately rejoins death-text or late-controller presentation flow

Those are different enough that one shared `B6EB` callee should not collapse
the two caller families into one semantic bucket.

## Source-Backed Contract

The current source polish promotes the following local vocabulary:

- `$9FAC` = battlers table base
- `0x4E` = battler row size
- `+0x0C` = consciousness/active byte
- `+0x0E` = ally-or-enemy byte, reused here as the startup-vs-late route gate
- `+0x0F` = npc id / route byte
- `+0x1D/+0x1E` = affliction/substate bytes used by the hard-collapsed route
- `$A180` = companion scratch battler base
- `$A18D/$A18F` = companion seed active/id mirror bytes

The exact gameplay name of the `0xD5` companion remains provisional, but the
local mechanism is now clear: selected-row collapse flow may clear or rebuild a
scratch battler record through the normal enemy-data initializer.

## Current Safest Takeaway

`C2:760C` is no longer just an unresolved `B6EB` caller. It is the source-backed
companion rebuild call inside the selected-battler collapse/affliction runtime
path. Keep it separate from the `4Dxx` battle-start caller family, and treat
future work here as late selected-row/controller polish rather than encounter
setup polish.
