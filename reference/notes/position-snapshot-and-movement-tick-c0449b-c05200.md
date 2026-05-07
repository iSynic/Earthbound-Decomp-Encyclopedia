# Position Snapshot and Movement Tick `C0:449B-C0:5200`

This note covers the mid-bank `C0` cluster that sits immediately after the front-interaction probes:

- `C0:449B`
- `C0:476D`
- `C0:47CF`
- `C0:48D3`
- `C0:4A7B`
- `C0:4A88`
- `C0:4AAD`
- `C0:4B53`
- `C0:4C45`
- `C0:4D78`
- `C0:4EF0`
- `C0:4F60`
- `C0:4F9F`
- `C0:4FFE`
- `C0:5200`

The safest current system-level read is that this is the overworld player-position tick and snapshot-commit layer. It updates `$9875/$9877/$9879/$987B/$987F/$9881/$9883/$9885`, mirrors the result into the 12-byte transition snapshot ring rooted at `$5156`, and dispatches special movement states such as scripted step, bicycle step, and temporary mode `$98A5`.

## Reference Anchors

`ebsrc-main` still leaves these as `UNKNOWN_C0...` routines, but the event scripts give two useful high-level anchors:

- `EVENT_1` installs `UNKNOWN_C05200` with `EVENT_SET_TICK_CALLBACK`.
- `EVENT_2` calls `UNKNOWN_C04EF0`, clears current entity collision, then installs `UNKNOWN_C04D78` with `EVENT_SET_TICK_CALLBACK`.

So `C0:5200` and `C0:4D78` are script-installed tick callbacks, while `C0:4EF0` is script-callable setup for the same leader/object snapshot family.

## Tooling Note

This pass expanded `tools/decode_snippet.py` with 65C816 direct-page indirect modes:

- `LDA ($dp)`
- `STA ($dp)`
- `STA ($dp),Y`
- nearby stack/direct-page forms used by the same listings

That matters because `C0:4C45` and `C0:4D78` write snapshot records through direct-page pointers. Before this fix, the local decoder drifted after opcodes like `B2`, `91`, and `92`.

## `C0:5200`: Main Overworld Tick Callback

`C0:5200` is installed by `EVENT_1` as a tick callback.

It first exits early if `$4DC2 != 0`. Otherwise it runs a few service hooks:

- toggles the `$9F6B/$9F6F` family through `C0:7716` or `C0:777A`
- runs optional hooks at `C0:0172`, `C0:030F`, and `C4:8FC4`
- calls `C0:4C45`

After `C0:4C45`, it watches the high bytes of `$9877/$987B` against
`$5D5C/$5D5E`. If the coarse position changed and `$B549 != 0`, it calls the
previously documented `C0:3C25` refresh path. The music-specific follow-up now
names `$B549` as the auto-sector music-change latch and ties the `C0:3C25 ->
C0:68F4 -> C0:69AF -> C4:FBBD` chain to the C4 `ChangeMusic` loader; see
`notes/c0-current-position-music-refresh-c068f4-c069af.md`.

The tail also:

- skips `C0:DCC6` while `$9E54 != 0` or `$98A5 == 2`
- clears `$9F6F`
- copies `$987F -> $5D76`
- copies `$9889 * 2 -> $5D78`
- sets `$0A34 = 1` when `$9885 != 0`

That makes `C0:5200` the best current "normal overworld tick callback" boundary for this pass.

## `C0:4C45`: Position Snapshot Commit Front Door

`C0:4C45` is directly called from `C0:524A`.

The live emulator follow-up in
`notes/overworld-live-walking-controller-c04c45-c04d33.md` confirms this routine
on the ordinary walking stack upstream of the smooth `C0:400E -> C0:4010 ->
C0:1558` camera path, and narrows the next walking-state investigation to the
`C0:4C45 -> C0:5F82 -> C0:400E/4010` chain.

It is the main local coordinator:

1. Save the old `$9885` dirty/moved word, then clear `$9885`.
2. If `$5D58 != 0`, run `C0:7C5B` and decrement `$5D58`.
3. Under the `$436C` plus `$0065 & #$0040` controller/debug gate, return early when direct-page `$0002 & #$000F` is nonzero.
4. Resolve the current party/member object through `$9889 -> $0E9A -> $4DC8`.
5. Write `$987D` into object field `+$3D`.
6. Dispatch the movement body:
   - `$98A5 != 0` -> `C0:4B53`
   - `$9883 == #$000C` -> `C0:47CF`
   - `$9883 == #$0003` -> `C0:48D3`
   - otherwise -> `C0:449B`
7. Recompute `$9881` with `C0:5F82`.
8. If `$9885 != 0`, store current `$9877/$987B` into snapshot record offsets `+0/+2`, increment `$987D`, call `C0:400E`, and set `$4DD4 = 1`.
9. Always store `$9881`, `$9883`, and `$987F` into snapshot offsets `+4/+6/+8`.
10. Update `$289C` to `#$0010` or `#$0012` when `$9881` has bit `#$0008` set, depending on bit `#$0004`.

The snapshot record index is the byte at `$987D`. The code computes:

```text
record = $5156 + ($987D * 12)
```

So the 12-byte record layout now looks like:

```text
+0  x / first coordinate word
+2  y / second coordinate word
+4  tile/context word from $9881
+6  traversal/movement mode from $9883
+8  facing/direction from $987F
```

The final two bytes remain unproven in this local slice.

## `C0:449B`: Normal Input-Driven Movement Step

`C0:449B` is called only from `C0:4CBB`.

It uses the reference-named `MAP_INPUT_TO_DIRECTION` at `C0:404F` against the current `$9883` mode word. If there is no accepted input direction, it refreshes collision/context at the current `$9877/$987B` through `C0:5FF6` and exits.

When a direction is accepted, it:

- updates `$987F` unless `$5D56 & 1` blocks facing writes
- treats `$9883 == #$000D` specially, coercing direction into `1/5` or `3/7` families and writing `$987F` as `2` or `6`
- increments `$2890`
- increments `$9885`
- builds candidate coordinate pairs from `$9875/$9877` and `$9879/$987B`
- applies direction transforms through `C0:2D8F` and `C0:3017`
- probes movement/collision through `C0:5B7B`, `C0:5FD1`, and `C0:5FF6`
- dispatches movement-trigger helpers through `C0:7526` when `$5DA8 != #$FFFF`
- commits new `$9875/$9877/$9879/$987B` only when the movement is accepted

This makes `C0:449B` the normal accepted-input movement-step body below the `C0:4C45` snapshot front door.

## `C0:476D`: Copy Active Slot Position Into Player Globals

`C0:476D` is called only from `C0:4C3B`, the `$98A5 == 2` branch of `C0:4B53`.

It reads the active slot index from `$9E33`, then copies the slot arrays:

- `$0B8E[slot] -> $9877`
- `$0BCA[slot] -> $987B`
- `$0C42[slot] -> $9875`
- `$0C7E[slot] -> $9879`
- `$2AF6[slot] -> $987F`

It compares those values against the old player globals first and stores `1` to `$9885` if any changed.

So `$98A5 == 2` currently looks like a follow/external-slot-sync mode where the player globals are driven from an active entity slot rather than direct input.

## `C0:47CF`: Scripted Step Mode `#$000C`

`C0:47CF` is selected when `$98A5 == 0` and `$9883 == #$000C`.

It refuses to move while `$4DBA != 0` or while `$5D60` is counting down. Otherwise it derives a direction from `$5DC6 & #$0300`:

```text
0000 -> 7
0100 -> 1
0200 -> 5
0300 -> 3
```

Then it probes `C0:5B7B`, optionally dispatches `C0:7526` when `$5DA8` is set, and sets `$9885 = 1`. This looks like a forced/scripted movement tick keyed by the high byte of `$5DC6`, not ordinary live controller input.

## `C0:48D3`: Bicycle/Special Mode Step `#$0003`

`C0:48D3` is selected when `$9883 == #$0003`, the same traversal state that `GET_ON_BICYCLE` sets.

The caller passes the old `$9885` value in `A`. If live input has no accepted direction and the caller supplied a nonzero old dirty word, this routine reuses `$987F` as the direction. It also maintains a small `$5D5A` latch that keeps odd directions sticky for a few frames.

The body then:

- writes the selected direction back to `$987F`
- computes candidate `$9875/$9877` and `$9879/$987B` pairs
- probes the target through `C0:5CD7` and `C0:5FF6`
- increments `$9885` and `$2890` if the move is accepted
- rejects commits when tile flags contain `$00C0`

This is the clearest local reason to keep `$9883 == 3` named as bicycle/special traversal mode rather than a generic door context.

## `$98A5` Temporary Movement Modes

`C0:4B53` dispatches based on low byte `$98A5`:

```text
1 -> timed offset mode inside C0:4B53
2 -> C0:476D
3 -> C0:4AAD
other -> return
```

Mode `1` applies two coordinate deltas using tables indexed by `(mode $9883 * 32) + (direction * 4)`. It decrements `$98A7`, and when that reaches zero it clears `$98A5` and restores `$9883` from `$98A9`.

Mode `3` is entered by `C0:4A88`, whose only direct caller is `C0:D6A4`. `C0:4A88`:

- stores `#$000C -> $5D7C`
- backs up `$98A5 -> $5D7A`
- writes `$98A5 = 3`
- calls `C0:AC0C(2)`
- sets `$5D98 = 1`

While mode `3` is active, `C0:4AAD` decrements `$5D7C`. Until it expires, it uses current input direction to refresh `$2AF6` for slots `$18..$1D`, skipping inactive slots and snapshot records whose mode word at offset `+6` is `7` or `8`. When the timer expires, it calls `C0:4A7B`, which restores `$98A5` from `$5D7A` and calls `C0:D19B`.

## `C0:4D78`: Event-2 Tick Callback

`EVENT_2` installs `C0:4D78` as a tick callback after calling `C0:4EF0` and clearing current entity collision.

The routine is gated off when:

- `$98A5 == 3`
- `$5D60 != 0`
- `$4DBA != 0`
- `$4DC2 != 0`

When allowed, it resolves the current leader object through:

```text
$1A42 -> $0E9A -> $4DC8 -> object pointer in $4DC6
```

Then it uses object field `+$3D` as a `$5156` snapshot-record index, copies snapshot fields back into live arrays, and calls `C0:7A56` with the snapshot mode word at offset `+6`.

The second half decides what object field `+$3D` should become next. It uses snapshot mode offset `+6`, `$9883`, `$9887`, character index `$0E5E`, `C3:E09A`, and the existing `C0:3EC3` previous-registry gap helper.

The strong local read is that `C0:4D78` is the event-2 object/snapshot reconciliation tick: it pulls the current object from the snapshot ring, refreshes live slot coordinates/facing, and advances the object's snapshot/order byte.

## `C0:4EF0`: Script-Callable Snapshot Restore

`EVENT_2` calls `C0:4EF0` immediately before installing `C0:4D78`.

It resolves the current object and current `$5156` snapshot record from object field `+$3D`, then copies:

- snapshot `+8 -> $2AF6[current_slot]`
- snapshot `+4 -> $2BAA[current_slot]`
- snapshot `+6 -> C0:7A56(current_slot, $0E5E[current_slot])`

This is a compact "restore current slot pose/context from the snapshot record" helper.

## `C0:4FFE` and `C0:4F9F`: Party Condition Decay Gate

`C0:4FFE` is called from the broader transition/reset branch at `C0:B95E`, just before the saved-coordinate reload path documented in `saved-coordinate-reload-path-c4c718-c0b967.md`.

It returns `1` immediately if `$98A5 == 2` or `$5D98 != 0`. Otherwise it scans a small party-related table rooted at `$9891/$989C` and object pointers from `$4DC8`.

The body uses per-entry timers at `$5D66 + entry*2`; when a timer expires it subtracts from object fields `+$45` and `+$47`. For some object state values it subtracts `#$000A`; for others it subtracts `2`. When field `+$45` crosses out of the positive range, it clears six bytes at object offset `+$0E`, sets object `+$0E = 1`, clears `+$45/+47`, writes `$0F12[object +$3B] = #$0010`, and marks that a reset/refresh happened.

`C0:4F9F`, called by `C0:4FFE`, compares a value derived from object field `+$0A` through `C0:915B` against object field `+$45`. It sets or clears `$5D8C[entry]` and triggers `C1:DBBB(object +$35 + 1)` on the first threshold crossing.

The exact gameplay label is still open, but this is not part of the direct movement-step commit. It is a transition-side party/object condition decay gate that can request broader refresh work through `C0:34D6`, `C0:7B52`, and `C0:9451`.

## Working Names

These are working names, not final symbols:

- `C0:5200` -> `Tick_OverworldPlayerPositionAndCallbacks`
- `C0:4C45` -> `Commit_PlayerPositionSnapshotTick`
- `C0:449B` -> `Step_PlayerFromDirectionalInput`
- `C0:2D8F` -> `AdjustPositionHorizontal`
- `C0:3017` -> `AdjustPositionVertical`
- `C0:476D` -> `Sync_PlayerGlobalsFromActiveSlot`
- `C0:47CF` -> `Step_ScriptedMode0C`
- `C0:48D3` -> `Step_BicycleTraversalMode`
- `C0:4A88` -> `Enter_TemporaryPartyFacingRefreshMode`
- `C0:4AAD` -> `Tick_TemporaryPartyFacingRefreshMode`
- `C0:4A7B` -> `Restore_TemporaryMovementMode`
- `C0:4B53` -> `Dispatch_TemporaryMovementMode98A5`
- `C0:4D78` -> `Tick_Event2SnapshotObjectReconcile`
- `C0:4EF0` -> `Restore_CurrentSlotFromSnapshotRecord`
- `C0:4F60` -> `Queue_PartyObjectConditionDecayCallback`
- `C0:4FFE` -> `Process_PartyObjectConditionDecayGate`
- `C0:4F9F` -> `Update_PartyObjectConditionThresholdLatch`

## Open Edges

- Some offset tables used by `C0:48D3` and `$98A5 == 1` are addressed inside ranges that `ebsrc-main` also treats as code chunks. That may be deliberate code-byte-as-data reuse or a sign that older chunk boundaries are too coarse. The behavior is clear enough to document the call flow, but the table names should stay cautious.
- Object fields `+$45/+47` in `C0:4FFE` still need a stronger gameplay label.
- `$4DBA`, `$4DC2`, and `$4DD4` are now clearly movement/snapshot gates, but their final names should wait for stronger caller-side context rather than the neighboring `C0:52D4+` cluster. That next cluster is now decoded enough to identify `C0:52D4` as the party trail/snapshot-ring initializer and `C0:54C9-C0:5E82` as the collision/surface probe layer.

## Source Polish Follow-Up

The 2026-05-06 C0 source polish pass named the movement-step helper-call edges
in `C0:449B`: mushroomized movement swap, input-to-direction mapping,
horizontal/vertical position adjustment, movement surface/collision resolution,
centered collision tile reads, overlap search, movement-trigger dispatch, and
movement-boundary trigger checks. The same pass named the `C0:52D4` trail-ring
calls into the horizontal and vertical adjustment helpers.

## Follow-up From The Neighboring Seam

The follow-up pass on `C0:52D4-C0:5E3A` confirms that the snapshot ring model used above is the right frame for the movement tick. `C0:52D4` pre-populates all `$5156` records after transition-style setup, then assigns active party follower objects to every 16th trailing record by writing object field `+$3D`.

The same pass also grounds the movement probes called by `C0:449B` and `C0:48D3`: `C0:5B7B` resolves movement surface/collision state, while `C0:5CD7` and `C0:5D8B` probe actor footprints against the active collision byte page at `$E000`. The focused write-up lives in `notes/collision-surface-probes-c052d4-c05e3a.md`.
