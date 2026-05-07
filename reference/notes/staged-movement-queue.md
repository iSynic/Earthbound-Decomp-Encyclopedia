# Staged Movement Queue in WRAM

This note captures the queue machinery behind `Queue_StagedMovementFromGridCoords` and the later consumer at `C0:75DD`.

## Core correction

The family rooted at `$5DEA` is not a ROM table.

It is a WRAM-backed 4-entry queue read and written through the data bank. The earlier attempt to treat `$5DEA` like bank-`C0` static data was wrong.

## Confirmed queue routines

- `Reset_StagedMovementQueue` at `C0:64D4`
- `Enqueue_StagedMovementQueueEntry` at `C0:64E3`
- `Process_StagedMovementQueueEntry` at `C0:75DD`

## Queue layout

The enqueue and consume code both use the same slot math:

- slot index in `$5E04` or `$5E02`
- `slot_offset = slot_index * 6`
- entry type at `$5DEA + slot_offset`
- entry payload word 0 at `$5DEC + slot_offset`
- entry payload word 1 at `$5DEE + slot_offset`

That gives a 4-entry ring buffer of 6-byte records.

## Ring-buffer state words

The strongest current interpretation is:

- `$5E04`: write index
- `$5E02`: read index
- `$5DC0`: current or last-processed queue type, also used for duplicate suppression during enqueue
- `$5D9A`: queue-pending flag or queue-state flag

What is byte-proven:

- `C0:64D4` clears `$5E04` and `$5E02`, then writes `#$FFFF` to `$5DC0`.
- `C0:64E3` writes a type word into `$5DEA + 6*n` and two payload words into `$5DEC/$5DEE + 6*n`, advances `$5E04` modulo 4, and sets `$5D9A = 1`.
- `C0:64E3` skips enqueue entirely when the incoming type matches `$5DC0`.
- `C0:75DD` reads one entry from `$5DEA/$5DEC/$5DEE + 6*n`, copies the entry type into `$5DC0`, advances `$5E02` modulo 4`, and later resets `$5DC0` to `#$FFFF`.
- `C0:75DD` also recomputes `$5D9A` by comparing `$5E02` against `$5E04` after processing.

## Servicing conditions

Two confirmed direct callers service the queue:

- `C0:B840`
- `EF:E541`

The `C0:B840` path is especially informative. It only calls `Process_StagedMovementQueueEntry` when:

- `$5E02 != $5E04`
- `$5D60 == 0`
- `$4DBA == 0`
- `$4DC2 == 0`

That makes this look like a deferred movement or scripted-step queue that is only drained when the engine is not already busy with blocking state.

## Queue entry dispatch

`Process_StagedMovementQueueEntry` dispatches by entry type:

- type `#$0002`: loads payload into `$0E/$10` and `JSR $6BFF`
- types `#$0000`, `#$0008`, `#$0009`: loads payload into `$0E/$10` and `JSL $C10004`
- type `#$000A`: also calls `JSL $C10004`, then checks for payload `C7:D33E` and, on match, seeds `$9E54 = #$0697` and clears `$9E56`
- other types currently fall through without an obvious extra action in this consumer

## Relationship to `C0:70CB`

`Queue_StagedMovementFromGridCoords` at `C0:70CB` is one producer-side helper in the broader family, but it does not write directly into `$5DEA` itself. Instead, it builds staged movement state and hands completion to the delayed timer callbacks at `C0:6F82` or `C0:6FED`.

The larger selector around `C0:75AF` belongs to a neighboring helper family that picks among several movement-related routines before the queue consumer at `C0:75DD` later drains entries from WRAM.

## Targeted legacy cross-check

A narrow compare against the legacy reference aligns with our byte-level read:

- the selector around `75xx` branches on small mode values
- mode `4` reaches `C0:70CB`
- nearby modes reach sibling helpers at `C0:6A91`, `C0:6ACA`, `C0:6E6E`, `C0:6A8B`, and `C0:6A8E`

We should still treat those as a targeted cross-check, not authoritative naming.

## Best next target

- Decode the upstream selector that calls `JSL $C07477` and then branches into the `75xx` helper family, because that should tell us what the queue entry types and sibling movement helpers actually mean in gameplay terms.

## Correction on queue type `#$000A`

A later pass around `C06B21`, `C06B3D`, and `C06BFF` tightened the meaning of type `#$000A`.

The older wording here leaned too far toward movement because `Process_StagedMovementQueueEntry` handles type `#$000A` in the same queue consumer as the movement-like types.

The stronger current read is:

- type `#$000A` = deferred far script pointer

Why that is stronger now:

- `C06B3D` scans the queue specifically for type `#$000A`, copies only the payload pointers into a temporary buffer at `5E58`, and then re-enqueues them as type `#$000A`.
- `C06BFF` is a pointer-driven script runner that dispatches through `C10004` and then runs transition/world-state refresh plus `C06B21`.
- `C0:DCF8` enqueues `DATA_C7D33E` as type `#$000A`, and `C7:D33E` is a real phone/text-side script.

So type `#$000A` still belongs to the same WRAM ring buffer, but it now looks much more like a deferred script class than a movement helper subtype.

See also: [post-transition-deferred-script-queue-c06b21-c06bff.md](notes/post-transition-deferred-script-queue-c06b21-c06bff.md).

## Narrower producer picture for type `#$000A`

A later pass over the apparent `#$000A` sites removed a lot of noise.

For the shared `$5DEA` queue, the currently pinned type-`#$000A` producers are narrow:

- `C06B3D` re-enqueues preserved deferred pointers as type `#$000A`
- `C0:DCF8` enqueues `DATA_C7D33E` as type `#$000A`

Most other literal `#$000A` values nearby are just local bounds, counters, or selector constants, not queue producers.

So the cleanest current update is:

- type `#$000A` is a relatively specialized deferred-script-pointer class
- it is not a broadly emitted catch-all queue subtype

That makes the whole `$5DEA` family read better as a shared deferred-action / deferred-pointer queue than as a pure movement queue.
