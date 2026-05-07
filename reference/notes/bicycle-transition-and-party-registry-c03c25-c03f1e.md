# Bicycle Transition and Party Registry Helpers `C0:3C25..3F1E`

This note covers the next audit-led C0 cluster after `character-affliction-clear-c0329f.md`. The useful reference clue is that `ebsrc-main` does not leave this whole region anonymous: it names the large body at `C0:3C5E` as `GET_ON_BICYCLE`, while the surrounding helpers remain mostly `UNKNOWN_...`.

## Reference Status

- `C0:3C25` is `unknown/C0/C03C25.asm`.
- `C0:3C4B` is `UNKNOWN_C03C4B`.
- `C0:3C5E` is the reference-named `GET_ON_BICYCLE`.
- `C0:3CFD` is `UNKNOWN_C03CFD`, with internal exported labels `UNKNOWN_C03CFD_ON_BICYCLE` and `UNKNOWN_C03CFD_RETURN`.
- `C0:3DAA`, `C0:3E25`, `C0:3E9D`, `C0:3EC3`, and `C0:3F1E` remain unknown in `ebsrc-main`.
- `C0:3E5A` is a real internal helper but does not appear as a separate exported symbol in `ebsrc-main`; it is called by `C0:3E9D`.

Direct caller anchors found locally:

- `C0:3C25`: `C0:5279`
- `C0:3C4B`: `C1:B182`
- `C0:3C5E` / `GET_ON_BICYCLE`: `C1:864E`
- `C0:3CFD`: `C0:2C79`, `C1:BEF6`, `C1:C032`, `EF:0FF1`
- `C0:3DAA`: no direct `JSL/JSR` found, but a raw long pointer appears at `C3:A067`
- `C0:3E9D`: `C0:3ED7`, `EF:02EA`
- `C0:3EC3`: `C0:4EC4`, `C0:E24E`, `EF:0386`, `EF:03BF`
- `C0:3F1E`: internal call from `C0:3FD4`

## Working Model

This cluster is a bicycle and party-registry transition layer. It bridges:

- the live coordinate/context words around `$9877/$987B/$987F/$9881/$9883/$9887`
- the six-entry overworld entity-type registry at `$988B/$9891/$9897/$98A3`
- the entity slot lifecycle helper `C0:1E49`
- party-character records reached through the `$99CE` stride-`$005F` family
- object/slot side fields reached through `$4DC8` object pointers

The important shape is:

1. `GET_ON_BICYCLE` validates that the registry contains only the leader type, frees slot `$18`, and rebuilds slot `$18` as a bicycle-mode entity.
2. `C0:3CFD` is the matching bicycle/special-mode teardown or handoff path. It frees slot `$18`, clears bicycle-mode words, and rebuilds the ordinary slot `$18` entity.
3. `C0:3DAA..3EC3` keep the party-character and live-object ordering fields synchronized while party members or registry entries change around that mode.
4. `C0:3F1E` and `C0:3FA9` push transition coordinates back out to all registry-backed live entities.

## `C0:3C25`

Suggested local name:

- `Refresh_DestinationContextIfPositionChanged`

This routine sets `$5DDA = 1`, calls `C0:68F4` with the current `$9877/$987B`
position pair, compares `$5DD6` against `$5DD4`, and if the value changed calls
`C0:8756` and `C0:69AF`. It then clears `$5DDA` and returns. The later audio
follow-up names `$5DD6` as the current map music track, `$5DD4` as its latched
mirror, and `$5DDA` as the cue-suppression latch during guarded refreshes; see
`notes/c0-current-position-music-refresh-c068f4-c069af.md`.

The direct caller at `C0:5279` only runs it after detecting that the packed current-position pair changed from the cached pair at `$5D5C/$5D5E`, and only when `$B549` is nonzero. So this is best read as a guarded destination/music/context refresh after current position changes, not a general update tick.

## `C0:3C4B`

Suggested local name:

- `Probe_CurrentPositionHighCollisionBits`

This routine calls `C0:5D8B` with:

```text
A = $9877
X = $987B
Y = #$000C
```

and returns only `result & #$00C0`.

The visible caller at `C1:B182` checks this only for one battle/text-side case where `$22 == #$00B0`; if the masked bits are nonzero, it selects a fixed `C7:C833` text pointer instead of the ordinary text table. The exact player-facing condition is still open, but mechanically this is a small high-bit terrain/collision predicate for the current position.

## `GET_ON_BICYCLE` / `C0:3C5E`

Reference name:

- `GET_ON_BICYCLE`

This body only proceeds when the overworld entity registry has exactly one active entry and that entry's type code is `1`. In other words, it refuses to enter bicycle mode unless the leading party/leader state is simple enough.

When accepted, it:

- optionally plays music track `#$0052` through `C4:FBBD ChangeMusic` when
  `$5DD8 == 0`
- frees slot `$18` through `C0:2140`
- sets `$9887 = 6`
- sets `$9883 = 3`
- clears `$9A0B`, `$987D`, `$0A38`, and `$0A3A`
- seeds the entity initializer with the current position from `$0BBE/$0BFA`
- calls `C0:1E49` with `A = #$0007`, `X = #$0002`, `Y = #$0018`
- sets high bits in slot-side words around `$10E6` and `$1032`
- clears `$1122`
- copies `$987F` to `$2B26`
- calls `C4:FD45(0)` to disable auto-sector music changes
- sets `$9885 = 1`, `$5DBA = 1`, and `$5D74 = 2`

The safest read is that slot `$18` is rebuilt as the bicycle mode's special player entity, while the `$988x` and `$5Dxx` words latch the corresponding traversal/presentation state.

## `C0:3CFD`

Suggested local name:

- `Restore_LeaderEntityFromBicycleMode`

This routine only does its main work when `$9883 == 3`, matching the bicycle-mode setup above. It:

- calls `C4:FD45(1)` to reenable auto-sector music changes
- if neither `$4DC2` nor `$5D9A` is set, calls `C0:6A07` to reapply the
  current-position music track
- frees slot `$18`
- clears `$9887`, `$9883`, `$9A0B`, and `$987D`
- optionally runs several refresh helpers when `$5D9A == 0`
- clears `$0A38/$0A3A`
- calls `C0:1E49` with `A = #$0001`, `X = #$0002`, `Y = #$0018`
- clears `$1122`
- copies `$987F` to `$2B26`
- marks `$1032` with `#$9000`
- if `$5D9A != 0`, also marks `$10E6` with `#$C000`, calls `C0:8756` twice, and refreshes slot `$18` through `C0:A780`
- clears `$5DBA` and sets `$5D74 = 2`

This is the strongest local fit for leaving bicycle/special traversal mode and restoring the ordinary leader entity.

## `C0:3DAA`

Suggested local name:

- `Sync_CurrentSlotToPartyCharacterRecord`

This helper starts from the current slot id in `$1A42`. It:

- clears `$3456[slot]` to `#$FFFF`
- writes timer/state `8` to `$0F12[slot]`
- seeds `$0ED6[slot]` with a random low nibble
- refreshes the current slot through `C0:A780`
- maps `$0E9A[slot]` through the party-character stride helper `C0:8FF7(#$005F)`
- writes the current slot id to character record offset `+$3B`
- copies `$0E5E[slot]` to character record offset `+$35`
- clears character record offset `+$39`
- writes `#$FFFF` to character record offset `+$5C`
- if character record offset `+$0E` equals `1`, upgrades `$0F12[slot]` from `8` to `16`
- writes `$2898 = $9889 * 2`

The offset `+$0E` test is important because `character-affliction-clear-c0329f.md` confirms that record offset as the first affliction/status byte. So `C0:3DAA` is status-aware when seeding the current slot's timer/state word.

## `C0:3E25`

Suggested local name:

- `Get_PreviousRegistryTypeCode`

Input:

- `A` = zero-based party/type index

Behavior:

- search `$988B` for type code `A + 1`
- if it is the first entry, return `#$FFFF`
- otherwise return the preceding `$988B` type code

This is a small ordered-registry predecessor lookup.

## `C0:3E5A`

Suggested local name:

- `Get_PreviousRegistryObjectOrderByte`

Input:

- `A` = zero-based party/type index

Behavior:

- search `$988B` for type code `A + 1`
- if it is the first entry, return `#$FFFF`
- otherwise take the previous registry entry's live slot from `$9897`
- map that slot through `$0E9A` and `$4DC8`
- return object field `+$3D`

This is the object-side predecessor counterpart to `C0:3E25`.

## `C0:3E9D`

Suggested local name:

- `Measure_PreviousRegistryOrderDelta`

This helper calls `C0:3E5A`, reads object field `+$3D` from the current object pointer at `$4DC6`, then returns the unsigned wrapped delta from the previous object's field to the current object's field.

If the previous value is lower than the current value, it adds `#$0100` before subtracting. That makes the returned value a circular byte-range delta.

## `C0:3EC3`

Suggested local name:

- `Advance_RegistryOrderAndUpdateGapFlag`

This helper is called by movement/order-update paths. It:

- saves caller `Y` as an accumulated output
- saves caller `X` as a target delta
- calls `C0:3E9D`
- if the measured delta equals the target, increments the output by one and clears bit `#$1000` in the current slot's `$1002`-family word
- if the measured delta is greater than the target, adds caller DP `$1E` to the output and sets bit `#$1000`
- returns the adjusted output in `A`

The naming is cautious, but the role is clear enough: it compares current and previous registry/object ordering and reflects the result into a per-slot bit at `$1002 + current_slot * 2`.

## `C0:3F1E`

Suggested local name:

- `Apply_TransitionSnapshotToRegistryEntities`

This helper copies the current transition/context words into two 12-byte snapshot records rooted at `$5156` and a second record reached by adding `#$0BF4`.

For each record it writes:

- `+0 = $9877`
- `+2 = $987B`
- `+4 = $9881`
- `+6 = $9883`
- `+8 = $987F`
- `+A = 0`

It also clears `$5D56`.

Then it walks every active registry entry (`Y < $98A3`) and:

- maps `$9891[Y]` through `$4DC8` to an object pointer
- clears object field `+$3D`
- writes `#$FFFF` to object fields `+$41` and `+$37`
- maps `$9897[Y]` to a live entity slot
- copies `$9877/$987B/$987F/$9881` to `$0B8E/$0BCA/$2AF6/$2BAA` for that live slot

So `C0:3F1E` is the fanout that applies the current transition snapshot to every registry-backed live entity.

## Relation to `C0:3FA9`

`C0:3FA9` is already documented in the post-transition queue notes. With this pass, its front half is clearer:

1. Store incoming position/context to `$9877/$987B/$987F`.
2. Derive `$9881` through `C0:5F33`.
3. Call `C0:3A94` to refresh the position-derived context class.
4. Call `C0:3F1E` to fan the snapshot out to registry-backed entities.
5. Clear several follow-up arrays and run the visible-entity refresh path through `C0:7B52`.

This makes `C0:3F1E` the lower-level registry fanout under the already-known post-transition refresh entry.

## Updates to Older Model

The older C0 overview described bodies around this region as generic scene wrappers. That was not wrong mechanically, but the reference name and local flow now sharpen the boundary:

- `C0:3C5E` is specifically the get-on-bicycle path.
- `C0:3CFD` is the matching restore/leave-special-mode path.
- `C0:3DAA..3EC3` are not bicycle-only; they are ordered party-registry and object-spacing helpers used by nearby movement/update paths.
- `C0:3F1E` is a registry fanout helper used by transition refresh.

The broader family still touches door/transition state through `C0:6A07`, `$5D9A`, and `C0:3FA9`, so the doorway and deferred-script notes remain relevant. The bicycle path is one special traversal mode layered on top of the same registry and transition machinery.

## Working Names

- `C0:3C25` = `Refresh_DestinationContextIfPositionChanged`
- `C0:3C4B` = `Probe_CurrentPositionHighCollisionBits`
- `C0:3C5E` = `Get_OnBicycle`
- `C0:3CFD` = `Restore_LeaderEntityFromBicycleMode`
- `C0:3DAA` = `Sync_CurrentSlotToPartyCharacterRecord`
- `C0:3E25` = `Get_PreviousRegistryTypeCode`
- `C0:3E5A` = `Get_PreviousRegistryObjectOrderByte`
- `C0:3E9D` = `Measure_PreviousRegistryOrderDelta`
- `C0:3EC3` = `Advance_RegistryOrderAndUpdateGapFlag`
- `C0:3F1E` = `Apply_TransitionSnapshotToRegistryEntities`
- `C0:3FA9` = `Refresh_PostTransitionEntityPlacement`
