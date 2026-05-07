# NPC attention and path coordinator (`C0:D19B-C0:D98F`)

## Scope

This strip follows the movement-vector script runtime and continues to use the
same current-slot, pathfinding, and movement-state fields:

- `$1A42`: current entity slot.
- `$4DB6`: focal slot for this coordinator.
- `$4DB8`: related or target slot.
- `$4DBA`: coordinator-active flag.
- `$4DBC`: relative-facing relation flag.
- `$5D60`: short global countdown/lockout used while the coordinator is active.
- `$2C5E`: per-slot path/attention state.
- `$4A7C/$4A84`: four small type/count buckets built from the entity table.
- `$9F8A/$9F8C`: compact list of affected entity types.

The exact gameplay label is still cautious, but event script `EVENT_32` uses
`C0:D5B0` immediately before the "butterfly hit" text path, and `EVENT_33`
uses `C0:D77F` in the same cleanup family. This strongly ties the strip to
scripted NPC attention/interaction cleanup rather than generic math.

## Working Names

- `C0:D19B` = `Prepare_NpcAttentionPathSet`
- `C0:D4DE` = `Prepare_RandomizedNpcAttentionCandidates`
- `C0:D59B` = `Check_NpcAttentionCoordinatorActive`
- `C0:D5B0` = `Gate_NpcAttentionCoordinatorFromScript`
- `C0:D77F` = `MarkOtherSlotsAttentionLocked`
- `C0:D7B3` = `Save_CurrentSlotAttentionPosition`
- `C0:D7C7` = `Restore_CurrentSlotAttentionPosition`
- `C0:D7E0` = `Normalize_CurrentSlotAttentionState`
- `C0:D7F7` = `Consume_CurrentSlotAttentionPath`
- `C0:D98F` = `Export_CurrentSlotAttentionTarget`

## `C0:D19B`: build attention/path state for a focal slot

`C0:D19B` starts from the focal slot in `$4DB6` and clears `$4DBA` before doing
three larger passes.

First, it compares the focal slot and related slot `$4DB8`:

- If `$1A86[focal] == 8`, it takes a fixed relation path.
- Otherwise it computes the direction from focal to related through
  `C4:1EFF`, normalizes that direction with `C0:915B`, and compares it against
  both the focal slot's `$1A86` direction and player facing `$987F`.
- It writes a small relation flag to `$4DBC`: `0`, `1`, or `2`.
- It seeds `$5D60 = #$0078`.

Second, it looks up the focal slot's type `$2C9A & #$7FFF` in the `D0:C60D`
table family, calls `C2:E8E0`, and walks four compact table groups. For each
group it records a type/count pair in `$4A7C/$4A84` and marks matching live
slots in `$2C5E` when their `$2D12` type appears in the table.

Third, it calls the named pathfinder entry `C0:BC74` with a `#$0040` rectangle,
then walks the same table groups again to reconcile the returned path/candidate
records with live slots:

- Matching slots can be marked in `$2C5E`.
- Slots no longer selected have `$2C5E` cleared.
- `$10B6` and `$116A` high bits are toggled as per-slot visual or interaction
  flags.
- `$9F8A/$9F8C` receive a compact list of affected `$2D12` types.

The safest local interpretation is that `C0:D19B` prepares a coordinated
attention/path state around one focal NPC and a small set of related entity
types.

## Randomized candidate setup and active-state predicates

`C0:D4DE` builds a 128-entry temporary candidate table starting at `$0200`.
It seeds the table through `C0:8EED`, decodes each packed word into small X/Y
components, remixes those components through the shared shift/divide helpers,
and writes the transformed packed value back. It finishes with `C0:856B(#$18)`.
This appears to be a shuffled/randomized candidate list used before the
coordinator picks related entities.

`C0:D59B` is a simple active-state predicate. It returns `1` when either
`$5D60` or `$4DBA` is nonzero; otherwise it returns `0`.

## `C0:D5B0`: event-facing coordinator gate

`C0:D5B0` is the main event-facing gate. It rejects immediately when broader
movement/script locks are active, including `$4DC2`, `$5DC2`, `$98A5 == 2`,
`$5D56 & 2`, `$9883 == #$000C`, and `$5D58`.

When no coordinator is active and the current slot's `$2D12` type is
`#$00E1`, it returns `1` immediately. Otherwise, if the current slot has a
usable neighbor/overlap context through `C0:D15C`, it starts the coordinator:

- Sets `$4DBA = 1`.
- Calls `C0:D4DE` to prepare randomized candidates.
- Stores the current slot in `$4DB6`.
- Stores either `$28CC` fallback slot `#$0018` or the slot's `$289E` neighbor
  in `$4DB8`.
- Marks broad slot flags in `$10B6`.
- Calls `C0:4A88`.
- Returns `1`.

While the coordinator is already active, it marks the current slot's neighbor
cache `$289E` with `#$8000`, checks the `$4A7C/$4A84` type/count buckets, and
marks matching slots through `$10B6` and `$9F8A/$9F8C`. If no bucket remains and
`C2:E9C8` allows it, it sets `$5D60 = 1` and marks the broad slot flag family.

## Cleanup, save/restore, and path consumption

`C0:D77F` sets the high `#$C000` bits in `$10B6` for all entity slots except
the current slot and slot `#$0017`. Event scripts call this immediately before
stopping velocities or ending the scripted object interaction.

`C0:D7B3` saves the current slot's `$0B8E/$0BCA` position into `$4DBE/$4DC0`.
`C0:D7C7` restores those saved coordinates back to the current slot.

`C0:D7E0` normalizes `$2C5E[current]`: if it is nonzero, it writes `1`.

`C0:D7F7` consumes a current-slot path when `$2C5E[current] == #$FFFF`.
It reads the path pointer `$2E02[current]`, converts the next path grid point
back into world coordinates through the C4 coordinate tables, and checks
whether the current position is within three units of that target. When reached,
it decrements `$2E3E[current]`, advances `$2E02[current]` by four bytes, and
updates `$2AF6[current]` from the direction toward the next path target. When
the path count reaches zero, it clears `$2C5E[current]` and ORs `#$0080` into
`$28DA[current]`.

`C0:D98F` is the lighter target-export variant. If `$2E3E[current]` is nonzero,
it converts the next path point into world coordinates, writes it into
`$0FC6/$1002[current]`, decrements `$2E3E`, advances `$2E02`, and returns `1`.
If no path steps remain, it returns `0`.

## Practical interpretation

This strip is the bridge between the earlier pathfinding buffers and scripted
NPC behavior:

- `C0:D19B` prepares a focal-slot attention/path set.
- `C0:D5B0` starts or advances that coordinator from event scripts.
- `C0:D7F7` and `C0:D98F` consume the path output into live movement or target
  coordinates.
- `C0:D77F/D7B3/D7C7/D7E0` are small cleanup and state-normalization helpers
  around the same interaction path.

The next separate frontier is the active-slot draw/order dispatcher around
`C0:DA31/DB0F`, which we already partially understand from earlier notes but
can still tighten.
