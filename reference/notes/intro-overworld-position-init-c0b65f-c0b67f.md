# Intro overworld position/init pair (`C0:B65F-C0:B67F`)

## Scope

`C0:B65F` and `C0:B67F` sit after the file-select/sine-table block and just
before the named `INIT_BATTLE_OVERWORLD` and `MAIN_LOOP` entries. The legacy
disassembly explicitly notes `C0:B67F` as related to the intro cutscene where
the game pans over Onett.

## Working Names

- `C0:B65F` = `SeedPlayerOverworldStartPosition`
- `C0:B67F` = `InitializeIntroOverworldScene`
- `C0:B525` = `FileSelectInit`
- `C0:2D29` = `ResetOverworldPartyRuntimeState`
- `C0:8F42` = `SnapshotContinuationFrame`

## `C0:B65F`: seed player position/facing

`C0:B65F` is a tiny position initializer:

- Copies incoming X/Y into `$9877/$987B`, the low player X/Y position fields.
- Stores facing direction `#$0002` in `$987F`.
- Sets `$986F` to `1`.
- Mirrors the same X/Y into `$0B46/$0B82`.

This is a direct position/facing seed rather than a movement integrator. It
sets the player coordinate truth fields and their matching entity-coordinate
mirrors, then returns.

## `C0:B67F`: intro/Onett pan setup

`C0:B67F` is a compact overworld initialization script for the intro scene:

- Resets display/task state with `C0:927C`, entity pool setup at `C0:1A86`,
  allocation/setup helpers at `C0:1C11` and `C0:1A69`.
- Clears or seeds scene state:
  `$4DC2 = 0`, `$5D74 = 0`, `$4A58 = 1`, `$4A5A = FFFF`,
  `$4A5E = 000A`, `$5D60 = 0`, `$5D9A = 0`.
- Calls `C4:FD45(1)`, stores `$0697` in `$9E54`, and installs callback
  pointer `C0:DC4E` through `C0:851C`.
- Clears `$9F41/$9F3F`, sets `$B4A8 = FFFF`, seeds `$0A4C/$0A4E` as
  `17/18`, and initializes script/task state via `C0:9321`.
- Calls `C0:2D29` and `C0:3A24`, then copies/decompresses a `$0200`-byte
  block through `C0:8EFC`.
- Runs C4 setup helpers, restores the player coordinate fields through
  `C0:13F6`, processes the deferred transition/script queue at `C0:6B21`,
  and finishes with `C0:39E5`.

## Practical decomp notes

The pair gives a useful top-level boot contract for porting:

- `C0:B65F` can lift as `setPlayerOverworldStart(x, y, facing=2)`.
- `C0:B67F` can lift as `initializeIntroOverworldScene()`, with the callback
  at `C0:DC4E` treated as the intro camera/pan driver until that later main
  loop region is named.

## Source Polish Follow-Up

The 2026-05-06 C0 source polish pass added a local source anchor for `C0:2D29`
as the shared overworld party-runtime reset entry. `C0:B67F` now calls that
entry by name before rebuilding the mushroomized-walking controller and display
setup.

The later 2026-05-06 helper-call pass extended the same source module through
the `INIT_BATTLE_OVERWORLD` and main overworld loop surfaces. The initializer now
names the delayed-action pool/state setup, auto-sector music change toggle,
frame-callback install, overworld VRAM/map-load setup, deferred script queue,
mushroomized target refresh, EF debug-mode predicates, C2 instant-win check and
handler, battle common init, teleport mainloop state machine, C4 intro/file
select and menu-name setup, movement-record consumption, get-off-bicycle text
exit, Magic Truffle direction helper, Your Sanctuary test display stub, and
party condition-decay gate.

`C0:8F42` is named here as `SnapshotContinuationFrame`: it writes the current
long-call return/processor/direct-page/stack state into the caller-selected
buffer (`$0A20` or `$0A2A` in this module), while the already observed `C0:8F68`
path restores that frame.

The adjacent 2026-05-06 source-split pass promoted the pre-`B67F`
`C0:B2FF..B65F` corridor into clamp-table, projection-helper, sine-table, and
file-select-init pieces. The continuation now calls `C0:B525` as
`FileSelectInit`, closing the previous numeric same-bank helper edge. See
`notes/file-select-init-and-projection-c0b2ff-c0b65f.md`.
