# Entity Placement Probe `C0:263D..2C3D`

This note follows the next `bank-0-1-progress-audit.md` gap after the entity-pool allocator pass. The reference tree is already helpful here: `ebsrc-main` leaves `C0:263D` as `UNKNOWN_C0263D`, leaves `C0:2668` as an unnamed unknown include, and then immediately names the next two bodies as `SPAWN_HORIZONTAL` and `SPAWN_VERTICAL`.

## Reference Status

- `refs/ebsrc-main/ebsrc-main/src/bankconfig/US/bank00.asm` includes `unknown/C0/C0263D.asm`, `unknown/C0/C02668.asm`, `overworld/spawn_horizontal.asm`, then `overworld/spawn_vertical.asm`.
- `refs/ebsrc-main/ebsrc-main/include/symbols/bank00.inc.asm` exports `UNKNOWN_C0263D`, `SPAWN_HORIZONTAL`, `SPAWN_HORIZONTAL_RETURN`, and `SPAWN_VERTICAL`.
- Direct callers found locally:
  - `C0:263D`: `C0:2AF7`, `C0:2B05`, `C0:2BE0`, `C0:2BEE`, and `EF:DE72`
  - `C0:2668`: `C0:2B31` and `C0:2C1A`
  - `SPAWN_HORIZONTAL` / `C0:2A6B`: `C0:1533`, `C0:16C4`, and `C0:1716`
  - `SPAWN_VERTICAL` / `C0:2B55`: `C0:1606` and `C0:1659`

## Working Model

The local model is now:

1. `C0:2A6B` and `C0:2B55` probe candidate world positions along horizontal and vertical axes.
2. Those probes call `C0:263D` to look up a placement/terrain word from `D0:1880`.
3. A candidate only continues when two adjacent probed words are both nonzero and equal.
4. The probes then call `C0:2668`, which decides which spawn-candidate list to consume.
5. That list is handed to `C0:2A50`, which iterates entries and eventually feeds `C0:1E49` to allocate/init an entity slot.

That makes this seam the bridge between the movement/update side of the overworld engine and the entity lifecycle layer described in `entity-pool-allocation-and-release-c01a9d-c020f1.md`.

## `C0:263D`

Suggested local name:

- `Lookup_PlacementTileWord_D01880`

Inputs:

- `A` = low coordinate/index, accepted only when `< #$0080`
- `X` = high coordinate/index, accepted only when `< #$00A0`

Output:

- `A = D0:1880[(X << 8) + (A * 2)]` on success
- `A = 0` when either input is out of range

The caller-side usage is stronger than the isolated routine name: `SPAWN_HORIZONTAL` and `SPAWN_VERTICAL` call it in adjacent pairs, reject zero, and require both return words to match. That suggests this table is not merely a collision flag; it is a placement compatibility word or terrain-region word used to decide whether a spawn candidate can attach to the local map cells.

The external caller at `EF:DE72` is useful corroboration that `C0:263D` is a reusable map-cell lookup helper, not private bookkeeping for the spawn loop.

## `C0:2668`

Suggested local name:

- `Resolve_SpawnProbeCandidateList`

Inputs preserved into the local DP frame:

- `A -> $2C`
- `X -> $2E`
- `Y -> $30`

Important state touched:

- `$4A6C` = nonzero caller `Y` retained for the table-backed candidate path
- `$4A70` = spawn-list chance/count byte
- `$4A72` = selected candidate id or sentinel candidate id
- `$4A74/$4A76` = secondary values loaded from the `D5:9589` table in the entry iterator
- `$4A7A` = frame/throttle counter for the random/special path

There are two visible candidate sources.

### Special/random path

When `$436C != 0`, `C0:2668` calls `EF:E759`; a nonzero result can route through `C0:8E9A` and select the list at `D0:D52D` with candidate id `$0000`.

Otherwise it increments `$4A7A` and only continues every 16th call. It reads a packed class from `D7:B200`, masks the low three bits, maps that class to a small threshold, then compares a random result against that threshold. On success it forces candidate id `$01E1`, writes `$01E1` to `$4A72`, loads the list pointer from `D0:D515`, and enters `C0:2A50`.

The same `D7:B200` table is already known from `position-derived-visual-context-class-9887.md` as a packed map/cell classification table, so this branch is likely terrain-class-weighted.

### Table-backed path

If the caller supplied nonzero `Y`, `C0:2668` also has a table-backed route:

1. Derive a coarse map index from `$2C/$2E`.
2. Read `D7:A800[index]`, shift right three, and compare against current map group `$436E`.
3. If the group matches, store the caller's `Y` to `$4A6C`.
4. Index the pointer table at `D0:B880 + (Y * 4)`.
5. Load the pointed candidate list and hand it to `C0:2A50`.

That `D0:B880` table begins with long pointers into the same `D0:BBxx` data region, which fits it as a spawn candidate-list registry.

## `C0:2A50..2A69`

Suggested local name:

- `Iterate_SpawnCandidateList`

This small iterator reads the first byte of the candidate list into `$4A6E`; `#$FF` terminates the routine. Otherwise it jumps into `C0:28E7`.

`C0:28E7..2A3A` then:

- reads the candidate id from the list
- chooses chance/metadata bytes from `D5:9589`
- rejects duplicates by checking active slots for the same `$2C9A` candidate marker and `$2D4E` map-cell index
- calls `C0:1E49` to allocate/init a slot
- runs up to 20 random placement attempts through `C0:5F33` and `C0:5DE7`
- commits final position and identity into `$0B8E/$0BCA/$2C9A/$2D12/$2D4E/$3186`

The candidate marker write is especially useful:

```text
$2C9A[slot] = candidate_id + $8000
$2D12[slot] = list entry id from [$0A + 1]
$2D4E[slot] = (Y << 7) + X map-cell index
```

That ties this placement seam directly to `C0:2140` and `C0:20F1`, which both clear `$2C9A` during release.

## `SPAWN_HORIZONTAL` / `C0:2A6B`

Suggested local name:

- keep reference name `SPAWN_HORIZONTAL`

This routine is gated by event flags `#$000B` and `#$0049`, `$4A5A`, horizontal alignment, and bounds. It derives probe coordinates from the caller's `A/X`, then tries a small series of candidate positions.

For each candidate it calls `C0:263D` twice:

- reject if the first lookup returns zero
- reject if the second lookup differs from the first
- otherwise increment `$4A62` by `8` and call `C0:2668`

`$4A62` is therefore a horizontal spawn-distribution or random-range accumulator consumed later by `C0:9231` in the placement loop.

## `SPAWN_VERTICAL` / `C0:2B55`

Suggested local name:

- keep reference name `SPAWN_VERTICAL`

This body mirrors the horizontal path with the axis and bounds swapped. It calls `C0:263D` in the same adjacent-pair pattern, then calls `C0:2668` for successful pairs.

The vertical-specific accumulator is `$4A64`, which is later used beside `$4A62` when `C0:28E7..2A3A` picks random offsets for the final placement attempt.

## Naming Notes

I would not yet rename `D0:1880` as a pure collision table. The code only proves "nonzero equal placement word" semantics, while the nearby use of `D7:B200` shows the engine already has richer packed map classification tables. `PlacementTileWord` keeps the name useful without overclaiming.

The strongest next seam after this note is `C0:2C3E`, because it immediately follows `SPAWN_VERTICAL` in `ebsrc-main` and is now the first still-unexplained address after the placement bridge.

## Source Polish Follow-Up

The 2026-05-06 source polish pass replaced the raw helper calls in
`SPAWN_HORIZONTAL` and the first `SPAWN_VERTICAL` spawn-probe body with the
local names from this note. `C0:2A6B` and `C0:2B55` now call
`Lookup_PlacementTileWord_D01880` for their adjacent nonzero/equal placement
checks and `Resolve_SpawnProbeCandidateList` for accepted probe windows. The
candidate commit path in `C0:2957` now also names its footprint, terrain
compatibility, and failed-placement release helpers.

The later 2026-05-06 follow-up added source anchors for the merged routines
after `SPAWN_VERTICAL` without splitting the source file yet. The reference
`adjust_position_horizontal.asm` and `adjust_position_vertical.asm` entries are
now locally anchored as `AdjustPositionHorizontal` and `AdjustPositionVertical`,
and their repeated long-multiply helper calls are named through the local
hardware-multiply contract.

## Working Names

- `C0:263D` = `Lookup_PlacementTileWord_D01880`
- `C0:2668` = `Resolve_SpawnProbeCandidateList`
- `C0:28E7` = `TryPlaceSpawnCandidateFromListEntry`
- `C0:2A50` = `Iterate_SpawnCandidateList`
- `C0:2A6B` = `Spawn_Horizontal`
- `C0:2B55` = `Spawn_Vertical`
