# Teleport Menu Wrapper `C1:BB71` and Teleport Executor `C1:BCAB`

This note covers the unknown include at `C1:BB71` and its immediate named neighbor at `C1:BCAB`.

See also [text-command-family-1a-menus.md](notes/text-command-family-1a-menus.md).
See also [battle-psi-user-selection-front-end-c1b5b6-b7c6.md](notes/battle-psi-user-selection-front-end-c1b5b6-b7c6.md).
See also [teleport-mainloop-state-machines-c0e214-c0ebdf.md](notes/teleport-mainloop-state-machines-c0e214-c0ebdf.md).

## Main Result

`C1:BB71` is best treated as the party-menu side wrapper for PSI Teleport destination selection.

The direct caller is the PSI branch of the top-level menu controller:

- `C1:3C01` prepares menu state and sets `$5E71`
- `C1:3C0B -> C1:BB71`
- the caller clears `$5E71` afterward and returns to the main menu loop

That separates this helper from the text command `[1A 0B]` teleport menu helper at `C1:AAFA`: both are user-facing teleport destination selection flows, but `BB71` is reached from the ordinary command menu/PSI path rather than the text-command menu dispatcher.

## `C1:BB71` Shape

`C1:BB71` opens window/context `0x2E` and creates four category rows from the fixed `C3:F090` text block.

The local flow is:

- set `$5E71 = 1`
- run a small generic selection with callback `C1:952F`
- if the selection is `3`, restart the first stage
- create rows `1..4` from `C3:F090 + index * 8` using `C1:15F4`
- open/focus window `0x2E`
- install `C1:CAF5` as the row refresh callback and run `C1:196A`
- if a PSI entry is selected, open a temporary detail/help loop using `C1:BB06`
- close windows `0x04` and `0x2F` after the help loop
- on backout, close windows `0x2E`, `0x01`, and finally `0x08`

The `CAF5`/`BB06` pair is the same PSI-menu metadata lane already documented for battle PSI menus. Here it is reused for the Teleport PSI branch in the field menu.

## `C1:BCAB` Teleport Executor

`C1:BCAB..BEFC` is now source-backed at `src/c1/c1_bcab_execute_teleport_destination.asm`. The source split keeps `BCAB..BE4D` as the destination executor, `BE4D..BEC6` as the homesickness attempt helper, and `BEC6..BEFC` as the get-off-bicycle text/script wrapper.

The named `overworld/teleport.asm` body starts at `C1:BCAB`. It takes a teleport destination index in `A`, indexes the `D5:EBAB` teleport destination table with an 8-byte stride, and stages the overworld transition.

Important local actions:

- saves and forces `$5D98 = 1` during setup
- clears event flags `1..10` through `C2:165E`
- calls `C0:6B3D`
- uses destination byte `+5` as a sound/sprite/environment selector through `C0:68AF`
- calls `C0:ABE0`
- computes tile-scaled coordinates from destination bytes `+0` and `+2`
- reads destination byte `+4`, masks bit `7`, and treats low bits as a direction/landing selector
- calls the same movement/placement helpers used by the C0 teleport stack:
  - `C0:13F6`
  - `C0:3FA9`
  - `C0:52D4` when the high bit of byte `+4` is set
  - `C0:68F4`
  - `C0:69AF`
- dispatches pending text pointer `$9D1B/$9D1D` through `C0:9279` if it changed
- calls `C0:65A3`
- restores the pre-teleport sound/environment selector
- writes `$5DC4 = FFFF`
- queues the post-transition script path through `C0:6B21`
- restores `$5D98`

## Reference Corroboration

The bank include order puts these functions in the expected field-menu strip:

- `overworld/use_item.asm`
- `unknown/C1/C1B5B6.asm`
- `unknown/C1/C1BB06.asm`
- `unknown/C1/C1BB71.asm`
- `overworld/teleport.asm`
- `overworld/attempt_homesickness.asm`
- `overworld/get_off_bicycle.asm`

Community control-code docs also distinguish the separate script-side teleport menu:

- `[1A 0B]` = Display Teleport Menu
- `[1F 20]` = Trigger PSI-style Teleport
- `[1F 21]` = Teleport to Preset Coordinates

That makes the safest split:

- `C1:AAFA` = text command display-teleport-menu helper
- `C1:BB71` = field-menu/PSI branch destination picker
- `C1:BCAB` = actual destination-table-driven overworld teleport executor
- `C1:BE4D` = homesickness attempt/result helper
- `C1:BEC6` = get-off-bicycle message and exit wrapper

`C1:AAFA..AC00` is now source-backed as `RunTeleportDestinationSelectionMenu` in `src/c1/c1_aa5d_run_party_equipment_menu_controller.asm`.
