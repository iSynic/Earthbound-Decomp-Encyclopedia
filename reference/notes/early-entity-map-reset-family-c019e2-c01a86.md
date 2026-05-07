# Early Entity/Map Reset Family `C0:19E2..1A86`

This note records the first pass over three `ebsrc-main` reference-unknown chunks that the progress audit flagged as not directly covered in local notes yet:

- `C0:19E2` = `refs/ebsrc-main/.../unknown/C0/C019E2.asm`
- `C0:1A63` = `refs/ebsrc-main/.../unknown/C0/C01A63.asm`
- `C0:1A86` = `refs/ebsrc-main/.../unknown/C0/C01A86.asm`

The reference only names these as unknown entry chunks, so all semantic names below are local and provisional.

## `C0:19E2`

`C0:19E2` is a small scene/map refresh initializer around the already-studied `0AC5/0CF3` loader pair.

Observed behavior:

- pushes `D`, then shifts direct page down by `-$12`
- clears four 16-byte byte tables at `$4390`, `$43A0`, `$43B0`, and `$43C0` to `#$FF`
- derives coarse map coordinates from `$0031` and `$0033` by subtracting `#$0080` and shifting right three times
- loops `Y=0..0x3B`
- for each row/column-like index, calls `C0:0AC5` once and `C0:0CF3` once with the coarse coordinate in `A` and the running index folded into `X`
- restores `D` and returns long

The local stutter notes already treat `C0:0AC5` and `C0:0CF3` as the vertical/horizontal strip reload helpers, so the safest local name for `C0:19E2` is something like `Refresh_MapStripsAroundCamera`.

Direct refs:

- `C4:736B` performs `JSL $C019E2`
- `C4:7369` is only `REP #$31; JSL C0:19E2; RTL`, so it is a thin far wrapper
- `lookup_ref_symbol.py C0:19E2` only finds the three `bank00.asm` includes and `UNKNOWN_C019E2`

## `C0:1A63`

`C0:1A63` is currently just a wrapper:

```text
C0:1A63  REP #$31
C0:1A65  JSR $0E16
C0:1A68  RTL
```

`C0:0E16` is covered in the walking-stutter work as part of the producer/refresh side of the map update path. Direct/contextual calls found so far are:

- `C4:7360` performs `JSL $C01A63`
- `C4:734C` preserves the caller value, uses it as `X`, passes `A = $0031 >> 3`, calls `C0:1A63`, and returns the preserved value for script tempvar loops

`C4:7350..7368` derives `X` from the caller value, computes `$0031 >> 3`, calls `C0:1A63`, then returns the original caller value in `A`. That makes `C0:1A63` another map-refresh bridge rather than a standalone gameplay routine.

## `C0:1A86`

`C0:1A86` clears a large byte pool:

```text
C0:1A86  REP #$31
C0:1A88  LDX #$0000
C0:1A8D  SEP #$20
C0:1A8F  LDA #$FF
C0:1A91  STA $467E,X
C0:1A94  INX
C0:1A95  CPX #$0380
C0:1A98  BCC $1A8D
C0:1A9A  REP #$20
C0:1A9C  RTL
```

This is the broad reset for the `$467E..49FD` byte area. The nearby allocator at `C0:1A9D` scans `$4682+X` in 5-byte steps for `#$FF` entries and stores the requested allocation size in `$4A6A`, so this region is probably the byte backing store for the `7E:4682` free-space family mentioned by the reference symbol `FIND_FREE_7E4682`.

Direct refs:

- `C0:B53D` calls it during a larger startup path after `C0:927C`, `C0:88B1`, and `C0:8B26`, before `C0:1C11`, `C0:1A69`, and map/VRAM setup
- `C0:B68B` calls it during an overworld or scene reinitialization path after `C0:927C`, before `C0:1C11`, `C0:1A69`, delayed-action callback setup, movement state clears, and active slot initialization
- `C4:D999` and `EF:E19E` are additional direct callers that still need a focused context pass

The safest local name for now is `Reset_EntityBytePool467E`.

## Relationship to Existing C0 Notes

This small cluster sits just before the entity lifecycle material already summarized in `notes/bank-c0-entry-notes.md` and tightened in `notes/entity-pool-allocation-and-release-c01a9d-c020f1.md`:

- `C0:1A69` clears 30 word slots at `$2B32`, `$289E`, and `$2C9A`
- `C0:1A86` clears the byte pool at `$467E..49FD`
- `C0:1A9D` and `C0:1B15` operate on the same `$467E/$4682` region
- later setup paths call `C0:1C11`, `C0:1E49`, `C0:2140`, and the task-slot allocator family

So the best current boundary is: `19E2/1A63` are map strip refresh wrappers, while `1A69/1A86/1A9D/1B15` are early entity or object-state pool reset/allocation helpers.

## Source Polish Follow-Up

The 2026-05-06 C0 source polish pass named the ordinary helper-call edges in
this boundary. `C0:19E2` now calls the vertical movement map-strip payload
loader and vertical collision-strip payload loader by name, while `C0:1A63`
names its thin bridge into the vertical movement map-strip uploader. The entity
visual setup/release side of the same lane now names its allocator, release,
reservation-map rewrite, and task cleanup helpers in source.

## Remaining Checks

- Decode the `C4:D999` and `EF:E19E` callers of `C0:1A86` to distinguish full scene reset from narrower pool reset.
- Continue tracing consumers of `$112E/$116A` so the 5-byte `$467E` record layout can be named more confidently.
- Cross-check whether `$4390..$43CF` has a reference WRAM name before naming those four strip-cache byte tables.

## Working Names

- `C0:19E2` = `Refresh_MapStripsAroundCamera`
- `C0:1A63` = `Refresh_MapStripVia0E16_FarWrapper`
- `C0:1A69` = `Reset_EntitySlotStateTables`
- `C0:1A86` = `Reset_EntityBytePool467E`
