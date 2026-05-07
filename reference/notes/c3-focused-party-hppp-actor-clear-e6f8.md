# C3 focused party HP/PP actor clear helper `C3:E6F8`

## Purpose

This pass closes the unnamed C3 source-helper row at `C3:E6F8`. It is the C3-side clear/reset half of the focused party HP/PP actor display path already documented around `C4:3573`.

## Evidence

Direct callers:

- `C1:0A04` calls `C3:E6F8`, then sets text display mode byte `$89C9 = 1`, marks `$9623 = 1`, and writes `FFFF` to `$9647`.
- `C1:0A1D` calls `C3:E6F8` while leaving text display mode, before clearing/redrawing party HP/PP state.
- menu/status paths at `C1:2714`, `C1:2AAD`, `C1:3644`, `C1:3BA6`, `C1:3BC8`, and `C1:DDD5` call it after small presentation/audio actions when a single-party-member status/menu path needs the HP/PP focus row cleared.
- `C4:3573` calls it first when `$89CA` already contains a live focused party actor, then stores a new actor id into `$89CA` and clears the matching row in the `$847E` tile region. The C4 working name is `SelectFocusedPartyHpPpActorAndBlankRow`.

`C3:E6F8` itself:

- returns immediately if `$89CA == FFFF`
- waits one frame through `C0:8756`
- computes a row offset from the focused party actor in `$89CA` and player-controlled party count `$98A4`
- clears seven 16-bit tile words at `$827E + computed_offset`
- resets `$89CA = FFFF`
- sets `$9623 = 1` so the window/tile presentation layer refreshes

The offset math matches `C4:3573`; only the base tile-buffer address differs (`$827E` here, `$847E` in the C4 selector). That makes `C3:E6F8` a source helper, not data or event bytecode.

## Working Names

- `C3:E6F8` = `ClearFocusedPartyHpPpActorAndBlankRow`

## Remaining questions

- The exact visual distinction between the `$827E` and `$847E` backing regions should stay tied to the C2/C4 HP/PP tilemap notes. The behavioral contract here is clear enough for source extraction: clear the old focused actor row and drop the focus latch.
